#!/usr/bin/env python3
"""Apply deterministic semantic-accessibility checks to built HTML pages."""

from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path


class PageAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.headings: list[int] = []
        self.h1_count = 0
        self.images_without_alt = 0
        self.tables = 0
        self.table_headers = 0
        self.in_table = 0
        self.has_main = False
        self.has_title = False
        self.has_lang = False
        self.named_navs = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        identifier = values.get("id")
        if identifier:
            if identifier in self.ids:
                self.duplicate_ids.add(identifier)
            self.ids.add(identifier)
        if tag == "html" and values.get("lang"):
            self.has_lang = True
        elif tag == "title":
            self.has_title = True
        elif tag == "main":
            self.has_main = True
        elif tag == "nav" and (values.get("aria-label") or values.get("aria-labelledby")):
            self.named_navs += 1
        elif tag == "img" and "alt" not in values:
            self.images_without_alt += 1
        elif tag == "table":
            self.tables += 1
            self.in_table += 1
        elif tag == "th" and self.in_table:
            self.table_headers += 1
        elif len(tag) == 2 and tag[0] == "h" and tag[1].isdigit():
            level = int(tag[1])
            self.headings.append(level)
            self.h1_count += level == 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "table":
            self.in_table -= 1


def validate(site: Path) -> None:
    site = site.resolve(strict=True)
    pages = sorted(site.rglob("*.html"))
    if not pages:
        raise ValueError("site contains no HTML pages")
    for page in pages:
        audit = PageAudit()
        audit.feed(page.read_text(encoding="utf-8"))
        relative = page.relative_to(site)
        failures: list[str] = []
        if not audit.has_lang:
            failures.append("missing document language")
        if not audit.has_title:
            failures.append("missing title")
        if not audit.has_main:
            failures.append("missing main landmark")
        if audit.h1_count != 1:
            failures.append(f"expected one h1, found {audit.h1_count}")
        if any(current > previous + 1 for previous, current in zip(audit.headings, audit.headings[1:])):
            failures.append("heading level is skipped")
        if audit.images_without_alt:
            failures.append(f"{audit.images_without_alt} image(s) lack alt attributes")
        if audit.tables and not audit.table_headers:
            failures.append("table markup has no header cells")
        if audit.duplicate_ids:
            failures.append(f"duplicate ids: {sorted(audit.duplicate_ids)}")
        if not audit.named_navs:
            failures.append("navigation landmarks lack accessible names")
        if failures:
            raise ValueError(f"{relative}: {'; '.join(failures)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    args = parser.parse_args()
    try:
        validate(args.site)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
