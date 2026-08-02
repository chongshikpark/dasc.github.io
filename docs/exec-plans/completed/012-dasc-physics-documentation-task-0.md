# Task 0 execution summary: audit and correct the current DASC framing

## Outcome

The portal framing now identifies DASC as the physics, derivation, analysis,
reproducibility, and publication project for differentiable, self-consistent
space-charge modeling and beam-dynamics maps. PyDASC is identified separately as
the computational and numerical software package. The incorrect data-assimilation
description and the DASC installation/command-line wording were removed.

This task did not add a derivation, import a LaTeX file, change a source lock or
publication allowlist, change a documentation status, edit either upstream
repository, push, or deploy.

## Evidence and traceability

The following reviewed public sources support the bounded framing correction:

- `/Users/cspark/Work/projects/dasc/docs/differentiable_symplectic_space_charge_study.tex:35`
  introduces self-consistent space-charge simulation; lines 40–55 define the
  proposed TGF, DA/TPSA, Hamiltonian, and map roles; lines 72–95 describe the
  source-to-observable differentiable pipeline.
- `/Users/cspark/Work/projects/dasc/docs/space_charge_fields_with_aperture_study.tex:28`
  scopes the causal finite-cavity field problem; lines 43–61 distinguish the
  desired self-consistent solver from the present prescribed-trajectory
  derivation.
- `/Users/cspark/Work/projects/dasc/docs/space_charge_research_plan.tex:34`
  describes the physics-first research program and treats the DA–VGF method as
  an instrument rather than the result; lines 533–568 define falsification and
  evidence gates.
- `/Users/cspark/Work/projects/dasc/README.md:31` distinguishes PyDASC as the
  simulation/numerical-method package and DASC as the analysis,
  reproducibility, and manuscript repository in the currently published source.
- `/Users/cspark/Work/projects/dasc/docs/SOURCE_MAP.md:54` requires the
  electrostatic/quasistatic free-space TGF work and the time-dependent cavity
  eigenmode work to remain distinct.

The LaTeX sources are Git-tracked at DASC checkout
`94033eae4d8eac81f4c42c41f6cfba69e1cd2a25`. They informed this audit but remain
excluded from the website publication boundary. Statements in early
`abstract.tex` and `space_charge_prab.tex` that present benchmarks or validation
as completed were not reused. The later source map marks the former as broad and
promotional and the latter as a legacy formulation requiring reassessment.

## Current-site findings

The signed-out site and matching source tree were reviewed on 2026-08-03.

| Severity | Finding and evidence | Task 0 disposition |
| --- | --- | --- |
| High | The live home page and `docs/index.md:3` called DASC a data-assimilation ecosystem. No reviewed DASC source supports that identity. | Corrected to differentiable, self-consistent space-charge modeling and beam-dynamics maps. |
| High | The live DASC page, generated from `/Users/cspark/Work/projects/dasc/README.md`, opens with two paper nicknames and devotes most headings to titles, milestones, and manuscript sequencing. | Recorded for Task 1. Generated content was not edited in place; an upstream project-first public overview or newly approved website page is required. |
| Medium | `mkdocs.yml` exposed only `DASC → Overview`, with no physics hierarchy. | Relabeled the current page `Project overview`; the proposed hierarchy below is reserved for Task 1 and later approved imports. |
| Medium | Material footer navigation linked the last PyDASC page directly to DASC and DASC directly to Contribute. | Disabled global previous/next footer navigation temporarily. Restore it only when section-local behavior or a complete DASC sequence prevents unexpected project crossing. |
| Medium | The single imported DASC README carries `Unvalidated`, which correctly warns about planned results but can make the whole project overview appear to be an unvalidated derivation. | No status was changed. Split project lifecycle/review status from scientific validation status in an upstream publication-contract review. |
| Low | `docs/getting-started.md` described DASC primarily as a paper-development repository and framed the choice as installation. | Corrected the project roles and changed the heading to “Before using either project.” |

## Content inventory

This inventory classifies material; it does not approve any new file for public
copying.

