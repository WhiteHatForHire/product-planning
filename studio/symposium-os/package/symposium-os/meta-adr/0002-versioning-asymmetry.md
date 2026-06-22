# Meta-ADR 0002: Versioning Asymmetry Between Protocol and Skills

**Date**: 2026-05-18
**Status**: Accepted
**Authors**: Symposium OS

## Context

Symposium OS has multiple artifact types: the protocol (`AUTONOMY_LAYER.md`), the spec-to-directive compiler (`META_PROMPT.md`), invocable skills (`skills/[category]/[name]/SKILL.md`), scaffold templates (`templates/`), and architecture decision records (`adr/`, `meta-adr/`).

A natural assumption is that everything in the OS should version together: when canonical bumps, every artifact gets a new version number, and projects upgrade everything in lockstep.

In practice, that creates friction. Skills evolve incrementally as patterns clarify; bumping a version on every typo fix in a SKILL.md is noise. Meanwhile, protocol changes (e.g., adding section 1.15 in v2.0) genuinely require operator attention and a migration step.

## Decision

Apply asymmetric versioning across artifact types:

- **`AUTONOMY_LAYER.md`** and **`META_PROMPT.md`** carry semantic version numbers and ship together. They are the contract.
- **Skills** evolve in place. No individual version numbers. They reflect the state of the canonical at any given commit.
- **Templates** (in `template/templates/`) evolve in place. No version numbers.
- **In-template `README.md`** and **`CONTEXT.md`** template evolve in place. No version numbers.
- **ADRs** are immutable once accepted. Each ADR has a date and status; superseded ADRs are replaced by new ADRs, not edited.

The canonical version number is the version of `AUTONOMY_LAYER.md` at any given release. When that bumps, the full `template/` directory ships as a coherent release. Skills, templates, and other unversioned artifacts are assumed to be at "current canonical" by reference.

## Consequences

### Positive
- Skills can be improved continuously without ceremony. A typo fix in a SKILL.md does not require a version bump.
- The protocol stays stable. Version bumps signal real changes operators need to evaluate.
- ADR immutability protects the historical record. Decisions don't quietly change after the fact.

### Negative
- A project on canonical v2.0 cannot easily tell which skills are "v2.0 skills" vs "v2.1 skills" if they care to compare. The skills carry no version stamps.
- The canonical version number does not capture skill-level changes. CHANGELOG.md must explicitly note when a release includes meaningful skill updates.

### Neutral
- Operators upgrading a project pull the entire `template/` at the new canonical version, which includes any skill evolution since the project's last upgrade. This is intentional: skills move forward when the protocol does.

## Alternatives Considered

- **Uniform versioning across all artifacts**: rejected because it creates ceremony around minor skill improvements and slows iteration.
- **Per-skill version numbers**: rejected because it complicates the upgrade procedure (operator must reconcile multiple version numbers per upgrade) without commensurate benefit.
- **No versioning at all**: rejected because protocol changes are real and operators need a stable contract to depend on.

## References

- `docs/VERSIONING.md` — implementation of this decision
- `meta-adr/0001-skills-marketplace-architecture.md` — the architecture this versioning supports
- `CHANGELOG.md` — the canonical version history
