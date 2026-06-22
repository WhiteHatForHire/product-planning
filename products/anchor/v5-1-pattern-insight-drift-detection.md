---
title: "# V5.1 Pattern Insight + Drift Detection"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/# V5.1 Pattern Insight + Drift Detection.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# # V5.1 Pattern Insight + Drift Detection

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# V5.1 Pattern Insight + Drift Detection

## Header block

Surfaces: Pattern Insight Engine (api-server lib), assembleSystemPrompt surface variant, recovery-checkin Home card UI, event_log additions

Production impact: Code-only. No new tables. No production schema migration required. event_log gains three new type strings (additive, no migration).

Council of Models: REQUIRED before merge. Eight signal copy banks plus universal forbidden phrases plus drift framing line plus "Why am I seeing this?" template.

Auto-merge: No. Pattern Insight surface introduces a new AI-touching surface variant and a copy bank. Safety-adjacent.

Credentials: None for CC Cloud. CC Local optional for post-merge production smoke against sobrietyanchor.com (HUMAN_REVIEW).

Agent: CC Cloud Opus, high effort. One directive, one branch, one PR. Codex may assist UI in Phase E if scope pressure requires.

## Role statement

You are implementing V5.1 Pattern Insight Engine plus Drift Detection on Anchor. The engine computes ranked behavioral signals deterministically from existing check-in, commitment, event_log, and tracker data. It surfaces at most one primary insight card on Home, or nothing. The card body is phrased by the AI through a new pattern_insight surface variant of assembleSystemPrompt that inherits program and experience-level fragments. Drift Detection sets V4's drift_signal flag when missed_checkin_drift fires, which injects a verbatim framing line into the Time-Aware Framing section of all V4 surfaces. The engine uses no ML, no AI for signal computation, no raw note parsing, no chat-content parsing, and writes no system inference into stable_profile.

## Apply AUTONOMY_LAYER.md before executing

Apply AUTONOMY_LAYER.md (Anchor edition v1.2, repo root) before executing this directive. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1.

## Execution gate (hard stop)

Do not begin Phase A until all of the following are true:

1. feat/v41-practice-mode is merged to main

2. V4.1 has passed Council review

3. Production main is stable, no open critical blockers

4. Marcus has explicitly authorized V5.1 execution

If any condition is not met: stop, log to BLOCKERS_FOR_MARCUS.md per AUTONOMY_LAYER section 0.4, do not proceed.

## Deployment posture

Per AUTONOMY_LAYER section 1.8:

- Agent does NOT merge manually. Auto-merge ineligible (see header). Open PR and stop.

- Agent does NOT deploy. CD handles main pushes after Marcus merges.

- No production schema changes in this directive. No flyctl secret changes. No Vercel env changes.

- event_log type additions require no migration. State in PR body: "No Neon migration required."

## Working files protocol

Per AUTONOMY_LAYER section 0.4, create and maintain throughout:

- ISSUE_EXECUTION_PLAN.md at repo root

- AUTONOMOUS_RUN_LOG.md at repo root

- BLOCKERS_FOR_MARCUS.md at repo root

Append per-session run note: docs/run-notes/session-YYYY-MM-DD-v51-pattern-insight.md

## Design data

### Schema deltas

No tables. No columns. event_log gains three new type string values:

- pattern_insight_generated — summary template: "Generated [signal_id] insight for [focus]."

- pattern_insight_dismissed — summary template: "Dismissed [signal_id] insight for [focus]."

- pattern_insight_action_clicked — summary template: "Clicked [action_id] action from [signal_id] insight."

Event summary must not include: severity score, raw values, notes content, chat content.

### File structure

New files:

- api-server/src/lib/patternInsight/index.ts — engine entry

- api-server/src/lib/patternInsight/signals.ts — all signal computations

- api-server/src/lib/patternInsight/ranking.ts — deterministic ranking

- api-server/src/lib/patternInsight/types.ts — PatternSignal type

- api-server/src/lib/patternInsight/__tests__/signals.test.ts — per-signal unit tests

- api-server/src/lib/patternInsight/__tests__/ranking.test.ts — ranking unit tests

- recovery-checkin/src/components/PatternInsightCard.tsx — Home card component

- recovery-checkin/src/components/WhyAmISeeingThis.tsx — affordance component

- recovery-checkin/tests/e2e/pattern-insight.spec.ts — Playwright specs

Modified files:

- api-server/src/lib/prompts/assembleSystemPrompt.ts — add pattern_insight surface variant, pattern_signal param

- api-server/src/lib/prompts/types.ts — extend BuildOptions surface union

- api-server/src/lib/events/types.ts (or equivalent event_log type module) — add three new type strings

- api-server/src/routes/home.ts (or equivalent Home data route) — invoke engine, return signal or null

