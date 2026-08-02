# TGF fields, particle forces, and kicks

The free-space solve produces a grid potential. Two different derivatives of
that potential are useful, but they answer different questions: a spectral
grid field is an accurate field observable, while a particle force intended for
a canonical kick must be the derivative of the same discrete interaction energy
used by the algorithm.

## Spectral grid field

For component j, PyDASC evaluates the comparison field directly in Fourier
space as

<div id="eq-tgf-direct-field" class="dasc-equation" role="group" aria-label="Spectral component of the electric field">
<math display="block"><msub><mover><mi>E</mi><mo>^</mo></mover><mi>j</mi></msub><mo>(</mo><mi mathvariant="bold">k</mi><mo>)</mo><mo>=</mo><mo>−</mo><mi>i</mi><msub><mi>k</mi><mi>j</mi></msub><msub><mover><mi>K</mi><mo>^</mo></mover><mi>h</mi></msub><mo>(</mo><mi mathvariant="bold">k</mi><mo>)</mo><msub><mover><mi>ρ</mi><mo>^</mo></mover><mi>h</mi></msub><mo>(</mo><mi mathvariant="bold">k</mi><mo>)</mo><mo>/</mo><msub><mi>ε</mi><mn>0</mn></msub><mo>.</mo></math>
</div>

Here K̂_h is the stored, volume-weighted discrete free-space kernel. The zero
derivative mode and each unpaired Nyquist derivative mode are set explicitly to
zero so that the inverse transform is real and follows the declared discrete
operator. This field is valuable for analytic field-error studies. Depositing a
density, evaluating [this equation](#eq-tgf-direct-field), and gathering the
result to particles does **not** by itself establish an energy-consistent or
symplectic particle map.

## Discrete interaction energy

Let K_h denote the unscaled symmetric discrete convolution operator, let ΔV be
the cell volume, and define φ = K_h ρ/ε₀. The discrete interaction energy is

<div id="eq-tgf-discrete-energy" class="dasc-equation" role="group" aria-label="Discrete space charge interaction energy">
<math display="block"><msub><mi>U</mi><mi>h</mi></msub><mo>(</mo><mi mathvariant="bold">q</mi><mo>)</mo><mo>=</mo><mfrac><mrow><mi>Δ</mi><mi>V</mi></mrow><mrow><mn>2</mn><msub><mi>ε</mi><mn>0</mn></msub></mrow></mfrac><msup><mi mathvariant="bold">ρ</mi><mi>T</mi></msup><msub><mi>K</mi><mi>h</mi></msub><mi mathvariant="bold">ρ</mi><mo>=</mo><mfrac><mrow><mi>Δ</mi><mi>V</mi></mrow><mn>2</mn></mfrac><msup><mi mathvariant="bold">ρ</mi><mi>T</mi></msup><mi mathvariant="bold">φ</mi><mo>.</mo></math>
</div>

The factor 1/ε₀ appears exactly once: it is already present in φ returned by
`FreeSpaceVGF.solve`. If D = ∂ρ/∂q is the Jacobian of the declared deposition
map, symmetry of K_h gives the particle force

<div id="eq-tgf-energy-force" class="dasc-equation" role="group" aria-label="Particle force as the negative gradient of discrete interaction energy">
<math display="block"><mi mathvariant="bold">F</mi><mo>(</mo><mi mathvariant="bold">q</mi><mo>)</mo><mo>=</mo><mo>−</mo><mfrac><mrow><mi>∂</mi><msub><mi>U</mi><mi>h</mi></msub></mrow><mrow><mi>∂</mi><mi mathvariant="bold">q</mi></mrow></mfrac><mo>=</mo><mo>−</mo><mi>Δ</mi><mi>V</mi><msup><mi>D</mi><mi>T</mi></msup><mi mathvariant="bold">φ</mi><mo>.</mo></math>
</div>

This transpose-Jacobian expression, rather than an independently gathered grid
field, is the force implemented by the reviewed discrete Hamiltonian path.

## Kick map and canonical boundary

For a time step Δt in the current time-based PyDASC convention, the reduced
kick is

<div id="eq-tgf-kick" class="dasc-equation" role="group" aria-label="Canonical momentum kick from the energy-consistent force">
<math display="block"><msup><mi mathvariant="bold">q</mi><mo>+</mo></msup><mo>=</mo><msup><mi mathvariant="bold">q</mi><mo>−</mo></msup><mo>,</mo><mspace width="1em"/><msup><mi mathvariant="bold">p</mi><mo>+</mo></msup><mo>=</mo><msup><mi mathvariant="bold">p</mi><mo>−</mo></msup><mo>+</mo><mi>Δ</mi><mi>t</mi><mi mathvariant="bold">F</mi><mo>(</mo><msup><mi mathvariant="bold">q</mi><mo>−</mo></msup><mo>)</mo><mo>.</mo></math>
</div>

This map is a canonical kick only when **q** and **p** are a declared canonical
pair and **F** is the exact gradient of [the discrete scalar energy](#eq-tgf-discrete-energy).
That statement does not prove that an entire tracking composition is
symplectic; the external map, splitting, frame changes, and numerical
derivatives require separate checks.[^qiang]

PyDASC presently documents a time-based rest-frame solve and the corresponding
laboratory scaling in its imported [conventions](pydasc/reference/conventions.md).
A general DASC tracking-coordinate normalization is not yet frozen, so this page
does not invent a universal frame factor or longitudinal canonical kick.

## Differentiability contract

The chain ρ(**q**) → φ → U_h → **F** is differentiable only to the degree that
every declared operator is differentiable. The FFT convolution is linear.
Gaussian deposition is globally smooth; the reviewed cubic B-spline path is
locally differentiable only while its frozen stencil remains valid. A particle
crossing a stencil boundary leaves that trust cell and requires relinearization.
Differentiability of a reported observable also includes its gather or reduction
operator; it is not inherited merely because the potential solve is smooth.

[^qiang]: J. Qiang, R. D. Ryne, S. Habib, and V. Decyk, “An object-oriented parallel particle-in-cell code for beam dynamics simulation in linear accelerators,” *J. Comput. Phys.* 163 (2000), 434–451, [doi:10.1006/jcph.2000.6570](https://doi.org/10.1006/jcph.2000.6570).
