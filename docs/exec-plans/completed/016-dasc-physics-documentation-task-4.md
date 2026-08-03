# Task 4 execution summary: causal finite-cavity eigenmode derivation

## Outcome

Added a five-page derivation of the causal electromagnetic self-field for an
axisymmetric source in a finite cylindrical PEC cavity with a centered aperture
and downstream circular pipe. The section distinguishes the analytically
derived closed-cavity reference, the specified aperture mode-matching
formulation, and small-aperture theory as a controlled limiting benchmark.

No upstream source, source lock, publication-manifest entry, imported document,
benchmark artifact, implementation status, or validation status changed.
Nothing was pushed or deployed.

## Derivation scope

The new section records:

- the cavity, cathode, end wall, aperture, and semi-infinite pipe domains;
- the prescribed-trajectory axisymmetric slice source, signed normalization,
  current, and continuity requirement;
- Lorenz-gauge scalar and longitudinal-vector wave equations with initial-data
  assumptions;
- distinct scalar Dirichlet and vector-potential Neumann axial boundaries;
- normalized Bessel radial modes, sine/cosine axial families, modal wave
  numbers, frequencies, and source projections;
- retarded Green functions and trajectory-history convolutions, including the
  required velocity factor in the accelerating current source;
- analytic radial electric, longitudinal electric, and azimuthal magnetic
  fields without finite-differencing the potentials;
- on-axis regularity, PEC behavior, physical signs, and Lorentz-force coupling;
- cavity/pipe mode matching, tangential interface conditions, overlap matrices,
  outgoing and evanescent pipe modes, and causal reconstruction;
- the valid role and scale limits of small-aperture theory; and
- numerical truncation, causality, resonance, differentiability, and
  self-consistency failure modes.

## Evidence labels and non-claims

The closed-cavity equations are labeled analytic derivation. Aperture mode
matching is labeled a specified primary formulation rather than a completed
solver. Full-wave comparison, convergence, DA derivatives, self-consistent
tracking, and physical validation are planned checks only. The pages do not
claim a canonical or symplectic particle map because the complete particle
integrator and canonical normalization for this branch remain unfrozen.

The verification hierarchy separates dimensional/sign, source/gauge,
boundary, symmetry, causality, modal/quadrature, reference-limit, aperture,
energy/radiation, independent-solver, and particle/DA checks. It defines a
normalized boundary residual and the complete provenance/configuration record
required before numerical results can be published.

## Reviewed sources

The controlling source is DASC commit
`94033eae4d8eac81f4c42c41f6cfba69e1cd2a25`, file
`docs/space_charge_fields_with_aperture_study.tex`. Its reassessment supersedes
the earlier small-hole manuscript and incremental supplements for this
formulation. Approved primary references represented in the pages include Hess,
Park, and Bolton for the retarded cathode-pipe formulation; Collin for guided
waves; Bethe for the small-aperture limit; and the shared Jackson-based field
conventions.

## Files added

- `docs/dasc-eigenmode-problem.md`
- `docs/dasc-eigenmode-closed-cavity.md`
- `docs/dasc-eigenmode-fields.md`
- `docs/dasc-eigenmode-aperture.md`
- `docs/dasc-eigenmode-verification.md`
- `docs/exec-plans/completed/016-dasc-physics-documentation-task-4.md`

## Files updated

- `docs/dasc-eigenmode-method.md`
- `mkdocs.yml`
- `tests/test_physics_docs.py`

## Visible unresolved issues

1. A complete, reviewed cavity-to-pipe mode-matching implementation and
   allowlisted result artifacts are not available.
2. Lossy walls, resonance handling, finite-length/nonaxisymmetric sources, and
   full-wave comparisons require separate development and validation.
3. The self-consistent source-history iteration, particle interpolation and
   integration scheme, and canonical coordinate normalization are not frozen.
4. DA/TPSA differentiation across causal quadrature, mode changes, aperture
   solves, trajectory feedback, and resonant degeneracies remains Task 5 work.

## Verification

- 25 tests passed.
- Physics equation, anchor, citation, and forbidden-path validation passed.
- Exact-lock source collection and publication-boundary validation passed.
- Repeated source assembly produced no generated-content diff.
- `mkdocs build --strict` passed without warnings.
- Site link/presentation and semantic-accessibility validation passed.
- The built artifact scan found no local filesystem path or excluded task file.

Interactive browser, screen-reader, copy/paste, 200% zoom, and print-to-PDF
inspection remain part of the final Task 7 review.
