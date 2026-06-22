---
title: "Neskala Prompt Pack"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/#Neskala/MVP build /Neskala Prompt Pack.docx"
status: reference
privacy: private/internal
tags:
  - product
---

# Neskala Prompt Pack

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# Neskala Prompt Pack

**Sequenced prompts for V0 build.** Copy each section into the named agent. Verify the acceptance criteria before moving to the next.

This file is the operator’s handbook for the week. The spec pack is the constitution; this is the daily orders.

-----

## How to use this file

- **Prompts are numbered by agent + day.** C = Claude Code, P = Replit Agent (Product), X = Codex Cloud.

- **Run in order.** Skipping ahead breaks the build.

- **One prompt per agent session.** Don’t paste two prompts into the same Replit chat — you lose the focus that makes this work.

- **Verify before moving on.** Each prompt has acceptance criteria. If it doesn’t pass, fix in the same agent session before moving to the next prompt.

- **Spec pack is context, not paste-target.** When a prompt says “read X.md,” the agent should be able to access the file in the repo. If you’re in a fresh session without repo access, paste the relevant section as context.

-----

## Pre-flight checklist (before P01 / C01)

Do these once, before any prompt runs.

- [ ] GitHub repo created: `neskala` (private)

- [ ] All 11 spec pack files committed to repo root

- [ ] Neon Postgres database created, connection string saved

- [ ] Anthropic API key generated, saved to password manager

- [ ] OpenAI API key generated (for Whisper), saved

- [ ] Vercel project linked to GitHub repo

- [ ] Sentry project created, DSN saved

- [ ] Replit account ready, GitHub integration enabled

- [ ] Claude Code installed on your machine, authenticated

- [ ] Codex Cloud configured (or Claude Code can run Playwright — your call)

-----

# Day 1 — Scaffold (Claude Code)

Day 1 is Claude Code only. Replit comes Day 2 once the foundation is solid.

-----

## C01 — Repo scaffold

**Agent:** Claude Code

**Estimated cost:** ~$2-4 in Claude API usage

**Out of scope:** any UI, any AI calls, any business logic

### Context

```

Read these files first:

- README.md

- BUILD_BRIEF.md

- AGENTS.md

- MVP_SPEC.md (§ Stack only)

```

### Prompt

```

You are scaffolding the Neskala repo. Read README.md, BUILD_BRIEF.md, and AGENTS.md before starting.

Set up a Next.js 14 (App Router) + TypeScript + Tailwind project with the following structure:

src/

app/

(customer)/

page.tsx                    # landing

intake/page.tsx

match/[intake_id]/page.tsx

booking/[booking_id]/pending/page.tsx

booking/[booking_id]/feedback/page.tsx

tos/page.tsx

privacy/page.tsx

(admin)/

admin/page.tsx

admin/intakes/page.tsx

admin/bookings/page.tsx

admin/providers/page.tsx

admin/providers/new/page.tsx

admin/feedback/page.tsx

admin/audit/page.tsx

api/

intake/route.ts

match/route.ts

booking/route.ts

whisper/route.ts

admin/auth/route.ts

ai/

classifier.ts                 # placeholder, Claude Code will fill Day 3

matcher.ts

summarizer.ts

structure-provider.ts

__fixtures__/

db/

client.ts

schema.ts                     # Drizzle schema, mirroring DATABASE_SCHEMA.md

seed.ts

lib/

auth.ts                       # single-password admin auth

sentry.ts

components/

ui/                           # shared UI components

migrations/                       # SQL files, numbered

tests/

safety-classifier-eval.test.ts  # placeholder

provider-safe-summary.test.ts   # placeholder

explanation-language.test.ts    # placeholder

e2e/                            # Playwright

Required setup:

- pnpm as package manager

- Drizzle ORM for Postgres

- Tailwind with sensible defaults (no custom config yet)

- Sentry initialized but disabled in dev

- ESLint + Prettier

- TypeScript strict mode

- A .env.example with all required keys (DATABASE_URL, ANTHROPIC_API_KEY, OPENAI_API_KEY, SENTRY_DSN, ADMIN_PASSWORD)

- A .gitignore that excludes .env.local, node_modules, .next, .vercel

- A package.json with scripts: dev, build, lint, typecheck, test, db:migrate, db:seed

- Wire up basic layout.tsx with Inter font and Tailwind base styles

Do NOT:

- Write any AI calls. Stub them out as functions that throw "not implemented yet"

- Write any UI beyond a barebones layout

- Generate seed data yet (C02 handles this)

- Create migrations beyond an empty migrations folder

When done, run pnpm install, pnpm typecheck, and pnpm lint. All three must pass.

```

### Acceptance criteria

- [ ] Repo scaffold matches the structure above

- [ ] `pnpm install` completes without errors

- [ ] `pnpm typecheck` passes

- [ ] `pnpm lint` passes

- [ ] `.env.example` has all 5 keys

- [ ] Sentry initialized in `src/lib/sentry.ts` but not throwing in dev

- [ ] First commit pushed to `main`

-----

## C02 — Schema + migrations + seed

**Agent:** Claude Code

**Estimated cost:** ~$3-5

**Out of scope:** any business logic, any AI

### Context

```

Read DATABASE_SCHEMA.md fully. This prompt implements every table, enum, and the state machine constraint.

```

### Prompt

```

You are implementing the V0 database for Neskala. Read DATABASE_SCHEMA.md fully before starting.

Create:

1. SQL migrations in migrations/ numbered 0001 through 0009 as specified in DATABASE_SCHEMA.md. Use raw SQL files, not Drizzle migrations — we want explicit control over enums and constraints.

2. The Drizzle schema in src/db/schema.ts mirroring the SQL. Use Drizzle's pg-core types and enum imports.

3. The check_booking_transition() Postgres function and trigger as specified. The trigger fires on booking_status_events INSERT and validates from_state → to_state against the allowed transitions in DATABASE_SCHEMA.md § State Machine.

4. REVOKE UPDATE and REVOKE DELETE on safety_audit_log and booking_status_events. These tables are insert-only.

5. Seed data in src/db/seed.ts with:

- 8 providers covering the bench distribution (3 Balinese, 2 deep tissue, 2 villa/couples-capable, 1 female specialist)

- All seed providers use names like "Test Provider 1", "Test Provider 2" — never plausible Indonesian names

- 3 referral partners (1 villa, 1 coworking, 1 yoga studio) with referral_codes

- Idempotent: running seed twice doesn't duplicate

6. db:migrate script: applies migrations in order against DATABASE_URL

7. db:seed script: runs seed.ts

Test the full flow:

- pnpm db:migrate against a fresh Neon DB

- pnpm db:seed

- Query providers, confirm 8 rows

- Try to UPDATE a row in safety_audit_log, confirm it's rejected

- Insert a booking_status_events with an invalid transition, confirm it's rejected

Do NOT:

- Add any business logic

- Add any auth

- Skip the immutability constraints (these are load-bearing for the audit log)

When done, document the test commands in a NOTES section in the PR description.

```

