# Reproducibility and result release

Every DASC numerical result must be traceable from its physical claim to exact
source, configuration, raw data, analysis, figure, and validation decision.
Passing tests is not a substitute for this record.

## Required result record

| Category | Required fields |
|---|---|
| Identity | Result ID, title, owner, creation/review dates, validation status, linked row in the [validation matrix](dasc-validation-matrix.md) |
| Immutable source | Full DASC, PyDASC, website, source-document, and reference-solver commit SHAs; dirty-worktree status |
| Physical contract | Formulation, equations/section links, assumptions, boundary and initial conditions, frame, coordinates, signs, units, gauge where applicable |
| Runtime environment | OS, architecture, CPU/GPU, Python, locked dependencies, FFT/BLAS backend, thread settings, floating-point precision |
| Invocation | Configuration file, command line or workflow, working-directory-independent input paths, environment variables that change numerics |
| Source/particles | Distribution and trajectory parameters, total signed charge, particle count, shape, loading method, generator and seed or quiet-start definition |
| TGF controls | Grid shape/order, physical bounds, spacing, padding, cutoff radius/policy, kernel cache identity, deposition/gather, kick step and splitting |
| Eigenmode controls | a,L,b, material model, initial history, radial/axial modes, time/frequency grids, quadrature, cavity/pipe/aperture bases, propagating/evanescent counts, resonance/radiation treatment |
| DA/TPSA controls | Independent variables, references, physical scales, order, coefficient convention, trust region, fixed branches/stencils/modes, backend |
| Self-consistency | Integrator, iteration/update definition, absolute/relative residuals, stopping tolerance, maximum iterations, convergence history |
| Validation | Norms, sampling regions, reference definitions, independent solver setup, resolution/step/order sweeps, thresholds, pass/fail decision, known limitations |
| Artifact graph | Input, raw output, processed table, plot specification, figure, log, and manifest paths with byte sizes and SHA-256 checksums |

Use SI units unless a normalized study explicitly defines every scale and the
conversion back to SI. Store machine-readable numeric values, not only rounded
values copied from a plot.

## Artifact layout

A release package should use an explicit, nonrecursive allowlist and a layout
equivalent to:

```text
result-id/
├── result.yml                 # metadata and validation decision
├── configuration.yml          # complete numerical inputs
├── environment.txt            # locked environment and platform record
├── commands.txt               # exact nonsecret invocations
├── data/                      # immutable raw and processed numeric outputs
├── figures/                   # generated figures plus plotting specifications
├── checksums.sha256           # all released files except this checksum file
└── README.md                  # claim, reproduction steps, limits, reviewers
```

Never include credentials, private URLs, unrestricted logs, caches, temporary
checkouts, or undeclared files. A checksum proves byte identity, not scientific
correctness.

## Result statuses

| Status | Meaning |
|---|---|
| Planned | Claim and acceptance criteria exist; no completed run is asserted |
| Exploratory | Output exists but convergence, independence, or review is incomplete |
| Numerically verified | Declared equations and numerical acceptance gates pass for the recorded configuration |
| Physically validated | A suitable independent calculation or measurement also passes predeclared agreement criteria |
| Superseded | Retained for provenance but replaced by an identified result record |
| Withdrawn | Known invalid; reason and affected claims are recorded |

Software unit/regression tests can support “numerically verified,” but cannot
alone assign it. Status changes require review of the full artifact graph and
must not overwrite the prior record.

## Reproduction sequence

1. Verify all source commits and artifact checksums.
2. Recreate the locked environment without installing or executing unreviewed
   upstream project code merely to collect documentation.
3. Run the exact configuration and compare raw-output checksums where the
   platform promises bitwise reproducibility; otherwise compare declared
   numerical norms and tolerances.
4. Regenerate processed data and figures from raw data.
5. Repeat the stated convergence and independent-reference checks.
6. Record deviations, platform sensitivity, reviewer, and final status.

The current portal publishes no allowlisted DASC numerical result package.
Consequently its detailed derivations and software/test inventory must not be
read as a completed accuracy, performance, optimization, collective-physics,
aperture-validation, or experimental result.
