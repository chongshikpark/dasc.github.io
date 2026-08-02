# Physics foundations

This section will hold the shared physical definitions used by both the TGF and
eigenmode formulations. Keeping them here prevents frames, signs, units, and
source conventions from drifting between method pages.

!!! note "Architecture, not derivation"
    Task 1 defines the boundaries below. The reviewed derivation, equations,
    citations, and convention tables belong to Task 2.

## Self-consistent space charge

The foundation will distinguish a prescribed source-field calculation from a
self-consistent update in which the particle or source state changes in response
to its generated field. It will state the update sequence and the point at which
each formulation recomputes or holds its source fixed.

## Frames, coordinates, units, and conventions

The shared convention record will define laboratory, reference-particle,
beam-rest, and cavity coordinates only where used. It will freeze charge and
current signs, SI or normalized units, Fourier conventions, canonical variables,
and the independent variable before dependent equations are published.

## Potentials, fields, and particle dynamics

This boundary connects charge/current sources to scalar and vector potentials,
fields, forces, and a stated particle update. Electrostatic Poisson and causal
retarded-wave problems will remain visibly distinct.

## Approximations and validity limits

Every later derivation must separate exact identities, modeling approximations,
discretizations, and implementation choices. Quasistatic assumptions,
prescribed trajectories, symmetry, finite-domain or boundary models, modal or
grid truncation, and intentionally omitted physics will be recorded before
results that depend on them.

Primary candidate sources are the public DASC
[DA–TGF study](https://github.com/chongshikpark/dasc/blob/94033eae4d8eac81f4c42c41f6cfba69e1cd2a25/docs/differentiable_symplectic_space_charge_study.tex)
and [reassessed cavity study](https://github.com/chongshikpark/dasc/blob/94033eae4d8eac81f4c42c41f6cfba69e1cd2a25/docs/space_charge_fields_with_aperture_study.tex).
Linking these sources does not add them to the website publication allowlist.

