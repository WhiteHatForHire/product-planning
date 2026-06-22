---
title: "Anchor V4 Master Doc Final"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/Anchor_V4_Master_Doc_Final.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor V4 Master Doc Final

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ANCHOR V4 MASTER DOC

Final Implementation Pack: Post-V3 Stabilization, Product Intelligence, Safety, Trust, and Micromanaged Replit Prompts

Working final • April 25, 2026

Core doctrine: Anchor should reduce isolation and increase wise action. It should not become an AI cocoon. V4 makes the app clearer, safer, more pattern-aware, more reliable, and more capable of bridging the user back to embodied action and real human contact.

Implementation posture: micromanage invariants, contracts, file boundaries, safety behavior, tests, failure states, and platform traps. Let the coding agent discover exact file paths when needed, but do not let it invent architecture, duplicate systems, or broaden scope.

Table of Contents

1. Executive Summary

2. V3 Current State

3. V4 North Star and Product Doctrine

4. Product Invariants

5. What V4 Is and Is Not

6. V3.7 Stabilization Before V4

7. Feature Inventory

8. Improvement Inventory

9. Change and Refactor Inventory

10. Priority Matrix

11. Revised V4 Roadmap

12. Architecture Principles

13. AI System Design

14. Anchor V4 Insight Engine

15. Event Taxonomy and Data Governance

16. Data Contracts

17. Safety and Ethics

18. UX/UI Recommendations

19. Data Model Impact

20. Testing and QA Plan

21. Deployment, Logging, and Operations

22. Do Not Build Yet

23. Implementation Doctrine for AI Coding Agents

24. Replit Prompt Template

25. Final Hardened Replit Implementation Prompts

26. Final Recommended Build Order

27. Closing Note

1. Executive Summary

Anchor V3 is now a working recovery companion: persistent memory, check-in ritual, sponsor-adjacent chat, commitments, voice input, proactive email, TTS, human handoff, and user-controlled memory. V4 should not simply add more features. It should make the product clearer, safer, more trustworthy, more pattern-aware, and easier to use when the user is dysregulated.

The recommended V4 doctrine is simple: do not turn Anchor into an AI cocoon. Make it a better bridge back to wise action and real human contact.

Stabilize and correct post-V3 behavior before adding major product surface area.

Make Home feel like a recovery cockpit: what matters today, what action is next, and how to reach a person.

Add deterministic pattern intelligence before vector databases, agent frameworks, or biometric prediction.

Add persistent SOS and offline safety so human handoff is available without needing AI detection first.

Add trust features: export, explainability, structured logs, debug view, and invariant tests.

Defer high-complexity ideas like realtime voice, wearables, vector RAG, and multi-agent orchestration until real usage proves need.

2. V3 Current State

V3 should be treated as a working foundation. The current system already includes the major ethical and behavioral pillars that make Anchor differentiated.

Pillar

Current V3 capability

Post-V3 concern

Persistent layered memory

stable_profile, recent_summary, event_log, Memory screen

Audit source-of-truth consistency and phone-number exclusion from AI prompts.

Sponsor-adjacent chat

Memory-aware chat, risk-first crisis routing, human handoff

Align chat voice auto-submit behavior and strengthen tests.

Commitment loop

Suggested commitment after check-in, due follow-up banner, completion stats

Add pending commitment visibility before due time.

Human handoff

Saved contacts, meeting links, tell-on-myself, crisis card

Add persistent SOS and offline access.

Voice input and TTS

Whisper transcription and TTS on sponsor-facing responses

Avoid jank and prevent raw audio/transcript leakage.

Proactive email

Daily reminders, missed follow-up, weekly summaries

Harden scheduler, feature flag, structured logs, and production deployment plan.

User control

Memory edit/pin/delete/reset, email settings, onboarding reset

Add export, explainability, debug health, and better source-of-truth discipline.

3. V4 North Star and Product Doctrine

V3 North Star: reduce isolation and increase wise action, not merely comforting conversation. V4 extends this by helping the user notice drift earlier, take the next right action faster, and involve a real person when risk rises.

V4 North Star

Anchor V4 should help the user notice drift earlier, take the next right action faster, and get a real person involved when risk rises.

Doctrine

Pattern intelligence over novelty: make existing behavior visible before adding flashy interfaces.

Human handoff remains the soul: AI can prepare, clarify, and nudge, but it must not replace people.

Deterministic first: use rules, aggregates, and typed helpers before model-heavy infrastructure.

Explain the signal: if Anchor flags a pattern, show why without exposing raw private text.

No automatic social exposure: prefill calls/texts, but the user confirms outbound contact.

Recovery is not gamification: measure follow-through, honesty, contact, and repair, not just streaks.

Privacy by design: do not send phone numbers, raw transcripts, full chat history, or raw journals into unnecessary AI calls.

Phronesis over performance: the app is judged by whether it helps the user choose wisely when judgment is degraded.

4. Product Invariants

These are laws. Every prompt, feature, refactor, and test should preserve them.

Anchor helps the user move toward wise action, not endless conversation.

AI never replaces human handoff.

Crisis flow interrupts normal AI conversation and shows structured crisis resources.

No automatic call, text, email, or social exposure occurs without explicit user confirmation.

Phone numbers never enter AI prompts, memory context, TTS, summaries, logs, or pattern insight copy.

Raw notes, raw transcripts, raw voice input, and full chat history are minimized and never sent to unnecessary AI calls.

Deterministic code computes stats, thresholds, dedupe, drift, and pattern signals.

AI explains, reflects, and supports, but does not fabricate certainty.

Home presents one primary next action at a time.

The user can inspect, edit, pause, export, or delete meaningful memory where applicable.

getCurrentUserId() is used everywhere. No hardcoded user IDs.

Background operations must use safeBackgroundTask() or equivalent safe wrappers.

No new database schema is added unless the prompt explicitly authorizes it.

No duplicate memory, insight, scheduler, or audio systems are created.

Every safety-sensitive helper has tests.

5. What V4 Is and Is Not

V4 is

V4 is not

A stabilization and intelligence layer on top of V3.

A therapist portal.

A better Home experience.

A social network.

A deterministic pattern-detection layer using existing data.

An automatic emergency messaging system.

A safety-access upgrade with SOS and offline resources.

A full multi-agent research lab.

A trust upgrade with export, explainability, debug view, and invariant tests.

A biometric/wearable platform yet.

A disciplined build sequence.

A native app rewrite.

A bridge back to real human contact.

A replacement sponsor or crisis intervention service.

6. V3.7 Stabilization Before V4

Before true V4 features, run focused correction passes. These are not new V4 product bets. They are post-V3 stabilization items.

V3.7A: Safety and Runtime Stabilization

Fix check-in yes/no runtime error at the root cause.

Audit and enforce phone-number exclusion from every AI prompt and memory context.

Audit and enforce raw note, raw transcript, and full chat-history minimization.

Add backend invariant tests for memory, risk, handoff, event log, and background tasks.

Confirm crisis flow stops normal AI generation.

Confirm TTS never receives forbidden source text.

Confirm background tasks cannot crash the app.

V3.7B: UX and Operations Stabilization

Add pending commitment card on Home.

Align chat voice auto-submit behavior with product decision, docs, and tests.

Simplify Home into the Recovery Command Center or recovery cockpit.

Add system health/debug view.

Harden scheduler, email feature flag, and last-run visibility.

Item

Why it matters

Database impact

Priority

Runtime error on check-in yes/no buttons

Runtime overlays destroy trust even if UI still works.

None

P0

Phone-number AI prompt audit and redaction helper

Critical privacy invariant.

None

P0

Raw content minimization audit

Prevents transcript/raw note leakage.

None

P0

Helper invariant tests

Protects memory, event log, risk classifier, handoff, and background tasks.

None

P0

Pending commitment card on Home

A saved commitment currently feels invisible until due.

None

P0

Source-of-truth audit

Prevents drift between stable_profile and app_settings.

Probably none

P0

Scheduler hardening

Proactive outreach is safety-sensitive and must be observable.

Probably none

P0/P1

Chat voice auto-submit alignment

Built behavior, tests, and docs must match.

None

P1

System health/debug view

Makes failures visible during solo development.

Optional none

P1

Home command center simplification

Reduces cognitive friction and clarifies daily loop.

None

P1

7. Feature Inventory

Feature

Description

Build timing

Notes

Pending commitment card

Show current incomplete commitment before it is due.

V3.7

Small UX correction with high value.

Pattern Insight card

One deterministic insight on Home from recent data.

V4.1

Start with rules, not ML.

Drift detection

Detect missed-check-in clusters and changes after strong streaks.

V4.2

High-value predictive feature after insight helper.

SOS Mode

Persistent route to real people and crisis resources.

V4.1/V4.2

No AI required. No auto-send.

Offline safety card

Access contacts, meeting links, 988/SAMHSA/local note offline.

V4.2

Use local cache. No AI.

Data export

Export JSON, CSV, and Markdown recovery records.

V4.3

Trust and portability.

Memory Search Lite

Search event_log and retrieve relevant past events.

V4.4

Before vector DB.

Relapse response protocol

If not sober today, activate specific reset/handoff/repair flow.

V4.5

High value, copy-sensitive.

Micro check-ins

10-second pulse check without AI response.

V4.6

Only if daily check-in feels heavy.

Evening reflection

One win, one thing to improve tomorrow.

V4.6

Feeds weekly summary.

Commitment streak

Track days of follow-through separately from sobriety.

V4.6

Measures the work, not perfection.

Step work integration

Optional prompts based on AA/NA/SMART/current program.

Later

Careful content design.

Realtime voice call mode

Low-latency voice support with guardrails.

Later

Powerful but AI-cocoon risk.

Wearables/Apple Health

Sleep/HRV/activity integration.

Later

High complexity/privacy.

Vector RAG memory

Semantic retrieval over long history.

Later

Only after deterministic search proves insufficient.

8. Improvement Inventory

Area

Improvement

Reason

Home

Rebuild as Recovery Command Center with one primary next action.

Home should answer what matters now.

Insights

