# Free-space Poisson problem

## Domain and assumptions

Let Ω be a rectangular physical domain containing the support of a sufficiently
regular signed charge density ρ(**r**). The TGF branch assumes an electrostatic
or approved quasistatic solve in the model-specific frame. Conducting-wall and
retardation effects are absent from this boundary-value problem.

The potential is defined on all of ℝ³ by

<div id="eq-tgf-poisson" class="dasc-equation" role="group" aria-label="Free-space Poisson equation and decay condition">
<math display="block"><msup><mo>∇</mo><mn>2</mn></msup><mi>φ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo><mo>=</mo><mo>−</mo><mfrac><mrow><mi>ρ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo></mrow><msub><mi>ε</mi><mn>0</mn></msub></mfrac><mo>,</mo><mspace width="1em"/><mi>φ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo><mo>→</mo><mn>0</mn><mspace width="0.5em"/><mtext>as</mtext><mspace width="0.5em"/><mo>‖</mo><mi mathvariant="bold">r</mi><mo>‖</mo><mo>→</mo><mo>∞</mo><mo>.</mo></math>
</div>

The sign follows the [shared conventions](dasc-conventions.md). Its dimensional
check is V m⁻² on both sides.

## Green-function solution

The free-space Coulomb Green function is G(**r**) = 1/(4π‖**r**‖). Therefore

<div id="eq-tgf-green-convolution" class="dasc-equation" role="group" aria-label="Free-space Coulomb convolution for potential">
<math display="block"><mi>φ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><msub><mi>ε</mi><mn>0</mn></msub></mfrac><msup><mo>∫</mo><msup><mi mathvariant="normal">ℝ</mi><mn>3</mn></msup></msup><mfrac><mrow><mi>ρ</mi><mo>(</mo><mi mathvariant="bold">r</mi><mo>′</mo><mo>)</mo></mrow><mrow><mn>4</mn><mi>π</mi><mo>‖</mo><mi mathvariant="bold">r</mi><mo>−</mo><mi mathvariant="bold">r</mi><mo>′</mo><mo>‖</mo></mrow></mfrac><mrow><mi>d</mi><msup><mi>r</mi><mn>3</mn></msup><mo>′</mo></mrow><mo>.</mo></math>
</div>

This is an aperiodic convolution. The 1/‖**r**‖ singularity is integrable in
three dimensions but cannot be sampled naively at zero separation.

## Why a periodic FFT is not the target problem

A discrete Fourier transform represents periodic data. Directly multiplying a
periodic transform of ρ by an unmodified Coulomb kernel produces interactions
with periodic replicas and an ill-defined sampled origin. Enlarging the box may
reduce image error but does not define a controlled free-space algorithm by
itself. The TGF construction instead modifies the kernel outside the required
source–target separations, obtains an analytic nonsingular Fourier transform,
and uses zero padding to compute the required aperiodic convolution.[^vico]

## Applicability

The source support, observation region, and chosen cutoff must fit the geometric
condition on the [TGF formulation page](dasc-tgf-formulation.md#eq-tgf-cutoff-condition).
If nearby conductors materially change the field, use a boundary-aware solver.

[^vico]: F. Vico, L. Greengard, and M. Ferrando, “Fast convolution with free-space Green's functions,” *J. Comput. Phys.* 323 (2016), 191–203, [doi:10.1016/j.jcp.2016.07.028](https://doi.org/10.1016/j.jcp.2016.07.028).

