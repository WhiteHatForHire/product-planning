---
title: "Anchor Case Study In Progress"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/Anchor Case Study In Progress.docx"
status: archive
privacy: public-candidate
tags:
  - product
  - case-study
  - archive
---

# Anchor Case Study In Progress

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor — Case Study In Progress

Status: Working doc. Not for publication. Captures evidence and notes for later synthesis. Started: April 30, 2026 Last updated: April 30, 2026 (v3 — added "What this does NOT claim", objections, clinical/ethical boundary, artifacts list, output versions, Stage 0 progress)

Purpose

Capture, while it's still fresh, the full timeline and depth of the Anchor build so a credible case study can be written later. The case study itself is written after full production deployment is complete (post Stage 11 of the deployment plan). This doc is the evidence locker that feeds it.

The headline of the eventual case study will be something like: "Anchor: How a Three-Hour Prototype Became a Production-Grade Recovery App in Two Weeks, Solo, with Zero Lines of Hand-Written Code."

The framing is an escalation arc: 3 hours to working V1 → days to V3 with 111 tests → ~2 weeks to production launch. Each number is verifiable. The compound story is more persuasive than any single number.

The Real Timeline (Verified Against Source Documents)

April 23, 2026 — V1 Built And Documented

3 hours, 11 minutes. $14 total cost. 0 lines of code written by hand.

A working recovery check-in app shipped in a single session. Built via Replit Agent, directed by a precisely-written initial prompt that specified the stack (Node.js, Express, OpenAI JS SDK), the API pattern (Chat Completions, not Responses API), the system prompt verbatim, the structured JSON output shape, the database schema (with user_id included from day one), the form fields, the loading state, the results card, the design constraints, and the error handling.

The same day, a postmortem was written documenting exactly what was built. That postmortem exists as a contemporaneous artifact. Key data points from it:

7 database tables (check_ins, trackers, resets, settings, others)

OpenAI GPT-4o-mini integration with structured JSON

Sobriety tracking system with live counters

Insights dashboard with trend charts and calendar heatmap

PWA-installable frontend

Sponsor-toned AI referencing user-specific patterns

8 iterative build phases (V1 → V2A → V2B → V2C → V2D + fixes)

12+ revision prompts run that day

3 AI models consulted (Claude, ChatGPT, Gemini)

For comparison: a 2020-era agency would have charged $25,000-$30,000 and taken 2-3 months for the same scope

The V1 postmortem also articulates the Director Model methodology that becomes the architectural through-line of everything that follows.

April 23-24, 2026 — V3 Fork Begins

V3 began as a fork of the V2 codebase. The first V3 prompt removed authentication (Clerk) to enable single-user development, with auth planned for re-introduction at production deployment. This decision — strip the multi-user shim, ship features fast, add real auth right before launch — is reflected in the deployment plan (Stage 3: Multi-User Code Refactor).

April 23-25, 2026 — V3A Through V3F Build Phases

Eight feature phases shipped in sequence:

V3 Shared Architecture Cleanup — consolidated getCurrentUserId(), loadUserMemory(), and other shared helpers into a single utilities file before building features on top.

V3A — three-layer persistent memory system: stable_profile, recent_summary, event_log. Injected into every AI call so responses feel longitudinal.

V3A Revision Patch — performance tuning (summarization frequency), schema additions (last_checkin_local_date), onboarding lock.

V3B — sponsor chat interface with memory-aware AI, crisis routing to 988/SAMHSA, human handoff.

V3C — commitment and follow-up loop. Each check-in offers a single next action; the app follows up later.

V3D — voice input via OpenAI Whisper.

V3E — proactive email outreach. Daily reminders, missed check-in follow-ups, weekly pattern summaries via Resend. Hardened scheduler with feature flag (EMAIL_OUTREACH_ENABLED).

V3F1 — text-to-speech via OpenAI tts-1, scoped to result card "Remember" sections and sponsor chat bubbles only. Global audio manager. Strict invariants: no audio files written to disk, never speak raw notes/transcripts/chat history, only speak visible generated content.

V3F2 → V3F4 — TTS expansion: full-summary listen, history detail TTS, contextual coach handoff, mobile bottom-nav fix.

April 25, 2026 — V3.7 Stabilization Wraps

Per the V4 Master Doc v2 (also written April 25):

Test 26 fix (auto-submit alignment) shipped

Two new WCAG AA compliant themes added (6 themes total)

Recovery program selection mapped to 39 official meeting resource URLs

Inline memory editing (sober contacts, meeting links, profile fields)

Stoic + DBT-oriented chat coach with mode detection (Reflect, Plan, Pattern, Handoff, Commitment)

Deterministic recent patterns generation (replacing markdown-rendering AI text)