- recovery-checkin/src/pages/Home.tsx — render PatternInsightCard when signal present

- recovery-checkin/src/api/home.ts (or equivalent) — type for pattern_signal field in Home response

### BuildOptions extension (verbatim)

type BuildOptions = {

surface: 'chat' | 'checkin_synthesis' | 'practice' | 'pattern_insight';

pattern_signal?: PatternSignal;

// existing fields unchanged

};

### Signal threshold rules

missed_checkin_drift:

- Lookback: 14 local calendar days

- Min data: 3+ completed check-ins in last 14 days

- Cadence: daily (do not add user-configured cadence in V5.1)

- Fire: 2 consecutive missed expected check-ins after baseline established

- Severity: 2 (1 day missed past threshold), 3 (2+ days missed past threshold)

- Action: check_in

rising_craving:

- Window: 7 days primary; expand to 14 days only when 7-day window has fewer than 3 craving values

- Min data: 3 numeric craving ratings

- Fire: latest 3-rating average is at least +2 above prior comparable average AND recent average is at least 5/10

- Average comparison only, no slope math

- Severity: Opus defines 1-5 scale, documents in BUILD_REPORT

- Action: chat (moderate); contact_someone (high craving and contacts present)

low_sleep_high_craving:

- Low sleep cutoff: 5 hours or fewer

- High craving cutoff: 6/10 or higher

- Window: 14 days

- Min data: 4 check-ins with both sleep and craving values present

- Fire: 2 or more days in window where both co-occur

- Hard constraint: never say sleep "caused" craving; only "lined up with"

- Severity: Opus defines

- Action: chat or tiny_commitment (Opus chooses deterministically, document in BUILD_REPORT)

repeated_incomplete_commitments:

- Window: 14 days

- Incomplete = past due and not completed, OR explicitly marked failed/not done

- Do not count: not-yet-due, manually deleted, days with no due commitments

- Fire: 2 or more incomplete in window

- Severity: Opus defines

- Action: smaller_commitment

time_of_day_risk:

- Min data: 60+ days of check-in data

- Bucket: day-of-week + 4-hour block

- Elevated craving: 6/10 or higher

- Fire: current bucket has 3+ historical elevated-craving instances AND bucket average is at least +2 above user's overall craving average

- Do not fire on thin user state or no clear historical recurrence

- Severity: Opus defines

- Action: contact_someone (contacts exist); check_in (no contacts)

approaching_milestone:

- Consumed from V4 recoveryProfile.getApproachingMilestone (5-day window)

- Surface ONLY when no drift, craving, sleep, commitment, or safety-adjacent signal is active

- Encouragement tier only, never outranks drift

- Severity: 1

- Action: check_in

### Scaffolded null signals

no_recent_contact:

- Scaffold the signal ID and type in the engine

- ALWAYS return null in V5.1

- Do NOT infer contact from notes, chat, or sponsor_message_opened proxy events

- Code comment verbatim: // V6 implementation pending contact-event tracking

anniversary_seasonal:

- Scaffold the signal ID and type in the engine

- ALWAYS return null in V5.1 unless Marcus explicitly re-enables

- Do not leave a stub that can throw or accidentally fire

- Code comment verbatim: // V5.4 deferred — enable only on Marcus's explicit authorization

### Ranking

Deterministic order:

1. Tier: drift (missed_checkin_drift, rising_craving, low_sleep_high_craving) > commitment (repeated_incomplete_commitments, time_of_day_risk) > encouragement (approaching_milestone). Safety tier reserved.

2. Numeric severity (internal only, not user-visible, not written to stable_profile, never called "risk")

3. Recency of underlying data window

4. Signal ID alphabetical order

Return one primary signal or null. Never return multiple.

### Drift Detection wiring

Drift fires when missed_checkin_drift fires.

When drift detected: set drift_signal = true in assembleSystemPrompt call.

Drift framing text (verbatim, appended to V4 Time-Aware Framing section when drift_signal=true):

"Time-aware: The user's recent Anchor rhythm has changed. Respond with a grounded, low-pressure tone. Do not imply failure or danger. Offer one small way back into contact with the work."

Drift clears on any of:

- Full check-in completed

- Relapse response completed

- Practice module completed

- Commitment completed

Chat alone does NOT clear drift.

Dismissal does NOT clear drift from prompt layer (suppresses card only).

Stale window: 72 hours. Daily background task clears stale drift signals that do not recompute true.

### pattern_insight surface variant rules

Inherits: User Context block, program fragment, experience_level fragment.

Excludes: milestone framing unless active signal is approaching_milestone.

Output constraints (enforce in prompt template):

- One paragraph

- 2 to 3 sentences

- No preamble

- No closing question

