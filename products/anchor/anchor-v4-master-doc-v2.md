---
title: "Anchor V4 Master Doc v2"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Anchor V4/Anchor V4 Master Doc v2.docx"
status: active
privacy: working
tags:
  - product
---

# Anchor V4 Master Doc v2

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ANCHOR V4 MASTER DOC v2

Post V3.7 Stabilization, Field Test, and Production Path

Working draft. April 25, 2026.

Maxwell / Eagle Rocket LLC

Preamble

This is v2 of the Anchor V4 Master Doc, rewritten on April 25 2026 to reflect ground truth after a multi week sprint. The original V4 master doc was forward looking and proposed a stabilization queue (V3.7A through V3.7E) that has now been substantially completed under different names, with different scope, and in a different order. This document replaces it.

Ground truth: V3 is feature complete. V3.7 is shipped. The app currently has 111 passing Playwright smoke tests, two new WCAG AA compliant themes, structured recovery program selection with 39 official meeting resource URLs, inline memory editing, a Stoic and DBT oriented chat coach with mode detection, deterministic recent patterns generation, hardened email scheduler infrastructure, and a clean separation between user generated facts and AI generated inference.

What V4 will be: a deliberate slowdown. The next phase is not more features. The next phase is production. The next phase is multi user. The next phase is real users. V4 features as originally scoped (Pattern Insight Engine, SOS Mode, Drift Detection, Data Export, Memory Search Lite, Relapse Response Protocol) are deferred until production usage proves which of them are actually needed.

Doctrine: ship V3 to production. Port to mobile. Then decide what V4 means based on real signal, not speculation.

Table of Contents

1. Executive Summary

2. What Changed Since V4 Master Doc v1

3. Current Ground Truth: V3.7 Shipped State

4. Test Suite Inventory

5. Architecture and Stack As Built

6. Product Invariants (Updated)

7. Known Issues and Deferred Items

8. Recovery Program System (New Architecture)

9. Theme System (New Architecture)

10. Memory System Current State

11. Chat System Current State

12. The V4 Pivot: Production Before Features

13. V4 Phase 1: Production Deployment

14. V4 Phase 2: Mobile Port via Expo

15. V4 Phase 3: Real Usage and Signal Gathering

16. V4 Phase 4: Reassessed Feature Roadmap

17. Deferred Features from V4 v1

18. Permanent Non Goals

19. Closing Note

1. Executive Summary

Anchor V3 is a working recovery companion app. It includes persistent layered memory, a sponsor adjacent chat coach, structured check ins, commitments, voice input, TTS, email outreach scheduling, multi step crisis routing, human handoff, and a now structured recovery program selection system that maps to 39 official meeting resource URLs.

V3.7 stabilization wrapped on April 25 2026. Test 26 fixed. V3F2 post and V3F4 cleanup verified. Chat Mode Detection (V3F5) shipped. Bug Fix A and B shipped (binary field default state, commitments week count, recovery habits aggregation, multi check in algorithm, Recent Patterns markdown render, email diagnostic endpoint). UX Features A and B shipped (memory inline editing, recovery program expansion, find a meeting routing, structured meeting links, trackers home scroll fix, full theme contrast audit, two new themes, Recent Patterns 3 bullet structured format).

The original V4 plan called for an extensive feature build: SOS Mode, Pattern Insight Engine, Drift Detection, Memory Search Lite, Data Export, Relapse Response Protocol, and habit architecture. Most of these are good ideas but none of them solve the actual current bottleneck, which is that Anchor is a single user PWA running on a Replit dev URL with no production deployment, no real auth, no real domain, and no real users.

The V4 doctrine is therefore inverted from v1: do not build more features. Ship what exists. Get real users. Listen. Then decide which V4 features actually matter.

2. What Changed Since V4 Master Doc v1

Already Shipped (was treated as future work in v1)

Chat voice auto submit alignment (Test 26 fix) — done.

Pending commitment card on Home — already exists from V3C.

Phone number AI prompt audit — done as a V3 invariant.

Backend invariant tests — partially done in the smoke suite (111 tests).

Email feature flag (EMAIL_OUTREACH_ENABLED) — done.

Email diagnostic endpoint — done in Bug Fix B.

Chat Mode Detection (Reflect, Plan, Pattern, Handoff, Commitment) — V3F5, shipped, not in v1 doc.

Coach context handoff via sessionStorage on Chat with my coach button — V3F4, shipped, not in v1 doc.

Full summary TTS placement below header above card — V3F4, shipped, not in v1 doc.

