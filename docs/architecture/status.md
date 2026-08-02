# Controlled documentation status

Status labels communicate review state; they do not create scientific evidence or publication permission. A label may be applied only by the content owner or a documented review process, and the evidence must be recorded in publication metadata or a review record.

## Vocabulary

| Label | Meaning | Minimum evidence |
| --- | --- | --- |
| Draft | Content is being developed and is not approved as authoritative guidance. | Identified owner and source revision; visible draft warning if publicly previewed |
| Reviewed | Content was checked for technical meaning, public suitability, links, attribution, and license. | Reviewer identity or review record, reviewed commit, and review date |
| Reference | Content defines a version-scoped interface, format, convention, or vocabulary. | Reviewed source, applicable project/version, and evidence that the owning project designates it as reference material |
| Validated | A stated result or procedure has passed a defined validation process. | Named validation method, inputs/version, acceptance criteria, result, date, and responsible reviewer |
| Unvalidated | Content describes a result or procedure without completed validation evidence. | Explicit limitation statement, scope, source revision, and owner acknowledgement |
| Superseded | Content remains available for history but has a reviewed replacement. | Link to the replacement, supersession decision, affected versions, and date |
| Released | Content belongs to an identified public project release. | Immutable release identifier or tag, release URL, project, and release date |

“Reviewed” does not mean “Validated,” and “Released” does not automatically mean either. “Reference” describes the function of a page, not its scientific validity.

## Where labels may appear

- Structured source-publication metadata.
- Generated page provenance or a visible status banner near the page title.
- A versioned documentation inventory.
- Release-readiness and content-review records.

Labels must not be inferred from directory names, prose tone, a passing site build, repository visibility, or the existence of a Git tag.

## Application rules

1. Record one lifecycle/review label where applicable: Draft, Reviewed, Superseded, or Released.
2. Add Reference only when the owning project explicitly assigns a reference role.
3. Add Validated or Unvalidated only where a scientific or procedural validation claim is relevant.
4. Record the evidence for every label; an unsupported label is an error.
5. Display the project and version or immutable revision with the label.
6. Never translate “tests passed” into scientific validation unless the approved validation definition says those tests are sufficient.
7. When evidence expires or a replacement is approved, update or supersede the status rather than silently removing context.

## Examples of valid combinations

- `Reviewed · Reference` for an approved, version-scoped interface definition.
- `Released · Validated` when a specific release includes content backed by recorded validation evidence.
- `Draft · Unvalidated` for an explicitly limited preview when public preview is approved.
- `Superseded · Reference` for an older reference page retained with a link to its replacement.

These examples define label semantics only; they do not assign a status to any current PyDASC or DASC document.
