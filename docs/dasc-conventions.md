# Frames, coordinates, units, and conventions

This page freezes only conventions supported by the current reviewed DASC and
PyDASC sources. A symbol is local to the model whose domain is stated.

## Symbols and SI units

| Symbol | Meaning | SI unit |
| --- | --- | --- |
| <span lang="en">t</span> | laboratory or cavity time | s |
| **r** = (x,y,z) | Cartesian observation position | m |
| (r,θ,z) | cylindrical cavity coordinates | m, rad, m |
| ρ(**r**,t) | signed charge density | C m⁻³ |
| **J**(**r**,t) | signed current density | A m⁻² |
| Q | signed total source charge; Q &lt; 0 for electrons | C |
| φ, **A** | scalar and vector potentials | V, V s m⁻¹ |
| **E**, **B** | electric field and magnetic flux density | V m⁻¹, T |
| ε₀, μ₀, c | vacuum constants, with c² = 1/(ε₀μ₀) | F m⁻¹, H m⁻¹, m s⁻¹ |
| q, m | signed particle charge and rest mass | C, kg |
| **F** | Lorentz force | N |

Bold symbols denote vectors. A prime on **r**′ denotes a source coordinate, not
a derivative. Subscripts `sc`, `RF`, `lab`, and `rest` mean space charge,
prescribed radio-frequency field, laboratory frame, and beam-rest frame.

## Sign and source conventions

Charge and current densities are signed. For an electron bunch, Q &lt; 0. The
total charge definition is the exact normalization

<div id="eq-total-charge" class="dasc-equation" role="group" aria-label="Total charge equals the volume integral of charge density">
<math display="block"><mi>Q</mi><mo>=</mo><msub><mo>∫</mo><mi>V</mi></msub><mi>ρ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>,</mo><mi>t</mi><mo>)</mo><mrow><mi>d</mi><mi>V</mi></mrow><mo>.</mo></math>
</div>

The field definitions are **E** = −∇φ − ∂**A**/∂t and **B** = ∇×**A**.[^jackson]
Therefore the force on a particle is q(**E** + **v**×**B**); the sign of q must
not be hidden in a field convention.

## Fourier convention for the TGF branch

For a sufficiently integrable scalar field f on ℝ³, DASC uses

<div id="eq-fourier-pair" class="dasc-equation" role="group" aria-label="Forward and inverse Fourier transform pair">
<math display="block"><mover><mi>f</mi><mo>^</mo></mover><mo>(</mo><mi mathvariant="bold">k</mi><mo>)</mo><mo>=</mo><msup><mo>∫</mo><msup><mi mathvariant="normal">ℝ</mi><mn>3</mn></msup></msup><mi>f</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo><msup><mi>e</mi><mrow><mo>−</mo><mi>i</mi><mi mathvariant="bold">k</mi><mo>·</mo><mi mathvariant="bold">r</mi></mrow></msup><mrow><msup><mi>d</mi><mn>3</mn></msup><mi mathvariant="bold">r</mi></mrow><mo>,</mo><mspace width="1em"/><mi>f</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><msup><mrow><mo>(</mo><mn>2</mn><mi>π</mi><mo>)</mo></mrow><mn>3</mn></msup></mfrac><msup><mo>∫</mo><msup><mi mathvariant="normal">ℝ</mi><mn>3</mn></msup></msup><mover><mi>f</mi><mo>^</mo></mover><mo>(</mo><mi mathvariant="bold">k</mi><mo>)</mo><msup><mi>e</mi><mrow><mi>i</mi><mi mathvariant="bold">k</mi><mo>·</mo><mi mathvariant="bold">r</mi></mrow></msup><mrow><msup><mi>d</mi><mn>3</mn></msup><mi mathvariant="bold">k</mi></mrow><mo>.</mo></math>
</div>

The discrete FFT scaling is documented in the reviewed
[PyDASC conventions](pydasc/reference/conventions.md). A continuous identity
must not be silently substituted for a discrete normalization.

## Frames and coordinates

The cavity formulation is written in laboratory/cavity coordinates (r,θ,z,t),
with a prescribed reference trajectory z_b(t) during the baseline field solve.
The TGF branch solves an electrostatic problem in the frame declared by its
tracking model; transforming that field to tracking coordinates is a separate
modeling step.

!!! danger "Open frame decision"
    DASC has not approved one general Lorentz-transform and canonical-coordinate
    convention shared by both formulations. Current PyDASC tracking uses a
    documented paraxial equal-time canonical scaling, explicitly **not** a
    general Lorentz transform. Until DASC freezes its independent variable,
    reference momentum, metric convention, and canonical normalization, later
    pages must link to the model-specific convention instead of inventing one.

## Dimensional checks

- ∫ρ d³r has unit C, matching Q in [the charge normalization](#eq-total-charge).
- ∂ρ/∂t and ∇·**J** both have unit A m⁻³.
- −ρ/ε₀ has unit V m⁻², matching ∇²φ.
- q**E** and q**v**×**B** both have unit N.

[^jackson]: J. D. Jackson, *Classical Electrodynamics*, 3rd ed. This primary reference is cited by the reviewed DASC cavity source for potentials, fields, gauges, and conducting boundaries.