History detail TTS — V3F4, shipped, not in v1 doc.

New since v1 (was not in v1 doc at all)

Recovery program system: 12 primary categories, 39 official meeting resource URLs, multi select sub program structure, structured stable_profile shape with non destructive migration.

Find a meeting routing: program aware, multi program picker, fallback to aa-intergroup.org.

Inline editing across the entire memory screen: recovery focus, recovery program, support style, sobriety why, sober contacts (CRUD), meeting links (CRUD with structured 5 field shape: label, day_of_week, time, timezone, url), email, reminder time, timezone.

Two new themes: Paper (warm light, off white background, sepia accents) and Midnight (cool deep dark, near black background, indigo accents). Both WCAG AA compliant.

Full WCAG AA contrast audit of all 4 existing themes. Border tokens fixed across anchor-dark, high-contrast-dark, and others. High-contrast-dark destructive token raised to AA.

theme_preference field added to stable_profile.

Recent Patterns rewritten as deterministic 3 bullet structured AI output: top_triggers, mood_trend, pattern_to_notice. Plain prose, banned phrase list, no contact name invention, JSON parsed server side, fallback message on parse failure or insufficient data.

Trackers home page scroll bar fix.

Multi check in algorithm: last value wins for binary fields, average for numeric (mood, craving, sleep, energy, focus).

Treated as V3.7 in v1 but actually superseded

V3.7A Safety and Runtime Stabilization — replaced by Bug Fix A scope (binary field defaults, commitments week count, Recovery Habits aggregation, multi check in algorithm).

V3.7B Backend Invariant Test Suite — partially absorbed into the running 111 test smoke suite. A separate dedicated unit test suite for helpers was not built.

V3.7C Scheduler Hardening — partially done; EMAIL_OUTREACH_ENABLED gate is in place, last sent timestamps are tracked, structured logging is not. Diagnostic endpoint added in Bug Fix B.

V3.7D System Health Debug View — not built. /api/email-status endpoint serves a partial version. A full debug view is deferred.

V3.7E Pending Commitment Card — already shipped in V3C.

3. Current Ground Truth: V3.7 Shipped State

Test Suite

111 Playwright smoke tests, all passing. Tests are organized by feature phase: V3A through V3F5 (existing), Bug Fix A (Tests 88 to 91), Bug Fix B (Tests 92 to 94), UX Features A (Tests 95 to 104), UX Features B (Tests 105 to 111).

Database Tables (Current)

user_memory: id, user_id, stable_profile (jsonb), recent_summary, event_log (jsonb array, cap 90), last_summarized_at_event_count, last_checkin_local_date, updated_at

app_settings: id, user_id, onboarding_version, first_open_completed (legacy), last_daily_reminder_sent_date, last_missed_followup_sent_date, last_weekly_summary_sent_week

commitments: id, user_id, created_at, check_in_id (nullable int, NO foreign key), commitment_text, followup_scheduled_at, completed, completed_at, followup_response, smaller_version

chat_sessions: id, user_id, started_at, ended_at, message_count, session_summary, risk_level_detected

check_ins: existing table from V1/V2 (with all binary and numeric fields)

sobriety_trackers: existing table from V1/V2

tracker_resets: existing table from V1/V2

stable_profile shape (Current)

{
  "recovery_focus": [],
  "sobriety_start_dates": {},
  "known_triggers": [],
  "support_style": "",
  "recovery_program": {
    "primary": "",
    "specific": []
  },
  "sobriety_why": "",
  "sober_contacts": [{ "name": "", "phone": "" }],
  "meeting_links": [{
    "label": "",
    "day_of_week": "",
    "time": "",
    "timezone": "",
    "url": ""
  }],
  "recurring_commitments": [],
  "pinned_facts": [],
  "email": "",
  "reminder_time": "08:00",
  "timezone": "America/New_York",
  "commitment_followup_hours": 4,
  "reminder_enabled": true,
  "weekly_summary_enabled": true,
  "theme_preference": ""
}

Required Replit Secrets

OPENAI_API_KEY

RESEND_API_KEY

RESEND_FROM_EMAIL

EMAIL_OUTREACH_ENABLED (must be "true" to activate scheduled sends)

APP_USER_ID (defaults to "dev_user" — currently single user)

OPENAI_TTS_MODEL (defaults to "tts-1")

OPENAI_TTS_VOICE (defaults to "onyx")

4. Test Suite Inventory