Bug Fix A and Bug Fix B shipped (binary field default state, commitments week count, recovery habits aggregation, multi-check-in algorithm, email diagnostic endpoint)

UX Features A and B shipped (memory inline editing, recovery program expansion, find a meeting routing, structured meeting links, trackers home scroll fix, full theme contrast audit)

111 Playwright smoke tests. All passing.

April 25, 2026 — V4 Master Doc v2 Written

Doctrine pivot documented: V4 is not more features. V4 is production. The original V4 plan (SOS Mode, Pattern Insight Engine, Drift Detection, Memory Search Lite, Data Export, Relapse Response Protocol, habit architecture) is deferred until production usage proves which features actually matter.

The pivot itself is part of the case study. Most builders accelerate when they get fast. The discipline shown in the V4 v2 doc is the opposite: deliberate slowdown after a sprint, refusal to confuse motion with progress, and clear criteria for what V4 will actually be after real users have shipped signal.

April 25, 2026 — V3 Production Deployment Plan Written

Comprehensive 21-section operational doc covering 11 deployment stages: domain, database (Neon), auth (Supabase), multi-user refactor, backend deploy (Fly.io), frontend deploy (Vercel), email (Resend production domain), error tracking (Sentry), landing page, legal/compliance, first real account, smoke test in production. Plus go/no-go checklist, rollback plan, post-launch first week observation protocol, cost expectations, common traps, environment variable reference, and useful commands.

This doc itself is evidence of how the work was approached: deployment treated as a sequenced engineering project with checkpoints, not a sprint.

April 26, 2026 — V4.1 Spec Written

Anchor V4.1 — Practice Mode (Guided Skill Practice). A focused practice surface where users rehearse recovery-relevant skills (urge surfing, asking for help, refusing offers, repair after a slip, holding a no when asked) inside short branching scenarios. AI generates dialogue inside human-authored branch trees. Six modules planned, including a codependency POC.

Notable: V4.1 is fully spec'd but explicitly gated on V4 stability. The spec includes dependencies on V4, product invariants extending V3 and V4 invariants, the Practice surface variant of buildChatSystemPrompt, module structure, branch tree authoring format (JSON), the deterministic state machine, the dialogue generator pattern, need-state entry, the "this doesn't fit my situation" affordance, Repair Loops replacing dead-ends, three-path completion (commitment / tiny next action / save without committing), and immediate post-module rating.

V5 Post-V4.1 Roadmap also drafted same week.

April 26-28, 2026 — Anchor V4 Folder Created, App User Feedback Collected

Active product evolution between V3 ship and production deployment.

April 28, 2026 — V3.x Live On Replit Deploy URL

Working application running on a Replit-assigned URL. Field-testable. Used personally daily by the developer.

April 30, 2026 — Production Deployment Begins

Today. Stage 0 of the V3 Production Deployment Plan in motion. Domain registered: sobrietyanchor.com. Desktop containment pass shipped via V3F5A focus prompt (5 minutes, $0.75 agent cost, 8/8 smoke tests passing, +42/-36 lines).

What Was Built (As Of V3 Replit Deploy)

Architecture

Frontend: React/TypeScript via Vite, Tailwind CSS, Wouter for routing

Backend: Node.js/Express

Database: PostgreSQL (Replit-hosted during build, Neon planned for production)

AI: OpenAI GPT-4o-mini (chat + check-in synthesis), Whisper (voice transcription), tts-1 (speech)

Email: Resend (scheduled reminders, missed-check-in follow-ups, weekly summaries)

Hosting: Replit during build phase; Fly.io + Vercel planned for production

Tests: 111 Playwright smoke tests organized by feature phase (V3A through V3F5, plus Bug Fix A/B and UX Features A/B)

Memory System

Three-layer persistent architecture. Every AI call receives:

stable_profile — recovery program, sober contacts, meeting links, sobriety start dates per substance, timezone, reminder time, theme preference. User-editable inline.

recent_summary — AI-generated rolling summary of recent state, regenerated when event_log accumulates 3+ new entries (performance-tuned).

event_log — append-only log of check-ins, chat sessions, commitments, tracker resets.

Strict separation between user-generated facts and AI-generated inference.

Check-In System

Full check-in: 14 fields (mood, energy, craving, focus, hours slept, sober today, meeting attended, sober contact, fellow called, exercised, ate enough, trigger tags, notes, gratitude)

Quick check-in: 5-field rapid version with prefill

24 trigger tag options as multi-select pill buttons

Color-coded sliders: red-to-green for mood/energy/focus, inverted green-to-red for craving

Structured JSON output: state summary, risk level, main risk factor, next moves, recovery support prompt, grounding reminder, optional sponsor note

Multi-check-in algorithm: last value wins for binary fields, average for numeric fields

Chat System

Memory-aware sponsor-adjacent AI

