# Differentiating self-consistent calculations

## Explicit propagation

In forward DA, every smooth operation receives TPSA coefficients and returns
coefficients through the same arithmetic graph. Linear field operators act
independently on each source coefficient. Nonlinear deposition, force,
tracking, and observables mix coefficients through truncated polynomial
products. The coefficient index should be a batch dimension; spatial FFTs or
modal operations act on numerical arrays, not opaque high-level DA objects.

For a TGF density expansion ρ = Σ_αρ_αδ^α, linearity gives

<div id="eq-da-linear-field-propagation" class="dasc-equation" role="group" aria-label="Coefficientwise propagation through a fixed linear field operator">
<math display="block"><msub><mi>φ</mi><mi mathvariant="bold">α</mi></msub><mo>=</mo><msub><mi>K</mi><mi>h</mi></msub><msub><mi>ρ</mi><mi mathvariant="bold">α</mi></msub><mo>/</mo><msub><mi>ε</mi><mn>0</mn></msub><mo>.</mo></math>
</div>

This coefficientwise identity assumes the grid, physical domain, padding,
cutoff policy, and kernel remain fixed throughout the local expansion. Making
a discrete solver choice depend on δ changes the computational branch and is
not represented by this derivative.

## Iterated and fixed-point models

Suppose a converged self-consistent state <math><msup><mi>x</mi><mo>∗</mo></msup><mo>(</mo><mi>θ</mi><mo>)</mo></math> satisfies <math><msup><mi>x</mi><mo>∗</mo></msup><mo>=</mo><mi>F</mi><mo>(</mo><msup><mi>x</mi><mo>∗</mo></msup><mo>,</mo><mi>θ</mi><mo>)</mo></math>. If F is differentiable at the solution and I−F_x is invertible, implicit differentiation gives

<div id="eq-da-fixed-point-derivative" class="dasc-equation" role="group" aria-label="Implicit derivative of a converged self consistent fixed point">
<math display="block"><mo>(</mo><mi>I</mi><mo>−</mo><msub><mi>F</mi><mi>x</mi></msub><mo>)</mo><mfrac><mrow><mi>d</mi><msup><mi>x</mi><mo>*</mo></msup></mrow><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac><mo>=</mo><msub><mi>F</mi><mi>θ</mi></msub><mo>.</mo></math>
</div>

This equation may be solved with matrix-free Jacobian-vector products. It is
not justified at a nonconverged iterate, a nonsmooth branch, or a singular
fixed point. Near loss of invertibility, sensitivities can be physically large
and numerically ill-conditioned.

Alternatively, DA can be propagated through exactly K iterations. That result
is the derivative of the K-step algorithm. It approaches the fixed-point
derivative only when the primal iteration and its tangent iteration converge.
Stopping on a parameter-dependent iteration count makes the program map
piecewise defined; either freeze the count locally or verify tolerance and
derivative convergence independently.

## Differentiability hazards

- Particle-cell or frozen-stencil changes invalidate a local deposition map.
- Clipping, min/max limiters, absolute-value cusps, and hard aperture penalties
  are nonsmooth at their switching surfaces.
- Adaptive meshes, mode counts, quadrature nodes, cutoff policies, and solver
  fallbacks create branch changes.
- Particle loss and scraping change state dimension or membership.
- Random resampling changes the function being differentiated.
- Labeled eigenvectors are unstable at degeneracy or mode crossing; use an
  invariant subspace or a smooth spectral projector when available.
- Resonance poles and nearly singular aperture or fixed-point systems amplify
  conditioning error.

A trust region must keep the active branch and representation valid. Crossing
that boundary requires rebuilding the reference state and TPSA map.