All 111 tests live in tests/e2e/anchor-smoke.spec.ts. They are run via Playwright against a live Replit preview environment. Tests are gated by: server reachability, Chromium browser availability, and clean test data state.

Test Phases

Tests 1 to 56: Original V3A through V3F1 smoke tests (memory system, check in, chat, commitments, voice input, email scheduler, TTS, navigation, crisis routing, handoff).

Tests 57 to 70: V3F2 onboarding and animation polish.

Tests 71 to 75: V3F2 post additions (full summary TTS, Chat with my coach button, Home quick action, nav audit).

Tests 76 to 82: V3F4 verification (TTS placement, history detail TTS, raw notes exclusion, checkin_context one shot, crisis suppression, single nav render).

Tests 83 to 87: V3F5 Chat Mode Detection (commitment offer, no repeat, crisis still fires, handoff at moderate, banned phrases excluded).

Tests 88 to 91: Bug Fix A (binary field defaults, commitments week count, Recovery Habits aggregation, multi check in numeric average).

Tests 92 to 94: Bug Fix B (Recent Patterns no markdown, /api/email-status returns 6 fields, RESEND_API_KEY value not exposed).

Tests 95 to 104: UX Features A (memory edit affordances, sober contact CRUD, recovery_program routing, multi program picker, meeting_links 5 field persistence, migration non destructive, trackers no internal scroll, fallback to aa-intergroup).

Tests 105 to 111: UX Features B (Paper theme, Midnight theme, theme_preference persists, Recent Patterns 3 sections, no markdown chars, insufficient data fallback, malformed JSON fallback).

Smoke Suite Health

All 111 tests currently pass. Test 26 was once a known stale failure; it was rewritten in V3.7 to assert auto submit behavior and now passes. There are no known persistent failures. Pre-existing minor known issues are tracked in Section 7.

5. Architecture and Stack As Built

Current Stack (Dev)

Frontend: React/TypeScript via Vite, Tailwind CSS, Wouter for routing, deployed on Replit preview URL.

Backend: Node.js/Express, file-based routes under artifacts/api-server/src/routes/, single-user via APP_USER_ID env var.

Database: PostgreSQL on Replit (single instance, dev grade).

AI: OpenAI gpt-4o-mini for chat and check in response generation, whisper-1 for voice transcription, tts-1 with onyx voice for spoken summaries.

Email: Resend with node-cron scheduler, gated behind EMAIL_OUTREACH_ENABLED="true".

Testing: Playwright via npm scripts, runs against the Replit preview URL with libgbm.so.1 system dependency.

Hosting: Replit deployments / preview only. No production deployment exists yet.

Helper Layer

All shared helpers live in utils/v3helpers.js (or equivalent). Named functions, no inline code. Single source of truth for getCurrentUserId(), loadUserMemory(), normalizeStableProfile(), buildMemoryContext(), appendEventLog(), classifyRisk(), buildHandoffPayload(), safeBackgroundTask(). The normalizeStableProfile function was extended in UX Features A to handle the new recovery_program object shape and 5 field meeting_links shape, with non destructive migration from prior plain string values.

Key Architectural Rules (Current and Enforced)

getCurrentUserId() everywhere. No hardcoded user IDs. No "maxwell" string. Returns process.env.APP_USER_ID || "dev_user".

stable_profile is single source of truth for ALL user preferences.

Phone numbers NEVER appear in AI prompts, memory context, TTS, summaries, or logs. Names only in AI context. Phones only in frontend payloads via buildHandoffPayload().

event_log cap is 90 entries. appendEventLog() always.

All background async operations use safeBackgroundTask().

Crisis = suicidal ideation, self harm, harm to others, overdose, acute medical danger ONLY. Imminent relapse = HIGH, not crisis.

No audio files written to disk. multer.memoryStorage() only.

No full chat history stored in database.

TTS never autoplays. Always user initiated.

Chat voice auto submits (intentional). Check in fields do not.

No FK on check_in_id in commitments table.

Memory summarization only when 3+ new event_log entries since last summarization.

last_checkin_local_date updated after every check in.

Email outreach requires EMAIL_OUTREACH_ENABLED === "true".

No catch up email sends after server restart.

Recent Patterns AI prompt returns strict JSON only. Parse failure falls back to generic message. Insufficient data (fewer than 3 check ins in window) shows 'check in a few more times' message.

Recovery program lookup uses recoveryResources.ts catalog. 39 URLs seeded. Find a meeting button is program aware. Multi program selection shows picker. Empty state falls back to aa-intergroup.org/.

6. Product Invariants (Updated)