### Acceptance criteria

- [ ] All 9 migrations apply cleanly to a fresh DB

- [ ] Seed creates 8 providers with realistic field distribution

- [ ] Audit log UPDATE attempt rejected at DB level

- [ ] Invalid state transition rejected at DB level

- [ ] Drizzle schema matches SQL one-to-one

- [ ] PR merged to main

-----

# Day 2 — Vertical slice (Replit Agent)

Day 2 is Replit territory. Build the visible product end-to-end with mocked AI. Customer can complete a booking flow without any real Claude calls happening yet.

-----

## P01 — Landing page

**Agent:** Replit Agent

**Estimated Replit credit:** ~$5-10

**Out of scope:** any AI, any DB writes, any auth

### Context paste at top of session

```

Project: Neskala — AI matching for Bali wellness bookings.

Stack: Next.js 14 App Router + Tailwind + Drizzle/Postgres on Neon.

You own VISIBLE PRODUCT only. Never touch: classifier code, AI contracts, audit log writers, state machine, DB migrations.

Read in repo:

- BUILD_BRIEF.md (full)

- MVP_SPEC.md § Customer-facing pages → Landing page (just this section)

- AGENTS.md § The 8 non-negotiable rules

Then build.

```

### Prompt

```

Build the landing page at src/app/(customer)/page.tsx.

Requirements (from MVP_SPEC.md):

- Headline: "Feel sore, tired, or overstimulated? We'll match you with a trusted Bali bodywork practitioner."

- Subhead: "Tell us how your body and mind feel today. We'll recommend three vetted local practitioners who fit your needs, your preferences, and your villa."

- Trust row: 6 small icon+text items (use lucide-react icons)

- Personally vetted practitioners (Shield icon)

- In-villa or in-area sessions (Home icon)

- WhatsApp confirmation before anyone arrives (MessageCircle icon)

- You choose gender preference (Users icon)

- Wellness only — never sexual services (HeartHandshake icon)

- Cash or QRIS direct to provider (Wallet icon)

- Primary CTA: "Find my match →" button, links to /intake

- Secondary link: "How it works" — opens a simple modal with 4 short steps

- Footer with links to /tos and /privacy (placeholder pages OK)

Design notes:

- Mobile-first, 320-414px primary

- Calm, warm tone — not legalistic

- Use a soft natural palette: warm neutrals, soft greens or terracotta accents

- Inter font (already configured)

- The page should feel like landing somewhere trustworthy at 9pm in a villa, not like an insurance form

- Do NOT use stock wellness photography — we don't have provider photos yet

- Do NOT add a hero image. Type-first design.

- Read URL query param ?ref=PRT123 — store in sessionStorage as referral_code (we'll wire to DB in P03)

Page must:

- Load in under 2s on simulated 4G (Lighthouse mobile)

- Be visually clean on iPhone Safari and Android Chrome

- Pass typecheck and lint

Out of scope:

- DB calls

- Auth

- Modal animation libraries (use a basic state-driven modal)

```

### Acceptance criteria

- [ ] Page renders at `/` matching the description

- [ ] All 6 trust-row icons visible and labeled

- [ ] CTA links to `/intake`

- [ ] “How it works” modal opens and closes

- [ ] `?ref=PRT123` stored in sessionStorage

- [ ] Mobile screenshot at 375px wide looks clean

- [ ] Lighthouse mobile performance >85

-----

## P02 — Intake page (text-only first pass)

**Agent:** Replit Agent

**Out of scope:** Whisper integration (P08 adds it), real Claude calls (P06 adds them)

### Context paste

```

Read in repo:

- BUILD_BRIEF.md (full)

- MVP_SPEC.md § Customer-facing pages → /intake

- AI_CONTRACTS.md § Pipeline overview (just to understand the data shape)

You own VISIBLE PRODUCT only.

```

### Prompt

```

Build the intake page at src/app/(customer)/intake/page.tsx.

Stage 1 (initial open question):

- Single large textarea

- Prompt: "Rough day? Tell us how your body and mind are feeling right now."

- Below: hint text "Or tap the mic to speak. Up to 90 seconds." — but the mic button is a placeholder DIV for now (P08 wires Whisper). Mark it disabled, show "Voice coming soon" tooltip.

- ToS acknowledgment checkbox: "I agree to the Terms of Service" with link to /tos

- Submit button "Continue" — disabled until textarea has content AND ToS checked

Stage 2 (follow-ups, after submitting Stage 1):

Show 5 follow-up questions in a single scrollable card:

1. Health considerations textarea (optional, label: "Any areas, injuries, or health considerations we should know about before matching you?")

2. Gender preference radios: female / male / either / no_preference

3. Timing radios: today / tomorrow / this_week / flexible

4. Location text input + budget range radios: 350-500k / 500-800k / 800k+ / open

5. Contact: WhatsApp number text input

Optional woo-level slider, shown only after primary fields filled: practical / open_to_intuition / spiritual / surprise

Submit button on Stage 2: "Get my matches"

On Stage 2 submit:

- POST to /api/intake with the full payload

- API returns mocked response: { intake_id: "mock-uuid", routed_to_human_review: false }

- Redirect to /match/[intake_id]

- If routed_to_human_review: true, redirect to /intake/review-pending instead

The /api/intake route should:

- Accept the payload

- For now, return a hardcoded mock response (Claude Code wires real classifier in C03)

- ALSO: hardcode 1 trigger word handling — if raw_intake_text contains "pregnant" or "pregnancy" return routed_to_human_review: true. This is so we can test the kill-switch path before the real classifier exists.

Build /intake/review-pending page too:

- "Thanks — we want to match you safely. Our team will reach out within an hour."

- Display the WhatsApp number they entered (if provided)

- Calm, no-pressure tone

Design:

- Mobile-first

- Stage 1 textarea is minimum 6 rows, visually inviting

- Don't shrink the touch target on the mic button placeholder — minimum 44pt

- Form validation errors visible above keyboard on mobile

- Loading state on submit (spinner + "Finding your matches…")

Out of scope:

- Real Whisper integration (P08)

- Real Claude classifier (C03)

- Voice input (P08)

- Saving intake to DB (P06 wires this)

```

### Acceptance criteria

- [ ] Stage 1 form renders, ToS checkbox blocks submit until checked

- [ ] Stage 2 form renders all 5 questions

- [ ] Mock API responds in under 500ms

- [ ] “pregnant” trigger word routes to /intake/review-pending

- [ ] All other paths route to /match/:id

- [ ] Mobile keyboard doesn’t hide validation errors

-----

## P03 — Match results page (mocked)

**Agent:** Replit Agent

**Out of scope:** Real ranking (C03/P07 add it)

### Context paste

```

Read:

- MVP_SPEC.md § Customer-facing pages → /match/:intake_id

- DATABASE_SCHEMA.md § providers (just the table fields, to know what data shape to mock)

```

### Prompt