Mode detection: Reflect, Plan, Pattern, Handoff, Commitment (silent — never named to user)

Voice: Stoic + DBT-oriented, plain-speaking, non-shaming, action-oriented

Crisis routing to 988 + SAMHSA with normal AI response suppression

Human handoff banner at moderate/high risk

Banned-phrase suppression

Single commitment offer per session, no repeat

Voice input via Whisper

TTS playback per message via global audio manager

Recovery Program System

39 official meeting resource URLs. Multi-program selection (primary + specific). "Find a Meeting" routing based on selected program with fallback to aa-intergroup.org.

Trackers

Multiple sobriety trackers running simultaneously. Live counters (days + hours, updates every 60 seconds). Reset flow with neutral language and optional notes logged to tracker_resets table. 10-color picker. Calendar heatmap. Date-shift banner on home (non-blocking, first-open-of-day).

Insights Dashboard

Streak stats, trend charts (mood, energy, craving, focus, sleep — 7/30/90 day toggle), calendar heatmap colored by risk level, recovery habit frequency as percentage bars, sobriety tracker history, CSV export.

TTS Architecture

Single endpoint /api/speak with context validation (checkin or chat only)

Context-specific truncation (500 chars for checkin, 1000 for chat)

Global audio manager — one stream at a time, stops on navigation

User-initiated only (no autoplay)

Hard invariants: no audio files written to disk, never speak raw notes / transcripts / chat history / phone numbers / hidden memory context

Crisis cards suppress TTS

Email Scheduler

Daily reminder at user-configured time per stable_profile

Missed check-in follow-ups

Weekly pattern summaries

Feature flag (EMAIL_OUTREACH_ENABLED) defaults off until production verified

Health diagnostic endpoint /api/email-status

Themes

6 themes total, all WCAG AA compliant. Theme preference persists to stable_profile.

Crisis & Safety Surface

Crisis cards for self-harm/suicidal ideation routing to 988

Moderate-distress handoff banner

Banned phrase suppression in AI output

Phone numbers never enter AI prompts, TTS payloads, or memory context

Raw user input never re-injected into subsequent AI calls

Mode detection silent (mode never named to user)

The Director Model Methodology

The methodology is part of the case study, not just the result. From the V1 postmortem and the V3F prompt archive, the actual operating principles:

Narrow scope per prompt

Each V3F prompt does one thing. V3F1 is text-to-speech only. V3F2 is the second TTS surface. V3F4 is layout polish across four specific concerns. V3F5A is desktop containment. Broad prompts produce broad failures. The V4 master doc explicitly names this: "V4 is a deliberate slowdown."

Explicit over implicit

Prompts specify: file paths to inspect during pre-flight, function signatures, exact JSON shapes, copy strings verbatim, explicit out-of-scope lists, V3 safety invariants reproduced in every prompt, verification checklists, and final report format constraints.

Pre-flight inspection before edits

Every V3F-format prompt requires the agent to inspect the codebase first and report findings in 3-5 bullets before changing anything. This catches errors before they propagate.

Strict rules and out-of-scope lists

Every prompt has a "STRICT RULES" section enumerating what NOT to touch. The desktop containment prompt explicitly forbids sidebars, top nav, hover affordances, multi-pane layouts, copy changes, color changes, theme changes, backend changes, and routing changes. Without explicit fences, agents drift.

V3 safety invariants reproduced verbatim every time

getCurrentUserId() everywhere, no hardcoded user IDs, phone numbers never in prompts/TTS/logs, raw notes never in TTS, crisis cards suppress normal output, single commitment offer per session, audio never written to disk. The same block appears in every prompt — even when the prompt is layout-only and the invariants don't seem relevant. Reproduction prevents regression.

Multi-model consultation

Claude for architecture and spec writing. ChatGPT for spec generation and validation. Gemini for product innovation. Codex CLI for some implementation work. Multiple instances running in parallel, each scoped to its strength.

Revision discipline

Never correct mid-build. Let each phase complete, test on real device, then write a clean fix prompt. The codebase is the source of truth; the fix prompt is the next directive.

Forward planning

The original V1 prompt included user_id in the database schema even though V1 was single-user. V3 memory columns were documented before they were needed. Onboarding was designed for 9 steps from the start to avoid downstream renumbering.

The shape of a Director Model prompt

Every V3F prompt has the same skeleton: title, brief context, goals as numbered list, stack context, strict rules, pre-flight inspection requirements, V3 safety invariants, parts (one section per discrete change), out-of-scope list, verification checklist, deliverable format. This is a methodology, not improvisation.

The Numbers (As Of April 30, 2026)

Build Phase

Idea to working V1: 3 hours 11 minutes ($14)

V1 to V3 feature-complete: ~5 days

Lines of code written by hand: 0