These are laws. Every prompt, feature, refactor, and test must preserve them.

Anchor helps the user move toward wise action, not endless conversation.

AI never replaces human handoff.

Crisis flow interrupts normal AI conversation and shows structured crisis resources (988, SAMHSA, sober contacts, meeting links).

No automatic call, text, email, or social exposure occurs without explicit user confirmation.

Phone numbers never enter AI prompts, memory context, TTS, summaries, logs, pattern insight copy, or Recent Patterns output.

Raw notes, raw transcripts, raw voice input, and full chat history are minimized and never sent to unnecessary AI calls.

Deterministic code computes stats, thresholds, dedupe, drift, and pattern signals where possible.

AI explains, reflects, and supports, but does not fabricate certainty.

AI never invents contact names. Only names present in memory context can appear in AI output.

Home presents one primary next action at a time.

The user can inspect, edit, pause, export, or delete meaningful memory.

getCurrentUserId() is used everywhere. No hardcoded user IDs.

Background operations must use safeBackgroundTask() or equivalent safe wrappers.

No new database schema is added unless the prompt explicitly authorizes it.

No duplicate memory, insight, scheduler, or audio systems are created.

Every safety sensitive helper has tests.

Recovery program selections route to official, verified meeting resource URLs only.

All themes must pass WCAG AA contrast for normal text (4.5:1), large text (3:1), and UI components (3:1).

7. Known Issues and Deferred Items

Pre-existing Minor Issues (Not Blocking Production)

Check-in form state resets on tab navigation. Wouter unmounts the component. Fix would require localStorage persistence. Deferred.

Calendar heatmap font size at 10px on tiny cells. Increasing the font risks grid overflow. Deferred.

Items Surfaced by Field Test Not Yet Fixed

Light theme contrast already audited and fixed in UX Features B. Resolved.

Recovery Habits multi check in deduplication. Implemented in Bug Fix A. Resolved.

Commitments this week count showing wrong number. Fixed in Bug Fix A. Resolved.

Recent Patterns rendering raw markdown. Fixed in Bug Fix B. Resolved.

Find a meeting button always opening the same URL. Fixed in UX Features A. Resolved.

Memory screen read only. Fixed in UX Features A. Resolved.

Trackers home page scroll bar cut off. Fixed in UX Features A. Resolved.

Ate enough today defaulting to Yes. Fixed in Bug Fix A. Resolved.

Items Deferred Pending Production Decision

Full system health debug view (V3.7D in v1 doc). Partial replacement via /api/email-status. Deferred until production observability needs are clearer.

Backend invariant unit test suite separate from smoke tests (V3.7B in v1 doc). Smoke tests currently cover core invariants at the e2e level. Deferred.

Structured safe logging with trace IDs across all routes. Deferred until production load surfaces specific debugging needs.

Multi user migration. Required before any public deployment. See Section 13.

Real authentication. Required before any public deployment. See Section 13.

8. Recovery Program System (New Architecture)

This is one of the more substantive new pieces of architecture introduced in V3.7. It deserves its own section because it changes the shape of stable_profile and introduces a new lib file that should be treated as architectural reference data.

Primary Categories

AA

NA

12-Step (other)

Codependency / Relationships

Sex / Love / Porn / Intimacy

SMART Recovery

Recovery Dharma

Refuge Recovery

Secular / No Program

Gambling / Money / Work

Food / Eating

Other / Not sure yet

Sub Program Lists (Multi Select)

When primary is one of: 12-Step (other), Codependency / Relationships, Sex / Love / Porn / Intimacy, Secular / No Program, Gambling / Money / Work, Food / Eating, or Other / Not sure yet — a multi select sub picker is shown.

12-Step (other): Cocaine Anonymous, Crystal Meth Anonymous, Marijuana Anonymous, Heroin Anonymous, Pills Anonymous, Nicotine Anonymous

Codependency / Relationships: CoDA, ACA, Al-Anon, Nar-Anon, Families Anonymous

Sex / Love / Porn / Intimacy: SLAA, SAA, SPAA, SA, SCA, Porn Addicts Anonymous, COSA

Secular / No Program: LifeRing, Women for Sobriety, Secular AA, Moderation Management

Gambling / Money / Work: Gamblers Anonymous, Debtors Anonymous, Underearners Anonymous, Spenders Anonymous, Workaholics Anonymous

Food / Eating: Overeaters Anonymous, Food Addicts Anonymous, Food Addicts in Recovery Anonymous, Eating Disorders Anonymous, Anorexics and Bulimics Anonymous

