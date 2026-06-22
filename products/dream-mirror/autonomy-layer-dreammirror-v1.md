---
title: "AUTONOMY LAYER DreamMirror v1"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Dream Mirror /Dream Mirror OS/AUTONOMY_LAYER_DreamMirror_v1.md"
status: active
privacy: working
tags:
  - product
---

# AUTONOMY LAYER DreamMirror v1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# AUTONOMY_LAYER.md — DreamMirror Edition v1.0

**Project:** DreamMirror  
**Protocol version:** 1.0 (inherits Anchor AUTONOMY_LAYER v1.2 safety rules)  
**Maintained by:** Marcus Vale / Eagle Rocket LLC  
**Last updated:** May 2026

---

## Purpose

This document is the standing behavioral protocol for all autonomous agents working on DreamMirror. It is not a one-time instruction. It governs every session. Agents must read this document before beginning any work on DreamMirror.

It complements the directive (the task-specific instruction). When the directive and this document conflict, this document wins — unless the directive explicitly overrides a named rule with a named justification.

---

## §1. Core Operating Rules

### §1.1 — Read before you build
Before writing a single line of code, read:
1. This document (AUTONOMY_LAYER)
2. The META_PROMPT for the current session
3. The directive

Do not start building based on the directive alone.

### §1.2 — The stack is locked
The stack is defined in the ADR. Do not propose, scaffold, or suggest alternatives. If you encounter a legitimate technical reason to deviate, flag it in a `// DIRECTOR:` comment and implement the locked choice anyway. Let Marcus decide on the exception.

### §1.3 — RLS is non-negotiable
Every Supabase table that stores user data must have Row-Level Security enabled. This is not a post-launch task. Do not create user-facing features on tables without RLS. If you are creating a new table, enable RLS before the feature that uses it.

### §1.4 — No auto-merge for sensitive changes
Open a PR for every meaningful unit of work. Do not auto-merge any PR that touches:
- Prompt content or system instructions
- UI copy visible to users
- Safety logic or the Safety Agent
- RLS policies or Supabase Auth configuration
- Schema migrations
- Environment variables in production

These PRs require manual review by Marcus before merge.

### §1.5 — All AI calls are server-side
No AI model calls from the browser. No API keys in the client. All model calls go through the Express backend. If you find client-side AI logic in existing code, flag it in the PR description.

### §1.6 — Store everything the moat needs
Every analysis run must store: `model_version`, `prompt_version`, `summary`, `output_json`, `safety_flags`, and `token_cost_by_stage`. This is required from the first deploy. Do not defer it.

### §1.7 — Token cost logging is required
Every AI pipeline run must log token count per stage. Use a consistent structure: `{ stage: string, model: string, input_tokens: number, output_tokens: number }`. Store this in the Analysis record. Do not estimate or skip this at V0.

### §1.8 — Cache analysis results
Do not rerun an analysis on the same dream unless the user explicitly requests a refresh. Store the analysis output and serve from cache on re-open. This controls cost at beta scale.

### §1.9 — Safety Agent runs on every analysis
The Safety Agent is the final step before any analysis output reaches the user. It is not optional, not skippable, not bypassable for speed. See the Prompt Library for Safety Agent instructions including the positive-instruction crisis path.

### §1.10 — Preserve the raw dream
The user's raw dream text must be stored separately and immutably from any cleaned or reconstructed narrative. The user must always be able to see and export their own words. Do not overwrite raw text with the cleaned version.

### §1.11 — Smoke test before opening a PR
Do not open a PR that breaks the build. Run the available tests (or at minimum a manual smoke test of the affected flow) before opening. Note what was tested in the PR description.

### §1.12 — MCP write safety preflight (required before any production write)
Before any tool call that writes to production infrastructure — Supabase production, Fly.io production, Vercel production environment variables, DNS records, or any external service — stop and confirm:

1. Is this the production environment or a preview/staging environment?
2. Is this write reversible without data loss?
3. Has Marcus explicitly authorized this specific write in the current session?

If any answer is unclear or no, do not proceed. Open a PR or leave a `// DIRECTOR: needs manual authorization` comment for Marcus to act on.

This rule exists because production writes to a database holding real user dream content cannot be undone carelessly. The sensitivity of the data makes this more critical, not less.

### §1.13 — Spec-reality reconciliation (required before starting any directive)
Before starting work on a directive, scan the existing codebase for any prior implementation of the feature being specified. If prior implementation conflicts with the directive:

1. Document the conflict with a `// DIRECTOR: conflict with existing implementation —` comment.
2. Implement the directive as specified.
3. Flag the conflict explicitly in the PR description.

Do not silently override existing code. Do not assume the directive already accounts for what exists.

---

## §2. Decision-Making Rules

### §2.1 — Conservative by default
When the directive is ambiguous, implement the conservative interpretation. More features and more complexity can be added; bad schema decisions and missing safety logic are hard to undo.

### §2.2 — Product decisions belong to Marcus
Implementation decisions (how to structure a function, which library to use, how to handle an edge case in logic) are yours to make. Product decisions (what the output says, what a feature does, what the UX flow is) belong to Marcus. When you are not sure which category a decision falls into, flag it and implement the conservative version.

### §2.3 — Do not invent scope
Do not implement features that are not in the current directive, even if they seem obviously useful. Leave a `// DIRECTOR: [feature idea]` comment and move on.

### §2.4 — One PR per coherent unit
Do not batch unrelated changes into a single PR. If implementing a directive naturally produces two separate units of work, open two PRs.

---

## §3. Dream Content Handling Rules

### §3.1 — Treat dream content as sensitive personal data
Dream entries, emotional check-in responses, and user notes about waking-life context are sensitive personal data. They may contain references to relationships, trauma, grief, health, sexuality, family, and crisis states. Handle with the same care you would give medical records.

### §3.2 — User controls over their own data from day one
Export and delete must be functional before any real user touches the product. Do not launch a beta without these controls implemented and tested.

### §3.3 — No dream content in error logs
Do not log raw dream text, emotional check-in responses, or user notes in server logs or error reporting tools. Log dream IDs and status codes only.

### §3.4 — Crisis content requires the positive-instruction path
If the Safety Agent detects crisis-adjacent content (suicidal ideation, self-harm language, acute relational danger, severe distress), the response must not merely strip the flagged content. It must include the positive-instruction path defined in the Prompt Library. Silenced output is not sufficient.

---

## §4. What Is Out of Scope for All Agent Sessions

No agent, in any session, should implement or scaffold:

- Native mobile app code (iOS / Android / React Native)
- Social features or shared dream feeds
- GraphQL API
- Stripe in-app payment processing
- Therapist marketplace or practitioner management
- Multilingual localization
- Client-side AI model calls
- Any feature not in the current directive

If a dependency or library being installed implies one of the above, flag it and do not proceed.

---

## §5. Protocol Update Log

| Version | Change |
|---|---|
| 1.0 | Initial DreamMirror edition. Inherits §1.12 (MCP write safety preflight) and §1.13 (spec-reality reconciliation) from Anchor AUTONOMY_LAYER v1.2. Adds §3 Dream Content Handling Rules specific to DreamMirror. |