AI models directed: Claude (primary), ChatGPT, Gemini, Codex, Replit Agent

Database tables (V3): ~7 (check_ins, user_memory, app_settings, commitments, chat_sessions, sobriety_trackers, tracker_resets — exact count needs verification)

Themes: 6, all WCAG AA

Recovery program URLs: 39

Test count: 111 Playwright smoke tests, all passing

Replit cost through V3 build: ~$80

OpenAI API spend through V3 build: ~$0.09 (one user testing)

V3F5A desktop containment agent run (April 30): $0.75

Domain (sobrietyanchor.com, 1 year): ~$10-15

Total spend to date: ~$90-95

Field-test bugs from real-device testing: 17 (all triaged, most shipped as Bug Fix A/B/UX Features A/B)

Comparable agency build (2020): $25,000-$30,000, 2-3 months

Cost narrative for case study: "Under $100 to ship a working multi-feature recovery app. ~$10-25/month to run it in production at one user. Comparable 2020-era agency build: $25,000-$30,000."

Production Deployment Phase (In Progress)

Deployment plan: 21 sections, 11 stages

Estimated cost at 1 user: ~$10-25/month (Vercel, Neon, Supabase, Sentry, Resend on free tiers; Fly ~$2-5/month; OpenAI ~$5-15/month)

Estimated time to production: 1-2 weeks from April 30

Spec/Roadmap Depth (Beyond V3)

V4 Practice Mode: fully spec'd, gated on V4 production deployment

V4.1 modules: 6 planned (urge surfing, asking for help, refusing offers, repair after slip, holding a no, codependency POC)

V5 roadmap: drafted

Evidence Inventory

This section tracks what evidence exists in concrete form. Most of this is now confirmed via the source archive.

Already Have (from merged source doc)

[x] V1 postmortem (April 23, 2026) — contemporaneous documentation with exact numbers

[x] V1 initial prompt — saved verbatim

[x] V3 fork prompt — "This is a forked version of the Anchor recovery app. We are building V3..." saved verbatim

[x] Field test backlog (April 25, 2026) — 17 issues triaged

[x] V3 Production Deployment Plan (April 25, 2026) — full operational doc

[x] V4 Master Doc v2 (April 25, 2026) — pivot doctrine documented

[x] V4.1 Practice Mode spec (April 26, 2026) — full architectural spec

[x] V3F1 (TTS) prompt — saved verbatim, demonstrates Director Model prompt shape

[x] V3 Shared Architecture Cleanup prompt — saved verbatim

[x] V3A Revision Patch prompt — saved verbatim

[x] Multiple V4 prompt drafts saved verbatim (V4 Prompt 1-6, V4.1 Prompt 1-12)

[x] V3F4 prompt (Result Summary Placement + History TTS + Contextual Coach Handoff + Nav Fix) — saved verbatim

[x] V3F5A (Desktop Containment) prompt — saved verbatim

[x] Google Drive folder screenshot showing creation date (Apr 23, 2026) and file timeline

[x] Replit Agent screenshot showing "7 days ago" timestamp confirming April 23 V1 build

[x] Pre-V4 Pre-Deploy Prompts doc

Need To Capture

[ ] Git history export — git log --all --pretty=format:'%h %ad %s' --date=iso > git_history.txt

[ ] Repo size at V3 deploy (LOC, file count)

[ ] package.json snapshot

[ ] Smoke test file headers — at minimum the names of each of the 111 tests

[ ] Screenshots of Replit cost dashboard with dates

[ ] OpenAI usage dashboard screenshot showing $0.09 April spend

[ ] Working app screenshots: Home, Check-In flow (Quick + Full), Chat (with crisis routing demo), History list, History detail, Trackers home, Memory, Insights, Settings — both mobile and desktop

[ ] Smoke test pass output screenshot ("111/111 passed")

[ ] Replit deploy logs screenshots with dates

Production Phase Evidence (Capture As It Happens)

[ ] Stage-by-stage notes for deployment work (April 30 onward) — voice memo or short text per session

[ ] Cost evidence for production stack (Fly, Neon, Supabase, Resend, Vercel, Sentry)

[ ] Domain registration receipt + screenshot

[ ] First successful magic link delivery screenshot

[ ] First production check-in screenshot

[ ] First-week post-launch observations (per Section 17 of deployment plan)

[ ] Final cost tally

Voice Memos To Record

If you do nothing else from this doc, do these. Each is 5-15 minutes, dated.

Build week recap (one memo, ~10-15 minutes):

What was the actual idea on April 23?

What was the original V1 spec doc's strongest move? (Hint: specifying Chat Completions over Responses API, including user_id in V1 schema for future multi-user.)

What were the V2A through V2D iterations doing?

When did the V3 fork happen and why?

