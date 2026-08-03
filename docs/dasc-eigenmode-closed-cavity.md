# Closed-cavity retarded modal solution

## Transverse and axial bases

Let j₀ₙ be the nth positive zero of J₀ and kₙ = j₀ₙ/a. The normalized
axisymmetric radial eigenfunction is

<div id="eq-cavity-radial-mode" class="dasc-equation" role="group" aria-label="Normalized axisymmetric radial cavity eigenfunction">
<math display="block"><msub><mi>ψ</mi><mi>n</mi></msub><mo>(</mo><mi>r</mi><mo>)</mo><mo>=</mo><mfrac><mrow><msub><mi>J</mi><mn>0</mn></msub><mo>(</mo><msub><mi>j</mi><mrow><mn>0</mn><mi>n</mi></mrow></msub><mi>r</mi><mo>/</mo><mi>a</mi><mo>)</mo></mrow><mrow><msqrt><mi>π</mi></msqrt><mi>a</mi><mo>|</mo><msub><mi>J</mi><mn>1</mn></msub><mo>(</mo><msub><mi>j</mi><mrow><mn>0</mn><mi>n</mi></mrow></msub><mo>)</mo><mo>|</mo></mrow></mfrac><mo>,</mo><mspace width="1em"/><mn>2</mn><mi>π</mi><msubsup><mo>∫</mo><mn>0</mn><mi>a</mi></msubsup><mi>r</mi><msub><mi>ψ</mi><mi>n</mi></msub><msub><mi>ψ</mi><mi>m</mi></msub><mi>d</mi><mi>r</mi><mo>=</mo><msub><mi>δ</mi><mrow><mi>n</mi><mi>m</mi></mrow></msub><mo>.</mo></math>
</div>

The distinct normalized axial families are u_p(z) = √(2/L) sin(pπz/L), p ≥ 1,
for φ and v_p(z) = √((2−δ_p0)/L) cos(pπz/L), p ≥ 0, for A_z. Although both
families have κ_np = √(kₙ²+(pπ/L)²) and ω_np = cκ_np, their p ranges and boundary
conditions differ. Superscripts D and N below prevent accidental interchange.

## Causal Green functions

For Δt = t−t′, the scalar Green function is

<div id="eq-cavity-scalar-green" class="dasc-equation" role="group" aria-label="Retarded closed cavity scalar potential Green function">
<math display="block"><msubsup><mi>G</mi><mi>φ</mi><mn>0</mn></msubsup><mo>=</mo><msup><mi>c</mi><mn>2</mn></msup><mi>H</mi><mo>(</mo><mi>Δ</mi><mi>t</mi><mo>)</mo><munderover><mo>∑</mo><mrow><mi>n</mi><mo>=</mo><mn>1</mn></mrow><mo>∞</mo></munderover><munderover><mo>∑</mo><mrow><mi>p</mi><mo>=</mo><mn>1</mn></mrow><mo>∞</mo></munderover><msub><mi>ψ</mi><mi>n</mi></msub><mo>(</mo><mi>r</mi><mo>)</mo><msub><mi>ψ</mi><mi>n</mi></msub><mo>(</mo><mi>r</mi><mo>′</mo><mo>)</mo><msub><mi>u</mi><mi>p</mi></msub><mo>(</mo><mi>z</mi><mo>)</mo><msub><mi>u</mi><mi>p</mi></msub><mo>(</mo><mi>z</mi><mo>′</mo><mo>)</mo><mfrac><mrow><mi>sin</mi><mo>(</mo><msubsup><mi>ω</mi><mrow><mi>n</mi><mi>p</mi></mrow><mi>D</mi></msubsup><mi>Δ</mi><mi>t</mi><mo>)</mo></mrow><msubsup><mi>ω</mi><mrow><mi>n</mi><mi>p</mi></mrow><mi>D</mi></msubsup></mfrac><mo>.</mo></math>
</div>

The vector-potential Green function has the same retarded sine oscillator, but
u_p is replaced by v_p and the axial sum starts at p = 0. The Heaviside factor
H(Δt) enforces retarded support; a numerical implementation must mask
noncausal samples rather than perturbing them to small positive arguments.

## Source projection and modal potentials

Define F_n = 2π∫₀ʳᵇ r f(r)ψ_n(r)dr. For the parabolic radial profile specified
in the reviewed source, this integral has a closed Bessel-function expression;
other profiles require their own normalized projection.

The scalar potential is

<div id="eq-cavity-scalar-potential" class="dasc-equation" role="group" aria-label="Closed cavity retarded scalar potential modal expansion">
<math display="block"><msup><mi>φ</mi><mn>0</mn></msup><mo>=</mo><mfrac><mi>Q</mi><msub><mi>ε</mi><mn>0</mn></msub></mfrac><munderover><mo>∑</mo><mrow><mi>n</mi><mo>≥</mo><mn>1</mn><mo>,</mo><mi>p</mi><mo>≥</mo><mn>1</mn></mrow><mo>∞</mo></munderover><msub><mi>ψ</mi><mi>n</mi></msub><mo>(</mo><mi>r</mi><mo>)</mo><msub><mi>u</mi><mi>p</mi></msub><mo>(</mo><mi>z</mi><mo>)</mo><msub><mi>F</mi><mi>n</mi></msub><msubsup><mo>∫</mo><mn>0</mn><mi>t</mi></msubsup><mfrac><msup><mi>c</mi><mn>2</mn></msup><msubsup><mi>ω</mi><mrow><mi>n</mi><mi>p</mi></mrow><mi>D</mi></msubsup></mfrac><mi>sin</mi><mo>[</mo><msubsup><mi>ω</mi><mrow><mi>n</mi><mi>p</mi></mrow><mi>D</mi></msubsup><mo>(</mo><mi>t</mi><mo>−</mo><mi>t</mi><mo>′</mo><mo>)</mo><mo>]</mo><msub><mi>u</mi><mi>p</mi></msub><mo>[</mo><msub><mi>z</mi><mi>b</mi></msub><mo>(</mo><mi>t</mi><mo>′</mo><mo>)</mo><mo>]</mo><mi>d</mi><mi>t</mi><mo>′</mo><mo>.</mo></math>
</div>

For A_z, replace Q/ε₀ by μ₀Q, u_p by v_p, D by N, begin p at zero, and include
v_b(t′) inside the time integral. That current factor cannot be removed for an
accelerating source. Each retained coefficient is therefore a causal functional
of the trajectory history, not merely of the observation-time position.

The double modal sum is truncated numerically. Radial modes, axial modes, and
causal quadrature resolution are independent controls; convergence in one does
not establish convergence in the others.[^hess]

[^hess]: M. Hess, C. S. Park, and D. Bolton, “Green's function based space-charge field solver for electron source simulations,” *Phys. Rev. ST Accel. Beams* 10, 054201 (2007), [doi:10.1103/PhysRevSTAB.10.054201](https://doi.org/10.1103/PhysRevSTAB.10.054201).
