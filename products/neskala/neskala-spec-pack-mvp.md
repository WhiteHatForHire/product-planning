---
title: "# Neskala Spec Pack — MVP"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/#Neskala/MVP build /# Neskala Spec Pack — MVP.docx"
status: reference
privacy: working
tags:
  - product
---

# # Neskala Spec Pack — MVP

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Index.md

# Neskala Spec Pack — Index

**Purpose:** Single entry point for every agent (human or AI) working on Neskala. Read this first. It tells you where to go next based on what you’re trying to do.

**Status:** V0 build, pre-first-booking. Field-ready target: end of Day 7.

**Doctrine in one line:** Replit owns visible product. Claude Code owns safety-critical code. Codex owns repo-wide verification. Manual ops until reality earns automation.

-----

## The 11 documents

|# |File                 |Owner of source-of-truth|Read when                                   |

|--|---------------------|------------------------|--------------------------------------------|

|1 |`SPEC_INDEX.md`      |This doc — Marcus       |Always first                                |

|2 |`README.md`          |Marcus                  |Onboarding to repo                          |

|3 |`AGENTS.md`          |Marcus                  |Before any agent session                    |

|4 |`BUILD_BRIEF.md`     |Marcus                  |Pinned at top of every session              |

|5 |`MVP_SPEC.md`        |Marcus                  |Implementing customer/admin features        |

|6 |`AI_CONTRACTS.md`    |Claude Code             |Touching any AI call                        |

|7 |`DATABASE_SCHEMA.md` |Claude Code             |Touching schema or migrations               |

|8 |`SAFETY_AND_TRUST.md`|Claude Code             |Touching classifier, audit log, or ToS gates|

|9 |`OPS_PLAYBOOK.md`    |Yuni / Marcus           |Yuni’s manual workflows                     |

|10|`TEST_PLAN.md`       |Codex                   |Writing or running tests                    |

|11|`POST_MVP_ROADMAP.md`|Marcus                  |Anything not in V0                          |

Source-of-truth means: if the code disagrees with the doc, the doc wins until Marcus updates it.

-----

## Agent ownership map

### Replit Agent owns

The visible product. Components, pages, styling, mobile responsiveness.

- Landing page (`/`) and QR target route

- Customer intake UI (textarea, Whisper microphone button, follow-up questions)

- Match card display (`/match/:intake_id`)

- Booking request form

- Customer feedback form (post-session)

- Admin dashboard pages (provider list, booking queue, intake review)

- Admin provider profile create/edit form

- Admin “structure raw text into provider fields” Claude button

- WhatsApp message copy buttons in admin

- Mobile QA (iPhone Safari + Android Chrome)

- Tailwind styling, empty states, error states

**What Replit Agent does not touch:** anything in the safety-critical list below. If a Replit prompt would require modifying classifier code, AI contracts, audit log writers, or state machine transitions, stop and route to Claude Code.

### Claude Code owns

The invisible product. Safety-critical code where silent breakage is the failure mode.

- AI safety classifier (`src/ai/classifier.ts`) and its eval harness

- AI contracts layer (request/response schemas for every Claude call)

- Match generator + explanation generator

- Provider-safe summary generator (separate from raw intake display)

- Audit log writers (every state change writes to `safety_audit_log` and `booking_status_events`)

- Booking state machine with DB-enforced transitions

- Whisper transcription handler (with fallback to text input on failure)

When Claude Code edits any of these files, it must run the relevant eval/test suite before committing.

### Codex Cloud owns

Repo-wide verification. Things that cross file boundaries.

- Schema migrations (drafted by Claude Code, verified and applied by Codex)

- Playwright smoke tests across the full stack

- Daily smoke test runner (cron or GitHub Action)

- Security audits before pre-first-booking gate sign-off

- `BUG_MATRIX.md` and `PRE_FIRST_BOOKING_GATE.md` generation

### Marcus owns

Strategy, scope, the gate itself.

- Updating any spec doc (agents propose, Marcus approves)

- Pre-first-booking gate sign-off

- Stop conditions and budget overrides

- The list of things explicitly excluded from V0

### Yuni owns

Field operations. Ground truth for what providers and partners actually want.

- Provider interview script and structured field entry

- WhatsApp confirmation flow

- Villa partner pitch and onboarding

- Incident response (with Marcus on call)

- The provider bench composition (Part 8 of v6.3)

-----

## Task-to-doc routing

|If you’re trying to…             |Read first                                                            |

|---------------------------------|----------------------------------------------------------------------|

|Add a customer-facing feature    |`MVP_SPEC.md` → `BUILD_BRIEF.md`                                      |

|Touch any AI call                |`AI_CONTRACTS.md` → `SAFETY_AND_TRUST.md`                             |

|Add or alter a DB table/field    |`DATABASE_SCHEMA.md` → `MVP_SPEC.md`                                  |

|Modify the safety classifier     |`SAFETY_AND_TRUST.md` → `TEST_PLAN.md`                                |

|Change a booking state transition|`DATABASE_SCHEMA.md` (state machine section) → `SAFETY_AND_TRUST.md`  |

|Write a test                     |`TEST_PLAN.md`                                                        |

|Set up Yuni’s manual workflow    |`OPS_PLAYBOOK.md`                                                     |

|Decide if something is V0        |`MVP_SPEC.md` “In scope” section + `POST_MVP_ROADMAP.md` deferred list|

|Suggest a feature not in V0      |`POST_MVP_ROADMAP.md` first; if not there, ask Marcus                 |

-----

## The non-negotiable rules

These are repeated in `AGENTS.md` but listed here so they hit you on first read:

1. **V0 accepts text and Whisper-transcribed voice. No audio is stored.** Transcribe on receipt, write transcript to `customer_intakes.raw_intake_text`, discard audio.

1. **The AI never decides safety, medical fit, booking confirmation, refunds, or provider tier promotions.**

1. **The 13-category kill-switch must pass eval before any real customer booking.**

1. **GitHub is source of truth.** Replit pushes commits, doesn’t own state.

1. **No multi-agent frameworks. No vector embeddings. No real-time anything. Boring stack wins.**

1. **No payment custody.** V0 is cash/QRIS direct customer-to-provider.

1. **No public reviews, no star ratings, no provider self-serve calendar, no instant booking.**

1. **Every state change writes to the audit log. No try/catch silently swallowing audit failures.**

If a request from any human or agent conflicts with these rules, stop and surface the conflict to Marcus.

-----

## Build budget (Week 1)

- Replit credits: **$200 USD hard cap**

- Claude API: **$100 USD hard cap**

- Combined hard stop: **$400 USD**. If approaching, scope is wrong — stop and reassess, don’t raise the cap.

- Allowed reasons to exceed: safety classifier hardening only. Never feature creep.

-----

## Build sequence (high level)

|Day|Owner               |Output                                                                                                          |

|---|--------------------|----------------------------------------------------------------------------------------------------------------|

|1  |Marcus + Claude Code|Spec pack finalized, repo scaffolded, schema migrated, seed data                                                |

|2  |Replit Agent        |Vertical slice with mocked AI: QR → intake → 3 hardcoded matches → booking request → admin sees it              |

|3  |Claude Code         |Safety classifier + eval harness (50+ cases, all 13 kill-switch categories)                                     |

|4  |Claude Code + Replit|Real Claude API wired in, match + explanation generators, Whisper integration, admin “structure raw text” button|

|5  |Claude Code + Codex |Booking state machine with DB-enforced transitions, Playwright smoke tests                                      |

|6  |Marcus              |Pre-first-booking safety gate review, ops artifacts (ToS, agreements, scripts) finalized                        |

|7  |All                 |End-to-end dry run, mobile QA, sign-off or defer                                                                |

Detail in `BUILD_BRIEF.md`.

-----

*Last updated: Day 0. Source documents: Neskala v6.3 Vision, v6.1 Checklist Audit, Build Brief v1.*

Readme.md

# Neskala

*Tell us how you feel. We’ll match you with the right trusted practitioner in Bali.*

-----

## What this is

Neskala is an AI-matching layer for Bali wellness bookings. A guest scans a QR code at their villa, describes how their body and mind feel, and gets three vetted practitioners with a clear explanation of why each fits.

V0 is a supervised concierge experiment: AI matches, humans confirm. Yuni handles WhatsApp coordination. Customers pay providers directly. No payment custody, no instant booking, no autonomous safety decisions.

The wedge: Ubud villa and guesthouse referrals for English-speaking travelers seeking trusted in-villa bodywork within 24-72 hours.

Working title. Final name TBD by Yuni.

-----

## Status

**Phase:** V0 build, pre-first-booking.

**Target:** Field-ready by end of Day 7. First real customer booking after the safety gate clears.

**Build sprint:** 1 week. **Validation sprint:** 30 days following.

**Stop condition:** 20 booking requests / 10-15 paid sessions / Net IDR/min trending toward Rp 3k by week 4.

-----

## How to read this repo

Read `SPEC_INDEX.md` first. It’s the entry point and tells you which doc to read for what task.

Short version of the doc layout:

- `BUILD_BRIEF.md` — pin this every session

- `MVP_SPEC.md` — what V0 ships

- `AI_CONTRACTS.md` — every Claude call’s input/output schema

- `DATABASE_SCHEMA.md` — tables, enums, state machine

- `SAFETY_AND_TRUST.md` — kill-switch, audit log, ToS gates

- `OPS_PLAYBOOK.md` — Yuni’s manual workflows

- `TEST_PLAN.md` — happy paths, edge cases, classifier eval

- `POST_MVP_ROADMAP.md` — everything explicitly not built now

- `AGENTS.md` — permanent rules for AI agents

-----

## How to run it

*To be filled in after Day 1 scaffolding.*

```bash

# Expected commands:

pnpm install

pnpm db:migrate

pnpm db:seed

pnpm dev

```

Required env vars (see `.env.example`):

- `DATABASE_URL` — Postgres connection (Neon or Supabase)

- `ANTHROPIC_API_KEY` — Claude API

- `OPENAI_API_KEY` — Whisper only (cheaper than Claude voice)

- `SENTRY_DSN` — error tracking

- `ADMIN_PASSWORD` — single-password admin auth for V0

-----

## Stack

- **Frontend:** Next.js 14 (App Router) + Tailwind

- **Backend:** Next.js API routes

- **Database:** Postgres (Neon for V0, can move to Supabase if RLS becomes useful)

- **AI:** Claude API for intake parsing, matching, explanations, safety classification

- **Voice:** OpenAI Whisper API (transcription only, no audio storage)

- **Hosting:** Vercel

- **Error tracking:** Sentry

- **Auth:** No customer auth. Single-password admin auth.

- **Messaging:** Manual WhatsApp via copy-button workflow. No WhatsApp Business API in V0.

Why this stack: Marcus already has accounts on all of these (from Anchor) and the patterns are familiar. “Boring stack wins” per the build brief.

Why Neon over Supabase for V0: customer auth isn’t needed (QR scan = no login), so RLS isn’t doing meaningful work. Neon is simpler for this shape. If V1 needs RLS or auth, migration is straightforward.

-----

## Contributing

This is a solo build with AI agents. Workflow:

1. Read `SPEC_INDEX.md` to find the right doc for your task

1. Read `AGENTS.md` for the rules

1. Make the change in a branch

1. PR back to main

1. Marcus reviews and merges

Branch naming: `feat/`, `fix/`, `safety/`, `ops/`, `spec/` prefixes.

-----

## License

Private and confidential. Not yet open source. Eagle Rocket LLC.

Agents.md

# AGENTS.md

**Permanent rules for every AI agent working on Neskala.** Read this at the start of every session. These rules exist because Neskala sends people into private spaces in someone else’s villa. Silent breakage of safety code is the failure mode.

-----

## Identity

You are working on Neskala, an AI-matching layer for Bali wellness bookings. The product is in V0, pre-first-booking. A real customer will use this to book a real practitioner who will visit their villa. The stakes are real.

-----

## Your role depends on your name

**If you are Replit Agent:** You own the visible product. Customer pages, admin pages, components, styling, mobile responsiveness. You do not touch the safety classifier, AI contracts, audit log writers, state machine transitions, or DB migrations. If a request requires modifying any of those, stop and tell Marcus to route to Claude Code.

**If you are Claude Code:** You own safety-critical code. Classifier, AI contracts, audit log, state machine, Whisper handler, schema migrations. You always run the relevant test/eval suite before declaring a task done.

**If you are Codex Cloud:** You own repo-wide verification. Migrations, Playwright smoke tests, security audits, the daily smoke test runner. You do not write product features.

**If you are something else:** Ask Marcus.

-----

## The eight non-negotiable rules

### 1. V0 accepts text and Whisper-transcribed voice. Audio is never stored.

Customer intake supports either typed text or Whisper-transcribed voice. The transcript is written to `customer_intakes.raw_intake_text`. The audio file is discarded immediately after transcription completes. Do not add audio storage. Do not add audio retention. Do not write audio blobs to the database.

`input_source` enum tracks the input mode: `typed | whisper_voice | admin_entered | pasted_transcript`.

### 2. The AI never decides safety, medical fit, booking confirmation, refunds, or provider tier promotions.

The AI’s job is to classify (safety flags), filter (hard rules), rank (matching within filtered pool), and explain (two-sentence why-this-person). Every other decision is human.

If you are tempted to write code where the AI confirms a booking, approves a refund, promotes a provider tier, or makes a final safety call, stop. Route to a human-review queue instead.

### 3. The 13-category kill-switch must pass eval before any real customer booking.

The categories are listed in `SAFETY_AND_TRUST.md`. The eval harness is in `tests/safety-classifier-eval.test.ts`. Before any commit that touches the classifier, run the full eval. A single category failure blocks merge.

### 4. GitHub is source of truth.

Replit pushes commits; it does not own state. If Replit and GitHub disagree, GitHub wins. Pull from main at the start of every Replit session.

### 5. No multi-agent frameworks. No vector embeddings. No real-time anything. Boring stack wins.

If you find yourself reaching for CrewAI, AutoGen, LangGraph, vector DBs, websockets, server-sent events, or any “real-time” feature, stop. The reason for V0’s tight scope is that volume doesn’t justify the complexity. We add complexity when reality earns it.

