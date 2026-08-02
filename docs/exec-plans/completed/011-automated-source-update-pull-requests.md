# Task 10 execution summary: automated source-update pull requests

## Outcome

Added a weekly and manually dispatchable source-lock updater. It proposes
reviewable pull requests and never merges or deploys them.

The updater uses public, credential-disabled clones of the two fixed repository
identities. Candidate default-branch heads and the exact older content commits
declared by their publication manifests are fetched shallowly. The helper then
validates the current website manifest, candidate Git identities, strict source
contract schemas, publication decisions, approved files and destinations,
documentation statuses, licenses, and committed source bytes before writing
only candidate `checkout_commit` values.

If locks changed, the workflow runs the full release gate: tests, collection,
publication validation, byte-for-byte repeat assembly, strict MkDocs build,
site-link and presentation validation, semantic accessibility validation, and
the complete artifact security scan. A stable open-proposal check prevents
parallel duplicate updates. A new run-specific branch avoids rewriting an old
branch. The pull-request body explicitly requires review as a public release.

## Security and permissions

The workflow grants only `contents: write` and `pull-requests: write`, which are
required to push its proposal branch and open the pull request. Its two actions
use the same reviewed immutable pins as the validation workflows. Upstream
repositories remain read-only public inputs; no upstream configuration or code
is executed, no moving ref enters production, and no allowlist entry is inferred.

The workflow does not enable auto-merge, approve its own pull request, modify
Pages, use a deployment credential, or trigger deployment. If a candidate
contract or artifact fails any check, it fails closed without a branch or PR.

## Verification

- 20 tests passed, including candidate-only lock replacement and workflow-policy
  assertions.
- A live rehearsal anonymously cloned both current upstream default branches.
- The rehearsal fetched the exact content commits declared by both candidate
  publication manifests and validated both complete contracts.
- Both current heads equal the existing reviewed checkout locks, so a production
  run today would correctly make no change and open no pull request.
- The complete repository collection, strict build, site validation,
  accessibility validation, and artifact scan passed after implementation.

## Administrative activation

GitHub must allow Actions to create pull requests in repository workflow
settings. That setting and the first manual dispatch are administrator actions;
this implementation does not change either. Automated proposals must retain
normal branch protection and human review requirements.