```

Build the match results page at src/app/(customer)/match/[intake_id]/page.tsx.

Show 3 provider cards. Each card:

- Provider photo placeholder (initials in a circle, soft color)

- First name + last initial (e.g., "Wayan S.")

- Two-sentence explanation (use mock data for now — see below)

- "Availability to be confirmed" badge — small, gray, prominent enough to be noticed

- "Request booking with [Name]" primary button

Below the 3 cards:

- "Or, you choose — let Yuni recommend after a quick chat" link → opens manual review request modal

Footer:

- Small "How matching works" link → modal explaining classifier + filter + rank + human confirm

Mock data:

The page reads ?intake_id from URL. For V0 mock, hardcode 3 mock match cards regardless of intake_id. Use these mock providers:

1. Wayan S. — "Wayan is matched to you because you mentioned emotional heaviness alongside physical depletion and asked for a quieter session. She specialises in nervous-system-aware traditional Balinese massage and is typically available within 24 hours."

2. Made R. — "Made is matched to you because you mentioned tight shoulders and travel fatigue. He's known for grounding deep-tissue work and works in-villa across Ubud."

3. Kadek L. — "Kadek is matched to you because you asked for a female practitioner and mentioned hip tension. She specialises in post-yoga recovery and is highly rebooked by long-stay residents."

When user clicks "Request booking with [Name]":

- POST to /api/booking with { intake_id, provider_id }

- Mock API returns { booking_id: "mock-booking-uuid" }

- Redirect to /booking/[booking_id]/pending

Manual review request:

- Modal with textarea: "Tell Yuni what you're looking for, and she'll match you over WhatsApp."

- Submit creates a booking with state="customer_requested" and a flag indicating manual matching needed

- Mock returns booking_id, redirects to pending page

Design:

- Cards stack vertically on mobile, side-by-side on desktop (3-up)

- Calm, scannable. No urgency framing.

- "Availability to be confirmed" badge does work — explain in tooltip on tap

- The explanation is the most important text on the page. Make it readable.

Out of scope:

- Real ranking

- Real provider data from DB (use the mock above)

- Provider photos (use initials circles)

```

### Acceptance criteria

- [ ] 3 cards render with mock data

- [ ] “Request booking” button POSTs and redirects

- [ ] Manual review modal works

- [ ] “How matching works” modal explains the pipeline

- [ ] Mobile layout is single-column, scannable

-----

## P04 — Booking pending page

**Agent:** Replit Agent

### Prompt

```

Build src/app/(customer)/booking/[booking_id]/pending/page.tsx.

Read MVP_SPEC.md § Customer-facing pages → /booking/:booking_id/pending.

Page content:

- Confirmation message: "Got it. Yuni from our team will message you on WhatsApp within 30 minutes to confirm [Provider]'s availability. She'll send a short brief about what to expect, the address she's coming to, and how to pay (cash or QRIS, direct to her). If anything changes, message us back."

- Booking summary card:

- Provider name (mock for now)

- Service ("60-min Balinese massage")

- Requested time (from intake)

- Location (from intake)

- Estimated price range

- Yuni's WhatsApp number as a tappable native link (use Yuni's real number from env: WHATSAPP_YUNI_NUMBER)

- Provider-safe summary section:

- Heading: "What Yuni will share with [Provider]"

- The mock summary text (use a placeholder for now — C04 generates this for real)

- Calm framing: "We only share what's needed for your session. Your full intake stays private."

For V0 mock:

- /api/booking returns the mock booking, including a placeholder provider_safe_summary like: "Customer prefers a quiet, nurturing session. Mentioned post-flight depletion and tight shoulders. Avoid heavy conversation."

Design:

- Calm, settled feel — they've made the choice, this is the "good, you're in good hands" page

- Don't show a loading spinner here unless data is actually loading

- The WhatsApp number should be the most actionable element on the page

Out of scope:

- Real provider_safe_summary (C04)

- DB writes (P06 wires this)

- Booking state polling (V0.1 maybe)

```

### Acceptance criteria

- [ ] Page renders with all sections

- [ ] WhatsApp link opens the messaging app on mobile

- [ ] Provider-safe summary visible and editable framing is clear

- [ ] Looks calm and settled, not anxious

-----

## P05 — Admin shell + auth

**Agent:** Replit Agent

### Context paste

```

Read:

- MVP_SPEC.md § Admin-facing pages

- AGENTS.md § The 8 non-negotiable rules

Single-password admin auth. No customer-side auth ever.

```

### Prompt

```

Build the admin shell.

1. Auth (src/lib/auth.ts):

- Single shared password from ADMIN_PASSWORD env var

- POST /api/admin/auth checks password, sets a httpOnly signed cookie valid 12 hours

- Middleware in src/middleware.ts protects all /admin/* routes

- Unauthenticated /admin/* requests redirect to /admin/login

- Use iron-session or @vercel/edge-config style minimal session, NOT NextAuth (we're not adding the complexity)

2. Login page src/app/(admin)/admin/login/page.tsx:

- Single password field

- Subtle branding — this is for Marcus and Yuni only

- Error state if wrong password

- Rate limiting: 5 failed attempts per IP per 15 min, return 429

3. Admin layout (src/app/(admin)/admin/layout.tsx):

- Sidebar nav: Dashboard / Intakes / Bookings / Providers / Feedback / Audit Log

- Top bar: "Logged in" + Logout button

- Mobile: collapsible drawer nav

4. Dashboard page (src/app/(admin)/admin/page.tsx):

- 4 stat cards: today's intakes / today's bookings / this week's revenue / Net IDR per Yuni-min

- Today's booking queue table (mock data for now): customer name, provider, requested time, status, last action

- Today's intakes flagged for human review table (mock for now)

For now, stat cards and tables show mock data. Real data wires up in P09.

Out of scope:

- Real DB queries (P09)

- WhatsApp templates (P09)

- Detail views beyond dashboard (later prompts)

```

### Acceptance criteria

- [ ] /admin redirects to /admin/login when unauthenticated

- [ ] Correct password sets cookie, redirects to /admin

- [ ] Wrong password shows error

- [ ] 5 failed attempts in 15 min returns 429

- [ ] Logout button clears cookie

- [ ] Sidebar nav renders, mobile drawer works

- [ ] Dashboard shows mock stat cards

-----

## End of Day 2 checkpoint

Smoke test before EOD:

1. Open `/?ref=PRT001` in mobile browser

1. Click “Find my match”

1. Type intake, accept ToS, continue

1. Fill follow-ups, submit

1. See 3 mock match cards

1. Click “Request booking with Wayan S.”

1. See pending page with WhatsApp link

1. Open `/admin/login`, log in, see dashboard

If all 8 work, commit and end the day. If something breaks, fix in the same Replit session.

-----

# Day 3 — Safety classifier (Claude Code)

Day 3 is Claude Code only. No Replit work. Safety-critical code is built carefully.

-----

## C03 — Classifier prompt + AI contracts layer

**Agent:** Claude Code

**Estimated cost:** $5-10 (a lot of testing during dev)

