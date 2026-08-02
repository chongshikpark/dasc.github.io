# API documentation and executable-content decision

## Decision

The current website release publishes authored, allowlisted Markdown only. It
does not generate API reference material, copy or render notebooks, or execute
examples from either source repository.

PyDASC's reviewed publication contract approves `docs/PUBLIC_API.md`. This file
is an authored description of the supported public interface and is assembled as
`docs/pydasc/reference/public-api.md`; it is not generated API output. The
contract explicitly excludes generated API documentation and notebooks from its
schema-version-1 release.

DASC's reviewed publication contract approves only its top-level `README.md` and
explicitly excludes notebooks, executable examples, and generated or manuscript
content.

## Link behavior

An approved Markdown page may link to an existing, unlisted notebook or example
in its source repository. The collector rewrites such a link to an immutable
GitHub URL at the reviewed source commit. The target is not copied, rendered, or
executed, and is not part of the website's publication inventory.

## Deferred approval requirements

Generated API documentation can be considered only after a source contract
explicitly identifies the approved inputs and outputs, generator and fully pinned
environment, stable public symbols, provenance format, and deterministic static
rendering procedure.

A notebook or executable example can be considered only after it is individually
allowlisted with a public-release status, license and attribution evidence,
scientific validation status, execution policy, pinned isolated environment,
resource limits, deterministic outputs, and checks rejecting credentials, local
paths, private endpoints, development data, and oversized artifacts.

Any such approval requires an explicit `docs-manifest.yml` review. Directory
discovery, wildcard inclusion, and executing upstream code remain prohibited.

## Verification boundary

Task 6 verifies that:

- `docs/PUBLIC_API.md` remains an explicit PyDASC selection;
- no selected source has a notebook extension or resides in an examples or
  notebooks tree;
- the documentation environment contains no notebook or API-generation tool;
- collection is deterministic and leaves both source checkouts unchanged;
- provenance, links, assets, checksums, publication-boundary validation, and the
  strict MkDocs build pass.
