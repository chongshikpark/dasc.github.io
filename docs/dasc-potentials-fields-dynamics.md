# Potentials, fields, and particle dynamics

## Electromagnetic model

Assume SI units, a specified domain, signed sources ρ and **J** satisfying the
[continuity equation](dasc-self-consistent-space-charge.md#eq-continuity), and
the Lorenz gauge. The gauge condition is

<div id="eq-lorenz-gauge" class="dasc-equation" role="group" aria-label="Lorenz gauge: divergence of vector potential plus time derivative of scalar potential divided by c squared equals zero">
<math display="block"><mo>∇</mo><mo>·</mo><mi mathvariant="bold">A</mi><mo>+</mo><mfrac><mn>1</mn><msup><mi>c</mi><mn>2</mn></msup></mfrac><mfrac><mrow><mo>∂</mo><mi>φ</mi></mrow><mrow><mo>∂</mo><mi>t</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>.</mo></math>
</div>

Under these assumptions, the potentials satisfy the exact inhomogeneous wave
equations[^jackson]:

<div id="eq-potential-waves" class="dasc-equation" role="group" aria-label="Wave equations for scalar and vector potentials in Lorenz gauge">
<math display="block"><mrow><mo>(</mo><msup><mo>∇</mo><mn>2</mn></msup><mo>−</mo><mfrac><mn>1</mn><msup><mi>c</mi><mn>2</mn></msup></mfrac><mfrac><msup><mo>∂</mo><mn>2</mn></msup><mrow><mo>∂</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>)</mo></mrow><mi>φ</mi><mo>=</mo><mo>−</mo><mfrac><mi>ρ</mi><msub><mi>ε</mi><mn>0</mn></msub></mfrac><mo>,</mo><mspace width="1em"/><mrow><mo>(</mo><msup><mo>∇</mo><mn>2</mn></msup><mo>−</mo><mfrac><mn>1</mn><msup><mi>c</mi><mn>2</mn></msup></mfrac><mfrac><msup><mo>∂</mo><mn>2</mn></msup><mrow><mo>∂</mo><msup><mi>t</mi><mn>2</mn></msup></mrow></mfrac><mo>)</mo></mrow><mi mathvariant="bold">A</mi><mo>=</mo><mo>−</mo><msub><mi>μ</mi><mn>0</mn></msub><mi mathvariant="bold">J</mi><mo>.</mo></math>
</div>

Boundary conditions, initial conditions, and the retarded Green function are
part of the problem definition. The cavity formulation uses distinct scalar
Dirichlet and longitudinal-vector Neumann axial modal families; replacing them
with one family changes the boundary-value problem.

## Electrostatic free-space limit

For a time-independent or approved quasistatic rest-frame source with magnetic
effects removed from that solve, [the wave equations](#eq-potential-waves)
reduce to the Poisson boundary-value problem

<div id="eq-free-space-poisson" class="dasc-equation" role="group" aria-label="Free-space Poisson equation with potential vanishing at infinity">
<math display="block"><msup><mo>∇</mo><mn>2</mn></msup><mi>φ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo><mo>=</mo><mo>−</mo><mfrac><mrow><mi>ρ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo></mrow><msub><mi>ε</mi><mn>0</mn></msub></mfrac><mo>,</mo><mspace width="1em"/><mi>φ</mi><mo>→</mo><mn>0</mn><mspace width="0.5em"/><mtext>as</mtext><mspace width="0.5em"/><mo>‖</mo><mi mathvariant="bold">r</mi><mo>‖</mo><mo>→</mo><mo>∞</mo><mo>.</mo></math>
</div>

Its exact free-space Green-function representation is

<div id="eq-coulomb-convolution" class="dasc-equation" role="group" aria-label="Coulomb Green-function convolution for electrostatic potential">
<math display="block"><mi>φ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><mrow><mn>4</mn><mi>π</mi><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfrac><msup><mo>∫</mo><msup><mi mathvariant="normal">ℝ</mi><mn>3</mn></msup></msup><mfrac><mrow><mi>ρ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>′</mo><mo>)</mo></mrow><mrow><mo>‖</mo><mi mathvariant="bold">r</mi><mo>−</mo><mi mathvariant="bold">r</mi><mo>′</mo><mo>‖</mo></mrow></mfrac><mrow><mi>d</mi><msup><mi>r</mi><mn>3</mn></msup><mo>′</mo></mrow><mo>.</mo></math>
</div>

Conducting walls, apertures, or image charges are not contained in
[this free-space convolution](#eq-coulomb-convolution).[^vico]

## Fields and Lorentz force

After solving the appropriate potential problem, use

<div id="eq-fields-from-potentials" class="dasc-equation" role="group" aria-label="Electric and magnetic fields from scalar and vector potentials">
<math display="block"><mi mathvariant="bold">E</mi><mo>=</mo><mo>−</mo><mo>∇</mo><mi>φ</mi><mo>−</mo><mfrac><mrow><mo>∂</mo><mi mathvariant="bold">A</mi></mrow><mrow><mo>∂</mo><mi>t</mi></mrow></mfrac><mo>,</mo><mspace width="1em"/><mi mathvariant="bold">B</mi><mo>=</mo><mo>∇</mo><mo>×</mo><mi mathvariant="bold">A</mi><mo>.</mo></math>
</div>

For a particle with signed charge q and velocity **v**, the exact Lorentz-force
law in that frame is

<div id="eq-lorentz-force" class="dasc-equation" role="group" aria-label="Lorentz force equals charge times electric field plus velocity cross magnetic field">
<math display="block"><mfrac><mrow><mi>d</mi><mi mathvariant="bold">p</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mi mathvariant="bold">F</mi><mo>=</mo><mi>q</mi><mrow><mo>(</mo><mi mathvariant="bold">E</mi><mo>+</mo><mi mathvariant="bold">v</mi><mo>×</mo><mi mathvariant="bold">B</mi><mo>)</mo></mrow><mo>.</mo></math>
</div>

The fields and particle state must be evaluated at a consistent time. For the
cavity problem, omitting −∂**A**/∂t removes the inductive part of the
longitudinal electric field.

## Canonical map boundary

A Lorentz-force update is not automatically the canonical map used by a beam
tracking code. A Hamiltonian split requires declared canonical coordinates,
independent variable, frame factors, and a force derived consistently from its
Hamiltonian. Current PyDASC documents a time-based reference map and a discrete
energy-consistent kick; DASC has not yet approved a universal normalization for
both TGF and cavity dynamics.

!!! danger "Decision required before a shared Hamiltonian equation"
    Do not copy the symbolic upstream factor `C_sc` into a public derivation as
    though it were frozen. Task 3 must map the TGF Hamiltonian and kick to the
    exact reviewed PyDASC convention. Task 4 must separately decide how causal
    cavity fields enter prescribed and self-consistent trajectories.

[^jackson]: J. D. Jackson, *Classical Electrodynamics*, 3rd ed., cited by the reviewed DASC cavity source.
[^vico]: F. Vico, L. Greengard, and M. Ferrando, “Fast convolution with free-space Green's functions,” *J. Comput. Phys.* 323 (2016), 191–203, [doi:10.1016/j.jcp.2016.07.028](https://doi.org/10.1016/j.jcp.2016.07.028).

