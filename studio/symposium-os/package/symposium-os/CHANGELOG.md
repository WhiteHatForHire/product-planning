# Changelog

All notable changes to the canonical Symposium OS releases.

The format is based on Keep a Changelog. Symposium OS uses semantic-ish versioning: major version bumps for incompatible protocol changes, minor for additive doctrine, patch for clarifications and typo fixes.

---

## [2.3] — 2026-05-19

### Added
- Four new canonical skills, each motivated by patterns that recurred across enough sessions to earn a name:
  - `template/skills/planning/production-bug-triage/` — convert user-reported bugs into scoped, sequenced fix directives. Replaces the "fix one, ship, find next, repeat" pattern that doesn't compound.
  - `template/skills/planning/directive-audit-revise/` — apply external lenses to a draft directive before firing. Catches brittle assertions, phase dependencies, scope drift, and tier mismatches before they consume a run.
  - `template/skills/planning/model-routing/` — pick the right agent capability tier per directive type. Routing matrix covers spec-to-directive, architectural decisions, mechanical execution, batch processing.
  - `template/skills/review/post-run-mortem/` — short retrospective after a multi-phase directive completes. Distinct from `build-report-ledger` (the receipt); the mortem is the lessons.
- Two new templates:
  - `template/templates/cross-platform-handoff-template.md` — handoff when an in-flight directive must continue on a different agent runtime (e.g., Claude → Codex due to credit limits).
  - `template/templates/qa-tester-onboarding-template.md` — brief for onboarding a junior QA tester to file structured bug reports against a project.
- New meta-ADR:
  - `meta-adr/0004-stabilization-before-optimization.md` — the phronesis principle. When the visible product is incoherent, stop optimizing the engine; stabilize the integration loop first.
- New top-level explainer:
  - `OVERVIEW.md` — complete file map of the OS. One paragraph per file explaining what it does, when to read it, how it relates to the others. Companion to `README.md` for navigation.

### Changed
- `template/templates/directive-template.md`: added `## Non-Goals` section immediately after `## Role`. Explicit non-goals prevent scope drift during stabilization directives in particular. Omit only when scope is small enough that drift isn't a risk.
- `template/AUTONOMY_LAYER.md`: version header bumped to v2.3. No semantic protocol changes; the version bump tracks the canonical release that includes the new skills, templates, and meta-ADR above.
- `template/META_PROMPT.md`: version header bumped to v2.3 in lockstep with `AUTONOMY_LAYER.md`.

### Archived
- `archive/AUTONOMY_LAYER-v2.2.md` — verbatim snapshot of the v2.2 canonical.

### Migration from v2.2
- No protocol changes. v2.3 is fully backward-compatible with v2.2 directives.
- Existing project copies of `.symposium/` can pull `template/templates/directive-template.md` (with Non-Goals section) and the four new skills on demand. Update the project's `template/AUTONOMY_LAYER.md` version header to v2.3 when convenient.
- New directives should populate the Non-Goals section explicitly. Existing in-flight directives do not need to be revised.

---

## [2.2] — 2026-05-18

### Added
- `AUTONOMY_LAYER.md` section 3 EXECUTION: docs-only smoke validation rule. Documentation-only and template-only phases use validation checks (paths resolve, cross-references resolve, no unfilled placeholders, markdown parses) instead of test code. Prevents agents from inventing unit tests for files with no runtime.
- `AUTONOMY_LAYER.md` section 1.15: explicit "no halt between phases" clarification. Agents open each PR in a stacked chain and immediately continue to the next phase. The operator merges all PRs in order after the full run completes. Applies whether `Auto-merge: yes` or `Auto-merge: no`.
- `META_PROMPT.md` rule 19: directing AIs must NOT generate directives containing "operator merges each PR before the next phase begins" or equivalent halt-per-merge language.

### Changed
- `template/templates/directive-template.md`: Phase Plan section now states "No halt between phases" explicitly at the top and notes end-of-phase behavior in each phase.
- `template/skills/planning/generate-directive/SKILL.md`: added stop condition that halts directive generation if the draft contains halt-per-merge language.

### Migration from v2.1
- Existing directives with "operator merges each phase before the next begins" language are malformed under v2.2. Either rewrite to the no-halt pattern, or split into separate directives (one per phase) if per-phase review gating is genuinely required.
- No changes to project-side `AUTONOMY_LAYER.md` files needed beyond a version-header bump. Section 1.15 was already in v2.1; v2.2 only clarifies behavior that was already canonical.

---

## [2.1] — 2026-05-18

### Added
- `AUTONOMY_LAYER.md` section 1.15 sub-section: "Sequential merge maintenance" — formalizes how the agent maintains a stacked PR chain across a sequential merge sequence without requiring a re-fired directive per merge.
- `AUTONOMY_LAYER.md` section 0.6: Operator-Agent contract — clarifies ownership boundaries between the human operator and the executing agent.

### Changed
- `AUTONOMY_LAYER.md` section 0.1 stripped of all stack assumptions. Now a true blank template that each project fills in.
- All personal and project-specific references removed throughout the protocol.
- Command examples generalized to operator-agnostic placeholders.

### Migration from v2.0
- Replace `BLOCKERS_FOR_MARCUS.md` references with `BLOCKERS_FOR_OPERATOR.md` in any project copy.
- Re-read section 1.15 for the new sequential-merge protocol.
- Read section 0.6 to confirm the project's operator/agent split matches the canonical contract.

---

## [2.0] — 2026-05

### Added
- `AUTONOMY_LAYER.md` section 1.15: Stacked PR conflict resolution protocol — Tier 1/2/3 conflict resolution rules, squash-merge SHA drift detection, `--onto` rebase pattern.
- `GENERIC-12` self-repair entry: stale dependencies after squash-merge pull.

### Changed
- "Accept incoming" clarified as NOT a blanket rule — applies only to Tier 1 files.
- Post-rebase verification (typecheck, build, test) made mandatory before push.

### Migration from v1.4
- Adopt the Tier 1/2/3 file classification for any project doing stacked PR work.
- Add `GENERIC-12` to project repair playbooks.

---

## [1.4] — 2026

### Added
- MCP write safety preflight protocol (section 1.12) — hard-stop checks for placeholder-pattern truncation.
- Spec-reality reconciliation requirement (section 1.13).

### Changed
- Working files moved from singleton root files to session-scoped paths under `docs/run-notes/` to eliminate parallel-agent merge conflicts.

---

## [1.3] — 2026

### Added
- First reusable canonical edition stripped of project-specific stack assumptions.
- Self-repair playbook with `GENERIC-N` and `WORKTREE-N` entries.

### Changed
- Section 0.1 became a fill-in template per project.

---

## Versioning policy

See `docs/VERSIONING.md` for the full policy, including:
- When to bump major / minor / patch
- How to ship a new canonical
- How projects upgrade
- How project-specific patterns get promoted to canonical
