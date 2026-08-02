from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).parents[1] / "scripts"))
from collect_docs import CollectionError, MAX_FILE_BYTES, collect, load_manifest  # noqa: E402
from validate_docs import validate  # noqa: E402


SHA = "a" * 40


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()


def make_repo(tmp_path: Path, name: str, files: dict[str, bytes | str]) -> tuple[Path, str]:
    repo = tmp_path / name
    repo.mkdir()
    git(repo, "init", "--quiet")
    git(repo, "config", "user.email", "tests@example.invalid")
    git(repo, "config", "user.name", "Tests")
    for relative, content in files.items():
        path = repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content if isinstance(content, bytes) else content.encode())
    git(repo, "add", ".")
    git(repo, "commit", "--quiet", "-m", "fixture")
    return repo, git(repo, "rev-parse", "HEAD")


def manifest_data(pydasc_sha: str = SHA, dasc_sha: str = SHA) -> dict:
    return {"schema_version": 1, "sources": {
        "pydasc": {"repository": "chongshikpark/pydasc", "ref": pydasc_sha, "files": [{"source": "README.md", "destination": "pydasc/index.md"}]},
        "dasc": {"repository": "chongshikpark/dasc", "ref": dasc_sha, "files": [{"source": "README.md", "destination": "dasc/index.md"}]},
    }}


def write_manifest(tmp_path: Path, data: dict) -> Path:
    path = tmp_path / "manifest.yml"
    path.write_text(yaml.safe_dump(data, sort_keys=False))
    return path


def fixture(tmp_path: Path, pydasc_text: str = "# PyDASC\n", dasc_text: str = "# DASC\n"):
    p_repo, p_sha = make_repo(tmp_path, "pydasc-repo", {"README.md": pydasc_text})
    d_repo, d_sha = make_repo(tmp_path, "dasc-repo", {"README.md": dasc_text})
    manifest = write_manifest(tmp_path, manifest_data(p_sha, d_sha))
    overrides = {"chongshikpark/pydasc": p_repo, "chongshikpark/dasc": d_repo}
    return manifest, overrides


def test_valid_deterministic_collection_attribution_and_stale_removal(tmp_path):
    manifest, overrides = fixture(tmp_path)
    output = tmp_path / "docs"
    (output / "pydasc").mkdir(parents=True)
    (output / "pydasc" / "stale.md").write_text("stale")
    collect(manifest, output, overrides)
    first = {p.relative_to(output): hashlib.sha256(p.read_bytes()).hexdigest() for p in output.rglob("*") if p.is_file()}
    collect(manifest, output, overrides)
    second = {p.relative_to(output): hashlib.sha256(p.read_bytes()).hexdigest() for p in output.rglob("*") if p.is_file()}
    assert first == second
    assert not (output / "pydasc/stale.md").exists()
    assert "Generated from https://github.com/chongshikpark/pydasc/blob/" in (output / "pydasc/index.md").read_text()
    validate(manifest, output)


@pytest.mark.parametrize("mutation", [
    lambda d: d.update(schema_version=2),
    lambda d: d.update(extra=True),
    lambda d: d["sources"]["pydasc"].update(repository="evil/repo"),
    lambda d: d["sources"]["pydasc"].update(ref="main"),
    lambda d: d["sources"]["pydasc"].update(extra=True),
    lambda d: d["sources"]["pydasc"]["files"][0].update(extra=True),
])
def test_manifest_structure_rejected(tmp_path, mutation):
    data = manifest_data()
    mutation(data)
    with pytest.raises(CollectionError):
        load_manifest(write_manifest(tmp_path, data))


@pytest.mark.parametrize(("field", "value"), [
    ("source", "/README.md"), ("destination", "/pydasc/index.md"),
    ("source", "../README.md"), ("destination", "pydasc/../index.md"),
    ("source", "*.md"), ("source", "secret.env"),
    ("destination", "dasc/index.md"),
])
def test_unsafe_paths_and_extensions_rejected(tmp_path, field, value):
    data = manifest_data()
    data["sources"]["pydasc"]["files"][0][field] = value
    with pytest.raises(CollectionError):
        load_manifest(write_manifest(tmp_path, data))


def test_duplicate_casefold_destination_rejected(tmp_path):
    data = manifest_data()
    data["sources"]["pydasc"]["files"].append({"source": "OTHER.md", "destination": "pydasc/INDEX.md"})
    with pytest.raises(CollectionError, match="duplicate"):
        load_manifest(write_manifest(tmp_path, data))