### 6. No payment custody.

V0 is cash/QRIS direct customer-to-provider. Neskala does not hold money. Do not integrate Stripe, Midtrans, Xendit, or any payment processor in V0. Commission is recorded manually in the `commissions` table. V2 introduces deposits.

### 7. No public reviews, no star ratings, no provider self-serve calendar, no instant booking.

Private feedback only. Yuni confirms availability via WhatsApp. Match output says “availability to be confirmed.” A calendar that lies is worse than no calendar.

### 8. Every state change writes to the audit log. No try/catch silently swallowing audit failures.

Every transition in the booking state machine writes to `booking_status_events`. Every classifier decision writes to `safety_audit_log`. If an audit write fails, the operation fails — do not catch and continue. The audit log is the legal trail.

-----

## What you do not change without a spec update

If your task would require any of the following, stop and surface to Marcus before proceeding:

- The list of kill-switch categories

- The booking state machine states or allowed transitions

- The schema for `customer_intakes`, `safety_audit_log`, `booking_status_events`, `match_results`, `booking_requests`

- The AI contract input/output schemas in `AI_CONTRACTS.md`

- The MVP scope in `MVP_SPEC.md`

- The “explicitly not in V0” list in `POST_MVP_ROADMAP.md`

These are not arbitrary. They are gated by the pre-first-booking safety review. Changing them changes the gate.

-----

## How you handle uncertainty

If you are uncertain whether a feature is V0:

1. Check `MVP_SPEC.md` “in scope” section

1. Check `POST_MVP_ROADMAP.md` deferred list

1. If still unclear, ask Marcus. Do not assume.

If you are uncertain whether a behavior is safe:

1. Check `SAFETY_AND_TRUST.md`

1. Check `TEST_PLAN.md` edge cases

1. Default to routing to human review. The safety classifier kill-switch behavior is “when in doubt, route to human.”

If you are uncertain whether to write a test:

1. The answer is yes. Write the test.

-----

## Commit hygiene

- Branch prefixes: `feat/`, `fix/`, `safety/`, `ops/`, `spec/`, `test/`, `chore/`

- Conventional commit messages: `feat(intake): add Whisper microphone button`

- Never commit secrets. Use `.env.local`, not committed.

- Never commit fake API keys, even in tests. Use environment-variable-driven mocks.

- PRs require a passing CI run including the safety classifier eval.

- Squash-merge to main.

-----

## The budget cap

Week-one build:

- Replit: $200 USD

- Claude API: $100 USD

- Combined hard stop: $400 USD

If approaching the cap, you stop and surface to Marcus. The only allowed reason to exceed is safety classifier hardening. Never feature creep.

If you are an agent burning through credits regenerating the same component, stop and tell Marcus the regeneration is the symptom of unclear spec.

-----

## When things break

- API failure during intake: customer falls back to text input, error logged to Sentry, intake continues. Do not block the customer on Whisper or Claude API outages.

- Postgres write failure after booking confirmation: alert Yuni via configured channel (initially email; WhatsApp later), do not silently lose the booking.

- Whisper failure: UI shows “voice unavailable, please type.” Logged to Sentry.

- Audit log write failure: the originating operation fails. Do not continue with a partial state change.

-----

## What you never do

- Roleplay as a human. You are an AI agent. Marcus knows.

- Tell Marcus a feature is “production-ready” if the safety classifier eval has not run.

- Use em-dashes in user-facing copy. Marcus’s voice does not use them. Long-dashes only in code comments where they’re load-bearing.

- Generate fake data that could be confused for real provider info. Seed data uses obviously fake names (“Test Provider 1”) not plausible Indonesian names.

- Hardcode API keys. Ever. Anywhere. Including throwaway tests.

- Make the code “more robust” by catching and swallowing errors. Errors are signal.

-----

*This document is the load-bearing constraint set. If you find yourself wanting to argue with it, surface the disagreement to Marcus before acting.*

Build_brief.md

# BUILD_BRIEF.md

*Pin this at the top of every Replit, Claude Code, or Codex session. One screen. Read it before opening the editor.*

-----

## Project meta

|                     |                                                                                                                              |

|---------------------|------------------------------------------------------------------------------------------------------------------------------|

|**Name**             |Neskala (working title — Yuni decides final)                                                                                  |

|**Mode**             |Pilot — real users, real money, real safety stakes                                                                            |

|**Phase**            |V0 build, pre-first-booking                                                                                                   |

|**Build sprint**     |1 week (Days 1-7)                                                                                                             |

|**Validation sprint**|30 days following                                                                                                             |

|**Stop condition**   |20 booking requests / 10-15 paid sessions / Net IDR/min trending toward Rp 3k by week 4. Or safety incident. Or Yuni draining.|

-----

## Budget cap

|                      |                                                      |

|----------------------|------------------------------------------------------|

|**Replit credits**    |$200 USD hard cap                                     |

|**Claude API**        |$100 USD hard cap                                     |

|**Combined hard stop**|$400 USD. If approaching, scope is wrong.             |

|**Allowed exceptions**|Safety classifier hardening only. Never feature creep.|

-----

## User & problem

|                      |                                                                                         |

|----------------------|-----------------------------------------------------------------------------------------|

|**Primary user (V0)** |Track A: English-speaking Ubud villa/guesthouse guest, 24-72hr booking window            |

|**Problem**           |Tourist can’t tell which Bali therapist or healer fits what they actually need today     |

|**Current workaround**|Google → 40 useless results → hotel spa or Klook, low trust                              |

|**Why now**           |AI changed expectations; Bali supply is dense + underdistributed; trust is the bottleneck|

-----

## Smallest valuable loop

QR scan → conversational intake (text or voice) → safety classifier → hard filters → semantic match → 3 provider cards with explanations and “availability to be confirmed” → booking request → Yuni confirms via WhatsApp → session happens → customer pays provider direct → feedback.

The smallest visible win: customer reads match explanation and feels “someone got it.”

-----

## AI role

The AI:

- **Classifies** safety flags (kill-switch routing)

- **Filters** hard rules (availability window, gender, language, budget, certifications)

- **Ranks** within filtered pool (state, archetype, feedback weights)

- **Explains** in two sentences why this person fits

- **Summarizes** raw intake into provider-safe brief

The AI never:

- Decides safety, medical fit, booking confirmation, refunds, or provider tier promotions

- Confirms availability autonomously

- Acts on a kill-switch flag without routing to human review

Fallback when AI uncertain: route to human-only review. Customer sees “one of our team will reach out within an hour.”

-----

## 13-category kill-switch

Halts automated matching. Routes to human review.

1. Pregnancy (any trimester)

1. Recent surgery or stitches

1. Chest pain, heart conditions, shortness of breath

1. Dizziness, fainting, balance issues

1. Severe pain, numbness, tingling, fever

1. Acute injury (sprain, fracture, recent fall)

1. Blood pressure issues or blood thinners

1. Medication that affects bodywork

1. Intoxication signals

1. Trauma disclosure (PTSD, recent assault, abuse history)

1. Self-harm language or suicidal ideation

1. Anything involving minors

1. “I need medical help” or equivalent

Detail in `SAFETY_AND_TRUST.md`. Eval harness in `tests/safety-classifier-eval.test.ts`.

-----

## Data scope

**Collected:** raw intake text, body areas, pregnancy/injury flags, location, contact, customer feedback, provider feedback, ops time.

**Not collected:** star sign, full medical history, payment card data, identity documents (beyond provider KTP held by Yuni outside the app), session audio.

**Retention:** raw intake 30 days → summarize-or-delete. Structured anonymized data persists. Deletion on request within 7 days.

-----

## V0 no-go scope

- No customer auth (QR scan = no login)

- No on-demand same-hour booking

- No payment custody, no escrow, no Stripe/Midtrans/Xendit

- No provider self-serve calendar

- No instant book

- No public reviews or star ratings

- No native app

- No Spirit vertical

- No multi-language detection

- No villa partner dashboard

- No premium tier UI

- No multi-agent frameworks

- No vector embeddings

- No real-time anything

- No autonomous safety decisions

- No audio storage

If a request would require any of these, stop and surface to Marcus.

-----

## Stack

- Next.js 14 (App Router) + Tailwind

- Postgres (Neon)

- Claude API for intake parsing, matching, explanations, classifier

- Whisper (OpenAI) for voice transcription only — audio discarded after transcription

- Vercel for hosting

- Sentry for errors

- Manual WhatsApp via copy-button workflow

- Single-password admin auth

-----

## Build sequence

|Day|Owner               |Output                                                                                                                                                                                            |

|---|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|1  |Marcus + Claude Code|Spec pack final, repo scaffolded, schema migrated, 8 seed providers covering bench distribution                                                                                                   |

|2  |Replit Agent        |Vertical slice with mocked AI: QR → intake → 3 hardcoded match cards → booking request → admin sees it. Mobile QA on iPhone Safari.                                                               |

|3  |Claude Code         |Safety classifier + eval harness (50+ cases, all 13 kill-switch categories, both typed and dictation registers)                                                                                   |

|4  |Claude Code + Replit|Real Claude API wired in. Match generator, explanation generator, provider-safe summary generator. Whisper integration on customer intake. Admin “structure raw text into provider fields” button.|

|5  |Claude Code + Codex |Booking state machine with DB-enforced transitions. Audit log writers. Playwright smoke tests for 5 happy paths and 10 edge cases.                                                                |

|6  |Marcus              |Pre-first-booking safety gate review. Ops artifacts (provider agreement, customer ToS, no-sexual-services policy, incident response script) finalized.                                            |

|7  |All                 |End-to-end dry run. Marcus + Yuni as fake customer + fake provider. Full QR-to-confirmed-booking + cancellation paths. Mobile QA on Android Chrome. Sign-off or defer.                            |

-----

## Daily smoke test

Runs at end of every day during build week. All must pass before EOD.

1. Customer happy path: QR → intake (text) → 3 matches → booking request → admin sees it → status transition → customer feedback link.

1. Customer voice path: QR → Whisper voice intake → 3 matches → booking request.

1. Safety kill-switch: typed intake mentioning pregnancy → kill-switch fires → routed to human review queue → no match cards generated.

1. Yuni admin: provider profile create → seed booking request → manual override match → state transition to provider_confirmed → state transition to customer_confirmed.

1. Audit log: every state change above wrote to `booking_status_events` with timestamp, actor, reason. Classifier decisions wrote to `safety_audit_log` with flags, providers considered, hard filters applied, final match.

Detail in `TEST_PLAN.md`.

-----

## Pre-first-booking safety gate

Booking #1 cannot happen until **all** of these are checked. See `SAFETY_AND_TRUST.md` for detail.

- [ ] Provider agreement signed (paper or DocuSign, stored outside repo)

- [ ] Customer ToS displayed and acknowledged before intake

- [ ] No-sexual-services policy visible to both sides

- [ ] Cancellation/refund policy visible

- [ ] AI safety classifier eval passing on all 13 categories

- [ ] Pregnancy/injury route to human review verified end-to-end

- [ ] Provider has ID + reference verified (Yuni’s records)

- [ ] Provider tier assigned (Tier 1 only for V0)

- [ ] Customer sees provider-safe summary, not raw intake

- [ ] Yuni has incident response script saved on her phone

- [ ] Provider WhatsApp check-in/check-out tested

- [ ] Customer behavior policy documented

- [ ] Audit log writes confirmed working (smoke test 5)

- [ ] End-to-end dry run completed (Marcus + Yuni)

- [ ] Booking state machine tested through happy path + 2 cancellation paths

Marcus signs off in writing on the gate before Yuni books anyone.

-----

## The principle

> Architect for the future. Operate manually until reality earns automation. Calendar-backed, not calendar-automated. The app is the recruiting pitch. Yuni is the truth layer. The dataset is the moat that compounds. Spend to learn, validate, and ship — not to chase an undefined feeling of completion. If a question can’t be answered from this brief or its sibling docs, the next move is discovery, not implementation.

-----

*Build Brief v0.1 · Companion to Neskala v6.3 · Sized for daily agent consumption*

MVP_spec.md

# MVP_SPEC.md

**Source of truth for what V0 ships.** If a feature is not in this doc, it is not V0. If a request would add or remove something here, propose a spec update before implementing.

-----

## North star

Customer scans QR at villa → answers one question about how they feel → sees three matched practitioners with explanations → requests a booking → Yuni confirms via WhatsApp → session happens → customer pays provider direct → both parties leave feedback.

That is the full V0 loop. Everything else is post-MVP.

-----

## In scope

### Customer-facing pages

#### `/` — Landing page (QR target)

Single screen, mobile-first.

- Headline: “Feel sore, tired, or overstimulated? We’ll match you with a trusted Bali bodywork practitioner.”

- Subhead: “Tell us how your body and mind feel today. We’ll recommend three vetted local practitioners who fit your needs, your preferences, and your villa.”

- Trust row (six small icons + text):

- Personally vetted practitioners

- In-villa or in-area sessions

- WhatsApp confirmation before anyone arrives

- You choose gender preference

- Wellness only — never sexual services

- Cash or QRIS direct to provider

- Primary CTA: “Find my match →”

- Secondary link: “How it works” (scrolls to FAQ section)

Loads in under 2s on mobile. No login.

#### `/intake` — Conversational intake

Single open question, large textarea, voice-friendly.

- Prompt: “Rough day? Tell us how your body and mind are feeling right now.”

- Microphone button (Whisper) next to textarea. On tap: records audio, transcribes via Whisper, populates textarea with transcript, discards audio.

- Below textarea, hint text: “Or tap the mic to speak. Up to 90 seconds.”

- Submit button: “Continue”

After submit, AI parses and displays follow-up questions:

1. “Any areas, injuries, or health considerations we should know about before matching you?” (textarea, optional, voice-enabled)

1. “Gender preference, or happy with whoever’s the best match?” (radio: female / male / either / no preference)

1. “When — today, tomorrow, this week, or whenever you find the best match?” (radio: today / tomorrow / this week / flexible)

1. “Where are you staying, and what’s your budget range?” (location text, budget radio: Rp 350-500k / Rp 500-800k / Rp 800k+ / open)

1. Contact — “How can we reach you to confirm? WhatsApp number please.” (text input)

