# Task 1 execution summary: DASC project overview and section architecture

## Outcome

Replaced the paper-first DASC entry experience with a hand-written,
physics-first project overview while preserving the imported upstream README as
a secondary research-output page. The publication manifest, source locks, and
five-file imported-content boundary did not change.

The new overview answers the required project questions: physical problem,
self-consistency versus differentiability, distinct TGF and eigenmode roles,
DA/TPSA limits, the supported role of Lie methods, DASC/PyDASC ownership,
current status and non-claims, and authoritative source/reproducibility records.
An accessible text flow and prose equivalent connect source construction, field
solution, particle effects, sensitivities, and validation.

## Published architecture

```text
DASC
├── Project overview
├── Physics foundations
│   ├── Self-consistent space charge
│   ├── Frames, coordinates, units, and conventions
│   ├── Potentials, fields, and particle dynamics
│   └── Approximations and validity limits
├── Differential-algebra methods
│   ├── DA and finite-order TPSA
│   ├── Differentiating the self-consistent solve
│   └── Lie maps and symplectic structure
├── Truncated Green's-function method
│   ├── Free-space Poisson problem
│   ├── TGF/Vico–Greengard–Ferrando formulation
│   ├── Field and kick construction
│   └── Verification and convergence
├── Eigenmode method
│   ├── Finite cylindrical cavity problem
│   ├── Retarded scalar and vector potentials
│   ├── Modal field derivation
│   ├── Aperture and downstream-pipe coupling
│   └── Verification and convergence
├── Comparison and method selection
├── Reproducibility
└── Research outputs and publications
    ├── Overview
    └── Reviewed source overview
```

Task 1 supplies section landing pages and explicit conceptual boundaries, not
the derivations assigned to Tasks 2–5. Each page marks planned evidence as
planned and links to immutable public DASC source files without copying excluded
LaTeX into the portal.

## Navigation behavior

The home card and project chooser now enter through `dasc-project-overview.md`.
The imported `dasc/index.md` appears only at the end of Research outputs and
publications, retaining its immutable source record and `Unvalidated` label.

A repository-owned footer override classifies pages as portal, PyDASC, or DASC
and displays previous/next links only when the adjacent page remains in the same
group. Rendered verification confirmed:

- DASC Project overview has no PyDASC previous link and advances to Physics
  foundations;
- Reviewed source overview returns to the DASC Research outputs overview and
  does not advance to Contribute; and
- the final PyDASC Conventions page returns within PyDASC and does not advance
  into DASC.

The left navigation and project chooser remain the explicit cross-project paths.

## Scientific scope

- TGF is described only as the electrostatic/quasistatic free-space Poisson line
  of work.
- Eigenmode is described only as the causal electromagnetic finite-cavity,
  aperture, and downstream-pipe line of work.
- DA/TPSA describes local parameter dependence and does not guarantee physical
  correctness, convergence, causality, energy consistency, or symplecticity.
- Lie methods are limited to construction or analysis where canonical variables
  and a supported map are actually defined.
- No kinetic-resonance, optimization, aperture-coupling, validation, or
  self-consistent-trajectory result is presented as completed.
- The legacy small-hole manuscript and supplements are identified as
  non-controlling sources; no equation or figure was copied from them.

## Files added

- `docs/dasc-project-overview.md`
- `docs/dasc-physics-foundations.md`
- `docs/dasc-differential-algebra-methods.md`
- `docs/dasc-tgf-method.md`
- `docs/dasc-eigenmode-method.md`
- `docs/dasc-method-selection.md`
- `docs/dasc-reproducibility.md`
- `docs/dasc-research-outputs.md`
- `docs/overrides/partials/footer.html`
- `docs/exec-plans/completed/013-dasc-physics-documentation-task-1.md`

## Files updated

- `docs/index.md` and `docs/getting-started.md` — project-first DASC entry links.
- `mkdocs.yml` — explicit DASC hierarchy and restored controlled footer feature.
- `README.md` — DASC architecture and section-local navigation contract.
- `tests/test_docs.py` and `tests/test_presentation.py` — entry-point and
  boundary-navigation policy regression checks.

## Verification

- 21 tests passed.
- Exact-lock source collection and publication validation passed.
- Repeated collection was byte-for-byte deterministic.
- `mkdocs build --strict` passed without warnings.
- Site-link/presentation and semantic-accessibility validators passed.
- All new local links, breadcrumbs, and explicit navigation entries resolved.
- Search indexed space charge, truncated Green function, eigenmode, Differential
  Algebra, TPSA, Lie, symplectic, and causal terminology.
- The task brief, architecture/operations/execution records, upstream LaTeX,
  local paths, credentials, and excluded source files were absent from `site/`.

No browser was available for interactive desktop/mobile, keyboard, 200% zoom,
or screenshot review. Structural markup, responsive assets, section-local footer
links, and automated accessibility checks passed; interactive visual review
remains a Task 7 release gate.

Nothing was pushed or deployed.
