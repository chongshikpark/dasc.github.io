# Task 6 execution summary: approved API documentation and examples

## Outcome

Task 6 is complete as a static-publication decision. The reviewed PyDASC and
DASC contracts approve no generated API documentation, notebook publication, or
executable examples, so no execution or rendering mechanism was introduced.

PyDASC's approved `docs/PUBLIC_API.md` remains published as authored reference
material at `docs/pydasc/reference/public-api.md`. DASC remains limited to its
approved README. Links from approved documents to unlisted source material remain
immutable upstream links rather than copied website content.

## Changes

- Added `docs/architecture/api-and-examples-decision.md` to record the release
  boundary, link behavior, and requirements for any future explicit approval.
- Updated `README.md` to explain the static API and executable-content policy.
- Added a regression test requiring the authored PyDASC API policy, rejecting
  notebook/example selections, and preventing notebook or API-generation tools
  from entering the pinned documentation environment unnoticed.

No source repository was modified. No publication-manifest or website allowlist
entry was added or removed.

## Verification

Completed on 2026-08-02 using the pinned repository virtual environment:

- `python -m pytest`: 10 passed.
- Source assembly completed twice from PyDASC
  `0506b8a9feb75813ae979f0c1c25a307b21096d2` and DASC
  `94033eae4d8eac81f4c42c41f6cfba69e1cd2a25`.
- The two generated inventories compared byte-for-byte equal.
- `scripts/validate_docs.py` passed.
- `mkdocs build --strict` passed.
- Before/after Git status comparisons confirmed both source checkouts were
  unchanged.
- The five-file inventory contains the authored API policy, full commit and
  checksum provenance, and no notebook or examples-tree input.
- Symlink, credential-pattern, oversized-file, and whitespace-error scans passed.

The first strict-build attempt used a shell without `mkdocs` on `PATH`; rerunning
with `./.venv/bin/mkdocs` completed successfully. A subsequent audit-script field
name typo was corrected to match the inventory's documented `commit` and
`repository` keys; the corrected audit passed.
