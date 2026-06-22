---
title: "# Kairos — V1 Bootstrap Build Directive"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Kairos app /Core app stuff /# Kairos — V1 Bootstrap Build Directive.docx"
status: active
privacy: working
tags:
  - product
---

# # Kairos — V1 Bootstrap Build Directive

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# Kairos — V1 Bootstrap Build Directive

```

Surfaces:          Next.js scaffold, .symposium/AUTONOMY_LAYER (already present),

ICS ingest pipeline, events.enriched.json, Explore mode,

shortlist, schedule generation, single + bulk ICS export,

Marcus public route, text + voice intake, two-pass relevance scoring

Production impact: API change (new) + UI change (new) + prompt change (new)

Council of Models: no (V1; no safety-relevant content yet)

Auto-merge:        no (V1 bootstrap; Marcus reviews before merge)

Credentials:       gh, ANTHROPIC_API_KEY, OPENAI_API_KEY, BLOB_READ_WRITE_TOKEN

Agent:             split (see Parallel-Agent Split below)

```

## Role

You are building Kairos V1, an intelligence layer on top of the Carly NYC Tech Week 2026 ICS feed. The product converts ~1,035 noisy events into a personalized, decision-ready schedule for any attendee. It ships before Tech Week (week of June 1, 2026). It is a Symposium Studios proof artifact. The full product specification lives at `docs/kairos-spec-v1.1.md`. Read it before starting.

## Protocol

Apply `.symposium/AUTONOMY_LAYER.md` before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see `.symposium/AUTONOMY_LAYER.md` section 0.1 (filled in below for Kairos).

### Stack (fill-in for `.symposium/AUTONOMY_LAYER.md` section 0.1)

```

Frontend:   Next.js 15 (App Router) + TypeScript strict + Tailwind + shadcn/ui + Framer Motion

Backend:    Next.js Route Handlers (Node runtime for AI; Edge for static reads)

Database:   None in V1. events.enriched.json in Vercel Blob. Profile, shortlist, relevance cache in browser localStorage.

Auth:       None in V1 (anonymous sessions via localStorage)

AI:         Anthropic SDK (Claude Sonnet 4 for runtime; Claude Haiku 4.5 for batch enrichment) + OpenAI SDK (Whisper)

Email:      None in V1

Monorepo:   Single repo, pnpm

CI/CD:      Vercel auto-deploys main. Vercel Cron at /api/cron/ingest every 6h pre-Tech-Week, hourly during.

```

Apply this to `.symposium/AUTONOMY_LAYER.md` section 0.1 as part of Phase A pre-flight.

## Deployment Posture

- PR-only stop for V1. Auto-merge is no. Marcus reviews and merges.

- Vercel auto-deploys main on merge.

- Vercel Blob requires `BLOB_READ_WRITE_TOKEN` set in Vercel project env. State exact command in PR body for Marcus to run.

- All other env vars (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `ADMIN_TOKEN`, `SENTRY_DSN`) similarly Marcus-only to apply.

## Design Data

The full design data lives in `docs/kairos-spec-v1.1.md`. Treat that spec as the authoritative source. Highlights below for orientation.

### File structure (new files)

```

src/app/

layout.tsx

page.tsx                       redirect or landing for /tech-week

tech-week/

page.tsx                     Explore mode

shortlist/page.tsx           Shortlist view

schedule/page.tsx            Schedule generation view

marcus/page.tsx              Marcus public route

api/

intake/parse/route.ts

intake/voice/route.ts

search/parse/route.ts

relevance/route.ts

schedule/generate/route.ts

events/route.ts

events/[uid]/ics/route.ts

shortlist/ics/route.ts

cron/ingest/route.ts

admin/ingest/route.ts

admin/ops/route.ts

src/lib/

ics/parse.ts                   node-ical wrapper

ics/export.ts                  ics npm wrapper

enrichment/batch.ts            Haiku enrichment per 20 events

enrichment/types.ts            EventEnrichment + EnrichedEvent types

relevance/pass1.ts             client-side coarse scoring

relevance/pass2.ts             server route helper for Pass 2 batch

storage/blob.ts                Vercel Blob read/write helpers

storage/local.ts               localStorage hooks (typed)

src/components/

EventCard.tsx

FilterPanel.tsx

IntakeForm.tsx

ShortlistView.tsx

ScheduleView.tsx

MarcusRoute.tsx

data/

marcus-route.json              checked-in

docs/

kairos-spec-v1.1.md            paste in from existing spec

run-notes/                     created per-session

```

### Schemas / types

Per spec v1.1 sections 5.2, 5.3, 5.7, 5.8, 8. Reproduce verbatim into `src/lib/enrichment/types.ts` and related.

### AI prompt fragments

