---
title: "Build Brief"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/#Neskala/Build Brief.docx"
status: reference
privacy: working
tags:
  - product
---

# Build Brief

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Build Brief  ·  Pin this at the top of every Replit session.

From Marcus's Serious Build Checklist, Section 8. One page. Read it before opening Cursor.

PROJECT META

Project name

Neskala (working title — final name TBD by Yuni)

Mode

Pilot — real users, real money, real safety stakes

Credit cap

$200 USD Replit + $100 USD Claude API for week-one build (hard stop $400)

Session timebox

1-week build sprint, then 30-day field validation

Stop condition

20 booking requests / 10–15 paid sessions / Net IDR/min trending toward Rp 3k by week 4 — OR safety incident, OR Yuni draining

Build sequence

Full vertical slice end-to-end days 1–2, then safety + capture days 3–4, then polish days 5–7

USER & PROBLEM

Primary user (V0)

Track A: English-speaking Ubud villa/guesthouse guest, 24–72 hr booking window

Problem

Tourist can't tell which Bali therapist or healer fits what they actually need today

Current workaround

Google (40 useless results) → hotel spa or random Klook booking, low trust

Why now

AI changed expectations; Bali supply is dense + underdistributed; trust is the bottleneck

SMALLEST VALUABLE LOOP

Input

QR scan → conversational intake (free text, AI parses state)

Transformation

Safety classifier → hard filters → semantic match → 2-sentence explanation per match

Output

3 provider cards with availability marked PROVISIONAL; CTA to request booking

Next human action

Yuni confirms availability via WhatsApp, then customer-confirms, then session happens

Smallest visible win

Customer reads match explanation and feels: “someone got it”

AI ROLE & SAFETY

AI role

Classify (safety) → filter (hard rules) → rank (within filtered pool) → explain

AI never decides

Safety. Medical fit. Booking confirmation. Refunds. Provider tier promotions.

Human approval required for

Any safety classifier flag, all match overrides, all incident escalations, all premium tier bookings in V0

Fallback when AI uncertain

Route to human-only review; customer sees “one of our team will reach out within an hour”

Kill-switch triggers

13 categories — pregnancy, surgery, chest pain, dizziness, severe pain, injury, BP, medication, intoxication, trauma, self-harm, minors, “I need medical help”

DATA & NO-GO SCOPE

Sensitive data collected

Emotional state text (raw, 30-day retention), body areas, pregnancy/injury flags, location, contact

Sensitive data NOT collected

Star sign, full medical history, payment card data, identity documents beyond provider KTP

Retention

Raw intake 30 days → summarize-or-delete; structured anonymized data persists; deletion on request within 7 days

No-go scope (V0)

No on-demand same-hour booking; no medical/therapy claims; no payment custody; no provider self-serve calendar; no instant book; no public reviews; no Spirit vertical; no minors

STACK & ARCHITECTURE

Frontend

Mobile-first web (no native app), Next.js + Tailwind, deployed Vercel or Replit

Backend

Postgres (Supabase or Replit), single Claude API call for intake-to-match, Whisper for Yuni voice memos

Database tables

providers, provider_services, customer_intakes, safety_audit_log, match_results, booking_requests, booking_status_events, referral_partners, provider_feedback, customer_feedback, commissions, ops_time_log, voice_memos

Anti-pattern

NO multi-agent frameworks (CrewAI/AutoGen). NO vector embeddings yet. NO real-time anything. Boring stack wins.

TEST PLAN

Five happy paths

(1) Tourist Track A villa booking; (2) Nomad Track B repeat; (3) Resident Track C referral; (4) Premium couples; (5) Healer single session

Ten edge cases

Provider unavailable mid-confirm; customer goes silent post-match; double-booking; language mismatch; payment confusion; customer changes timing; late-night request; out-of-area; sexual-services request (auto-ban); Yuni offline

Smoke test

Daily during build week: full QR-scan-to-confirmed-booking dry run by Marcus + fake voice-memo-to-DB by Yuni. Both must pass before EOD.

Mobile QA

iPhone Safari + Android Chrome, both must work end-to-end before week-1 close

LAUNCH & OPS

First 10 users path

Yuni's existing therapist network → 5 villa partners → QR cards at reception → Track A inbound

One-sentence offer

Tell us how you feel. We'll match you with the right person in Bali.

Frictionless onboarding step

QR scan → first intake question must load <2s on mobile; no signup required

Ops owner

Yuni (booking coordination, provider WhatsApp, partner relationships); Marcus (system, AI, weekly review)

Issue log

Single Notion / Linear board; one ticket per issue; no carrying things in head

PRE-FIRST-BOOKING SAFETY GATE

Booking #1 cannot happen until ALL of these are checked:

☐ Provider agreement signed   ☐ Customer ToS displayed   ☐ No-sexual-services policy visible   ☐ Cancellation/refund policy visible   ☐ AI safety classifier kill-switch tested across all 13 categories   ☐ Pregnancy/injury routes to human review   ☐ Provider has ID + reference verified   ☐ Provider tier assigned (Tier 1 only for V0)   ☐ Customer sees provider-safe summary (NOT raw intake)   ☐ Yuni has incident response script saved   ☐ Provider WhatsApp check-in/check-out tested   ☐ Customer behavior policy documented   ☐ Audit log writes confirmed working   ☐ End-to-end dry run completed (Marcus + Yuni as fake customer + fake provider)   ☐ Booking state machine tested through happy path + 2 cancellation paths

POST-BUILD REVIEW

Review date

End of week 1 (build) + end of week 4 (sprint) — both scheduled before starting

What shipped vs. spec

(fill in)

What broke

(fill in)

What surprised us

(fill in — capture customer quotes verbatim)

Reusable component / pattern

(fill in — AI safety classifier, voice-memo capture, archetype vocab, state machine)

The principle:

Architect for the future. Operate manually until reality earns automation. Calendar-backed, not calendar-automated. The app is the recruiting pitch. Yuni is the truth layer. The dataset is the moat that compounds. Spend to learn, validate, and ship — not to chase an undefined feeling of completion.

If a question can't be answered from this brief, the next move is discovery, not implementation.

Build Brief v1  ·  Companion to Neskala v6.3  ·  Per Marcus's Serious Build Checklist
