---
title: "5 11 2026 Next Features Master Doc"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/5-11-2026 Next Features Master Doc.docx"
status: active
privacy: working
tags:
  - product
---

# 5 11 2026 Next Features Master Doc

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
5-11-2026 Next Features Master Doc

Status snapshot

V3.7 baseline shipped and exceeded. M-series UX work (M1 through M5j) shipped. Production deployment, CD pipeline, multi-user auth, email, real domain all live. M5c fragment bundling fix landed at PR #45 and is verified in production. AUTONOMY_LAYER v1.2 lands at PR #46.

What is NOT yet built from the V4 / V4.1 / V5 specs is most of the actual feature roadmap. This doc lays out the next eight tiers in order with rationale, build approach, and what can run in parallel under the autonomy system.

The operating constraint: low supervision. Marcus designs specs in chat conversations with Charlie, runs them through META_PROMPT, fires directives at CC Cloud (or CC Local where credentials matter), agents open PRs autonomously, Marcus reviews and merges. Auto-merge is on for mechanical PRs where CI gates exist.

TIER 1 — Mechanical follow-ups (batch parallel, fire now)

Four small directives. All low-risk, all autonomous, all can run as parallel CC Cloud sessions. No spec conversation needed because the work is mechanical.

Job 1.1 — META_PROMPT v1.2 add to docs/ Adds the directive-generation prompt to docs/META_PROMPT.md. Pairs with the v1.2 AUTONOMY_LAYER on main. Pure docs PR. Auto-merge eligible once Playwright CI status checks are required.

Job 1.2 — Tracker display name fix Follow-up from PR #42. The social_media tracker still stores and renders the raw slug in trackers list, history, and other render sites. Add a formatTrackerLabel helper and apply at all render sites. Stored values stay as slugs; only display changes. Frontend-only.

Job 1.3 — B6 retry-with-backoff on loadUserMemory Parked from the May 10 handoff. Neon free tier auto-pauses; the first request after idle can return 500 because loadUserMemory throws. Add retry with exponential backoff for transient Neon 5xx. Backend-only. ANCHOR-2 self-repair entry already documents the pattern.

Job 1.4 — Stale HALT comment removal The May 10 diagnostic surfaced a stale comment in composeSystemPrompt.ts that says "HALT: This module is drafted and unit-tested but NOT wired into any active production path." It IS wired. Remove the comment. One-line PR.

Parallel agent split for Tier 1: all four can run as separate CC Cloud sessions simultaneously. No coordination needed. Each opens its own PR. Marcus reviews and merges in any order.

Auto-merge eligibility per directive depends on whether Playwright CI is required by branch protection. If yes, Jobs 1.1, 1.2, 1.4 are auto-merge yes. Job 1.3 touches backend behavior and warrants Marcus's review even though it's mechanical.

TIER 2 — V5.0 SOS Mode

Why this position: The V5 spec itself states "V5.0 is the one phase that should ship regardless of any other consideration. SOS Mode and Offline Safety Cache materially improve user safety without depending on AI inference, network availability, or any V4 surface." Zero V4 dependency. Highest standalone safety value. Architecturally simple.

What it is:

SOS button reachable from every major surface (Home, Check-In, Chat, Settings)

SOS screen with: persistent route to call or text saved contacts, prefilled tell-on-myself message, 988 and SAMHSA crisis card, tiny grounding fallback at top, open meeting link

No AI inside SOS Mode

Offline Safety Cache via localStorage or IndexedDB: cached sober contacts, meeting links, crisis info, tell-on-myself template

Logs sos_opened event to event_log

Dependencies: None. Reads from existing stable_profile.sober_contacts and stable_profile.meeting_links.

Spec design conversation needed before directive generation. Topics:

Exact placement and label for SOS button on each surface

Full copy for SOS screen header and subtext ("Need a person or immediate support?" placeholder per V5 spec)

Exact tell-on-myself prefilled message text

Crisis card content for 988, SAMHSA, and a fallback for non-US users

Tiny grounding fallback text ("Put both feet on the floor. Take one breath. Then tap one person." per V5 spec)

Offline cache refresh frequency and staleness banner copy

Settings entry for "Clear safety cache"

Build approach:

Single directive, four phases.

Phase A: schema additions (event_log gains sos_opened type, no new tables, localStorage keys defined) Phase B: SOS route, SOS page component, all buttons across surfaces Phase C: Offline Safety Cache implementation, refresh logic, staleness banner Phase D: BUILD_REPORT and PR

Council of Models: yes for the crisis card copy and tell-on-myself template. These are safety-adjacent. Required Council review before merge.

