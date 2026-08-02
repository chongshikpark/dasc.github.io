# Self-consistent space charge

## Source conservation

A physically admissible signed charge/current source obeys local charge
conservation:

<div id="eq-continuity" class="dasc-equation" role="group" aria-label="Continuity equation: time derivative of charge density plus divergence of current density equals zero">
<math display="block"><mfrac><mrow><mo>∂</mo><mi>ρ</mi></mrow><mrow><mo>∂</mo><mi>t</mi></mrow></mfrac><mo>+</mo><mo>∇</mo><mo>·</mo><mi mathvariant="bold">J</mi><mo>=</mo><mn>0</mn><mo>.</mo></math>
</div>

Integrating [the continuity equation](#eq-continuity) over a fixed volume shows
that charge changes only through boundary flux. A deposition or modal source
that violates this identity changes the physical problem, even if its field
solver converges numerically.

## Prescribed source versus self-consistent update

A **prescribed-source solve** evaluates fields from a source history fixed in
advance. The baseline cavity derivation uses a prescribed z_b(t) and
J_z = ρ dz_b/dt. A **self-consistent solve** closes the feedback loop:

1. represent particles or a source distribution at the current state;
2. construct signed ρ and, for an electromagnetic model, **J**;
3. solve the stated field problem with its boundary and initial conditions;
4. evaluate the force or Hamiltonian contribution consistently;
5. update the particle/source state; and
6. repeat at the model's declared step, slice, or iteration boundary.

Holding the source fixed during step 3 can be a discretization choice. Holding
it fixed for the whole calculation is a prescribed-source model, not a
self-consistent simulation.

## Discrete particle source

For macroparticles with signed charges qₚ and a normalized particle shape S_h,
a common discrete source model is

<div id="eq-deposition" class="dasc-equation" role="group" aria-label="Deposited charge density is the sum of particle charges times normalized particle shapes">
<math display="block"><msub><mi>ρ</mi><mi>h</mi></msub><mo>(</mo><mi mathvariant="bold">r</mi><mo>)</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mi>p</mi><mo>=</mo><mn>1</mn></mrow><msub><mi>N</mi><mi>p</mi></msub></munderover><msub><mi>q</mi><mi>p</mi></msub><msub><mi>S</mi><mi>h</mi></msub><mo>(</mo><mi mathvariant="bold">r</mi><mo>−</mo><msub><mi mathvariant="bold">q</mi><mi>p</mi></msub><mo>)</mo><mo>.</mo></math>
</div>

Here h labels the spatial discretization and **q**ₚ is particle position. If
∫S_h d³r = 1, then ∫ρ_h d³r = Σₚqₚ. Near finite boundaries, normalization,
clipping, or lost support must be stated because it can change charge and force
consistency.

## Differentiating the loop

DA/TPSA may propagate selected local parameter coefficients through source
construction, field solution, particle update, and observables. This requires
the executed branch and numerical stencil to remain differentiable over the
declared trust region. It does not establish that the loop has converged to a
physical fixed point, that an approximation is valid, or that its map is
symplectic.[^qiang]

## Conservation and reproducibility checks

At each resolution, record signed charge, boundary flux or loss, force sign,
source support, field-solve residuals, update step, and whether the source was
prescribed or recomputed. Particle number, grid or modal resolution, seed or
quiet start, and exact source/software commits belong in the
[reproducibility record](dasc-reproducibility.md).

[^qiang]: J. Qiang, “Differentiable self-consistent space-charge simulation for accelerator design,” *Phys. Rev. Accel. Beams* 26, 024601 (2023), cited by the reviewed DASC DA–TGF source.
