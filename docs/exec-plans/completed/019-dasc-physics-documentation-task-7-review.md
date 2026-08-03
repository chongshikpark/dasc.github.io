# Task 7 review: complete DASC physics section

## Review disposition

**Conditional; not release-clean.** No critical model-boundary, sign, causality,
or false-validation defect was found. Two high-severity rendered-content issues,
two medium documentation/provenance issues, one low-severity stale-workflow issue,
and one high-priority manual-test gap remain.

This was a review-only task. No disputed physics or reported defect was silently
repaired. No source lock, imported file, manifest, deployment setting, or
publication status changed.

## Severity-ranked findings

### High — DASC-REV-001: wide tables can be clipped on mobile and at high zoom

- **Pages/URLs:**
  - `docs/dasc-method-selection.md`,
    `https://chongshikpark.github.io/dasc.github.io/dasc-method-selection/`
  - `docs/dasc-validation-matrix.md`,
    `https://chongshikpark.github.io/dasc.github.io/dasc-validation-matrix/`
  - `docs/dasc-reproducibility.md`,
    `https://chongshikpark.github.io/dasc.github.io/dasc-reproducibility/`
  - also every other DASC Markdown table.
- **Evidence:** generated tables are bare `<table>` elements, not children of
  `.md-typeset__table`. At `docs/stylesheets/readthedocs.css:547`, horizontal
  overflow is assigned only to `.md-typeset__table`; at lines 554–557 bare
  tables become `width: max-content`. The page containers suppress horizontal
  overflow, so the widest columns have no local scroll surface.
- **Impact:** method-selection and validation evidence can become unreadable or
  unreachable on a narrow viewport or at 200% zoom. Keyboard users also lack a
  focusable, labeled scroll region.
- **Proposed owner:** portal presentation/accessibility owner.
- **Proposed correction:** wrap every table in a labeled, keyboard-scrollable
  container, or apply overflow directly to a suitable block wrapper generated
  consistently by MkDocs. Preserve header semantics and add a visible focus
  style.
- **Retest:** **Not passed.** Test narrow mobile widths, 200% and 400% zoom,
  keyboard-only horizontal scrolling, forced colors, and print/PDF.

### High — DASC-REV-002: MathML encodes volume elements with the exponent on the variable

- **Pages/equations:**
  - `docs/dasc-conventions.md:31`, `#eq-total-charge`
  - `docs/dasc-conventions.md:43`, `#eq-fourier-pair`
  - `docs/dasc-tgf-free-space-poisson.md:23`, `#eq-tgf-green-convolution`
  - `docs/dasc-potentials-fields-dynamics.md:37`, `#eq-coulomb-potential`
- **URLs:** corresponding `dasc-conventions/`,
  `dasc-tgf-free-space-poisson/`, and
  `dasc-potentials-fields-dynamics/` equation anchors.
- **Evidence:** MathML uses `<mi>d</mi><msup><mi>V|r|k</mi><mn>3</mn></msup>`,
  which represents dV³, dr³, or dk³. The search index exposes the same strings
  (`dV3`, `dr3`, `dk3`), while surrounding prose and dimensional checks require
  d³r or dV.
- **Impact:** the structured equation and assistive/search text state a
  dimensionally different measure from the intended three-dimensional volume
  element. This is not merely visual typography.
- **Proposed owner:** DASC physics documentation owner, with accessibility review.
- **Proposed correction:** encode a standard volume element consistently, such
  as `<msup><mi>d</mi><mn>3</mn></msup><mi>r</mi>` for d³r or `<mi>d</mi><mi>V</mi>`
  for dV, including primed source coordinates.
- **Retest:** **Not passed.** Re-run dimensional review, inspect browser and
  screen-reader math output, and confirm corrected search-index text.

### Medium — DASC-REV-003: fixed-point notation is corrupted by Markdown emphasis

- **Page/section:** `docs/dasc-da-self-consistency.md:25`,
  `https://chongshikpark.github.io/dasc.github.io/dasc-da-self-consistency/#iterated-and-fixed-point-models`.
- **Evidence:** source text `x*(θ) satisfies x* = F(x*,θ)` renders as
  `x<em>(θ) satisfies x</em> = F(x*,θ)`. The fixed-point stars disappear or
  delimit an italic span, while the following MathML equation correctly uses x*.
- **Impact:** the prose definition of the fixed point is ambiguous and disagrees
  with its displayed derivative equation.
- **Proposed owner:** DA/TPSA documentation owner.
- **Proposed correction:** use inline MathML, escaped stars, or unambiguous
  Unicode notation consistently.
- **Retest:** **Not passed.** Inspect visible text, copied text, accessibility
  tree, and search-index extraction.

### Medium — DASC-REV-004: validation-matrix implementation evidence is not directly traceable

- **Page/section:** `docs/dasc-validation-matrix.md:17–35`,
  `https://chongshikpark.github.io/dasc.github.io/dasc-validation-matrix/`.