Auto-merge: no. Safety-adjacent UI changes warrant manual review even with CI passing.

Agent: CC Cloud for code (no production credentials needed). CC Local optional for any localStorage testing that needs a real browser.

Parallel split: not needed for a single feature. Sequential phases work.

TIER 3 — V4 Extend (extend, do not replace)

Why this position: Unlocks V4.1 Practice Mode and V5.1 Pattern Insight. The actual V4 spec calls for a full buildChatSystemPrompt six-section assembler, but the agreed strategy is to EXTEND the existing composeSystemPrompt (which now works post-M5c) with the missing pieces rather than replace it. Smaller scope, faster ship, same functional outcome.

What it is:

New stable_profile.experience_level field: first_attempt | returning | long_term_stable | chronic_relapse | unspecified

Decision: store stable_profile.recovery_method field or derive from existing user_programs? Derive is recommended; user_programs already has primary program with category, which maps to method.

Onboarding step for experience_level (becomes step 6 or similar, depending on current flow)

Settings UI for editing experience_level

Existing-user migration modal: one-screen prompt on first open after deploy ("Two quick questions Anchor uses to talk to you better")

Four new prompt fragment files for experience_level voice differentiation:

first-attempt.txt

returning.txt

long-term-stable.txt

chronic-relapse.txt

Milestone helpers in a new lib/recoveryProfile.ts:

getDayCount(focus, profile)

getApproachingMilestone(profile) — 5-day window

getRecentlyCrossedMilestone(profile) — 24-hour window

Milestone list: 3, 7, 14, 30, 60, 90, 180, 365, then yearly

Extend composeSystemPrompt to consume experience_level and milestone state. Add a time-aware framing section to assembled prompts when milestone is approaching or recently crossed.

Expose drift_signal parameter (default false, not yet wired — V5.1 will wire it)

Dependencies:

