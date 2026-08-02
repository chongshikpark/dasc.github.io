# Task 8 execution summary: GitHub Pages deployment

## Outcome

Implemented `.github/workflows/deploy-pages.yml` for main-branch pushes and
explicit manual dispatch. No workflow was pushed, dispatched, or executed, and no
GitHub setting, environment, secret, or Pages state was changed.

The build job reproduces Task 7 in the deployment run: it validates the website
lock before network access, fetches exact public source commits without persisted
credentials, validates both source contracts, runs tests, assembles twice,
compares the complete generated output, validates the publication boundary,
builds with strict MkDocs, and scans the complete site. Only that `site/` tree is
uploaded. The dependent deploy job uses the protected `github-pages` environment.

The workflow has exactly the required permissions and concurrency policy:

```yaml
permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false
```

All actions use reviewed immutable SHAs. The Pages actions were updated to their
signed current releases reviewed on 2026-08-02:

- `actions/configure-pages` v6.0.0
  (`45bfe0192ca1faeb007ade9deae92b16b8254a0d`)
- `actions/upload-pages-artifact` v5.0.0
  (`fc324d3547104276b827a68afc52ff2a11cc49c9`)
- `actions/deploy-pages` v5.0.0
  (`cd2ce8fcbc39b97be8ca5fce6e763baed58fa128`)

Pages enablement is explicitly false in the workflow. The manual runbook at
`docs/operations/pages-deployment-checklist.md` covers Pages source selection,
environment and default-branch protection, first-artifact inspection, signed-out
release verification, and rollback. `docs/operations/` is excluded from the
public MkDocs artifact.

## Verification

Completed locally on 2026-08-02:

- `python -m pytest`: 14 passed, including the internal-runbook exclusion check.
- Deployment workflow parsed successfully with the string-preserving YAML loader.
- Policy tests verified exact triggers, permissions, concurrency, job dependency,
  environment, immutable action pins, validation order, and `site/` upload scope.
- Two local assemblies and all publication validators passed.
- Generated namespaces and inventory compared byte-for-byte.
- `mkdocs build --strict` passed.
- Site symlink, size, credential, private-endpoint, and local-path scans passed.
- Both source worktrees remained unchanged.
- `git diff --check` passed.

## External actions remaining

Before the first deployment, an administrator must complete every item in
`docs/operations/pages-deployment-checklist.md`. In particular:

1. Resolve PyDASC anonymous Git access and obtain a passing Task 7 workflow.
2. Approve the complete public artifact.
3. Set Pages source to GitHub Actions.
4. Configure `github-pages` environment and default-branch protections.
5. Inspect the first artifact before environment approval.
6. Verify the deployed site while signed out and record rollback evidence.

Until then, do not push or manually dispatch this deployment workflow.
