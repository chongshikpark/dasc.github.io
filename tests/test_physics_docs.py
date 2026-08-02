from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_physics_docs import validate


def test_authored_physics_docs_have_valid_equations_and_citations() -> None:
    validate(ROOT / "docs")


def test_undefined_equation_and_citation_keys_fail(tmp_path: Path) -> None:
    page = tmp_path / "dasc-test.md"
    page.write_text("# Test\n\n[missing](#eq-missing) and citation[^missing].\n")
    with pytest.raises(ValueError):
        validate(tmp_path)