Lead with interpretation, not charts.

Recovery users need meaning, not just graphs.

Memory

Add why-this-memory-matters and search/filter.

Makes memory less creepy and more useful.

Commitments

Show pending commitment before due and track follow-through.

Action bias becomes visible.

Chat

If voice auto-submits, add failure restoration and tests.

Fast voice matters if review UI is inadequate.

Email

Add feature flag, last-run logs, and manual scheduler test.

Prevents accidental outreach and debugging pain.

Crisis/SOS

Make human handoff accessible without AI detection first.

Safety access should not depend on model inference.

Testing

Add invariant backend tests and redaction tests.

Protects privacy and safety rules.

UX

Progressive disclosure in Settings and Insights.

Reduces overwhelm.

Logging

Structured safe logs with trace IDs.

Allows audit without exposing private content.

9. Change and Refactor Inventory

Change

Purpose

Risk level

Centralize preference source-of-truth

Avoid stable_profile/app_settings drift.

Medium

Add backend invariant tests

Protect helper behavior and privacy.

Low

Add system health/debug route

Expose scheduler, email, AI, memory, DB status for dev.

Low

Normalize pattern detection helpers

Keep deterministic logic out of prompts and UI.

Low

Separate AI generation from deterministic metrics

Reduce cost and improve reliability.

Medium

Add event actor/source taxonomy

Prevent AI/system inferences from becoming user facts.

Medium

Add local safety cache

Offline SOS resources.

Medium

Refactor Home state loader

Show due, pending, insight, and SOS states cleanly.

Medium

Add export endpoints

Data trust and portability.

Medium

Add structured safe logging

Audit important operations without private content.

Medium

10. Priority Matrix

Category

Feature/Change

User value

Complexity

Risk

Recommendation

P0 correction

Runtime error fixes

High

Low/Med

Med

Build immediately

P0 correction

Phone/raw-content leakage audit

High

Low/Med

High if wrong

Build immediately

P0 correction

Invariant tests

High

Low

Low

Build immediately

P0 correction

Pending commitment card

High

Low

Low

Build immediately

P0/P1 ops

Scheduler hardening

High

Med

High if wrong

Build early

V4 safety

SOS Mode

High

Med

Low if no auto-send

Build soon

V4 core

Home Command Center

High

Med

Low

Build soon

V4 core

Pattern Insight card

High

Low/Med

Low

Build soon

V4 core

Drift detection

High

Med

Low/Med

Build after insight helper

V4 trust

Data export

Med/High

Med

Privacy if sloppy

Build after safety

V4 memory

Memory Search Lite

Med/High

Med

Low

Build before vector DB

Later

Realtime voice

High

High

Medium/High

Defer

Later

Wearables

Med/High

High

High privacy

Defer

Later

Vector RAG

Med

High

Med

Defer until needed

No for now

CrewAI/AutoGen

Unclear

High

High complexity

Reject for now

11. Revised V4 Roadmap

Phase 1: V3.7A Safety and Runtime Lockdown

Runtime error fix.

Phone-number and raw-content leakage audit.

Central redaction/assertion helpers.

Backend invariant tests.

Crisis/TTS/background task verification.

Phase 2: V3.7B Operations and Core Loop Stabilization

Scheduler hardening.

System health/debug view.

Pending commitment card.

Chat voice behavior alignment.

Source-of-truth audit.

Phase 3: V4.0 Home and Handoff

Home Command Center.

SOS Mode.

Offline Safety Cache.

Tell-on-myself/contact polish.

Phase 4: V4.1 Pattern Intelligence

Pattern Insight Engine.

Pattern Insight Card.

Drift Detection.

Why am I seeing this? explanations.

Phase 5: V4.2 Trust and Memory

Data Export and Trust.

Memory Search Lite.

Memory source labeling and retrieval controls.

Phase 6: V4.3 Recovery Protocols

Relapse Response Protocol.

Evening Reflection.

Micro Check-ins only if needed.

Phase 7: Later Differentiators

Step work integration.

Milestone intelligence.

Realtime voice call mode.

Wearables.

Vector RAG.

12. Architecture Principles

Do not create duplicate memory systems.

Do not pass phone numbers to AI.

Do not add automatic outbound messages without explicit user confirmation.

Use AI for synthesis, not counting.

Use deterministic code for stats, thresholds, and dedupe.

Preserve structured crisis handling.

Keep no-auth builds private.

Prefer small helpers and focused prompts over giant rebuild prompts.

Add database schema only when existing storage is insufficient and the prompt explicitly authorizes it.

Every feature must reduce isolation, increase wise action, improve trust, or reduce friction.

Every intelligence helper should be a strict tool-shaped module with typed input and output.

System-generated inferences must never be treated as user-generated facts.

13. AI System Design

V4 should not jump to agent frameworks. Use a modular AI pipeline inside the existing Node/Express system. The deterministic modules should be shaped like strict tools so they are testable today and portable later.

Stage

Purpose

AI or deterministic?

V4 rule

Risk classifier

Determine low/moderate/high/crisis before response.

AI with strict JSON + fallback

Malformed output defaults to moderate.

Memory/context retriever

Pull stable profile, recent summary, safe event summaries.

Deterministic first

Phone numbers excluded. Raw notes minimized.

Pattern detector

Compute drift, triggers, trends, completion patterns.

Deterministic

No AI required for V4.1.

Response generator

Produce sponsor-adjacent language.

AI

Must respect risk route and memory limits.

Action recommender

Suggest one concrete next move.

Hybrid

Prefer deterministic priority order.

Safety validator

Reject AI cocoon, enforce handoff/crisis rules.

Deterministic + optional AI later

Blocks unsafe behavior.

Logger/telemetry

Record structured safe events.

Deterministic

No private content in logs.

Do not build CrewAI, AutoGen, full vector RAG, realtime voice, or biometric prediction in this version. Build strict, typed modules now so those options remain possible later without rewriting the core logic.

14. Anchor V4 Insight Engine

The Insight Engine prevents Pattern Insight, Drift Detection, and future What Helps/What Hurts features from becoming duplicate systems. There should be one deterministic engine that produces ranked signals and one primary insight for Home.

Collect source data: check_ins, commitments, event_log, tracker state, and stable_profile only where relevant.

Filter event_log by actor/source so AI-generated interpretations are not treated as user facts.

Compute deterministic signals: missed check-ins, craving trend, sleep trend, commitment completion, recent contact gap, tracker resets, and SOS openings.

Rank signals: safety first, drift second, commitment/action loop third, encouragement fourth.

Generate one primary insight for Home. Secondary insights may live in Insights later.

Attach explainability using data basis, not raw notes.

Recommend one next action: check in, contact someone, go to meeting, complete commitment, simplify day, or SOS.

Return null if the data is insufficient.

Signal

Minimum data

Allowed copy

Forbidden copy

Missed check-in drift

At least 3 recent check-ins, then 2 expected check-ins missed

Your pattern changed a little. This might be nothing, but it is worth checking in.

Relapse risk detected. You are slipping.

Rising craving

At least 3 numeric craving values

Craving has been trending higher across your recent check-ins. Keep the next action small.

You are about to relapse.

Low sleep + high craving

At least 4 check-ins with both sleep and craving

Low-sleep days have lined up with harder craving days recently. Keep tonight simple.

Your sleep caused your craving.

Repeated incomplete commitments

At least 2 recent incomplete commitments

The follow-through loop needs attention. Pick one smaller promise today.

You keep failing commitments.

No recent contact

Only if contact tracking is reliable

You have not logged contact recently. Consider one low-pressure text.

You are isolating dangerously.

15. Event Taxonomy and Data Governance

This is a critical V4 addition. The system must distinguish user-generated facts from system actions and AI-generated interpretations. Otherwise, Anchor can start reading its own old assumptions as user truth.

Required event fields

type EventActor = "user" | "system" | "ai" | "scheduler";

type EventSource =

| "checkin"

| "chat"

| "commitment"

| "tracker"

| "sos"

| "email"

| "memory"

| "pattern_insight"

| "risk_classifier"

| "debug";

type EventKind =

| "check_in_submitted"

| "commitment_created"

| "commitment_completed"

| "tracker_reset"

| "sos_opened"

| "human_contact_opened"

| "pattern_insight_generated"

| "email_sent"

| "risk_classification"

| "memory_summary_updated"

| "scheduler_run"

| "system_error";

type EventLogEntry = {

id: string;

timestamp: string;

actor: EventActor;

source: EventSource;

kind: EventKind;

summary: string;

metadata?: Record<string, unknown>;

};

Retrieval rules

Pattern detection uses user behavioral events and direct check-in/commitment data.

Pattern detection must not use old pattern_insight_generated events as evidence.

Memory summaries may include system events only when clearly labeled.

Chat memory should not treat AI inference as user truth.

Why am I seeing this? should cite computed signals, not old AI conclusions.

Event summaries must be compact and should not contain raw notes, full transcripts, phone numbers, or secrets.

16. Data Contracts

Every V4 feature should use explicit contracts. These are intended to be adapted to the actual codebase, but the shapes should guide implementation.

StableProfile source-of-truth map

Data

Source of truth

Notes

recovery focus

stable_profile

User-editable.

support style

stable_profile

Used in safe memory context.

sobriety why

stable_profile

Pinned if user chooses.

sober contact names

stable_profile or contacts payload

Names may appear in AI context.

sober contact phone numbers

frontend/handoff payload only

Never AI context.

meeting links

stable_profile or safety profile

May be cached offline.

reminder time

stable_profile

Used by scheduler.

email address

choose stable_profile or app_settings

Must be consistent.

onboarding complete/version

app_settings

System metadata.

last email sent timestamps

app_settings

Scheduler metadata.

memory pause flag

app_settings/session state

Skips memory injection for session.

pinned facts

stable_profile

User-controlled.

event log

user_memory.event_log

Typed event entries.

PatternInsight contract