Optional: woo-level slider (practical only / open to intuition / spiritual / surprise me). Shown only after primary fields are filled.

If safety classifier flags during initial parse → skip follow-ups, show human-review screen (`/intake/review-pending`).

#### `/match/:intake_id` — Match results

Three cards. Each card shows:

- Provider photo (or initials if no photo yet)

- Provider name (first name + initial)

- Two-sentence explanation: “Wayan is matched to you because [state-specific reason]. She specialises in [modality] and is available [provisional window].”

- “Availability to be confirmed” badge

- “Request booking with [Name]” button

Below cards: “Or, you choose — let Yuni recommend after a quick chat” → opens manual-review request.

Footer: small “How matching works” link (modal explaining classifier + filter + rank + human confirm).

#### `/booking/:booking_id/pending` — Confirmation pending

After customer requests booking:

- “Got it. Yuni from our team will message you on WhatsApp within 30 minutes to confirm [Provider]’s availability. She’ll send a short brief about what to expect, the address she’s coming to, and how to pay (cash or QRIS, direct to her). If anything changes, message us back.”

- Booking summary

- Yuni’s WhatsApp number (clickable)

- Show provider-safe summary that Yuni will send to provider — *customer sees what the provider will see before booking*

#### `/intake/review-pending` — Human review fallback

When kill-switch fires.

- “Thanks — we want to match you safely. Our team will reach out within an hour.”

- Contact field if not yet collected

- No match cards shown

- No timeline pressure

#### `/feedback/:booking_id` — Customer feedback

Sent via WhatsApp link 30 minutes after session end time.

Counterfactual questions:

1. Did the match feel right for your state? (1-5)

1. Did the match explanation increase your trust in this booking? (yes / somewhat / no)

1. Would you have booked without the explanation? (yes / no / unsure)

1. Did the provider feel matched to your state? (yes / somewhat / no)

1. Would you have preferred browsing a list? (yes / no / unsure)

1. Open: “In one sentence, how did this match feel?” (textarea, optional)

1. Rebook intent (yes / maybe / no)

#### `/tos` and `/privacy` — Terms and privacy

Linked from intake before submission. Customer must acknowledge ToS before submitting intake.

ToS includes no-sexual-services policy in plain language at the top.

-----

### Admin-facing pages

Single-password auth. Yuni and Marcus share credentials in V0.

#### `/admin` — Dashboard

- Today’s booking requests (status: requested, provider_pending, provider_confirmed, customer_confirmed, completed)

- Today’s intakes flagged for human review

- This week’s stats: intakes started, intakes completed, match cards generated, bookings requested, bookings completed, revenue, avg Yuni minutes per booking, Net IDR per minute

#### `/admin/intakes` — Intake review

Table view: timestamp, raw intake text (truncated), parsed state summary, safety flags, status.

Click row → detail view with:

- Full raw intake

- Parsed state (JSON)

- Safety classifier output

- Hard filter results

- Match candidates and ranks

- Final match output

- Manual override controls (swap match, add notes)

- Audit log entries for this intake

#### `/admin/bookings` — Booking queue

Table: customer name, provider, requested time, status, last action, ops time logged.

Click row → detail view with:

- Full intake + parsed state

- Provider-safe summary (Yuni’s view to send)

- WhatsApp message templates (pre-filled, copy buttons):

- To provider: “Hi [Provider], a customer matched with you. Here’s the brief: [provider-safe summary]. Available [time]?”

- To customer (confirmed): “Confirmed — [Provider] will arrive at [address] at [time]. Cash or QRIS direct to her, Rp [amount]. Here’s what to expect: [brief].”

- To customer (alternative): “[Provider] isn’t available — but [Alternative] can come at [time]. Want to go with her?”

- State transition buttons (with reason text required for non-default transitions)

- Ops time stopwatch (start/stop while working on this booking)

#### `/admin/providers` — Provider list

Table: name, tier, archetypes, English level, total bookings, last active.

Click row → detail view with full profile and edit form.

#### `/admin/providers/new` — New provider form

Structured fields per `DATABASE_SCHEMA.md` `providers` table.

Plus: free-text “interview notes” textarea with “Structure this for me” button → fires Claude call to extract archetypes, modalities, English level, energy style, best client types from the notes and pre-fill the structured fields. Yuni reviews and edits before save.

#### `/admin/feedback` — Feedback browser

Both customer and provider feedback in one view. Sortable by date, rating, rebook intent.

Customer quotes pulled out for marketing copy capture (per Part 16 of v6.3).

#### `/admin/audit` — Audit log browser

Filter by: intake_id, booking_id, classifier flag, manual override, date range.

Read-only. No edits ever.

-----

### AI pipeline

A single Claude API call per intake handles:

1. **Safety classification** — outputs flags from the 13 categories

1. **State extraction** — physical, emotional, body areas, desired outcome, energy preference, pressure preference

1. **Hard filter generation** — required gender, language, certifications, budget, time window

1. **Provider-safe summary** — sanitized brief that drops emotional/private text

Provider retrieval, ranking, and explanation generation happen in a second Claude call (after Postgres returns the filtered candidate pool).

Schemas in `AI_CONTRACTS.md`. The two-call structure is deliberate: classification gates everything; if it fires the kill-switch, the second call never happens.

#### Whisper transcription

- Customer taps mic → records up to 90s of audio

- Audio sent to Whisper API

- Transcript returned, populated into textarea

- Audio file discarded immediately

- `input_source` set to `whisper_voice` on the intake record

If Whisper fails, UI shows “voice unavailable, please type.” Logged to Sentry. Customer continues with text input.

-----

### Database

12 tables. Full schema in `DATABASE_SCHEMA.md`.

- `providers`

- `provider_services`

- `customer_intakes`

- `safety_audit_log`

- `match_results`

- `booking_requests`

- `booking_status_events`

- `referral_partners`

- `provider_feedback`

- `customer_feedback`

- `commissions`

- `ops_time_log`

Note: no `voice_memos` table in V0 (deferred to V0.1).

-----

### Booking state machine

Full diagram in `DATABASE_SCHEMA.md`. States:

```

intake_started → match_generated → customer_requested

→ provider_pending → provider_confirmed

→ customer_pending → customer_confirmed

→ completed → commission_settled

```

Plus cancellation paths and issue paths.

DB enforces allowed transitions. Every transition writes to `booking_status_events`.

-----

## Out of scope (V0)

If you find yourself wanting to add any of these, stop. They’re documented in `POST_MVP_ROADMAP.md`.

- Customer accounts / login

- Payment processing of any kind

- Provider portal beyond admin-edited profile

- Provider self-serve calendar

- Real-time availability

- Instant booking

- Public reviews or star ratings

- Native app

- Multi-language UI (English only in V0)

- Push notifications

- Email confirmations (WhatsApp only)

- Spirit vertical

- Concierge vertical

- Premium tier dedicated UI

- Couples-specific UI (use the standard flow with notes)

- Villa partner dashboard

- Affiliate/referral codes in customer flow

- SEO-optimized marketing pages beyond the QR landing

- Provider-side voice memo automation (Yuni uses external tools + admin form)

- Audio storage of any kind

- Vector embeddings

- Multi-agent frameworks

- Server-sent events, websockets, anything real-time

-----

## Acceptance criteria for V0

V0 is done when:

1. All 5 daily smoke tests pass for 3 consecutive days

1. Safety classifier eval passes on all 13 kill-switch categories with at least 50 test cases (mix of typed and dictation-style inputs)

1. End-to-end dry run completed by Marcus + Yuni without any manual database fixes

1. Mobile QA passes on iPhone Safari and Android Chrome

1. Pre-first-booking safety gate checklist fully signed off

1. Yuni can navigate the admin without help

1. Sentry shows zero unhandled errors over 24h of dry-run testing

When all 7 are true, Marcus signs off and Yuni starts field recruitment with the working app on her phone.

-----

*MVP Spec v0.1 · Living document · Update via PR with `spec/` prefix*

AI_contracts.md

# AI_CONTRACTS.md

**Source of truth for every AI call’s input and output schema.** Touched only by Claude Code. If you are about to change a schema, propose a spec update first.

-----

## Why these contracts matter

The classifier writes to `safety_audit_log`. The match generator writes to `match_results`. The provider-safe summary writes to `customer_intakes.provider_safe_summary`. Schema drift between code and spec means audit log entries that don’t parse, classifier flags that don’t route, summaries that leak private intake text to providers.

If the schema changes, the migration changes too. Co-evolve them in the same PR.

-----

## Pipeline overview

```

[Customer intake (text or whisper transcript)]

│

▼

┌──────────────────────────┐

│ Call 1: Classify+Extract │  (Claude)

│ - safety classification  │

│ - state extraction       │

│ - hard filter generation │

│ - provider-safe summary  │

└──────────────────────────┘

│

├── kill-switch fired? ──► route to /intake/review-pending, end pipeline

│

▼

[Postgres query: candidates filtered by hard filters]

│

▼

┌──────────────────────────┐

│ Call 2: Rank+Explain     │  (Claude)

│ - rank top 3             │

│ - 2-sentence explanation │

└──────────────────────────┘

│

▼

[Match cards displayed to customer]

```

Whisper runs separately, before Call 1, only when input is voice.

-----

## Whisper transcription

### Endpoint

OpenAI Whisper API (`whisper-1`).

### Input

- Audio file (webm or m4a from MediaRecorder API)

- Max 90 seconds

- Language hint: `en` (V0 is English-only)

### Output

```typescript

{

text: string  // transcript

}

```

### Handler behavior

1. Receive audio blob from client

1. Send to Whisper API

1. On success: return transcript, do NOT save audio file, log `input_source: "whisper_voice"`

1. On failure: return `{ error: "voice_unavailable" }`, client falls back to text input

1. Audio buffer is freed before response returns

No audio is ever written to disk or to S3 or anywhere persistent.

-----

## Call 1: Classify + Extract

### Endpoint

Anthropic Messages API. Model: `claude-opus-4-7` (high-stakes safety call).

### Input

```typescript

interface ClassifyExtractInput {

raw_intake_text: string;       // typed or transcribed

follow_ups: {

health_considerations: string | null;  // optional textarea response

gender_preference: "female" | "male" | "either" | "no_preference";

timing: "today" | "tomorrow" | "this_week" | "flexible";

location: string;             // free-text villa/area

budget_range: "350-500k" | "500-800k" | "800k+" | "open";

contact_whatsapp: string;

woo_level: "practical" | "open_to_intuition" | "spiritual" | "surprise" | null;

};

input_source: "typed" | "whisper_voice" | "admin_entered";

}

```

### Output

Strict JSON. Claude is prompted to return ONLY this object, no preamble.

```typescript

interface ClassifyExtractOutput {

// Safety classification — ALL 13 categories explicitly evaluated

safety: {

flags: SafetyFlag[];           // empty array = clear

kill_switch_fired: boolean;    // true if any flag is in kill-switch list

classifier_reasoning: string;  // 1-3 sentences, stored in audit log

};

// State extraction

state: {

physical: string[];            // ["depleted", "tight shoulders", "tight hips"]

emotional: string[];           // ["heavy", "scattered"]

body_areas: string[];          // ["shoulders", "hips", "neck"]

desired_outcome: string;       // "grounding and physical release"

energy_preference: "quiet" | "talkative" | "no_preference";

pressure_preference: "light" | "medium" | "deep" | "no_preference";

};

// Hard filters for DB query

hard_filters: {

required_gender: "female" | "male" | null;     // null = either OK

required_language_level: "basic" | "conversational" | "fluent";

required_certifications: string[];              // ["prenatal"] if pregnancy

couples_capable_required: boolean;

travel_to_location: string;                     // location for radius check

time_window: {

start_iso: string;

end_iso: string;

};

budget_max_idr: number;

excluded_provider_tiers: number[];              // e.g. [2, 3] for sensitive cases

};

// Provider-safe summary

provider_safe_summary: string;   // 2-4 sentences, drops emotional/private text

// Example: "Prefers quiet, nurturing session. Avoid heavy conversation. Tight shoulders and hips after long flight."

// Customer-facing acknowledgement (shown on /intake/review-pending if kill-switch)

customer_message: string | null; // populated only if kill_switch_fired

}

type SafetyFlag =

| "pregnancy"

| "recent_surgery"

| "chest_pain_or_heart"

| "dizziness_balance"

| "severe_pain_neuro"

| "acute_injury"

| "blood_pressure_or_thinners"

| "medication_relevant"

| "intoxication"

| "trauma_disclosure"

| "self_harm_or_si"

| "minor"

| "medical_help_request";

```

### System prompt structure

```

You are the safety classifier and state extractor for Neskala, an AI-matching layer

for Bali wellness bookings. Your job is to:

1. Classify safety risk across 13 categories. Flag conservatively — when in doubt, flag.

2. Extract state from natural language describing how someone feels.

3. Generate hard filters for a database query.

4. Write a provider-safe summary that drops private/emotional content.

You never decide whether a session is safe. You flag, and a human reviews.

You never make medical claims or recommendations.

The 13 kill-switch categories are: [...full list with examples...]

Return ONLY the JSON object specified. No preamble, no explanation, no markdown.

```

### Failure modes

- Claude returns invalid JSON → log to Sentry, route customer to text-input retry, do NOT proceed to Call 2

- Claude returns valid JSON but unexpected schema → same handling

- Claude API timeout → fallback message “We’re taking longer than usual — try again in a moment”

- Claude API rate limit → fallback message + Sentry alert

In every failure case, no match cards are generated. The audit log records the failure.

-----

## Call 2: Rank + Explain

### Endpoint

Anthropic Messages API. Model: `claude-sonnet-4-6` (cheaper, this is ranking + writing).

### Input

```typescript

interface RankExplainInput {

intake_id: string;

state: ClassifyExtractOutput["state"];   // from Call 1

desired_outcome: string;

candidates: Provider[];                  // already filtered by hard filters in Postgres

// Provider has: id, name, archetypes, modalities, energy_style, pressure_style,

//                best_client_types, english_level, gender, bio, own_words

}

```

### Output

Strict JSON.