Spec verbatim in directive (see spec sections 5.2 and 10.2). The agent does NOT invent prompt text. If a prompt is referenced by the spec but not specified verbatim, halt and add to `BLOCKERS_FOR_MARCUS.md`.

### Default values

- Profile defaults: empty arrays, “no-preference” for alcohol, available_days defaults to all Tech Week days.

- Relevance Pass 1 weights: domain overlap 0.6, vibe match 0.2, alcohol penalty -0.3 when applicable, agentic signal bonus +0.1 per point above 1.

### Marcus’s public route content

Spec’d as a checked-in `data/marcus-route.json`. Marcus will populate after Phase I. For Phase I scaffolding, write a placeholder JSON with empty arrays so the page renders an “intro coming soon” state.

## Working Files Protocol

Per `.symposium/AUTONOMY_LAYER.md` section 0.4:

- `docs/run-notes/session-2026-05-16-kairos-bootstrap-plan.md`

- `AUTONOMOUS_RUN_LOG.md` at repo root

- `BLOCKERS_FOR_MARCUS.md` at repo root

- `docs/deferred-issues.md`

## Parallel-Agent Split (V1)

This directive supports a split if Marcus runs two concurrent agents. Otherwise execute sequentially.

### Track 1 (CC Cloud, code-only, no credentials)

- Phase A: Project bootstrap (Next.js scaffold, Tailwind, shadcn, project structure)

- Phase C: Explore mode UI (FilterPanel, EventCard, listing page) with mocked data

- Phase G: Shortlist UI + schedule view UI with mocked data

- Phase I: Marcus route page rendering from placeholder JSON

### Track 2 (CC Local, credentialed)

- Phase B: ICS ingest pipeline (parse + dedup + normalize + enrichment via Haiku, write to Vercel Blob)

- Phase D: Voice intake (Whisper API integration)

- Phase E: Two-pass relevance scoring (Pass 2 server route + caching)

- Phase F: NL search route (Claude query parsing)

- Phase H: ICS export (single + bulk)

- Phase J: Deployment, smoke tests, Sentry wiring

Coordination: shared `AUTONOMOUS_RUN_LOG.md` at repo root. Track 2 depends on Phase A complete and Phase B’s `events.enriched.json` shape stable before Phase E.

For single-agent execution, run sequentially A → B → C → D → E → F → G → H → I → J.

## Phase Plan

### Phase A: Project Bootstrap

- **Pre-flight**: `git status` clean, `node --version` ≥ 20, fresh Next.js scaffold ready to init.

- **Smoke assertions (write first)**:

- `pnpm build` succeeds on empty scaffold.

- `/` route returns 200.

- **Implementation**:

- `pnpm create next-app@latest` with TypeScript, Tailwind, App Router, ESLint.

- Add shadcn/ui per its installer.

- Add Framer Motion, React Hook Form, Zod, node-ical, ics, @vercel/blob, @anthropic-ai/sdk, openai.

- Configure tsconfig strict.

- Add Sentry SDK (Next.js integration, error monitoring only for now).

- Create the file structure scaffolded above with placeholder content.

- Apply Stack to `.symposium/AUTONOMY_LAYER.md` section 0.1 (currently filled in this directive; copy into the layer file).

- **AUTOMATED criteria**: build passes, both smoke assertions pass.

- **HUMAN_REVIEW**: none.

- **Commit**: `chore(bootstrap): Next.js scaffold + Symposium stack applied`

### Phase B: ICS Ingest Pipeline

- **Pre-flight**: spec-reality reconciliation per `.symposium/AUTONOMY_LAYER.md` section 1.13. Read `docs/kairos-spec-v1.1.md` sections 3, 5.1, 5.2. Invoke skill `.symposium/skills/diagnostics/ics-feed-diagnostic/SKILL.md` to validate the live Carly feed shape against expectations.

- **Smoke assertions (write first)**:

- Vitest: parse a fixture ICS sample → returns array of EnrichedEvent shape (pre-enrichment).

- Vitest: dedup logic removes known duplicate UIDs.

- Vitest: neighborhood extraction handles “Brooklyn, New York, NY” and “Virtual (NYC), New York, NY”.

- Integration: full pipeline against live Carly feed produces non-empty events.enriched.json in test environment.

- **Implementation**:

- `src/lib/ics/parse.ts`: fetch + parse + dedup + normalize.

- `src/lib/enrichment/batch.ts`: Haiku batch enrichment, 20 events per call, with retry and validation against EventEnrichment schema.

- `src/lib/enrichment/types.ts`: full type definitions per spec.

- `src/lib/storage/blob.ts`: Vercel Blob read/write.

- `src/app/api/cron/ingest/route.ts`: cron endpoint that runs the pipeline and writes to Blob.

- `src/app/api/admin/ingest/route.ts`: manual trigger (token-gated via `ADMIN_TOKEN`).

