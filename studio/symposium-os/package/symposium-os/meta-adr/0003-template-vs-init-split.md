# Meta-ADR 0003: Template/Init Split

**Date**: 2026-05-18
**Status**: Accepted
**Authors**: Symposium OS

## Context

Symposium OS needs to do two things when a project adopts it:

1. **Provide a baseline scaffold** — the protocol, the skills, the templates, the in-template documentation. Same for every project. Versioned and stable.
2. **Tailor the scaffold to the project** — fill in the stack, the ubiquitous language, the first architectural decision. Different per project. Dynamic and operator-driven.

A naive approach is to combine these: one interactive scaffold-generator that asks operator questions and emits a tailored `.symposium/` directly. But this couples the static baseline to the dynamic interview, which creates two problems:

- **Baseline upgrades are harder** because the operator can't just diff a static directory against the new canonical. They'd have to re-run the generator with the new logic and reconcile against the project's tailored state.
- **Multiple interview styles can't coexist.** Some operators want a heavy interview with stack-discovery questions. Others want a fast preset-driven init. Some teams will want a custom interview for their own conventions. Coupling these to the baseline forces one style on everyone.

## Decision

Separate the static baseline (`template/`) from the dynamic init step (`init/`).

`template/` is the canonical, versioned scaffold. It contains:
- The protocol (`AUTONOMY_LAYER.md`)
- The spec-to-directive compiler (`META_PROMPT.md`)
- The blank `CONTEXT.md` template
- The blank in-template `README.md`
- All canonical skills
- All scaffold templates
- The placeholder `adr/0001-adopted-symposium-os.md`

`init/` is the interview system that tailors a fresh copy of `template/` into a project. It contains:
- `INIT_PROMPT.md` — the operator-authored interview prompt
- `stack-presets/` — short-circuit configurations for common stacks
- `POST_INIT_CHECKLIST.md` — verification after init runs

Adoption flow:
1. Copy `template/` into the project root as `.symposium/`.
2. Run the init step against the copied template.
3. Run the post-init checklist to verify.

Template upgrades follow `docs/VERSIONING.md`: diff the project's `.symposium/` against the new `template/` and merge. Init upgrades are separate: operators can author or revise their `INIT_PROMPT.md` without touching `template/`.

## Consequences

### Positive
- Template upgrades are mechanical diff-and-merge. No interview replay required.
- Operators can author and version their own init prompts independently.
- Multiple init styles coexist: one operator's heavy interview, another's preset-driven init, a team's custom flow.
- Static template is easier to audit, vendor, and re-distribute as an artifact.

### Negative
- Two-step adoption (copy template, then run init) is heavier than a one-step generator.
- New adopters need to understand the distinction. Documentation overhead.
- If init prompts diverge significantly across operators, projects adopting Symposium OS can have inconsistent tailoring.

### Neutral
- The init step itself is intentionally not versioned. Operators own their init flow and can revise it freely.
- The relationship is one-way: the template can be upgraded without touching init, but a new init can only fill in what the current template exposes.

## Alternatives Considered

- **Single interactive scaffold-generator**: rejected for the coupling reasons above. Operators lose flexibility, upgrades become harder, and the canonical becomes harder to audit as a standalone artifact.

- **No init step — operator fills in blanks manually**: rejected because manual fill-in is error-prone (operators skip fields, leave placeholders, forget to verify). The interview enforces completeness, and `POST_INIT_CHECKLIST.md` makes the verification explicit.

- **Init prompt lives inside `template/` rather than a sibling directory**: rejected because then `template/` carries operator-specific interview style, which contradicts the goal of canonical neutrality.

## References

- `docs/VERSIONING.md` — upgrade procedure that depends on template being static
- `init/README.md` — what the init system does
- `init/POST_INIT_CHECKLIST.md` — the verification step
- `meta-adr/0001-skills-marketplace-architecture.md` — the structural architecture this split sits inside
