---
title: "# V5.3 Council Revisions — Approved Bank Reword + Adds, Forbidden List Expansion, Start Over Nuance"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/# V5.3 Council Revisions — Approved Bank Reword + Adds, Forbidden List Expansion, Start-Over Nuance.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# # V5.3 Council Revisions — Approved Bank Reword + Adds, Forbidden List Expansion, Start Over Nuance

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# V5.3 Council Revisions — Approved Bank Reword + Adds, Forbidden List Expansion, Start-Over Nuance

STATUS: READY TO FIRE. No execution gate. V5.3 is merged to main.

## Header block

Surfaces: Relapse Response prompt context (api-server) — approved copy bank, forbidden copy list, start-over nuance rule

Production impact: Code-only. No schema. No new tables. No new event_log types. Changes are to prompt-injected copy constants only. Affects AI behavior on /relapse-response surface.

Council of Models: This directive APPLIES Council edits that have already been approved. No second Council pass required before merge.

Auto-merge: No. Safety-adjacent prompt copy revision. Marcus reviews diff before merge.

Credentials: None. CC Cloud or Codex, code-only.

Agent: CC Cloud (Sonnet sufficient — pure text edit work) OR Codex. Single agent.

## Role statement

You are applying approved Council of Models edits to the V5.3 Relapse Response approved copy bank and forbidden copy list, and adding a new "Start-over nuance" rule. V5.3 is already merged to main (PR #55). This directive produces a small, atomic follow-up PR with copy revisions only. No code logic changes. No schema. No new files outside test updates. Find the exact files in the merged V5.3 code via spec-reality reconciliation before editing.

## Apply AUTONOMY_LAYER.md before executing

Apply AUTONOMY_LAYER.md (Anchor edition v1.2, repo root) before executing this directive. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1.

## Deployment posture

Per AUTONOMY_LAYER section 1.8:

- Agent does NOT merge manually. Open PR and stop.

- Agent does NOT deploy. CD handles main pushes after Marcus merges.

- No production schema changes. No flyctl secret changes. No Vercel env changes.

- State in PR body: "No Neon migration required."

## Working files protocol

Per AUTONOMY_LAYER section 0.4. Append per-session run note: docs/run-notes/session-YYYY-MM-DD-v53-council-revisions.md.

## Design data

### Spec-reality reconciliation (run before any edit)

Per AUTONOMY_LAYER section 1.13. V5.3 (PR #55, branch feat/v53-relapse-response, HEAD 3fc0d4c) introduced the approved copy bank and forbidden copy list as prompt-injection constants. Exact file paths are not specified in this directive. Locate them via:

1. Grep for any line from the V5.3 approved bank, e.g.: "Thank you for being honest."

2. Grep for any line from the V5.3 forbidden list, e.g.: "You failed." or "You ruined your progress."

3. Identify the module(s) that export these constants and the module that injects them into assembleSystemPrompt as relapseContext.

4. Identify all test files that reference these constants (presence asserts, byte-equality asserts).

Log the discovered file paths and current line counts to AUTONOMOUS_RUN_LOG.md before making any edit. If the constants are split across multiple files, log each.

### Approved copy bank — REWORD

Locate the existing line:

"Let's get you through the next window cleanly."

Replace with:

"Let's get you through the next window safely and honestly."

### Approved copy bank — ADD (two new lines, at end of bank)

"If you are still in danger or still close to using, we start with support first."

"We can deal with the tracker honestly without treating the reset as a punishment."

### Forbidden copy list — KEEP ALL existing lines

Do not remove any line from the existing V5.3 forbidden list. All 19 lines stay.

### Forbidden copy list — ADD (12 new lines, at end of list)

Shame and fatalism additions (add in this order):

"You blew it."

"You're back to day zero."

"All that time is gone."

"You have to earn back your progress."

"You should be ashamed."

"You knew better."

"I warned you."

"This is what happens when you don't stay connected."

"You clearly weren't serious."

False-hope and pressure additions (add in this order, after shame/fatalism):

"This will never happen again."

"This has to be your last relapse."

"Promise me this is the last time."

### Start-over nuance rule — ADD new labeled section

Add a new section immediately after the forbidden copy list in the same module. Use a clearly labeled heading "Start-over nuance" so it is parseable as a rule, not a bank entry. Verbatim text:

"Start-over nuance: Do not impose 'starting over,' 'back to zero,' or 'square one' language on the user. If the user's recovery program uses reset language, day-count resets, or Day 1 chips, validate the accountability without implying that prior work was erased. A tracker reset may be honest; it is not a punishment or proof that progress is gone."

How this is injected into relapseContext: include the start-over nuance as a clearly labeled rule block in the prompt template, separate from the approved bank and forbidden list. The AI must treat it as a behavioral rule, not as a quote to repeat to the user.

## Phase plan

Each phase follows AUTONOMY_LAYER section 3: pre-flight, smoke first, implementation, health check, commit.

Phase A is the first data-consuming phase and MUST execute spec-reality reconciliation per AUTONOMY_LAYER section 1.13 as its first implementation step.

### Phase A — Approved copy bank revisions

- Pre-flight: git status clean on feat/v53-council-revisions cut from main, credentials preflight per section 0.5 (none required), baseline api-server test counts recorded, ANCHOR-1 build order (lib/db, lib/api-zod first)

- SPEC-REALITY RECONCILIATION FIRST per section 1.13: locate approved copy bank file(s), forbidden list file(s), and any test files asserting on either. Log to AUTONOMOUS_RUN_LOG.md.

- Smoke first: unit test asserting the reworded line is present byte-for-byte, the two new approved lines are present byte-for-byte, the old "cleanly" line is absent. Run red.

- Implementation: apply reword and two adds

- Health check: full api-server tests green; any pre-existing test asserting the old "cleanly" line is updated as part of this commit

- Commit: "fix(v5.3): approved copy bank Council revisions"

### Phase B — Forbidden list expansion + Start-over nuance rule

- Pre-flight: prior commit exists

- Smoke first: unit test asserting all 12 new forbidden lines present byte-for-byte; unit test asserting all 19 existing forbidden lines retained; unit test asserting start-over nuance rule present as a labeled section. Run red.

- Implementation: append 9 shame/fatalism lines, append 3 false-hope/pressure lines (in the spec order), add start-over nuance labeled section after forbidden list, verify prompt injection includes the nuance rule

- Health check: full api-server tests green

- Commit: "fix(v5.3): forbidden list expansion and start-over nuance rule"

### Phase C — BUILD_REPORT and PR

- Pre-flight: prior commits exist

- Write docs/run-notes/session-YYYY-MM-DD-v53-council-revisions-build-report.md per AUTONOMY_LAYER section 5

- Include: file paths discovered during spec-reality reconciliation, exact diff per file, all changed files, test counts, MANUAL_PLAYTEST_REQUIRED items (none expected), confirmation no Neon migration required, confirmation no second Council pass needed (this PR applies pre-approved Council edits)

- Open PR to main: title "fix: V5.3 Council revisions — approved bank + forbidden list + start-over nuance"

- PR body includes: Council source reference, phase summary, changed files, test counts, "No Neon migration required" statement

- Auto-merge: NO. Stop after PR open.

## Forbidden side quests

- Do NOT remove any existing line from the V5.3 forbidden list

- Do NOT change any existing line from the V5.3 approved bank besides the single "cleanly" reword

- Do NOT alter relapseContext injection logic

- Do NOT alter /relapse-response route, six-step flow, or tracker reset logic

- Do NOT alter event_log entries or types

- Do NOT modify any other prompt fragment, surface variant, or copy bank

- Do NOT bundle unrelated cleanup with these commits per section 1.9

## Self-repair playbook

Apply AUTONOMY_LAYER section 2 (ANCHOR-1 through ANCHOR-16). No new entries from this directive.

## Deferred-issues format

Per AUTONOMY_LAYER section 4.

## BUILD_REPORT format

Per AUTONOMY_LAYER section 5.

## Hard stops

Per AUTONOMY_LAYER section 6.

## GO

Begin Phase A pre-flight per AUTONOMY_LAYER section 3. Credentials preflight scope: none (code-only). Cut branch from main: feat/v53-council-revisions. Create or append ISSUE_EXECUTION_PLAN.md and AUTONOMOUS_RUN_LOG.md at repo root.
