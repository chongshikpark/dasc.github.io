# Comparison and method selection

Choose from the physical boundary-value problem and the evidence required for
the decision. TGF and eigenmode calculations are not interchangeable merely
because both can return an electric field.

## Formulation comparison

| Property | TGF free-space formulation | Causal finite-cavity eigenmode formulation | Separate reference solver |
|---|---|---|---|
| Physical domain | Three-dimensional free space over a bounded source/observation region | Finite cylindrical PEC cavity; centered aperture and semi-infinite circular pipe where included | Domain supplied by the reference model |
| Boundary condition | Potential decays at infinity; no conducting image field | PEC cavity boundaries, causal initial data, aperture continuity, outgoing/decaying pipe condition | Choose to reproduce the target boundaries or deliberately test model error |
| Time model | Electrostatic or approved quasistatic Poisson solve in a declared frame | Laboratory-time retarded electromagnetic wave problem | Electrostatic, frequency-domain, time-domain, or particle model as independently justified |
| Baseline source | General sufficiently regular signed charge density supported by the physical grid; particle deposition where used | Reviewed baseline is an axisymmetric moving slice with prescribed z_b(t), v_b(t), and longitudinal current | Prefer a source class overlapping the case being tested |
| Potentials/fields | φ and **E**; grid field or energy-consistent particle force must be distinguished | φ, A_z, E_r, E_z, B_θ for the closed cavity; scattered/transmitted modal fields for aperture coupling | Must expose quantities, signs, frames, and sampling needed for comparison |
| Self-consistency | Supported conceptually through repeated deposition, solve, energy force, and tracking | Current reviewed workflow is prescribed-source; feedback through causal source history remains separate work | Use an independent self-consistent method when validating feedback claims |
| DA/TPSA role | Source, particle, accelerator, force/map, and observable sensitivities inside fixed grid/kernel and deposition trust contracts | Source, trajectory, modal, geometry, aperture-system, field, and observable sensitivities inside fixed mode/branch contracts | Finite differences, complex step, AD, or an independent DA implementation |
| Dominant controls | Grid spacing, domain, equal-spacing constraint, padding, cutoff radius, particle count/shape, kick step | Radial/axial modes, source-time quadrature, cavity/pipe/aperture modes, frequency/time reconstruction, particle/source resolution | Mesh, order, timestep, tolerance, particle/model controls declared by that solver |
| Nominal computational form | Padded FFT convolution: O(M log M) per scalar solve, plus deposition/force and DA batches | Modal sums and causal convolution; aperture block solves add basis/frequency-dependent cost | Record measured and asymptotic cost separately |
| Expected accuracy regime | Smooth, resolved, compactly supported sources whose required separations fit the approved cutoff/padding geometry; negligible conductor effects | Axisymmetric sources in the declared cylindrical PEC geometry with converged modal, quadrature, and matching truncations | Use when geometry/source lies outside either model or independent evidence is required |
| Characteristic failure modes | Periodic images, invalid cutoff geometry, insufficient domain, wrong FFT/ε₀ normalization, source under-resolution, inconsistent gather force | Noncausal sampling, wrong D/N axial family, omitted v_b or −∂A_z/∂t, modal ringing, resonance/conditioning, incomplete evanescent content | Discretization/model bias, mismatched signs/frames, nonindependent shared assumptions |
| Current portal evidence | Reviewed PyDASC implementation and repository tests exist; no allowlisted public accuracy/result artifact is published here | Reviewed PyDASC prescribed-source, aperture, and DA implementation/tests exist; no allowlisted public validation/result artifact is published here | No single reference solver or artifact is approved by this portal yet |

## Selection questions

1. Are nearby conducting boundaries, reflection arrival, radiation, aperture
   transmission, or magnetic/inductive fields material? If yes, the free-space
   TGF model is not sufficient.
2. Is the physical region accurately represented by the current axisymmetric
   cylindrical cavity, centered aperture, and circular pipe? If not, use or
   develop a geometry-appropriate reference solver.
3. Is a prescribed trajectory sufficient, or is source-field-particle feedback
   central to the claim? The current eigenmode workflow does not establish a
   self-consistent causal tracker.
4. Does the decision require only a field, or an energy-consistent canonical
   particle map? A gathered field and a Hamiltonian force have different
   evidence requirements.
5. Are local parameter derivatives required? Freeze and report the active
   grid, stencil, modes, causal/radiation branch, and trust region before using
   DA/TPSA.
6. Is the calculation itself the subject of validation? Use an independently
   implemented method with overlapping physical assumptions rather than
   comparing two wrappers around the same operator.

## When to require a separate solver

Use a full-wave finite-element or finite-integration calculation for selected
cavity/aperture cases; a high-resolution Hockney, gridless, fast-multipole, or
direct N-body calculation for suitable free-space cases; or an independent
particle/Vlasov calculation for self-consistent dynamics. Agreement is
meaningful only after matching sources, units, frames, boundary conditions,
initial data, observation coordinates, and observable definitions.

Continue with the [claim validation matrix](dasc-validation-matrix.md),
[reproducibility record](dasc-reproducibility.md), or the detailed
[TGF](dasc-tgf-method.md), [eigenmode](dasc-eigenmode-method.md), and
[DA/TPSA/Lie](dasc-differential-algebra-methods.md) sections.
