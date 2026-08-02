# Comparison and method selection

Choose a formulation from the physical boundary-value problem, not from the
numerical technique or desired plot.

| Question | TGF formulation | Eigenmode formulation |
| --- | --- | --- |
| Primary physical domain | Free space | Finite conducting cylindrical cavity with aperture/pipe coupling |
| Field model | Electrostatic or quasistatic Poisson problem | Causal, time-dependent electromagnetic problem |
| Typical source description | Charge distribution used by a free-space solve | Axisymmetric charge/current source on a stated trajectory |
| Boundary treatment | Open free-space boundary represented by the approved TGF construction | Conducting cavity boundaries plus modal aperture/pipe matching |
| Main truncation controls | Grid, domain, padding, kernel cutoff, particle/source representation | Radial/axial/coupling modes, causal quadrature, observation time |
| DA/TPSA role | Selected source, accelerator, map, and observable sensitivities | Selected source, trajectory, modal, and geometry sensitivities where smooth |
| Evidence required | Analytical free-space checks, convergence, force/map diagnostics | Boundary, causality, modal convergence, matching, and independent-field checks |

This is an architecture-level comparison. Accuracy regimes, computational
scaling, verified parameters, and method-selection recommendations require the
reviewed derivations and evidence from later tasks. Use a separate independent
solver when neither boundary model matches the physical question or when a
validation gate requires a reference calculation.

- [TGF section](dasc-tgf-method.md)
- [Eigenmode section](dasc-eigenmode-method.md)
- [Physics foundations](dasc-physics-foundations.md)

