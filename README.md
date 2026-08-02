# DASC Documentation Website

This repository builds the public documentation portal for DASC and PyDASC with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). It provides a single Read-the-Docs-like interface while the project documentation remains authored in its respective source repository.

- Website repository: `https://github.com/chongshikpark/dasc.github.io`
- Published website: `https://chongshikpark.github.io/dasc.github.io/`
- PyDASC source: `https://github.com/chongshikpark/pydasc`
- DASC source: `https://github.com/chongshikpark/dasc`

> GitHub Pages project sites use `https://<owner>.github.io/<repository>/`. Because this repository is named `dasc.github.io` rather than `chongshikpark.github.io`, the canonical Pages URL includes `/dasc.github.io/`.

## Design

The portal contains hand-written landing and project-selection pages plus a reviewed subset of public documentation imported from `pydasc` and `dasc`. The build has four stages:

1. Read `docs-manifest.yml`, the sole allowlist of publishable upstream files.
2. Fetch the exact reviewed commit of each source repository into temporary storage.
3. Copy and, where necessary, safely rewrite the selected documents into `docs/pydasc/` and `docs/dasc/`.
4. Build the static site with MkDocs and deploy its `site/` artifact through GitHub Pages.

No upstream repository is mounted as a writable dependency, no upstream code is executed, and no unlisted file is published.

## Repository layout

```text
.
├── .github/workflows/docs-check.yml
├── .github/workflows/deploy-pages.yml
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   ├── pydasc/                 # generated from allowlisted PyDASC docs
│   ├── dasc/                   # generated from allowlisted DASC docs
│   ├── assets/
│   └── overrides/
├── scripts/collect_docs.py
├── scripts/validate_docs.py
├── tests/
├── docs-manifest.yml
├── mkdocs.yml
├── requirements-docs.txt
├── AGENTS.md
└── README.md
```

## Publication manifest

Only entries in `docs-manifest.yml` may cross the public-site boundary. Production refs are full commit SHAs so a build is reproducible and cannot silently ingest newly pushed content.

```yaml
schema_version: 1
sources:
  pydasc:
    repository: chongshikpark/pydasc
    ref: "<40-character commit SHA>"
    files:
      - source: README.md
        destination: pydasc/index.md
  dasc:
    repository: chongshikpark/dasc
    ref: "<40-character commit SHA>"
    files:
      - source: README.md
        destination: dasc/index.md
```

Adding a manifest entry is a publication decision. Confirm that the file is intentionally public, properly licensed, free of secrets and private links, and suitable for the portal. Wildcards and directory-wide copying are intentionally unsupported.

The generated `docs/pydasc/` and `docs/dasc/` directories are intentionally ignored by Git and created in CI. The collector first validates the complete manifest, fetches only its exact commits, verifies path containment and file types, and then replaces only those two generated namespaces from a temporary staging tree. Repeated runs are covered by a byte-for-byte determinism test.

Relative links to allowlisted files are relocated within the portal. Links to existing but unlisted upstream documents are rewritten to immutable GitHub URLs at the same commit; missing or unsafe targets fail collection. Images must be explicitly allowlisted, and arbitrary remote content is never downloaded.

## MkDocs configuration

The implementation should use this baseline:

```yaml
site_name: DASC Documentation
site_description: Documentation for DASC and PyDASC
site_url: https://chongshikpark.github.io/dasc.github.io/
repo_name: chongshikpark/dasc.github.io
repo_url: https://github.com/chongshikpark/dasc.github.io
edit_uri: edit/main/docs/
docs_dir: docs
site_dir: site

theme:
  name: material
  language: en
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - navigation.tracking
    - search.highlight
    - search.share
    - search.suggest
    - content.code.copy

plugins:
  - search

markdown_extensions:
  - admonition
  - attr_list
  - footnotes
  - md_in_html
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.superfences
  - toc:
      permalink: true

nav:
  - Home: index.md
  - Getting started: getting-started.md
  - PyDASC:
      - Overview: pydasc/index.md
  - DASC:
      - Overview: dasc/index.md
```

Expand `nav` explicitly as documents are approved. Material for MkDocs and all plugins must be version-pinned in `requirements-docs.txt`.

### Presentation

The portal uses a repository-owned, classic documentation theme adaptation in
`docs/stylesheets/readthedocs.css`. It retains Material for MkDocs behavior while
providing a fixed 300 px desktop navigation rail, bounded reading column,
breadcrumb trail, responsive drawer, print rules, and reduced-motion support.
The implementation uses local/system font fallbacks and does not download fonts,
styles, branding, advertising, analytics, or assets from Read the Docs or another
documentation project.

After building, validate subpath-safe links and presentation assets with:

```bash
python scripts/validate_site.py --site site \
  --css docs/stylesheets/readthedocs.css
```

## Local preview

Python 3.11 or newer and Git are recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --requirement requirements-docs.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/`. This builds the hand-written scaffold only and does not fetch either source repository. For its strict check, run:

```bash
mkdocs build --strict
```

After the deterministic source-assembly task is reviewed, the complete local sequence is:

```bash
python -m pytest
python scripts/collect_docs.py --manifest docs-manifest.yml --output docs \
  --pydasc /path/to/pydasc --dasc /path/to/dasc
python scripts/validate_docs.py --manifest docs-manifest.yml --docs docs
mkdocs build --strict
```

The two source paths must be local checkouts whose `HEAD` commits exactly match `docs-manifest.yml`. Assembly validates each checkout's `docs/publication-manifest.json`, reads approved Git objects and regular files only, never installs or executes source code, and writes a checksummed `docs/generated-inventory.json` excluded from the public site.

## API documentation and executable content

The current release is static. PyDASC's allowlisted `docs/PUBLIC_API.md` is an
authored public-interface policy page, not generated API output. Neither reviewed
source contract approves generated API documentation, notebooks, or executable
examples, so the website does not install either source package or provide a
notebook/API execution pipeline.

Links from approved pages to unlisted upstream notebooks or examples are rewritten
to immutable GitHub URLs at the reviewed commit. Those targets are not copied,
rendered, executed, or included in the publication inventory. See the internal
decision record in `docs/architecture/api-and-examples-decision.md` for the
requirements that a future, explicitly reviewed approval must satisfy.

## Updating imported documentation

1. Choose a reviewed commit from `chongshikpark/pydasc` or `chongshikpark/dasc`.
2. Audit each proposed source file for public suitability and licensing.
3. Update the source `ref` and explicit file entries in `docs-manifest.yml`.
4. Run collection, validation, tests, and the strict MkDocs build.
5. Inspect the rendered navigation, links, images, code blocks, attribution, and mobile layout.
6. Submit the manifest change and any necessary portal changes for review.

Do not hand-edit generated copies. Fix content upstream or adjust the reviewed collection/transformation rules.

## Continuous integration and deployment

`docs-check.yml` runs for documentation-related pull requests and main-branch
pushes with `contents: read` permission. It checks out the website without
persisting credentials, reads the exact source locks from `docs-manifest.yml`,
fetches those commits through public HTTPS into detached temporary worktrees, and
never executes source-repository configuration or code. It runs the same tests,
collector, validator, and strict MkDocs build used locally, repeats collection and
compares the complete generated tree byte-for-byte, and scans the built `site/`
artifact for symlinks, oversized files, credentials, and private or local paths.
Its dependency cache is keyed by `requirements-docs.txt`; it neither uploads nor
deploys an artifact.

`deploy-pages.yml` runs on pushes to `main` and by manual dispatch. It should:

- check out `chongshikpark/dasc.github.io`;
- configure Python and install `requirements-docs.txt`;
- collect sources at the manifest's immutable commit SHAs;
- validate the staged documentation and run tests;
- build with `mkdocs build --strict`;
- upload `site/` with the official Pages artifact action;
- deploy with the official Pages deployment action in the `github-pages` environment.

Use these workflow permissions and concurrency controls:

```yaml
permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false
```

Pin every action to a reviewed commit SHA. Configure the repository's **Settings → Pages → Build and deployment → Source** to **GitHub Actions**. The workflow must not commit the built `site/` directory or use a `gh-pages` branch.

The repository workflow keeps Pages enablement disabled and cannot perform the
required administrative review. Before the first deployment, follow
`docs/operations/pages-deployment-checklist.md` to configure environment and
branch protection, inspect the first artifact, verify the site while signed out,
and rehearse the reviewed rollback procedure. Do not push or manually dispatch
the deployment workflow until that release is explicitly authorized.

## Security model

- The manifest is an allowlist, not a discovery mechanism.
- Production inputs are immutable commit SHAs.
- Source and destination paths are resolved and checked for containment.
- Symlinks, path traversal, absolute paths, duplicate destinations, and unsupported file types fail the build.
- Imported repositories are data only; their scripts, actions, plugins, and configuration are never executed.
- Deployment uses GitHub's short-lived OIDC credentials and minimal permissions.
- A strict build, link checks, and tests must pass before upload.

See [AGENTS.md](AGENTS.md) for contributor and automation rules and [docs/codex_tasks.md](docs/codex_tasks.md) for the sequential implementation tasks.

## License and attribution

The website's own license should be declared in this repository. Imported files retain their upstream copyright and license terms. Each generated document should identify its source repository, source path, and exact commit. Do not assume that public visibility alone grants republication rights.