type PatternInsight = {

id: string;

type:

| "missed_checkin_drift"

| "rising_craving"

| "low_sleep_high_craving"

| "repeated_incomplete_commitments"

| "no_recent_contact";

severity: "low" | "medium" | "high";

title: string;

body: string;

why: string[];

suggestedAction: {

label: string;

action: "checkin" | "chat" | "sos" | "contact" | "meeting" | "commitment";

};

dataWindowDays: number;

};

type PatternInsightResult = {

insight: PatternInsight | null;

diagnostics: {

signalsChecked: string[];

insufficientDataReasons: string[];

};

};

Safe logging contract

type SafeLogEvent = {

level: "info" | "warn" | "error";

event:

| "risk_classifier_failed"

| "risk_route_chosen"

| "crisis_card_shown"

| "sos_opened"

| "human_handoff_opened"

| "ai_call_failed"

| "scheduler_run_failed"

| "scheduler_run_completed"

| "export_generated"

| "phone_redaction_triggered"

| "invariant_violation_blocked";

userId?: string;

traceId: string;

timestamp: string;

metadata?: Record<string, unknown>;

};

// Never log raw notes, transcripts, full prompts, phone numbers, secrets, API keys, or full chat history.

17. Safety and Ethics

Anchor is not a therapist, crisis service, or human sponsor.

At crisis: AI conversation stops; resource card and human contact options take over.

At moderate/high risk: human handoff must be visible.

SOS Mode bypasses AI and is available from major screens.

Never auto-send texts, calls, or emails to contacts without explicit confirmation.

Do not use shame language after relapse/reset.

Do not create endless AI soothing loops.

If distress conversation continues too long, gently nudge toward human contact or embodied action.

Always preserve user control over memory, email, contacts, and exports.

Never include phone numbers, raw transcripts, full chat history, or raw notes in unnecessary AI prompts.

If outside the U.S., show local emergency language alongside 988/SAMHSA where applicable.

18. UX/UI Recommendations

Home as Recovery Command Center

Home should answer only three questions: Where am I today? What is the next right action? How do I reach a human if needed?

Recovery State: checked in today or not, sobriety state if available, calm neutral tone.

Primary Next Right Action: crisis/SOS, due commitment, pending commitment, missed check-in drift, suggested check-in, human contact, or reflection.

Secondary Pattern Insight: one card only, collapsible why section.

Quick Actions: Check In, Chat, SOS, Contacts/Meetings.

Sobriety counters and stats below the primary action, not above it.

SOS Mode UX

Header: Need a person or immediate support?

Subtext: Anchor will not send anything automatically. You stay in control.

Primary actions: call saved contact, text saved contact, open meeting link, copy tell-on-myself message.

Crisis resources: 988, SAMHSA, local emergency note if outside U.S.

Tiny grounding fallback: Put both feet on the floor. Take one breath. Then tap one person.

No AI chat inside SOS Mode.

Settings

Group settings into Account/Data, Recovery Profile, Contacts/Meetings, Email, Memory, Safety, Advanced/Debug.

Hide developer/system details unless in dev mode.

Keep destructive controls behind confirmations.

Explain offline safety cache and provide Clear Cache control.

19. Data Model Impact

Feature

Data impact

Recommended storage

Pending commitment card

None

Existing commitments table

Pattern Insight card

None initially

Computed from check_ins, commitments, event_log

Drift detection

None initially

Computed server-side

SOS Mode

Optional event log

Existing stable_profile plus optional event_log entry

Offline safety cache

Local cache only

localStorage or IndexedDB

Data export

None

Existing tables, export endpoints

Memory Search Lite

None initially

event_log keyword/date filtering

Event taxonomy

May need shape migration

Existing event_log entries plus normalization

Micro check-ins

Likely new type or table

Prefer existing check_ins type if safe

Evening reflection

New type or event_log kind

Could use event_log first

Commitment streak

None

Computed from commitments

Vector RAG

New embeddings table/vector store

Defer

Wearables

New integration tables

Defer

20. Testing and QA Plan

Backend invariant tests

normalizeStableProfile fills all expected fields with safe defaults.

buildMemoryContext excludes phone numbers in common U.S. and Indonesian formats.

appendEventLog caps event_log at 90 and handles malformed logs.

event_log preserves actor/source/kind taxonomy and does not treat AI inference as user fact.

classifyRisk defaults to moderate on malformed output.

loadUserMemory creates a default memory row safely.

buildHandoffPayload returns phone numbers only for frontend payload use.

safeBackgroundTask catches rejected promises.

redactPhoneNumbers removes phone numbers from AI-bound payloads.

assertNoPhoneNumbers blocks AI-bound payloads in test/dev mode.

Manual QA checklist

Save commitment; verify pending card appears on Home.

Make commitment due; verify due banner appears.

Tap yes/no pills; verify no runtime overlay.

Use chat voice auto-submit; verify send failure restores transcript.

Trigger high risk; verify handoff visible.

Trigger crisis; verify structured crisis card, no normal AI result.

Open SOS from Home, Check-In, Chat, and Settings safety section.

Go offline; verify safety card if built.

Run export; verify no raw phone leak.

Use Pattern Insight with no data; verify no card.

Use Pattern Insight with trend data; verify one card and why section.

Run scheduler manually in dev; verify no email if feature flag disabled.

Check logs; verify no raw text or phone numbers.

E2E smoke tests

App loads.

Navigation tabs render.

Check-in form opens.

Chat opens and mocked response returns.

Commitment save flow.

Home pending/due commitment states.

Settings loads and saves.

Trackers render.

History/Insights render.

SOS opens from major screens.

Export buttons produce files.

21. Deployment, Logging, and Operations

Keep Replit preview as dev/testing, not production scheduling guarantee.

Use EMAIL_OUTREACH_ENABLED feature flag for scheduled emails.

Add system health/debug page with database, OpenAI, Resend, scheduler, memory, and last cron status.

Use structured safe logging with trace IDs. Do not log private content.

Add manual Run Scheduler Now dev action only if it cannot accidentally email users when disabled.

Move to Reserved VM, Scheduled Deployment, or external scheduler before public email outreach.

Track environment variable presence in Settings/Debug without exposing values.

Use feature flags for V4 features so broken new work can be disabled quickly.

Recommended feature flags

EMAIL_OUTREACH_ENABLED=false

SOS_MODE_ENABLED=true

PATTERN_INSIGHTS_ENABLED=true

OFFLINE_SAFETY_CACHE_ENABLED=true

DATA_EXPORT_ENABLED=true

DEBUG_HEALTH_ENABLED=true

RUN_LIVE_AI_TESTS=false

22. Do Not Build Yet

CrewAI / AutoGen orchestration.

Full vector database memory.

Automatic texting of contacts.

Apple Health / Oura / Whoop integration.

Realtime voice call mode as default interface.

Therapist portal.

Social/community feed.

Native iOS/Android rewrite.

Accountability partner pairing.

Meeting API integration.

Voice tone analysis.

Full local-only encrypted offline mode.

Biometric relapse prediction.

Autonomous outreach escalation.

23. Implementation Doctrine for AI Coding Agents

The V4 prompts should be micromanaged. The goal is not to micromanage taste. The goal is to micromanage invariants, boundaries, contracts, failure behavior, and verification.

Rules

Every prompt begins with stack context and preservation instructions.

Every prompt includes a pre-flight inspection step.

When exact file paths are unknown, the agent must discover and report target files first.

When exact file paths are known, list target files and forbidden files.

Every prompt includes V3/V4 invariants relevant to the feature.

Every prompt defines out-of-scope behavior.

Every feature with data must define input/output contracts.

Every safety-sensitive feature must define failure behavior.

Every feature must include tests or a manual QA checklist.

Every prompt ends with a concise final report requirement.

The agent must not create new parallel systems when a helper or component already exists.

The agent must not change unrelated UI, schema, secrets, deployment, or auth.

What to micromanage

Safety invariants.

Privacy boundaries.

AI prompt inputs.

Data contracts.

File boundaries.

Endpoint contracts.

Platform traps like iOS Safari audio.

Loading/error/empty states.

Test cases.

Final verification report.

What not to micromanage unless necessary

Minor component naming when existing code conventions differ.

CSS class names if the app already has a design system.

Internal implementation details that do not affect contracts, safety, or UX.

Exact file paths before inspection if the codebase structure is unknown.

24. Replit Prompt Template

# ANCHOR V4.X: FEATURE NAME

Upgrade the existing recovery check-in app with [specific feature] only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

Use existing V3A through V3F architecture and patterns. Extend what exists.

Do not rebuild from scratch. Preserve all prior V3 behavior.

IMPORTANT CONSTRAINTS:

- Do NOT add new database tables or columns unless this prompt explicitly authorizes it.

- Do NOT add unrelated product features.

- Do NOT change auth, deployment, secrets, or unrelated UI.

- Do NOT create duplicate memory, insight, scheduler, handoff, or audio systems.

- Do NOT send phone numbers, raw notes, raw transcripts, or full chat history to AI.

PRE-FLIGHT:

Inspect the current implementation. Report in 5 bullets:

1. Relevant files to modify.

2. Existing helpers/routes/components to reuse.

3. Whether any similar feature already exists.

4. Conflicts with prior phases or tests.

5. Implementation plan.

Then proceed using only the relevant files.

V3/V4 INVARIANTS:

- getCurrentUserId() everywhere. No hardcoded user IDs.

- Phone numbers never in AI prompts, memory context, TTS, summaries, logs, or insights.

- Crisis flow stops normal AI response generation.

- Human handoff remains visible at moderate/high risk.

- No automatic outbound contact without explicit user confirmation.

- All background async operations use safeBackgroundTask() or equivalent.

- Pattern/stat logic must be deterministic unless explicitly stated otherwise.

SCOPE:

[exact build scope]

OUT OF SCOPE:

[exact non-goals]

DATA CONTRACT:

[types, endpoints, helpers, request/response shapes]

FRONTEND REQUIREMENTS:

[components, states, loading, empty, error, accessibility]

BACKEND REQUIREMENTS:

[routes, helpers, validation, failure behavior]

TESTS:

[unit/invariant/manual/e2e]

AT THE END:

Report files changed, behavior confirmed, tests run, known issues, and exact next step.

