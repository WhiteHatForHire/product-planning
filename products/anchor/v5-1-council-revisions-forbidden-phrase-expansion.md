---
title: "V5.1 council revisions forbidden phrase expansion"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/V5.1 council revisions forbidden phrase expansion.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# V5.1 council revisions forbidden phrase expansion

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
V5.1 Council Revisions — Forbidden Phrase Expansion, Drift Reword, Disclosure Reword

Status: FIRE AFTER PR #59 IS MERGED TO MAIN

Header block

Field

Value

Surfaces

assembleSystemPrompt.ts (api-server), WhyAmISeeingThis.tsx (recovery-checkin)

Production impact

Prompt change only. No schema. No new tables. No new event_log types. No route/UI logic changes.

Council of Models

This directive APPLIES Council edits already approved across 4 models. No second Council pass required.

Auto-merge

No. Safety-adjacent prompt copy revision. Marcus reviews diff before merge.

Credentials

None. CC Cloud or Codex, code-only.

Agent

CC Cloud (Sonnet sufficient — targeted text edits to two files) OR Codex.

Role statement

You are applying approved Council of Models edits to the V5.1 Pattern Insight forbidden phrase banks, voice block structure constraints, drift framing line, and "Why am I seeing this?" disclosure template. PR #59 is already merged to main. This directive produces a small, atomic follow-up PR with copy revisions only. No code logic changes. No schema. No new files outside test updates. Locate the exact constants in the merged V5.1 code via spec-reality reconciliation before editing.

Apply AUTONOMY_LAYER.md before executing

Apply AUTONOMY_LAYER.md (v1.3, repo root) before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1.

Deployment posture

Per section 1.8:

Agent does NOT merge. Open PR and stop.

Agent does NOT deploy. CD handles main pushes after Marcus merges.

No schema changes. No flyctl secret changes. No Vercel env changes.

State in PR body: "No Neon migration required."

Working files protocol

Per section 0.4. Create:

docs/run-notes/session-YYYY-MM-DD-v51-council-revisions-plan.md

AUTONOMOUS_RUN_LOG.md (append)

BLOCKERS_FOR_MARCUS.md (if needed)

Design data

Spec-reality reconciliation (run before any edit)

Per AUTONOMY_LAYER section 1.13. Locate:

patternInsightUniversalForbiddenPhrases array in artifacts/api-server/src/lib/prompts/assembleSystemPrompt.ts

patternInsightPerSignalForbidden object (or equivalent per-signal arrays) in the same file

buildPatternInsightContext function (voice block + structure rules) in the same file

driftFramingLine export in the same file

The disclosure template string in artifacts/recovery-checkin/src/components/WhyAmISeeingThis.tsx

All test files asserting on any of the above

Log discovered file paths and current array lengths to AUTONOMOUS_RUN_LOG.md before editing. If constants are structured differently than expected, log a SPEC_REALITY_DELTA and adopt repo reality.

Change 1 — Universal forbidden phrases (EXPAND)

Locate patternInsightUniversalForbiddenPhrases. Keep all existing entries. Append these in order:

"This is a warning sign."

"This is concerning."

"You are at risk."

"Warning:"

"Urgent:"

"Anchor is worried about"

"The system detected"

"The model detected"

"The algorithm detected"

"Your behavior shows"

"You need to"

"You must"

"You are backsliding."

"You are regressing."

"You are off track."

"You are slipping."

"Your data proves"

"This means you are unsafe."

"If you don't"

"you may relapse"

Do NOT remove any existing entry. Append only.

Change 2 — Per-signal forbidden phrases (EXPAND)

Locate the per-signal forbidden phrase structure. Keep all existing entries per signal. Append the following per signal:

missed_checkin_drift — append:

"You vanished."

"You ghosted."

"You checked out."

"You stopped showing up."

"You are neglecting your recovery."

"You lost your rhythm."

"You are disconnected from recovery."

"You've been pulling away."

rising_craving — append:

"Your cravings are escalating."

"Cravings are getting worse."

"This craving could get stronger."

"You are in a risky state."

"You need to act now."

"You may relapse if this continues."

"It's only a matter of time."

low_sleep_high_craving — append:

"Poor sleep is fueling this."

"Your body is working against you."

"This is a biological warning sign."

"Your nervous system is dysregulated."

"You are vulnerable because you slept badly."

"Sleep is the problem."

"Your body is failing you."

repeated_incomplete_commitments — append:

"You failed again."

"You did not follow through again."

"You are not keeping your word."

"You need accountability."

"You need to try harder."

"You lack consistency."

"You are not serious."

"You're struggling to stick with things."

time_of_day_risk — append:

"This is your relapse window."

"This is when you fall apart."

"This time of day is dangerous for you."

"Be careful tonight."

"You should avoid tonight."

"Your pattern says tonight is risky."

"This time of day is tough for you."

approaching_milestone — append:

"Stay strong."

"Don't blow it."

"You made it this far."

"You're so close."

"This is the hardest part."

"Milestones are dangerous."

"Now is not the time to slip."

"The stakes are high."

"Don't let this milestone slip."

Change 3 — Voice block structure constraints (ADD to buildPatternInsightContext)

