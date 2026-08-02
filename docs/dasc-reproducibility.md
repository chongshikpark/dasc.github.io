# Reproducibility

Every DASC numerical result must be traceable to the physical model, software,
configuration, and generated artifact that produced it.

At minimum, record:

- exact DASC, PyDASC, and source-document commits;
- the physical formulation, assumptions, coordinates, signs, and units;
- configuration files and all solver/truncation controls;
- dependency environment, platform, and floating-point precision;
- grid/domain or modal/quadrature resolutions;
- particle or source loading, random seed, or quiet-start definition;
- convergence and independent-reference evidence;
- output-data and figure checksums; and
- documentation/validation status plus known limitations.

Passing a software test does not automatically validate a physics claim. A
result becomes publication-ready only when its stated acceptance criteria,
configuration, source commits, output data, and plotting procedure are reviewed
together.

The imported [DASC source overview](dasc/index.md) contains the current public
result-freeze rule. Detailed reusable manifests and the validation matrix will
be added only after their upstream sources are individually approved.