| Classification | Existing material | Assessment |
| --- | --- | --- |
| Project overview | `/Users/cspark/Work/projects/dasc/README.md`; `docs/getting-started.md`; `docs/index.md` | The README contains correct project separation and reproducibility rules but is paper-first. A project-first overview is needed. |
| Reusable physics foundation | `differentiable_symplectic_space_charge_study.tex:58-164`; `space_charge_fields_with_aperture_study.tex:45-114,507-543` | Candidate sources for problem statements, geometry, source models, frames, signs, units, and governing equations. Conflicts and conventions require scientific review before publication. |
| TGF formulation | `differentiable_symplectic_space_charge_study.tex:127-302`; `space_charge_research_plan.tex:154-199` | Contains free-space Poisson, truncated Green-function, and analytical-check structure. It is excluded and not yet an approved website derivation. |
| Eigenmode formulation | `space_charge_fields_with_aperture_study.tex:45-660` | The reassessed finite-cavity source is primary. It supersedes unsupported aperture assumptions in `space_charge_prab.tex` and the supplements, subject to formal source approval. |
| DA/TPSA/Lie methodology | `differentiable_symplectic_space_charge_study.tex:303-427,605-667`; `space_charge_research_plan.tex:200-390` | DA/TPSA coefficient propagation and canonical/Lie-map uses must be separated from claims of differentiability, energy consistency, or symplecticity. |
| Validation and numerical evidence | `differentiable_symplectic_space_charge_study.tex:249-300,703-794`; `space_charge_fields_with_aperture_study.tex:544-660`; `docs/SIMULATION_MATRIX.md` | Primarily validation plans and acceptance checks, not completed evidence. Legacy claims of completed validation must not be published as results. |
| Reproducibility | `/Users/cspark/Work/projects/dasc/README.md:106-120`; `docs/SIMULATION_MATRIX.md:36-38`; `docs/MANUSCRIPT_POLICY.md` | Strong basis for commit/configuration/seed/checksum requirements. Currently only the README portion is allowlisted. |
| Paper-specific planning | `abstract.tex`; `space_charge_research_plan.tex:572-634`; README research program/milestones; `milestones/`, `tasks/`, and `manuscripts/` | Retain under a secondary Research outputs and publications section; do not organize the physics documentation around it. |
| Internal or excluded | All current `.tex`, `.pdf`, `.synctex.gz`, supplements, source maps, decision logs, simulation matrices, upstream execution plans, and website `architecture/`, `operations/`, and `exec-plans/` | None is allowlisted by `docs-manifest.yml`. Supplements are incremental legacy drafts; binary/build artifacts and internal plans must remain excluded. |

## Proposed DASC page map

The following is the Task 1 target, not a Task 0 publication change:

```text
DASC
├── Project overview
├── Physics foundations
│   ├── Self-consistent space charge
│   ├── Frames, coordinates, units, and conventions
│   ├── Potentials, fields, and particle dynamics
│   └── Approximations and validity limits
├── Differential-algebra methods
│   ├── DA and finite-order TPSA
│   ├── Differentiating the self-consistent solve
│   └── Lie maps and symplectic structure
├── Truncated Green's-function method
│   ├── Free-space Poisson problem
│   ├── TGF/Vico–Greengard–Ferrando formulation
│   ├── Field and kick construction
│   └── Verification and convergence
├── Eigenmode method
│   ├── Finite cylindrical cavity problem
│   ├── Retarded scalar and vector potentials
│   ├── Modal field derivation
│   ├── Aperture and downstream-pipe coupling
│   └── Verification and convergence
├── Comparison and method selection
├── Reproducibility
└── Research outputs and publications
```

The main flow should describe charge/source construction → field solve →
DA/TPSA propagation where applicable → particle map/observables → independent
validation. Paper titles, abstracts, milestones, journal decisions, and
submission plans belong only in the final secondary section.

## Unresolved scientific and publication decisions

1. Freeze the TGF tracking canonical coordinates, independent variable, frame
   transformation, and explicit space-charge normalization. The upstream
   decision remains open in `docs/DECISION_LOG.md:14`.
2. Map both formulations to actual reviewed PyDASC public APIs and passing tests;
   the upstream decision remains open at `docs/DECISION_LOG.md:15` even though a
   PyDASC checkout is now available to the website collector.
3. Decide whether the eigenmode documentation stops at a prescribed-trajectory
   baseline or includes an approved iterative self-consistent trajectory update.
   The staged decision is recorded at `docs/DECISION_LOG.md:12` and the source
   distinction at `space_charge_fields_with_aperture_study.tex:61`.
4. Freeze shared or separate notation for the TGF and eigenmode formulations
   (`docs/DECISION_LOG.md:23`).
5. Define the exact supported role of Lie methods in each formulation; do not
   infer a Lie-map implementation from paper framing alone.
6. Reconcile lifecycle review labels with scientific validation labels before
   replacing the single `Unvalidated` overview status. This requires an upstream
   source-publication decision, not a portal-only edit.
7. Review redistribution approval file by file before adding any LaTeX-derived
   page. Public Git visibility and an MIT repository license do not by themselves
   add a file to `docs-manifest.yml`.

## Files changed

- `docs/index.md` — corrected the project identity and DASC card.
- `docs/getting-started.md` — corrected project roles and usage framing.
- `mkdocs.yml` — relabeled the DASC page and temporarily removed cross-project
  previous/next footer controls.
- `tests/test_presentation.py` — locked the temporary footer-navigation policy.
- `docs/exec-plans/completed/012-dasc-physics-documentation-task-0.md` — this
  excluded audit, inventory, proposed map, and decision record.

The pre-existing `.gitignore` modification was preserved and is unrelated to
this task.