Other / Not sure yet: SAMHSA, Psychology Today, Find a Helpline

URL Catalog

39 official URLs are seeded in src/lib/recoveryResources.ts. The list is treated as architectural reference data. Adding or removing a program requires updating both the onboarding picker, the Memory edit picker, and the catalog. The catalog is the single source of truth for the Find a meeting routing.

Find a Meeting Routing Behavior

If primary matches a top level key in the catalog AND specific is empty: open that URL.

If specific has one entry: open that entry's URL.

If specific has multiple entries: open inline picker with each option as a button.

Fallback if no match found or no program set: open https://aa-intergroup.org/.

All external links use target="_blank" and rel="noopener noreferrer".

9. Theme System (New Architecture)

As of V3.7 UX Features B, Anchor has 6 selectable themes. All pass WCAG AA contrast standards for primary text, secondary text, button text, input text, link text, and UI components.

Available Themes

anchor-light: Default light theme. WCAG AA verified after V3.7 audit.

anchor-dark: Default dark theme. WCAG AA verified after V3.7 audit. Border tokens raised.

high-contrast-light: High contrast light. WCAG AA verified.

high-contrast-dark: High contrast dark. WCAG AA verified. Border tokens raised. Destructive token raised from 58% to AA-compliant lightness.

paper: Warmer light theme. Off white background (#FAF7F2). Sepia / soft brown accents. Designed for low harshness reading. WCAG AA verified.

midnight: Deeper dark theme. Near black background (#0A0E14). Cool blue grey text. Indigo / violet accents for primary actions. WCAG AA verified.

Theme Persistence

User selection is stored in stable_profile.theme_preference. If missing, defaults to whatever the system default is. Theme is applied via [data-theme] attribute on the document root, with CSS custom properties scoped under :root, .dark, [data-theme="..."] selectors.

Token Changes from V3.7 Audit

anchor-dark --border, --card-border, --popover-border: raised from 22% to AA compliant lightness.

high-contrast-dark --border, --card-border, --popover-border: raised from 30% to AA compliant lightness.

high-contrast-dark --destructive: raised from 58% to AA compliant lightness.

slate (an existing minor theme variant): --border, --card-border, --popover-border raised from 26%.

All other tokens in all themes already passed WCAG AA prior to the audit.

10. Memory System Current State

Three Layer Memory

stable_profile (JSONB): persistent user preferences and configuration. Single source of truth for all user editable settings.

recent_summary (text): rolling AI generated summary of recent activity. Updated when 3+ new event_log entries accumulate since last summarization.

event_log (JSONB array): structured event history capped at 90 entries. Append only with capping enforced by appendEventLog() helper.

Memory Screen (As of V3.7)

The Memory screen now supports inline editing for every stable_profile field that the user can reasonably edit. Recovery focus, recovery program (with structured primary + specific picker), support style, sobriety why, sober contacts (full CRUD), meeting links (full CRUD with 5 field structured form), email, reminder time, timezone.

Edit pattern: tap to expand inline, Save / Cancel pair. PATCH to user_memory endpoint. No modals. No new screens.

Recent Patterns section now renders three labeled rows (Top triggers, Mood trend, Pattern to notice). Each is a single sentence of plain prose, generated from a strict JSON contract with the AI.

If fewer than 3 check ins exist in the relevant window, the AI call is skipped and the section displays "Check in a few more times to see your patterns."

Memory Privacy and Safety

Memory pause toggle in Settings (session only).

Reset memory button (typed confirmation "reset").

Phone number redaction enforced before any AI call.

AI generated insight events tagged so they cannot be treated as user generated facts in pattern detection.

event_log entries do not contain raw notes, raw transcripts, or full chat history.

11. Chat System Current State

Voice Orientation

Stoic and DBT oriented sponsor adjacent voice. Direct, warm, no flinching, never cruel, never contemptuous. Banned phrases list is enforced. Coach voice is preserved across all V3.7 prompt updates.

Mode Detection (V3F5)

Reflect: user is processing emotion or venting. Hold space, ask one good question, keep response short (1 to 3 sentences).

Plan: user is thinking through a decision. Help them think clearly, surface tradeoffs, longer responses are fine.

Pattern: user is describing a recurring behavior or dynamic. Name it directly, connect to known history if relevant.

Handoff: user is expressing isolation or asking for support beyond the coach. Route to named contact from memory. Make it the point, not a footnote.

Commitment: user states a concrete intended action. Offer to save it as a commitment exactly once. Do not repeat.

Mode is silently detected and never named to the user.

Crisis Flow (Unchanged)

Crisis detection runs structured risk classifier before every chat response. Crisis = self harm, suicidal ideation, harm to others, overdose, acute medical danger. Crisis triggers full screen crisis card with 988, SAMHSA, sober contacts, meeting links. Normal AI response generation is suppressed when crisis is detected.

Memory Injection

First message of session: full memory context (stable_profile summary, recent_summary, recent event log entries with phone numbers redacted).

Subsequent messages: stable_profile summary only, no recent_summary repeat.

Crisis messages: no memory injection beyond what the risk classifier needs.

Coach Context Handoff (V3F4)

When user taps "Chat with my coach" on a check in result card, checkinContextForCoach is written to sessionStorage. Chat reads it on first send only, passes as checkin_context to /api/chat (capped at 800 chars), injects as system level instruction. Cleared immediately after first use. Never stored, never in event_log.

12. The V4 Pivot: Production Before Features

The original V4 master doc proposed a heavy feature roadmap: Pattern Insight Engine, SOS Mode, Drift Detection, Memory Search Lite, Data Export, Relapse Response Protocol, plus habit architecture. Most of those features are good ideas in the abstract. None of them solve the actual current bottleneck.

The bottleneck is this: Anchor is a single user PWA running on a Replit dev URL with no production deployment, no real authentication, no real domain, no real users, and no signal about what features actually matter to people in recovery.

Building Pattern Insight Engine for one user (the developer) is shadow boxing. Building SOS Mode with no real users to test it on is shadow boxing. Building Drift Detection with one person's data is statistical nonsense.

The V4 doctrine therefore inverts: do not build more features until production is real. Ship V3 to a real domain with real auth and at least the developer's own production account. Port to Expo to have a real mobile artifact. Use both for two to four weeks. Listen for what actually breaks. Then decide which V4 features matter and which were speculation.

V4 Phases (Revised)

Phase 1: Production Deployment. Detailed in the separate Anchor V3 Production Deployment Plan document. Goal: Anchor V3 running on a real domain, with real auth, real users (at least one), real Postgres, real email, real error tracking. ETA: 1 to 2 weeks of focused work.

Phase 2: Mobile Port via Expo. Goal: Anchor running natively on iOS via Expo Go, then TestFlight. Goal artifact: a real native build to demo. App Store submission optional. ETA: 1 to 2 weeks.

Phase 3: Real Usage and Signal Gathering. Goal: at least 4 weeks of real usage by the developer in recovery, plus 2 to 5 invited beta users if appropriate. Listen for what breaks, what is missing, what is annoying. ETA: 4 weeks minimum.

Phase 4: Reassessed Feature Roadmap. Goal: pick the 1 to 3 highest signal V4 features and build them. Defer the rest. ETA: depends on what Phase 3 surfaces.

13. V4 Phase 1: Production Deployment

Detailed walkthrough lives in the separate Anchor V3 Production Deployment Plan document. This section captures the strategic decisions only.

Stack Decisions

Frontend: Vercel.

Backend: Fly.io. Cron compatible, has a real free tier, scales globally if needed, better fCTO résumé story than Railway.

Database: Neon Postgres. Generous free tier, branching for staging environments, modern, focused.

Auth: Supabase Auth. Free up to 50K users, OAuth providers built in (Google, Apple, GitHub), magic links available, clean SDK. Decoupled from database choice.

Email: Resend. Already integrated. Need to verify production domain (DNS, SPF, DKIM) and set production secrets.

Errors: Sentry. Free tier covers expected volume.

Analytics: None for now. For a recovery app, ethical bar is high. Sentry tells us what is broken; that is enough until there is a clear product analytics need. PostHog self hosted is the eventual answer if needed.

Landing page: Static site on Vercel, separate from the app. One page is sufficient. Hero, what it does, why it exists, screenshots, request access or direct app link.

Domain: TBD. Decide during deployment plan execution. Likely options: anchor.recovery, useanchor.app, or similar.

The Multi User Migration

This is the highest risk piece of the production deployment. Right now everything in the app is keyed off getCurrentUserId() returning process.env.APP_USER_ID || "dev_user". That is a single user shim. Multi user means every backend route, every helper that reads or writes user data, must derive user_id from an authenticated session. Supabase Auth handles auth. The app code must replace what getCurrentUserId() returns with the session derived user ID.

Approach: getCurrentUserId() is the chokepoint. Replace its implementation. Add a Supabase JWT verifier to every API route. Adjust helpers as needed. Add tests for cross user data isolation.

Production database starts fresh. Existing dev data is dev data and is not migrated. The user creates a real production account on first launch.

Pre Launch Must Haves

Privacy policy and terms of service. For a recovery app touching mental health data, this is not optional. Generated docs are acceptable for portfolio and TestFlight; lawyer review before any public marketing.

Real account deletion flow. Required by law in most jurisdictions and the right thing to do regardless.

Crisis disclaimer on the landing page: "This is not a replacement for professional care. If in crisis, call 988."

Resend domain verification (DNS, SPF, DKIM). Required before any production email send.

All test data wiped from production database before any real user signs up.

14. V4 Phase 2: Mobile Port via Expo

After production deploy stabilizes, port to Expo. The PWA already works on iOS Safari, but a native build is a stronger artifact for the fCTO transition story and unlocks proper push notifications, better audio handling, and a home screen presence.

Approach

Expo with React Native. Reuse most of the existing React component logic. Replace web-only modules (browser audio, web routing, etc.) with Expo equivalents.

Backend stays the same. The Fly.io API serves both web and mobile.

Auth stays the same. Supabase Auth has React Native SDK.

Storage: AsyncStorage replaces sessionStorage and localStorage.

Audio: expo-av for recording and playback. Replaces MediaRecorder.

Routing: Expo Router.

Build target: Expo Go for dev, then EAS Build for TestFlight.

App Store Considerations (Optional)

App Store submission for a recovery and mental health app is doable but slow. Apple reviews this category more carefully. Required: privacy policy, terms, age rating, possibly a clinical disclaimer. TestFlight is faster and is enough for portfolio and demo purposes. Decide on submission after TestFlight feedback.

What This Teaches

Native build pipelines (EAS Build).

Apple Developer certificate and provisioning.

TestFlight distribution.

Push notification architecture (APNs).

Mobile-specific UX constraints.

These are real CTO craft skills and are difficult to learn without doing. The mobile port is therefore both a portfolio piece and a tuition payment.

15. V4 Phase 3: Real Usage and Signal Gathering

Goal: at least four weeks of real, daily, sober use of Anchor by the developer, plus a small number of invited beta users if appropriate.

What to Watch For

Which features get used daily.

Which features never get touched.

Where the app feels slow, buggy, or annoying.

Where the AI is helpful versus where it is in the way.

Whether email outreach is actually wanted or feels invasive.

Whether the chat coach is genuinely useful or just performative.

Whether memory feels alive or stale.

Whether crisis routing has ever fired and whether the routing was right.

Whether human handoff has ever been used and whether the user actually called.

Where the user wishes the app could do something it can't.

How to Capture Signal

Daily field notes. Voice memo or written. 5 minutes a day.

Weekly summary review.

Sentry error reports.

Beta user 1:1 conversations if applicable. No forms. Voice.

What Not to Do During This Phase

Do not build new features.

Do not pivot the product.

Do not add analytics out of anxiety.

Do not optimize for users you do not have.

Do not respond to every annoyance with a code change. Capture, sit, decide.

16. V4 Phase 4: Reassessed Feature Roadmap

After Phase 3, pick the 1 to 3 highest signal items from the original V4 master doc v1 list and build them. Defer the rest. Below is the original list with current commentary on whether each one still seems likely worth building.

Likely Worth Building (Tentative)

SOS Mode: a persistent, AI-free, one-tap route to human contact. Strong product instinct. Likely to feel useful in real recovery. Build if Phase 3 confirms.

Data Export: trust feature. Cheap to build. Probably worth building regardless of signal.

Pending Commitment Card: already exists. Confirmed valuable in Phase 3 use.

Conditional

Pattern Insight Engine: deterministic ranked signals on Home. Could be valuable, could be noise. Build only if Phase 3 confirms users want pattern surfacing on Home.

Drift Detection: gentle early warning when check in pattern shifts. Risk of feeling like surveillance. Build only if Phase 3 confirms users want this signal.

Memory Search Lite: keyword search over event_log. Useful only if memory grows large. Probably defer until users have months of data.

Relapse Response Protocol: structured non shame flow when user reports not sober. High value if it exists, high risk if poorly executed. Copy must be near perfect. Build only after Phase 3 surfaces a real moment where this would have helped.

Habit Architecture (micro check ins, evening reflection): low priority. Build only if Phase 3 surfaces fatigue with the full check in flow.

Probably Defer Indefinitely

CrewAI / AutoGen orchestration. No clear use case.

Vector RAG memory. Deterministic search will be sufficient until proven otherwise.

Realtime voice call mode. AI cocoon risk. Cost risk. Privacy risk.

Wearables integration. High complexity. Privacy load. Defer until clear signal.

Therapist portal. Different product.

Social / community feed. Fundamentally different product. AI cocoon risk inverted.

Native iOS / Android rewrite from scratch. Expo is sufficient.

Biometric relapse prediction. Ethically fraught. Scientifically thin.

Autonomous outreach escalation. Violates the no automatic contact invariant.

17. Deferred Features from V4 v1

These were specified in detail in the v1 master doc with full implementation prompts. They are deferred but not abandoned. The full prompts in v1 remain useful as starting points if and when these features are built. Below is a summary of each with the current deferral reasoning.

Home Command Center

Original v1 scope: rebuild Home as a recovery cockpit with one primary next action, secondary pattern insight, quick actions, and lower priority stats. Current state: Home already does most of this implicitly through the existing layout (check in CTA, due commitment banner, pending commitment card from V3C, trackers, recent activity). A formal redesign can wait until Phase 3 surfaces specific Home pain points.

SOS Mode

Original v1 scope: persistent AI-free human handoff surface accessible from every major screen. Crisis card, sober contacts, meeting links, tell-on-myself template, 988, SAMHSA. Current state: handoff banner already exists at moderate and high risk in chat. Crisis routing is structured. The full SOS surface is not built. Strong candidate for V4.1 if Phase 3 confirms.

Offline Safety Cache

Original v1 scope: localStorage cache of contacts, meeting links, crisis resources for offline access. Current state: not built. Lower priority than SOS itself. Build only with SOS or after.

Pattern Insight Engine

Original v1 scope: deterministic helper that computes one PatternInsight from user data and returns it for Home display. Five signal types: missed_checkin_drift, rising_craving, low_sleep_high_craving, repeated_incomplete_commitments, no_recent_contact. Current state: Recent Patterns now does part of this in a different shape (3 bullet AI summary). A separate deterministic engine on Home is not built. Conditional on Phase 3 signal.

Pattern Insight Card UI

Original v1 scope: render the engine output as one card on Home with expandable why section. Current state: not built. Depends on engine.

Drift Detection

Original v1 scope: deterministic early warning with calm copy. Current state: not built. Conditional on Phase 3 signal.

Data Export and Trust

Original v1 scope: JSON, CSV, Markdown export with privacy defaults. Current state: not built. Probably worth building regardless of Phase 3 signal because it is a trust feature.

Memory Search Lite

Original v1 scope: keyword and filter search over event_log without embeddings. Current state: not built. Defer until memory volume justifies it.

Relapse Response Protocol

Original v1 scope: structured non shame flow when user reports not sober. Tracker reset confirmation, no auto contact, crisis routing if signals present. Current state: not built. High value if executed well, high risk otherwise. Defer until Phase 3 surfaces a moment when this would have helped.

Habit Architecture (Micro Check-ins, Evening Reflection)

Original v1 scope: optional low friction habit inputs. Current state: not built. Low priority.

Future Design Notes (Realtime Voice, Wearables)

Original v1 scope: design notes only, no implementation. Current state: design notes not written. Realtime voice is a cocoon risk. Wearables are a complexity and privacy risk. Both deferred indefinitely.

18. Permanent Non Goals

These are not deferred. They are explicit non-goals for Anchor as a product. Reassessing them requires reassessing the product itself.

Anchor is not a therapist.

Anchor is not a crisis service.

Anchor is not a replacement for a sponsor.

Anchor is not a social network.

Anchor does not auto contact anyone on behalf of the user.

Anchor does not pretend to predict relapse.

Anchor does not gamify recovery with shame loops or streak pressure.

Anchor does not optimize for engagement, time-in-app, or daily active sessions.

Anchor does not store full chat history.

Anchor does not send phone numbers, raw notes, raw transcripts, or full chat history into AI prompts.

Anchor does not create endless AI soothing loops. If distress conversation continues, it nudges toward human contact.

19. Closing Note

The strongest move at this point is not more code. It is shipping what already exists, putting it in front of real users (starting with the developer in real recovery), and listening.

V3 is good. V3 is not perfect. V3 is more than enough to be useful right now.

V4 will earn its existence by being shaped by real usage rather than speculation. Until then, the next document to write is the Anchor V3 Production Deployment Plan, and the next thing to do is execute it.

Ship the bridge.

— end —