- Structure: observation + grounded implication + suggested next step

- Suggested action button text is separate from generated body and handled by UI

Voice constraints (enforce in prompt template):

- Cite computed signals only, never chat content, never raw notes

- Never use phrases: "the AI detected", "Anchor predicts", "risk score", "risk detected"

- Never write system-generated inference into stable_profile

### Universal forbidden Pattern Insight phrases (verbatim)

NEVER appear in any template, generated card, or "Why am I seeing this?" text:

- Relapse risk detected.

- You are about to relapse.

- You are spiraling.

- You are failing.

- You keep failing.

- You are isolating dangerously.

- Your data shows you are unsafe.

- Anchor predicts...

- The AI detected...

- You should be worried.

### Per-signal title style and forbidden phrases (verbatim)

missed_checkin_drift

Titles: "Two quiet check-in days" / "Your rhythm changed a little"

Forbidden: "You disappeared." / "You are avoiding recovery." / "You fell off." / "Relapse risk detected."

rising_craving

Titles: "Craving has been higher" / "A higher-craving stretch"

Forbidden: "You are about to relapse." / "This is dangerous." / "You are losing control." / "Craving spike detected."

low_sleep_high_craving

Titles: "Sleep and craving lined up" / "Low sleep, harder days"

Forbidden: "Your sleep caused your craving." / "You are biologically at risk." / "You need to fix your sleep." / "This pattern proves..."

repeated_incomplete_commitments

Titles: "The follow-through loop needs attention" / "Make the next promise smaller"

Forbidden: "You keep failing commitments." / "You cannot follow through." / "You broke your promises." / "You need more discipline."

time_of_day_risk

Titles: "This time has been harder before" / "A familiar harder window"

Forbidden: "You always struggle now." / "Tonight is risky." / "You are in danger tonight." / "This is your danger window."

approaching_milestone

Titles: "A milestone is close" / "Close to [N] days"

Forbidden: "Don't mess this up." / "You're almost there." / "Everything changes after this." / "This proves you're safe now."

anniversary_seasonal (scaffolded null; titles reserved for future activation)

Titles: "This week is worth keeping simple" / "A familiar hard stretch"

### "Why am I seeing this?" affordance template (verbatim)

"Anchor noticed [computed fact in plain English]. That is why this card is here. It is not a prediction. This is based only on [data source], not your chat messages."

Show fields: signal name in plain English, date range, computed values, threshold rationale, suggested action reason.

Never show: raw notes, chat content, severity score, risk wording, model language.

### Dismissal logic

Suppress same signal_type + focus + computed_window for 24 hours.

Use event_log pattern_insight_dismissed lookback to check 24h window before surfacing any insight.

Different signal type after dismissal: can surface same day.

Dismissal does not cool entire card for 24h.

No dismissal reason field in V5.1.

## Phase plan

Each phase follows AUTONOMY_LAYER section 3: pre-flight, smoke assertions written first, implementation, health check, commit.

Phase B is the first data-consuming phase and MUST execute spec-reality reconciliation per AUTONOMY_LAYER section 1.13 as its first implementation step: read actual interfaces for check_ins, commitments, event_log, stable_profile, recoveryProfile.ts before implementing signal logic. Log any SPEC_REALITY_DELTA findings to AUTONOMOUS_RUN_LOG.md. Adopt repo reality; the directive is a plan.

### Phase A — Types and BuildOptions extension

- Pre-flight: git status clean on feat/v51-pattern-insight, credentials preflight per section 0.5, baseline test counts recorded, ANCHOR-1 build order (lib/db, lib/api-zod first)

- Smoke first: unit test asserting BuildOptions surface union accepts 'pattern_insight', pattern_signal optional. Run red.

- Implementation: extend BuildOptions surface union, add pattern_signal optional, add PatternSignal type stub, add three event_log type strings, run typecheck

- Health check: full typecheck pass on api-server and recovery-checkin, all existing tests green

- Commit: "feat(v5.1): extend BuildOptions with pattern_insight surface and pattern_signal"

### Phase B — Pattern Insight Engine

- Pre-flight: prior commit exists, ANCHOR-1 build order

- SPEC-REALITY RECONCILIATION FIRST per section 1.13: read check_ins, commitments, event_log, stable_profile, recoveryProfile.ts actual interfaces before implementing. Log deltas to AUTONOMOUS_RUN_LOG.md.

- Smoke first: per-signal unit tests with synthetic fixtures asserting fire at threshold, no-fire below threshold, null on insufficient data. Both null-scaffolded signals always return null. Ranking returns deterministic order. Run red.

- Implementation: build engine to green

- Health check: full api-server tests green, both null signals reliably return null without throwing

- Commit: "feat(v5.1): pattern insight engine with deterministic ranking"