- **AUTOMATED criteria**: all smoke assertions pass. Pipeline completes for full Carly feed in under 5 minutes locally.

- **HUMAN_REVIEW**: Marcus reviews a sample of enrichment outputs (10 events) for tag and vibe quality. Logged as MANUAL_PLAYTEST_REQUIRED.

- **Commit**: `feat(ingest): Carly ICS pipeline with Haiku enrichment`

### Phase C: Explore Mode UI

- **Pre-flight**: events.enriched.json shape stable from Phase B. If running parallel, mock the shape per the spec.

- **Smoke assertions (write first)**:

- Playwright: /tech-week loads, shows event cards.

- Playwright: filter by neighborhood updates the list.

- Playwright: alcohol-forward exclude toggle hides flagged events.

- **Implementation**:

- `src/app/tech-week/page.tsx`: Explore mode with FilterPanel + event grid.

- `src/components/FilterPanel.tsx`: structured filters per spec section 5.4.

- `src/components/EventCard.tsx`: card per spec section 5.5.

- Client-side filter state in URL params via Next.js searchParams.

- **AUTOMATED criteria**: all smoke assertions pass. Build passes.

- **HUMAN_REVIEW**: visual review of EventCard, mobile readability. MANUAL_PLAYTEST_REQUIRED.

- **Commit**: `feat(explore): filterable event grid`

### Phase D: Text + Voice Intake

- **Pre-flight**: Phase A complete.

- **Smoke assertions (write first)**:

- Vitest: intake parser returns structured Profile from a known-good raw text.

- Playwright: text intake form submits, parsed profile persists in localStorage.

- Vitest: voice route accepts multipart audio, returns transcription string.

- **Implementation**:

- `src/components/IntakeForm.tsx`: textarea + structured toggles + mic button.

- `src/app/api/intake/parse/route.ts`: Claude Sonnet 4 call returning Profile.

- `src/app/api/intake/voice/route.ts`: Whisper transcription.

- `src/lib/storage/local.ts`: typed localStorage hooks for Profile.

- **AUTOMATED criteria**: smoke assertions pass.

- **HUMAN_REVIEW**: voice intake works on iOS Safari, Chrome desktop, Chrome Android. MANUAL_PLAYTEST_REQUIRED.

- **Commit**: `feat(intake): text and voice intake with Claude parsing`

### Phase E: Two-Pass Relevance Scoring

- **Pre-flight**: Phases B and D complete.

- **Smoke assertions (write first)**:

- Vitest: Pass 1 returns score and rank for a profile + event pair.

- Vitest: Pass 2 route returns score + blurb for batched event UIDs.

- Vitest: cache key includes profile hash; profile change invalidates cache.

- **Implementation**:

- `src/lib/relevance/pass1.ts`: client-side coarse scoring per ADR 0004.

- `src/lib/relevance/pass2.ts`: server helper for batch Claude calls.

- `src/app/api/relevance/route.ts`: POST endpoint.

- localStorage caching of Pass 2 results keyed by event UID + profile hash.

- Wire Pass 1 into EventCard rendering. Pass 2 hydrates progressively on viewport entry.

- **AUTOMATED criteria**: smoke assertions pass. Time-to-first-render under 1 second on a 100-event list.

- **HUMAN_REVIEW**: blurb quality on 10 sample (profile, event) pairs. MANUAL_PLAYTEST_REQUIRED.

- **Commit**: `feat(relevance): two-pass scoring with lazy AI hydration`

### Phase F: Natural-Language Search

- **Pre-flight**: Phase C complete.

- **Smoke assertions (write first)**:

- Vitest: NL parser returns a structured filter object for “Tuesday afternoon agentic events no alcohol”.

- Playwright: NL search bar parses query and applies filters.

- **Implementation**:

- `src/app/api/search/parse/route.ts`: Claude query → filter object.

- Wire NL search bar into the FilterPanel.

- **AUTOMATED criteria**: smoke passes on 8 of 10 representative queries.

- **HUMAN_REVIEW**: none.

- **Commit**: `feat(search): natural-language filter parsing`

### Phase G: Shortlist + Schedule Generation

- **Pre-flight**: Phases C and E complete.

- **Smoke assertions (write first)**:

- Vitest: shortlist add/remove persists across page reloads.

- Vitest: schedule generator resolves time conflicts with no overlapping attend decisions.

- Playwright: shortlist view shows conflict flags; schedule generation completes and renders timeline.

- **Implementation**:

- `src/components/ShortlistView.tsx`: per spec section 5.6.

- `src/components/ScheduleView.tsx`: per spec section 5.7.

- `src/app/api/schedule/generate/route.ts`: Claude call producing ProposedSchedule.

- localStorage shortlist hooks.

