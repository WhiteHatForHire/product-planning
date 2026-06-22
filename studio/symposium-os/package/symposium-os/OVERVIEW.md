# Symposium OS — Complete File Overview

Every file in the Symposium OS repo, what it does, when to read it, and how it relates to the others. Use this as a map when you can't remember where something lives.

Canonical version: **v2.3**

---

## Quick reference: "When I want to..."

| When I want to... | Read this |
|---|---|
| Understand what Symposium OS is | `README.md`, then `PHILOSOPHY.md` |
| Adopt the OS in a new project | `init/INIT_PROMPT.md` |
| Generate a build directive | `template/META_PROMPT.md` + `template/skills/planning/generate-directive/SKILL.md` |
| Audit a directive before firing | `template/skills/planning/directive-audit-revise/SKILL.md` |
| Pick the right agent tier | `template/skills/planning/model-routing/SKILL.md` |
| Triage production bugs | `template/skills/planning/production-bug-triage/SKILL.md` |
| Hand off across runtimes | `template/templates/cross-platform-handoff-template.md` |
| Onboard a QA tester | `template/templates/qa-tester-onboarding-template.md` |
| Mortem a completed run | `template/skills/review/post-run-mortem/SKILL.md` |
| Upgrade a project to a new canonical | `docs/VERSIONING.md` |
| Promote a project pattern to canonical | `docs/PROMOTING_PROJECT_LEARNINGS.md` |
| Decide whether to stop optimizing | `meta-adr/0004-stabilization-before-optimization.md` |
| Check the protocol contract | `template/AUTONOMY_LAYER.md` |
| Look up project vocabulary | The project's own `.symposium/CONTEXT.md` |

---

## Top-level files

These live at the root of the Symposium OS repo. They describe and version the OS itself.

### `README.md`
The entry point. Explains what Symposium OS is, who it's for, how the directory is laid out, and how to adopt it in a project. First file to read.

### `PHILOSOPHY.md`
The operating philosophy. The three-layer model (memory / judgment / language), the Director Model contract, why doctrine is non-negotiable, why skills are libraries and not rules, why promotion is rule-of-three. Read this when wondering why the system is shaped the way it is.

### `CHANGELOG.md`
Version history for the canonical protocol. Each entry covers what was added, what changed, and how to migrate. Read this when upgrading a project to a new canonical version.

### `OPERATOR_NOTES.md`
Internal operator-facing context that should NOT be in the public-facing canonical files. Captures decisions still pending (license, public/private status), patterns that should not be promoted to canonical, and open questions about how the OS itself should evolve. Read this before sharing the repo externally.

### `OVERVIEW.md`
This file. The map of every file in the repo.

---

## `template/` — the canonical scaffold copied into projects

The `template/` directory is the canonical `.symposium/` that gets copied into every project that adopts Symposium OS. After copying, projects run `init/INIT_PROMPT.md` to tailor the template to their stack and domain.

Strip nothing from `template/`. Customize only via section 0.1 (stack) of `AUTONOMY_LAYER.md`, section 2.3 (project-specific repair entries), `CONTEXT.md` content, and per-project ADRs.

### `template/README.md`
In-template README. Explains how to navigate `.symposium/` from inside a project. Shorter and more practical than the OS-level `README.md`.

### `template/AUTONOMY_LAYER.md` (v2.3)
The protocol. The contract agents unconditionally obey when executing a directive. Covers:
- Scope review and directive header format (section 0)
- Tiered self-repair: self-heal → defer → hard stop (section 1)
- Atomic commits, no silent failures, production safety boundaries (sections 1.9–1.11)
- MCP write safety preflight (section 1.12)
- Spec-reality reconciliation (section 1.13)
- Open-PR check before rebase (section 1.14)
- Stacked PR conflict resolution and sequential merge maintenance (section 1.15)
- Self-repair playbook with GENERIC entries and project-specific section 2.3 (section 2)
- Phase execution protocol (section 3)
- Deferred-issues and BUILD_REPORT formats (sections 4–5)
- Hard stop conditions (section 6)

This file is the most important file in the entire OS. Read it before writing any directive.

