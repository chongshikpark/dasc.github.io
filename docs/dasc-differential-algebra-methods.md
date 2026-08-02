# Differential-algebra methods

This section defines where Differential Algebra (DA), finite-order Truncated
Power Series Algebra (TPSA), and Lie methods enter DASC. They describe local
parameter dependence and map structure; they do not certify the underlying
physics.

## DA and finite-order TPSA

The detailed method page will define expansion points, variables, order,
truncation, and coefficient interpretation. It will distinguish derivatives
with respect to particle coordinates, distribution parameters, accelerator
controls, trajectories, geometry, and numerical controls.

## Differentiating the self-consistent solve

The documentation will trace supported coefficients through source
construction, field solution, force or kick evaluation, particle evolution,
and observables. Branch changes, clipping, changing particle stencils, adaptive
choices, particle loss, and mode crossings require explicit treatment rather
than an assumption of smoothness.

## Lie maps and symplectic structure

Where DASC defines canonical variables and a Hamiltonian map, Lie methods can
support construction, composition, and analysis. Differentiability, energy
consistency, and symplecticity remain separate properties with separate tests.

The source scope is recorded in the public DASC
[DA–TGF study](https://github.com/chongshikpark/dasc/blob/94033eae4d8eac81f4c42c41f6cfba69e1cd2a25/docs/differentiable_symplectic_space_charge_study.tex)
and [physics-first research plan](https://github.com/chongshikpark/dasc/blob/94033eae4d8eac81f4c42c41f6cfba69e1cd2a25/docs/space_charge_research_plan.tex).
No proposed collective result is treated here as evidence.

