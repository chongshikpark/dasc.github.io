# Task 5 execution summary: DA, TPSA, and Lie methods

## Outcome

Replaced the placeholder Differential Algebra page with a five-page method
section shared by the TGF and causal eigenmode formulations. It defines the
local expansion and normalization contract, differentiates explicit and
self-consistent computations, limits Lie/symplectic claims to declared
canonical maps, traces both physics pipelines, and specifies independent
derivative verification.

No upstream source, source lock, publication-manifest entry, imported document,
benchmark artifact, implementation status, or validation status changed.
Nothing was pushed or deployed.

## Method scope

The section records:

- dimensionless DA variables defined from physical references and scales;
- total-order TPSA objects, multi-indices, truncation remainders, coefficient
  count, coefficient/factorial convention, and conversion back to physical
  derivatives;
- an analytically exact second-order example for a squared physical parameter;
- separate particle-coordinate, distribution, accelerator, geometry, and
  numerical-control sensitivities;
- coefficientwise propagation through fixed linear field operators;
- forward propagation through a fixed iteration versus implicit
  differentiation of a converged, nonsingular fixed point;
- branch, stencil, clipping, adaptivity, loss, randomness, mode-crossing,
  resonance, and conditioning hazards;
- canonical Poisson brackets, Lie generators, symmetric map composition, and
  full multiparticle symplectic-defect diagnostics;
- parallel TGF and causal eigenmode dependency maps from parameters through
  sources, fields, particle evolution, observables, and derivatives; and
- finite-difference, complex-step, analytic, independent-AD, and energy-gradient
  derivative checks with step-size/order/tolerance studies.

## Scientific boundaries

The pages distinguish differentiability, energy consistency, symplecticity,
field accuracy, physical correctness, convergence, gauge consistency, and
causality. DA/TPSA does not establish any of the latter properties.

The reviewed TGF energy-gradient kick is identified as a candidate canonical
submap only under its declared coordinate convention. The causal eigenmode
branch currently derives a laboratory-time Lorentz force but has no frozen
canonical tracking normalization or complete self-consistent Hamiltonian split,
so no Lie or symplectic-map claim is made for that branch.

The dependency maps are mathematical architecture, not a claim that all edges
are implemented. The portal has no approved result artifact for a full
coefficient-space tracker, differentiated aperture solve, self-consistent
eigenmode map, derivative performance, or collective-mode result.

## Reviewed sources

The controlling DASC source commit is
`94033eae4d8eac81f4c42c41f6cfba69e1cd2a25`, principally:

- `docs/differentiable_symplectic_space_charge_study.tex`; and
- `docs/space_charge_research_plan.tex`.

Approved primary references represented in the pages include Qiang for
differentiable self-consistent tracking and multiparticle symplectic models,
and Erdelyi, Nissen, and Manikonda for differential-algebraic Poisson methods.

## Files added

- `docs/dasc-da-tpsa.md`
- `docs/dasc-da-self-consistency.md`
- `docs/dasc-da-lie-maps.md`
- `docs/dasc-da-pipelines.md`
- `docs/dasc-da-verification.md`
- `docs/exec-plans/completed/017-dasc-physics-documentation-task-5.md`

## Files updated

- `docs/dasc-differential-algebra-methods.md`
- `mkdocs.yml`
- `tests/test_physics_docs.py`

## Visible unresolved issues

1. The exact TPSA library storage convention and supported primitive set must
   be verified at each implementation boundary.
2. The complete coefficient-space TGF tracker and its performance evidence are
   not approved public results.
3. Eigenmode geometry, aperture-system, causal-history, and self-consistency
   derivatives require implementation and validation.
4. Canonical coordinates and a Hamiltonian split for the cavity branch remain
   unfrozen.
5. Nonsmooth branch policies, mode degeneracies, loss, and adaptive solver
   decisions require explicit application-specific treatment.

## Verification

- 26 tests passed.
- Physics equation, anchor, citation, and forbidden-path validation passed.
- Exact-lock source collection and publication-boundary validation passed.
- Repeated source assembly produced no generated-content diff.
- `mkdocs build --strict` passed without warnings.
- Site link/presentation and semantic-accessibility validation passed.
- The built artifact scan found no local filesystem path or excluded task file.

Interactive browser, screen-reader, copy/paste, 200% zoom, and print-to-PDF
inspection remain part of the final Task 7 review.
