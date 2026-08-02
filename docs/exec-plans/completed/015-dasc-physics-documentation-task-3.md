# Task 3 execution summary: TGF free-space space-charge derivation

## Outcome

Added a four-page derivation of the truncated Green's-function free-space
space-charge method. It begins with the physical boundary-value problem,
derives the free-space convolution and truncation geometry, records the reviewed
Vico–Greengard–Ferrando discretization, and distinguishes a spectral grid field
from the energy-consistent particle force and canonical kick.

No upstream source, source lock, publication-manifest entry, imported document,
benchmark artifact, or validation status changed. Nothing was pushed or
deployed.

## Derivation scope

The section records:

- the free-space Poisson equation, decay condition, Coulomb convolution, and
  integrable singularity;
- why an unmodified periodic FFT solves the wrong boundary-value problem;
- physical kernel truncation and the exact source–observation separation
  condition;
- PyDASC's reviewed equal-spacing, twofold-padding cutoff constraint;
- the analytic truncated-kernel spectrum and finite zero-mode limit;
- volume-weighted discrete-kernel, inverse-transform, normalization, cropping,
  complexity, memory, and failure-mode conventions;
- the direct spectral grid field and its zero/Nyquist derivative treatment;
- the discrete interaction energy, transpose deposition-Jacobian force, and
  time-based momentum kick;
- the precise condition under which that kick is canonical, without extending
  the claim to an unverified tracking composition; and
- differentiability boundaries for Gaussian and frozen-stencil cubic B-spline
  deposition.

## Verification and evidence boundary

The verification page specifies independent analytic-reference, grid, domain,
cutoff, padding, deposition, charge/sign, finite-difference, operator-symmetry,
self-force, momentum-balance, reversibility, and symplectic-defect studies. It
also defines a relative discrete L2 metric and the metadata/checksums required
for a reproducible result.

The page intentionally contains no numerical result table. Reviewed PyDASC
tests and benchmark entry points establish implementation evidence only; no
approved raw benchmark artifact and configuration were available for a public
accuracy or convergence claim.

## Reviewed sources

The derivation is traceable to DASC commit
`94033eae4d8eac81f4c42c41f6cfba69e1cd2a25`, principally
`docs/differentiable_symplectic_space_charge_study.tex`, and to reviewed PyDASC
implementation commit `0506b8a9feb75813ae979f0c1c25a307b21096d2`, including:

- `src/pydasc/space_charge_kernels/space_charge_vgf.py`;
- `src/pydasc/hamiltonian/space_charge.py`;
- `docs/CONVENTIONS.md`;
- `docs/SIMULATION_WORKFLOW.md`; and
- the associated solver, Hamiltonian, validation, and benchmark tests.

The VGF kernel construction is cited to the primary Vico, Greengard, and
Ferrando paper. The map discussion cites the approved source used by the DASC
study.

## Files added

- `docs/dasc-tgf-free-space-poisson.md`
- `docs/dasc-tgf-formulation.md`
- `docs/dasc-tgf-field-kick.md`
- `docs/dasc-tgf-verification.md`
- `docs/exec-plans/completed/015-dasc-physics-documentation-task-3.md`

## Files updated

- `docs/dasc-tgf-method.md`
- `mkdocs.yml`
- `tests/test_physics_docs.py`

## Visible unresolved issues

1. The general DASC tracking independent variable, canonical normalization,
   and complete rest-frame-to-tracking-frame transformation remain unfrozen.
2. Anisotropic boxes that cannot satisfy the reviewed twofold-padding cutoff
   interval require a separately reviewed padding policy.
3. Self-force, boundary behavior, particle-number convergence, momentum
   balance, and full-map structural diagnostics remain planned verification.
4. Direct grid-field accuracy and energy-consistent particle-force accuracy
   must be reported separately.

## Verification

- 24 tests passed.
- Physics equation, anchor, citation, and forbidden-path validation passed.
- Exact-lock source collection and publication-boundary validation passed.
- Repeated source assembly produced no generated-content diff.
- `mkdocs build --strict` passed without warnings.
- Site link/presentation and semantic-accessibility validation passed.
- The built artifact scan found no local filesystem path or excluded task file.

Interactive browser, screen-reader, copy/paste, 200% zoom, and print-to-PDF
inspection remain part of the final Task 7 review.
