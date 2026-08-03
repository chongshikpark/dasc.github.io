# Derivative verification, limits, and scaling

## Verification methods

Use at least one independent derivative route and vary its control parameter:

| Method | Check | Limits |
|---|---|---|
| Analytic identity | charge linearity, translation identities, the [quadratic TPSA example](dasc-da-tpsa.md#eq-tpsa-small-example), modal derivatives | available only for selected cases |
| Centered finite difference | [f(θ+h)−f(θ−h)]/(2h) over a logarithmic h sweep | O(h²) truncation followed by cancellation/noise |
| Complex step | Im f(θ+ih)/h over an h study | only for a holomorphic code path; invalid through conjugation, real-only branches, clipping, many eigensolver labels |
| Independent automatic differentiation | compare value, JVP/VJP, gradient, and selected Hessian actions | independence is reduced if it shares the same faulty primitives |
| Energy difference | compare the TGF force with centered differences of the same U_h | tests energy consistency, not continuous field accuracy |

For reference derivative d_ref and candidate d, define

<div id="eq-da-derivative-error" class="dasc-equation" role="group" aria-label="Relative derivative verification error with absolute fallback scale">
<math display="block"><mi>e</mi><mo>=</mo><mfrac><mrow><mo>‖</mo><mi>d</mi><mo>−</mo><msub><mi>d</mi><mtext>ref</mtext></msub><mo>‖</mo></mrow><mrow><mi>max</mi><mo>(</mo><mo>‖</mo><msub><mi>d</mi><mtext>ref</mtext></msub><mo>‖</mo><mo>,</mo><msub><mi>d</mi><mtext>abs</mtext></msub><mo>)</mo></mrow></mfrac><mo>.</mo></math>
</div>

Report the norm, d_abs, units, parameter scale, perturbation sequence, DA order,
precision, reference method, and a predeclared tolerance. A single convenient
h or one agreement digit is not a verification study. Repeat after grid,
particle, mode, quadrature, step, and fixed-point convergence; derivative
agreement for an unconverged primal problem is not physical validation.

## Truncation and trust-region studies

For orders p and p+1, compare retained coefficients and direct evaluations at
several dimensionless radii ‖δ‖. The expected local remainder is order
‖δ‖^(p+1) only while the underlying map is sufficiently smooth and the active
branch stays fixed. Report coefficient norms by total order; rapid growth may
indicate poor scaling, nearby singularities, or an oversized trust region.

## Computational scaling

N_DA grows combinatorially as shown in [the TPSA definition](dasc-da-tpsa.md#eq-tpsa-expansion).
For a padded TGF grid with M values, coefficientwise convolution costs roughly
O(N_DA M log M) time and O(N_DA M) coefficient storage before workspace and
particle state. Deposition/force work is roughly O(N_DA N_p n_s) for N_p
particles and n_s shape points, although nonlinear TPSA multiplication costs
depend on order, sparsity, and library representation.

For the eigenmode branch, cost additionally scales with retained radial/axial
modes, source-time quadrature, observation points, frequency blocks, aperture
basis size, and dense or iterative block-system solution. DA coefficients can
reuse fixed factorizations only when geometry, basis, radiation branch, and
matrix structure remain compatible with the differentiated parameter.

Report peak memory, coefficient sparsity, wall time, field solves, factorization
reuse, precision, and batch strategy by DA order and parameter count. Forward
DA is attractive for a moderate number of meaningful controls and higher-order
local maps; it is not automatically cheaper than adjoint or reverse methods.

## Required non-claims

Passing derivative checks does not establish the TGF free-space approximation,
cavity boundary model, causality, gauge residual, aperture convergence,
energy consistency, symplecticity, or experimental validity. Those remain the
separate verification programs linked from the [TGF](dasc-tgf-verification.md)
and [eigenmode](dasc-eigenmode-verification.md) sections.[^erdelyi]

[^erdelyi]: B. Erdelyi, E. Nissen, and S. Manikonda, “A Differential Algebraic method for the solution of the Poisson equation for charged particle beams,” *Commun. Comput. Phys.* 17 (2015), 47–78, [doi:10.4208/cicp.240813.170614a](https://doi.org/10.4208/cicp.240813.170614a).