Keep final report under 300 words.

25. Final Hardened Replit Implementation Prompts

Run these one at a time. Do not paste the full Master Doc into Replit. Each prompt is deliberately micromanaged in the style of the V3F1 TTS prompt.

Prompt 1: V3.7A Safety and Runtime Stabilization

# V3.7A: SAFETY AND RUNTIME STABILIZATION

Upgrade the existing recovery check-in app with safety and runtime fixes only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

V3A through V3F should already be in place. Extend what exists. Do not rebuild from scratch.

Preserve persistent memory, check-in, chat, commitments, crisis routing, TTS, voice input, email, and handoff behavior.

IMPORTANT CONSTRAINTS:

- Do NOT add new database tables or columns.

- Do NOT add new product features.

- Do NOT change auth, deployment, secrets, or unrelated UI.

- Do NOT silence runtime overlays by config unless the underlying bug is confirmed harmless and fixed.

- Do NOT create duplicate memory, risk, handoff, event log, or audio systems.

PRE-FLIGHT:

Inspect current implementation. Confirm in 7 bullets:

1. Relevant files for check-in yes/no pill buttons.

2. Relevant files for AI prompt construction.

3. Relevant files for memory context construction.

4. Relevant files for TTS text selection.

5. Relevant files for crisis/risk routing.

6. Relevant files for event_log helpers.

7. Implementation plan.

Then proceed.

V3/V4 INVARIANTS:

- getCurrentUserId() everywhere. No hardcoded IDs.

- Phone numbers never in AI prompts, memory context, TTS, summaries, logs, or pattern insights.

- Raw notes, raw transcripts, and full chat history are not sent to unnecessary AI calls.

- Crisis flow stops normal AI response generation.

- Human handoff remains visible at moderate/high risk.

- safeBackgroundTask() or equivalent wraps background async work.

- No new schema.

SCOPE:

1. Reproduce and fix the check-in yes/no runtime error at the root cause.

2. Add or verify a phone-number redaction helper.

3. Add or verify an AI-bound payload assertion helper for phone numbers in dev/test.

4. Audit memory context, chat prompt, check-in prompt, weekly summary prompt, risk classifier prompt, TTS endpoint, and scheduler prompts for forbidden data leakage.

5. Confirm crisis flow still blocks normal AI response.

6. Confirm TTS only receives sponsor-facing visible text and never raw notes/transcripts/user messages.

PHONE REDACTION REQUIREMENTS:

Create or reuse helpers similar to:

redactPhoneNumbers(text: string): string

assertNoPhoneNumbers(label: string, payload: unknown): void

The detection should catch at minimum:

- +1 555 123 4567

- (555) 123-4567

- 555-123-4567

- 555.123.4567

- +62 812-3456-7890

- long digit sequences that look like phone numbers

Do not over-redact normal short numbers like sobriety days, ratings, or dates.

RUNTIME ERROR REQUIREMENTS:

- Reproduce the yes/no pill bug.

- Capture the actual browser/runtime error.

- Fix the root cause.

- Do not hide the overlay as the primary solution.

- Verify yes/no pills still update state correctly.

AI PAYLOAD AUDIT REQUIREMENTS:

Inspect every server-side call that sends text to OpenAI or another AI service.

Before AI calls, ensure payloads do not include:

- phone numbers

- raw voice transcripts unless specifically required for transcription flow

- raw private notes unless specifically required for the check-in response

- full chat history beyond intended context window

- secrets or API keys

Do not log full AI prompts.

TESTS:

Add or update tests for:

1. redactPhoneNumbers catches U.S. and Indonesian formats.

2. assertNoPhoneNumbers blocks AI-bound payload with phone numbers in test/dev mode.

3. buildMemoryContext excludes phone numbers but may include contact names.

4. TTS text selection excludes user messages and raw notes.

5. Crisis route does not continue normal AI response generation.

MANUAL QA:

- Tap every yes/no pill and confirm no runtime overlay.

- Complete a check-in and confirm normal behavior.

- Trigger high-risk input and confirm handoff remains visible.

- Trigger crisis input and confirm structured crisis card appears instead of normal AI result.

- Use TTS and confirm it still works.

AT THE END:

Report: root cause of runtime error, files changed, redaction/assertion helpers added or verified, AI payload surfaces audited, tests run, manual QA results, known issues, and exact next step for V3.7B. Keep under 300 words.

Prompt 2: V3.7B Backend Invariant Test Suite

# V3.7B: BACKEND INVARIANT TEST SUITE

Upgrade the existing recovery check-in app with backend invariant tests only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

V3A through V3F should already be in place. Extend existing test setup. Do not rebuild.

IMPORTANT CONSTRAINTS:

- Do NOT add product features.

- Do NOT change UI.

- Do NOT add database tables or columns.

- Do NOT call live OpenAI unless RUN_LIVE_AI_TESTS=true.

- Do NOT change product behavior except to make helpers testable.

- Use mocks for AI, email, and database where appropriate.

PRE-FLIGHT:

Inspect current implementation. Confirm in 6 bullets:

1. Existing test framework and commands.

2. Existing helper files for memory/profile/event log.

3. Existing helper files for risk classification.

4. Existing handoff/contact helper files.

5. Existing background task helper files.

6. Implementation plan.

V3/V4 INVARIANTS TO TEST:

- normalizeStableProfile fills all expected keys with safe defaults.

- buildMemoryContext excludes phone numbers.

- appendEventLog caps event_log at 90 and handles malformed logs.

- classifyRisk defaults to moderate on malformed model output.

- loadUserMemory creates a default memory row safely.

- buildHandoffPayload returns phone numbers only for frontend payload use.

- safeBackgroundTask catches rejected promises.

- event_log entries preserve actor/source/kind taxonomy if taxonomy exists.

- system/AI-generated inference events are not treated as user facts by pattern helpers if any exist.

TEST REQUIREMENTS:

1. Do not rely on network calls.

2. Mock OpenAI classifier responses.

3. Mock malformed classifier output.

4. Mock missing memory row.

5. Mock malformed event_log.

6. Include phone numbers in multiple formats.

7. Verify contact names may be included where allowed but phone numbers are excluded.

8. Verify background task rejection is caught and logged safely.

IF HELPERS ARE NOT TESTABLE:

- Extract pure helper functions with minimal behavior change.

- Do not rewrite feature logic.

- Do not create duplicate helpers.

- Preserve existing exports unless unsafe.

COMMANDS:

Add or update package scripts if needed for:

- unit tests

- backend invariant tests

AT THE END:

Report: test files added/changed, helpers made testable, exact commands run, pass/fail results, skipped tests with reasons, and exact next step for Scheduler Hardening. Keep under 300 words.

Prompt 3: V3.7C Scheduler Hardening

# V3.7C: SCHEDULER HARDENING

Upgrade the existing recovery check-in app with scheduler hardening only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app may already include daily reminders, missed follow-up emails, and weekly summaries through Resend/node-cron or similar.

Extend existing scheduler code. Do not rebuild from scratch.

IMPORTANT CONSTRAINTS:

- Do NOT change email copy unless required for safety or broken behavior.

- Do NOT send scheduled emails unless EMAIL_OUTREACH_ENABLED=true.

- Do NOT add new database tables unless absolutely necessary. Prefer existing app_settings or metadata storage.

- Do NOT expose API keys or email secrets.

- Do NOT log private user content.

- Do NOT send duplicate emails in the same intended window.

PRE-FLIGHT:

Inspect current implementation. Confirm in 7 bullets:

1. Existing scheduler files.

2. Existing email sending helper files.

3. Existing app_settings or send-tracking fields.

4. Existing environment variables.

5. Whether EMAIL_OUTREACH_ENABLED already exists.

6. Whether manual test email exists.

7. Implementation plan.

V3/V4 INVARIANTS:

- getCurrentUserId() everywhere. No hardcoded IDs.

- No scheduled email sends unless feature flag is true.

- No phone numbers in email generation prompts or logs.

- No raw notes/transcripts in logs.

- Background scheduler errors must not crash the Express server.

- safeBackgroundTask() or equivalent wraps async scheduler operations.

GOALS:

1. Add or enforce EMAIL_OUTREACH_ENABLED gate.

2. Add last scheduler run status.

3. Add last successful daily/missed/weekly send timestamps if not already tracked.

4. Add concise structured logs for scheduler started/completed/failed.

5. Add dev-only manual Run Scheduler Now endpoint or function if safe.

6. Prevent accidental duplicate sends.

STRUCTURED LOGGING:

Use existing logger if present. If not present, create a minimal safe logger wrapper.

Log JSON-shaped events with:

- level

- event

- userId if safe

- traceId if available or generated

- timestamp

- metadata without private content

Never log:

- raw check-in notes

- raw transcripts

- full AI prompts

- email body text

- phone numbers

- API keys

- secrets

FEATURE FLAG BEHAVIOR:

If EMAIL_OUTREACH_ENABLED is not true:

- scheduled job may compute due work

- scheduled job must not send real email

- debug status should say disabled by flag

- manual test email may remain manual if already implemented and clearly user-triggered

DEV-ONLY RUN ENDPOINT:

If adding an endpoint:

- protect it as dev-only

- do not expose in production UI

- do not send if EMAIL_OUTREACH_ENABLED=false

- return JSON status

- do not include private content in response

TESTS:

Add or update tests for:

1. Scheduler does not send when EMAIL_OUTREACH_ENABLED=false.

2. Scheduler can send when enabled and due, using mocked email sender.

3. Duplicate send prevention works.

4. Scheduler failure is caught and logged safely.

5. Logs do not include private content or phone numbers.

AT THE END:

Report: scheduler files changed, feature flag behavior confirmed, send-tracking confirmed, structured logs confirmed, tests run, known issues, and exact next step for System Health Debug View. Keep under 300 words.

Prompt 4: V3.7D System Health Debug View

# V3.7D: SYSTEM HEALTH DEBUG VIEW

Upgrade the existing recovery check-in app with a private dev-only health/debug view only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

Extend existing Settings, admin, or debug patterns if present. Do not rebuild.

