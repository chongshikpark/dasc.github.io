# DA dependency maps across both formulations

These maps state what a coefficient depends on. They do not claim every edge is
implemented or validated in current PyDASC.

## TGF free-space branch

| Stage | Nominal value | DA/TPSA action | Required fixed contract |
|---|---|---|---|
| Parameters | particle/distribution, accelerator, selected physical controls | seed normalized δ variables | reference, units, scales, order |
| Particle loading | q_i(δ), fixed samples ξ_i | reparameterize the same sample | seed/quiet start and support |
| Deposition | ρ_g(q,δ) | differentiate shape and normalization | grid, shape, frozen stencil/trust cell |
| Free-space solve | φ = K_hρ/ε₀ | apply the same linear VGF operator to each coefficient | domain, equal spacing, padding, cutoff, kernel |
| Particle force | F = −ΔV Dᵀφ | propagate deposition Jacobian and energy gradient | same shape/derivative and canonical normalization |
| Tracking | external half-map, kick, external half-map | compose coefficient maps | canonical variables, step and splitting |
| Observable | moments, losses, objective, map coefficients | TPSA-compatible reduction | smooth definition and membership |

For first-order seed ε in a direction v,
M(z₀+εv) = M(z₀)+ε(DM·v)+O(ε²); the coefficient of ε is a matrix-free
Jacobian-vector product. Blocks of seeds can propagate multiple tangent
directions without forming the full multiparticle Jacobian.

## Causal eigenmode branch

| Stage | Nominal value | DA/TPSA action | Required fixed contract |
|---|---|---|---|
| Parameters | Q, source profile, prescribed trajectory, RF/geometry controls | seed dimensionless local variables | reference, scales, differentiable parameterization |
| Modal source | F_n, u_p[z_b(t)], v_p[z_b(t)]v_b(t) | differentiate source moments and trajectory history | fixed source model, mode labeling and time grid |
| Closed-cavity solve | retarded modal convolutions for φ and A_z | propagate coefficients through quadrature and modal sums | radial/axial mode sets, causal mask, initial data |
| Aperture solve | block system for A_ν,B_μ | differentiate fixed linear system or use implicit solve | basis, frequency blocks, radiation branches, nonsingularity |
| Fields | analytic E_r,E_z,B_θ sums | differentiate modal factors and histories | field convention and regularity treatment |
| Particle update | Lorentz force and source-history feedback | propagate through the declared time integrator/iteration | interpolation, loss policy, converged self-consistency |
| Observable | fields, power, beam statistics, residuals | TPSA-compatible reduction | smooth measurement and fixed domains |

Geometry differentiation is more delicate than source differentiation: Bessel
roots may be fixed dimensionless numbers, but physical wave numbers, basis
normalizations, boundaries, observation coordinates, aperture overlaps, and
pipe propagation constants all change. A mode crossing must be treated as a
subspace problem rather than differentiating an arbitrary label.

## Status boundary

The reviewed sources support these mathematical dependency maps. The TGF
linear coefficient solve and energy-consistent force have concrete reviewed
PyDASC counterparts. The full coefficient-space tracker, causal eigenmode
implementation, aperture derivative solve, and self-consistent DA map do not
have approved public result artifacts in this portal.
