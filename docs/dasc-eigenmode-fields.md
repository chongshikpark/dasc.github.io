# Analytical cavity fields and particle coupling

## Exact modal differentiation

Define I_np^φ and I_np^A as the retarded sine convolutions appearing in φ and
A_z, and define C_np^A = ∂I_np^A/∂t. Because the sine kernel vanishes at its
upper integration limit, C_np^A is obtained by replacing its sine factor divided
by ω_np^N with a cosine factor. No finite difference of the potential is needed.

The field definitions give

<div id="eq-cavity-fields" class="dasc-equation" role="group" aria-label="Closed cavity radial electric longitudinal electric and azimuthal magnetic fields">
<math display="block"><msubsup><mi>E</mi><mi>r</mi><mn>0</mn></msubsup><mo>=</mo><mo>−</mo><mfrac><mi>Q</mi><msub><mi>ε</mi><mn>0</mn></msub></mfrac><mo>∑</mo><msubsup><mi>ψ</mi><mi>n</mi><mo>′</mo></msubsup><msub><mi>u</mi><mi>p</mi></msub><msub><mi>F</mi><mi>n</mi></msub><msubsup><mi>I</mi><mrow><mi>n</mi><mi>p</mi></mrow><mi>φ</mi></msubsup><mo>,</mo><mspace width="1em"/><msubsup><mi>E</mi><mi>z</mi><mn>0</mn></msubsup><mo>=</mo><mo>−</mo><mfrac><mi>Q</mi><msub><mi>ε</mi><mn>0</mn></msub></mfrac><mo>∑</mo><msub><mi>ψ</mi><mi>n</mi></msub><msubsup><mi>u</mi><mi>p</mi><mo>′</mo></msubsup><msub><mi>F</mi><mi>n</mi></msub><msubsup><mi>I</mi><mrow><mi>n</mi><mi>p</mi></mrow><mi>φ</mi></msubsup><mo>−</mo><msub><mi>μ</mi><mn>0</mn></msub><mi>Q</mi><mo>∑</mo><msub><mi>ψ</mi><mi>n</mi></msub><msub><mi>v</mi><mi>p</mi></msub><msub><mi>F</mi><mi>n</mi></msub><msubsup><mi>C</mi><mrow><mi>n</mi><mi>p</mi></mrow><mi>A</mi></msubsup><mo>,</mo><mspace width="1em"/><msubsup><mi>B</mi><mi>θ</mi><mn>0</mn></msubsup><mo>=</mo><mo>−</mo><msub><mi>μ</mi><mn>0</mn></msub><mi>Q</mi><mo>∑</mo><msubsup><mi>ψ</mi><mi>n</mi><mo>′</mo></msubsup><msub><mi>v</mi><mi>p</mi></msub><msub><mi>F</mi><mi>n</mi></msub><msubsup><mi>I</mi><mrow><mi>n</mi><mi>p</mi></mrow><mi>A</mi></msubsup><mo>.</mo></math>
</div>

The first two sums use n,p ≥ 1. The vector-potential sums use n ≥ 1,p ≥ 0.
The inductive term −∂A_z/∂t in E_z is essential; omitting it changes the
magnitude, symmetry, and relativistic behavior. The analytic ψ′_n and u′_p
enforce the same modal conventions as the potentials.

## Regularity and signs

Since J₁(0) = 0, ψ′_n(0) = 0, hence E_r and B_θ vanish on axis. Tangential
electric field vanishes on the closed PEC walls when the converged modal sums
and compatible potential conditions are used. Individual truncated sums can
show wall or source-edge ringing and must be assessed by residuals.

With Q &lt; 0, the electric field points toward an isolated electron bunch:
E_r &lt; 0 for r &gt; 0 near the bunch, E_z &lt; 0 ahead, and E_z &gt; 0 behind. The
cathode, end wall, acceleration, and aperture break exact front–back
antisymmetry. Normalize plots with a positive scale such as
|Q|/(4πε₀a²), or explicitly state when a signed scale reverses the plotted sign.

## Force and self-consistent dynamics

The field acting on a particle of signed charge q is

<div id="eq-cavity-lorentz-force" class="dasc-equation" role="group" aria-label="Particle Lorentz force from radio frequency and cavity self fields">
<math display="block"><mi mathvariant="bold">F</mi><mo>=</mo><mi>q</mi><mo>{</mo><msub><mi mathvariant="bold">E</mi><mtext>RF</mtext></msub><mo>+</mo><msub><mi mathvariant="bold">E</mi><mtext>sc</mtext></msub><mo>+</mo><mi mathvariant="bold">v</mi><mo>×</mo><mo>[</mo><msub><mi mathvariant="bold">B</mi><mtext>RF</mtext></msub><mo>+</mo><msub><mi mathvariant="bold">B</mi><mtext>sc</mtext></msub><mo>]</mo><mo>}</mo><mo>.</mo></math>
</div>

In the baseline derivation, z_b(t) and v_b(t) are prescribed inputs to the
retarded convolution. A self-consistent calculation must update particle
trajectories and rebuild the charge/current history while preserving continuity.
The independent variable, canonical momentum, interpolation, time integration,
and iteration strategy are not yet frozen for this DASC branch. Consequently,
this page derives a physical force but does not claim a canonical or symplectic
particle map.

Differentiation through this pipeline requires smooth source projection, causal
quadrature, modal evaluation, aperture solve, field evaluation, particle
coupling, and observable reduction. Mode-set changes, branch-dependent
quadrature, particle loss, aperture interception, and resonant degeneracy are
potential nondifferentiable points; the [DA/TPSA eigenmode pipeline](dasc-da-pipelines.md#causal-eigenmode-branch)
states the differentiability conditions and validation boundary separately.