```typescript

interface RankExplainOutput {

matches: [

{

provider_id: string;

rank: 1 | 2 | 3;

explanation: string;       // exactly 2 sentences, customer-facing

reasoning: string;         // internal reasoning, stored in match_results

},

// ... rank 2 and rank 3

];

}

```

### Constraints on explanation

- Exactly two sentences

- First sentence: state-specific reason (“X is matched to you because you mentioned [extracted state] and asked for [preference].”)

- Second sentence: provider qualifier (“She specialises in [modality] and [availability/style note].”)

- Never makes medical claims

- Never uses words from the “never use” list in `SAFETY_AND_TRUST.md`

- Never mentions other candidates by name

### Failure modes

- Fewer than 3 candidates returned by Postgres → return only what we have, customer sees “We found 2 matches” or “1 match,” with text encouraging them to check back or accept manual matching

- Claude returns invalid JSON → log to Sentry, fall back to “Yuni will recommend you a match by WhatsApp” flow

- Provider IDs returned by Claude that aren’t in the candidate set → reject the response, fall back to manual

-----

## Call 3 (admin): Structure provider intake notes

### When fired

Admin clicks “Structure this for me” on the new-provider form after pasting Yuni’s interview notes.

### Endpoint

Anthropic Messages API. Model: `claude-sonnet-4-6`.

### Input

```typescript

interface StructureProviderInput {

raw_notes: string;     // Yuni's notes — typed, pasted, or transcribed externally

}

```

### Output

```typescript

interface StructureProviderOutput {

suggested_fields: {

archetypes: ProviderArchetype[];

modalities: string[];

english_level: "basic" | "conversational" | "fluent";

energy_style: string;

pressure_style: "light" | "medium" | "deep" | "varied";

best_client_types: string[];

languages: string[];

travel_radius_km: number | null;

own_words: string;     // 1-2 sentence summary in provider's voice

gaps: string[];        // ["price not mentioned", "gender not specified"]

};

}

type ProviderArchetype =

| "grounder"

| "deep_tissue_recovery"

| "quiet_nurturer"

| "no_woo_professional"

| "premium_villa_specialist";

```

Yuni reviews and edits all fields before saving. The Claude output is suggestion, not authority.

### Failure modes

- Claude returns invalid JSON → form shows “couldn’t structure, fill manually”

- Notes too short to extract anything useful → return mostly empty `suggested_fields` and populate `gaps` with what’s missing

-----

## Audit log writes

Every Claude call writes to `safety_audit_log`. Schema in `DATABASE_SCHEMA.md`. Fields:

- `intake_id` (links to customer_intakes)

- `call_type`: “classify_extract” | “rank_explain” | “structure_provider”

- `model_used`: e.g. “claude-opus-4-7”

- `input_summary`: redacted/short version of input for human review

- `output_summary`: redacted/short version of output

- `classifier_flags`: array (only on classify_extract calls)

- `kill_switch_fired`: boolean (only on classify_extract calls)

- `latency_ms`: number

- `tokens_in`, `tokens_out`: number

- `cost_usd`: number (calculated from token counts)

- `failure_mode`: null | “invalid_json” | “schema_mismatch” | “timeout” | “rate_limit” | “other”

- `created_at`: timestamp

Audit writes are synchronous. If the audit write fails, the originating operation fails. **No try/catch swallowing audit failures.**

-----

## Test mocks

For dev and Replit Agent work where real Claude calls would burn budget:

- `MOCK_CLAUDE=true` env var swaps real calls for fixtures

- Fixtures live in `src/ai/__fixtures__/`

- Each fixture covers a representative case (clear safety / kill-switch fired / partial data / borderline)

- Replit can run the full UI flow against mocks without spending API budget

- CI uses real API for the classifier eval (Day 3 onward), mocks for the rest

-----

## Cost monitoring

- Each call’s cost is logged

- Daily rollup view in `/admin/audit` showing cost per call type

- If daily Claude spend exceeds $10, alert (Sentry or email)

- If approaching the $100 weekly cap, surface to Marcus before the next call

-----

*AI Contracts v0.1 · Owned by Claude Code · Schema changes via PR with `spec/` prefix*

database_schema.md

# DATABASE_SCHEMA.md

**Source of truth for the V0 schema.** Owned by Claude Code. Migrations live in `migrations/`. Co-evolve schema and `AI_CONTRACTS.md` in the same PR.

-----

## Conventions

- All tables have `id` (UUID, default `gen_random_uuid()`), `created_at`, `updated_at` (timestamptz)

- All foreign keys use `ON DELETE RESTRICT` by default — we do not silently lose audit data

- Enum types use Postgres native enums (not text + check constraints) so they’re enforced at the DB layer

- Money in IDR stored as `bigint` (no decimals — IDR has no subdivision in practice)

- Money in USD (Claude API costs) stored as `numeric(10,4)`

- Times stored as `timestamptz`, never naive timestamps

-----

## Enums

```sql

CREATE TYPE input_source AS ENUM (

'typed',

'whisper_voice',

'admin_entered',

'pasted_transcript'

);

CREATE TYPE customer_track AS ENUM ('A', 'B', 'C');

-- A: tourist, B: nomad, C: resident

CREATE TYPE provider_tier AS ENUM ('tier_1', 'tier_2', 'tier_3', 'do_not_list');

CREATE TYPE provider_archetype AS ENUM (

'grounder',

'deep_tissue_recovery',

'quiet_nurturer',

'no_woo_professional',

'premium_villa_specialist'

);

CREATE TYPE english_level AS ENUM ('basic', 'conversational', 'fluent');

CREATE TYPE pressure_style AS ENUM ('light', 'medium', 'deep', 'varied');

CREATE TYPE gender AS ENUM ('female', 'male', 'other');

CREATE TYPE gender_preference AS ENUM ('female', 'male', 'either', 'no_preference');

CREATE TYPE woo_level AS ENUM (

'practical',

'open_to_intuition',

'spiritual',

'surprise'

);

CREATE TYPE timing_pref AS ENUM ('today', 'tomorrow', 'this_week', 'flexible');

CREATE TYPE budget_range AS ENUM (

'r350_500k',

'r500_800k',

'r800k_plus',

'open'

);

CREATE TYPE booking_state AS ENUM (

'intake_started',

'match_generated',

'customer_requested',

'provider_pending',

'provider_confirmed',

'customer_pending',

'customer_confirmed',

'completed',

'commission_settled',

'canceled_by_customer',

'canceled_by_provider',

'no_show_customer',

'no_show_provider',

'rescheduled',

'issue_reported',

'under_review',

'resolved_refund_credit',

'resolved_no_action',

'escalated',

'safety_incident'

);

CREATE TYPE safety_flag AS ENUM (

'pregnancy',

'recent_surgery',

'chest_pain_or_heart',

'dizziness_balance',

'severe_pain_neuro',

'acute_injury',

'blood_pressure_or_thinners',

'medication_relevant',

'intoxication',

'trauma_disclosure',

'self_harm_or_si',

'minor',

'medical_help_request'

);

CREATE TYPE referral_partner_type AS ENUM (

'villa',

'guesthouse',

'coworking',

'yoga_studio',

'cafe',

'customer'

);

CREATE TYPE ai_call_type AS ENUM (

'classify_extract',

'rank_explain',

'structure_provider'

);

CREATE TYPE failure_mode AS ENUM (

'invalid_json',

'schema_mismatch',

'timeout',

'rate_limit',

'other'

);

```

-----

## Tables

### `providers`

Yuni’s vetted practitioners.

|Column             |Type                |Notes                                                 |

|-------------------|--------------------|------------------------------------------------------|

|id                 |uuid                |PK                                                    |

|name               |text                |Display name                                          |

|photo_url          |text                |Nullable until photo collected                        |

|bio                |text                |Yuni’s notes from interview                           |

|own_words          |text                |Provider’s own description, 1-2 sentences             |

|location           |text                |Home base (e.g., “Penestanan, Ubud”)                  |

|travel_radius_km   |int                 |How far they’ll travel for villa visits               |

|archetypes         |provider_archetype[]|Multi-select                                          |

|tier               |provider_tier       |Default ‘tier_2’ (trial)                              |

|modalities         |text[]              |[“Balinese”, “deep tissue”, “lymphatic drainage”]     |

|pressure_style     |pressure_style      |                                                      |

|energy_style       |text                |Free-form (“quiet, grounding”)                        |

|best_client_types  |text[]              |[“jet-lagged tourists”, “post-yoga”]                  |

|languages          |text[]              |[“Bahasa Indonesia”, “English”]                       |

|english_level      |english_level       |                                                      |

|gender             |gender              |                                                      |

|certifications     |text[]              |[“prenatal”, “lymphatic”]                             |

|availability_notes |text                |Free-form (“usually free Tuesday-Thursday afternoons”)|

|price_range_min_idr|bigint              |                                                      |

|price_range_max_idr|bigint              |                                                      |

|boundaries_notes   |text                |Yuni’s private notes on what they will/won’t do       |

|internal_notes     |text                |Yuni-only private notes                               |

|customer_track_fit |customer_track[]    |Which tracks this provider fits                       |

|active             |boolean             |Default true. False = paused, not deleted             |

|created_at         |timestamptz         |                                                      |

|updated_at         |timestamptz         |                                                      |

Index on `tier`, `archetypes` (GIN), `active`.

### `provider_services`

What sessions each provider offers.

|Column       |Type  |Notes                                  |

|-------------|------|---------------------------------------|

|id           |uuid  |PK                                     |

|provider_id  |uuid  |FK providers                           |

|service_name |text  |“60-min Balinese”, “90-min deep tissue”|

|duration_mins|int   |                                       |

|price_idr    |bigint|                                       |

|description  |text  |                                       |

### `customer_intakes`

Every intake submission, including the ones that never converted.

|Column               |Type             |Notes                                                             |

|---------------------|-----------------|------------------------------------------------------------------|

|id                   |uuid             |PK                                                                |

|referral_partner_id  |uuid             |FK referral_partners, nullable                                    |

|customer_track       |customer_track   |Inferred or asked                                                 |

|input_source         |input_source     |typed / whisper_voice / admin_entered / pasted_transcript         |

|raw_intake_text      |text             |The customer’s words. 30-day retention then summarized-or-deleted.|

|extracted_state      |jsonb            |Output of Call 1 state extraction                                 |

|body_areas           |text[]           |                                                                  |

|desired_outcome      |text             |                                                                  |

|energy_pref          |text             |                                                                  |

|woo_level            |woo_level        |Nullable                                                          |

|safety_flags         |safety_flag[]    |Empty array if clear                                              |

|kill_switch_fired    |boolean          |                                                                  |

|gender_pref          |gender_preference|                                                                  |

|language_pref        |english_level    |                                                                  |

|location             |text             |                                                                  |

|budget               |budget_range     |                                                                  |

|timing_pref          |timing_pref      |                                                                  |

|contact_whatsapp     |text             |                                                                  |

|provider_safe_summary|text             |Sanitized version for provider                                    |

|created_at           |timestamptz      |                                                                  |

Index on `created_at`, `kill_switch_fired`, `referral_partner_id`.

### `safety_audit_log`

Every Claude call writes here. Read-only after insert.

|Column                  |Type         |Notes                                        |

|------------------------|-------------|---------------------------------------------|

|id                      |uuid         |PK                                           |

|intake_id               |uuid         |FK customer_intakes, nullable for admin calls|

|booking_id              |uuid         |FK booking_requests, nullable                |

|call_type               |ai_call_type |                                             |

|model_used              |text         |“claude-opus-4-7”                            |

|input_summary           |text         |Redacted/short version                       |

|output_summary          |text         |Redacted/short version                       |

|classifier_flags        |safety_flag[]|Only populated for classify_extract          |

|kill_switch_fired       |boolean      |Default false                                |

|hard_filters_applied    |jsonb        |Only for classify_extract                    |

|providers_considered    |uuid[]       |Only for rank_explain                        |

|final_match_provider_ids|uuid[]       |Only for rank_explain                        |

|manual_overrides        |jsonb        |Populated when admin overrides               |

|latency_ms              |int          |                                             |

|tokens_in               |int          |                                             |

|tokens_out              |int          |                                             |

|cost_usd                |numeric(10,4)|                                             |

|failure_mode            |failure_mode |Nullable                                     |

|failure_detail          |text         |Nullable                                     |

|created_at              |timestamptz  |                                             |

Index on `intake_id`, `booking_id`, `call_type`, `kill_switch_fired`, `created_at`.

**Constraint:** rows are insert-only. Updates rejected at DB level (use a trigger or `REVOKE UPDATE`).

### `match_results`

Output of Call 2.

|Column                |Type       |Notes                 |

|----------------------|-----------|----------------------|

|id                    |uuid       |PK                    |

|intake_id             |uuid       |FK customer_intakes   |

|provider_1_id         |uuid       |FK providers          |

|provider_1_explanation|text       |Customer-facing       |

|provider_1_reasoning  |text       |Internal              |

|provider_2_id         |uuid       |FK providers, nullable|

|provider_2_explanation|text       |Nullable              |

|provider_2_reasoning  |text       |Nullable              |

|provider_3_id         |uuid       |FK providers, nullable|

|provider_3_explanation|text       |Nullable              |

|provider_3_reasoning  |text       |Nullable              |

|manual_override_notes |text       |If Marcus/Yuni edited |

|created_at            |timestamptz|                      |

### `booking_requests`

|Column              |Type         |Notes                                    |

|--------------------|-------------|-----------------------------------------|

|id                  |uuid         |PK                                       |

|intake_id           |uuid         |FK customer_intakes                      |

|match_result_id     |uuid         |FK match_results                         |

|selected_provider_id|uuid         |FK providers                             |

|state               |booking_state|Default ‘customer_requested’             |

|requested_datetime  |timestamptz  |What the customer asked for              |

|confirmed_datetime  |timestamptz  |Nullable until confirmed                 |

|location            |text         |Villa address                            |

|service_id          |uuid         |FK provider_services                     |

|price_idr           |bigint       |At time of booking                       |

|commission_idr      |bigint       |Computed                                 |

|referral_partner_id |uuid         |FK referral_partners, nullable           |

|referral_fee_idr    |bigint       |Nullable                                 |

