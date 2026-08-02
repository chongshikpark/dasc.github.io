# TGF/Vico–Greengard–Ferrando formulation

## Physical-space truncation

Let D be the largest required separation between any source point and target
point in Ω. Define the truncated kernel Gᴸ(**r**) = G(**r**) for ‖**r**‖ &lt; L
and zero otherwise. If L &gt; D, replacing G by Gᴸ leaves every required value of
[the physical convolution](dasc-tgf-free-space-poisson.md#eq-tgf-green-convolution)
unchanged. Truncation is therefore an exact geometric device on Ω, not a claim
that the Coulomb interaction is physically finite range.

For PyDASC's twofold online padding of a rectangular domain with lengths
(Lₓ,Lᵧ,L_z), the reviewed admissibility condition is

<div id="eq-tgf-cutoff-condition" class="dasc-equation" role="group" aria-label="Cutoff radius is greater than the domain diameter and less than twice the shortest domain length">
<math display="block"><msqrt><mrow><msubsup><mi>L</mi><mi>x</mi><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>L</mi><mi>y</mi><mn>2</mn></msubsup><mo>+</mo><msubsup><mi>L</mi><mi>z</mi><mn>2</mn></msubsup></mrow></msqrt><mo>&lt;</mo><msub><mi>L</mi><mtext>cut</mtext></msub><mo>&lt;</mo><mn>2</mn><mo>min</mo><mo>(</mo><msub><mi>L</mi><mi>x</mi></msub><mo>,</mo><msub><mi>L</mi><mi>y</mi></msub><mo>,</mo><msub><mi>L</mi><mi>z</mi></msub><mo>)</mo><mo>.</mo></math>
</div>

An excessively anisotropic box may admit no such cutoff and requires a different
padding policy rather than a bypassed check.

## Analytic spectral kernel

With the [frozen Fourier convention](dasc-conventions.md#eq-fourier-pair), the
three-dimensional truncated Coulomb kernel has transform

<div id="eq-tgf-spectrum" class="dasc-equation" role="group" aria-label="Fourier transform of the spherically truncated Coulomb kernel">
<math display="block"><msup><mover><mi>G</mi><mo>^</mo></mover><mi>L</mi></msup><mo>(</mo><mi mathvariant="bold">k</mi><mo>)</mo><mo>=</mo><mn>2</mn><msup><mrow><mo>[</mo><mfrac><mrow><mi>sin</mi><mo>(</mo><mi>L</mi><mo>‖</mo><mi mathvariant="bold">k</mi><mo>‖</mo><mo>/</mo><mn>2</mn><mo>)</mo></mrow><mrow><mo>‖</mo><mi mathvariant="bold">k</mi><mo>‖</mo></mrow></mfrac><mo>]</mo></mrow><mn>2</mn></msup><mo>,</mo><mspace width="1em"/><msup><mover><mi>G</mi><mo>^</mo></mover><mi>L</mi></msup><mo>(</mo><mn>0</mn><mo>)</mo><mo>=</mo><mfrac><msup><mi>L</mi><mn>2</mn></msup><mn>2</mn></mfrac><mo>.</mo></math>
</div>

The finite zero-mode value is the continuous limit, so no singular division is
introduced at **k** = 0. This analytic regularization is the central device in
the Vico–Greengard–Ferrando construction.[^vico]

## Discrete aperiodic convolution

PyDASC's reviewed construction is:

1. freeze a uniform grid with equal physical spacing on all axes;
2. validate [the cutoff interval](#eq-tgf-cutoff-condition);
3. sample the analytic spectrum on an auxiliary grid and inverse-transform it
   to a volume-weighted discrete kernel;
4. retain the kernel needed for a twofold padded online convolution;
5. zero-pad ρ, FFT it, multiply by the stored kernel spectrum, inverse FFT, and
   crop Ω; and
6. apply 1/ε₀ exactly once in `FreeSpaceVGF.solve`.

NumPy's inverse FFT normalization is already part of the construction; no extra
cell-volume or FFT-size factor belongs in the online solve.

For M padded grid values, the repeated solve is O(M log M) time and O(M) storage,
up to constant factors for real/complex work arrays. Kernel setup, cached
spectrum, density coefficients, and simultaneous field components must be
reported separately in memory measurements.

## Failure modes

Invalid cutoff geometry, insufficient source containment, periodic wraparound,
duplicated or missing 1/ε₀ scaling, inconsistent axis order, undersampled source
shape, and nonconverged domain/grid choices can all produce a plausible-looking
but wrong field. [Verification](dasc-tgf-verification.md) must vary these controls
independently.

[^vico]: F. Vico, L. Greengard, and M. Ferrando, “Fast convolution with free-space Green's functions,” *J. Comput. Phys.* 323 (2016), 191–203, [doi:10.1016/j.jcp.2016.07.028](https://doi.org/10.1016/j.jcp.2016.07.028).
