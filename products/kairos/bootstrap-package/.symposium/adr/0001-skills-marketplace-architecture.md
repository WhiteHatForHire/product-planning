# ADR 0001: Skills Marketplace Architecture for Symposium OS

**Date**: 2026-05-16
**Status**: Accepted
**Authors**: Marcus Vale / Symposium Studios

## Context

Symposium Studios has developed a set of recurring patterns across builds (Anchor, Kairos, others): AUTONOMY_LAYER for execution doctrine, META_PROMPT for spec-to-directive conversion, API Surface Diagnostic, Deployment Preflight, MCP Write Safety, Build Report Ledger, Council Review, Public Surface QA. These patterns currently live scattered across build logs, chat conversations, and ad-hoc documentation.

Without a structured home, these patterns suffer from:
- Drift (each new project reinvents them slightly)
- Discoverability (new agents and collaborators cannot find them)
- Composability (no way to invoke a pattern by name from within a directive)
- Demonstrability (no public artifact showcases the Symposium method)

## Decision

Adopt a `.symposium/` folder structure at the root of every Symposium project. The folder contains:

- `AUTONOMY_LAYER.md` (kernel: protocol that agents always apply)
- `META_PROMPT.md` (compiler: spec-to-directive converter)
- `CONTEXT.md` (language layer: project-specific glossary)
- `skills/[category]/[name]/SKILL.md` (libraries: invocable named patterns)
- `templates/` (scaffolds: directive, handoff, build report, ADR)
- `adr/` (decision archive: immutable records of non-obvious choices)

Skills are organized by action mode: planning, diagnostics, execution, review, handoff.

## Consequences

### Positive
- Symposium build method becomes a portable, version-controlled artifact.
- Skills compose: a directive can reference `.symposium/skills/diagnostics/api-surface-diagnostic/` instead of inlining the entire pattern.
- The folder is a public proof artifact when the repo is public.
- New projects inherit the baseline by copying `.symposium/` and filling in `AUTONOMY_LAYER.md` section 0.1 (stack).

### Negative
- Maintenance overhead: skills must be kept up to date as patterns evolve.
- Risk of skill bloat: if every minor pattern becomes a skill, the marketplace loses focus.
- ADRs require discipline: only write ADRs for hard-to-reverse, non-obvious, real-trade-off decisions.

### Neutral
- Versioning is asymmetric: `AUTONOMY_LAYER.md` and `META_PROMPT.md` are versioned files; skills evolve in place.

## Alternatives Considered

- **Long chat prompts and memory only**: rejected because patterns are lost between sessions and across collaborators.
- **A single monolithic `RULES.md`**: rejected because monolithic files are hard to navigate and update. Composability suffers.
- **Per-project custom agent platform (Cursor rules, etc.)**: rejected because it locks Symposium into one tool. Skills should work across Claude, Codex, and future agents.

## References

- `.symposium/README.md`
- Levelingup doc: `docs/levelingup/symposium-os-skills-marketplace.md` (parked, post-Tech-Week)
- Anchor edition v1.3 of AUTONOMY_LAYER and META_PROMPT (precursor)
