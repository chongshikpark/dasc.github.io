# Execution summary: Read the Docs-inspired visual style

## Outcome

Implemented an original, locally owned classic documentation presentation on top
of Material for MkDocs. No manifest, allowlist, source lock, scientific content,
repository identity, dependency, deployment permission, or deployment trigger was
changed.

The design uses a fixed 300 px charcoal navigation rail and blue project/search
block above the `76.25em` desktop breakpoint. Below it, Material's drawer and
compact header remain in use. At `30em` and below, tables become independently
scrollable and content padding contracts further. A white 800 px reading surface
sits on an off-white page background.

Local/system font fallbacks replace external font requests. Lato-compatible sans
serifs are used for body text, Roboto Slab/Rockwell/Georgia fallbacks for headings,
and system monospace fonts for code. Breadcrumbs, heading permalinks, repository
source access, copy controls, previous/next navigation, tables, admonitions, code,
equation containers, footer, print, forced-colors, reduced-motion, and focus states
have explicit styles.

The requested `#2980b9` accent remains a token and non-text accent. Text-bearing
blue surfaces use the nearby `#246f9f`, and links use `#1f6f9f`, because both meet
WCAG AA normal-text contrast against their backgrounds whereas white on `#2980b9`
is approximately 4.3:1.

## Files

- Added `docs/stylesheets/readthedocs.css`.
- Added `docs/javascripts/navigation.js` for Enter/Space activation, Escape close,
  focus return, and synchronized accessible drawer state.
- Added narrow Material overrides for the accessible header control and semantic
  breadcrumb trail.
- Removed the superseded `docs/assets/stylesheets/extra.css` after preserving its
  status and focus styling in the new stylesheet.
- Updated `mkdocs.yml` for local assets, system fonts, breadcrumbs, previous/next
  navigation, and exclusion of template/task sources from the public artifact.
- Added `scripts/validate_site.py` and presentation regression tests.
- Added the post-build validator to both existing workflows.
- Updated `README.md` with the presentation and validation contract.

## Verification

- 17 pytest tests passed.
- Source assembly and publication validation passed before presentation review.
- `mkdocs build --strict` passed without warnings.
- The built-site validator passed all local links/assets, canonical project-base
  references, stylesheet tokens, personal-path checks, and accessible drawer
  markers.
- Confirmed template sources, task briefs, architecture records, execution plans,
  and operations records are absent from `site/`.
- Generated markup contains breadcrumbs, previous/next controls, heading
  permalinks, repository source access, and the local CSS/JavaScript assets.
- CSS and generated markup were reviewed structurally for the 1280 px desktop
  mode and 1024 px, 768 px, and 390 px drawer modes.
- Keyboard behavior, focus styling, contrast values, reduced-motion,
  forced-colors, print, narrow tables/code/equations/images, and 200%-zoom
  breakpoint behavior were checked in source and automated assertions.
- `git diff --check` passed.

## Visual-review limitation

No controllable browser was available in this session. Consequently, the ImpactX
reference and local pages could not be screenshot-compared or interactively tested
at the requested viewports. Home, the long simulation workflow, the nested public
API reference, code blocks, tables, and the home-page admonition were covered by
generated-markup and CSS checks, not rendered visual inspection. No published page
currently contains an equation, so equation styling is defensive only.

A browser-based pass remains required to confirm actual 1280/1024/768/390 px
rendering, drawer interaction, keyboard traversal, 200% zoom, and print preview.
The site intentionally differs from ImpactX by retaining Material's search engine,
icons, copy controls, footer attribution, and mobile drawer implementation, and by
omitting Read the Docs branding, version selection, advertising, analytics, fonts,
and project assets.