IMPORTANT CONSTRAINTS:

- Dev-only. Do not expose this as a normal user-facing feature.

- Do NOT expose secrets, API key values, tokens, raw prompts, raw notes, transcripts, phone numbers, or full chat history.

- Do NOT add new database tables unless absolutely necessary.

- Do NOT change scheduler behavior except to read status.

- Do NOT create a production admin system.

PRE-FLIGHT:

Inspect current implementation. Confirm in 6 bullets:

1. Existing Settings or debug UI files.

2. Existing backend route structure.

3. Existing app_settings/scheduler status fields.

4. Existing environment variable access pattern.

5. Existing logger if any.

6. Implementation plan.

V3/V4 INVARIANTS:

- getCurrentUserId() everywhere. No hardcoded IDs.

- No secrets shown.

- No phone numbers shown.

- No raw private content shown.

- Debug route must be gated by environment/dev mode.

GOAL:

Add a private health/debug surface that helps solo development and QA.

BACKEND STATUS SHOULD INCLUDE:

- database connection status

- OpenAI env presence, not value

- Resend env presence, not value

- EMAIL_OUTREACH_ENABLED status

- last scheduler run timestamp/status if available

- last daily/missed/weekly email send tracking if available, no email body

- user_memory row exists

- event_log count

- last_checkin_local_date if available

- feature flag statuses

- smoke test command hints

FRONTEND VIEW:

- Place behind Settings > Advanced/Debug or a dev-only route.

- Show status cards or simple rows.

- Use dark theme.

- Clearly label as Dev Only.

- Do not show in production mode.

- Include refresh button.

ERROR BEHAVIOR:

- If one check fails, show partial status instead of crashing.

- Log concise safe error server-side.

- Frontend should display “unavailable” for failed checks.

TESTS:

Add or update tests for:

1. Debug endpoint does not reveal env values.

2. Debug endpoint does not include phone numbers.

3. Debug endpoint returns partial status on failed checks.

4. Production gating works or route is clearly disabled outside dev.

MANUAL QA:

- Open debug view in dev.

- Confirm statuses render.

- Confirm refresh works.

- Confirm no secrets or phone numbers appear.

- Confirm production gating behavior.

AT THE END:

Report: route/view files changed, statuses included, dev gating confirmed, secrets not exposed confirmed, tests run, known issues, and exact next step for Pending Commitment Card. Keep under 300 words.

Prompt 5: V3.7E Pending Commitment Card

# V3.7E: PENDING COMMITMENT CARD

Upgrade the existing recovery check-in app with a pending commitment card on Home only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has commitments and may already show due follow-up banners.

Extend the existing commitment/Home flow. Do not rebuild.

IMPORTANT CONSTRAINTS:

- Do NOT add new database tables or columns.

- Do NOT change commitment creation logic unless it is broken.

- Do NOT remove the existing due commitment banner.

- Do NOT add new AI behavior.

- Do NOT change unrelated Home UI beyond what is required.

PRE-FLIGHT:

Inspect current implementation. Confirm in 6 bullets:

1. Existing commitment data model or API shape.

2. Existing Home component files.

3. Existing due commitment banner logic.

4. Existing local time/date helper usage.

5. Edge cases found.

6. Implementation plan.

V3/V4 INVARIANTS:

- getCurrentUserId() everywhere. No hardcoded IDs.

- Commitment text is user-visible only. Do not send it to AI in this prompt.

- No new schema.

- Existing due banner remains higher priority than pending card.

GOAL:

If an incomplete commitment exists but is not yet due, show a Current Commitment card on Home.

DISPLAY RULES:

Priority order:

1. If incomplete commitment is due, show existing due banner. Do not also show pending card for the same commitment.

2. If incomplete commitment exists but is not due, show pending card.

3. If no incomplete commitment exists, show nothing.

CARD COPY:

Title: Current commitment

Body: [commitment text]

Subtext: I’ll ask you about it around [local due time].

If due time is missing:

Subtext: I’ll ask you about it when it comes due.

ACTIONS:

- If existing flow supports viewing or completing commitment, use existing action.

- Do not create a new completion system if one already exists.

- Do not add AI suggestions.

UX:

- Match dark theme.

- Keep tap targets 44px minimum.

- Card should not dominate Home.

- It should feel like a quiet reminder, not a warning.

ERROR/EMPTY STATES:

- If commitments fail to load, do not block Home.

- Log concise safe error.

- Show no pending card rather than scary error UI unless existing Home error pattern requires it.

TESTS:

Add or update tests for:

1. No incomplete commitment means no card.

2. Incomplete not-due commitment shows pending card.

3. Due commitment shows due banner, not duplicate pending card.

4. Missing due time uses fallback copy.

5. Completed commitment does not show.

MANUAL QA:

- Create a commitment due later and confirm card appears.

- Make it due and confirm due banner appears instead.

- Complete it and confirm card disappears.

- Refresh Home and confirm state persists.

AT THE END:

Report: files changed, commitment priority logic confirmed, no schema changes confirmed, tests run, manual QA results, known issues, and exact next step for Home Command Center. Keep under 300 words.

Prompt 6: V4.0 Home Command Center

# V4.0: HOME COMMAND CENTER

Upgrade the existing recovery check-in app Home screen into a Recovery Command Center only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

Use existing Home, check-in, chat, commitment, tracker, and handoff data. Extend what exists.

Do not rebuild the app shell.

IMPORTANT CONSTRAINTS:

- Do NOT add new database tables or columns.

- Do NOT add AI calls.

- Do NOT remove existing features or data.

- Do NOT change unrelated screens.

- Do NOT create new commitment, tracker, or check-in systems.

- Do NOT add Pattern Insight logic in this prompt unless it already exists.

PRE-FLIGHT:

Inspect current implementation. Confirm in 7 bullets:

1. Existing Home component structure.

2. Existing data loaders used by Home.

3. Existing check-in status source.

4. Existing commitment due/pending source.

5. Existing tracker/sobriety counter source.

6. Existing navigation/action patterns.

7. Implementation plan.

V3/V4 INVARIANTS:

- Home should answer: where am I today, what is the next right action, and how do I reach a human?

- One primary next action at a time.

- SOS/handoff should be easy to reach.

- No phone numbers displayed unless user explicitly opens contact/handoff action.

- No AI calls for this prompt.

HOME ORDER:

1. Recovery State: checked in today or not, sobriety/tracker state if available.

2. Primary Next Right Action:

- crisis/SOS if currently routed there by existing state

- due commitment

- pending commitment

- check in today

- contact/handoff nudge if already supported

3. Pattern Insight placeholder area only if existing insight helper exists. Otherwise omit.

4. Quick actions: Check In, Chat, SOS, Contacts/Meetings if available.

5. Sobriety counters/stats lower on page.

COPY RULES:

- Calm, direct, non-gamified.

- Avoid shame.

- Avoid hype.

- Avoid long paragraphs.

- Avoid “relapse risk detected.”

UX RULES:

- Match dark theme.

- Minimum tap target 44px.

- Progressive disclosure for stats.

- Do not bury Check In, Chat, or SOS.

- Home should be usable while dysregulated.

ERROR/EMPTY STATES:

- If one data source fails, render partial Home.

- If commitment load fails, omit commitment card and log safe error.

- If tracker load fails, omit tracker summary and log safe error.

- Do not crash Home due to optional data failure.

TESTS:

Add or update tests for:

1. Home renders with no data.

2. Home renders checked-in state.

3. Home renders not-checked-in state.

4. Due commitment outranks pending commitment.

5. Quick actions route correctly.

6. Missing optional data does not crash Home.

MANUAL QA:

- Open Home with no commitment.

- Open Home with pending commitment.

- Open Home with due commitment.

- Open Home after today’s check-in.

- Test all quick action buttons.

- Confirm mobile layout is clean.

AT THE END:

Report: Home hierarchy changed, files changed, no new AI/schema confirmed, tests run, manual QA results, known issues, and exact next step for SOS Mode. Keep under 300 words.

Prompt 7: V4.1 SOS Mode

# V4.1: SOS MODE

Upgrade the existing recovery check-in app with persistent SOS Mode only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has saved sober contacts, meeting links, human handoff, and crisis resources.

Extend those existing systems. Do not rebuild.

IMPORTANT CONSTRAINTS:

- Do NOT add automatic texting, calling, or emailing.

- Do NOT send phone numbers to AI.

- Do NOT add AI conversation inside SOS Mode.

- Do NOT require AI risk detection to open SOS Mode.

- Do NOT add new database schema unless absolutely necessary. Prefer existing stable_profile/handoff data.

- Do NOT remove existing crisis card behavior.

PRE-FLIGHT:

Inspect current implementation. Confirm in 7 bullets:

1. Existing contact/handoff data source.

2. Existing crisis resource card files.

3. Existing meeting link storage.

4. Existing Home/Chat/Check-In navigation patterns.

5. Existing tell-on-myself copy or helper if present.

6. Whether an event_log helper exists.

7. Implementation plan.

V3/V4 INVARIANTS:

- Human handoff remains the soul of the app.

- SOS bypasses AI.

- User must manually tap Call/Text/Send.

- Phone numbers never enter AI prompts, logs, memory context, or TTS.

- No automatic outbound contact.

- Crisis flow remains intact.

WHERE SOS APPEARS:

- Home quick actions.

- Chat header or safety affordance.

- Check-In screen safety affordance.

- Settings > Safety section if appropriate.

SOS SCREEN CONTENT:

Header: Need a person or immediate support?

Subtext: Anchor will not send anything automatically. You stay in control.

Actions:

1. Call saved sober contact.

2. Text saved sober contact.

3. Open saved meeting link.

4. Copy or open tell-on-myself message.

5. Call 988.

6. Call SAMHSA if included.

7. Show local emergency note: If you are outside the U.S., contact local emergency services.

IF NO CONTACTS:

- Still show 988, SAMHSA, local emergency note, meeting links if available.

- Show Add sober contact prompt using existing settings/onboarding path.

- Do not crash.