**Out of scope:** match ranking (C04 handles), provider-safe summary (C04 also)

### Context

```

Read fully:

- AI_CONTRACTS.md (entire doc)

- SAFETY_AND_TRUST.md § The 13-category kill-switch + § Self-harm and SI special handling

- MVP_SPEC.md § AI pipeline

```

### Prompt

```

You are implementing the safety classifier and intake state extractor (Call 1 in AI_CONTRACTS.md).

1. Build src/ai/classifier.ts:

- Function: classifyAndExtract(input: ClassifyExtractInput): Promise<ClassifyExtractOutput>

- Calls Anthropic Messages API with model claude-opus-4-7

- System prompt structured per AI_CONTRACTS.md § Call 1 → System prompt structure

- Output strictly matches the ClassifyExtractOutput TypeScript interface — validate with Zod after parsing

- On invalid JSON: throw ClassifierFailure with failure_mode='invalid_json'

- On schema mismatch: throw ClassifierFailure with failure_mode='schema_mismatch'

- On timeout (>30s): throw ClassifierFailure with failure_mode='timeout'

- On rate limit: throw with failure_mode='rate_limit'

- Every call (success OR failure) writes to safety_audit_log synchronously BEFORE returning

- Audit log write failure → throw the audit error, do NOT return classifier result

2. Build src/ai/types.ts with all TypeScript types from AI_CONTRACTS.md:

- ClassifyExtractInput, ClassifyExtractOutput, SafetyFlag (matches DB enum), etc.

- Export Zod schemas for runtime validation

3. Wire into /api/intake/route.ts (replace the mock from P02):

- Accept the payload

- Call classifyAndExtract

- If kill_switch_fired: return { intake_id, routed_to_human_review: true }

- If clear: insert customer_intakes row, return { intake_id, routed_to_human_review: false }

- All DB writes synchronous, all errors propagate

4. Add fixtures in src/ai/__fixtures__/:

- classifier-pregnancy.json

- classifier-clear.json

- classifier-self-harm.json

- classifier-trauma.json

- classifier-multi-flag.json

- classifier-confounder-yoga-soreness.json (should NOT flag)

5. Add MOCK_CLAUDE env var support:

- When MOCK_CLAUDE=true, classifier returns fixtures based on input keywords (Replit dev)

- When false, real API call

6. Cost tracking:

- Every successful call calculates cost from token counts (sonnet/opus pricing)

- Logged to safety_audit_log.cost_usd

- If daily cost exceeds $10, log warning to Sentry

- If approaching $100 weekly cap, throw an explicit BudgetExceeded error

Test:

- Run classifier on each fixture's expected input

- Verify outputs match expected flags

- Verify audit log row created for each

- Verify cost_usd populated

- Force a Claude API timeout (mock 35s delay), verify ClassifierFailure thrown and audit log row written with failure_mode

Do NOT:

- Build the eval harness yet (that's C04, in parallel session OR right after this prompt)

- Build the matcher (C04)

- Touch /api/match endpoint

- Modify any UI

When done: commit, push, smoke-test by running pnpm dev and submitting an intake with "I'm 6 weeks pregnant" — should route to human review.

```

### Acceptance criteria

- [ ] classifyAndExtract works on real Claude API for all 6 fixtures

- [ ] Audit log written synchronously, blocks return on failure

- [ ] /api/intake routes pregnancy mention to human review

- [ ] /api/intake routes clear intake to /match

- [ ] MOCK_CLAUDE=true works for Replit dev

- [ ] Cost tracking writes to DB

- [ ] All TypeScript strict, all Zod-validated

-----

## C04 — Eval harness + matcher + summarizer

**Agent:** Claude Code

**Estimated cost:** $10-20 (running 50+ classifier calls in eval is the bulk)

### Context

```

Read fully:

- AI_CONTRACTS.md § Call 2 + § Call 3

- SAFETY_AND_TRUST.md § The classifier eval harness + § Provider-safe summary

- TEST_PLAN.md § Classifier eval harness

```

### Prompt

```

Three things in this prompt. They're related and share fixture infrastructure.

PART A — Classifier eval harness

Build tests/safety-classifier-eval.test.ts.

Structure:

- evalCases array with 50+ entries

- At minimum 3 per kill-switch category (clear / borderline / dictation)

- At minimum 5 confounder cases (related concepts that should NOT flag)

- At minimum 3 multi-flag cases

- At minimum 3 weird-input cases (empty, very long, all caps, mixed languages)

Each case:

{

id: string,                    // e.g. "pregnancy_001_clear"

category: SafetyFlag | "confounder" | "multi_flag" | "edge",

register: "typed" | "dictation",

input: string,

expected_flags: SafetyFlag[],

expected_kill_switch: boolean,

notes: string

}

Test runner:

- Calls classifyAndExtract on each

- Compares actual vs expected flags

- Pass criteria from SAFETY_AND_TRUST.md:

- Clear positives: 100% recall (any miss = test fail)

- Borderline: ≥80% recall

- Confounders: ≤20% false positive rate

- Outputs a summary report: per-category recall, FP rate, total cost

- Marks PR-blocking if clear-positive recall <100%

Run the eval once, save the report to tests/eval-results/eval-baseline.md (committed).

If any clear-positive fails, iterate the classifier prompt in src/ai/classifier.ts until they pass.

PART B — Match generator (Call 2)

Build src/ai/matcher.ts:

- Function: rankAndExplain(input: RankExplainInput): Promise<RankExplainOutput>

- Calls claude-sonnet-4-6

- Input: intake state + filtered candidate providers (already filtered by hard rules in Postgres)

- Output: 3 ranked matches with 2-sentence explanations

- Strict JSON output, Zod validated

- Audit log row written synchronously

- Banned phrases enforced via tests/explanation-language.test.ts (Part D below)

Wire into /api/match/route.ts:

- Reads intake_id from request

- Loads customer_intakes row

- Builds Postgres query from extracted_state + hard_filters: filter providers by tier, gender, language, certifications, location radius

- Calls rankAndExplain on filtered candidates

- Inserts match_results row

- Returns 3 matches

If fewer than 3 candidates returned by Postgres:

- Return only what we have (1 or 2 matches)

- Page handles this gracefully (P07 will update UI)

PART C — Provider-safe summary

Build src/ai/summarizer.ts:

- Function: generateProviderSafeSummary(rawIntake, extractedState): Promise<string>

- Calls claude-sonnet-4-6 with explicit "no private content" instruction

- Output: 2-4 sentences, session-relevant only

Wire into /api/intake/route.ts (after classify-extract, before return):

- Generate summary

- Save to customer_intakes.provider_safe_summary

- Returned to client on /booking/:id/pending

Build tests/provider-safe-summary.test.ts:

- 10 fixture cases with raw intakes containing explicitly private content

- Verify summary contains NONE of the private phrases

- Verify summary contains relevant session info

- This test is PR-blocking

PART D — Explanation language test

Build tests/explanation-language.test.ts:

- Banned phrases list per SAFETY_AND_TRUST.md (medical, treat, cure, heal, diagnose, anxiety, depression, trauma, PTSD, therapy)

- Run rankAndExplain on 50 sample inputs (use the fixtures from Part A)

- Assert: no explanation contains any banned phrase

- PR-blocking

When done:

- All 4 parts committed in single PR

- Eval baseline report attached to PR description

- Cost report: $X spent on this prompt

Do NOT:

- Modify customer-facing UI (P07 handles intake → real match wiring on customer side)

- Touch the booking state machine (C05)

```

