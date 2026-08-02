# Task 2 execution summary: shared self-consistent space-charge foundations

## Outcome

Expanded the DASC physics foundation into four reviewed pages covering shared
conventions, source conservation and self-consistency, potentials/fields and
particle dynamics, and approximation/validity boundaries. The pages provide a
coherent source-to-particle sequence without merging the TGF free-space Poisson
model with the causal finite-cavity electromagnetic model.

No upstream file, source lock, publication-manifest entry, imported document,
benchmark value, figure, or scientific validation status changed.

## Derivation scope

The new foundation records:

- signed charge/current normalization and the continuity equation;
- SI symbols, dimensions, TGF Fourier convention, and field/force signs;
- the distinction between prescribed-source and self-consistent calculations;
- normalized particle deposition and its charge-conservation condition;
- the Lorenz gauge and scalar/vector potential wave equations;
- the electrostatic free-space Poisson limit and Coulomb convolution;
- fields reconstructed from potentials and the signed Lorentz force;
- the boundary between a force update and a canonical Hamiltonian map;
- exact identities versus modeling approximations, discretizations, and
  implementation choices; and
- regularity, causality, conservation, convergence, and evidence-label limits.

Every displayed equation defines its domain in surrounding prose, uses symbols
introduced in the convention table or locally, has a descriptive accessible
label and stable `eq-` anchor, and participates in per-page visible numbering.
Key equations include dimensional checks. Cross-references use descriptive
links rather than raw equation numbers.

## Source use and non-claims

The derivation is traceable to the DASC checkout
`94033eae4d8eac81f4c42c41f6cfba69e1cd2a25`, principally:

- `docs/differentiable_symplectic_space_charge_study.tex:127-248` for the
  free-space Poisson problem, Fourier convention, and TGF field boundary;
- the same file at lines 428–625 for the discrete-Hamiltonian and symplectic-map
  caveats;
- `docs/space_charge_fields_with_aperture_study.tex:45-194` for the cavity
  source, continuity, Lorenz gauge, boundary conditions, and distinct modal
  families; and
- the same file at lines 264–369 for field reconstruction, inductive terms,
  causality, and the finite-cavity/semi-infinite distinction.

Approved primary references already cited by those sources are represented as
keyboard-accessible footnotes. No legacy claim of completed cavity validation,
promotional abstract statement, proposed resonance, or future experimental
result was reused as evidence.

## Visible unresolved decisions

The pages intentionally stop rather than guess at:

1. a shared metric and Lorentz-transformation convention;
2. the DASC tracking independent variable and canonical normalization;
3. replacement of the symbolic TGF `C_sc` factor with the exact reviewed
   PyDASC map convention;
4. the cavity transition from prescribed trajectory to self-consistent
   trajectory closure;
5. finite-longitudinal-profile and non-axisymmetric cavity generalizations; and
6. the exact differentiated parameter set and smooth trust region for each
   formulation.

Current PyDASC's paraxial equal-time scaling is identified as model-specific and
not misrepresented as a general Lorentz transformation.

## Rendering and validation

Equations use native MathML, avoiding remote JavaScript, fonts, or a new build
dependency. Repository CSS supplies narrow-screen horizontal overflow,
print-safe page-break behavior, and visible counters. Each equation group has
an accessible prose label, while MathML preserves structured mathematical text.

Added `scripts/validate_physics_docs.py` and workflow integration to fail on:

- duplicate or undefined `eq-` anchors;
- inaccessible display-math containers;
- missing or unused citation-footnote keys;
- unsupported raw TeX citation/reference syntax; and
- local absolute filesystem paths.

The validator runs in documentation checks, deployment, and automated
source-update proposal validation.

## Files added

- `docs/dasc-conventions.md`
- `docs/dasc-self-consistent-space-charge.md`
- `docs/dasc-potentials-fields-dynamics.md`
- `docs/dasc-validity-limits.md`
- `scripts/validate_physics_docs.py`
- `tests/test_physics_docs.py`
- `docs/exec-plans/completed/014-dasc-physics-documentation-task-2.md`

## Files updated

- `docs/dasc-physics-foundations.md`
- `mkdocs.yml`
- `docs/stylesheets/readthedocs.css`
- `README.md`
- all three GitHub Actions workflows
- `tests/test_presentation.py` and `tests/test_workflow.py`

## Verification

- 23 tests passed.
- Physics equation/citation/path validation passed.
- Exact-lock source collection and publication validation passed.
- Repeated assembly was byte-for-byte deterministic.
- `mkdocs build --strict` passed without warnings.
- Site link/presentation and semantic-accessibility validation passed.
- Equation IDs, local references, footnote back-links, search terms, local
  assets, narrow-overflow CSS, and print rules were inspected in built HTML.
- Excluded task/source/internal records and local filesystem paths were absent
  from the artifact.

Interactive browser, screen-reader, copy/paste, 200% zoom, and print-to-PDF
inspection remain required in the final Task 7 review. Nothing was pushed or
deployed.