How did the V3F focus prompt format emerge?

What was the hardest moment in the build?

What did the AI do unexpectedly well?

What did the AI consistently get wrong, and how did you compensate?

The V4 pivot decision — when did it crystallize that V4 is production, not features?

What would you do differently?

Pre-deployment recap (one memo, ~5 minutes, before Stage 0):

Current state of the app

What you're nervous about for production

Why deployment feels different from build

Time and cost expectation to launch

Post-deployment recap (one memo per stage, 2-3 minutes):

Stage worked on

What worked first try

What broke

What you learned

These memos are the voice of the case study. The evidence is the proof, but the memos are the texture.

Synthesis Plan (Post-Production-Launch)

When the deployment is complete and the case study is ready to be written:

Step 1: Consolidate Evidence

Single /anchor_case_study/ folder. Subfolders: 01_timeline/, 02_artifacts/ (all V3F prompts, V4 master doc, deployment plan, V4.1 spec), 03_screenshots/ (build, deploy, app surfaces, costs), 04_costs/, 05_process/ (voice memos transcribed), 06_methodology/ (Director Model articulation).

Step 2: First Draft With Claude

Open a fresh long-context Claude session. Provide the case-study-in-progress doc, deployment plan, V4 master doc, V3F prompts in order, key conversation excerpts, cost screenshots, and the V1 postmortem. Ask for: a structured outline aimed at the fCTO audience (founders, VCs, technical leaders evaluating AI-directed work).

Step 3: Decide Format

Most likely formats based on positioning:

Long-form essay on personal site / Substack — primary asset for fCTO sales conversations

LinkedIn long-form post — distribution surface, distilled to ~2000 words

PDF case study — sent ahead of fCTO discovery calls

Section in Four Modes of Life — fits the Build mode chapter; the V4 v2 doctrine pivot is itself a Build-mode lesson

Twitter thread — probably too thin for the actual story; defer

The escalation arc is the asset. Distribution decides the wrapper.

Step 4: Draft With Discipline

Constraints for the draft:

Every claim has a receipt. If a number appears, evidence exists in the case study folder.

Honest about what AI did vs what the human did. The V1 postmortem already said this clearly: "the question is whether the person directing it understands the domain well enough to specify correctly, catch errors, iterate precisely, and maintain architectural integrity across a multi-phase build."

Honest about what was deferred (V4 features), what didn't work the first time (the field test backlog of 17 bugs), what cost more than expected.

No "AI built my entire app while I slept" framing. The actual story is more disciplined: a former agency operator with seven years of shipping software directing AI tools deliberately, with safety constraints, on a product that has real consequences.

Lead with the 3-hour V1 number. Escalate to the V3 feature-complete number. Land on the production-grade number. Each one is verifiable. The compound number is more defensible than any single one.

Step 5: Honest Critic Pass

Show draft to people who'll tell the truth, not validate. Marcus has historically responded well to honest critique over flattery — apply the same standard here.

Step 6: Distribution Decision

Public publication contributes to the Marcus Vale brand and fCTO positioning. Private use as a sales asset protects the leverage. Both defensible. Decide based on what the sales pipeline needs at that moment.

Framing Guidance For The Eventual Draft

A few framing choices worth thinking about now so they don't have to be made under pressure later:

The escalation arc beats any single number

"3 hours to working V1, 5 days to feature-complete V3 with 111 tests, ~2 weeks to production launch" is the through-line. Not "5 days to launch." The escalation tells a story; the single number invites skepticism.

"Working" and "production-ready" are different — say so

Real reviewers (VCs, senior engineers, skeptical founders) hold "production-ready" to a specific standard: real auth, custom domain, production hosting, verified email, error tracking, privacy/ToS, account deletion. The deployment plan exists because that gap is real. Don't claim production-ready before Stages 0-11 are complete.

Strongest honest framings:

"Working application in 1 week. Production launch in 2."

"From idea to working V3 with 111 tests in 1 week. From there to production-grade infrastructure in another week."

"3 hours to V1. 5 days to V3. 2 weeks total to a real domain with real auth."

Each is more credible and more impressive than "production-ready in 1 week" because each is true. The 2-week number is still a 10-15x compression on a comparable agency build. The bigger number doesn't need the smaller one to land.

A 1-week build case study is also legitimate and worth telling: "feature-complete recovery app with 111 passing tests in 7 days, solo, zero hand-written code." That's a real story. It just isn't a production case study. Tell both honestly, escalating from one to the other.

The Director Model is the methodology, not a buzzword

The case study should show the methodology, not just claim it. Reproduce a V3F prompt verbatim. Show what "narrow scope per prompt" looks like in practice. Show the V3 safety invariants block. Show the strict rules and out-of-scope lists. The receipts are the argument.

The seven-year agency track record is the prerequisite