### Acceptance criteria

- [ ] Classifier eval passes on 50+ cases, 100% clear-positive recall

- [ ] Matcher returns 3 explanations meeting language constraints

- [ ] Provider-safe summary fixture tests pass

- [ ] Explanation language test passes

- [ ] All 3 AI calls write to audit log synchronously

- [ ] PR merged with eval baseline report

-----

# Day 4 — Wire it up + Whisper (Replit + parallel Claude Code)

Day 4 connects what Replit built (Day 2 visible product) to what Claude Code built (Day 3 safety pipeline). Plus Whisper.

-----

## P06 — Wire intake to real classifier

**Agent:** Replit Agent

**Out of scope:** Whisper (P08), match ranking (P07)

### Prompt

```

The /api/intake endpoint is now real (Claude Code wired classifier in C03).

Update src/app/(customer)/intake/page.tsx:

- Stage 2 submit POSTs the full payload to /api/intake

- Show loading state: "Reading your intake…" with subtle animation

- Loading should hold for up to 30s before showing timeout error

- On success { intake_id, routed_to_human_review: false }: redirect to /match/[intake_id]

- On routed_to_human_review: true: redirect to /intake/review-pending

- On 5xx error: show "We're taking longer than usual — try again in a moment" with retry button

Update /api/intake response handling:

- It's now real — keep the client code resilient to errors

- Sentry capture on any 5xx

Update src/middleware.ts or env config:

- Make sure ANTHROPIC_API_KEY is wired

- Make sure MOCK_CLAUDE=true defaults in dev (Marcus toggles to false when ready)

Test:

- With MOCK_CLAUDE=true, intake flow works as before (mock fixtures based on keyword)

- With MOCK_CLAUDE=false (or unset), real API calls happen

- Verify cost_usd in safety_audit_log after a real submission

Do NOT:

- Touch classifier code itself (Claude Code's domain)

- Add audio upload / Whisper (P08)

```

### Acceptance criteria

- [ ] Real classifier called from production-style flow

- [ ] Loading state shown during call

- [ ] Timeout error shown after 30s

- [ ] Success redirects to /match/:id with real intake_id from DB

- [ ] Audit log row created per submission

-----

## P07 — Wire match results page to real ranking

**Agent:** Replit Agent

### Prompt

```

The /api/match endpoint is now real (Claude Code wired matcher in C04).

Update src/app/(customer)/match/[intake_id]/page.tsx:

- Fetch /api/match?intake_id=[id]

- Render the actual matches returned (1-3 cards)

- If 0 matches returned: show "We didn't find a perfect fit — Yuni will recommend over WhatsApp" and trigger manual matching flow

- If 1-2 matches: still show, prefix with "Here's what we have so far"

Provider photo handling:

- If provider has photo_url: render <img>

- If null: render initials circle with deterministic color from name hash

"Request booking with [Name]" button:

- POSTs to /api/booking with { intake_id, selected_provider_id, requested_datetime, location, contact_whatsapp }

- /api/booking should be real now — creates booking_requests row in 'customer_requested' state

- Redirect to /booking/[booking_id]/pending

Manual review request:

- Modal POSTs to /api/booking with manual_match: true flag

- Creates booking_requests with selected_provider_id NULL and manual_match flag set

- Yuni picks provider from admin

Update /booking/:id/pending:

- Now reads real booking from DB

- Real provider_safe_summary from customer_intakes row

Test:

- Submit intake → real classifier → real match → real booking → real DB row

- Verify booking_status_events row created with from_state=NULL, to_state='customer_requested'

- Verify Yuni's admin sees the new booking

Do NOT:

- Modify booking state machine

- Modify match ranking

```

### Acceptance criteria

- [ ] Real matches render from DB

- [ ] Booking creation creates DB row + state event

- [ ] Yuni admin sees the new booking

- [ ] Empty/partial match results handled gracefully

-----

## P08 — Whisper integration

**Agent:** Replit Agent

### Context paste

```

Read:

- AI_CONTRACTS.md § Whisper transcription

- AGENTS.md § Rule 1 (audio is never stored)

```

### Prompt

```

Add Whisper voice input to the intake page.

1. Build src/app/api/whisper/route.ts:

- Accepts multipart/form-data POST with audio blob

- Forwards to OpenAI Whisper API (whisper-1) with language=en

- Returns { text: transcript } on success

- Returns { error: "voice_unavailable" } on any failure

- After transcription, the audio buffer is freed — DO NOT save to disk, S3, or anywhere persistent

- Logs transcript length and duration to a basic counter (no audio content)

- Sentry on errors

2. Update intake page mic button:

- Use the MediaRecorder API (no third-party libs)

- Tap to start recording, tap to stop, max 90s auto-stop

- Visual feedback: pulsing indicator while recording, countdown to 90s

- On stop: send blob to /api/whisper, show "Transcribing…"

- Populate textarea with transcript

- User can edit transcript before submitting (this is important — Whisper makes mistakes)

- On error: show "Voice unavailable, please type" inline (not a modal)

3. Set input_source on intake submission:

- typed: user typed without using mic

- whisper_voice: user used mic, accepted transcript without editing

- whisper_voice: user used mic, edited transcript (still counts as voice — they started with voice)

Actually: just track if mic was tapped. If yes → whisper_voice. If no → typed.

4. Browser support:

- iPhone Safari (iOS 17+): MediaRecorder requires user gesture, audio/mp4 codec

- Android Chrome: MediaRecorder webm/opus

- Test both before commit

Privacy notes for users:

- Below mic button (small text): "Audio is transcribed and immediately discarded. Only the text is saved."

Test:

- Record 30s on iPhone Safari, transcript appears

- Record 30s on Android Chrome, transcript appears

- Verify NO audio file in /tmp, no audio in DB, no audio in any logs

- Force /api/whisper to fail (block in network tab) — UI shows fallback gracefully

Do NOT:

- Save audio anywhere

- Add audio retention "for QA"

- Add "play back what I said" feature (would require audio storage)

```

### Acceptance criteria

- [ ] Mic button records, sends to Whisper, transcribes, populates textarea

- [ ] User can edit transcript before submission

- [ ] No audio file persisted anywhere (verified by inspection)

- [ ] input_source correctly tracked

- [ ] Failure mode shows “voice unavailable, please type”

- [ ] Privacy disclosure visible

-----

## P09 — Admin booking detail + WhatsApp templates

**Agent:** Replit Agent

### Context paste