|payment_method      |text         |“cash” or “qris”                         |

|time_to_book_mins   |int          |From intake_started to customer_confirmed|

|created_at          |timestamptz  |                                         |

|updated_at          |timestamptz  |                                         |

Index on `state`, `selected_provider_id`, `requested_datetime`.

### `booking_status_events`

Append-only event stream for the state machine.

|Column    |Type         |Notes                                 |

|----------|-------------|--------------------------------------|

|id        |uuid         |PK                                    |

|booking_id|uuid         |FK booking_requests                   |

|from_state|booking_state|Nullable for initial state            |

|to_state  |booking_state|                                      |

|actor     |text         |“customer”, “yuni”, “marcus”, “system”|

|reason    |text         |Required for non-default transitions  |

|notes     |text         |Nullable                              |

|created_at|timestamptz  |                                      |

**Constraint:** insert-only. Allowed transitions enforced via DB function (see State Machine section).

### `referral_partners`

|Column          |Type                 |Notes                                |

|----------------|---------------------|-------------------------------------|

|id              |uuid                 |PK                                   |

|name            |text                 |                                     |

|type            |referral_partner_type|                                     |

|location        |text                 |                                     |

|contact_name    |text                 |                                     |

|contact_whatsapp|text                 |                                     |

|referral_code   |text                 |Unique short code embedded in QR URL |

|fee_structure   |text                 |“Rp 25k flat” / “Rp 50k flat” / “10%”|

|total_bookings  |int                  |Computed via view, but cached here   |

|total_payout_idr|bigint               |Cached                               |

|active          |boolean              |                                     |

|created_at      |timestamptz          |                                     |

### `provider_feedback`

|Column        |Type       |Notes                              |

|--------------|-----------|-----------------------------------|

|id            |uuid       |PK                                 |

|booking_id    |uuid       |FK booking_requests                |

|match_accurate|boolean    |                                   |

|energy_right  |boolean    |                                   |

|pressure_right|boolean    |                                   |

|on_time       |boolean    |                                   |

|rebook_intent |text       |“yes” / “maybe” / “no”             |

|private_notes |text       |Provider-only, not customer-visible|

|submitted_at  |timestamptz|                                   |

### `customer_feedback`

|Column                               |Type       |Notes                             |

|-------------------------------------|-----------|----------------------------------|

|id                                   |uuid       |PK                                |

|booking_id                           |uuid       |FK booking_requests               |

|overall_rating                       |int        |1-5                               |

|match_accurate                       |int        |1-5                               |

|would_have_booked_without_explanation|text       |“yes”/“no”/“unsure”               |

|trust_increase_from_explanation      |text       |“yes”/“somewhat”/“no”             |

|would_have_preferred_browse          |text       |“yes”/“no”/“unsure”               |

|match_felt                           |text       |Customer quote, marketing-eligible|

|rebook_intent                        |text       |“yes”/“maybe”/“no”                |

|notes                                |text       |                                  |

|submitted_at                         |timestamptz|                                  |

### `commissions`

|Column            |Type       |Notes                               |

|------------------|-----------|------------------------------------|

|id                |uuid       |PK                                  |

|booking_id        |uuid       |FK booking_requests, unique         |

|gross_idr         |bigint     |Customer paid                       |

|platform_idr      |bigint     |Neskala’s cut                       |

|provider_idr      |bigint     |What provider keeps                 |

|referral_idr      |bigint     |To villa partner                    |

|payment_fee_idr   |bigint     |QRIS fee or 0 for cash              |

|refund_reserve_idr|bigint     |Held for potential refund credit    |

|net_idr           |bigint     |platform - referral - fees - reserve|

|settled           |boolean    |True when Yuni has reconciled       |

|settled_at        |timestamptz|                                    |

|created_at        |timestamptz|                                    |

### `ops_time_log`

Tracks Yuni’s coordination minutes per booking.

|Column                |Type       |Notes                                                   |

|----------------------|-----------|--------------------------------------------------------|

|id                    |uuid       |PK                                                      |

|booking_id            |uuid       |FK booking_requests, nullable for non-booking ops       |

|actor                 |text       |“yuni” or “marcus”                                      |

|activity              |text       |“provider_outreach”, “customer_confirm”, “issue_resolve”|

|minutes               |int        |                                                        |

|whatsapp_message_count|int        |Optional                                                |

|failed_match_attempt  |boolean    |True for time spent on requests that didn’t convert     |

|net_idr_per_minute    |numeric    |Computed when commission settles                        |

|logged_at             |timestamptz|                                                        |

-----

## Booking state machine

### States

```

intake_started

│

▼

match_generated

│

▼

customer_requested ────┬────────────────────────►  canceled_by_customer

│                  │

▼                  │

provider_pending ──────┼────────────────────────►  canceled_by_provider

│                  │

▼                  │

provider_confirmed ────┼────────────────────────►  rescheduled (back to provider_pending)

│                  │

▼                  │

customer_pending ──────┤

│                  │

▼                  │

customer_confirmed ────┼────────────────────────►  no_show_customer

│                  │                            no_show_provider

▼                  │

completed              │

│                  │

▼                  │

commission_settled     │

│

└─►  issue_reported ──► under_review ──► resolved_refund_credit

──► resolved_no_action

──► escalated

└─►  safety_incident  (overrides all other paths)

```

### Allowed transitions

Enforced by Postgres function `check_booking_transition(from_state, to_state)`. Defined in migration. Runs as trigger on `booking_status_events` insert.

```

intake_started → match_generated, canceled_by_customer

match_generated → customer_requested, canceled_by_customer

customer_requested → provider_pending, canceled_by_customer

provider_pending → provider_confirmed, canceled_by_provider, rescheduled, canceled_by_customer

provider_confirmed → customer_pending, canceled_by_provider, rescheduled, canceled_by_customer

customer_pending → customer_confirmed, canceled_by_customer

customer_confirmed → completed, no_show_customer, no_show_provider, canceled_by_customer, canceled_by_provider

completed → commission_settled, issue_reported

commission_settled → issue_reported, safety_incident

* → safety_incident  (always allowed)

* → issue_reported   (always allowed except from terminal states)

issue_reported → under_review

under_review → resolved_refund_credit, resolved_no_action, escalated

escalated → resolved_refund_credit, resolved_no_action  (after Marcus review)

```

Invalid transitions raise an exception, the originating operation fails, no state mutation happens.

### Audit on every transition

Every `booking_status_events` insert is mirrored in app-side observability. The DB is the truth, the audit log is the trail.

-----

## Migrations

Tooling: `drizzle-kit` or raw SQL files in `migrations/` numbered by timestamp.

### Migration order for Day 1

1. `0001_enums.sql` — all enum types

1. `0002_providers.sql` — providers, provider_services

1. `0003_referral_partners.sql` — referral_partners

1. `0004_intakes.sql` — customer_intakes, safety_audit_log

1. `0005_matches_and_bookings.sql` — match_results, booking_requests, booking_status_events

1. `0006_feedback_and_commissions.sql` — provider_feedback, customer_feedback, commissions, ops_time_log

1. `0007_state_machine.sql` — `check_booking_transition` function and trigger

1. `0008_audit_immutability.sql` — REVOKE UPDATE on safety_audit_log and booking_status_events

1. `0009_indexes.sql` — all listed indexes

Each migration is irreversible-on-prod (no down migrations for V0; we forward-fix).

-----

## Seed data

For Day 1 development:

- 8 providers covering the bench distribution from v6.3 Part 8:

- 3 Balinese / relaxation (one Tier 1, two Tier 2)

- 2 deep tissue / therapeutic

- 2 villa / couples-capable

- 1 female specialist for women customers

- 2 with conversational+ English

- 3 referral partners (1 villa, 1 coworking, 1 yoga studio)

- All seed data uses obviously-fake names (“Test Provider 1”) to prevent confusion with real onboardings

Seed runs with `pnpm db:seed`. Idempotent.

-----

## Backups

- Neon’s daily snapshots are V0 backup (no extra tooling)

- Before every deploy that changes schema, snapshot is verified

- For V1: scheduled exports to S3 weekly

-----

*Schema v0.1 · Owned by Claude Code · Migrations are append-only*

safety_and_trust.md

# SAFETY_AND_TRUST.md

**The single most important doc in the pack.** Owned by Claude Code. Touched only when the change has been thought through.

Neskala sends a stranger into someone’s villa. The platform’s reputation, legal exposure, and ethical responsibility live in this document. The 13-category kill-switch and the audit log are not features. They are the gate that lets us book anyone at all.

-----

## The principle

> The AI never decides safety. It flags. A human reviews.

Safety classification, hard-filter generation, ranking, and explanation are AI tasks. Decisions about whether a session can happen, whether a customer should be banned, whether a refund is owed, whether a provider should be promoted — those are human.

-----

## The 13-category kill-switch

If the classifier flags any of these on the raw intake, the system halts automated matching and routes to human-only review. Customer sees: “Thanks — we want to match you safely. Our team will reach out within an hour.”

|# |Category                    |What triggers it                                                                                                          |

|--|----------------------------|--------------------------------------------------------------------------------------------------------------------------|

|1 |`pregnancy`                 |Any mention of being pregnant, trying for pregnancy with confirmed positive test, recent pregnancy loss within 6 weeks    |

|2 |`recent_surgery`            |Surgery or stitches in past 6 months. Includes dental surgery, c-section, joint surgery                                   |

|3 |`chest_pain_or_heart`       |Chest pain, palpitations, shortness of breath, known heart condition                                                      |

|4 |`dizziness_balance`         |Dizziness, vertigo, fainting, balance issues, recent concussion                                                           |

|5 |`severe_pain_neuro`         |Severe pain, numbness, tingling, fever, sciatica with leg symptoms                                                        |

|6 |`acute_injury`              |Sprain, fracture, recent fall, recent motor accident                                                                      |

|7 |`blood_pressure_or_thinners`|Known BP issues, blood thinners (warfarin, eliquis, etc.)                                                                 |

|8 |`medication_relevant`       |Medication that affects bodywork (steroids, certain antidepressants, opioids). When uncertain, flag and let human review. |

|9 |`intoxication`              |Slurred typing, current drug/alcohol use mentioned, “I’m wasted” / “wrecked” / “off my face”                              |

|10|`trauma_disclosure`         |PTSD, recent assault, recent abuse, “trigger warning” framing, somatic flashback risk                                     |

|11|`self_harm_or_si`           |Self-harm language, suicidal ideation, “I want to disappear” type language                                                |

|12|`minor`                     |Stated age under 18, references to school/parents in a way suggesting minor, request for child massage                    |

|13|`medical_help_request`      |“I need medical help,” “should I go to a doctor,” “is this serious” — anything indicating they think they need a clinician|

### How “conservative” works in practice

When in doubt, flag. False positives route a customer to human review (Yuni messages them within an hour). False negatives put a customer with a medical issue in front of a non-clinical massage therapist. Asymmetric cost. Default to flag.

### Self-harm and SI special handling

If `self_harm_or_si` fires:

- No match cards generated, ever

- Customer-facing message includes a line acknowledging emotional weight: “We hear you. A massage isn’t the right help for what you’re describing right now, and we want you to be safe. We’re not a crisis service — please consider reaching out to a friend, family member, or a local crisis line. Yuni will message you within an hour.”

- Marcus is alerted by Sentry / email immediately, not just Yuni

- Yuni’s response script (see `OPS_PLAYBOOK.md`) explicitly avoids playing therapist; she expresses care and shares local crisis line info

-----

## The classifier eval harness

Lives in `tests/safety-classifier-eval.test.ts`. Runs in CI on every PR that touches the classifier or its prompt.

### Required coverage

At minimum 50 test cases. At minimum 3 per kill-switch category. Mix of:

- **Clear positives** — obvious mention of the flag (“I’m 6 weeks pregnant”)

- **Borderline positives** — implicit mention (“we’re trying for a baby and might be early”)

- **Confounders** — mentions of related-but-not-flagging concepts (“my back hurts but it’s just from yoga”)

- **Multi-flag cases** — intake mentions multiple concerns (“post-surgery and trying for pregnancy”)

- **Both registers** — typed prose AND dictation-style (run-on, “um,” disfluent)

### Eval pass criteria

- All 13 kill-switch categories: 100% recall on clear positives (no false negatives on the obvious cases)

- Borderline positives: at least 80% recall, with documented gaps reviewed by Marcus

- Confounders: false positive rate under 20% (some over-flagging is acceptable; under-flagging is not)

- Provider-safe summary never contains text from the raw intake’s emotional/private content (separate test)

### When eval fails

Any clear-positive failure → block merge, classifier prompt must be updated, eval re-runs. No exceptions.

Borderline failure → discuss with Marcus, document the gap, decide whether to update prompt or accept the gap with a logged-incident protocol.

-----

## Audit log integrity

The audit log is the legal trail. If something goes wrong in a villa, the audit log is what proves we did our part.

### What gets logged

Every Claude call. Every state transition. Every manual override. Every safety flag. Every kill-switch firing. Every fallback to human review. Every classifier failure mode.

### What does not get logged

- Customer raw intake text (lives in `customer_intakes` table, deleted after 30 days)

- Audio files (never stored)

- Provider private contact info (lives in `providers.internal_notes`)

- Customer payment card data (we never have it)

### Hard rules for audit log code

- Audit writes are synchronous. The originating operation waits for the audit write.

- If the audit write fails, the originating operation fails. No partial states.

- Audit log rows are insert-only. `REVOKE UPDATE` and `REVOKE DELETE` enforced at DB level.

- No try/catch around audit writes that swallows the error and continues.

- No “we’ll log this later” queuing. Synchronous, or it didn’t happen.

### Reading the audit log

- Admin UI at `/admin/audit` is read-only

- Filterable by intake_id, booking_id, classifier flag, manual override, date range

- Cost monitoring rolls up to a daily view

-----

## Provider-safe summary

The customer’s raw intake might say: “I feel emotionally heavy after a breakup and don’t want to talk.”

The provider does not need that text. They need a session-relevant brief.

### What goes in the summary

- Session-relevant physical state (“tight shoulders, post-flight depletion”)

- Session-relevant preferences (“prefers quiet, nurturing session, avoid heavy conversation”)

