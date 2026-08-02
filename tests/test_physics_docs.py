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


def test_tgf_derivation_is_explicitly_navigated() -> None:
    config = (ROOT / "mkdocs.yml").read_text()
    for page in (
        "dasc-tgf-free-space-poisson.md",
        "dasc-tgf-formulation.md",
        "dasc-tgf-field-kick.md",
        "dasc-tgf-verification.md",
    ):
        assert page in config

    equations = "\n".join(
        (ROOT / "docs" / page).read_text()
        for page in (
            "dasc-tgf-free-space-poisson.md",
            "dasc-tgf-formulation.md",
            "dasc-tgf-field-kick.md",
            "dasc-tgf-verification.md",
        )
    )
    for equation_id in (
        "eq-tgf-poisson",
        "eq-tgf-green-convolution",
        "eq-tgf-cutoff-condition",
        "eq-tgf-spectrum",
        "eq-tgf-direct-field",
        "eq-tgf-discrete-energy",
        "eq-tgf-energy-force",
        "eq-tgf-kick",
        "eq-tgf-relative-l2",
    ):
        assert f'id="{equation_id}"' in equations