@pytest.mark.parametrize("kind", ["missing", "directory", "symlink"])
def test_invalid_source_types_rejected(tmp_path, kind):
    manifest, overrides = fixture(tmp_path)
    repo = overrides["chongshikpark/pydasc"]
    if kind == "missing":
        (repo / "README.md").unlink()
    elif kind == "directory":
        (repo / "README.md").unlink(); (repo / "README.md").mkdir()
    else:
        (repo / "README.md").unlink(); (repo / "README.md").symlink_to("/etc/passwd")
    git(repo, "add", "-A"); git(repo, "commit", "--quiet", "-m", kind)
    data = yaml.safe_load(manifest.read_text()); data["sources"]["pydasc"]["ref"] = git(repo, "rev-parse", "HEAD"); write_manifest(tmp_path, data)
    with pytest.raises(CollectionError):
        collect(manifest, tmp_path / "docs", overrides)


def test_oversized_file_rejected(tmp_path):
    manifest, overrides = fixture(tmp_path)
    repo = overrides["chongshikpark/pydasc"]
    (repo / "README.md").write_bytes(b"x" * (MAX_FILE_BYTES + 1))
    git(repo, "add", "."); git(repo, "commit", "--quiet", "-m", "large")
    data = yaml.safe_load(manifest.read_text()); data["sources"]["pydasc"]["ref"] = git(repo, "rev-parse", "HEAD"); write_manifest(tmp_path, data)
    with pytest.raises(CollectionError, match="exceeds"):
        collect(manifest, tmp_path / "docs", overrides)


def test_relative_link_and_image_rewriting(tmp_path):
    p_repo, p_sha = make_repo(tmp_path, "p", {"README.md": "[Guide](guide.md) ![Plot](img/plot.png)\n", "guide.md": "# Guide\n", "img/plot.png": b"png"})
    d_repo, d_sha = make_repo(tmp_path, "d", {"README.md": "# DASC\n"})
    data = manifest_data(p_sha, d_sha)
    data["sources"]["pydasc"]["files"] += [{"source": "guide.md", "destination": "pydasc/guides/guide.md"}, {"source": "img/plot.png", "destination": "pydasc/assets/plot.png"}]
    manifest = write_manifest(tmp_path, data)
    collect(manifest, tmp_path / "docs", {"chongshikpark/pydasc": p_repo, "chongshikpark/dasc": d_repo})
    text = (tmp_path / "docs/pydasc/index.md").read_text()
    assert "[Guide](guides/guide.md)" in text and "![Plot](assets/plot.png)" in text
    validate(manifest, tmp_path / "docs")


def test_missing_relative_link_rejected(tmp_path):
    manifest, overrides = fixture(tmp_path, "[missing](missing.md)\n")
    with pytest.raises(CollectionError, match="missing or unsafe"):
        collect(manifest, tmp_path / "docs", overrides)


def test_unallowlisted_existing_document_rewritten_to_pinned_upstream(tmp_path):
    p_repo, p_sha = make_repo(tmp_path, "p", {"README.md": "[Note](notes/note.md)\n", "notes/note.md": "private staging note"})
    d_repo, d_sha = make_repo(tmp_path, "d", {"README.md": "# DASC\n"})
    manifest = write_manifest(tmp_path, manifest_data(p_sha, d_sha))
    collect(manifest, tmp_path / "docs", {"chongshikpark/pydasc": p_repo, "chongshikpark/dasc": d_repo})
    text = (tmp_path / "docs/pydasc/index.md").read_text()
    assert f"https://github.com/chongshikpark/pydasc/blob/{p_sha}/notes/note.md" in text
    assert not (tmp_path / "docs/pydasc/notes/note.md").exists()


def test_validator_rejects_broken_link_and_unexpected_file(tmp_path):
    manifest, overrides = fixture(tmp_path)
    output = tmp_path / "docs"; collect(manifest, output, overrides)
    (output / "pydasc/index.md").write_text((output / "pydasc/index.md").read_text() + "\n[bad](missing.md)\n")
    with pytest.raises(CollectionError, match="broken"):
        validate(manifest, output)
    collect(manifest, output, overrides); (output / "dasc/unexpected.md").write_text("no")
    with pytest.raises(CollectionError, match="unexpected"):
        validate(manifest, output)


def test_output_namespace_symlink_rejected(tmp_path):
    manifest, overrides = fixture(tmp_path)
    output = tmp_path / "docs"; output.mkdir(); (output / "pydasc").symlink_to(tmp_path)
    with pytest.raises(CollectionError, match="unsafe generated"):
        collect(manifest, output, overrides)
