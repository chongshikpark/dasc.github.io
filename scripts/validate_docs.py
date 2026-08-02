#!/usr/bin/env python3
"""Validate generated documentation against the publication manifest."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from collect_docs import CollectionError, EXPECTED, LINK_RE, load_manifest


def validate(manifest: Path, docs: Path) -> None:
    entries = load_manifest(manifest)
    docs = docs.resolve()
    expected = {e.destination.as_posix(): e for e in entries}
    actual: set[str] = set()
    for namespace in EXPECTED:
        root = docs / namespace
        if root.is_symlink() or not root.is_dir():
            raise CollectionError(f"generated namespace missing or unsafe: {namespace}")
        for path in root.rglob("*"):
            if path.is_symlink():
                raise CollectionError(f"symlink in generated output: {path.relative_to(docs)}")
            if path.is_file():
                actual.add(path.relative_to(docs).as_posix())
    if actual != set(expected):
        raise CollectionError(f"generated file set differs (missing={sorted(set(expected)-actual)}, unexpected={sorted(actual-set(expected))})")
    for relative, entry in expected.items():
        path = docs / relative
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        provenance = f"https://github.com/{entry.repository}/blob/{entry.ref}/{entry.source.as_posix()}"
        if not text.startswith("<!-- Generated from ") or provenance not in text.splitlines()[0]:
            raise CollectionError(f"missing or incorrect attribution: {relative}")
        for match in LINK_RE.finditer(text):
            raw = match.group(2)
            parsed = urlsplit(raw)
            if parsed.scheme in {"http", "https", "mailto"} or raw.startswith("#"):
                continue
            if parsed.scheme or parsed.netloc or raw.startswith("/"):
                raise CollectionError(f"unsafe link in {relative}: {raw}")
            target = (path.parent / unquote(parsed.path)).resolve()
            try:
                target.relative_to(docs)
            except ValueError as exc:
                raise CollectionError(f"link escapes docs in {relative}: {raw}") from exc
            if not target.is_file():
                raise CollectionError(f"broken internal link in {relative}: {raw}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--docs", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        validate(args.manifest, args.docs)
    except (CollectionError, OSError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