TELL-ON-MYSELF TEMPLATE:

Use calm, plain copy:

“I need to tell on myself before I isolate. I’m having a hard moment and I don’t want to handle it alone. Can you check in with me?”

EVENT LOG:

Optional: append compact event only if safe:

- actor: "user"

- source: "sos"

- kind: "sos_opened"

- summary: "User opened SOS mode."

Do not store phone numbers in event_log.

UX:

- Full-screen or modal route is acceptable.

- Dark theme.

- Large buttons.

- 44px minimum tap targets.

- No long AI-like paragraphs.

- Add a tiny grounding line: Put both feet on the floor. Take one breath. Then tap one person.

TESTS:

Add or update tests for:

1. SOS opens from Home.

2. SOS opens from Chat.

3. SOS opens from Check-In.

4. No contacts state works.

5. Phone numbers are not sent to AI/logs/event_log.

6. Buttons use tel:/sms: or platform-appropriate manual links only.

7. No automatic sending occurs.

MANUAL QA:

- Open SOS from all major surfaces.

- Verify no contact state.

- Verify saved contact state.

- Verify meeting link opens.

- Verify tell-on-myself message can be copied/opened manually.

- Verify no AI request is made when opening SOS.

AT THE END:

Report: SOS surfaces added, no auto-send confirmed, no AI usage confirmed, phone privacy confirmed, tests run, manual QA results, known issues, and exact next step for Offline Safety Cache. Keep under 300 words.

Prompt 8: V4.1B Offline Safety Cache

# V4.1B: OFFLINE SAFETY CACHE

Upgrade the existing recovery check-in app with Offline Safety Cache only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app should already have SOS Mode or human handoff resources.

Use simple client-side storage. Do not build a full offline database.

IMPORTANT CONSTRAINTS:

- Do NOT cache raw check-ins.

- Do NOT cache chat history.

- Do NOT cache raw notes.

- Do NOT cache raw transcripts.

- Do NOT cache recent_summary or full memory context.

- Do NOT send cached contacts to AI.

- Do NOT add service worker complexity unless the app already uses one and it is necessary.

- Do NOT build full local encrypted offline mode.

PRE-FLIGHT:

Inspect current implementation. Confirm in 6 bullets:

1. Existing SOS/handoff resources.

2. Existing saved contacts shape.

3. Existing meeting links shape.

4. Existing Settings structure.

5. Existing offline/PWA/service worker behavior if any.

6. Implementation plan.

V3/V4 INVARIANTS:

- Offline safety exists to reach humans, not continue AI chat.

- No phone numbers to AI.

- No automatic contact.

- User can clear local safety cache.

- User understands what is cached.

CACHE CONTENTS:

Allowed:

- saved sober contact names and phone numbers for local device use only

- saved meeting links

- 988/SAMHSA text and links

- local emergency note

- tell-on-myself template

- cache last updated timestamp

Forbidden:

- check-ins

- chat history

- raw notes

- transcripts

- memory summaries

- AI prompts

- event_log

- API keys/secrets

STORAGE:

Use localStorage unless existing app patterns prefer IndexedDB.

Keep storage key names clear, for example:

anchor_offline_safety_cache_v1

SETTINGS COPY:

Add copy near the setting:

“Anchor can store your saved recovery contacts and meeting links on this device so SOS resources still work if the internet is down. This does not cache your check-ins, chat history, or private notes.”

CONTROLS:

- Enable/refresh offline safety cache.

- Clear offline safety cache.

- Show last updated timestamp.

OFFLINE BEHAVIOR:

When network is offline:

- AI features should degrade gracefully.

- Show Offline Safety Card.

- Allow call/text links if device supports them.

- Show cached meeting links.

- Show tell-on-myself template.

- Do not attempt AI calls from Offline Safety Card.

TESTS:

Add or update tests for:

1. Cache includes allowed safety fields.

2. Cache excludes check-ins, chat, notes, transcripts, memory summaries.

3. Clear cache removes local data.

4. Offline card renders from cache.

5. No AI call occurs from offline card.

MANUAL QA:

- Enable cache.

- Turn network offline in browser tools.

- Open app and verify Offline Safety Card.

- Verify call/text/meeting links are visible.

- Clear cache and verify offline safety data disappears.

AT THE END:

Report: cache key, fields cached, forbidden fields excluded, offline behavior confirmed, tests run, manual QA results, known issues, and exact next step for Pattern Insight Engine. Keep under 300 words.

Prompt 9: V4.2 Pattern Insight Engine

# V4.2: PATTERN INSIGHT ENGINE

Upgrade the existing recovery check-in app with a deterministic Pattern Insight Engine only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

Use existing check-ins, commitments, trackers, and event_log data. Extend what exists.

Do not rebuild the Insights page or Home UI in this prompt unless needed for minimal verification.

IMPORTANT CONSTRAINTS:

- Do NOT add AI calls.

- Do NOT add new database tables or columns.

- Do NOT use vector DB, embeddings, CrewAI, AutoGen, or agent frameworks.

- Do NOT parse raw notes for this feature.

- Do NOT treat AI/system-generated event_log entries as user facts.

- Do NOT show more than one primary insight on Home in later UI prompts.

PRE-FLIGHT:

Inspect current implementation. Confirm in 7 bullets:

1. Existing check_ins data shape.

2. Existing commitments data shape.

3. Existing event_log data shape.

4. Whether event_log has actor/source/kind taxonomy.

5. Existing date/time helper patterns.

6. Existing Insights/Home helper patterns.

7. Implementation plan.

V3/V4 INVARIANTS:

- Pattern/stat logic is deterministic.

- getCurrentUserId() everywhere.

- No phone numbers in insight output.

- No raw notes or transcripts in insight output.

- AI-generated old insights are not evidence.

- Return null if data is insufficient.

GOAL:

Create a pure, typed helper that computes one PatternInsightResult.

REQUIRED TYPES:

Use or adapt these TypeScript shapes:

type PatternInsight = {

id: string;

type:

| "missed_checkin_drift"

| "rising_craving"

| "low_sleep_high_craving"

| "repeated_incomplete_commitments"

| "no_recent_contact";

severity: "low" | "medium" | "high";

title: string;

body: string;

why: string[];

suggestedAction: {

label: string;

action: "checkin" | "chat" | "sos" | "contact" | "meeting" | "commitment";

};

dataWindowDays: number;

};

type PatternInsightResult = {

insight: PatternInsight | null;

diagnostics: {

signalsChecked: string[];

insufficientDataReasons: string[];

};

};

HELPER:

Create or adapt:

getPatternInsight(userId: string): Promise<PatternInsightResult>

Prefer smaller pure helpers internally, for example:

- detectMissedCheckinDrift(input)

- detectRisingCraving(input)

- detectLowSleepHighCraving(input)

- detectRepeatedIncompleteCommitments(input)

- detectNoRecentContact(input)

PATTERN PRIORITY:

1. Missed check-in drift.

2. Rising craving trend.

3. Low sleep + high craving correlation.

4. Repeated incomplete commitments.

5. No recent sober contact if reliably tracked.

MINIMUM DATA RULES:

- Missed check-in drift: requires at least 3 check-ins in previous 7 days and then 2 missed expected check-ins.

- Rising craving: requires at least 3 recent check-ins with numeric craving values.

- Low sleep/high craving: requires at least 4 check-ins with both sleep and craving values.

- Repeated incomplete commitments: requires at least 2 incomplete/recently missed commitments.

- No recent contact: only if contact tracking exists and has reliable dates.

COPY RULES:

Tone must be calm, direct, and non-alarming.

Allowed examples:

- “Your pattern changed a little.”

- “This might be nothing, but it is worth checking in.”

- “Keep tonight simple.”

Forbidden examples:

- “Relapse risk detected.”

- “You are slipping.”

- “You are failing.”

- “Danger.”

WHY COPY:

The why array may include data-basis bullets like:

- “You checked in 5 of the previous 7 days, then missed 2 days.”

- “Your last 3 craving scores moved from 3 to 5 to 7.”

Do not include raw notes.

TESTS:

Add tests for:

1. No data returns insight null.

2. Insufficient data returns insight null with reasons.

3. Missed check-in drift returns correct insight.

4. Rising craving returns correct insight.

5. Low sleep/high craving returns correct insight.

6. Repeated incomplete commitments returns correct insight.

7. AI/system insight events are ignored as evidence.

8. Phone numbers and raw notes are not included in output.

AT THE END:

Report: helper files changed, data sources used, no AI confirmed, no schema changes confirmed, tests run, known issues, and exact next step for Pattern Insight Card UI. Keep under 300 words.

Prompt 10: V4.2B Pattern Insight Card UI

# V4.2B: PATTERN INSIGHT CARD UI

Upgrade the existing recovery check-in app with Pattern Insight Card UI only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The Pattern Insight Engine should already exist. Use it. Do not create another insight engine.

IMPORTANT CONSTRAINTS:

- Do NOT add AI calls.

- Do NOT add new database tables or columns.

- Do NOT compute duplicate pattern logic in the frontend if backend helper exists.

- Do NOT show raw notes, transcripts, phone numbers, or full event_log details.

- Do NOT show more than one primary insight on Home.

PRE-FLIGHT:

Inspect current implementation. Confirm in 6 bullets:

1. Existing Pattern Insight helper or endpoint.

2. Existing Home component structure.

3. Existing Insights page/component structure if any.

4. Existing API client/data loader patterns.

5. Existing card/design system patterns.

6. Implementation plan.

V3/V4 INVARIANTS:

- One primary insight on Home.

- Insight explains the signal without exposing raw private content.

- No scary/surveillance copy.

- Home must still render if insight fails.

GOAL:

Display one Pattern Insight Card on Home and optionally on Insights.

BACKEND/API:

If no endpoint exists, add:

GET /api/pattern-insight

Response: PatternInsightResult

Validation:

- Uses getCurrentUserId().

- Returns { insight: null, diagnostics } if no insight.

- On failure, returns safe JSON error or null behavior consistent with app patterns.

- Does not include raw notes or phone numbers.

FRONTEND:

Home placement:

- Below current/due commitment.

- Above lower stats/counters.

- If no insight, show nothing.

Card content:

- title

- body

- suggested action button

- “Why am I seeing this?” expandable section using why[] bullets

Suggested action routing:

- checkin -> Check-In screen

- chat -> Chat screen

- sos -> SOS Mode

- contact -> Handoff/contact surface

- meeting -> Meeting links if existing

- commitment -> Commitment section if existing

UX:

- Dark theme.

- 44px tap targets.

- Calm, compact card.

- Expand/collapse why section.

- Loading should not block Home.

- Error should silently omit card and log safe error.

TESTS:

Add or update tests for:

1. No insight means no card.

2. Insight renders title/body.

3. Why section expands/collapses.

4. Suggested action routes correctly.

5. Failed insight request does not crash Home.

6. No raw notes/phone numbers appear in rendered output.

MANUAL QA:

- User with no data sees no card.

- User with test trend sees one card.

- Why section works.

- Suggested action works.

- Mobile layout remains clean.

AT THE END:

Report: endpoint/view files changed, one-card behavior confirmed, why section confirmed, no AI/schema confirmed, tests run, manual QA results, known issues, and exact next step for Drift Detection. Keep under 300 words.

Prompt 11: V4.3 Drift Detection

# V4.3: DRIFT DETECTION

Upgrade the existing recovery check-in app with deterministic Drift Detection only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

Pattern Insight Engine should already exist. Extend it or add a closely related helper.

Do not create a second competing insight system.

IMPORTANT CONSTRAINTS:

- Do NOT add AI calls.

- Do NOT add new database tables or columns.

- Do NOT use alarmist language.

- Do NOT call this relapse prediction.

- Do NOT escalate to crisis unless explicit crisis signals are present through existing risk classifier flow.

- Do NOT treat AI/system-generated insights as user facts.

PRE-FLIGHT:

Inspect current implementation. Confirm in 6 bullets:

1. Existing Pattern Insight helper files.

2. Existing check-in frequency/date logic.

3. Existing commitment completion logic.

4. Existing contact tracking if any.

5. Existing Home insight display.

6. Implementation plan.

V3/V4 INVARIANTS:

- Drift detection is a gentle early-warning signal, not surveillance.

- No phone numbers in output.

- No raw notes in output.

- One primary Home insight.

- Deterministic logic only.

DRIFT SIGNALS:

Check these signals in this priority order:

1. 2+ missed check-ins after recent consistency.

2. Rising craving average over 3+ check-ins.

3. Falling sleep trend over 3+ check-ins if sleep is tracked.

4. Repeated incomplete commitments.

5. No recent human contact only if reliably tracked.

COPY RULES:

Allowed:

- “You went quiet. That can be nothing. It can also be drift. Do one small check-in now.”

- “Your pattern changed a little. Keep the next move small.”

- “This might be nothing, but it is worth checking in.”

Forbidden:

- “Relapse risk detected.”

- “You are slipping.”

- “Danger.”

- “You are failing.”

- “The app predicts relapse.”

OUTPUT:

Return a PatternInsight-compatible result so UI can reuse the same card.

Suggested action should usually be:

- Check In

- Text someone

- Open SOS

- Go to meeting

- Complete one small commitment

OPTIONAL EMAIL WORDING:

If email reminders are enabled and existing scheduler supports missed follow-up copy, provide optional safe copy but do not send emails in this prompt unless existing scheduler already does.

Email copy must be warm and non-alarming.

TESTS:

Add or update tests for:

1. Drift after missed check-ins returns calm insight.

2. No drift when user simply has no historical data.

3. Rising craving drift works.

4. Falling sleep drift works if data exists.

5. Repeated commitments drift works.

6. No AI/system-generated insight events are used as evidence.

7. Forbidden phrases do not appear.

MANUAL QA:

- Seed/mock recent consistent check-ins then missing days.

- Confirm one Home insight appears.

- Confirm copy is calm.

- Confirm suggested action works.

- Confirm no crisis escalation unless crisis flow is separately triggered.

AT THE END:

Report: drift signals implemented, pattern engine integration confirmed, no AI/schema confirmed, tests run, manual QA results, known issues, and exact next step for Data Export and Trust. Keep under 300 words.

Prompt 12: V4.4 Data Export and Trust

# V4.4: DATA EXPORT AND TRUST

Upgrade the existing recovery check-in app with data export and trust controls only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

Use existing check-ins, trackers, commitments, user_memory, stable_profile, and app_settings data.

Do not rebuild Settings.

IMPORTANT CONSTRAINTS:

- Do NOT include API keys, secrets, internal logs, or raw AI prompts.

- Do NOT include phone numbers in shareable export by default.

- Do NOT include raw transcripts unless explicitly part of full personal export and already stored.

- Do NOT add account deletion in this prompt unless already trivial and safe.

- Do NOT add new database schema.

- Do NOT send export content to AI.

PRE-FLIGHT:

Inspect current implementation. Confirm in 7 bullets:

1. Existing data tables/collections to export.

2. Existing Settings/Data UI location.

3. Existing backend route patterns.

4. Existing auth/user ID pattern.

5. Whether phone numbers are stored and where.

6. Existing file download/client patterns.

7. Implementation plan.

V3/V4 INVARIANTS:

- getCurrentUserId() everywhere.

- User owns their data.

- Export does not create privacy leaks.

- No phone numbers in shareable export by default.

- No AI calls.

EXPORT MODES:

1. Personal Full Export JSON

- Includes user-owned data.

- May include contacts only if the user explicitly chooses Include contacts.

- Clearly warn that it contains sensitive recovery information.

2. CSV Check-ins Export

- Rows of check-in structured fields.

- Exclude raw notes by default unless existing product clearly treats them as exportable and user opts in.

- No phone numbers.

3. Markdown Recovery Summary

- Shareable by default.

- Excludes phone numbers, raw notes, raw transcripts, full chat history, internal logs, and secrets.

- Includes high-level patterns, commitments, tracker summaries, and recent summary if safe.

SETTINGS UI:

Add Settings > Account/Data > Export Data.

Before export, show warning:

“This may include sensitive recovery information. Keep it somewhere private.”

Controls:

- Download full JSON export

- Download CSV check-ins

- Download Markdown recovery summary

- Checkbox: Include contact phone numbers in full JSON export only

- Checkbox should default false

BACKEND ENDPOINTS:

Use existing route conventions. Suggested:

GET /api/export/full-json?includeContacts=false

GET /api/export/check-ins.csv

GET /api/export/recovery-summary.md

RESPONSE HEADERS:

Set appropriate Content-Type and Content-Disposition for downloads.

TESTS:

Add or update tests for:

1. Full JSON export excludes contacts by default.

2. Full JSON export includes contacts only when includeContacts=true.

3. Shareable Markdown excludes phone numbers.

4. CSV excludes phone numbers and internal logs.

5. Export endpoints use getCurrentUserId().

6. Export does not call AI.

MANUAL QA:

- Download each export.

- Open files and inspect content.

- Confirm phone numbers excluded by default.

- Confirm include contacts works only for full JSON.

- Confirm warning copy appears.

AT THE END:

Report: endpoints added, UI added, formats supported, privacy defaults confirmed, tests run, manual QA results, known issues, and exact next step for Memory Search Lite. Keep under 300 words.

Prompt 13: V4.5 Memory Search Lite

# V4.5: MEMORY SEARCH LITE

Upgrade the existing recovery check-in app with Memory Search Lite only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

Use existing user_memory.event_log and stable_profile. Do not add vector DB, embeddings, or agent frameworks.

IMPORTANT CONSTRAINTS:

- Do NOT add embeddings.

- Do NOT add vector database.

- Do NOT add new database tables or columns.

- Do NOT treat AI/system-generated inferences as user facts.

- Do NOT surface old events unprompted in normal chat unless explicitly requested or safety-relevant.

- Do NOT search raw notes if they are not already safely summarized in event_log.

- Do NOT include phone numbers.

PRE-FLIGHT:

Inspect current implementation. Confirm in 7 bullets:

1. Existing event_log structure.

2. Whether actor/source/kind taxonomy exists.

3. Existing memory screen files.

4. Existing chat prompt memory injection helper.

5. Existing date/time formatting helpers.

6. Existing API route patterns.

7. Implementation plan.

V3/V4 INVARIANTS:

- Memory search retrieves compact event summaries, not raw private text.

- AI/system-generated insight events are labeled and not treated as user facts.

- Phone numbers never appear in search results.

- User remains in control of memory.

FEATURES:

1. Search event_log by keyword.

2. Filter by date range if easy.

3. Filter by event kind/type:

- check-in

- commitment

- tracker reset

- SOS/handoff

- chat session summary if present

4. Add backend helper:

getRelevantPastEvents(query: string, limit: number): Promise<EventLogEntry[]>

5. Optional UI in Memory screen: search box and filters.

SCORING:

Use simple deterministic scoring:

- exact keyword match in summary

- kind/source match

- recency boost

- actor=user boost

Do not use AI.

CHAT INTEGRATION:

Only use Memory Search Lite in chat when user asks things like:

- “When has this happened before?”

- “What helped last time?”

- “Do I have a pattern with this?”

- “Have I felt this before?”

Do not automatically inject old events into every normal chat.

RESULT DISPLAY:

- Show date/time.

- Show kind/source label.

- Show compact summary.

- Do not show phone numbers.

- Do not show raw notes.

TESTS:

Add or update tests for:

1. Keyword search returns matching user events.

2. AI/system inference events are excluded or clearly labeled based on filter.

3. Phone numbers are redacted/excluded.

4. Limit is respected.

5. Empty query returns safe empty or recent events depending on UI decision.

6. Chat integration only triggers on explicit memory-search intent.

MANUAL QA:

- Search a known event.

- Filter by commitment.

- Filter by tracker reset.

- Ask chat “when has this happened before?” and verify relevant event summaries appear.

- Ask normal chat message and verify old events are not over-injected.

AT THE END:

Report: helper/UI files changed, no embeddings/vector DB confirmed, retrieval rules confirmed, tests run, manual QA results, known issues, and exact next step for Relapse Response Protocol. Keep under 300 words.

Prompt 14: V4.6 Relapse Response Protocol

# V4.6: RELAPSE RESPONSE PROTOCOL

Upgrade the existing recovery check-in app with a structured relapse response protocol only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has check-ins, sobriety tracking, crisis routing, commitments, SOS/handoff, and event_log.

Extend existing flows. Do not rebuild.

IMPORTANT CONSTRAINTS:

- Do NOT use shame language.

- Do NOT hide sobriety reset reality.

- Do NOT automatically reset sobriety tracker without user confirmation.

- Do NOT automatically contact anyone.

- Do NOT continue normal AI conversation if crisis signals are present.

- Do NOT add new database tables unless absolutely necessary.

- Do NOT send phone numbers to AI.

PRE-FLIGHT:

Inspect current implementation. Confirm in 8 bullets:

1. Existing sober today / tracker reset logic.

2. Existing check-in flow for not sober today.

3. Existing crisis classifier/routing.

4. Existing SOS/handoff components.

5. Existing commitment creation flow.

6. Existing event_log helper.

7. Existing next check-in/reminder logic.

8. Implementation plan.

V3/V4 INVARIANTS:

- Truth without shame.

- Safety first.

- Human contact visible.

- User confirms tracker reset.

- Crisis signals route to crisis card.

- No automatic contact.

TRIGGER:

If user reports not sober today or indicates relapse/reset in existing structured check-in.

FLOW:

1. Acknowledge without shame.

2. Ask immediate safety question or run existing risk classifier if free text exists.

3. If crisis: show crisis card and stop normal flow.

4. Offer human contact shortcuts through SOS/handoff.

5. Ask what happened in plain language if appropriate.

6. Offer one cleanup action.

7. Offer tracker reset confirmation if applicable.

8. Save compact event_log summary.

9. Suggest next check-in time.

APPROVED COPY BANK:

Use or adapt:

- “I’m glad you told the truth. This is not the moment for shame.”

- “First we make sure you are safe. Then we take one repair step.”

- “This does not erase the work you have done. It does mean today needs honesty and support.”

- “Do you want to reset the tracker now, or decide after you contact someone?”

- “One repair step is enough for this moment.”

FORBIDDEN COPY:

- “You failed.”

- “You lost everything.”

- “Start over from zero.”

- “You ruined your progress.”

- “Relapse risk detected.”

CLEANUP ACTION OPTIONS:

Show one or a small list:

- Drink water and eat something simple.

- Remove alcohol/drugs from immediate reach if relevant and safe.

- Text a saved sober contact.

- Open a meeting link.

- Set a next check-in for later today.

- Write one honest sentence about what happened.

TRACKER RESET:

- Explain clearly what reset means.

- Require user confirmation.

- Do not reset automatically.

- Log compact event after confirmation.

EVENT LOG:

Save only compact summary.

Do not store raw confession text unless existing product already does and user expects it.

Example:

actor: "user"

source: "tracker"

kind: "tracker_reset"

summary: "User reported not sober today and opened relapse response protocol."

TESTS:

Add or update tests for:

1. Not sober triggers protocol.

2. Crisis language routes to crisis card.

3. Tracker does not reset without confirmation.

4. Human handoff visible.

5. Forbidden shame phrases do not appear.

6. No automatic contact occurs.

7. Event log summary is compact and contains no phone numbers.

MANUAL QA:

- Report not sober without crisis language.

- Report not sober with crisis language.

- Confirm tracker reset flow.

- Cancel tracker reset.

- Open SOS from protocol.

- Verify copy tone.

AT THE END:

Report: protocol surfaces changed, crisis routing confirmed, tracker reset confirmation confirmed, no shame copy confirmed, tests run, manual QA results, known issues, and exact next step for Habit Architecture. Keep under 300 words.

Prompt 15: V4.7 Habit Architecture: Evening Reflection and Micro Check-ins

# V4.7: HABIT ARCHITECTURE - EVENING REFLECTION AND MICRO CHECK-INS

Upgrade the existing recovery check-in app with optional low-friction habit inputs only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has full check-ins, commitments, trackers, and event_log.

This feature is optional habit support, not a replacement for the full check-in.

IMPORTANT CONSTRAINTS:

- Do NOT add push notifications in this prompt.

- Do NOT add AI responses to micro check-ins.

- Do NOT make micro check-ins compete with the main daily check-in.

- Do NOT add new database schema without proposing it first in the final report if existing schema cannot safely support it.

- Do NOT send micro check-in text to AI.

- Do NOT gamify with shame or streak pressure.

PRE-FLIGHT:

Inspect current implementation. Confirm in 8 bullets:

1. Existing check_ins schema.

2. Whether check_ins can safely support type = full | micro | evening.

3. Existing event_log helper.

4. Existing Home quick action structure.

5. Existing Insights/history display.

6. Existing date/time helper patterns.

7. Whether schema change is needed.

8. Implementation plan.

V3/V4 INVARIANTS:

- Main check-in remains primary.

- Micro check-in is optional.

- No AI response.

- No raw content sent to AI.

- No shame/gamification pressure.

MICRO CHECK-IN FIELDS:

- mood rating or simple mood selector

- craving rating

- one word optional

- sober today optional if safe with existing tracker logic

EVENING REFLECTION FIELDS:

- one win today

- one thing to do differently tomorrow

DATA STRATEGY:

Preferred:

- Use existing check_ins table with type field if already present.

- If no type field exists but event_log can safely store compact summaries, use event_log for first version.

- If neither is suitable, do not implement schema change automatically. Instead report proposed minimal schema.

UI:

- Keep small and optional.

- Place lower than primary check-in action.

- Make it clear this is not the full check-in.

- No AI loading states.

- Save quickly.

EVENT LOG:

If using event_log, store compact summaries only.

Examples:

- “User completed micro check-in: mood 6, craving 3.”

- “User completed evening reflection.”

Do not store long raw reflection text in event_log unless already expected.

TESTS:

Add or update tests for:

1. Micro check-in saves without AI call.

2. Evening reflection saves without AI call.

3. Main daily check-in still works.

4. History/Insights do not confuse micro with full check-in.

5. No phone numbers/raw private text are sent to AI.

MANUAL QA:

- Complete full check-in.

- Complete micro check-in.

- Complete evening reflection.

- Verify no AI response appears.

- Verify saved state/history behavior.

- Verify mobile layout.

AT THE END:

Report: whether schema change was avoided, files changed, no AI confirmed, tests run, manual QA results, known issues, and exact next step. Keep under 300 words.

Prompt 16: Future Design Note: Realtime Voice Call Mode

# FUTURE DESIGN NOTE ONLY: REALTIME VOICE CALL MODE

Do not implement realtime voice. Create a technical design note only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has chat, TTS, voice input/transcription, crisis routing, and human handoff.

IMPORTANT CONSTRAINTS:

- Do NOT add packages.

- Do NOT add endpoints.

- Do NOT change UI.

- Do NOT call OpenAI Realtime.

- Do NOT implement WebRTC.

- Create a markdown or doc note only if the project has a docs folder. Otherwise output the note in final response.

DESIGN NOTE MUST COVER:

1. Possible OpenAI Realtime/WebRTC architecture.

2. Session time limit.

3. Cost risks.

4. Mobile Safari risks.

5. Privacy risks.

6. Always-visible human handoff.

7. Crisis cutoff behavior.

8. No endless soothing loop rule.

9. Summary saved after call.

10. No auto-call or auto-text.

11. When this feature becomes justified by usage.

12. Why this is deferred for now.

AT THE END:

Report where the design note was placed and confirm no implementation changes were made. Keep under 200 words.

Prompt 17: Future Design Note: Wearables and Health Integration

# FUTURE DESIGN NOTE ONLY: WEARABLES / HEALTH INTEGRATION

Do not implement wearables or health integration. Create a technical design note only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has check-ins, pattern insights, drift detection, and recovery data.

IMPORTANT CONSTRAINTS:

- Do NOT add Apple Health, Oura, Whoop, Google Fit, or wearable APIs.

- Do NOT add packages.

- Do NOT add database tables.

- Do NOT change UI.

- Do NOT make medical claims.

- Create a markdown or doc note only if the project has a docs folder. Otherwise output the note in final response.

DESIGN NOTE MUST COVER:

1. Sleep.

2. HRV.

3. Resting heart rate.

4. Steps/activity.

5. Permission model.

6. Privacy language.

7. No medical claims.

8. How biometric signals might influence pattern insights.

9. Fallback when no wearable data exists.

10. User ability to disconnect/delete imported data.

11. Why this is deferred for now.

AT THE END:

Report where the design note was placed and confirm no implementation changes were made. Keep under 200 words.

26. Final Recommended Build Order

V3.7A Safety and Runtime Stabilization.

V3.7B Backend Invariant Test Suite.

V3.7C Scheduler Hardening.

V3.7D System Health Debug View.

V3.7E Pending Commitment Card.

V4.0 Home Command Center.

V4.1 SOS Mode.

V4.1B Offline Safety Cache.

V4.2 Pattern Insight Engine.

V4.2B Pattern Insight Card UI.

V4.3 Drift Detection.

V4.4 Data Export and Trust.

V4.5 Memory Search Lite.

V4.6 Relapse Response Protocol.

V4.7 Habit Architecture only if needed.

Future design notes only: realtime voice and wearables.

Only after real usage: vector RAG, agent frameworks, health integrations, realtime voice implementation.

27. Closing Note

Anchor V4 should not be bigger for the sake of being bigger. It should be clearer, safer, more trustworthy, and more able to catch drift before the user falls fully into it. The strongest next move is not a grand AI architecture rewrite. It is a disciplined product intelligence layer built on top of the working V3 foundation.

The product philosophy is sound: AI-assisted self-governance, recovery action loops, human handoff, pattern awareness, privacy-preserving memory, and practical wisdom. The execution discipline is now the key. Build in small passes. Test invariants. Keep the user in control. Make the next right action obvious.