### `template/META_PROMPT.md` (v2.3)
The compiler. The prompt the operator pastes into a fresh chat with a directing AI to convert a project spec into a runnable directive. Encodes the rules a directive must follow (acceptance criteria split, fallback content specification, no halt between phases, etc.). Used in conjunction with `template/skills/planning/generate-directive/`.

### `template/CONTEXT.md`
The language layer. Project-specific glossary. Empty in the canonical template; filled in during init. Contains Product terms, Domain terms, Architecture terms, Symposium terms (carry over), and Anti-vocabulary. Read first when joining a session on an unfamiliar project.

### `template/adr/0001-adopted-symposium-os.md`
Placeholder for the project's first architecture decision record, marking adoption of Symposium OS. Filled in during init. Subsequent project ADRs are appended as 0002, 0003, etc.

---

## `template/skills/` — invocable named patterns

Skills are libraries. Each is a named pattern with explicit trigger conditions, inputs, process steps, outputs, and stop conditions. Invoke a skill by name from within a directive or directly from operator context.

Categories correspond to action modes in a build session: **planning**, **diagnostics**, **execution**, **review**, **handoff**.

### Planning skills (before code)

#### `template/skills/planning/generate-directive/`
**When**: A spec is ready and needs to be converted into a runnable build directive.
**Output**: A single Markdown directive file using `templates/directive-template.md` as the scaffold.
**Stops if**: Stack section unfilled, CONTEXT.md unfilled, fallback content not specified, more than 10 phases needed without parallel split, draft contains halt-per-merge language.

#### `template/skills/planning/grill-with-docs/`
**When**: Before introducing new domain terminology or clarifying ambiguous concepts.
**Output**: A grill report listing resolved glossary terms, open ambiguities, recommended ADRs, code paths checked.
**Stops if**: Plan introduces terms conflicting with `CONTEXT.md` anti-vocabulary; more than 5 critical ambiguities surface.

#### `template/skills/planning/production-bug-triage/`
**When**: Real-user testing or production usage surfaces multiple bugs that need scoped, sequenced fixes.
**Output**: A bug triage report grouping bugs by layer, sequencing fix directives, surfacing operator decisions.
**Stops if**: Bug is safety-adjacent; bug requires reopening a locked architectural decision; bug list is too large for one triage session.

#### `template/skills/planning/directive-audit-revise/`
**When**: Before firing a high-stakes or long-running directive (more than 3 phases or 90 minutes of agent time).
**Output**: A revision diff plus an audit log with must-fix, should-fix, and nit findings.
**Stops if**: Must-fix findings cannot be applied without changing scope; lenses disagree on severity; multi-model audit produces sharply divergent findings.

#### `template/skills/planning/model-routing/`
**When**: Before firing any directive, when choosing which agent capability tier to assign.
**Output**: A routing note appended to the directive header and `AUTONOMOUS_RUN_LOG.md` with tier and rationale.
**Stops if**: Work type doesn't fit any row in the routing matrix; operator's budget can't support the recommended tier; a single phase would bounce between tiers.

### Diagnostics skills (read state)

#### `template/skills/diagnostics/api-surface-diagnostic/`
**When**: Before any frontend, mobile, or integration wave that touches backend APIs.
**Output**: A truth table listing endpoints with method, path, auth, runtime, request shape, response shape, error variants, and any spec deltas.
**Stops if**: Route handlers reference modules or types that don't exist; auth requirement is unclear at any endpoint.

#### `template/skills/diagnostics/feed-diagnostic/`
**When**: Before any wave that depends on an external feed, API, or scraped data source structure.
**Output**: A feed report with record counts, field presence percentages, duplicate counts, format anomalies, baseline drift summary, sample records, recommended ingest assertions.
**Stops if**: Record count is more than 25% off baseline; required field has under 90% presence; timezone info is missing on time-bearing data; primary key has duplicates and no dedup strategy exists.

### Execution skills (write state)

#### `template/skills/execution/mcp-write-safety/`
**When**: Before any MCP-based remote file write, especially on files over 5KB or append-only logs.
**Output**: A pre-write checklist log and either a confirmed write with post-write verification, or a blocked-write log with fallback action.
**Stops if**: Outgoing byte length is under 25% of remote size; content matches placeholder patterns; remote SHA cannot be verified; post-write byte length doesn't match expected.

