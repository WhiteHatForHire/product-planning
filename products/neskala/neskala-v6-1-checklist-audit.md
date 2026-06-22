---
title: "Neskala v6 1 Checklist Audit"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/#Neskala/Neskala v6 1 Checklist Audit.docx"
status: reference
privacy: public-candidate
tags:
  - product
---

# Neskala v6 1 Checklist Audit

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
NESKALA v6.1 vs. The Serious Build Checklist

How does the build hold up against your own guardrails?

Audit document  ·  April 2026

✓  PASS

Clearly addressed

!  PARTIAL

Partial / needs work

✗  GAP

Gap or not yet done

Executive Summary

Scorecard total: 17/20 — Build or pilot. Keep the scope tight.

Neskala v6.1 passes the Serious Build Checklist comfortably. The doc has a real user, a bounded V0, an AI safety boundary, an ops owner (Yuni), a budget cap mindset, and a stop condition. The three areas where it scores 1 instead of 2 are: technical feasibility (not yet shipped, can't verify), distribution (path is named but not yet tested), and operations (Yuni is named but the system depends heavily on her).

There are also five tactical gaps the v6.1 doc doesn't yet specify — they belong in a separate one-page build brief, not in the vision doc itself. Those are listed at the end with concrete fill-in suggestions.

Headline read

What's strong: user clarity, scope discipline, AI safety architecture, no-go scope, role separation, kill-fee, post-build review structure (the 30-day sprint criteria are essentially a Gate 10 review baked into the doc).

What's a gap: explicit credit cap (Replit/AI spend limit per session), explicit smoke test definition, written-down happy paths and edge cases, the actual one-page build brief from Section 8 of your checklist (which doesn't yet exist as a separate artifact).

What's a danger zone: Yuni is the ops layer for everything in V0. The capture system in Part 18 mitigates the SPOF risk for provider data, but doesn't mitigate the SPOF risk for daily booking coordination. If Yuni is sick for three days, the system halts. This is acknowledged in v6.1 but not mechanically solved.

§2 — What Counts as a Serious Build

Test: does Neskala qualify as a Serious Build that warrants the full checklist?

•

Question

