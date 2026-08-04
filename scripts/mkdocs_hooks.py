"""Small deterministic transformations applied to rendered documentation pages."""

from __future__ import annotations

import html
import re
from typing import Any


TABLE = re.compile(r"<table(?:\s[^>]*)?>.*?</table>", re.DOTALL)


def on_page_content(content: str, page: Any, **_: Any) -> str:
    """Wrap tables in named, keyboard-scrollable regions."""

    title = html.escape(str(page.title), quote=True)
    table_number = 0

    def wrap(match: re.Match[str]) -> str:
        nonlocal table_number
        table_number += 1
        label = f"Scrollable table: {title}, table {table_number}"
        return (
            '<div class="dasc-table-scroll" role="region" tabindex="0" '
            f'aria-label="{label}">\n{match.group(0)}\n</div>'
        )

    return TABLE.sub(wrap, content)
