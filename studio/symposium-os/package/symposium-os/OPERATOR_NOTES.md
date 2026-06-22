# OPERATOR_NOTES.md

**Internal status: v0.3 / internal canonical draft.** Not for client distribution. Not for public release. Read this before sharing the repo outside the operating organization.

This file captures decisions, caveats, and unsettled questions that should not be in the public-facing canonical files but matter for how the operator uses this OS internally.

---

## Status

**Internal canonical v0.3 — canonical version v2.3.** The OS itself is a first-party operating asset. The protocol, skills, templates, and meta-ADRs are real and used in production work. The repo as a whole is not yet a finished, distributable, public artifact.

What's stable enough for internal use:
- `template/AUTONOMY_LAYER.md` (v2.3)
- `template/META_PROMPT.md` (v2.3)
- `template/skills/` — all 14 skills
- `template/templates/` — all six scaffolds
- `meta-adr/0001`, `0002`, `0003`, `0004`
- `init/INIT_PROMPT.md` (v1.0)
- `init/POST_INIT_CHECKLIST.md`
- `OVERVIEW.md` — complete file map at OS root
- `docs/HOW_TO_AUTHOR_A_SKILL.md`, `HOW_TO_WRITE_AN_ADR.md`, `VERSIONING.md`, `PARALLEL_AGENTS.md`, `PROMOTING_PROJECT_LEARNINGS.md`

What's roadmap or pending:
- `init/stack-presets/*.yml` — stubs. Functional after operator authors full content per preset.
- `case-studies/kairos-bootstrap/` and `case-studies/kairos-rescue/` — slots. Replace stubs with real artifacts when projects ship and the operator approves publishing.
- License decision (see below).
- Public/private status decision (see below).

---

## Decisions required before public release

### License

The repo's `README.md` shows License as `[TBD]`. This is intentional. Do not default to MIT or Apache-2.0 without considering whether Symposium OS should be open-source at all. Options:

1. **Proprietary, internal use only.** No external distribution. Treated as first-party IP supporting the operating organization's positioning.
2. **Source-available with restrictions.** Public read but no redistribution or commercial use without a license. Examples: Business Source License, Polyform Strict.
3. **Permissive open source.** MIT or Apache-2.0. Maximizes adoption but gives away the IP.
4. **Hybrid.** Core protocol (`AUTONOMY_LAYER.md`, `META_PROMPT.md`) open-source under a permissive license; skills, case studies, and meta-ADRs proprietary or source-available.

The operator's positioning leans toward option 1 or 2 in the near term. Revisit when the OS has been used across enough projects to make the proprietary value clear.

### Public/private status

Currently the repo is treated as internal. Before flipping to public:

- Audit every file for accidental personal references, operator-specific names, project-specific names that aren't intended to be public (see `archive/` warning below).
- Decide what to do with `archive/`. Options: keep private even when the rest of the repo is public (use a separate private archive repo), redact the historical files, or accept that v1.3 contains operator-specific language that predates generalization.
- Decide what to do with `case-studies/`. Real case studies expose operator workflow, commercial context, and project specifics. The operator decides per case study whether the artifacts are publishable.
- Add a `CONTRIBUTING.md` if accepting external contributions.
- Add a `CODE_OF_CONDUCT.md` if hosting a public community.
- Add a `SECURITY.md` for vulnerability reporting.

---

## Things that should NOT be promoted to canonical

These are operator-specific patterns or preferences that work for the operating organization but should not become canonical Symposium OS:

- Specific stack preferences (Next.js + Vercel + Neon, etc.) — these belong in `init/stack-presets/`, not in the canonical protocol.
- Specific agent runtime preferences (Claude vs Codex vs Gemini per task type) — these belong in operator-side runbooks, not in canonical docs.
- Specific deploy commands or hosting platforms — these belong in `AUTONOMY_LAYER.md` section 0.1 per project, not in the canonical protocol.
- Specific copy banks or prompt fragments from any project — these are project-specific by definition.

---

## Things the operator should keep in mind while using the OS

- The protocol is the contract. Edits to `template/AUTONOMY_LAYER.md` outside sections 0.1 and 2.3 should be treated as a canonical version bump, not a casual edit.
- Skill bloat is real. Use the rule of three before adding a new canonical skill.
- ADRs are immutable. Future-self will want this discipline.
- The init prompt is operator-owned. Revise freely.
- Case studies need explicit publishing approval. Default to not sharing.

---

## Open questions

These are unresolved as of v0.2 / canonical v2.2:

1. How should project-specific skill variants discover and import from canonical skills? Right now the assumption is that operators copy and modify; could there be a "skill extends" pattern instead?
2. When multiple agents on a stacked chain produce semantically-conflicting changes that the protocol can't mechanically resolve, the operator adjudicates. Should there be a structured "adjudication skill" to make this less ad-hoc?
3. The Council of Models pattern assumes the operator can run prompts across multiple models cheaply. Token-cost reality may force this to be more selective. When is single-model review acceptable as a fallback?
4. Cross-project pattern detection: how does the operator notice when the same pattern has hit three projects (the promotion threshold) without manually tracking it?

These get answered as the OS matures across more projects.

---

## Revision history of this file

- **v0.3 (2026-05-19)** — canonical v2.3. Added four canonical skills (production-bug-triage, directive-audit-revise, model-routing, post-run-mortem), two templates (cross-platform-handoff, qa-tester-onboarding), meta-ADR 0004 (stabilization before optimization), Non-Goals section in directive template, OVERVIEW.md at OS root.
- **v0.2 (2026-05-18)** — canonical v2.2. Added INIT_PROMPT.md v1.0, docs-only smoke exception, no-halt-between-phases clarification, archive marker, stack-preset ROADMAP banner.
- **v0.1 (2026-05-18)** — canonical v2.1. Initial structure with all template, skills, docs, meta-ADRs, case-study slots. License and status decisions deferred.