The compression isn't just AI tools. It's an experienced operator using AI tools. Seven years running a software agency to near-million-dollar revenue is what makes the timeline credible. Don't bury it. The case study isn't "AI replaced engineering experience" — it's "engineering experience plus AI direction is a different category of capability than either alone."

The safety surface is the real story

Anchor isn't a CRUD app or a SaaS landing page. It's a recovery tool with crisis routing, banned-phrase suppression, mental-health-grade privacy considerations, and consequences if the AI misbehaves. Building this in days while taking the safety surface seriously is harder than building a generic CRUD app in days. The crisis routing, the banned-phrase suppression, the phone-numbers-never-in-AI-prompts invariant, the audio-never-written-to-disk invariant — these are the moves of an operator who understands the stakes.

The V4 pivot is its own data point

Most builders get faster and accelerate. The V4 v2 master doc shows a different move: a deliberate slowdown after a sprint. The pivot from "build V4 features" to "ship V3 to production, gather signal, then decide what V4 means" is a maturity signal that's hard to fake. Include it in the case study. The discipline is itself part of the offer.

What this proves about fCTO work

The Anchor build is a credible answer to "what can you do for a startup founder." Specifically: in days, alone, you can take a serious idea from spec to feature-complete application with real safety constraints and a real test suite. In weeks, alone, you can take that to production. That's the offer. The case study is the demonstration of the offer.

The lifestyle context isn't a footnote

The build happened from Bali. The fCTO positioning targets NYC. The book Four Modes of Life is in active manuscript completion under the Marcus Vale pen name. The neo-classical brand aesthetic is being built in parallel. The intentional lifestyle design isn't separate from the work — it's the operating context. The case study can mention it without making it the story.

Anchor is the depth proof. The utility apps are the breadth proof.

In addition to Anchor, ~7 shipped utility apps exist in Lovable, including:

Document Polisher (PDF tooling)

Mixref Deployer (audio reference analyzer)

Music Mix Hub (mix analysis)

Image Shrinker / Squish (image compression)

Audio Converter Hub

Doc Assembler (DOCX merger)

PDF Magic Compressor

These are not part of the Anchor case study, but they are part of the broader portfolio context. Anchor proves depth — one app, hard problem, full lifecycle, real safety constraints. The utility apps prove breadth — multiple apps, multiple domains (PDF, audio production, image, document tooling), consistent shipping.

For the portfolio site, the right structure is probably:

Anchor as the headline case study (depth + safety + production)

Utility apps as an "Other shipped work" grid below — small cards, one-line descriptions, live links, no individual case studies needed

Resist the urge to over-write the utilities. They don't need individual case studies. They need to exist as evidence of consistent shipping. One deep case study + a grid of live utilities is more persuasive than eight shallow case studies.

The portfolio site is downstream of Anchor's production launch. Sequence: ship Anchor V3 to production, then build the portfolio site around the Anchor case study with the utility grid as supporting evidence.

What This Case Study Does NOT Claim

Most important section in this document for protecting credibility. Skeptical readers will look for overclaiming. Pre-empting it makes the actual claim land harder.

This case study does NOT claim:

That AI replaced engineering judgment.

That the app was "production-ready" in 3 hours, or even in 5 days.

That zero hand-written code means zero technical work — direction, specification, testing, and architectural decisions are technical work.

That the current version is clinically validated, HIPAA-compliant, or appropriate for high-acuity crisis intervention beyond routing and handoff.

That the 988 routing replaces actual mental health care or human support.

That the app has product-market fit, validated user value, or proven clinical outcomes.

That every founder could reproduce this timeline. Seven years of prior software agency experience and an existing technical vocabulary are prerequisites that don't transfer trivially.

That "AI built the app" — Replit Agent and other AI tools were implementation engines directed by a human architect.

The actual claim is narrower and stronger:

An experienced software agency operator used AI tools as implementation engines while retaining architectural judgment, product judgment, safety judgment, and sequencing discipline, to compress a serious app build from months into days/weeks. The methodology is reproducible by other experienced operators. The compression is real. The discipline is what makes it credible.

Lead with the narrow claim. Don't broaden it. Broadening invites skeptics to argue with the broadest reading; narrow framing forces them to argue with what's actually being said.

Likely Objections And How To Address Them

The eventual case study should anticipate these objections and address them in the body, not in a defensive footer. Pre-empting skepticism is more credible than rebutting it after the fact.

"Zero hand-written code is a gimmick." The point isn't that code didn't matter. The point is that direction — specification, scope control, testing, architectural judgment, safety invariants — became the scarce skills. The prompt archive is the receipt. Show V3F1 verbatim. Let readers count the lines of specification per line of resulting code.

