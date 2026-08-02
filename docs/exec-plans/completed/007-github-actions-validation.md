# Task 7 execution summary: GitHub Actions validation

## Outcome

Added `.github/workflows/docs-check.yml` for documentation-related pull requests
and main-branch pushes. The workflow is validation-only: it does not upload an
artifact, deploy, use a secret, or modify GitHub settings.

The workflow:

- grants only `contents: read`;
- checks out the website with persisted credentials disabled;
- validates `docs-manifest.yml` before network access and derives both source
  repositories and commits from that single lock;
- fetches the exact commits through public HTTPS into detached repositories with
  credential helpers and Git hooks disabled;
- installs the exactly pinned documentation environment with a
  `requirements-docs.txt`-derived cache key;
- runs tests, source-contract validation through the collector, publication
  validation, two assemblies with a complete byte comparison, and
  `mkdocs build --strict`;
- scans the final `site/` artifact for symlinks, files over 5 MiB, credential-like
  content, private endpoints, and local paths;
- uses full reviewed SHA pins for `actions/checkout` v6.0.0 and
  `actions/setup-python` v6.2.0.

README documentation and workflow-policy regression tests were updated to match.

## Verification

Completed locally on 2026-08-02:

- Parsed the workflow successfully using PyYAML's string-preserving loader.
- `python -m pytest`: 12 passed.
- Assembled and validated from both exact local source checkouts twice.
- Compared both generated namespaces and the inventory byte-for-byte.
- `mkdocs build --strict` passed.
- The same final-artifact scan used by CI passed.
- Before/after Git status comparisons confirmed both sources were unchanged.
- `git diff --check` passed.
- Verified the action releases and pins against the actions' official GitHub
  release pages.

## External activation status

After the source pushes, an anonymous fresh-fetch rehearsal verified that DASC
commit `94033eae4d8eac81f4c42c41f6cfba69e1cd2a25` is publicly reachable.

PyDASC still fails at the anonymous Git endpoint before commit resolution with
`could not read Username for 'https://github.com'`. Its locked commit is
`0506b8a9feb75813ae979f0c1c25a307b21096d2`. This normally indicates that the
repository is not currently readable by an unsigned Git client; it is not a
collector or commit-validation failure.

The workflow intentionally does not bypass this condition with credentials or a
moving branch ref. PyDASC must be anonymously Git-readable before the hosted job
can pass. Task 7 did not alter its visibility or credentials, in accordance with
its scope and the upstream read-only rule.
