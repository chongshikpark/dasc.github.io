# Lie maps and symplectic structure

## Canonical operators

For declared canonical coordinates z = (q,p), the Poisson bracket is

<div id="eq-da-poisson-bracket" class="dasc-equation" role="group" aria-label="Canonical Poisson bracket for two phase space functions">
<math display="block"><mo>{</mo><mi>f</mi><mo>,</mo><mi>g</mi><mo>}</mo><mo>=</mo><munderover><mo>∑</mo><mi>j</mi><mi>n</mi></munderover><mo>(</mo><mfrac><mrow><mi>∂</mi><mi>f</mi></mrow><mrow><mi>∂</mi><msub><mi>q</mi><mi>j</mi></msub></mrow></mfrac><mfrac><mrow><mi>∂</mi><mi>g</mi></mrow><mrow><mi>∂</mi><msub><mi>p</mi><mi>j</mi></msub></mrow></mfrac><mo>−</mo><mfrac><mrow><mi>∂</mi><mi>f</mi></mrow><mrow><mi>∂</mi><msub><mi>p</mi><mi>j</mi></msub></mrow></mfrac><mfrac><mrow><mi>∂</mi><mi>g</mi></mrow><mrow><mi>∂</mi><msub><mi>q</mi><mi>j</mi></msub></mrow></mfrac><mo>)</mo><mo>.</mo></math>
</div>

Define the Lie operator :g: f = {g,f}. The formal transformation exp(:g:) acts
by f + {g,f} + {g,{g,f}}/2! + …. When g is a sufficiently regular scalar
generator on the declared canonical phase space, its exact Hamiltonian flow is
symplectic. A finite Taylor truncation of its coordinate map still requires a
symplectic-defect study at the retained order.

Lie generators can parameterize controlled distribution perturbations:
f_a(z) = exp(−:G(a):)f₀(z), with G = Σ_j a_jg_j. Linear/quadratic generators
can excite centroid, breathing, quadrupole, or coupling perturbations; higher
monomials can probe shape modes. Orthogonalize generators against lower moments
when the intended perturbation should not alter those moments.

## Map construction and composition

For a Hamiltonian split H = H_ext + H_sc, the symmetric second-order
composition is

<div id="eq-da-symmetric-split" class="dasc-equation" role="group" aria-label="Second order symmetric external and space charge map composition">
<math display="block"><msub><mi>M</mi><mrow><mi>Δ</mi><mi>s</mi></mrow></msub><mo>=</mo><msub><mi>M</mi><mtext>ext</mtext></msub><mo>(</mo><mi>Δ</mi><mi>s</mi><mo>/</mo><mn>2</mn><mo>)</mo><mo>∘</mo><msub><mi>M</mi><mtext>sc</mtext></msub><mo>(</mo><mi>Δ</mi><mi>s</mi><mo>)</mo><mo>∘</mo><msub><mi>M</mi><mtext>ext</mtext></msub><mo>(</mo><mi>Δ</mi><mi>s</mi><mo>/</mo><mn>2</mn><mo>)</mo><mo>+</mo><mi>O</mi><mo>(</mo><mi>Δ</mi><msup><mi>s</mi><mn>3</mn></msup><mo>)</mo><mo>.</mo></math>
</div>

Composition preserves symplecticity only if every submap uses the same
canonical variables and is symplectic. For the TGF branch, the
[energy-gradient kick](dasc-tgf-field-kick.md#eq-tgf-energy-force) is the
candidate space-charge submap. An independently gathered grid field is not
automatically the gradient of that discrete Hamiltonian.

The causal eigenmode branch currently derives a Lorentz force in laboratory
time but has no frozen canonical tracking normalization or self-consistent
Hamiltonian splitting. Lie analysis may be applied only after those structures
are declared; DA differentiability of its fields does not fill that gap.

## Structural diagnostic

For the full canonical multiparticle Jacobian M and canonical matrix J,

<div id="eq-da-symplectic-defect" class="dasc-equation" role="group" aria-label="Normalized Frobenius symplectic defect of a canonical map">
<math display="block"><msub><mi>η</mi><mtext>symp</mtext></msub><mo>=</mo><mfrac><mrow><mo>‖</mo><msup><mi>M</mi><mi>T</mi></msup><mi>J</mi><mi>M</mi><mo>−</mo><mi>J</mi><msub><mo>‖</mo><mi>F</mi></msub></mrow><mrow><mo>‖</mo><mi>J</mi><msub><mo>‖</mo><mi>F</mi></msub></mrow></mfrac><mo>.</mo></math>
</div>

Large systems can test bilinear residuals with Jacobian-vector and transpose-
Jacobian-vector products. Determinant one is insufficient. A projected moment
map need not be symplectic even if the complete 6N-particle canonical map is.
These tests establish numerical structure, not field accuracy or physical
validation.[^qiang]

[^qiang]: J. Qiang, “A symplectic multi-particle tracking model for self-consistent space-charge simulation,” *Phys. Rev. Accel. Beams* 20, 014203 (2017), [doi:10.1103/PhysRevAccelBeams.20.014203](https://doi.org/10.1103/PhysRevAccelBeams.20.014203).