```

Read:

- MVP_SPEC.md § Admin-facing pages → /admin/bookings

- OPS_PLAYBOOK.md § Booking confirmation workflow

```

### Prompt

```

Build out the admin booking workflow.

1. /admin/bookings page (list view):

- Real data from booking_requests JOIN customer_intakes JOIN providers

- Columns: customer first name, provider name, requested time, status, last_action_at, ops_minutes_logged

- Sortable by status and requested time

- Filter: state, today/week/all

- Click row → /admin/bookings/[id]

2. /admin/bookings/[id] detail page:

- Full intake (raw_intake_text, parsed state)

- Provider-safe summary (read-only display, with note that customer also saw this)

- Matched provider details + alternative ranks

- WhatsApp message templates with copy buttons:

- "To provider (request)": pre-filled with provider name, customer brief, time

- "To customer (confirmed)": pre-filled with provider name, address, time, price

- "To customer (alternative)": pre-filled for offering rank-2 match

- State transition controls:

- Buttons for valid next states from current state

- Reason text required for non-default transitions

- Manual override: "Pick different provider" → opens provider list, swaps match

- Ops time stopwatch:

- "Start working on this booking" button

- Tracks elapsed minutes

- "Stop" saves to ops_time_log with this booking_id

- Audit log section (last 10 events for this booking)

3. State transition API:

- POST /api/admin/booking/[id]/transition with { to_state, reason, notes }

- Validates against state machine (DB enforces; client-side just hides invalid options)

- Inserts booking_status_events row with actor='yuni' or 'marcus' (based on session)

4. WhatsApp templates (reference OPS_PLAYBOOK.md):

- Templates stored in src/lib/whatsapp-templates.ts

- Pre-fill from booking data

- One-click copy to clipboard, with toast confirmation

Test:

- View a booking from a fake intake

- Copy provider WhatsApp template, verify it has the right data

- Transition state from customer_requested → provider_pending → provider_confirmed → customer_confirmed

- Verify each transition wrote to booking_status_events

- Try an invalid transition (e.g., customer_requested → completed), verify it's rejected

Do NOT:

- Modify state machine logic itself (Claude Code's C05 owns)

- Build provider profile editing yet (P10)

```

### Acceptance criteria

- [ ] Booking list shows real DB data, filterable

- [ ] Detail page shows full booking context

- [ ] WhatsApp copy buttons work

- [ ] State transitions write to event stream

- [ ] Ops time logging works

- [ ] Invalid transitions rejected by DB

-----

## P10 — Provider create form + structure-this button

**Agent:** Replit Agent

### Context paste

```

Read:

- MVP_SPEC.md § Admin-facing pages → /admin/providers/new

- AI_CONTRACTS.md § Call 3: Structure provider intake notes

- OPS_PLAYBOOK.md § Provider interview workflow

```

### Prompt

```

Build /admin/providers/new and the supporting "structure this" Claude call.

1. Form structure (mirroring providers table from DATABASE_SCHEMA.md):

- Name, photo upload (or URL), bio, own_words

- Location, travel_radius_km

- Archetypes (multi-select: 5 V0 archetypes)

- Tier (default tier_2)

- Modalities (multi-text-input)

- Pressure style, energy style

- Best client types (multi-text-input)

- Languages, English level

- Gender

- Certifications (multi-text-input)

- Availability notes

- Price range min/max

- Boundaries notes

- Internal notes (Yuni-only flag, hidden from any customer-facing path)

- Customer track fit (multi: A, B, C)

2. "Structure this for me" panel (above the structured fields):

- Big textarea: "Paste interview notes here"

- Button: "Structure for me"

- Calls /api/admin/structure-provider with the raw text

- /api/admin/structure-provider:

- Calls structureProviderNotes() in src/ai/structure-provider.ts (Claude Code built this in C04 or builds in C05? Verify and build if not)

- Returns suggested_fields per AI_CONTRACTS.md § Call 3

- On response: pre-fills form fields with suggestions, highlighting changes

- Yuni edits, then saves

- "gaps" section displayed if Claude couldn't extract certain fields ("price not mentioned, please fill manually")

Photo upload:

- If photo_url provided as URL: just save the URL

- If actual file upload: out of V0 (use Cloudinary URL or skip)

3. Save handler:

- POST /api/admin/providers

- Validates required fields

- Inserts providers row

- Returns provider_id

4. Edit existing provider:

- /admin/providers/[id]/edit reuses the same form, pre-filled

- Save = UPDATE

Test:

- Paste sample interview notes, click "Structure for me"

- Verify Claude returns suggested fields

- Edit, save, verify provider appears in /admin/providers list

- Verify the provider can now appear as a match candidate (run intake that should match them)

Do NOT:

- Build photo upload infrastructure (V0.1)

- Add reference verification fields (V0.1)

- Save audio of interviews (never)

```

### Acceptance criteria

- [ ] Form renders with all provider fields

- [ ] “Structure for me” Claude call works

- [ ] Suggested fields pre-fill, Yuni can edit

- [ ] Save creates provider row

- [ ] Edit flow works

- [ ] New provider can be matched in subsequent intakes

-----

# Day 5 — State machine + audit + tests (Claude Code + Codex)

Day 5 hardens the safety-critical layer. Two sessions in parallel.

-----

## C05 — State machine reinforcement + audit completeness

**Agent:** Claude Code

### Context

```

Read:

- DATABASE_SCHEMA.md § Booking state machine (full)

- SAFETY_AND_TRUST.md § Audit log integrity

- AI_CONTRACTS.md § Audit log writes

```

### Prompt

```

Audit the state machine and audit log for completeness.

1. Verify the check_booking_transition trigger is enforcing ALL transitions in DATABASE_SCHEMA.md.

- Write a test that attempts every invalid transition pair and verifies rejection

- Write a test that attempts every valid transition and verifies acceptance

- tests/state-machine.test.ts — comprehensive

2. Verify every place state changes in the codebase:

- /api/intake creates intake_started → match_generated transition

- /api/match creates customer_requested transition (after user picks)

- /api/booking creates the customer_requested transition

- /api/admin/booking/[id]/transition creates state changes

- For each: verify booking_status_events row written with correct from_state, to_state, actor, reason

3. Write a "transitionTo" helper in src/db/state-machine.ts:

- Single function that wraps the SQL INSERT into booking_status_events

- All state transitions in the codebase MUST go through this helper

- Refactor any direct INSERTs to use it

- Helper signature: transitionTo({ booking_id, to_state, actor, reason, notes? })

4. Audit log completeness sweep:

- Every Claude API call writes to safety_audit_log (verify in classifier.ts, matcher.ts, summarizer.ts, structure-provider.ts)

- Every state transition writes to booking_status_events (verified above)

- Every manual override writes to safety_audit_log with manual_overrides field populated

- No try/catch wrapping audit writes that swallows failures (grep for it, fix any instance)

5. Run the audit log immutability test:

- Try UPDATE on safety_audit_log → expect error

- Try DELETE on safety_audit_log → expect error

- Same for booking_status_events

- Test in tests/audit-immutability.test.ts

Test:

- pnpm test runs all of state-machine.test.ts, audit-immutability.test.ts

- All pass

Do NOT:

- Change the state list (it's locked in spec)

- Add new states without updating spec first

```