Where this lives in v6.1 (or doesn't)

✓

A real person will use it

Sarah's Wednesday narrative names the exact user persona. Three customer tracks (tourist, nomad, resident) each with concrete profiles.

✓

A client, partner, or local operator will depend on it

Yuni is the local operator. Villa partners depend on the system not embarrassing them. Providers depend on lead quality.

✓

It may create or influence revenue

Direct booking commission, villa referral splits, FX rails (V2+). Real money.

✓

Stores private/personal/health-adjacent/payment data

Customer emotional state, body location of tension, pregnancy/injury flags, location, contact. Squarely in the high-care zone.

✓

Gives advice, matches people, routes opportunities, makes recommendations

Core function of the product. This is exactly the high-care category.

✓

Affects Marcus's public reputation as builder/founder/fCTO

Marcus-only Appendix A explicitly names this as the NYC builder narrative case study.

Verdict: This is unambiguously a Production/Pilot Build. Every checkbox is yes. The full Serious Build checklist applies.

§3 — The Ten Gates

Gate 0: Mode and Motive

•

Question

Where this lives in v6.1 (or doesn't)

✓

What mode am I in: Exploration, Integration, Build, or Arena?

Build mode (V0 sprint). The Letter to Yuni explicitly contrasts this with the franchise (Arena/Build distortion).

✓

Am I building from clarity, or from urgency/avoidance?

The Letter to Yuni names this exact failure mode ("shadow operator gravity") and explicitly designs against it.

✓

Practice, pilot, or production?

Pilot. 30-day validation sprint with go/stop criteria. Not pretending it's production.

!

What does a clean stopping point look like in 72 hours?

30-day stop criteria are clear (Part 21). 72-hour mid-sprint stopping points are NOT defined. Add weekly checkpoints to the build brief.

✓

What would I regret not bounding before I start?

Kill-fee for Yuni, no equity during trial, no payment custody V0, AI safety kill-switch list — all bounded explicitly.

Gate 1: User, Problem, and Outcome

•

Question

Where this lives in v6.1 (or doesn't)

✓

Who is the exact user?

Sarah, 34, Melbourne, day 4 of an 8-day Ubud yoga retreat. Plus Track B nomad and Track C resident profiles.

✓

Painful, repeated, expensive, confusing, or emotionally charged problem?

Discovery anxiety + trust deficit + state-not-service mismatch. Sarah's Wednesday opens with exactly this.

✓

What do they do today without this tool?

Google (40 results, none mean anything), Klook (cheap, generic, scary), hotel spas (impersonal). Named explicitly in Sarah's Wednesday.

✓

What does success look like after one use?

Single-sentence customer quote captured: "It felt like she knew exactly what I needed." Named as the unit of marketing copy in Part 21.

✓

What would make them tell another person about it?

Explicit goal: "By Sunday afternoon she texts the WhatsApp number with a referral for her friend Anna." Word-of-mouth is the V1 distribution thesis.

Gate 2: Smallest Valuable Loop

•

Question

Where this lives in v6.1 (or doesn't)

✓

What is the smallest useful version?

QR scan → conversational intake → 3 matches with explanations → WhatsApp confirmation → cash to provider → feedback. Defined in Part 19.

✓

Input, transformation, output, next human action?

Input (free-text intake) → Transformation (Claude classifies + ranks) → Output (3 cards with explanations) → Next action (customer chooses + Yuni confirms).

!

Can the core loop work manually before automation?

Yes — V0 is supervised AI with manual override. BUT: v6.1 explicitly chose to ship the prototype before manual. This is a deliberate inversion of the checklist's standard advice. Worth flagging as a conscious choice.

✓

What features are explicitly out of scope for V1?

Strong no-go list: not on-demand, not medical, not retreat marketplace, not review site, not native app, not payment custody, not Spirit vertical.

✓

What is the smallest visible win the user can feel?

Reading the match explanation and feeling "someone got it." That moment is the entire product.

Gate 3: Data and Trust

•

Question

Where this lives in v6.1 (or doesn't)

✓

What data is collected?

Schema in Part 16: customer_intakes table lists every field. Audit log captures classifier decisions.

✓

What data is truly necessary?

Data minimization explicitly stated in Part 10: "Collect only what is needed for matching."

✓

What data should never be collected in V1?

Astrology de-emphasized. No medical diagnostic data. No emotional intake stored indefinitely.

!

Where is the data stored?

"Postgres in Replit/Supabase" mentioned in Part 16 build sequence — but the actual hosting decision, encryption-at-rest, backup strategy, and data residency are NOT specified. Indonesian PDP law is named in Part 17 but not yet operationalized.

✓

How can a user delete, correct, or avoid sharing sensitive info?

"Customers can request deletion of intake history at any time" (Part 10). Consent-to-share intake design separates private text from provider-safe summary.

Gate 4: AI Role and Safety Boundary

•

Question

Where this lives in v6.1 (or doesn't)

✓

Is the AI classifying, matching, drafting, summarizing, coaching, recommending, or routing?

Classifying (safety), filtering (hard rules), ranking (matching), generating (explanations). All explicit.

✓

Where can AI be wrong without serious harm?

Soft ranking is fine to be wrong — three matches give the customer choice and the AI is ranking, not deciding.

✓

Where must a human approve before action is taken?

Any safety classifier flag → human-only review. Marcus/Yuni can override any match in V0 (supervised matching with human override).

✓

What should the AI never claim?

Part 10 "Language to use and avoid" table is explicit: never medical, never cure, never AI diagnosis. AI never decides safety — only ranks within pre-filtered safe pool.

✓

Fallback when AI is uncertain, unsafe, or out of scope?

Kill-switch list in Part 10 routes 13 categories to human-only review with explicit user message. Best-in-class.

Gate 5: Architecture and Implementation

•

Question

Where this lives in v6.1 (or doesn't)

✓

What stack is being used and why is it sufficient for V1?

Postgres (Replit/Supabase) + single Claude API call + mobile web. Explicitly rejected multi-agent frameworks. "Keep it boring" stated in Part 16.

✓

Database tables and required fields?

12 tables specified in Part 16 with key fields each. providers, customer_intakes, safety_audit_log, etc.

✗

API keys, environment variables, and secrets needed?

NOT IN THE DOC. Belongs in build brief, not vision doc. Need: Claude API key, Whisper API key, Postgres connection, WhatsApp Business API or fallback, Vercel/Replit deployment secrets.

✗

What happens when an API fails?

NOT IN THE DOC. If Claude API is down mid-intake, what does the customer see? If Postgres write fails after a booking is confirmed, what's the recovery path? Add explicit failure modes to build brief.

!

Logs, admin views, error states needed to debug?

Audit log is specified for safety pipeline. Admin dashboard for Yuni is named. But generic application error logging, alerting, and debug views are not specified.

Gate 6: Test Plan and Verification

•

Question

Where this lives in v6.1 (or doesn't)

✗

What are the five happy paths?

NOT EXPLICITLY LISTED. Implied by Sarah's Wednesday + first-20 playbook, but not formalized. Add to build brief: tourist QR scan, nomad recurring booking, resident referral, premium couples, healer booking.

✗

What are the ten obvious edge cases?

NOT LISTED. AI safety classifier covers ~13 medical edge cases — but product edge cases (provider unavailable, customer changes mind, payment fails, customer goes silent, double-booking, language mismatch, late-night request, etc.) are not enumerated.

!

Empty, weird, hostile, duplicated, or incomplete inputs?

Hostile inputs partially covered by AI safety classifier. Empty/weird/duplicate inputs not specified. Build brief gap.

✓

Does the main flow work on mobile?

Mobile-web-first is non-negotiable in v6.1. "iPhone Safari and Android Chrome" QA explicitly required in Part 16 day 5–7.

✗

What smoke test should run after every meaningful change?

NOT SPECIFIED. Belongs in build brief. Suggested: full QR-scan-to-confirmed-booking dry run by Marcus + Yuni once per day during the build week.

Gate 7: Launch and Distribution

•

Question

Where this lives in v6.1 (or doesn't)

✓

How will the first 10 users find this?

Part 15 names 5 channels. Track A via villa/guesthouse QR. Track B via coworking + WhatsApp groups. Track C via community word-of-mouth.

✓

What exact message explains the offer in one sentence?

"Tell us how you feel. We'll match you with the right person in Bali." Plus full landing page copy in Part 11.

!

What onboarding step must be frictionless?

QR scan → first intake question is well-designed. But specific friction points (loading speed, language detection, location prompt, browser permissions) are not enumerated.

✓

Who handles questions, complaints, refunds, or confusion?

Yuni via WhatsApp. Refund policy explicit in Part 12. Incident response protocol in Part 10.

✓

What proof do we need before spending more credits?

30-day go/stop criteria in Part 21. Explicit thresholds before proceeding to Phase 1.

Gate 8: Operations and Ownership

•

Question

Where this lives in v6.1 (or doesn't)

✓

Who checks the system daily or weekly?

Yuni daily (booking coordination, feedback). Marcus weekly (review feedback, update provider weights, iterate).

!

Who handles manual exceptions?

Yuni for booking-level exceptions. Marcus for AI/system-level exceptions. But what happens when Yuni is sick/offline for 3+ days is acknowledged as a risk but not mechanically solved.

✗

Where do issues get logged?

NOT EXPLICIT. Audit log captures AI decisions. But customer complaints, provider issues, partner concerns, system bugs — no unified ticketing or issue log specified. Add to build brief.

✓

What needs a backup, export, or rollback path?

Data legacy clause in Part 20 names what stays with whom. But operational backup procedures (Postgres backups, voice memo audio retention) are not specified.

✓

What recurring work does this create after launch?

Yuni's ops time is tracked per booking (Net IDR/ops-min). Ramp from 60 min/booking week 1 to ~20 min/booking week 4 is the explicit trajectory.

Gate 9: Budget, Timebox, Stop Condition

•

Question

Where this lives in v6.1 (or doesn't)

✗

What is the Replit or AI credit cap?

NOT SPECIFIED. The doc names Yuni's stipend (Rp 1.5–2m) and legal budget (Rp 5–10m for Month 2 lawyer) but does not cap Marcus's build spend. This is the single biggest checklist gap. Add explicit Replit credits + Claude API budget cap for the build week.

✓

What is the session timebox?

One-week build sprint stated in Part 16. 30-day validation sprint stated in Part 21.

✗

Allowed reasons to exceed the cap?

NOT SPECIFIED. Should be: only safety-related build-outs, only AI-safety-classifier hardening, never feature creep. Add to build brief.

✓

What result justifies another build pass?

Real go signal in Part 21: 20 requests, 10–15 completed, 70%+ match accuracy, etc. Explicit thresholds.

✓

What result means pause, kill, or simplify?

Stop criteria table in Part 21 names 8 explicit stop signals.

Gate 10: Post-Build Review

•

Question

Where this lives in v6.1 (or doesn't)

!

What shipped?

Will be answerable end of week 1. Not yet documented (the build hasn't happened).

!

What actually worked?

30-day sprint criteria define what counts as "worked."

!

What broke?

No formal post-build review template yet. Add to build brief.

!

What did users do that surprised us?

Customer feedback form captures "In one sentence, how did this match feel?" — but a structured "surprises log" is not part of the doc.

✓

What reusable component, prompt, schema, or pattern did this create?

Marcus-only appendix explicitly tracks this for the NYC narrative. The Yuni capture system, AI safety classifier pattern, and provider archetype vocabulary are all explicitly designed as reusable.

§4 — Red Flags and Green Flags

Red Flags — pause or shrink the build if these are true

•

Question

Where this lives in v6.1 (or doesn't)

✓

User is vague (tourists, businesses, everyone, creators, healers, founders)

User is specific and sharply named. Sarah's Wednesday is the protagonist. Three named tracks each with profiles.

!

App needs a two-sided marketplace before manual version has worked

Two-sided marketplace IS V0. v6.1 explicitly chose build-first over manual-first. This is a deliberate inversion of the checklist's default — flagged as a conscious choice but worth re-examining if prototype doesn't recruit providers.

✓

AI is expected to act autonomously in high-trust situation

Hard NO. AI safety classifier + human override + 13-category kill-switch list. The AI never makes safety decisions.

✓

System collects sensitive info without clear reason

Data minimization explicit. Consent-to-share design. Astrology de-emphasized.

✓

Feature list keeps growing before core loop is proven

Aggressive deferral: Spirit vertical Phase 2, Concierge Phase 3, expansion hubs after Bali proven, payment custody V2+.

✓

No path to first 10 users

5 named acquisition channels with specific tactics per track.

!

No budget cap or timebox

Timebox yes (1 week build, 30 days validation). Credit cap NO. This is a real gap.

✓

"We can monetize later" doing too much work

Day-1 commissions on Track A. Pricing tiers explicit. Real money from booking one.

✓

Build avoiding hard conversation, rest need, or simpler business task

The Letter to Yuni and "shadow operator gravity" framing show explicit awareness. Cashflow concierge framing acknowledges this isn't venture-scale yet.

Green Flags — proceed if these are true

•

Question

Where this lives in v6.1 (or doesn't)

!

A manual or concierge version can work before full automation

Yes in principle. v6.1 deliberately chose to ship the app first as the recruiting tool. Checklist's standard advice was to validate manually first; founder chose to invert.

✓

First 10 users can be named, reached, or recruited directly

Yuni's existing relationships + named partner channels. Within a week of launch, first users are reachable.

✓

System creates immediate benefit even if it never becomes huge company

Direct customer benefit (find the right massage). Provider benefit (foreign card payments, distribution). Local business benefit (referral fees). Wins independent of scale.

✓

AI role is bounded and explainable

Safety classifier + ranker + explanation generator. Never decision-maker.

✓

No-go list is clear

Five-section no-go list in Part 5 IS NOT table. Plus AI safety kill-switch. Plus Phase 2/3 deferrals.

!

Budget and stop condition written down before build begins

Stop condition: yes. Budget: stipend yes, AI/Replit credit cap NO.

✓

Build creates reusable infrastructure for future products

AI safety classifier pattern, Yuni capture system, provider graph schema, archetype vocabulary, NYC narrative case study — all designed as reusable.

✓

Every human contributor has defined role, compensation path, or learning agreement

Marcus / Yuni roles explicit. Staged compensation. Kill-fee. Equity ladder. Data legacy clause. Full set.

§5 — Scorecard (0-2 per dimension)

Dimension

Question

Score

Notes

Real user

A specific person or group can be named

2

Sarah, 34, Melbourne. Three named tracks. Best in class.

Pain clarity

Problem is urgent, repeated, or costly enough to matter

2

Discovery anxiety + trust deficit + state-not-service mismatch is a real and chronic pain.

Small loop

Core action can be completed without a full marketplace

2

QR → intake → 3 matches → WhatsApp → cash. Loop is small and complete.

Data safety

Sensitive data minimized, protected, and explained

2

Data minimization, consent-to-share, audit log, deletion rights. PDP scoping deferred to Month 2 lawyer.

AI safety

AI role bounded, fallbacks defined, humans approve risky actions

2

13-category kill-switch, supervised matching, pipeline architecture, audit log. Strongest section in v6.1.

Tech feasibility

Stack, schema, APIs, failure modes realistic for V1

1

Stack is realistic. Schema is detailed. But API failure modes and error handling are not specified yet.

Distribution

Believable path to first 10 users

1

Path is named (5 channels). Path is not yet tested. Villa partner economics still need real-world testing.

Operations

Someone owns support, quality control, manual edge cases

1

Yuni owns it. Yuni is also the SPOF. Capture system mitigates data SPOF, not ops SPOF.

Budget

Credit cap, timebox, and stop condition set

1

Timebox and stop condition: yes. Replit/AI credit cap for build week: NO. Single biggest checklist gap.

Learning value

Even if it fails, build produces reusable skill or infrastructure

2

AI safety pattern, voice-memo capture, schema, archetype vocab, NYC case study. Reusable across future builds.

TOTAL

17/20

Build or pilot. Keep scope tight.

17/20 — Build or pilot. Keep the scope tight.

Above the 16-threshold cleanly. Three dimensions score 1: tech feasibility (because nothing has been built yet — this scores up once the prototype runs), distribution (because no real users have tested it yet — this scores up after first 5 villa partner pitches), and operations + budget (which need explicit fill-in to bring to 2).

§6 — Bali Wellness Connector Validation Targets

Your checklist's own example section listed 6 validation targets for this exact business. Here's how v6.1 maps:

•

Question

Where this lives in v6.1 (or doesn't)

!

Recruit 20 credible providers

v6.1 targets 10 approved (Provider Acquisition Funnel: 40 leads → 10 approved). The checklist target is 20. Worth re-examining whether 10 is enough to test matching across archetypes.

✓

Simple provider profile database with categories, location, availability, price, language, quality notes

Schema in Part 16 covers all of these and more. archetypes[], modalities[], languages[], english_level, price_range, availability_notes.

✓

Match 10 real customers or serious inquiries

20 booking requests is the v6.1 "real go signal." Exceeds the checklist's 10.

✓

Complete at least 3 bookings or strong proofs of demand

10–15 completed paid sessions is the v6.1 target. Exceeds the checklist's 3.

✓

Collect feedback from both sides within 24 hours

Private feedback form sent 30 minutes post-session (customer). Provider feedback collected per booking. Within 24h easily.

✓

Decide after pilot whether to continue, simplify, niche down, or kill

Part 21 stop criteria + go criteria. Phase 1/2/3 progression is explicit.

§7 — What's Missing (and Where to Put It)

Five concrete gaps. None are fatal. None belong in the vision doc itself — they belong in a separate one-page Build Brief (your checklist's Section 8).

Gap 1: Replit and Claude API credit cap for build week

Suggested: $200 USD Replit credit cap, $100 Claude API cap for week-one build. Hard stop at $400 combined; if exceeded, scope is wrong.

Gap 2: API failure modes

If Claude API errors mid-intake → fall back to a 3-question form, log the failure. If Postgres write fails after booking confirmation → Yuni gets WhatsApp alert with intake data. If Whisper transcription fails on Yuni voice memo → audio is preserved, manual transcription queued.

Gap 3: Five happy paths and ten edge cases

Happy paths: Track A tourist single booking, Track B nomad rebooking, Track C resident first booking, premium couples, healer booking. Edge cases: provider unavailable mid-confirmation, customer goes silent post-match, language mismatch, double-booking, payment confusion, customer changes timing, late-night request, customer outside service area, customer asks for sexual services (auto-ban + log), Yuni offline.

Gap 4: Smoke test definition

Daily during build week: Marcus runs full QR-scan-to-confirmed-booking with a fake customer profile and a fake provider. Yuni runs full voice-memo-to-database with a fake provider interview. Both must pass before end of day.

Gap 5: One-page build brief

Section 8 of your checklist literally specifies a one-page copy-paste brief. v6.1 doesn't yet have one — the vision doc is too long to serve as the daily reference. Recommend producing it as a sibling artifact: "Neskala Build Brief v0.1" — a single page Marcus pins at the top of every Replit session.

§8 — Final Verdict

v6.1 passes the Serious Build Checklist at 17/20. Build or pilot, keep scope tight, fill the 5 gaps in a separate build brief.

The doc is a vision document, not a build brief. It does its job — it defines the user, the wedge, the moat, the safety boundaries, the operational owner, the kill-fee, and the stop conditions. It is genuinely strong on user clarity, AI safety, and scope discipline.

What's missing is operational granularity (credit cap, smoke test, edge cases, failure modes). These are not vision-doc-shaped questions. They are build-brief questions. The right next artifact is not a v6.2 — it is a one-page Build Brief that sits next to v6.1 as the daily working document.

The single most important checklist item to address before opening Replit on day 1:

Set the credit cap. Write it down. Tape it to your monitor. Spend to learn, validate, and ship — not to chase an undefined feeling of completion.

Audit complete  ·  v6.1 vs. Serious Build Checklist  ·  April 2026