- **Evidence:** the page gives locked commit SHAs, but component and test cells
  contain abbreviated code text such as `space_charge_vgf.py` and
  `test_vgf_kernel.py`, not links to the exact repository, path, and immutable
  commit. Several test descriptions do not state a complete path.
- **Impact:** a reviewer cannot move directly from claim to immutable
  implementation/test evidence, and similarly named files are possible.
- **Proposed owner:** portal provenance and DASC validation owners.
- **Proposed correction:** link every component and named test/reference to its
  complete path at the locked PyDASC commit; retain the artifact-pending label.
- **Retest:** **Not passed.** Check every matrix link reaches the intended public
  repository/path/SHA and that no branch link replaces an immutable revision.

### Low — DASC-REV-005: completed task numbers remain in reader-facing physics prose

- **Pages/sections:**
  - `docs/dasc-potentials-fields-dynamics.md:72–76`, “Decision required before a
    shared Hamiltonian equation”
  - `docs/dasc-eigenmode-fields.md:50–54`, “Force and self-consistent dynamics”
- **Evidence:** published prose says “Task 3 must,” “Task 4 must,” and “Task 5
  treats,” although Tasks 3–5 now have permanent linked sections.
- **Impact:** readers encounter internal workflow history instead of the current
  scientific status and may infer that completed derivations are still absent.
- **Proposed owner:** DASC documentation editor.
- **Proposed correction:** replace task numbers with links to the completed TGF,
  eigenmode, and DA/TPSA pages while preserving unresolved decisions.
- **Retest:** **Not passed.** Search all published DASC pages for task-number or
  future-placeholder language.

## Manual review gap

### High priority — DASC-REV-GAP-001: interactive accessibility review unavailable

The in-app browser backend was unavailable in this session. Therefore desktop
and mobile interaction, keyboard navigation, 200%/400% zoom, screen-reader math,
copy/paste, contrast, and print-to-PDF were **not tested**. Static HTML and CSS
inspection cannot close these requirements. This gap is especially important
because DASC-REV-001 and DASC-REV-002 affect responsive and assistive output.

- **Proposed owner:** accessibility reviewer with a supported browser and screen
  reader.
- **Retest:** **Blocked by unavailable browser backend**, not by repository code.

## Checks that passed

### Physics and content

- The home page/project chooser and DASC overview remain project- and
  physics-first rather than paper-first.
- TGF and eigenmode formulations state distinct domains, boundaries, time
  models, sources, fields, and applicability limits.
- DA/TPSA, energy consistency, Lie/canonical structure, and symplecticity are
  described as separate properties.
- Assumptions precede the reviewed TGF and cavity equations.
- Planned aperture, self-consistent cavity, DA, convergence, performance, and
  physical results are not presented as validated results.
- The method comparison and validation matrix agree on the prescribed-source
  cavity boundary and the absence of a public allowlisted result package.
- The matrix explicitly leaves a self-consistent symplectic cavity map open.

### Equations, citations, provenance, and search

- 40 displayed equations have unique stable IDs and accessible group labels;
  local equation references and footnote keys resolve.
- Direct DASC source links use commit
  `94033eae4d8eac81f4c42c41f6cfba69e1cd2a25`; local exact-commit checkouts
  contain the referenced source files.
- The locked PyDASC checkout at
  `0506b8a9feb75813ae979f0c1c25a307b21096d2` contains the components and tests
  summarized by the matrix. Direct remote URL fetching was unavailable, so
  public reachability still belongs in the link retest.
- The generated search index contains space charge, TGF, truncated Green
  function, eigenmode, retarded Green function, DA, TPSA, Lie map,
  symplecticity, and causality.

### Navigation and static accessibility

- Navigation is explicit; all DASC physics pages are in `mkdocs.yml`.
- Previous/next footer links stay inside DASC at the project boundaries.
- The secondary table-of-contents rail is hidden, preserving the requested
  two-column navigation/article layout.
- Generated pages pass language/title, landmark, H1, heading-order, image-alt,
  table-header, and unique-ID checks.
- Equations have narrow-screen overflow and print break rules; reduced-motion
  and forced-color rules are present.
- No private/local filesystem path, excluded task source, credential, unapproved
  figure, or unexpected generated file appears in the built artifact.

## Automated verification

- 27 tests passed.
- Physics equation, anchor, citation, and forbidden-path validation passed.
- Exact-lock source collection and publication-boundary validation passed.
- Repeated source assembly produced no generated-content diff.
- `mkdocs build --strict` passed without warnings.
- Site link/presentation and semantic-accessibility validation passed.
- Required search terms were present in the generated search index.
- The built artifact scan found no local filesystem path or excluded task file.
- `git diff --check` passed; the only worktree addition from this review is this
  excluded execution report.

## Release recommendation

Resolve DASC-REV-001 through DASC-REV-004, then run the interactive review in
DASC-REV-GAP-001 before calling the DASC physics section release-clean.
DASC-REV-005 may follow in the same editorial pass. Numerical physics claims
remain artifact-pending exactly as stated in the validation matrix.