### Acceptance criteria

- [ ] All transitions enforced in DB and tested

- [ ] transitionTo helper used everywhere state changes

- [ ] Audit writes verified in all AI calls and state changes

- [ ] No swallowed audit errors (grep clean)

- [ ] Immutability tests pass

-----

## X01 — Playwright E2E for happy paths + edge cases

**Agent:** Codex Cloud (or Claude Code with Playwright)

### Context

```

Read:

- TEST_PLAN.md § Five happy paths + § Ten edge cases

```

### Prompt

```

Build Playwright E2E tests covering 5 happy paths and 10 edge cases from TEST_PLAN.md.

Setup:

- Playwright installed, configured for Chromium + WebKit (Safari surrogate)

- Tests run against a staging DB seeded fresh each test run

- Use page.route() to mock external APIs (Whisper, Claude) during tests

- Real DB, real Postgres, mocked AI

Tests in tests/e2e/:

- happy-1-tourist.spec.ts (HP1 from TEST_PLAN.md)

- happy-2-nomad-rebook.spec.ts (HP2)

- happy-3-resident.spec.ts (HP3)

- happy-4-couples.spec.ts (HP4)

- happy-5-healer.spec.ts (HP5)

- edge-1-provider-unavailable.spec.ts

- edge-2-customer-silent.spec.ts

- edge-3-double-booking.spec.ts

- edge-4-language-mismatch.spec.ts

- edge-5-payment-confusion.spec.ts (mostly admin verification)

- edge-6-customer-reschedules.spec.ts

- edge-7-late-night.spec.ts

- edge-8-out-of-area.spec.ts

- edge-9-sexual-services.spec.ts

- edge-10-yuni-offline.spec.ts

For each:

- Setup state (seed providers, seed intake if needed)

- Walk through customer or admin flow

- Assert end state in DB and UI

GitHub Action:

- .github/workflows/e2e.yml runs Playwright on every PR

- Tests against ephemeral DB

- Required to pass before merge

Test stability:

- No flaky tests. If a test is flaky, fix or remove.

- Each test independent (no shared state).

- Reasonable timeouts (no infinite waits).

Do NOT:

- Mock the DB (real Postgres, mocked AI only)

- Hardcode dates that will break next week

- Add tests for features not in V0

```

### Acceptance criteria

- [ ] 15 E2E tests pass against staging

- [ ] CI runs E2E on every PR

- [ ] All happy paths pass

- [ ] All edge cases assert correct behavior

-----

# Day 6 — Pre-first-booking gate (Marcus + ops)

Day 6 is mostly NOT code. It’s the gate review + ops artifacts. Code-side, just one Codex prompt for the security audit.

-----

## X02 — Security audit pass

**Agent:** Codex Cloud

### Prompt

```

Run a security audit on the Neskala repo before the pre-first-booking gate.

Check:

1. No secrets committed: grep for known key patterns (sk-, ANTHROPIC_API_KEY=, hardcoded passwords)

2. .env files in .gitignore

3. All API routes that mutate state require admin auth (where appropriate)

4. /api/intake doesn't leak the safety_audit_log content to client

5. /api/match doesn't return raw_intake_text to provider-facing surfaces (it shouldn't, but verify)

6. SQL injection: confirm Drizzle parametrization on all queries (no string concat)

7. CORS configured (Next.js default is fine for V0)

8. Rate limiting on /api/admin/auth (5 per 15 min per IP)

9. Sentry doesn't capture customer raw_intake_text (privacy)

10. Audit log truly insert-only at DB layer

For each: report PASS/FAIL with file/line if FAIL.

Output: tests/security-audit-baseline.md committed to repo, signed by Marcus before gate sign-off.

Do NOT:

- Fix issues automatically — report them, Marcus assigns the fix

```

### Acceptance criteria

- [ ] Security audit baseline committed

- [ ] All FAILs assigned and resolved before gate sign-off

-----

## Gate review (Marcus, manual)

Not a code prompt — but listing here so it’s not skipped.

Marcus walks through `SAFETY_AND_TRUST.md § Pre-first-booking safety gate`:

- [ ] Provider agreement signed (Yuni’s records)

- [ ] Customer ToS displayed and acknowledged before intake

- [ ] No-sexual-services policy visible

- [ ] Cancellation/refund policy visible

- [ ] Classifier eval passing (CI green)

- [ ] Pregnancy/injury route to human review verified (smoke test)

- [ ] Provider has ID + reference verified

- [ ] Provider tier assigned (Tier 1 only for V0)

- [ ] Customer sees provider-safe summary

- [ ] Yuni has incident response script saved

- [ ] Provider WhatsApp check-in/check-out tested with one provider

- [ ] Customer behavior policy in ToS

- [ ] Audit log writes confirmed

- [ ] End-to-end dry run completed

- [ ] Booking state machine tested (happy path + 2 cancellations)

Marcus signs off in `PRE_FIRST_BOOKING_GATE.md` (created Day 6) with date, initials, and any caveats.

-----

# Day 7 — Dry run + mobile QA

Day 7 is verification. Marcus + Yuni as fake customer + fake provider. Mobile QA on real devices.

-----

## P11 — Customer feedback flow

**Agent:** Replit Agent

### Prompt

```

Build the customer feedback page at src/app/(customer)/feedback/[booking_id]/page.tsx.

Read MVP_SPEC.md § Customer feedback for the question list.

7 questions (per spec):

1. Did the match feel right for your state? (1-5 stars or scale)

2. Did the match explanation increase your trust? (yes/somewhat/no)

3. Would you have booked without the explanation? (yes/no/unsure)

4. Did the provider feel matched to your state? (yes/somewhat/no)

5. Would you have preferred browsing a list? (yes/no/unsure)

6. Open: "In one sentence, how did this match feel?" (textarea, optional)

7. Rebook intent (yes/maybe/no)

Submit:

- POST to /api/feedback with booking_id + answers

- Inserts customer_feedback row

- Updates booking_requests.feedback_submitted = true

- Redirects to /feedback/thank-you

Trigger:

- Yuni manually triggers feedback link send from admin (admin button "Send feedback link")

- Generates a unique URL: /feedback/[booking_id]?token=[short_token]

- Yuni copies WhatsApp template with the link

- For V0, no email/SMS — Yuni sends via WhatsApp manually

- Token validates the booking_id, no auth needed

Do NOT:

- Build email sending

- Build push notifications

- Build automatic feedback timing (V0.1 will)

```

### Acceptance criteria

- [ ] Feedback form renders

- [ ] All 7 questions submit

- [ ] customer_feedback row created

- [ ] Yuni admin can trigger send link

-----

## P12 — Audit log browser + provider feedback intake

**Agent:** Replit Agent

### Prompt

