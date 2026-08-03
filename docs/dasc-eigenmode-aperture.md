# Aperture coupling and downstream pipe

## Mode matching is the primary formulation

The closed-cavity field incident on the aperture is the source for a frequency-
domain scattering problem. On the cavity side, write the source field plus
reflected cavity modes with amplitudes A_ν. In the pipe, write outgoing or
evanescent circular-waveguide modes with amplitudes B_μ. Here ν labels cavity
modes and μ labels pipe modes; neither is the radial index n or axial index p of
the closed-cavity derivation.

At z = L, Maxwell's interface conditions require

<div id="eq-aperture-matching" class="dasc-equation" role="group" aria-label="Tangential field matching across the aperture and metallic annulus">
<math display="block"><msubsup><mi mathvariant="bold">E</mi><mi>t</mi><mi>I</mi></msubsup><mo>=</mo><msubsup><mi mathvariant="bold">E</mi><mi>t</mi><mrow><mi>I</mi><mi>I</mi></mrow></msubsup><mo>,</mo><mspace width="0.5em"/><msubsup><mi mathvariant="bold">H</mi><mi>t</mi><mi>I</mi></msubsup><mo>=</mo><msubsup><mi mathvariant="bold">H</mi><mi>t</mi><mrow><mi>I</mi><mi>I</mi></mrow></msubsup><mspace width="0.5em"/><mo>(</mo><mn>0</mn><mo>≤</mo><mi>r</mi><mo>&lt;</mo><mi>b</mi><mo>)</mo><mo>,</mo><mspace width="1em"/><msubsup><mi mathvariant="bold">E</mi><mi>t</mi><mi>I</mi></msubsup><mo>=</mo><mn>0</mn><mspace width="0.5em"/><mo>(</mo><mi>b</mi><mo>&lt;</mo><mi>r</mi><mo>&lt;</mo><mi>a</mi><mo>)</mo><mo>.</mo></math>
</div>

Projection onto aperture basis functions produces overlap matrices such as
C_νμ = ∫_aperture **e**^I_ν,t·(**e**^II_μ,t)* dS and a block linear system for
A_ν and B_μ. The pipe longitudinal propagation constant distinguishes
propagating modes from evanescent modes. The radiation condition selects waves
outgoing as z → ∞; evanescent modes select the decaying branch. Both classes are
needed near the aperture until field continuity and observables converge.[^collin]

This formulation supports finite b/a, repeated cavity reflection, transmitted
power, and recovery of the closed cavity as b → 0. The reviewed source specifies
the formulation and validation program; it does not supply an approved complete
implementation or result artifact.

## Small-aperture benchmark

Bethe-type theory replaces an electrically small aperture in a sufficiently
thin PEC screen by normal electric and tangential magnetic polarizations. Its
controlled scale conditions include

<div id="eq-small-aperture-limit" class="dasc-equation" role="group" aria-label="Small aperture asymptotic scale conditions">
<math display="block"><mi>k</mi><mi>b</mi><mo>≪</mo><mn>1</mn><mo>,</mo><mspace width="1em"/><mfrac><mi>b</mi><mi>a</mi></mfrac><mo>≪</mo><mn>1</mn><mo>.</mo></math>
</div>

Screen thickness and polarizability convention must also be declared, and the
point-dipole field is an outer solution not evaluated at the aperture point.[^bethe]

For a centered axisymmetric source, regularity gives H_θ(0,L,t) = 0 and the
azimuthal unit vector is undefined at r = 0. Therefore a nonzero single
azimuthal magnetic point dipole at the center is not the leading perturbation.
The generally finite normal field E_z(0,L,t) can drive a normal electric
polarization; distributed magnetic polarization may enter through higher
multipoles. A geometry with b/a = 0.4 is not asymptotically small, so the
small-hole model is a limiting comparison, not its quantitative primary model.

## Time-domain reconstruction

Frequency blocks must be inverse transformed with a causal prescription. A
frequency sweep or modal truncation that omits poles, uses an incoming pipe
branch, or excludes needed evanescent modes can violate arrival time, interface
continuity, or energy flow even when individual field plots look smooth.

[^collin]: R. E. Collin, *Field Theory of Guided Waves*, 2nd ed. (IEEE Press, 1991).
[^bethe]: H. A. Bethe, “Theory of diffraction by small holes,” *Physical Review* 66 (1944), 163–182, [doi:10.1103/PhysRev.66.163](https://doi.org/10.1103/PhysRev.66.163).
