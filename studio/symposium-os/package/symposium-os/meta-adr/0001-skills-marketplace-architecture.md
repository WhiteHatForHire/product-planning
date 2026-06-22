# Meta-ADR 0001: Skills Marketplace Architecture for Symposium OS

**Date**: 2026-05-16
**Status**: Accepted
**Authors**: Symposium OS

## Context

Across multiple projects, a recurring set of patterns has emerged for directed AI agent work: `AUTONOMY_LAYER` for execution doctrine, `META_PROMPT` for spec-to-directive conversion, API Surface Diagnostic, Feed Diagnostic, Deployment Preflight, MCP Write Safety, Build Report Ledger, Council Review, Public Surface QA, Session Handoff. Without a structured home, these patterns suffer from:

- **Drift** — each new project reinvents them slightly differently
- **Discoverability** — new agents and collaborators cannot find them
- **Composability** — no way to invoke a pattern by name from within a directive
- **Demonstrability** — no public artifact showcases the method

## Decision

Adopt a `.symposium/` folder structure at the root of every project using this method. The folder is a copy of the Symposium OS canonical `template/` directory, tailored at init time. It contains:

- `AUTONOMY_LAYER.md` (kernel: protocol that agents always apply)
- `META_PROMPT.md` (compiler: spec-to-directive converter)
- `CONTEXT.md` (language layer: project-specific glossary)
- `skills/[category]/[name]/SKILL.md` (libraries: invocable named patterns)
- `templates/` (scaffolds: directive, handoff, build report, ADR)
- `adr/` (decision archive: immutable records of non-obvious choices)

Skills are organized by action mode: planning, diagnostics, execution, review, handoff.

## Consequences

### Positive
- The build method becomes a portable, version-controlled artifact.
- Skills compose: a directive can reference `.symposium/skills/diagnostics/api-surface-diagnostic/` instead of inlining the entire pattern.
- The folder is a public proof artifact when the repo is public.
- New projects inherit the baseline by copying `template/` and tailoring via init.
- Improvements promote upward: a pattern that recurs across three or more projects gets promoted from project-specific (section 2.3 of `AUTONOMY_LAYER.md`) to canonical.

### Negative
- Maintenance overhead: skills must be kept up to date as patterns evolve.
- Risk of skill bloat: if every minor pattern becomes a skill, the marketplace loses focus.
- ADRs require discipline: only write ADRs for hard-to-reverse, non-obvious, real-trade-off decisions.

### Neutral
- Versioning is asymmetric: `AUTONOMY_LAYER.md` and `META_PROMPT.md` are versioned files; skills evolve in place; ADRs are immutable once accepted. See `meta-adr/0002-versioning-asymmetry.md`.

## Alternatives Considered

- **Long chat prompts and memory only**: rejected because patterns are lost between sessions and across collaborators.
- **A single monolithic `RULES.md`**: rejected because monolithic files are hard to navigate and update; composability suffers.
- **Per-tool custom agent platform (vendor-locked rules)**: rejected because it locks the method into one tool. Skills should work across any agent runtime.

## References

- `README.md`
- `template/README.md`
- `template/AUTONOMY_LAYER.md` (Symposium OS Canonical Edition v2.1)
- `template/META_PROMPT.md` (Symposium OS Canonical Edition v2.1)
- `meta-adr/0002-versioning-asymmetry.md` — related decision on versioning
- `meta-adr/0003-template-vs-init-split.md` — related decision on template vs init separation