### Phase C — Drift Detection wiring

- Pre-flight: prior commit exists

- Smoke first: unit test asserting drift_signal=true when missed_checkin_drift fires, drift clears on qualifying actions only, chat alone does not clear. Run red.

- Implementation: wire engine output to drift_signal flag, implement clearing logic on qualifying event types, daily background task stub for 72h staleness

- Health check: full api-server tests green

- Commit: "feat(v5.1): drift detection wires to V4 drift_signal hook"

### Phase D — pattern_insight surface variant in assembleSystemPrompt

- Pre-flight: prior commit exists

- Smoke first: unit test asserting pattern_insight surface inherits program and experience_level fragments, excludes milestone framing unless signal is approaching_milestone, output constraints encoded, drift framing line appears verbatim when drift_signal=true. Run red.

- Implementation: add surface case to assembleSystemPrompt, encode voice constraints and forbidden phrase guards

- Health check: full api-server tests green, typecheck pass

- Commit: "feat(v5.1): pattern_insight surface variant in assembleSystemPrompt"

### Phase E — Home card UI

- Pre-flight: prior commit exists, recovery-checkin workspace builds

- Smoke first: Playwright spec asserting card renders for each active signal type, does not render when engine returns null, "Why am I seeing this?" expands. Run red.

- Implementation: PatternInsightCard component, WhyAmISeeingThis component, wire to Home page below primary next action

- Health check: recovery-checkin build green, Playwright specs green

- Commit: "feat(v5.1): home pattern insight card with affordance"

### Phase F — Dismissal and event logging

- Pre-flight: prior commit exists

- Smoke first: integration test asserting dismissal logs pattern_insight_dismissed, 24h suppression applies to same signal+focus+window only, different signal type can surface same day. Run red.

- Implementation: dismissal handler, event_log inserts for generated/dismissed/action_clicked, suppression lookback logic

- Health check: full api-server and recovery-checkin tests green

- Commit: "feat(v5.1): dismissal logic and event logging"

### Phase G — End-to-end Playwright specs

- Pre-flight: prior commit exists

- Smoke first: Playwright specs from the suite above run against full stack. Run red where new behavior expected.

- Implementation: ensure all e2e specs green

- Health check: full Playwright suite green for new pattern-insight.spec.ts; pre-existing failing tests documented in AUTONOMY_LAYER (classifyRisk.fallback, matchesCrisisKeywords, verifyJwt) are NOT regressions and not in scope to fix

- Commit: "test(v5.1): end-to-end pattern insight specs"

### Phase H — BUILD_REPORT and PR

- Write docs/run-notes/session-2026-MM-DD-v51-pattern-insight-build-report.md per AUTONOMY_LAYER section 5

- Include: per-signal severity scale (1-5) Opus chose with rationale, SPEC_REALITY_DELTA findings, all changed files, unit and Playwright test counts, Council prompt ready to paste, known remaining risks, MANUAL_PLAYTEST_REQUIRED items, confirmation no Neon migration required

- Open PR to main: title "feat: V5.1 Pattern Insight + Drift Detection". Body includes phase summary, changed files, test counts, Council prompt, post-merge actions (none expected)

- Auto-merge: NO. Stop after PR open.

## Forbidden side quests

- Do NOT add a secondary Insights screen

- Do NOT implement pattern_insight_state cache table

- Do NOT implement no_recent_contact signal logic beyond null scaffold

- Do NOT enable anniversary_seasonal signal logic

- Do NOT add user-configurable check-in cadence

- Do NOT write any system-generated inference into stable_profile

- Do NOT add ML, embeddings, vector search, or non-deterministic computation

- Do NOT modify V4 composeSystemPrompt (use assembleSystemPrompt only)

- Do NOT auto-reset trackers or write to practice tables

- Do NOT modify crisis routing path

- Do NOT bundle unrelated cleanup with feature commits per section 1.9

## Self-repair playbook

Apply AUTONOMY_LAYER section 2 (ANCHOR-1 through ANCHOR-16). No new self-repair entries from this directive.

## Deferred-issues format

Per AUTONOMY_LAYER section 4. Log to deferred-issues.md at repo root.

## BUILD_REPORT format

Per AUTONOMY_LAYER section 5.

## Hard stops

Per AUTONOMY_LAYER section 6.

## GO

When Marcus authorizes execution:

Begin Phase A pre-flight per AUTONOMY_LAYER section 3. Credentials preflight scope: none (CC Cloud, code-only). Cut branch from main: feat/v51-pattern-insight. Create ISSUE_EXECUTION_PLAN.md, AUTONOMOUS_RUN_LOG.md, and BLOCKERS_FOR_MARCUS.md at repo root if not already present from V4.1 cycle.