"Replit Agent did the real work." Replit Agent implemented. Marcus directed. The evidence is the prompt archive, the scope discipline (each V3F prompt did one thing), the safety invariants reproduced verbatim across every prompt, the test count, the V4 doctrine pivot decision. An undirected agent doesn't produce 111 passing tests on a recovery app with crisis routing. Direction is the work.

"This isn't production-ready until auth, domain, hosting, legal, deletion, monitoring, and email are all real." Correct. That's why this case study explicitly separates working V1, feature-complete V3, and production launch as three distinct milestones, not as one number. The 2-week production timeline is the honest claim. The 5-day V3 number is the honest claim. They're different claims.

"Recovery apps are high-risk; speed is dangerous." Correct if speed replaces safety. Not correct in this case. Safety was treated as a first-class surface from V1: crisis routing, banned-phrase suppression, prompt boundary enforcement, phone-number isolation, TTS content restrictions, human handoff at moderate risk. The V3 safety invariants block was reproduced in every prompt, even when prompts were layout-only. The discipline was the same as the discipline applied to features.

"Could this survive real users?" Unproven. The case study explicitly distinguishes build compression (proven) from product-market validation (not yet attempted). The V4 doctrine — defer feature work until production usage produces signal — is the discipline that recognizes this distinction.

"Why should anyone trust an AI-built recovery app with mental health data?" Because the build methodology was conservative on safety even when fast on features. Because the architecture has explicit boundaries (no audio to disk, no phone numbers in prompts, no raw user input re-injected, RLS-equivalent enforcement at the application layer). Because this case study itself is honest about what's not yet validated.

Clinical And Ethical Boundary

Anchor is a recovery-support and self-reflection tool. It is not a therapist, not a sponsor, not an emergency service, not a clinical treatment provider, and not a substitute for any of those. The case study must not imply otherwise.

Public framing language to AVOID:

"AI therapist"

"Replaces sponsor"

"Prevents relapse"

"Crisis support app" (as the primary positioning)

"Mental health treatment"

Any claim of clinical efficacy or outcomes without evidence

Any phrase that implies the AI is providing care rather than reflection support

Public framing language to USE:

"Sobriety companion"

"Recovery reflection tool"

"Daily check-in and grounding system"

"AI-assisted self-governance support"

"Built with crisis-routing and safety constraints"

"Sponsor-adjacent" (deliberately uses "adjacent" — Anchor is not a sponsor)

The crisis routing and 988 referrals are real and important, but they are routing, not care. The case study should describe them as routing infrastructure, not as crisis intervention capability. A reader skimming the case study should leave with a clear understanding that Anchor supports recovery work; it does not replace human support, professional care, or established programs (12-step, MAT, secular recovery, harm reduction).

This boundary is not just legal protection. It's honest positioning. Overclaiming on clinical capability would be the single fastest way to destroy the credibility this case study is meant to build.

Artifacts To Show In The Final Case Study

Show, don't just tell. The eventual case study should be visually grounded so readers don't have to take the narrative on faith. Target artifact list, in suggested order of appearance:

Original V1 prompt — show the actual specificity. Reader sees Chat Completions API choice, system prompt verbatim, schema with user_id from day one, exact JSON shape. Argues itself.

Screenshot of V1 working app — same day as the prompt above, dated April 23.

V3F prompt structure excerpt — V3F1 (TTS) is the strongest example. Show the strict rules, the safety invariants, the pre-flight requirements, the verification checklist.

Smoke test pass screenshot — "111/111 passed" with timestamp.

Replit cost screenshot — agent spend through V3 build phase.

OpenAI usage screenshot — showing trivial spend during build.

Production deployment plan ToC — 21 sections, 11 stages. Argues that deployment was treated as engineering, not improvisation.

Before/after desktop containment screenshots — show V3F5A's effect. Five-minute change, $0.75, tests still green.

Live sobrietyanchor.com screenshot — production landing page when ready.

One sanitized check-in output — show the AI's actual output quality with all personal data removed/replaced.

One sanitized crisis-routing demo — show how the safety surface activates. Critical for the "we took this seriously" argument.

Architecture diagram — Vercel + Fly + Neon + Supabase + Resend + Sentry + OpenAI. Shows the stack is real and portable.

Cost breakdown chart — build cost vs comparable agency cost vs ongoing operational cost.

Rule: every numeric claim in the case study should have a corresponding artifact in the supporting evidence. No screenshot, no claim.

Case Study Output Versions

The case study should be packaged as multiple artifacts targeting different audiences. Same source material, different wrappers. Don't try to make one document serve all audiences.

Version 1: Long-form essay (4000-6000 words) Audience: founders, technical leaders, AI-native operators, the Marcus Vale brand audience. Purpose: establish credibility, explain the Director Model methodology in depth. Distribution: personal site / Substack / Medium. Primary asset for the brand. Tone: confident but disciplined. The narrow claim, the methodology, the receipts.