#### `template/skills/execution/deployment-preflight/`
**When**: Before any deploy to production, staging, or a new environment.
**Output**: A preflight checklist showing pass/fail per environment item, with the deploy command staged at the bottom.
**Stops if**: Any preflight check fails; production is degraded and the deploy isn't a rollback; deploy would change a production env var as part of itself.

### Review skills (gate state)

#### `template/skills/review/council-review/`
**When**: Before merging safety-adjacent PRs, publishing public surfaces, or shipping high-stakes content.
**Output**: A council report with per-lens findings, per-model findings (if multi-model), cross-conflicts surfaced, severity (block / warn / nit) per finding.
**Stops if**: Any "block" severity finding surfaces; lenses disagree on severity; lens findings can't be reconciled without operator adjudication.

#### `template/skills/review/public-surface-qa/`
**When**: Before publishing any externally-visible page or artifact.
**Output**: A QA report with pass/fail per check, screenshots or notes for fails, recommended fixes ordered by severity.
**Stops if**: Any credibility check fails (fake metric, broken proof link); mobile readability fails on primary target browser; QR destination is wrong; accessibility fails on a primary CTA.

#### `template/skills/review/build-report-ledger/`
**When**: At the end of any meaningful work session, especially autonomous build sessions.
**Output**: A `BUILD_REPORT.md` per `AUTONOMY_LAYER.md` section 5, plus an optional Compression Ledger appendix with pre-AI baseline and operator hours.
**Stops if**: Operator can't honestly cite a pre-AI baseline (skip the ratio rather than fake it); session was under one hour (compression signal is too noisy).

#### `template/skills/review/post-run-mortem/`
**When**: After a multi-phase autonomous directive completes, before the operator moves to the next work block.
**Output**: A mortem file documenting what worked, what surprised, what should change in canonical, candidates for promotion, action items.
**Stops if**: Directive run is still in flight; operator doesn't have time for a thoughtful mortem; findings cluster around a single architectural decision (those go to meta-ADR instead).

### Handoff skills (transfer state)

#### `template/skills/handoff/session-handoff/`
**When**: Passing context between agents or sessions on the same runtime, or before a context-limit cliff.
**Output**: A handoff doc at `docs/handoffs/session-YYYY-MM-DD-[slug].md` using `templates/handoff-template.md`.
**Stops if**: Next agent's objective is unclear; more than 5 open decisions; handoff would require embedding safety-adjacent content.

---

## `template/templates/` — reusable scaffolds

Templates are skeleton documents. Skills produce instances of these.

### `template/templates/directive-template.md`
The skeleton for a build directive. Used by `skills/planning/generate-directive`. Includes header block, Role, Non-Goals (added v2.3), Protocol reference, Deployment Posture, Design Data, Working Files Protocol, Phase Plan with no-halt-between-phases banner, Parallel-Agent Split, Stacked PR Chain, Directive-Specific Repair Entries, and GO instruction.

### `template/templates/handoff-template.md`
The skeleton for a same-runtime session handoff. Used by `skills/handoff/session-handoff`. Includes Objective, Current State, Durable Artifacts, Your Job, Suggested Skills, Stop Gates, Known Risks, Acceptance Criteria.

### `template/templates/cross-platform-handoff-template.md`
The skeleton for a handoff that crosses agent runtimes (e.g., Claude → Codex when credits run out). Carries extra context the destination runtime can't infer from chat history: current state, files changed, runtime-specific notes, known risks of the cross-platform handoff, acceptance criteria.

### `template/templates/build-report-template.md`
The skeleton for a build report. Used by `skills/review/build-report-ledger`. Includes Phase Outcomes table, Spec-Reality Deltas, Deferred by Severity, Test Status, Manual Verification Required, Council Review Required, Production Application Pending, Compression Ledger (optional), Next Actions.

### `template/templates/qa-tester-onboarding-template.md`
The skeleton for onboarding a junior QA tester. Includes what the project is, what the role is, setup requirements, session workflow, bug report format, escalation path, glossary, first-session checklist.

### `template/templates/adr-template.md`
The skeleton for an architecture decision record. Used both for project ADRs (in `template/adr/`) and meta-ADRs (in `meta-adr/`). Includes Date, Status, Authors, Context, Decision, Consequences (positive/negative/neutral), Alternatives Considered, References.

