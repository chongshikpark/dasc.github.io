#!/usr/bin/env python3
"""Collect an explicit, immutable allowlist of upstream documentation."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

import yaml

EXPECTED = {
    "pydasc": "chongshikpark/pydasc",
    "dasc": "chongshikpark/dasc",
}
ALLOWED_EXTENSIONS = {".md", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
MAX_FILE_BYTES = 5 * 1024 * 1024
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
LINK_RE = re.compile(r"(!?\[[^\]]*\])\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)")


class CollectionError(ValueError):
    pass


@dataclass(frozen=True)
class Entry:
    source_name: str
    repository: str
    ref: str
    source: PurePosixPath
    destination: PurePosixPath


def _strict_keys(value: object, expected: set[str], context: str) -> dict:
    if not isinstance(value, dict):
        raise CollectionError(f"{context} must be a mapping")
    unknown = set(value) - expected
    missing = expected - set(value)
    if unknown or missing:
        raise CollectionError(f"{context} keys invalid (missing={sorted(missing)}, unknown={sorted(unknown)})")
    return value


def _safe_relative(value: object, label: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\0" in value or "\\" in value:
        raise CollectionError(f"{label} must be a non-empty POSIX path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise CollectionError(f"unsafe {label}: {value!r}")
    if any(char in value for char in "*?["):
        raise CollectionError(f"globs are forbidden in {label}: {value!r}")
    return path


def load_manifest(path: Path) -> list[Entry]:
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        raise CollectionError(f"cannot read manifest: {exc}") from exc
    root = _strict_keys(raw, {"schema_version", "sources"}, "manifest")
    if root["schema_version"] != 1:
        raise CollectionError("unsupported schema_version; expected 1")
    sources = root["sources"]
    if not isinstance(sources, dict) or set(sources) != set(EXPECTED):
        raise CollectionError("sources must contain exactly 'pydasc' and 'dasc'")
    entries: list[Entry] = []
    destinations: set[str] = set()
    for name, expected_repo in EXPECTED.items():
        source = _strict_keys(sources[name], {"repository", "ref", "files"}, f"source {name}")
        if source["repository"] != expected_repo:
            raise CollectionError(f"repository for {name} must be {expected_repo}")
        if not isinstance(source["ref"], str) or not SHA_RE.fullmatch(source["ref"]):
            raise CollectionError(f"ref for {name} must be a lowercase 40-character commit SHA")
        if not isinstance(source["files"], list) or not source["files"]:
            raise CollectionError(f"files for {name} must be a non-empty list")
        for index, item in enumerate(source["files"]):
            item = _strict_keys(item, {"source", "destination"}, f"{name}.files[{index}]")
            src = _safe_relative(item["source"], "source path")
            dest = _safe_relative(item["destination"], "destination path")
            if not dest.parts or dest.parts[0] != name:
                raise CollectionError(f"destination must be below {name}/")
            if src.suffix.lower() not in ALLOWED_EXTENSIONS or dest.suffix.lower() not in ALLOWED_EXTENSIONS:
                raise CollectionError(f"unapproved extension for {src} -> {dest}")
            if src.suffix.lower() != dest.suffix.lower():
                raise CollectionError(f"source and destination extensions differ: {src} -> {dest}")
            folded = dest.as_posix().casefold()
            if folded in destinations:
                raise CollectionError(f"duplicate destination: {dest}")
            destinations.add(folded)
            entries.append(Entry(name, expected_repo, source["ref"], src, dest))
    return entries


def _run_git(args: list[str], cwd: Path | None = None) -> None:
    # Keep administrator-provided transport/proxy configuration, but never allow
    # credential prompts or repository hooks from fetched content.
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
    try:
        subprocess.run(["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd, env=env,
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = exc.stderr.strip() if isinstance(exc, subprocess.CalledProcessError) else str(exc)
        raise CollectionError(f"git operation failed: {detail}") from exc


def _fetch(repository: str, ref: str, target: Path, repo_overrides: dict[str, Path] | None) -> None:
    remote = str(repo_overrides[repository]) if repo_overrides and repository in repo_overrides else f"https://github.com/{repository}.git"
    _run_git(["init", "--quiet", str(target)])
    _run_git(["remote", "add", "origin", remote], target)
    _run_git(["fetch", "--quiet", "--depth=1", "origin", ref], target)
    _run_git(["checkout", "--quiet", "--detach", "FETCH_HEAD"], target)
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=target, check=True, capture_output=True, text=True)
    if result.stdout.strip() != ref:
        raise CollectionError(f"fetched commit does not match requested ref for {repository}")


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _resolve_files(entries: list[Entry], checkouts: dict[str, Path]) -> dict[Entry, Path]:
    resolved: dict[Entry, Path] = {}
    for entry in entries:
        root = checkouts[entry.source_name].resolve()
        candidate = root.joinpath(*entry.source.parts)
        if candidate.is_symlink():
            raise CollectionError(f"symlink source is forbidden: {entry.source}")
        real = candidate.resolve(strict=False)
        if not _inside(real, root):
            raise CollectionError(f"source escapes checkout: {entry.source}")
        try:
            mode = candidate.stat(follow_symlinks=False).st_mode
        except FileNotFoundError as exc:
            raise CollectionError(f"source file is missing: {entry.source}") from exc
        if not stat.S_ISREG(mode):
            raise CollectionError(f"source is not a regular file: {entry.source}")
        if candidate.stat().st_size > MAX_FILE_BYTES:
            raise CollectionError(f"source exceeds {MAX_FILE_BYTES} bytes: {entry.source}")
        resolved[entry] = candidate
    return resolved


def _rewrite_markdown(text: str, entry: Entry, by_source: dict[tuple[str, str], Entry], checkout: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        label, raw = match.groups()
        parsed = urlsplit(raw)
        if parsed.scheme in {"http", "https", "mailto"} or raw.startswith("#"):
            return match.group(0)
        if parsed.scheme or parsed.netloc or raw.startswith("/"):
            raise CollectionError(f"unsafe link {raw!r} in {entry.source}")
        decoded = unquote(parsed.path)
        target = entry.source.parent.joinpath(PurePosixPath(decoded))
        normalized_parts: list[str] = []
        for part in target.parts:
            if part == "..":
                if not normalized_parts:
                    raise CollectionError(f"link escapes repository in {entry.source}: {raw}")
                normalized_parts.pop()
            elif part not in {"", "."}:
                normalized_parts.append(part)
        normalized = PurePosixPath(*normalized_parts).as_posix()
        approved = by_source.get((entry.source_name, normalized))
        if approved is not None:
            relative = os.path.relpath(approved.destination.as_posix(), entry.destination.parent.as_posix()).replace(os.sep, "/")
        else:
            candidate = checkout.joinpath(*PurePosixPath(normalized).parts)
            if candidate.is_symlink() or not candidate.exists() or not _inside(candidate.resolve(), checkout.resolve()):
                raise CollectionError(f"relative link target is missing or unsafe in {entry.source}: {raw}")
            if label.startswith("!"):
                raise CollectionError(f"image target is not allowlisted in {entry.source}: {raw}")
            kind = "tree" if candidate.is_dir() else "blob"
            relative = f"https://github.com/{entry.repository}/{kind}/{entry.ref}/{normalized}"
        suffix = f"?{parsed.query}" if parsed.query else ""
        suffix += f"#{parsed.fragment}" if parsed.fragment else ""
        return f"{label}({relative}{suffix})"

    return LINK_RE.sub(replace, text)


def collect(manifest: Path, output: Path, repo_overrides: dict[str, Path] | None = None) -> None:
    entries = load_manifest(manifest)  # Validate fully before fetching or writing.
    output = output.resolve()
    by_source = {(e.source_name, e.source.as_posix()): e for e in entries}
    with tempfile.TemporaryDirectory(prefix="dasc-docs-") as temp_name:
        temp = Path(temp_name)
        checkouts: dict[str, Path] = {}
        for name in EXPECTED:
            checkout = temp / f"checkout-{name}"
            sample = next(e for e in entries if e.source_name == name)
            _fetch(sample.repository, sample.ref, checkout, repo_overrides)
            checkouts[name] = checkout
        files = _resolve_files(entries, checkouts)
        stage = temp / "stage"
        for entry, source_file in files.items():
            destination = stage.joinpath(*entry.destination.parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            data = source_file.read_bytes()
            if entry.source.suffix.lower() == ".md":
                try:
                    body = data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
                except UnicodeDecodeError as exc:
                    raise CollectionError(f"Markdown is not UTF-8: {entry.source}") from exc
                body = _rewrite_markdown(body, entry, by_source, checkouts[entry.source_name])
                banner = f"<!-- Generated from https://github.com/{entry.repository}/blob/{entry.ref}/{entry.source.as_posix()}; do not edit. -->\n\n"
                data = (banner + body.rstrip() + "\n").encode("utf-8")
            destination.write_bytes(data)
        for name in EXPECTED:
            target = output / name
            if target.is_symlink() or (target.exists() and not target.is_dir()):
                raise CollectionError(f"unsafe generated namespace: {target}")
            if target.exists():
                shutil.rmtree(target)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(stage / name, target)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        collect(args.manifest, args.output)
    except CollectionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