- Explicit safety flags that affect the session (injuries, areas to avoid, certifications needed)

- Logistical details (location, time, gender preference if specified)

### What never goes in the summary

- Emotional state text from the raw intake

- Trauma disclosures

- Mental health language

- Personal context unrelated to the bodywork

- Customer’s name beyond first name

### Tested separately

`tests/provider-safe-summary.test.ts` runs a fixture set of intakes with clearly-private content and verifies that none of it appears in the summary. This test runs in CI.

### Customer sees the summary before booking

On `/booking/:booking_id/pending`, the customer sees the provider-safe summary that Yuni will send to the provider. This is the consent-to-share mechanism. If they’re uncomfortable with what’s there, they can edit or withdraw before confirmation.

-----

## Customer-side safety

### Before booking

- ToS acknowledged before intake submission

- No-sexual-services policy displayed prominently in ToS top section

- Customer provides villa address before any provider contact

### During booking

- First-time customers in private villas get a confirmation call from Yuni (not just WhatsApp text)

- Provider’s first name and photo (if available) shared with customer

- Late-night bookings (after 9pm) require Marcus + Yuni explicit approval; default to disabled in V0

### Behavior policy

- One boundary violation = permanent ban. No second chances.

- Customer agrees to no-sexual-services terms before booking.

- Aggressive behavior, intoxication, sexual requests → provider leaves immediately, full payment, customer banned.

-----

## Provider-side safety

Symmetric. Good providers don’t work with platforms that protect only customers.

- Provider receives customer name, address, WhatsApp, booking details before accepting

- Provider can refuse any booking, no penalty, no explanation required

- Provider can leave immediately with full payment if customer is intoxicated, sexual, aggressive, unsafe

- Optional check-in/check-out via WhatsApp for late-night or first-time villa sessions

- Customer permanently banned after any sexual request or boundary violation

- Platform supports the provider in disputes. Default: believe the provider on safety claims.

### Provider vetting (V0)

Tier 1 only for V0 bookings. Tier 2 (trial) providers get bookings only after their first 3 sessions are clean.

Tier 1 requirements:

- KTP or passport, phone, address, photo verified by Yuni

- At least one reference Yuni has spoken to

- 30-45 min structured interview

- First 3 bookings monitored

- Signed agreement (no-sexual-services, no-medical-claims, boundary respect, incident reporting)

-----

## Pre-first-booking safety gate

Booking #1 cannot happen until **all** of these are checked. Marcus signs off in writing.

|# |Item                                                                  |Owner              |Verification                                                                      |

|--|----------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------|

|1 |Provider agreement signed for all V0 providers                        |Yuni               |Paper copies in Yuni’s folder, summary in `providers.internal_notes`              |

|2 |Customer ToS displayed and acknowledged before intake                 |Claude Code        |UI test: cannot submit intake without checkbox                                    |

|3 |No-sexual-services policy visible to both sides                       |Claude Code        |Top of ToS, top of provider agreement                                             |

|4 |Cancellation/refund policy visible                                    |Claude Code        |Linked from ToS, linked from booking confirmation                                 |

|5 |AI safety classifier eval passing on all 13 categories                |Claude Code        |CI green on `tests/safety-classifier-eval.test.ts`                                |

|6 |Pregnancy/injury route to human review verified end-to-end            |Claude Code + Codex|Smoke test 3 (build brief) passes                                                 |

|7 |Provider has ID + reference verified                                  |Yuni               |Yuni’s records                                                                    |

|8 |Provider tier assigned (Tier 1 only for V0 bookings)                  |Yuni               |DB query: all `tier_1` providers have `references_verified=true` in internal_notes|

|9 |Customer sees provider-safe summary, not raw intake                   |Claude Code        |Test in `tests/provider-safe-summary.test.ts`                                     |

|10|Yuni has incident response script saved on her phone                  |Yuni               |See `OPS_PLAYBOOK.md`                                                             |

|11|Provider WhatsApp check-in/check-out tested                           |Yuni               |Tested with one provider, documented in playbook                                  |

|12|Customer behavior policy documented                                   |Marcus             |In ToS                                                                            |

|13|Audit log writes confirmed working                                    |Codex              |Smoke test 5 passes                                                               |

|14|End-to-end dry run completed                                          |All                |Marcus + Yuni as fake customer + fake provider                                    |

|15|Booking state machine tested through happy path + 2 cancellation paths|Codex              |Playwright tests green                                                            |

Marcus signs the gate by appending to `PRE_FIRST_BOOKING_GATE.md` (created Day 6) with date, his initials, and any caveats.

-----

## Incident response

### Incident types and responses

|Type                                                           |Response                                                                                                                                           |

|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|

|Provider reports unsafe customer                               |Booking paused immediately. Customer statement collected. Customer banned if pattern or severity warrants. **Default to believing the provider.**  |

|Customer reports boundary violation                            |Booking paused. Both statements. Refund decision. Provider suspended pending review. Escalated if serious.                                         |

|Provider no-show or cancellation                               |Customer offered immediate alternative. Provider flagged. 3 strikes = removal.                                                                     |

|Serious safety incident                                        |Platform suspended for both parties. Statements collected. Authorities involved if required. **No cover-up.**                                      |

|AI safety classifier failure (medical condition matched anyway)|Booking paused. Audit log reviewed. Classifier rules updated. Customer contacted by human. **Provider not penalized — system failure, not theirs.**|

### Incident logging

In V0, incidents are logged via `booking_status_events` with `to_state = 'safety_incident'` and full notes. Marcus and Yuni both review.

In V0.1, a dedicated `incidents` table with structured fields (severity, type, parties, resolution, timeline). For now, the booking events stream is enough.

-----

## Refund policy (V0)

Payment is direct customer-to-provider. Neskala does not process automatic refunds. Refund decisions are credit toward future bookings.

|Situation                            |Resolution                                                    |

|-------------------------------------|--------------------------------------------------------------|

|Provider no-show                     |Replacement provider OR full booking credit. Provider strike. |

|Provider 30+ min late without warning|Customer offered Rp 50-75k platform credit toward next booking|

|Service quality complaint            |Up to 50% future-booking credit at Marcus/Yuni discretion     |

|Customer cancellation 4+ hours before|Free                                                          |

|Customer cancellation under 4 hours  |Provider may bill Rp 50-100k transport fee at their discretion|

|Safety/boundary violation            |Overrides all refund logic; triggers incident protocol        |

-----

## Language to use and avoid

### Use

- “Wellness support, relaxation, bodywork”

- “Grounding, restoration, nervous system support”

- “Spiritual guidance and personal ritual” (Spirit vertical, post-V0)

- “Preference-based matching”

- “For serious concerns, consult a qualified professional”

### Never use

- “Medical treatment” or any medical/diagnostic language

- “Cure,” “heal,” or “fix” as guaranteed outcomes

- “Treat anxiety, depression, trauma, addiction”

- “AI diagnosis” or any framing that implies medical recommendation

- Any claim Neskala replaces professional care

This list is enforced in the explanation generator (Call 2) prompt and verified by `tests/explanation-language.test.ts`.

-----

## Cultural respect

- Yuni and local cultural advisors decide what’s appropriate to list. Marcus does not override.

- Not every traditional practice should be productized. Some Balinese healing is not appropriate to commodify.

- Balian listings require special permission and extended vetting. Body vertical only in V0; Balian listings are post-V0.

- No “ancient secrets,” “mystic healing,” or exoticizing copy in marketing.

- Use Indonesian and Balinese language respectfully and accurately.

-----

## Data privacy

- Collect only what’s needed for matching. No indefinite storage of emotional intake.

- Raw intake retained 30 days, then summarized-or-deleted.

- No selling, sharing, or using customer emotional/health data outside the match.

- Customers can request deletion at any time; honor within 7 days.

- Indonesia’s Personal Data Protection Law (UU PDP) applies. Compliance scoping happens Month 2 with a Bali startup lawyer (per v6.3 Part 18). V0 operates as a private referral experiment, not a public marketplace, until that scoping is done.

-----

## When something this doc doesn’t cover happens

Surface to Marcus immediately. Do not improvise on safety. Do not extend the kill-switch list mid-conversation with a customer. Do not write new policy in PR comments.

The audit log captures the deviation. Marcus updates this doc. The next version is the truth.

-----

*Safety doc v0.1 · Owned by Claude Code · Reviewed before pre-first-booking gate sign-off*

ops_playbook.md

# OPS_PLAYBOOK.md

**Yuni’s daily manual workflows.** Owned by Yuni and Marcus. Updated as patterns emerge during the 30-day validation sprint.

The product behind the polish is a person. This document is what that person actually does.

-----

## Daily rhythm

### Morning (15-30 min)

1. Check admin dashboard for overnight intakes

1. Review any kill-switch flags routed to human review — respond within 1 hour during operating hours (9am-9pm Bali time)

1. Check pending booking confirmations from yesterday — anyone need a follow-up?

1. Check provider feedback from yesterday’s sessions

### Midday (varies)

1. Field provider outreach — interviews, photo collection, agreements

1. Villa partner check-ins — relationship maintenance, refresh QR cards

1. Active booking coordination as requests come in

### Evening

1. Send customer feedback links 30 min after each session’s scheduled end

1. Reconcile commissions for completed sessions (mark `commissions.settled = true`)

1. Log ops minutes for the day’s bookings

1. End-of-day review: anything to flag for Marcus?

-----

## Provider interview workflow

### Before the interview

1. Yuni messages provider on WhatsApp to schedule

1. Sends the provider intake script (below) so they know what to expect

1. Confirms time and location (provider’s home, cafe, or studio)

### The interview script

Open with warmth. Then structured questions:

1. **Modalities** — what kinds of bodywork do you do? How long have you been practicing?

1. **Style** — describe how you work. Are you more grounding, more energizing, more clinical?

1. **Best-fit clients** — who are your favorite clients? Who do you do your best work with?

1. **Pressure** — light, medium, deep, or varies by client?

1. **Energy** — talkative, quiet, depends on client?

1. **Languages and English level** — what level are you comfortable with for English-speaking clients?

1. **Travel** — do you do villa visits? How far will you travel?

1. **Pricing** — what do you charge for 60 min, 90 min, couples?

1. **Equipment** — do you bring oils, table, sheets?

1. **Boundaries** — what won’t you do? Late nights? Specific areas? Specific client types?

1. **Availability** — typical week. When are you usually free vs. booked?

1. **References** — who can speak to your work? Yuni will follow up with one.

1. **Agreement** — walk through no-sexual-services, no-medical-claims, incident reporting, commission terms.

### Capturing the interview

Yuni’s choice of method:

- **Default:** Type structured fields directly into `/admin/providers/new` during or right after the interview. Best when laptop is available and the conversation has natural pauses.

- **Voice memo backup:** Apple Voice Memos with on-device transcription (iOS 18+). After the interview, Yuni transcribes within Voice Memos, copies the text into the admin form’s “interview notes” textarea, clicks “Structure this for me” to get suggested archetypes/modalities/etc., reviews and edits before saving.

- **Paper backup:** Notebook during interview, transcribe to admin form within 24 hours.

The voice memo and paper paths exist because in the field with a provider, full attention to the person matters more than typing. Whichever method Yuni uses, the structured fields must be filled in the admin panel within 24 hours of the interview.

### Provider can’t be Tier 1 until

- Identity verified (KTP or passport, photo)

- One reference contacted by Yuni

- Agreement signed (paper)

- Photo taken or provided

- Profile complete in admin (no missing fields)

- Interview notes captured in admin

-----

## Booking confirmation workflow

When a customer requests a booking, Yuni gets it in `/admin/bookings`. The flow:

### Step 1: Read the request (under 2 min)

- Open the booking detail in admin

- Read raw intake, parsed state, safety flags

- Note the matched provider and the explanation

- Note the requested time and location

- Check provider’s recent availability (from notes, last booking, or quick WhatsApp check)

### Step 2: Contact the provider (target: under 15 min)

Use the WhatsApp copy button:

> “Hi [Provider], a customer matched with you for [time]. Brief: [provider-safe summary]. Location: [villa/area]. Service: [60-min Balinese / 90-min deep tissue / etc]. Available?”

Wait for response. If the provider needs to think, message back: “Take your time, let me know within an hour if you can.”

### Step 3a: Provider confirms

State transition: `provider_pending → provider_confirmed`. Reason: “Provider confirmed via WhatsApp.” Notes: brief summary.

Use customer-confirm WhatsApp template:

> “Confirmed — [Provider] will arrive at [address] at [time]. She’ll bring oils and equipment. Cash or QRIS direct to her, Rp [amount]. Here’s what to expect: [provider-safe brief tailored to customer]. Message me if anything changes.”

When customer acknowledges, transition: `customer_pending → customer_confirmed`.

### Step 3b: Provider declines or doesn’t respond in 30 min

Two options:

1. **Offer alternative match** — go back to admin, click on rank 2 or rank 3 provider from `match_results`, repeat Step 2.

1. **Manual override** — if no rank 2/3 fits, use admin to manually pick a provider from the list. Notes field: “Manual override, original matches unavailable, [reason].”

Customer-side message:

> “[Provider] isn’t available — but [Alternative] can come at [time]. She specializes in [why-she-fits-instead]. Want to go with her?”

Wait for customer response. If yes, proceed. If no, ask what timing would work and revisit.

### Step 3c: Constraint collision (Ravi’s Friday case)

Couples + gender + late-night + same-day combinations need special handling.

If you can’t find a clean match in the first round, message customer with honesty:

> “Couples sessions usually take a day to coordinate well. Earliest realistic option: tomorrow afternoon. Want us to try for tonight, or shall we book tomorrow?”

The honesty wins. The customer feedback from Ravi’s case is *higher* than from a forced match.

### Step 4: Session day

Optional check-in for late-night or first-time villa sessions:

- Provider sends “arrived safely” WhatsApp at start

- Provider sends “session complete, all good” at end

- If either ping is missed, Yuni follows up within 15 min

For typical daytime bookings, no ping required. Provider has Yuni’s WhatsApp for any issue.

### Step 5: Post-session

30 minutes after scheduled end time:

- Yuni triggers customer feedback link send (admin button or auto-job)