```

Two small admin pages.

1. /admin/audit:

- Read-only table view of safety_audit_log

- Filter: intake_id, booking_id, call_type, kill_switch_fired, date range

- Click row → expanded view with full input_summary, output_summary, classifier_flags

- No edit, no delete (DB enforces, UI also doesn't expose)

- Shows daily cost rollup: today's $, this week's $, vs $100 cap

2. /admin/feedback:

- Tabs: Customer feedback / Provider feedback

- List view sortable by date, rating

- Customer quotes pulled out as a side panel: "Latest customer quotes for marketing capture"

- Provider feedback shows match_accurate, energy_right, pressure_right per provider, aggregated

3. Post-session provider feedback intake:

- Yuni manually enters provider feedback in admin (no provider-facing form in V0)

- Form on /admin/bookings/[id] with provider feedback fields

- Submit creates provider_feedback row

Do NOT:

- Build provider-facing feedback portal (V0.1)

- Build aggregated analytics dashboard (V0.1)

```

### Acceptance criteria

- [ ] Audit log viewable, filterable

- [ ] Cost rollup shown

- [ ] Customer quotes panel visible

- [ ] Provider feedback intake works from admin

-----

## P13 — Mobile QA fixes

**Agent:** Replit Agent

### Prompt

```

Mobile QA pass before pre-first-booking gate.

Test on:

- iPhone Safari (real device or BrowserStack iPhone 14)

- Android Chrome (real device or BrowserStack Pixel 7)

Run through TEST_PLAN.md § Mobile QA checklist (16 items).

Fix any failures. Common likely fixes:

- Form validation errors hidden by keyboard → add scrollIntoView

- Microphone button touch target too small on small phones → enlarge to 56pt

- Whisper recording on iPhone Safari requires user gesture chain → ensure tap-to-record sequence is clean

- Tailwind viewport classes not respected on some Androids → use explicit max-w-md

- WhatsApp link not opening native app → use whatsapp://send?phone=X format

After fixes, re-run the full checklist. Document any items that can't be fixed in V0 in NOTES section of PR.

Do NOT:

- Add a separate mobile-only codepath

- Add browser-specific hacks unless documented

```

### Acceptance criteria

- [ ] All 16 mobile QA checklist items pass on iPhone Safari + Android Chrome

- [ ] Or: any failure documented and assigned to V0.1

-----

## P14 — ToS + privacy pages + intake gating

**Agent:** Replit Agent

### Context paste

```

Read SAFETY_AND_TRUST.md fully — the ToS draws from this.

```

### Prompt

```

Build /tos and /privacy pages with content per SAFETY_AND_TRUST.md.

ToS content (Marcus reviews before merge):

- Top section: No sexual services, ever. Boundary violations = permanent ban.

- Service description: matching, not medical advice

- Data collection: what we collect, why, how long

- Cancellation: 4+ hours = free, under 4 hours = transport fee at provider discretion

- Refund: Neskala doesn't process refunds; credits toward future bookings

- Customer behavior policy

- Provider safety: customer agrees to these terms

- Liability disclaimer

- Indonesian law applies

Privacy:

- What data we collect (raw intake, follow-ups, contact)

- 30-day raw intake retention, then summarize-or-delete

- Audio never stored (just transcribed)

- Right to delete: email Yuni, honored within 7 days

- No selling, no sharing outside matching

- UU PDP disclosure (placeholder until V1 legal review)

Intake gating:

- ToS checkbox on /intake page (already exists from P02)

- Verify it actually blocks submit if unchecked

- Customer cannot proceed without acknowledging

Verify intake also displays the "no sexual services" line prominently, not buried in ToS.

Do NOT:

- Use legal language for its own sake — keep human

- Make ToS so long no one reads it

- Promise things we can't deliver

```

### Acceptance criteria

- [ ] /tos and /privacy pages render with the content

- [ ] ToS checkbox blocks submit on /intake

- [ ] Marcus reviews and approves content before merge

-----

## P15 — Empty states, error states, polish

**Agent:** Replit Agent

### Prompt

```

Empty/error state polish across the app.

Customer-facing:

- /match/:intake_id: 0 matches → "We didn't find a perfect fit. Yuni will recommend over WhatsApp." with manual review CTA

- /booking/:id/pending: booking not found → "Hmm, we can't find this booking. Message Yuni on WhatsApp."

- Network error during intake → "We're taking longer than usual. Try again." with retry button

- Whisper failure → already handled in P08, verify it's working

Admin-facing:

- /admin/bookings: empty state → "No bookings yet. They'll appear here as customers request them."

- /admin/providers: empty state → "Add your first provider to start matching." with CTA

- /admin/audit: empty state → "No audit events yet."

- /admin/feedback: empty state → "No feedback yet."

General:

- 404 page that's calm and useful

- 500 page that says "something broke, message Yuni" with WhatsApp link

- Loading skeletons on dashboard tables (not spinners — skeletons feel faster)

Do NOT:

- Add lottie animations (overkill)

- Add sound effects

- Add toast spam — restrain notifications to actually-meaningful events

```

### Acceptance criteria

- [ ] Every page has a defined empty state

- [ ] Network errors show helpful retry

- [ ] 404 and 500 pages exist

- [ ] No spinner-only loading states (use skeletons)

-----

## End-of-Day-7 dry run

Marcus + Yuni walk through:

1. Marcus as customer: scans QR, completes intake (text), sees matches, requests booking

1. Yuni as Yuni: receives booking, copies provider WhatsApp template

1. Yuni as provider: confirms via WhatsApp

1. Yuni as Yuni: confirms with customer (Marcus)

1. Marcus as customer: receives confirmation

1. Simulated session, Yuni triggers feedback link

1. Marcus as customer: submits feedback

1. Yuni reconciles in admin: marks complete, logs ops minutes, settles commission

Then voice path:

9. Marcus as customer: scans, uses voice intake

10. Repeat steps 2-8

Then kill-switch path:

11. Marcus as customer: types pregnancy intake

12. Routes to human review

13. Yuni receives notification, responds via WhatsApp

Then cancellation path:

14. Marcus as customer: requests booking

15. Yuni transitions to canceled_by_customer with reason

If all 15 work without manual DB fixes, Day 7 is done. Marcus signs the gate.

If anything broken: fix in same session, retry.

-----

# Post-Day-7

The build sprint is done. The 30-day validation sprint begins.

Don’t add features during validation. Observe, capture, learn. Patch only safety/critical bugs. Everything else goes in `POST_MVP_ROADMAP.md` for V0.1.

-----

## Notes for next iteration

When you split this into individual files at desktop later (per Marcus’s preference):

```

prompt-pack/

README.md            # this overview

day-1/

C01-scaffold.md

C02-schema.md

day-2/

P01-landing.md

...

day-3/

C03-classifier.md

C04-eval-matcher-summarizer.md

...

```

A simple Claude Code prompt: “Split PROMPTS.md into individual numbered files in prompt-pack/, organized by day. Preserve all content.”

-----

*Prompt Pack v0.1 · Companion to spec pack · Sequential execution required*