Locate the structure rules inside buildPatternInsightContext. The existing rules constrain output length and format. Add these constraints after the existing rules:

Use correlation language only, not causation language. Say "lined up with" not "caused by."

Suggested next steps must be optional and non-urgent. Do not frame the next step as required.

Do not use "need," "must," "should," "risk," "danger," "warning," "detected," "regression," or "relapse" in card body copy unless the signal itself is explicitly about a user-reported relapse event.

Do not compare the user to an ideal recovery pattern.

Do not imply the user has failed, declined, deteriorated, or become unsafe.

The grounded implication must describe a current feeling or state, not a future outcome.

Change 4 — Drift framing line (REWORD)

Locate driftFramingLine export. Replace current value verbatim with:

Time-aware: Recent check-in or commitment rhythm differs from the user's usual Anchor pattern. Respond with a grounded, low-pressure tone. Do not imply failure, danger, relapse risk, or prediction. Offer one small, optional way to reconnect with the work.

Change 5 — "Why am I seeing this?" disclosure template (REWORD)

Locate the disclosure template string in WhyAmISeeingThis.tsx. Make two targeted rewrites:

Rewrite 1: Replace any instance of "Anchor noticed" with "This card surfaced because"

Rewrite 2: Replace "It is not a prediction." with:

This is a simple pattern notice, not a prediction, diagnosis, relapse warning, or judgment.

If both phrases appear as a combined template, the full updated template should read:

This card surfaced because [computed fact in plain English] during [date range]. This is a simple pattern notice, not a prediction, diagnosis, relapse warning, or judgment. It is based only on [data source], not your chat messages.

Phase plan

Each phase follows AUTONOMY_LAYER section 3: pre-flight, smoke first, implementation, health check, commit.

Phase A is the first data-consuming phase and MUST execute spec-reality reconciliation per section 1.13.

Phase A — Universal and per-signal forbidden phrase expansion

Pre-flight: git status clean on feat/v51-council-revisions cut from main, credentials preflight per section 0.5 (none required), baseline api-server test counts recorded, ANCHOR-1 build order

SPEC-REALITY RECONCILIATION FIRST per section 1.13: locate all five targets listed above. Log paths and current lengths to AUTONOMOUS_RUN_LOG.md.

Smoke first: unit tests asserting all new universal forbidden phrases present byte-for-byte; unit tests asserting all new per-signal forbidden phrases present byte-for-byte; unit tests asserting all existing phrases retained. Run red.

Implementation: append new universal phrases, append new per-signal phrases. No removals.

Health check: full api-server tests green

Commit: fix(v5.1): expand universal and per-signal forbidden phrase banks

Phase B — Voice block structure constraints + drift framing reword

Pre-flight: prior commit exists

Smoke first: unit test asserting all six new structure constraint strings present in buildPatternInsightContext; unit test asserting driftFramingLine equals the new verbatim string exactly. Run red.

Implementation: add structure constraints to voice block, reword driftFramingLine

Health check: full api-server tests green

Commit: fix(v5.1): voice block structure constraints and drift framing reword

Phase C — Disclosure template reword

Pre-flight: prior commit exists

Smoke first: unit or snapshot test asserting "Anchor noticed" is absent from WhyAmISeeingThis.tsx; asserting "This card surfaced because" is present; asserting updated prediction disclaimer string is present. Run red.

Implementation: apply both disclosure rewrites

Health check: recovery-checkin build green, typecheck clean

Commit: fix(v5.1): disclosure template reword — remove surveillance phrasing

Phase D — BUILD_REPORT and PR

Pre-flight: prior commits exist

Write docs/run-notes/session-YYYY-MM-DD-v51-council-revisions-build-report.md per AUTONOMY_LAYER section 5

Include: file paths from spec-reality reconciliation, phrase counts before/after per array, test counts, confirmation no Neon migration required, confirmation no second Council pass needed

Open PR to main: title fix: V5.1 Council revisions — forbidden phrase expansion + drift reword + disclosure

PR body: Council source reference (4-model convergence), phase summary, changed files, test counts, "No Neon migration required"

Auto-merge: NO. Stop after PR open.

Forbidden side quests

Do NOT remove any existing forbidden phrase from any list

Do NOT alter the pattern insight engine signal logic

Do NOT alter the ranking, severity, or action mapping

Do NOT alter the Home card UI components beyond the disclosure template

Do NOT alter event_log entries or types

Do NOT modify any other prompt fragment, surface variant, or copy bank

Do NOT bundle unrelated cleanup per section 1.9

Self-repair playbook

Apply AUTONOMY_LAYER section 2. No new entries from this directive.

Deferred-issues format

Per AUTONOMY_LAYER section 4.

BUILD_REPORT format

Per AUTONOMY_LAYER section 5.

Hard stops

Per AUTONOMY_LAYER section 6.

GO

Begin Phase A pre-flight per AUTONOMY_LAYER section 3. Credentials preflight scope: none (code-only). Cut branch from main: feat/v51-council-revisions. Create docs/run-notes/session-YYYY-MM-DD-v51-council-revisions-plan.md and AUTONOMOUS_RUN_LOG.md at repo root.