---

## `init/` — the tailoring system

The init step runs after a project copies `template/` into its repo as `.symposium/`. It tailors the canonical scaffold to the project's stack and domain.

### `init/README.md`
What the init system does and how to use it.

### `init/INIT_PROMPT.md` (v1.0)
The interview prompt the operator pastes into a fresh chat with a directing AI to walk through the init interview. Five blocks: stack preset check, stack reality, ubiquitous language, first ADR, operating intent, skills enablement. Output: filled section 0.1, populated CONTEXT.md, completed ADR 0001, project init log.

### `init/POST_INIT_CHECKLIST.md`
Verification steps to confirm init completed correctly. Runs after the init interview emits the tailored files.

### `init/stack-presets/`
Short-circuit configurations for common stacks. Currently stubs marked as roadmap. When populated, an operator can name a preset during the init interview and skip Block 1 (stack reality) entirely.

- `nextjs-vercel-static.yml`
- `nextjs-vercel-neon.yml`
- `expo-eas-supabase.yml`
- `python-fastapi-postgres.yml`

### `init/stack-presets/README.md`
Explains the roadmap status of stack presets and how to author a full preset when the operator is ready.

---

## `docs/` — documentation about the OS itself

These are not files projects copy. They live at the OS level and describe how the OS works.

### `docs/HOW_TO_AUTHOR_A_SKILL.md`
Guide for authoring new skills. Covers when a skill is worth writing, project-specific vs canonical, anatomy of a SKILL.md, voice guidelines, anti-patterns, the checklist before merging a new skill.

### `docs/HOW_TO_WRITE_AN_ADR.md`
Guide for authoring architecture decision records. Covers when an ADR is warranted, the structure, voice, immutability rules.

### `docs/VERSIONING.md`
The versioning policy. When to bump major vs minor, how the canonical version maps to artifact versions, how projects upgrade, the upgrade diff-and-merge procedure.

### `docs/PARALLEL_AGENTS.md`
How Symposium OS supports running multiple concurrent agents against the same project. Coordination via working files, capability differentiation, failure isolation patterns.

### `docs/PROMOTING_PROJECT_LEARNINGS.md`
The rule of three and how project-specific patterns earn canonical promotion. What can be promoted, what can't, the promotion procedure, anti-patterns in promotion.

---

## `meta-adr/` — architecture decision records about the OS itself

These are NOT project ADRs. They document architectural decisions about how Symposium OS itself is structured. Immutable once accepted. Numbered sequentially.

### `meta-adr/0001-skills-marketplace-architecture.md`
Adoption of the `.symposium/` folder structure with five skill categories. The architectural foundation of the OS.

### `meta-adr/0002-versioning-asymmetry.md`
Different artifact types version differently: `AUTONOMY_LAYER` and `META_PROMPT` carry semantic version numbers; skills and templates evolve in place; ADRs are immutable. The decision and its rationale.

### `meta-adr/0003-template-vs-init-split.md`
Why the static baseline (`template/`) and the dynamic tailoring step (`init/`) are separate directories with separate lifecycles. Makes upgrades mechanical and lets multiple init styles coexist.

### `meta-adr/0004-stabilization-before-optimization.md`
The phronesis principle. When the visible product is incoherent — state doesn't propagate, integrations announce one thing and do another — the next move is integration stabilization, not more algorithm work. Encoded operationally via Non-Goals in directives, `production-bug-triage` skill, `post-run-mortem` flagging.

---

## `case-studies/` — real worked examples

Slots for documenting real production projects' use of Symposium OS. Each case study includes a narrative summary, the directive(s) fired, the resulting build reports, council reviews, and compression ledger.

### `case-studies/README.md`
Explains the case-study format and what slots are currently filled.

### `case-studies/kairos-bootstrap/`
Slot for the Kairos initial bootstrap session.

### `case-studies/kairos-rescue/`
Slot for the Kairos rescue session that recovered the project from a broken state.

Case studies are pending. Slots exist; artifacts will be added when projects ship and publishing is approved.

---

## `archive/` — historical canonical versions

Versioned snapshots of `AUTONOMY_LAYER.md` from prior canonical releases. Internal historical material — kept for reference and migration verification. May contain operator-specific language predating generalization. See the archive README for the internal-only marker.