M5c fragment bundling fix (done, PR #45 merged)

AUTONOMY_LAYER v1.2 (PR #46 pending merge)

Spec design conversation needed before directive generation. Topics:

Full content of each of the four experience_level fragments (verbatim, in Marcus's voice)

Onboarding step copy: "How would you describe where you are with this?" plus each option's label and brief non-judgmental subtext

Migration modal copy: header, body, button labels, skip behavior

Time-aware framing template per case: approaching milestone, recently crossed milestone (with focus parameterization)

Settings UI placement and labels

Decision: derive recovery_method from user_programs or store explicitly? Trade-offs of each.

Default value behavior for existing users (unspecified by default, modal prompts once)

Build approach:

Single directive, six phases, multiple parallel-agent opportunities.

Phase A: schema additions to stable_profile JSON, normalizeStableProfile handles new field with default, migration for existing users sets experience_level to 'unspecified' Phase B: milestone helpers (getDayCount, getApproachingMilestone, getRecentlyCrossedMilestone), unit tests Phase C: four experience_level fragments dropped into src/lib/prompts/fragments/, smoke test that each loads and contains the expected vocabulary Phase D: extend composeSystemPrompt to consume experience_level fragment + milestone state, add time-aware framing section Phase E: onboarding step for experience_level, existing-user migration modal, settings UI Phase F: BUILD_REPORT and PR

Council of Models: yes for the four experience_level fragments and time-aware framing template. Voice differentiation across experience levels is high-stakes — chronic relapse user must not get false-hope language, first-attempt must not get jargon. Council validates voice quality across all four cases.

Auto-merge: no. Prompt content changes always warrant manual review.

Agent split:

CC Cloud 1 handles Phases A, B (schema and helpers — pure logic, no design conversation needed beyond what's in the spec)

CC Cloud 2 handles Phase C (fragment files, content from spec)

CC Cloud 3 handles Phase E (frontend changes)

CC Local handles Phase D (extending composeSystemPrompt, integration testing)

Final assembly into one PR or three coordinated PRs depending on how cleanly the work splits

Recommendation: one PR per phase if the changes are independent. Phase D depends on A and C. Phase E depends on A. So natural order is A → B → C → D → E, with C running parallel to A+B if Marcus pre-writes the fragment content.

TIER 4 — V5.3 Relapse Response Protocol

Why this position: Pairs naturally with V4 Extend because the chronic-relapse experience_level voice matters most in relapse moments. Partially shipped already via the sober reset flow (PR #32) — the rest of the protocol fills in the cleanup actions, sponsor template offer, "what happened" prompt, and approved/forbidden copy enforcement at the prompt template level.

What it is:

Triggered when user reports not sober today, opens "I already slipped" via Practice (when V4.1 exists), or via a Home affordance

Acknowledge without shame

Run existing risk classifier on any free text — crisis path if elevated

Offer human contact shortcuts via SOS (Tier 2)

Ask what happened in plain language (free text or skip)

Offer one cleanup action: drink water, eat, remove substances if relevant and safe, text sober contact, open meeting link, set next check-in for later today, write one honest sentence

Tracker reset confirmation — never auto-reset

Save compact event_log entry: relapse_response_completed. No raw confession text stored.

Suggest next check-in time

Sponsor message drafting templates: pre-written for common moments ("I had a slip last night and want to talk", "craving help", "resentment", "gratitude", "update")

Approved copy bank loaded as positive constraint in composed prompt

Forbidden copy enforced at prompt template level: "You failed.", "You lost everything.", "Start over from zero.", "You ruined your progress.", "Relapse risk detected."

Dependencies:

V5.0 SOS Mode (for handoff shortcuts)

V4 Extend (chronic-relapse experience_level voice)

Spec design conversation needed. Topics:

Full approved copy bank (verbatim, six to ten lines)

Full forbidden copy list (verbatim, plus expansion of obvious variants)

Each sponsor message template (verbatim, with placeholders)

Tracker reset confirmation copy

Trigger logic: where in the app does the protocol start? Home affordance, Sober Today flow, manual entry from menu, post-classifier?

Build approach:

Single directive. Sequential phases. Council of Models REQUIRED for the approved-copy and forbidden-copy banks — these are safety-adjacent at the highest level.

Auto-merge: no.

Agent: CC Cloud for code, CC Local for the Council of Models review coordination (running identical prompt across Claude, GPT, Gemini, Grok and surfacing the convergence/divergence for Marcus).

TIER 5 — V4.1 Practice Mode

Why this position: Requires V4 Extend stable. The branch tree state machine, six modules, and practice surface variant of composeSystemPrompt are non-trivial but well-specified in the V4.1 doc. Most of the work is module authoring (writing the scenario branch trees and the voice exemplars), not engineering.

What it is:

Branch tree JSON schema, deterministic state machine, dialogue generator that wraps composeSystemPrompt with module context

New practice surface variant of composeSystemPrompt

Six modules: Lapse vs Relapse, The 20-Minute Urge, Ask for Help Without a Speech, Declining the Offer, What to Do After a Slip, Holding a No When Asked

Need-state entry on Home (six need-states)

Library screen filtered by user's recovery_focus

Module session UI with streaming, choices, pause/resume, "this doesn't fit my situation" affordance, repair loops, three-path completion (commitment, tiny next action, save without committing), immediate post-module rating

New tables: practice_progress, practice_choices, practice_scenario_feedback

event_log gains practice_module_completed and practice_module_rated_immediate types

Acute-distress detection at Practice surface entry (60-second stabilization or routing to SOS)

Per-focus sensitive data controls in Settings

Dependencies:

V4 Extend (practice surface needs experience_level voice differentiation built in)

V5.0 SOS Mode (Practice routes to SOS on acute distress)

Spec design conversation needed. Substantial topics:

Full content of each of the six modules (hook node, concept node, practice nodes with choices and repair loops, synthesis, outcome paths)

Voice exemplar set (authored short samples for each module's voice)

Contraindication checks per module (block, warn, route based on user state)

UI copy for need-state entry, library, module session screen

Schema for the three new tables

This is the largest feature work item in the queue. V4.1 spec estimates 4-6 weeks of solo work, mostly module authoring. Could be split into "ship the engine with one module" first, then add modules incrementally.

Build approach:

Multi-directive. Engine first, then one module end-to-end, then remaining modules in parallel.

Council of Models: yes for each module's content (voice eval across at least four focuses), and for the contraindication logic.

Auto-merge: no for any prompt or content changes.

Agent split: maximum parallelism. Engine on CC Local, each module authored as a separate CC Cloud branch with its own JSON file, then merged. The "this doesn't fit my situation" affordance and feedback collection can run as a parallel CC Cloud directive.

TIER 6 — V5.1 Pattern Insight + Drift Detection

Why this position: Wires V4 Extend's drift_signal hook. Adds one deterministic insight on Home with a clear "why am I seeing this?" affordance. No AI is used to compute signals; AI only phrases the surface via composeSystemPrompt.

What it is:

Pattern Insight Engine — one deterministic engine producing ranked signals from check-ins, commitments, user_memory

Eight signals: missed_checkin_drift, rising_craving, low_sleep_high_craving, repeated_incomplete_commitments, no_recent_contact, time_of_day_risk, anniversary_seasonal, approaching_milestone

Pattern Insight Card on Home — one card max, dismissible (24-hour suppression)

New pattern_insight surface variant of composeSystemPrompt

"Why am I seeing this?" expandable affordance citing computed signals, never raw notes

Drift Detection wires the engine's drift signal into V4's drift_signal hook → composed prompt picks up grounded-tone instruction

event_log gains pattern_insight_generated and pattern_insight_dismissed

Dependencies: V4 Extend with drift_signal hook exposed.

Spec design conversation needed. Smaller than V4.1, but signal thresholds and copy require Marcus's voice and judgment.

Build approach:

Single directive. The engine is the load-bearing piece. The card is straightforward UI.

Council of Models: yes for the eight signal copy strings (allowed and forbidden phrasings per signal type).

TIER 7 — V5.2 Data Export + Memory Search Lite

Why this position: Trust and ownership feature. Lower urgency than safety and personalization, but required for user data sovereignty.

What it is:

Three export formats: JSON (machine-readable), CSV (per-table zipped), Markdown (narrative recovery record)

Phone numbers excluded by default; opt-in inclusion

Memory Search Lite — search event_log by keyword and filter by date/kind, used to power chat queries like "when has this happened before?"

Memory search invoked only on memory-shaped queries (keyword/intent detection, not AI inference)

event_log gains export_generated

Dependencies: None hard. Can ship anytime after V4 Extend.

Spec design conversation needed but lighter — the export format decisions are mostly mechanical.

TIER 8 — V5.4 Polish basket

Why this position: Optional, opportunistic, pick based on user signal after V5.0 through V5.3 ship.

Includes: event taxonomy expansion (optional actor / source / kind fields), milestone intelligence (one-time card on milestone day with computed sentence about what the user did), step work integration, emotion wheel check-in, resentment tracker, gratitude bank, trigger mapping heatmap, weekly summary upgrade to pattern narrative.

Each is its own small feature. Pick based on production demand.

Build sequence recommendation

NOW (Tier 1, parallel):

Job 1.1 META_PROMPT v1.2 add

Job 1.2 Tracker display name fix

Job 1.3 B6 retry-with-backoff

Job 1.4 HALT comment cleanup

NEXT (Tier 2):

V5.0 SOS Mode

THEN (Tier 3):

V4 Extend

THEN (Tier 4, pairs with V4 Extend voice):

V5.3 Relapse Response Protocol

THEN (Tier 5):

V4.1 Practice Mode (engine first, then modules in parallel)

THEN (Tier 6):

V5.1 Pattern Insight + Drift Detection

WHEN USEFUL (Tier 7):

V5.2 Data Export + Memory Search Lite

OPPORTUNISTIC (Tier 8):

V5.4 Polish basket

Operating principles for low supervision

Batch parallel where possible. Tier 1 is the obvious case (four parallel CC Cloud sessions). Tier 3 V4 Extend splits across three or four parallel agents on different phases. Tier 5 V4.1 modules each get their own branch.

Spec design first, then directive. No directive ships without verbatim content for fragments, copy, and migration mappings (AUTONOMY_LAYER section 1.6 hard rule). Spec sessions happen in chat with Charlie. They are not coding work.

Council of Models is required for:

Any new prompt fragment or surface variant

Any safety-adjacent copy (crisis routing, relapse response, forbidden-copy lists)

Voice differentiation copy (the four experience_level fragments)

Sponsor message templates

Council is NOT required for:

Mechanical fixes (Tier 1)

Schema-only changes

Helper functions and computed signals

UI layout without copy changes

Auto-merge eligibility:

Tier 1: most are eligible once CI gate is required by branch protection

Tier 2 SOS Mode: no (safety-adjacent UI)

Tier 3 V4 Extend: no (prompt content)

Tier 4 V5.3: no (safety-adjacent prompt content)

Tier 5 V4.1: no per module

Tier 6 V5.1: signals and copy decisions warrant review

Tier 7-8: mixed, evaluate per PR

Working files survive across directives. ISSUE_EXECUTION_PLAN.md, AUTONOMOUS_RUN_LOG.md, BLOCKERS_FOR_MARCUS.md at repo root are the audit trail. Each directive appends.

MCP write safety (section 1.12) and spec-reality reconciliation (section 1.13) apply to every directive. The M5c run validated both.

Decision asked of Marcus

Fire Tier 1 now? Four parallel CC Cloud sessions, four small PRs.

After Tier 1 lands, start the V5.0 SOS Mode spec conversation in chat?

If yes to both: Tier 1 prompts already drafted from earlier in this session — Jobs 1.1, 1.2 ready to fire, Jobs 1.3 and 1.4 need short directive drafts. Spec session for V5.0 picks up whenever Marcus is ready.

End of 5-11-2026 Next Features Master Doc
