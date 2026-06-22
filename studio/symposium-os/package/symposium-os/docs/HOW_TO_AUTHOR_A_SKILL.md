# How to Author a Skill

Skills are the libraries of Symposium OS. They encode hard-won lessons as named, invocable patterns. This document is for operators authoring new skills, either project-specific or canonical.

---

## When to author a skill

A skill is worth writing when **all three** of the following are true:

1. The pattern has been applied at least twice and worked both times.
2. The pattern is not obvious from the protocol (`AUTONOMY_LAYER.md`) alone — it requires judgment about when to invoke and what to check.
3. Future invocations would benefit from a named reference point instead of re-deriving the pattern from memory.

Skills that fail any of these become noise. The marketplace becomes harder to navigate, agents waste tokens reading irrelevant skills, and the cost of finding the right skill exceeds the cost of re-deriving the pattern.

If the pattern is fully captured by an existing protocol section, don't write a skill — reference the protocol section.

If the pattern is a one-off, capture it in a run note or an ADR, not a skill.

---

## Project-specific vs canonical

**Project-specific skills** live in the project's `.symposium/skills/` directory. Append them as failure modes and patterns specific to that project's domain emerge.

**Canonical skills** live in `template/skills/` in the Symposium OS repo. To promote a project-specific skill to canonical, see `PROMOTING_PROJECT_LEARNINGS.md`. The bar is the rule of three: the pattern must recur across three or more projects.

Do not jump to canonical. Start project-specific. Promote later.

---

## Skill anatomy

Every skill is a single file: `skills/[category]/[name]/SKILL.md`.

The categories correspond to action modes in a build session:
- **planning** — before code (directive generation, planning interviews, scope review)
- **diagnostics** — read state (API truth tables, feed validation, contract verification)
- **execution** — write state (MCP write safety, deployment preflight, dangerous operations)
- **review** — gate state (council review, public surface QA, build report ledger)
- **handoff** — transfer state (agent-to-agent context, session boundaries)

If a skill doesn't fit cleanly into one of these, it's probably not shaped right. Reconsider the boundaries before forcing it in.

---

## SKILL.md structure

```markdown
---
name: [skill-name-kebab-case]
category: [planning | diagnostics | execution | review | handoff]
trigger: [One-sentence description of when this skill applies.]
---

# [Skill Name In Title Case]

## Purpose
[One paragraph, ideally one sentence. The outcome this skill produces.]

## When to invoke
- [Trigger condition]
- [Trigger condition]
- [Trigger condition]

## Inputs
- [What the skill needs to run]
- [What the skill needs to run]

## Process
1. [Numbered step]
2. [Numbered step]
3. [Numbered step]

## Output
[Description of the artifact this skill produces. Reference a template in `templates/` if structured.]

## Stop conditions
- [When the skill should halt and surface to the operator]
- [When the skill should halt and surface to the operator]

## Related
- [Cross-reference to protocol sections, other skills, templates]
- [Cross-reference to protocol sections, other skills, templates]
```

---

## Authoring guidelines

**Voice**: imperative, addressed to the agent or operator running the skill. Not prose. Not narrative.

**Specificity**: a skill that says "check the API" is useless. A skill that says "read the actual route handlers, list each endpoint with method/path/auth/runtime, extract request and response shapes from runtime validation" is useful. Be specific enough that the skill can be executed without further guidance.

**Stop conditions are mandatory**: every skill must list when it halts. Skills without stop conditions silently fail and surface nothing. The whole point of a named skill is to make halting a first-class behavior.

**Cross-reference, don't duplicate**: if the skill leans on `AUTONOMY_LAYER.md` section 1.13, reference the section by number. Do not restate the section. Drift between the skill and the protocol is a real failure mode.

**Examples are optional but powerful**: worked examples inside a skill (especially for diagnostics) make the skill executable without external context. The `feed-diagnostic` skill includes an ICS worked example for exactly this reason.

---

## Anti-patterns

- **Skills that wrap a single shell command.** That's a script, not a skill. Put it in the repo's tooling.
- **Skills that restate the protocol.** Reference the protocol instead.
- **Skills with no stop conditions.** Silent failure mode. Reject.
- **Skills that span multiple categories.** Split into two skills, one per category.
- **Skills with implementation details that change frequently.** Skills are stable patterns. If the implementation changes every sprint, the skill is at the wrong altitude.
- **Skills authored by an agent without operator review.** Agents are good at finding patterns; operators are better at judging which patterns are worth formalizing.

---

## Checklist before merging a new skill

- [ ] Pattern has been applied at least twice successfully.
- [ ] Category is correct (planning/diagnostics/execution/review/handoff).
- [ ] SKILL.md follows the structure above.
- [ ] Stop conditions are listed.
- [ ] Cross-references are correct (verify section numbers in `AUTONOMY_LAYER.md`).
- [ ] If the skill produces a structured artifact, a template exists in `templates/`.
- [ ] If the skill is project-specific: appended to the project's `skills/`. Not promoted to canonical.
- [ ] If the skill is canonical: rule of three is satisfied. Promotion documented per `PROMOTING_PROJECT_LEARNINGS.md`.
