# Task 5 execution summary: deterministic source assembly

Status: Completed  
Completed: 2026-08-02

## Outcome

Replaced network collection with deterministic local-checkout assembly. The command validates the website lock and both source publication contracts before writes, pins contract and content commits separately, copies only selected approved regular files, preserves source trees, generates checksummed inventory/provenance, validates output, and supports a strict final site build.

## Commands

```bash
python scripts/collect_docs.py --manifest docs-manifest.yml --output docs \
  --pydasc /path/to/pydasc --dasc /path/to/dasc
python scripts/validate_docs.py --manifest docs-manifest.yml --docs docs
mkdocs build --strict
```

No network access, source installation, hook, workflow, plugin, configuration, or project code execution occurs.

## Locked sources

| Source | Checkout/contract commit | Approved content commit |
| --- | --- | --- |
| PyDASC | `0506b8a9feb75813ae979f0c1c25a307b21096d2` | `dab60df7f8d1cc5f0338fbe1c3885c6624af1a33` |
| DASC | `94033eae4d8eac81f4c42c41f6cfba69e1cd2a25` | `0960f639055c4fe60029175ad603d1f52dc2fc53` |

## Assembled allowlist

- DASC `README.md` → `dasc/index.md` — Unvalidated, MIT.
- PyDASC `README.md` → `pydasc/index.md` — Reviewed, MIT.
- PyDASC `docs/SIMULATION_WORKFLOW.md` → `pydasc/guides/simulation-workflow.md` — Reviewed, MIT.
- PyDASC `docs/PUBLIC_API.md` → `pydasc/reference/public-api.md` — Reference, MIT.
- PyDASC `docs/CONVENTIONS.md` → `pydasc/reference/conventions.md` — Reference, MIT.

Each generated page contains repository, source path, content commit, status, license, and do-not-edit provenance. `docs/generated-inventory.json` records deterministic SHA-256 checksums and is excluded from publication.

## Security and boundary behavior

- Strict unknown-field/schema and exact repository identity validation.
- Exact checkout HEAD and source content-commit byte verification.
- Absolute/traversal/NUL/backslash/glob, symlink, missing/non-regular, unsupported, oversized, duplicate, and case-fold collision rejection.
- Website selections must exactly match source-contract approvals and destinations.
- Relative links are rewritten only in temporary staging; approved links relocate internally and other existing documents become immutable GitHub links.
- Unapproved/missing images and broken/unsafe links fail.
- Credential/private-key, common token, personal-path, and private/local-host patterns fail.
- Generated namespaces are replaced atomically and stale removal is restricted to resolved `docs/pydasc/` and `docs/dasc/`.
- Inventory validator rejects unknown/missing files, checksum changes, symlinks, missing provenance, and broken links.
- Final artifact scan rejects internal plans/contracts, credentials, and personal paths.

## Verification

- Synthetic unit/integration suite: 9 passed.
- Deterministic double assembly: identical inventory.
- Source checkout status and file hashes: unchanged before/after assembly.
- Real local-checkout assembly: passed.
- Inventory/output validation: passed.
- `mkdocs build --strict`: passed without warnings.
- Final artifact contained no execution plans, source publication manifests, generated inventory, credential patterns, or personal absolute paths.
- `git diff --check`: passed.

## Navigation

Removed the superseded Task4 placeholders. Explicit navigation now exposes only approved assembled pages plus hand-written portal pages.

## Deferred work

Notebook execution, generated API transformation, and executable examples remain deferred to Task6. Existing GitHub Actions still use the pre-Task5 CLI and must be updated in Task7/Task8 before CI/deployment use.

## Actions not taken

No source mutation, dependency installation, credential use, push, deployment, or repository-setting change was performed.
