from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).parents[1]
WORKFLOW = ROOT / ".github/workflows/docs-check.yml"
ACTION_PIN = re.compile(r"^\s*uses:\s*[^\s@]+@[0-9a-f]{40}\s+#\s+v\d", re.MULTILINE)


def test_docs_check_workflow_is_valid_and_least_privileged() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    workflow = yaml.load(text, Loader=yaml.BaseLoader)

    assert set(workflow) >= {"name", "on", "permissions", "jobs"}
    assert workflow["permissions"] == {"contents": "read"}
    assert set(workflow["jobs"]) == {"docs"}
    assert "pull_request" in workflow["on"]
    assert "push" in workflow["on"]
    assert "workflow_dispatch" not in workflow["on"]
    assert "deploy" not in text.casefold()


def test_docs_check_pins_actions_and_reproduces_local_build() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    uses_lines = [line for line in text.splitlines() if line.strip().startswith("uses:")]

    assert uses_lines
    assert all(ACTION_PIN.match(line) for line in uses_lines)
    for command in (
        "persist-credentials: false",
        "load_manifest(Path(\"docs-manifest.yml\"))",
        "credential.helper=",
        "core.hooksPath=/dev/null",
        "python -m pytest",
        "scripts/collect_docs.py",
        "scripts/validate_docs.py",
        "diff --recursive --no-dereference",
        "mkdocs build --strict",
    ):
        assert command in text