- Marks booking `completed` in admin

- Logs ops minutes for this booking

When provider feedback comes in (usually within 24h), Yuni reviews. Anything notable goes into `internal_notes` on the provider.

When customer feedback comes in, Yuni reviews. Captures customer quote for marketing capture (per v6.3 Part 16).

-----

## Villa partner workflow

### First contact

Yuni walks into the villa or guesthouse. Asks for the manager. The pitch (memorized):

> “I run a service that matches your guests with vetted local massage therapists for in-villa sessions. They scan a QR code at reception, tell us how they feel, and get matched with the right person. We confirm everything before anyone arrives. You earn a referral fee on every completed booking, no work for you.”

Show the working app on her phone. Demo the intake → match flow. This is why we built the app first.

### Onboarding a partner

1. Create entry in `/admin/referral-partners` — name, type, location, contact, fee structure

1. System generates a unique referral code embedded in QR URL: `https://neskala.app?ref=PRT123`

1. Yuni gets the QR card printed (small, professional) and brings it to the villa

1. Walk through the partner packet (1 page): how it works, what guests see, how commission is paid

1. Set expectations: Yuni responds within 1 hour during operating hours; bi-weekly payouts in IDR

### Test the three economics structures

Per v6.3 Part 12, test in parallel:

- Tier A: Rp 25k flat per completed booking (some partners)

- Tier B: Rp 50k flat per completed booking (some partners)

- Tier C: 10% of booking value (some partners)

After 4 weeks of data, pick the structure that drove adoption.

### Maintenance

- Weekly: WhatsApp check-in, “any guest interest? any feedback?”

- After every completed booking through their code: “thanks for sending [name]. session went well. commission Rp [x] added to your bi-weekly payout.”

-----

## Incident response

### What to do in the moment

If a provider reports an unsafe customer mid-session:

1. Tell the provider to leave immediately. Full payment owed regardless.

1. Acknowledge: “I believe you. Get out safely first, talk to me when you’re somewhere safe.”

1. Ban customer in admin (state transition `safety_incident`).

1. Document provider’s account in writing within 1 hour.

1. Inform Marcus.

If a customer reports a boundary violation:

1. Acknowledge and take it seriously: “I’m so sorry. Tell me what happened when you’re ready. Are you okay right now?”

1. Pause the booking immediately (state: `issue_reported → under_review`).

1. Get the provider’s statement separately.

1. Refund decision: default to credit, escalate to Marcus for any payment disagreement.

1. Provider suspended pending review.

1. If the violation is serious (sexual, physical, threatening), escalate to authorities. No cover-up.

If self-harm or SI is disclosed during operations (not just intake):

1. Express care: “I hear you. That sounds really hard. I want you to be safe.”

1. Don’t play therapist. Don’t try to fix it.

1. Share local crisis line info (memorize: Indonesia 119 ext 8 for mental health emergency).

1. If you’re worried about imminent danger, call Marcus.

1. Do not proceed with booking. Cancel and do not penalize the customer in any way.

### Yuni’s incident response script (memorized)

> “I believe you. Are you safe? Tell me what happened when you’re ready. I’m going to pause this booking right now. Marcus and I will figure out what to do next together. You don’t have to make any decisions right now.”

That’s it. Three lines. The whole script.

-----

## When Yuni is offline

Yuni is human. She gets sick, tired, has personal life. The system needs to handle 1-3 day Yuni-offline periods without breaking.

### Acknowledged limitation

Per v6.1 audit, Yuni offline for 3+ days is the unsolved SPOF in V0 ops. We’re not solving it in V0 with another hire — we’re managing it.

### Mitigations in V0

1. **Predictable offline periods** — Yuni tells Marcus 24h+ in advance when possible. Marcus puts a banner on the landing page: “Booking confirmations may be delayed today, we’ll respond by [time].”

1. **Marcus as backup confirmer** — if a booking comes in and Yuni can’t respond within 2 hours, Marcus can confirm via WhatsApp. He has access to the admin. Slower than Yuni (no on-the-ground provider relationships) but functional.

1. **Provider WhatsApp groups** — Yuni’s top 5 Tier 1 providers are in a WhatsApp group with Yuni. If Yuni is offline, providers can self-coordinate via the group for already-confirmed sessions.

1. **Customer-facing honesty** — landing page banner during Yuni-offline periods. Better to set expectations than to disappoint.

### V0.1 + V1 plans (not in V0)

- Yuni’s voice memo capture pipeline (so providers in her head get into the DB faster)

- A second field op to share the load

- Provider self-confirm via WhatsApp Business API

-----

## Commission reconciliation

End of every day:

1. For each `completed` booking, calculate gross, platform cut, provider share, referral share, fees, refund reserve, net

1. Record in `commissions` table

1. If customer paid cash: Yuni confirms with provider that they received it

1. If customer paid QRIS: Yuni reconciles against QRIS records

1. Mark `commissions.settled = true` only when reconciled

Bi-weekly:

1. Pay villa partner referral fees (bank transfer or cash)

1. Update `referral_partners.total_payout_idr`

-----

## Net IDR per Yuni-minute (the truth metric)

After every booking: log Yuni’s coordination minutes in `ops_time_log`.

Categories:

- `provider_outreach` — time spent contacting providers

- `customer_confirm` — time spent confirming with customer

- `issue_resolve` — time spent on problems

- `failed_match_attempt` — time on requests that didn’t convert (this is real cost too)

Weekly review with Marcus:

- Net IDR per Yuni-minute, trended over weeks

- Failed match minutes as % of total (should drop over time)

- Bookings that took >60 minutes of Yuni time — what happened?

V0 target: Rp 1,000-2,000 / minute (acceptable while learning)

Week 4 target: Rp 3,000-5,000 / minute (must be trending here)

If the metric doesn’t trend up by Week 4, we stop and rethink (per stop conditions).

-----

## When something doesn’t fit this doc

Yuni messages Marcus. Marcus updates the playbook. Next version is the truth.

The playbook is meant to encode patterns, not box her in. If a customer asks something that no script covers, use judgment, then surface the case so we add it next.

-----

*Ops Playbook v0.1 · Owned by Yuni + Marcus · Updated weekly during validation sprint*

Test_plan.md

# TEST_PLAN.md

**Source of truth for tests.** Owned by Codex Cloud (Playwright + repo-wide verification) with classifier eval owned by Claude Code.

-----

## Test pyramid

```

┌───────────────────────┐

│  Pre-first-booking     │   Manual gate, Marcus signs off

│  safety gate           │

└───────────────────────┘

▲

┌────────────────────────────┐

│  End-to-end (Playwright)    │   5 happy paths + 10 edge cases

└────────────────────────────┘

▲

┌────────────────────────────────────┐

│  Classifier eval harness (Claude)   │   50+ cases, 13 kill-switch cats

└────────────────────────────────────┘

▲

┌────────────────────────────────────────────┐

│  Unit + contract tests                      │   Per AI call, per state transition

└────────────────────────────────────────────┘

▲

┌───────────────────────────────────────────────────┐

│  Daily smoke tests                                 │   5 scenarios, run EOD during build

└───────────────────────────────────────────────────┘

```

-----

## Daily smoke tests

Run at end of every day during build week. All five must pass before EOD.

### Smoke 1: Customer happy path (text)

**Scenario:** Tourist books a standard 60-min Balinese.

**Steps:**

1. GET `/?ref=PRT001` (villa referral code) → 200, landing page renders

1. Click “Find my match” → `/intake`

1. Type: “I’m jet-lagged from a long flight, my shoulders are wrecked, I’d love a slow grounding massage today”

1. Submit, accept ToS

1. Answer follow-ups: no health issues, female preference, today, “Penestanan villa,” Rp 350-500k, valid WhatsApp

1. See 3 match cards with explanations, all marked “Availability to be confirmed”

1. Click “Request booking with [Provider 1]”

1. See `/booking/:id/pending` with provider-safe summary visible

1. Admin: open `/admin/bookings`, see new request in `customer_requested` state

1. Admin: click WhatsApp copy buttons, verify templates render correctly

1. Admin: transition to `provider_pending`, then `provider_confirmed`, then `customer_confirmed`

1. Admin: check `booking_status_events` — every transition logged with actor and reason

**Pass criteria:** all 12 steps complete without manual DB intervention.

### Smoke 2: Customer voice path

**Scenario:** Same booking, but voice intake.

**Steps:**

1. `/intake`, click microphone

1. Record 30s test audio (mocked in CI, real in manual smoke)

1. Whisper transcribes, populates textarea

1. Verify `customer_intakes.input_source = 'whisper_voice'`

1. Verify no audio file persisted anywhere (check logs, check `/tmp`, check S3 if connected)

1. Continue through booking flow as Smoke 1

**Pass criteria:** transcript appears, audio is gone, intake processes normally.

### Smoke 3: Safety kill-switch

**Scenario:** Pregnancy disclosure routes to human review.

**Steps:**

1. `/intake` with text: “I’m 6 weeks pregnant and feeling really tense in my lower back, can a massage help?”

1. Submit

1. Verify response routes to `/intake/review-pending`

1. Verify NO match cards generated

1. Verify `customer_intakes.kill_switch_fired = true`

1. Verify `customer_intakes.safety_flags` includes `pregnancy`

1. Verify `safety_audit_log` row exists with `kill_switch_fired = true`

1. Verify Yuni gets a notification (email or admin badge)

**Pass criteria:** all 8 steps. Repeat with one example from each of the 13 categories before pre-first-booking gate.

### Smoke 4: Yuni admin + provider create

**Scenario:** New provider gets onboarded into V0 system.

**Steps:**

1. Admin: `/admin/providers/new`

1. Paste Yuni’s interview notes (sample fixture)

1. Click “Structure this for me”

1. Verify Claude returns suggested fields, populated into form

1. Yuni edits, sets tier_2 (trial), saves

1. Verify `providers` row created with all required fields

1. Run a fake intake that should match this provider

1. Verify provider appears in match candidates

**Pass criteria:** provider created, structuring works, candidate retrieval works.

### Smoke 5: Audit log integrity

**Scenario:** Run all of Smokes 1-4, then verify audit completeness.

**Steps:**

1. Query `safety_audit_log` for the day’s intakes

1. Verify every intake has at least 1 row (classify_extract call)

1. Verify every successful match has a second row (rank_explain call)

1. Verify every classifier call has populated tokens, latency, cost

1. Verify rows are insert-only (try UPDATE, expect failure)

1. Query `booking_status_events` for the day’s bookings

1. Verify every state transition has actor, reason, timestamp

1. Verify rows are insert-only (try UPDATE, expect failure)

**Pass criteria:** all writes happened, all are immutable.

-----

## Five happy paths (Playwright)

### HP1: Track A tourist single booking

- Tourist scans villa QR, books 60-min Balinese, completes session, leaves feedback. Standard flow.

### HP2: Track B nomad rebooking

- Nomad has booked before (existing customer record, but no auth — matched by WhatsApp).

- Books a second time. Match should weight providers they previously rated highly.

- *Note: rebooking weight is V0.1, but the path of “second booking” should still complete.*

### HP3: Track C resident first booking

- Resident comes via referral code from existing customer (or community partner).

- Books a 90-min session. Pays cash.

- Resident is asked at feedback if they’d like to be contacted for repeat bookings.

### HP4: Premium couples booking

- Two-person couples session at villa.

- Higher price tier.

- Two providers may be coordinated (or one couples-capable solo).

- Verify pricing math, commission split.

### HP5: Healer booking (premium tier introduction only)

- *Spirit vertical is post-V0, BUT* a premium body practitioner (Tier 1, Rp 1-2M) bookable via existing flow.

- Verify higher-tier filters route correctly, premium price displays correctly.

-----

## Ten edge cases (Playwright)

### EC1: Provider unavailable mid-confirm

- Customer requests booking, Yuni messages provider, provider declines.

- Yuni offers rank-2 match.

- Customer accepts. State machine handles re-routing.

- Verify audit log shows the decline + re-route.

### EC2: Customer goes silent post-match

- Customer requests booking, never confirms.

- After 24 hours, state stays in `provider_pending` or `customer_pending`.

- Verify there’s an admin view to see “stale” bookings.

- *In V0, manual cleanup; V0.1 may add timeout.*

### EC3: Double-booking (provider has session conflict)

- Two booking requests for same provider, overlapping times.

- Yuni catches in admin, manually resolves by offering alternative for one.

- Verify state machine doesn’t autonomously create the conflict.

### EC4: Language mismatch

- Customer specifies fluent English required, all candidates are basic.

- Pipeline returns “no matches found” gracefully, routes to manual review.

### EC5: Payment confusion

- Customer at session: confused about cash vs QRIS amounts.

- Yuni intervenes by WhatsApp, clarifies.

- *Not a code path; verify manual logging of issue in `booking_status_events`.*

### EC6: Customer changes timing

- Customer confirmed, then asks to reschedule.

- Yuni transitions booking to `rescheduled`, then back through `provider_pending`.

- Verify allowed state transitions.

### EC7: Late-night request (post-9pm)

- Customer requests session at 10pm.

- V0 default: human-only review with explicit “late night requires Yuni approval” flag.

- Verify routing logic, not auto-confirmed.

### EC8: Out-of-area request

- Customer in Lovina (V0 covers Ubud + Canggu).

- Pipeline returns “we don’t cover that area yet, here’s what we can do” message.

- Verify graceful failure.

### EC9: Sexual-services request (auto-ban)

- Customer intake includes explicit sexual request.

- Classifier flags. Customer banned at intake. No match cards. Audit log records.

- Verify ban is enforceable (their WhatsApp number can’t book again easily — at minimum flagged in admin).

### EC10: Yuni offline simulation

- Booking comes in, Yuni doesn’t respond for 4 hours.

- Verify admin still functions (Marcus can take over).

- Verify customer gets a “we’re slower than usual today” auto-message after 2 hours.

- *Auto-message is V0.1; for V0, verify manual workflow only.*

-----

## Classifier eval harness

Lives in `tests/safety-classifier-eval.test.ts`. Owned by Claude Code. Runs in CI on every PR touching the classifier.

### Structure