- **AUTOMATED criteria**: smoke passes. Schedule generation completes in under 8 seconds for a 20-event shortlist.

- **HUMAN_REVIEW**: rationale quality on 5 sample schedules. MANUAL_PLAYTEST_REQUIRED.

- **Commit**: `feat(schedule): shortlist + time-conflict-aware generator`

### Phase H: ICS Export

- **Pre-flight**: Phase G complete.

- **Smoke assertions (write first)**:

- Vitest: single-event ICS export round-trips through node-ical with identical TZID and DTSTART/DTEND.

- Vitest: bulk ICS export contains all shortlisted events.

- Manual import into Apple Calendar, Google Calendar, Outlook works (logged as HUMAN_REVIEW).

- **Implementation**:

- `src/app/api/events/[uid]/ics/route.ts`: single-event ICS.

- `src/app/api/shortlist/ics/route.ts`: bulk ICS.

- Buttons wired into EventCard and ShortlistView.

- **AUTOMATED criteria**: round-trip smokes pass.

- **HUMAN_REVIEW**: cross-platform calendar import. MANUAL_PLAYTEST_REQUIRED.

- **Commit**: `feat(export): single and bulk ICS export`

### Phase I: Marcus Public Route

- **Pre-flight**: Phase C complete (EventCard reusable). Marcus has populated `data/marcus-route.json` or accepts a placeholder.

- **Smoke assertions (write first)**:

- Playwright: /tech-week/marcus renders day themes and statuses.

- Vitest: no real-time location data is exposed (no `going` status visible publicly).

- **Implementation**:

- `src/components/MarcusRoute.tsx`: per spec section 5.8.

- `src/app/tech-week/marcus/page.tsx`: SSR or static render from data/marcus-route.json.

- **AUTOMATED criteria**: smoke passes. Privacy assertion passes.

- **HUMAN_REVIEW**: Marcus reviews the rendered page on mobile + desktop. MANUAL_PLAYTEST_REQUIRED.

- **Commit**: `feat(marcus-route): public Tech Week route from static JSON`

### Phase J: Deployment, Smoke, Sentry

- **Pre-flight**: all prior phases complete. Invoke skill `.symposium/skills/execution/deployment-preflight/SKILL.md`.

- **Smoke assertions (write first)**:

- Playwright against Vercel preview deployment: home page, /tech-week, intake flow, shortlist, schedule.

- Sentry receives a deliberate test error and is visible in the Sentry dashboard.

- **Implementation**:

- Configure Vercel project (Marcus-only step; state exact env var settings in PR body).

- Configure Vercel Cron for `/api/cron/ingest`.

- Configure Sentry DSN.

- Run preflight checklist.

- Open PR. Stop. Marcus reviews and merges.

- **AUTOMATED criteria**: preview smoke passes.

- **HUMAN_REVIEW**: Marcus runs `.symposium/skills/review/public-surface-qa/SKILL.md` against the preview URL. MANUAL_PLAYTEST_REQUIRED.

- **Commit**: `chore(deploy): preview deployment + Sentry wiring; ready for production merge`

## Directive-Specific Repair Entries

- **KAIROS-1 — Carly feed parse fails or returns under 500 events**

- A1: Retry with backoff (3 attempts).

- A2: Use last known-good `events.enriched.json` from Blob.

- DEFER: Log to `BLOCKERS_FOR_MARCUS.md`. Continue with stale data.

- **KAIROS-2 — Haiku enrichment returns malformed JSON for some events**

- A1: Retry the batch once with same payload.

- A2: Split the batch in half and retry each half.

- DEFER: For unrecoverable events, mark with `enrichment: { topic_tags: [], vibe: "other", agentic_signal: 0, ...defaults }`. Log count.

- **KAIROS-3 — Whisper transcription returns empty or wrong-language text**

- A1: Surface empty transcription in UI; user edits the textarea directly.

- A2: No silent retry. User can re-record.

- DEFER: N/A; text fallback always works.

## Deferred-Issues Format

See `.symposium/AUTONOMY_LAYER.md` section 4.

## BUILD_REPORT Format

See `.symposium/AUTONOMY_LAYER.md` section 5. At end of directive, invoke skill `.symposium/skills/review/build-report-ledger/SKILL.md`.

## Hard Stops

See `.symposium/AUTONOMY_LAYER.md` section 6.

## GO

Begin Phase A pre-flight per `.symposium/AUTONOMY_LAYER.md` section 3. Credentials preflight scope: `gh auth status`. Cut branch from main: `feat/kairos-v1-bootstrap`. Create `docs/run-notes/session-2026-05-16-kairos-bootstrap-plan.md` and `AUTONOMOUS_RUN_LOG.md` at repo root. Apply the Stack block from this directive to `.symposium/AUTONOMY_LAYER.md` section 0.1 as the first commit of Phase A.