### `archive/README.md`
Explains the historical/internal status of the archive.

### `archive/AUTONOMY_LAYER-v1.3.md`
Symposium Generic Edition v1.3. Earlier reusable canonical, predating the v2.0 split between OS-level canonical and project-level template.

### `archive/AUTONOMY_LAYER-v2.1.md`
Symposium OS Canonical Edition v2.1. Predecessor to v2.2 and current v2.3. Archived when v2.2 introduced the docs-only smoke exception and the no-halt-between-phases clarification.

---

## How files relate to each other

The high-level flow when a project uses Symposium OS:

1. **Adopt**: copy `template/` into the project as `.symposium/`. The project inherits the protocol, skills, templates, and ADR placeholder.

2. **Tailor**: run `init/INIT_PROMPT.md` against a directing AI. Fill in section 0.1 of `AUTONOMY_LAYER.md`, populate `CONTEXT.md`, complete `adr/0001-adopted-symposium-os.md`. Verify with `init/POST_INIT_CHECKLIST.md`.

3. **Plan**: write a spec in chat. Run `META_PROMPT.md` + `skills/planning/generate-directive` to compile the spec into a directive. Optionally audit with `skills/planning/directive-audit-revise`. Route the directive's capability tier with `skills/planning/model-routing`.

4. **Execute**: fire the directive at the assigned agent. The agent obeys `AUTONOMY_LAYER.md` unconditionally. Working files (`AUTONOMOUS_RUN_LOG.md`, `BLOCKERS_FOR_OPERATOR.md`, `docs/run-notes/`, `docs/deferred-issues.md`) accumulate the audit trail.

5. **Diagnose**: at decision points within the directive, the agent (or operator) invokes diagnostic skills like `api-surface-diagnostic`, `feed-diagnostic`, or executes the spec-reality reconciliation pattern from `AUTONOMY_LAYER.md` section 1.13.

6. **Execute writes**: deploys and MCP writes are gated by `deployment-preflight` and `mcp-write-safety` skills. Production safety boundaries (section 1.11) are unconditional.

7. **Review**: PRs and artifacts are gated by `council-review` (safety-adjacent), `public-surface-qa` (public surfaces), or simple operator review.

8. **Triage**: user testing or production bugs flow through `production-bug-triage`, which produces follow-up fix directives.

9. **Ship**: PRs merge. `build-report-ledger` produces the receipt.

10. **Learn**: `post-run-mortem` captures operational lessons. Section 2.3 of `AUTONOMY_LAYER.md` accumulates project-specific repair entries. The project's own `skills/` directory grows.

11. **Hand off**: at end of session, `session-handoff` carries state forward. Across runtimes, `cross-platform-handoff-template.md` carries state across agent platforms.

12. **Promote**: after a pattern recurs across three projects (rule of three per `docs/PROMOTING_PROJECT_LEARNINGS.md`), promote to canonical. New canonical version ships per `docs/VERSIONING.md`. `CHANGELOG.md` documents the change.

---

## Maintenance and contribution

### Adding a new canonical skill
1. Confirm rule of three: pattern has worked across three or more projects
2. Generalize: strip stack and project specifics
3. Author `template/skills/[category]/[name]/SKILL.md` per `docs/HOW_TO_AUTHOR_A_SKILL.md`
4. Update this `OVERVIEW.md`
5. Update `CHANGELOG.md` for the next minor canonical version
6. Bump canonical version per `docs/VERSIONING.md`

### Adding a new template
1. Author the skeleton in `template/templates/`
2. Update the skill that produces instances of it (if applicable)
3. Update this `OVERVIEW.md`
4. Update `CHANGELOG.md`

### Adding a new meta-ADR
1. Author per `docs/HOW_TO_WRITE_AN_ADR.md`
2. Use the next sequential number
3. Cross-reference any related canonical artifacts that motivated or were motivated by the decision
4. Update this `OVERVIEW.md`

### Demoting or superseding a canonical artifact
See `docs/PROMOTING_PROJECT_LEARNINGS.md` section on demoting from canonical. Demote with a meta-ADR explaining what went wrong, deprecate in one release, remove in the next minor release.

---

End of `OVERVIEW.md`.
