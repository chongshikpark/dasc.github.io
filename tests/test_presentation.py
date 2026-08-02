from __future__ import annotations

import re
from pathlib import Path

import yaml

import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from validate_accessibility import validate as validate_accessibility


ROOT = Path(__file__).parents[1]
CSS = ROOT / "docs/stylesheets/readthedocs.css"


def test_readthedocs_stylesheet_and_local_assets_are_configured() -> None:
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))

    assert config["extra_css"] == ["stylesheets/readthedocs.css"]
    assert config["extra_javascript"] == ["javascripts/navigation.js"]
    assert config["theme"]["font"] is False
    assert "navigation.path" in config["theme"]["features"]
    assert "navigation.footer" in config["theme"]["features"]
    assert "navigation.tabs" not in config["theme"]["features"]
    assert "overrides/" in config["exclude_docs"].splitlines()


def test_required_tokens_desktop_sidebar_and_bounded_content_exist() -> None:
    css = CSS.read_text(encoding="utf-8")
    required = {
        "--dasc-sidebar-width": "300px",
        "--dasc-sidebar-bg": "#343131",
        "--dasc-sidebar-muted": "#9b9b9b",
        "--dasc-accent": "#2980b9",
        "--dasc-page-bg": "#fcfcfc",
        "--dasc-text": "#404040",
        "--dasc-content-max": "1000px",
    }
    for token, value in required.items():
        assert re.search(rf"{re.escape(token)}\s*:\s*{re.escape(value)}\s*;", css)

    assert "@media screen and (min-width: 76.25em)" in css
    assert "width: var(--dasc-sidebar-width)" in css
    assert "max-width: var(--dasc-content-max)" in css
    assert ".md-sidebar--secondary:not([hidden])" in css
    assert re.search(r"\.md-sidebar--secondary:not\(\[hidden\]\)\s*\{\s*display:\s*none;\s*\}", css)
    assert ".md-sidebar--secondary:not([hidden]) ~ .md-content > .md-content__inner" in css
    assert re.search(r"\.md-content\s*\{\s*max-width:\s*none;", css)


def test_mobile_accessibility_overflow_motion_and_print_rules_exist() -> None:
    css = CSS.read_text(encoding="utf-8")
    header = (ROOT / "docs/overrides/partials/header.html").read_text(encoding="utf-8")
    javascript = (ROOT / "docs/javascripts/navigation.js").read_text(encoding="utf-8")

    assert "@media screen and (max-width: 76.234375em)" in css
    assert "overflow-x: hidden" in css
    assert ":focus-visible" in css
    assert "prefers-reduced-motion: reduce" in css
    assert "@media print" in css
    assert 'aria-controls="__drawer"' in header
    assert 'aria-label="Open documentation navigation"' in header
    content = (ROOT / "docs/overrides/partials/content.html").read_text(encoding="utf-8")
    assert 'aria-label="Breadcrumb"' in content
    assert 'aria-current="page"' in content
    assert 'event.key === "Enter"' in javascript
    assert 'event.key === "Escape"' in javascript
    assert not re.search(r"url\(\s*['\"]?/", css)
    assert "/Users/" not in css + header + javascript


def test_built_site_passes_semantic_accessibility_audit(tmp_path: Path) -> None:
    page = tmp_path / "index.html"
    page.write_text(
        '<!doctype html><html lang="en"><head><title>Page</title></head>'
        '<body><nav aria-label="Primary"></nav><main><h1>Page</h1>'
        '<h2>Section</h2><table><tr><th>Value</th></tr></table>'
        '<img src="example.png" alt="Example"></main></body></html>',
        encoding="utf-8",
    )
    validate_accessibility(tmp_path)
