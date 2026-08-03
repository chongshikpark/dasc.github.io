# Finite-cavity problem

## Geometry and model boundary

Use laboratory/cavity coordinates (r,θ,z,t). The axisymmetric cavity has radius
a and length L:

<div id="eq-cavity-domains" class="dasc-equation" role="group" aria-label="Finite cavity and downstream circular pipe domains">
<math display="block"><msub><mi>Ω</mi><mtext>cav</mtext></msub><mo>=</mo><mo>{</mo><mn>0</mn><mo>≤</mo><mi>r</mi><mo>&lt;</mo><mi>a</mi><mo>,</mo><mspace width="0.5em"/><mn>0</mn><mo>&lt;</mo><mi>z</mi><mo>&lt;</mo><mi>L</mi><mo>}</mo><mo>,</mo><mspace width="1em"/><msub><mi>Ω</mi><mtext>pipe</mtext></msub><mo>=</mo><mo>{</mo><mn>0</mn><mo>≤</mo><mi>r</mi><mo>&lt;</mo><mi>b</mi><mo>,</mo><mspace width="0.5em"/><mi>z</mi><mo>&gt;</mo><mi>L</mi><mo>}</mo><mo>.</mo></math>
</div>

The cathode is at z = 0. The end plate at z = L contains a centered aperture of
radius b. All metal is initially ideal PEC. A specified RF field determines a
baseline trajectory z_b(t); the equations below derive only the beam-generated
self-field. Updating the trajectory from RF plus self-field is a later
self-consistency step, not part of the prescribed-trajectory solution.

## Source and continuity

For the reviewed zero-longitudinal-thickness slice with signed charge Q and
normalized radial profile f,

<div id="eq-cavity-source" class="dasc-equation" role="group" aria-label="Axisymmetric moving slice charge and longitudinal current densities">
<math display="block"><mi>ρ</mi><mo>(</mo><mi>r</mi><mo>,</mo><mi>z</mi><mo>,</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>Q</mi><mi>f</mi><mo>(</mo><mi>r</mi><mo>)</mo><mi>δ</mi><mo>[</mo><mi>z</mi><mo>−</mo><msub><mi>z</mi><mi>b</mi></msub><mo>(</mo><mi>t</mi><mo>)</mo><mo>]</mo><mo>,</mo><mspace width="1em"/><msub><mi>J</mi><mi>z</mi></msub><mo>=</mo><mi>ρ</mi><msub><mi>v</mi><mi>b</mi></msub><mo>,</mo><mspace width="0.5em"/><msub><mi>v</mi><mi>b</mi></msub><mo>=</mo><msub><mover><mi>z</mi><mo>˙</mo></mover><mi>b</mi></msub><mo>.</mo></math>
</div>

The normalization 2π∫₀ʳᵇ r f(r)dr = 1 makes ∫ρ d³r = Q. With J = J_z **e**_z,
the source satisfies ∂ρ/∂t + ∂J_z/∂z = 0. Q is signed; Q &lt; 0 for electrons.
Finite bunch length, transverse current, nonaxisymmetric structure, material
loss, and RF back-reaction are outside this baseline.

## Gauge, wave equations, and initial data

In the [shared Lorenz-gauge convention](dasc-potentials-fields-dynamics.md#eq-lorenz-gauge),
with **A** = A_z **e**_z,

<div id="eq-cavity-wave-equations" class="dasc-equation" role="group" aria-label="Lorenz gauge scalar and longitudinal vector potential wave equations">
<math display="block"><mo>(</mo><msup><mo>∇</mo><mn>2</mn></msup><mo>−</mo><mfrac><mn>1</mn><msup><mi>c</mi><mn>2</mn></msup></mfrac><msubsup><mo>∂</mo><mi>t</mi><mn>2</mn></msubsup><mo>)</mo><mi>φ</mi><mo>=</mo><mo>−</mo><mfrac><mi>ρ</mi><msub><mi>ε</mi><mn>0</mn></msub></mfrac><mo>,</mo><mspace width="1em"/><mo>(</mo><msup><mo>∇</mo><mn>2</mn></msup><mo>−</mo><mfrac><mn>1</mn><msup><mi>c</mi><mn>2</mn></msup></mfrac><msubsup><mo>∂</mo><mi>t</mi><mn>2</mn></msubsup><mo>)</mo><msub><mi>A</mi><mi>z</mi></msub><mo>=</mo><mo>−</mo><msub><mi>μ</mi><mn>0</mn></msub><msub><mi>J</mi><mi>z</mi></msub><mo>.</mo></math>
</div>

The retarded solution assumes vanishing self-field initial data before the
source is introduced, or explicitly supplied compatible initial modal data.
Changing the initial data adds a homogeneous cavity field.

## Closed-reference PEC conditions

For the closed reference cavity, the gauge-compatible potential conditions are

<div id="eq-cavity-potential-boundaries" class="dasc-equation" role="group" aria-label="Closed cavity scalar Dirichlet and longitudinal vector Neumann boundary conditions">
<math display="block"><mi>φ</mi><mo>(</mo><mi>a</mi><mo>,</mo><mi>z</mi><mo>,</mo><mi>t</mi><mo>)</mo><mo>=</mo><msub><mi>A</mi><mi>z</mi></msub><mo>(</mo><mi>a</mi><mo>,</mo><mi>z</mi><mo>,</mo><mi>t</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo><mspace width="1em"/><mi>φ</mi><mo>(</mo><mi>r</mi><mo>,</mo><mn>0</mn><mo>,</mo><mi>t</mi><mo>)</mo><mo>=</mo><mi>φ</mi><mo>(</mo><mi>r</mi><mo>,</mo><mi>L</mi><mo>,</mo><mi>t</mi><mo>)</mo><mo>=</mo><mn>0</mn><mo>,</mo><mspace width="1em"/><msub><mo>∂</mo><mi>z</mi></msub><msub><mi>A</mi><mi>z</mi></msub><mo>|</mo><msub><mrow/><mrow><mi>z</mi><mo>=</mo><mn>0</mn><mo>,</mo><mi>L</mi></mrow></msub><mo>=</mo><mn>0</mn><mo>.</mo></math>
</div>

Thus φ uses axial Dirichlet modes and A_z uses axial Neumann modes. Setting
A_z = 0 on the end plates would silently change this longitudinal-current
formulation.[^hess]

[^hess]: M. Hess, C. S. Park, and D. Bolton, “Green's function based space-charge field solver for electron source simulations,” *Phys. Rev. ST Accel. Beams* 10, 054201 (2007), [doi:10.1103/PhysRevSTAB.10.054201](https://doi.org/10.1103/PhysRevSTAB.10.054201).
