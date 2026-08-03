# Physics claim validation matrix

## Status vocabulary

- **Derived**: the reviewed DASC source supports the stated equation or mathematical formulation.
- **Implemented/tested**: the locked PyDASC checkout contains a corresponding component and repository test; this is software evidence.
- **Artifact pending**: this portal does not publish an allowlisted raw result package with complete configuration and checksums.
- **Open**: an implementation, independent comparison, convergence study, or scientific approval is still required.

The exact locked inputs are DASC `94033eae4d8eac81f4c42c41f6cfba69e1cd2a25`
and PyDASC `0506b8a9feb75813ae979f0c1c25a307b21096d2`.
Paths below identify evidence in those immutable revisions; tests are not
published result artifacts.

## TGF and particle-map claims

| Claim | Governing derivation | PyDASC component | Repository test/reference | Convergence or independent evidence | Status and acceptance criterion |
|---|---|---|---|---|---|
| Free-space potential solves Poisson with decay at infinity | [Poisson problem](dasc-tgf-free-space-poisson.md#eq-tgf-poisson) and [convolution](dasc-tgf-free-space-poisson.md#eq-tgf-green-convolution) | `space_charge_kernels/space_charge_vgf.py` | `test_vgf_kernel.py`, Gaussian potential/field references | Grid, domain, cutoff, padding, analytic Gaussian norms | **Derived; implemented/tested; artifact pending.** Accept only with converged norms and immutable result package. |
| Truncation/padding preserves required aperiodic convolution | [Cutoff condition](dasc-tgf-formulation.md#eq-tgf-cutoff-condition) and spectral kernel | `FreeSpaceVGF` | VGF kernel/invariance/operator-symmetry tests | Independent Hockney comparison and separate cutoff/padding sweeps | **Derived; implemented/tested; artifact pending.** Accept after geometry rejection and agreement criteria are recorded. |
| Grid field uses the declared spectral derivative and normalization | [Direct field](dasc-tgf-field-kick.md#eq-tgf-direct-field) | VGF direct-field path | `test_vgf_fields.py`, Gaussian field references | L2/max error and zero/Nyquist-mode tests | **Implemented/tested; artifact pending.** Do not infer particle-force energy consistency. |
| Particle force is the gradient of the same discrete energy | [Energy](dasc-tgf-field-kick.md#eq-tgf-discrete-energy) and [force](dasc-tgf-field-kick.md#eq-tgf-energy-force) | `hamiltonian/space_charge.py` | `test_discrete_energy_force.py`, `test_local_particle_force.py` | Centered energy differences, shape/stencil and resolution studies | **Derived; implemented/tested; artifact pending.** Accept when force error and trust-cell criteria pass. |
| Complete TGF tracking map is symplectic | [Kick boundary](dasc-tgf-field-kick.md#eq-tgf-kick) and [structural diagnostic](dasc-da-lie-maps.md#eq-da-symplectic-defect) | Hamiltonian kick, linear lattice, tracking modules | `test_space_charge_kick.py`, `test_full_tracking_map.py` | Step refinement, reversibility, long-term invariant and independent-method comparison | **Implemented/tested at software level; scientific artifact pending.** Accept only for declared canonical variables and full composition. |
| DA/TPSA coefficients equal physical TGF sensitivities | [Coefficient convention](dasc-da-tpsa.md#eq-tpsa-coefficient-derivative) and [TGF pipeline](dasc-da-pipelines.md#tgf-free-space-branch) | `da/`, `maps/gaussian_vgf.py` | DA arithmetic/batch and Gaussian DA derivative tests | Analytic identities, finite-difference step sweep, order/trust-region study | **Implemented/tested for supported cases; artifact pending.** Accept per parameter, order, scale, and tolerance. |

## Causal eigenmode and aperture claims

| Claim | Governing derivation | PyDASC component | Repository test/reference | Convergence or independent evidence | Status and acceptance criterion |
|---|---|---|---|---|---|
| Closed-cavity potentials obey causal wave equations and distinct axial boundaries | [Wave equations/boundaries](dasc-eigenmode-problem.md#eq-cavity-wave-equations), [retarded modes](dasc-eigenmode-closed-cavity.md#eq-cavity-scalar-green) | `closed_cavity_eigenmodes.py`, basis/source modules | closed-cavity unit/reference/convergence and Maxwell-residual tests | Radial, axial, time quadrature, boundary/gauge residual convergence | **Derived; implemented/tested; artifact pending.** Accept with predeclared residual and convergence thresholds. |
| Analytical E_r, E_z, B_θ include the inductive contribution and axis regularity | [Field reconstruction](dasc-eigenmode-fields.md#eq-cavity-fields) | `eigenmode_fields.py` | closed-cavity boundary/field and reconstruction tests | Analytic/on-axis limits, semi-infinite early-time reference, full-wave sample | **Derived; implemented/tested; independent artifact pending.** |
| Aperture fields satisfy interface, radiation, and energy conditions | [Mode matching](dasc-eigenmode-aperture.md#eq-aperture-matching) | `aperture_mode_matching.py` | aperture unit, convergence, balance, overlap tests | Propagating/evanescent refinement, reciprocity, Poynting balance, full-wave comparison | **Formulated; implemented/tested; full-wave artifact pending.** Accept only after all interface and energy thresholds pass. |
| Small-hole theory is a controlled limiting benchmark | [Scale conditions](dasc-eigenmode-aperture.md#eq-small-aperture-limit) | no general substitute for mode matcher | selected screening/aperture tests | b/a and kb asymptotic sequence with thickness convention | **Derived applicability limit; quantitative artifact pending.** Never apply as primary evidence outside the declared limit. |
| Eigenmode DA coefficients equal physical source/trajectory/geometry sensitivities | [Eigenmode dependency map](dasc-da-pipelines.md#causal-eigenmode-branch) | `maps/eigenmode.py`, coefficient/special modules | eigenmode DA unit/reference/convergence tests | Analytic cases, finite-difference step and TPSA-order/trust-region studies | **Implemented/tested for supported finite maps; artifact pending.** Geometry/mode-crossing claims require case-specific review. |
| Cavity calculation is self-consistent and symplectic | [Force/status boundary](dasc-eigenmode-fields.md#force-and-self-consistent-dynamics) | prescribed-source workflow; no approved complete canonical feedback contract | component tests do not establish this claim | converged causal source-history feedback, canonical-map derivation, structural and independent checks | **Open.** No current claim is allowed. |

## Cross-cutting acceptance rules

Every accepted row requires a [reproducibility record](dasc-reproducibility.md),
raw outputs and configuration with SHA-256 checksums, immutable commits, declared
precision, independently varied convergence controls, and a result-specific
acceptance threshold. “Tests pass,” a single resolution, or agreement between
two code paths sharing the same primitive cannot by itself close a physics
claim.
