# DA/TPSA objects and coefficients

## Expansion contract

Choose m independent physical quantities θ = (θ₁,…,θ_m), a reference θ₀,
nonzero scales s_j with the same units, and dimensionless DA variables
δ_j = (θ_j−θ₀j)/s_j. A scalar output has the total-order-p TPSA representation

<div id="eq-tpsa-expansion" class="dasc-equation" role="group" aria-label="Multivariate total order truncated power series expansion">
<math display="block"><mi>f</mi><mo>(</mo><mi mathvariant="bold">δ</mi><mo>)</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mo>|</mo><mi mathvariant="bold">α</mi><mo>|</mo><mo>≤</mo><mi>p</mi></mrow><mrow/></munderover><msub><mi>f</mi><mi mathvariant="bold">α</mi></msub><msup><mi mathvariant="bold">δ</mi><mi mathvariant="bold">α</mi></msup><mo>+</mo><mi>O</mi><mo>(</mo><mo>‖</mo><mi mathvariant="bold">δ</mi><msup><mo>‖</mo><mrow><mi>p</mi><mo>+</mo><mn>1</mn></mrow></msup><mo>)</mo><mo>,</mo><mspace width="1em"/><msub><mi>N</mi><mtext>DA</mtext></msub><mo>=</mo><mrow><mo>(</mo><mfrac linethickness="0"><mrow><mi>m</mi><mo>+</mo><mi>p</mi></mrow><mi>p</mi></mfrac><mo>)</mo></mrow><mo>.</mo></math>
</div>

The final parenthesized expression denotes the binomial coefficient “m+p
choose p.” The multi-index α contains nonnegative exponents and |α| is their
sum. Products are multiplied as polynomials and terms above order p are
discarded after each operation. Therefore the object is a local model, not an
exact global function.

For the unit multi-index e_j,

<div id="eq-tpsa-coefficient-derivative" class="dasc-equation" role="group" aria-label="Conversion from normalized TPSA coefficients to physical derivatives">
<math display="block"><msub><mi>f</mi><msub><mi mathvariant="bold">e</mi><mi>j</mi></msub></msub><mo>=</mo><msub><mi>s</mi><mi>j</mi></msub><mfrac><mrow><mi>∂</mi><mi>f</mi></mrow><mrow><mi>∂</mi><msub><mi>θ</mi><mi>j</mi></msub></mrow></mfrac><msub><mo>|</mo><msub><mi mathvariant="bold">θ</mi><mn>0</mn></msub></msub><mo>,</mo><mspace width="1em"/><mfrac><mrow><mi>∂</mi><mi>f</mi></mrow><mrow><mi>∂</mi><msub><mi>θ</mi><mi>j</mi></msub></mrow></mfrac><msub><mo>|</mo><msub><mi mathvariant="bold">θ</mi><mn>0</mn></msub></msub><mo>=</mo><mfrac><msub><mi>f</mi><msub><mi mathvariant="bold">e</mi><mi>j</mi></msub></msub><msub><mi>s</mi><mi>j</mi></msub><mo>.</mo></math>
</div>

Higher coefficients include both scale factors and factorials. With the
ordinary Taylor convention used here, f_α = (s^α/α!) ∂^αf at θ₀. A library
using derivative-normalized coefficients must declare that different storage
convention at its interface.

## Analytically checkable example

Let y(θ) = θ², δ = (θ−θ₀)/s, and retain order two. Substitution gives

<div id="eq-tpsa-small-example" class="dasc-equation" role="group" aria-label="Second order TPSA example for a squared physical parameter">
<math display="block"><mi>y</mi><mo>(</mo><mi>δ</mi><mo>)</mo><mo>=</mo><msubsup><mi>θ</mi><mn>0</mn><mn>2</mn></msubsup><mo>+</mo><mn>2</mn><msub><mi>θ</mi><mn>0</mn></msub><mi>s</mi><mi>δ</mi><mo>+</mo><msup><mi>s</mi><mn>2</mn></msup><msup><mi>δ</mi><mn>2</mn></msup><mo>.</mo></math>
</div>

The linear coefficient is 2θ₀s, so dividing it by s recovers the physical
derivative 2θ₀. Twice the quadratic coefficient divided by s² recovers the
second derivative 2. This example is the minimum useful normalization test for
a TPSA interface.

## What may be independent

Do not mix unlike sensitivities without labels:

| Class | Examples | Typical smoothness boundary |
|---|---|---|
| Particle phase space | canonical coordinates of selected particles or tangent directions | loss, collision, stencil crossing |
| Distribution | Q, centroid, widths, correlations, shape coefficients | resampling, support/topology change |
| Accelerator | magnet strengths, RF phase/amplitude, element lengths | branch or element-model change |
| Geometry | cavity radii/length, aperture size, grid domain | remeshing, mode reordering, cutoff feasibility |
| Solver controls | step size, grid spacing, mode count, tolerance | usually discrete choices, not physical derivatives |

Distribution derivatives should use fixed normalized samples or a quiet-start
reparameterization so that a parameter change transforms the same sample
rather than drawing a different random ensemble.[^qiang]

[^qiang]: J. Qiang, “Differentiable self-consistent space-charge simulation for accelerator design,” *Phys. Rev. Accel. Beams* 26, 024601 (2023), [doi:10.1103/PhysRevAccelBeams.26.024601](https://doi.org/10.1103/PhysRevAccelBeams.26.024601).