```typescript

const evalCases: EvalCase[] = [

{

id: "pregnancy_001_clear",

category: "pregnancy",

register: "typed",

input: "I'm 6 weeks pregnant and looking for a relaxing massage",

expected_flags: ["pregnancy"],

expected_kill_switch: true,

notes: "Clear positive"

},

{

id: "pregnancy_002_borderline",

category: "pregnancy",

register: "typed",

input: "We've been trying for a baby and I think I might be in early days",

expected_flags: ["pregnancy"],

expected_kill_switch: true,

notes: "Borderline — should flag conservatively"

},

{

id: "pregnancy_003_dictation",

category: "pregnancy",

register: "dictation",

input: "um yeah so I'm like 6 months pregnant and my back is killing me, like I just need someone to help me um relax",

expected_flags: ["pregnancy"],

expected_kill_switch: true,

notes: "Disfluent dictation register"

},

// ... at minimum 3 per category × 13 = 39 minimum, target 50+

];

```

### Required coverage

- All 13 kill-switch categories

- At least 3 per category: clear positive, borderline, dictation register

- At least 5 confounder cases (mentions related concepts that should NOT flag)

- At least 3 multi-flag cases

- At least 3 edge cases per the “weird inputs” list (empty, very short, very long, mixed languages, all caps)

### Pass criteria

- Clear positives: 100% recall (any miss blocks merge)

- Borderline: ≥80% recall

- Confounders: ≤20% false positive rate

- Provider-safe summary fixture set: 0 instances of private text leaking through

-----

## Provider-safe summary tests

`tests/provider-safe-summary.test.ts`. Owned by Claude Code.

Fixtures contain raw intakes with explicitly private content. Test verifies the generated summary contains none of it.

```typescript

const cases = [

{

raw: "I'm going through a really hard breakup and I just want to feel held but not talk about it",

private_phrases: ["breakup", "going through", "feel held"],

summary_should_contain: ["quiet", "nurturing"],

},

{

raw: "I have PTSD from a car accident and I get triggered by certain types of touch",

private_phrases: ["PTSD", "car accident", "triggered"],

summary_should_contain: ["please ask before", "areas to avoid"],

},

// ...

];

```

-----

## Explanation language tests

`tests/explanation-language.test.ts`. Owned by Claude Code.

Verifies the rank-explain Claude call never produces banned phrases.

```typescript

const banned_phrases = [

"treat", "treatment", "cure", "heal", "diagnos",

"anxiety", "depression", "trauma", "PTSD",

"medical", "therapy", "therapist" // (different from massage therapist context)

];

```

Run against 50 sample explanations. Any banned phrase in any explanation = fail.

-----

## Mobile QA checklist

Run on iPhone Safari + Android Chrome before pre-first-booking gate.

- [ ] Landing page renders within 2s on 4G

- [ ] QR code scan opens app correctly (test with actual phone camera)

- [ ] Intake textarea is large enough to type comfortably

- [ ] Microphone button visible and tappable (44pt minimum touch target)

- [ ] Whisper transcription works on iPhone Safari (iOS audio capture)

- [ ] Whisper transcription works on Android Chrome

- [ ] Follow-up questions display correctly

- [ ] Match cards readable at typical phone width (320-414px)

- [ ] Match cards’ “Availability to be confirmed” badge visible

- [ ] Booking pending page displays WhatsApp link as native link (tappable)

- [ ] Provider-safe summary readable on mobile

- [ ] ToS modal scrolls correctly

- [ ] Form validation errors visible without keyboard hiding them

- [ ] Loading states shown during Whisper / Claude calls

- [ ] Error states shown when API fails

- [ ] No layout shift after fonts load

-----

## API failure tests

### Whisper failure

- Mock Whisper returning 500

- Verify UI shows “voice unavailable, please type”

- Verify intake continues with text

### Claude Call 1 failure (classify_extract)

- Mock Claude returning malformed JSON

- Verify customer sees “we’re taking longer than usual, try again”

- Verify NO match cards generated

- Verify `safety_audit_log` records the failure

### Claude Call 1 timeout

- Mock 30s+ timeout

- Verify graceful timeout, customer sees fallback

- Verify request not silently retried infinitely

### Claude Call 2 failure (rank_explain)

- Same fallbacks

- Verify Yuni gets the intake in admin even without match cards (manual matching path)

### Postgres write failure

- Mock failed `INSERT` on `customer_intakes`

- Verify customer sees error, intake not lost (retry path)

- Verify alert fires (Sentry + email to Marcus)

### Audit log failure

- Mock failed `INSERT` on `safety_audit_log`

- Verify the originating Claude call result is NOT used (operation fails)

- This is the most important failure mode test. The audit log is mandatory.

-----

## Performance budgets

Not strict gates in V0 (we’ll learn from real usage), but track:

- Landing page LCP under 2s on 4G

- Intake submit → match cards under 8s (Claude calls are the bottleneck)

- Admin dashboard load under 3s

- Database query for filtered candidates under 200ms

-----

## What’s not tested in V0

Documented so we know what we accept as risk:

- No load testing — V0 is 20 booking requests over 30 days, traffic is trivial

- No accessibility audit — V1 priority

- No browser support beyond iPhone Safari + Android Chrome

- No internationalization tests — V0 is English-only

- No cross-tenant isolation tests — V0 is single-tenant

- No payment processing tests — no payment processing in V0

-----

## CI configuration

GitHub Actions runs on every PR:

1. Lint + typecheck

1. Unit tests

1. Contract tests (AI schema validation against fixtures)

1. Classifier eval (real Claude API, gated by `CLAUDE_API_KEY` secret)

1. Provider-safe summary tests

1. Explanation language tests

1. Playwright E2E (5 happy paths, 10 edge cases) against staging DB

PR cannot merge if any of 1-3, 5, 6, 7 fail.

PR cannot merge if classifier eval (4) shows any clear-positive failure. Borderline failures are flagged for Marcus review but don’t auto-block.

-----

*Test plan v0.1 · Owned by Codex Cloud + Claude Code · Updated as cases emerge*

post_mvp_roadmap.md

# POST_MVP_ROADMAP.md

**The graveyard of “let’s just add this real quick.”** Owned by Marcus.

If a feature isn’t in `MVP_SPEC.md`, it lives here. This doc exists so agents and humans can see *where* a deferred feature lands without asking. “Is X in V0?” answered by `MVP_SPEC.md`. “When does X happen?” answered here.

-----

## Phase boundaries

- **V0** (Days 1-7 + 30-day validation sprint): the supervised matching loop, end-to-end. Field-ready by Day 7.

- **V0.1** (Weeks 5-8): polish and the things we deliberately cut from V0 to ship faster

- **V1** (Months 2-4): real second iteration after validation sprint signals proceed

- **V2** (Months 5-8): payment rails, premium tier UX, public badges

- **V3** (Year 2): full marketplace payments, multi-city, autonomous ops where reality has earned them

A feature moves from a later phase to an earlier one only by Marcus updating this doc. Agents do not promote features.

-----

## V0.1 (Weeks 5-8)

Things we cut from V0 to keep the budget tight. Add only after validation sprint shows we should keep going.

### Polish

- Better empty/error state designs across customer flow

- Better mobile UI refinements based on real customer behavior

- Loading state animations (the actual content loads fast enough; the perception of speed is the issue)

- Admin UI keyboard shortcuts for Yuni’s repetitive workflows

- Customer-facing FAQ page (currently just a “How it works” modal)

### Capture and ops

- **Yuni voice memo automation** — the deferred-from-V0 feature. WhatsApp bot that transcribes 60-second voice memos and structures into provider DB records. Only after the manual workflow has produced enough structured data that we know what fields actually matter.

- Daily smoke test automation — currently manual, automate as GitHub Action

- Stale booking cleanup — auto-flag bookings stuck in `customer_pending` for 24+ hours

- Auto-message customer if Yuni hasn’t responded in 2+ hours during a confirmed Yuni-offline window

- Bulk operations in admin (mark multiple bookings settled, export commission CSV)

### Better audit and analytics

- Funnel dashboard: scan → intake started → intake completed → match generated → booking requested → confirmed → completed

- Per-channel funnel (which villas convert better)

- Provider performance dashboards (rebook rate per provider, avg customer rating, etc.)

- Net IDR per Yuni-minute trend chart

### Customer experience

- Rebooking flow for repeat customers (still no auth — match by WhatsApp number)

- Customer-side cancellation self-serve (currently requires WhatsApp)

- Ability for customer to upload an image of an injury (medical-relevant context)

- Customer can edit their provider-safe summary before sending (currently view-only)

-----

## V1 (Months 2-4)

After 50+ bookings/month and the validation sprint shows clear go signal.

### Provider experience

- Top-tier providers get a “preferred” badge and better matching weight

- Optional provider availability pings (not full calendar): “you have 3 open slots Friday afternoon, want us to fill them?”

- Private structured feedback for providers to read (not full dashboard, but a digest)

### Customer acquisition expansion

- Track B (nomad) channel activation: coworking partnerships, WhatsApp groups

- Track C (resident) channel activation: customer referral credit system

- Basic SEO landing pages: “AI-matched massage Ubud,” “in-villa massage Ubud,” “post-yoga massage Ubud”

- Influencer / yoga teacher referral codes

### Matching improvements

- Provider weight updates from feedback (post-session feedback adjusts provider matching scores)

- A/B test on the intake design (only viable at 50+ bookings/month)

- Better explanation generation (more specific, less templatey)

### Operations

- Issue ticketing system (currently uses `booking_status_events`; V1 gets dedicated `issues` table)

- Better reconciliation tooling for commissions

- Villa partner dashboard (lightweight — view their referrals, current commissions)

### Legal / compliance

- Bali startup lawyer consultation (per v6.3 Part 18)

- PSE registration if required at user threshold

- UU PDP compliance scoping

- Provider agreements moved from paper to DocuSign or equivalent

- Customer ToS reviewed by counsel before public marketplace positioning

-----

## V2 (Months 5-8)

After Bali V1 has produced 100+ bookings/month and provider network is 30+.

### Payment rails

- Midtrans or Xendit integration for booking deposits

- Customer can prepay with foreign card; provider settles in IDR

- Platform takes commission upfront, releases provider share within 24-48h

- Refunds and disputes handled through payment processor

### Premium tier dedicated UX

- Premium customer experience (higher-touch confirmation, optional video intro from provider)

- Premium provider profiles (longer bios, multiple photos, video)

- Premium pricing displayed differently in match cards

### Public badges (not star ratings)

- “Best for grounding”

- “Strong pressure”

- “Highly rebooked”

- “Great for post-travel”

Driven by aggregated private feedback, never by individual public reviews.

### FX conversion

- Foreign card → IDR settlement to provider bank account

- 2-4% FX margin disclosed to customer

- This is the real provider lock-in moat (per v6.3)

### Multi-language

- Bahasa Indonesia UI option

- French / German / Russian / Chinese intake support (Whisper handles many languages already)

### Spirit vertical (V0 scope expansion)

- Open the Spirit vertical only after Body has 100+ completed bookings and zero major incidents

- Sound healing, Reiki, breathwork, somatic, private yoga, private meditation

- Balian listings only after extended cultural advisory review (per v6.3 Part 9)

- Cultural advisory fund allocation begins (portion of Spirit revenue)

-----

## V3 (Year 2)

Multi-city. Autonomous operations. The platform play.

### Multi-city

- Koh Phangan, Thailand (per v6.3 Part 19)

- Rishikesh or Goa, India (requires local ops partner)

- City launch playbook proven and documented

- Local field agents on Phase 0 commission model

### Autonomous operations (where reality has earned them)

- Provider self-serve calendar (top-performers only, manually verified)

- Same-day instant booking (only for verified-availability providers)

- Auto-confirmation for Tier 1 providers in their default availability windows

- AI-suggested provider matches for Yuni’s review (currently AI matches independently, then Yuni overrides)

### Concierge vertical (per v6.3 Part 7)

- Scooter rental, private driver, day trip

- Babysitter / nanny (vetted, bilingual)

- Private chef

- Villa cleaning, laundry

### Provider tools (SaaS layer)

- Scheduling

- Customer notes

- Income tracker

- Per-customer history (with customer consent)

### City licensing

- Operators in new hubs can pay rev-share to use the Neskala platform and matching

- “Powered by Neskala” partner mode

-----

## Permanently excluded (not roadmap, not ever)

Things that will never be in Neskala. Documented so they don’t get re-litigated.

- **Star rating system** — the v6.3 design says private feedback only, badges in V2. No 4.3-star averages, no “rate your therapist 1-5.” The badge system replaces it.

- **Public reviews** — same reason. Public reviews punish new providers and create platform liability for disputes.

- **Open marketplace self-listing** — Neskala is curated supply. Anyone can apply, Yuni decides.

- **AI as safety decision-maker** — the AI flags. Humans decide. Forever.

- **Medical claims of any kind** — Neskala is wellness, not healthcare. Permanent constraint.

- **Children’s services** — minors are kill-switch flag #12. Never matched.

- **Sexual services** — auto-ban. Permanent.

- **Cryptocurrency payments** — adds compliance burden without solving any customer problem in V0-V3.

- **NFTs / “loyalty tokens”** — not the business.

- **Generative content from customer intake (e.g., “wellness journals”)** — surveillance product. Out of scope ethically.

-----

## How a feature moves up the roadmap

A V0.1 feature can move into V0 only if:

1. Marcus updates `MVP_SPEC.md` to include it

1. The corresponding spec doc (AI_CONTRACTS, DATABASE_SCHEMA, etc.) is updated

1. The build budget allows it without exceeding Week 1 caps

1. The pre-first-booking safety gate doesn’t get a new line item (or does, and the gate is re-reviewed)

A V1 feature does NOT move into V0 in any plausible scenario. If Marcus is tempted, the temptation is the signal that scope is wrong, not that V0 should grow.

A V2 feature absolutely never moves into V0. Anything payment-related, premium-UX-related, or multi-city is structurally V2+.

-----

## Update log

|Date |Change                 |Approved by|

|-----|-----------------------|-----------|

|Day 0|Initial roadmap drafted|Marcus     |

-----

*Roadmap v0.1 · Owned by Marcus · Updated when validation signals shift priorities*
