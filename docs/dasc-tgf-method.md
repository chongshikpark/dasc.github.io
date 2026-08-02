# Truncated Green's-function method

The TGF section concerns the free-space electrostatic or quasistatic Poisson
problem used by the DA–VGF line of work. It is separate from the causal cavity
eigenmode formulation.

## Free-space Poisson problem

The later derivation will state the source domain, open-boundary condition,
Green-function convolution, frame, units, and regularity assumptions before
introducing an FFT algorithm.

## TGF/Vico–Greengard–Ferrando formulation

This page boundary will explain physical-space kernel truncation, the geometric
condition under which it preserves the required convolution, padding, spectral
normalization, and aperiodic evaluation. Task 1 makes no convergence claim.

## Field and kick construction

The field, deposition/gathering operations, discrete interaction energy, force,
and space-charge kick must be connected consistently. An accurate field solve
alone does not make a particle map symplectic.

## Verification and convergence

Planned evidence includes analytical field checks, charge and sign checks,
domain/grid/padding studies, force-energy consistency, DA derivative checks,
and map diagnostics. Results will appear only with immutable configurations and
acceptance criteria.

See the public DASC
[DA–TGF source study](https://github.com/chongshikpark/dasc/blob/94033eae4d8eac81f4c42c41f6cfba69e1cd2a25/docs/differentiable_symplectic_space_charge_study.tex)
and the current [PyDASC simulation workflow](pydasc/guides/simulation-workflow.md).