Version 2: Sales PDF (4-8 pages) Audience: potential fCTO clients in active discovery conversations. Purpose: prove capability quickly before/after a discovery call. Distribution: emailed before or after a sales conversation. Linked from a private URL on the portfolio site. Tone: business-outcome-oriented. What this means for the founder reading it.

Version 3: LinkedIn long-form post (~1500-2500 words) Audience: broader professional network, NYC tech community, fCTO inbound. Purpose: distribution and inbound interest generation. Distribution: LinkedIn native long-form post. Possibly threaded. Tone: impressive but not hypey. Lead with the discipline, not the speed.

Version 4: Portfolio page Audience: people already evaluating Marcus. Purpose: concise proof asset embedded in the portfolio site, with screenshots, numbers, and live link to sobrietyanchor.com. Distribution: marcusvale.com (or whatever the brand URL becomes) /work/anchor. Tone: case-study-as-product-detail.

Version 5: Private technical appendix Audience: serious buyers, collaborators, investors who want depth. Purpose: detailed evidence — architecture decisions, testing approach, safety decisions, full cost breakdown, deployment plan, V3F prompt examples. Distribution: private link, shared deliberately. Not on the public site. Tone: technical and complete.

Version 6 (deferred): Twitter/X thread Probably skip. The story is too nuanced for the format. If pursued, it should be 8-12 posts maximum, lead with the discipline, link to the long-form essay for anyone who wants depth.

Versioning principle: All versions point at the same evidence locker. The numbers are identical across versions. Only framing, length, and tone vary by audience. This avoids the trap of having different "versions of the truth" floating around at different word counts.

Status Tracker

Update this section as evidence is gathered.

Pre-Production-Launch

[x] Source archive read (merged_extracted.md, ~25k lines)

[x] V1 postmortem confirmed (April 23, 2026)

[x] All V3F prompts located in archive

[x] V4 Master Doc v2 confirmed (April 25, 2026)

[x] V4.1 Practice Mode spec confirmed (April 26, 2026)

[x] Deployment plan confirmed (April 25, 2026)

[x] Google Drive folder screenshot (folder created Apr 23, 2026)

[x] Replit Agent screenshot ("7 days ago" — confirms April 23 V1 build)

[ ] Build week voice memo recorded

[ ] Pre-deployment voice memo recorded

[ ] Working app screenshots captured (mobile + desktop)

[ ] Cost screenshots captured (Replit, OpenAI)

[ ] Smoke test pass screenshot captured

[ ] Repo metadata captured (LOC, file count, package.json)

Production-Launch Phase

[~] Stage 0 (domain + accounts) — 85% complete as of April 30 PM

[x] Domain registered: sobrietyanchor.com

[x] 7 service accounts created (Vercel, Fly, Neon, Supabase, Resend, Sentry, GitHub confirmed private)

[x] LLC email used across all accounts

[x] Anchor Production Secrets master note created in LastPass

[x] Bonus: V3F5A desktop containment shipped (5 min, $0.75, 8/8 tests)

[ ] Vercel 2FA confirmed working (sign-out/sign-in test)

[ ] Fly billing alert at $20/month

[ ] OpenAI spend alert at $50/month confirmed

[ ] LastPass folder screenshot (cropped) captured

[ ] Stage 0 completion voice memo recorded

[ ] Stage 1-2 (Neon, Supabase) evidence captured

[ ] Model evaluation session evidence captured (session prep doc exists)

[ ] Stage 3 (multi-user refactor) evidence captured

[ ] Stage 4-7 (Fly, Vercel, Resend, Sentry) evidence captured

[ ] Stage 8-9 (landing, legal) evidence captured

[ ] Stage 10-11 (first real account, smoke) evidence captured

[ ] Final cost tally complete

[ ] First-week post-launch observations captured

Builder's Log

[x] April 30, 2026 entry written (Stage 0 day, ~205 lines, contemporaneous voice)

[ ] April 30 entry closed with final Stage 0 conditions verified

[ ] Subsequent daily/per-stage entries added as deployment progresses

Synthesis Phase

[ ] All evidence consolidated into /anchor_case_study/ folder

[ ] First-pass synthesis with Claude complete

[ ] Format decision made

[ ] Draft written

[ ] Honest critique pass complete

[ ] Distribution decision made

[ ] Published or filed as private asset

Closing Note

The deployment plan said "the fastest way to a clean production deploy is to refuse to compress steps." The same applies here. The fastest way to a clean case study is to refuse to write it before the deployment is done.

Right now: ship V3 to production. Capture evidence as you go. The case study writes itself when the timeline closes.

The work is the answer. The case study is the demonstration. The deployment is what makes both real.
