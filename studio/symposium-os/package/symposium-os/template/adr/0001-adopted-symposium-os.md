# ADR 0001: Adopted Symposium OS for [Project Name]

**Date**: YYYY-MM-DD
**Status**: Accepted
**Authors**: [name(s)]

## Context

This project requires structured autonomous agent work, language consistency across sessions, and reproducible build patterns. The operator has standardized on Symposium OS for these capabilities across projects.

## Decision

Adopt Symposium OS canonical version [VERSION] as the execution scaffold for this project.

The `.symposium/` folder is the project's local copy of the OS `template/` directory, tailored at init time to:
- This project's stack (`AUTONOMY_LAYER.md` section 0.1)
- This project's ubiquitous language (`CONTEXT.md`)
- This project's first architectural decisions (subsequent ADRs)

## Consequences

### Positive
- Autonomous agents have a shared protocol they unconditionally obey.
- Skills compose across sessions and across agents.
- New collaborators (human or AI) can read `.symposium/` to onboard without re-learning project conventions.

### Negative
- Drift risk if the project's `.symposium/` falls behind canonical Symposium OS releases.
- Upgrade cost: each canonical version bump requires a diff-and-merge against the project's local copy.

### Neutral
- Project-specific patterns appended to `AUTONOMY_LAYER.md` section 2.3 do not flow back to canonical automatically. Promote them via the OS-level process documented at `[link to Symposium OS repo]/docs/PROMOTING_PROJECT_LEARNINGS.md`.

## Alternatives Considered

- **No structured scaffold (ad-hoc agent instructions per session)**: rejected. Drift across sessions and across agents was the original problem.
- **A different framework (Cursor rules, Aider config, etc.)**: rejected. Locks the project to one agent runtime; Symposium OS is runtime-agnostic.

## References

- Symposium OS canonical: [link to repo, with version tag]
- `.symposium/AUTONOMY_LAYER.md` (this project's local copy)
- `.symposium/CONTEXT.md` (this project's ubiquitous language)
