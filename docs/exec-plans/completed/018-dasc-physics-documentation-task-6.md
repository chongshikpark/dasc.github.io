# Task 6 execution summary: comparison, validation, and reproducibility

## Outcome

Expanded the DASC decision and evidence layer with a three-way method
comparison, a claim-level physics validation matrix, and release-grade
reproducibility guidance. Updated the project and research-output pages so
reusable derivations remain separate from manuscripts, milestones, and result
packages.

No upstream source, source lock, publication-manifest entry, imported document,
benchmark artifact, implementation status, or scientific validation status
changed. Nothing was pushed or deployed.

## Method selection

The comparison covers the TGF formulation, causal finite-cavity eigenmode
formulation, and a separate reference solver across:

- physical domain, boundary and initial conditions, and time model;
- source/symmetry class, potentials and fields, and self-consistency scope;
- DA/TPSA sensitivity role and trust contracts;
- computational form and dominant truncation controls;
- expected applicability regime and characteristic failure modes;
- current implementation/test evidence and missing public artifacts; and
- questions that require an independent full-wave, free-space, particle, or
  Vlasov reference calculation.

## Validation matrix

The matrix maps major TGF, particle-map, cavity, aperture, and DA claims to:

- governing equation or derivation section;
- component in locked PyDASC commit
  `0506b8a9feb75813ae979f0c1c25a307b21096d2`;
- repository unit, reference, convergence, integration, or structural tests;
- required analytic benchmark, convergence study, or independent solver;
- current evidence status; and
- an explicit acceptance condition.

It distinguishes “derived,” “implemented/tested,” “artifact pending,” and
“open.” In particular, repository tests are described as software evidence,
not a public scientific result package. The causal cavity calculation is not
claimed to be a self-consistent symplectic map.

## Reproducibility and outputs

The result record now requires immutable DASC, PyDASC, portal, source-document,
and reference-solver commits; physical contracts; environment and precision;
complete TGF/eigenmode/DA/self-consistency controls; particle loading and seed
or quiet start; convergence and reference definitions; acceptance decisions;
and SHA-256 checksums for the full artifact graph.

The page defines planned, exploratory, numerically verified, physically
validated, superseded, and withdrawn statuses; a safe explicit package layout;
and a reproduction sequence. It states that this portal currently publishes no
allowlisted DASC numerical result package.

Paper titles, abstracts, journal targets, milestones, submission records, and
manuscript decisions remain under Research outputs and publications and link
back to reusable theory and evidence pages rather than duplicating derivations.

## Files added

- `docs/dasc-validation-matrix.md`
- `docs/exec-plans/completed/018-dasc-physics-documentation-task-6.md`

## Files updated

- `docs/dasc-method-selection.md`
- `docs/dasc-reproducibility.md`
- `docs/dasc-research-outputs.md`
- `docs/dasc-project-overview.md`
- `mkdocs.yml`
- `tests/test_physics_docs.py`

## Visible unresolved issues

1. No allowlisted raw DASC result package is currently published by the portal.
2. Result-specific numerical thresholds and independent-reference
   configurations must be approved with each future artifact.
3. No one reference solver is approved for every TGF, cavity, aperture, and
   self-consistent-dynamics claim.
4. The complete self-consistent causal cavity map and its canonical structure
   remain open.

## Verification

- 27 tests passed.
- Physics equation, anchor, citation, and forbidden-path validation passed.
- Exact-lock source collection and publication-boundary validation passed.
- Repeated source assembly produced no generated-content diff.
- `mkdocs build --strict` passed without warnings.
- Site link/presentation and semantic-accessibility validation passed.
- The built artifact scan found no local filesystem path or excluded task file.

Interactive browser, screen-reader, copy/paste, 200% zoom, and print-to-PDF
inspection remain part of the final Task 7 review.
