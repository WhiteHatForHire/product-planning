# Tech Week Signal Map

## Product Specification, v1.1 (Carly-aware)

**Project codename:** Signal Map
**Owner:** Marcus Vale / Symposium Studios (Bisel Legacy Global LLC)
**Source feed:** [Carly NYC Tech Week 2026 ICS](https://www.usecarly.com/calendars/nyc-tech-week-2026.ics) (1,035+ events)
**Target launch window:** Pre NYC Tech Week 2026 (week of June 1, 2026)
**Status:** Spec v1.1, pre-directive. Supersedes v1.0.
**Last updated:** 2026-05-16

---

## 0. Telos and positioning

**Telos.** Sit on top of the Carly feed as a personalized intelligence layer. Convert 1,000+ events into a decision-ready, ranked, personalized schedule for any visitor who tells it who they are.

**Positioning line.** "A personalized signal map for NYC Tech Week. Tell it who you are, it tells you which events matter for you. Built by Symposium Studios as a live prototype of agentic event intelligence."

**Architectural posture.** This product is not an event database. It is an enrichment, scoring, and curation layer on top of someone else's database. The Carly team did the ingestion work. Signal Map does the intelligence work.

**Strategic intent.**

1. Open conversations at Tech Week.
2. Demonstrate the Symposium pattern (messy public input → AI enrichment → decision-ready output) in public.
3. Provide a working live demo Marcus can reference in fCTO conversations and partnership pitches.

**What this is not.**

- Not an event aggregator (Carly already is).
- Not a ticketing system.
- Not a social network.
- Not a real-time location tracker.
- Not a year-round events platform.

---

## 1. Target users

**Primary persona: the signal-seeking attendee.**

A founder, operator, investor, or builder coming to Tech Week with a goal. Examples: technical founder building agentic infra, investor scanning agentic commerce, operator hunting fractional CTO signal, sober attendee filtering out alcohol-forward events, time-constrained attendee with one afternoon free.

**Secondary persona: the curious browser.** No deep goal yet, exploring.

**Anti-persona.** Casual partygoers who want pure social. Not for them.

---

## 2. Phasing overview

| Phase | Scope | Target |
|---|---|---|
| V1 | Carly ICS ingest + enrichment pipeline, Explore mode with filters and natural-language search, text + voice intake, two-pass relevance scoring with personalized blurbs, shortlist, time-conflict-aware schedule generator, single and bulk ICS export, Marcus's public route | Pre-launch (T-10 days minimum) |
| V2 | Maps Directions integration, transit preferences, per-leg commute time, tight-connection warnings, route reordering | Mid-week iteration if traction warrants |
| V3 | Shareable public schedules, post-event reflections, year-round event database evaluation, social signals | Post-Tech-Week, signal-gated |

---

## 3. Source feed analysis (Carly ICS)

### 3.1 Feed metadata

- **URL:** `https://www.usecarly.com/calendars/nyc-tech-week-2026.ics`
- **Format:** Standard iCalendar (VCALENDAR, VEVENT).
- **Volume:** 1,035+ events.
- **Timezone:** `America/New_York` (TZID set correctly on all events).
- **Window:** Begins 2026-06-01.

### 3.2 Per-event field set (confirmed)

Each VEVENT contains:

- `UID` (unique, format `nyctw-2026-MM-DD-NNN-slug@usecarly.com`)
- `DTSTART` with TZID
- `DTEND` with TZID
- `SUMMARY` (event title)
- `DESCRIPTION` (multiline: "Hosted by {host}\\nLocation: {neighborhood}\\nRSVP: {url}\\n\\nBrought to you by Carly\\nhttps://www.usecarly.com")
- `LOCATION` (format: "{neighborhood}, New York, NY" or "Virtual (NYC), New York, NY")
- `URL` (RSVP link, typically Partiful)

### 3.3 What the feed does NOT contain

- No category or topic tags.
- No alcohol or sober flags.
- No vibe classification (panel vs mixer vs workshop vs party).
- No real event description (just metadata).
- No host bio or social URL.
- No expected attendance signal.

### 3.4 Data quality observations

- Duplicate UIDs exist in the wild (caught one example: UATech Venture Night appears twice). Dedup required at ingest.
- Title encoding uses smart quotes (U+2019, U+2018), em-dashes (U+2014). Normalize at ingest.
- "Virtual" events have LOCATION "Virtual (NYC), New York, NY". Flag separately.
- A handful of titles are truncated in the SUMMARY. Accept and don't reconstruct.

### 3.5 Implication for AI strategy

Because the feed has no descriptions, AI scoring runs on title + host + neighborhood + time only. This is enough for decent relevance, but it means:

- AI prompts must emphasize signal extraction from titles ("Agents in Production: The Memory Problem" → tag agentic, devtools, infra; vibe panel/talk; not alcohol-forward).
- Host org names carry weight (a16z, McKinsey, Stripe, SAP, Insight Partners, Bessemer, etc.) and the enrichment prompt should leverage them.
- No fallback to "read the event description" exists. The system relies on AI inference, not source semantics.

---

## 4. V1 architecture overview

**File-first, no database in V1.**

```
                 ┌──────────────────────────────┐
                 │  Carly ICS feed (live URL)   │
                 └──────────────┬───────────────┘
                                │
                                ▼ (build-time + cron, every 6h)
                 ┌──────────────────────────────┐
                 │  Ingest + enrichment pipeline │
                 │  - parse ICS                 │
                 │  - dedup, normalize          │
                 │  - extract neighborhood, host│
                 │  - batch Claude enrichment   │
                 │    (tags, vibe, flags)       │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │  events.enriched.json        │
                 │  (checked into repo or Blob) │
                 └──────────────┬───────────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │  Next.js static + SSR pages  │
                 │  Vercel deployment           │
                 └──────────────┬───────────────┘
                                │
       ┌────────────────────────┼────────────────────────┐
       ▼                        ▼                        ▼
  Profile             Personalized blurb           Marcus route
  (localStorage)      (Claude API route)           (static JSON)
  Shortlist           NL filter parsing
  (localStorage)      Schedule generation
                      Whisper transcription
```

**Why no DB in V1.**

- Events are read-only and rebuildable from the source feed. JSON file suffices.
- Profile, shortlist, and personal cache live in localStorage. No cross-device sync required for V1.
- Marcus's route is rarely edited and lives in a checked-in file.
- Eliminates Drizzle, migrations, Neon, and the entire data layer for V1. Materially faster to ship.

**When a DB enters.** V2 or V3 if shareable schedules, cross-device sync, or analytics-at-scale become priorities. Adding Postgres later is straightforward.

---

## 5. V1 feature specification

### 5.1 Ingest and enrichment pipeline

**Trigger.** Vercel cron every 6 hours plus manual trigger. On Tech Week days, cron tightens to every hour.

**Steps.**

1. Fetch the Carly ICS over HTTPS.
2. Parse with `node-ical` or equivalent.
3. Dedup by UID. Where UIDs collide, keep the most recently parsed.
4. Normalize titles (Unicode normalization, strip extra whitespace).
5. Extract `neighborhood` from LOCATION (split on first comma).
6. Extract `host_org` from DESCRIPTION (regex on "Hosted by ").
7. Detect virtual events (LOCATION starts with "Virtual").
8. Hash the normalized event content. Compare against the previous run's hash to determine which events are new or changed.
9. For new or changed events only, batch-call Claude for enrichment (see 5.2).
10. Merge enrichment into the event record.
11. Write `events.enriched.json` to a Vercel Blob URL or checked-in artifact.

**Acceptance.**

- Full pipeline runs in under 5 minutes for the 1,035-event feed on a cold start.
- Incremental runs (after first full enrichment) hit Claude for under 5% of events.
- Pipeline is idempotent: rerunning with no source changes produces no Claude calls.

### 5.2 Enrichment per event (Claude batch)

For each event the AI infers and adds:

```typescript
type EventEnrichment = {
  topic_tags: string[];          // ["agentic", "devtools", "founder", "investor", "infra", "healthcare", "fintech", "crypto", "creator-economy", "robotics", "design", ...]
  vibe: "panel" | "talk" | "workshop" | "hackathon" | "mixer" | "happy-hour" | "dinner" | "breakfast" | "office-hours" | "demo" | "pitch" | "social" | "other";
  alcohol_forward: boolean;       // inferred from title (Happy Hour, Mixer, Drinks, etc.)
  sober_friendly: boolean;        // inferred (run, breakfast, coffee, workshop, hackathon)
  founder_density: "high" | "medium" | "low" | "unknown";
  investor_density: "high" | "medium" | "low" | "unknown";
  agentic_signal: 0 | 1 | 2 | 3;  // 0 = unrelated, 3 = explicitly agentic
  one_line_synopsis: string;       // ~12-word inferred description for cards
};
```

Batched at 20 events per Claude call. Stored alongside the event in `events.enriched.json`.

### 5.3 Intake

**Text intake.** Single textarea labeled "Tell me about yourself: who you are, what you're building, and what you're looking for at Tech Week." Plus structured toggles below (sober-friendly, transit preference defaults, available days).

**Voice intake.** Mic button. User taps, speaks (up to 90 seconds), upload to `/api/intake/voice`. Server pipes audio to OpenAI Whisper API. Transcription returns to the client, populates the textarea, user can edit before submit.

**Parsing.** On submit, a Claude API call takes the raw text and returns a structured Profile:

```typescript
type Profile = {
  raw_text: string;
  audio_url?: string;          // if voice
  name?: string;
  role: string;
  company?: string;
  stage?: "exploring" | "pre-seed" | "seed" | "series-a-plus" | "exited" | "operator";
  what_building?: string;
  looking_for: Array<"capital" | "partners" | "hires" | "customers" | "learning" | "deal-flow" | "community" | "other">;
  domains_of_interest: string[];  // free-form tags matching the enrichment vocabulary
  sober_friendly: boolean;
  alcohol_preference: "none" | "light" | "no-preference";
  transit_modes: Array<"walk" | "subway" | "car" | "bike">;
  available_days: string[];       // ISO dates within the Tech Week window
  notes?: string;
};
```

Profile stored in localStorage under a stable key.

**Acceptance.**

- Text intake completes in under 60 seconds.
- Voice transcription returns within 5 seconds of submit on a 30-second clip.
- Parsed profile is editable in a structured form after parsing.
- Profile updates invalidate cached relevance scores.

### 5.4 Explore mode

**Layout.** Two-column desktop, stacked mobile. Filter panel on left/top, event card grid on right/bottom.

**Structured filters.**

- Day (multi-select)
- Time of day (morning, midday, afternoon, evening, late)
- Neighborhood (multi-select from the extracted set)
- Topic tags (multi-select from enriched vocabulary)
- Vibe (multi-select)
- Alcohol-forward (exclude toggle)
- Sober-friendly (only-show toggle)
- Founder density (multi-select)
- Investor density (multi-select)
- Agentic signal (slider min)
- Priority bucket (Must Review, Strong Candidate, Maybe; computed from relevance score)

**Natural-language search.** Search bar above filters. User types or speaks ("Tuesday afternoon agentic events, no alcohol, Manhattan only"). A Claude call parses the query into a structured filter object. The system shows the parsed interpretation with a clear button.

**Sort.** Relevance (default), chronological, newest added.

**Voice query.** Same mic affordance as intake.

**Two-pass relevance scoring.**

- **Pass 1 (free, instant).** Coarse score computed client-side from the overlap between profile domains-of-interest and event topic_tags, plus a small bonus for matching vibe preferences and a penalty for alcohol-forward when the profile says sober-friendly. No AI call. Used to sort and rank.
- **Pass 2 (AI, lazy).** When an event card is first rendered or saved to shortlist, request a personalized score (0-100) and a 1-2 sentence blurb. Batched at 20 events per call. Cached in localStorage keyed by event UID and a profile hash.

**Acceptance.**

- Filter changes update the list in under 300 ms (client-side filter).
- NL query returns parsed filters in under 2 seconds.
- Filter state is in URL params (shareable filter URLs).
- Two-pass scoring keeps median time-to-first-render under 1 second; personalized blurbs hydrate progressively.

### 5.5 Event card

- **Header:** title, host org, date and time (user-local TZ with NYC-time hint).
- **Location:** neighborhood, expand to full address.
- **Relevance row:** score (0-100), priority bucket, alcohol-forward warning, sober-friendly badge, virtual badge.
- **Why this fits you:** 1-2 sentence personalized blurb (Pass 2 hydrated).
- **Tags:** topic tags + vibe pill.
- **Actions:**
  - Add to Shortlist
  - Add to Calendar (single-event ICS download)
  - RSVP (external link, new tab)
  - Share (copy URL)
- **Expandable:** the one_line_synopsis from enrichment, link to RSVP.

**Acceptance.**

- Personalized blurb hydrates within 1 second of card entering viewport.
- ICS exports import cleanly into Apple Calendar, Google Calendar, Outlook.
- All external links use `target="_blank" rel="noopener noreferrer"`.

### 5.6 Shortlist

- Stored in localStorage, keyed by event UID with status field.
- Statuses: Interested, Going, Maybe, Skipping.
- Dedicated `/tech-week/shortlist` view in chronological order with conflict highlighting.
- Bulk Add-All-To-Calendar exports the full shortlist as one ICS file.

**Acceptance.**

- Persists across sessions on the same device.
- Bulk ICS export contains correct TZID metadata.
- Time conflicts visually flagged.

### 5.7 Schedule generation

**Input.** Shortlist with statuses, profile preferences.

**No maps in V1.** Time-overlap detection only.

**Output.**

```typescript
type ProposedSchedule = {
  generated_at: string;
  profile_hash: string;
  events: Array<{
    event_uid: string;
    decision: "attend" | "skip" | "decide-later";
    rationale: string;
    time_pressure_note?: string;
  }>;
  summary: string;
  conflicts_resolved: Array<{ kept: string; dropped: string; reason: string }>;
};
```

UI is a day-by-day timeline. User can accept, edit per-decision, or regenerate with a different optimization preference (density, breathing-room, networking, talks).

**Acceptance.**

- Completes in under 8 seconds for a 20-event shortlist.
- All time conflicts resolved (no overlapping "attend" decisions).
- Regenerate is idempotent given identical inputs.

### 5.8 Marcus's public route

**View.** `/tech-week/marcus`.

**Source.** A checked-in JSON file at `data/marcus-route.json`:

```typescript
type MarcusRoute = {
  intro_text: string;        // hand-written, not AI-generated
  day_themes: Array<{ date: string; theme: string }>;
  event_statuses: Record<string, "planning" | "applied" | "backup" | "skipping">;
};
```

Marcus edits the file via PR. Deploy refreshes the public page. No admin UI in V1.

**Privacy.** No real-time location. No hotel. No private meetings. The "going" status is intentionally absent from the public set.

---

## 6. V2 feature specification (deferred): Route planning

### 6.1 Transit preferences

Added to profile: default modes, max walking duration per leg, tight-connection threshold, avoid-late-night-subway.

### 6.2 Commute computation

For each consecutive pair of "attend" events:
- Compute travel time via Google Maps Directions API.
- Compare against gap. Classify Comfortable / Tight / Infeasible.

### 6.3 UI integration

Transit chip between events showing mode, duration, feasibility. Tight or infeasible connections show resolution suggestions.

### 6.4 Cost controls

Per (origin_uid, dest_uid, mode) cache. Daily spend cap with alerting at 80% and shutoff at 100%.

### 6.5 Schedule reordering

Generator considers commute cost when choosing among same-slot events.

---

## 7. V3 (parked, signal-gated)

- Shareable public schedule URLs.
- Anonymized "most-shared events" leaderboard.
- Post-event reflections.
- Year-round event database evaluation.
- Multi-user collaborative shortlists.
- Integration with social platforms ("people I follow are attending").

Decision gate: revisit only if V1 and V2 demonstrate sustained value during Tech Week.

---

## 8. Data shapes (no DB in V1)

### 8.1 events.enriched.json (server-owned artifact)

```typescript
type EnrichedEvent = {
  uid: string;                  // from Carly
  title: string;                // normalized
  start: string;                // ISO 8601 with TZ
  end: string;                  // ISO 8601 with TZ
  neighborhood: string;         // extracted
  is_virtual: boolean;
  full_location: string;        // raw LOCATION
  host_org: string;             // extracted
  rsvp_url: string;
  source_url: string;           // points back to Carly for credit
  enrichment: EventEnrichment;  // from section 5.2
  hash: string;                 // content hash for change detection
};

type EnrichedFeed = {
  generated_at: string;
  source_feed_url: string;
  event_count: number;
  events: EnrichedEvent[];
};
```

### 8.2 Profile (localStorage)

Shape from section 5.3, plus a profile_hash for cache invalidation.

### 8.3 Shortlist (localStorage)

```typescript
type ShortlistEntry = {
  event_uid: string;
  status: "interested" | "going" | "maybe" | "skipping";
  added_at: string;
};
type Shortlist = ShortlistEntry[];
```

### 8.4 Relevance cache (localStorage)

```typescript
type RelevanceCacheEntry = {
  event_uid: string;
  profile_hash: string;
  score: number;
  blurb: string;
  computed_at: string;
};
```

### 8.5 Marcus route (checked-in JSON)

Shape from section 5.8.

---

## 9. API surface

Minimal in V1, since most state is client-side.

### 9.1 AI routes

- `POST /api/intake/voice` — multipart audio → `{ transcription }`.
- `POST /api/intake/parse` — body `{ raw_text }` → structured Profile.
- `POST /api/search/parse` — body `{ natural_language_query }` → structured filter object.
- `POST /api/relevance` — body `{ profile, event_uids[] }` → array of `{ event_uid, score, blurb }`. Batched server-side.
- `POST /api/schedule/generate` — body `{ profile, shortlist, optimization_preference? }` → ProposedSchedule.

### 9.2 Data routes

- `GET /api/events` — returns `events.enriched.json` content (cached with Cache-Control headers).
- `GET /api/events/:uid/ics` — single-event ICS.
- `POST /api/shortlist/ics` — body `{ event_uids[] }` → bulk ICS download.

### 9.3 Admin routes (Marcus only, IP-allowlisted or token-gated)

- `POST /api/admin/ingest` — manual ingest trigger.
- `GET /api/admin/ops` — dashboard metrics.

### 9.4 V2 additions

- `POST /api/commute` — body `{ origin_uid, dest_uid, mode }` → `{ duration_seconds, feasibility }`.

---

## 10. AI integration

### 10.1 Models

- **Primary:** Claude Sonnet 4 for relevance scoring, blurb generation, intake parsing, query parsing, schedule generation.
- **Batch enrichment:** Claude Haiku 4.5 for the one-time-per-event tag-and-flag pass (5.2). Validate on a 50-event sample before committing.
- **Transcription:** OpenAI Whisper API (`gpt-4o-transcribe` or `whisper-1`). Self-hosted whisper.cpp on Fly is a V2 cost optimization if usage warrants.

### 10.2 Prompt shapes

- **Enrichment prompt** (Haiku, batch 20): "Given these Tech Week events, infer for each one: topic_tags, vibe, alcohol_forward, sober_friendly, founder_density, investor_density, agentic_signal, one_line_synopsis. Return JSON array."
- **Intake parser** (Sonnet): structured Profile schema as the response shape. Failures fall back to a manual structured form.
- **Query parser** (Sonnet): structured filter schema. Failures fall back to keyword search.
- **Relevance scorer + blurb generator** (Sonnet, batched 20): user profile in system prompt, events in user content. Output array of `{ event_uid, score, blurb }`.
- **Schedule generator** (Sonnet): profile + shortlist + constraints in prompt. Output ProposedSchedule. Constraint: no overlapping attend decisions.

### 10.3 Cost estimate (rough)

- Enrichment: ~1,035 events at ~52 Haiku batch calls. Approximately under $5 total for a full re-enrichment.
- Per-user runtime: relevance scoring 20-40 events per session (only those the user views or shortlists) at batch sizes of 20. Roughly $0.01-0.05 per active session.
- Schedule generation: under $0.02 per generation.
- Whisper: ~$0.006 per minute of audio.

Expected daily ceiling under $30 even at 500 active users per day. Acceptable.

### 10.4 Cost controls

- Per-session rate limit: 50 AI calls per hour.
- Daily spend cap with alerting.
- Graceful degradation to coarse Pass 1 scoring only if API is rate-limited or down.

### 10.5 Caching and invalidation

- Per-event enrichment cached in `events.enriched.json` indefinitely. Invalidated only by ingest pipeline detecting a content hash change.
- Per-user relevance cache in localStorage, invalidated on profile change.
- Schedule generations not auto-cached (each generate is a fresh proposal).

---

## 11. Privacy and safety

Principle: privacy is stewardship, not shame. Archive everything internally, expose only what serves the user.

- **No real-time location.** Ever. V1 or V2.
- **No hotel, home base, private meetings on Marcus's public route.**
- **Voice audio retention.** Audio files retained for 30 days then deleted; transcription text retained against profile in localStorage only.
- **Profile data lives only in the user's browser** by default in V1. The server sees profile content only on AI calls, transiently, and does not persist it.
- **No PII required** to use the product.
- **Data deletion.** A "wipe my data" action clears all localStorage keys.
- **No tracking pixels, no third-party scripts** beyond Vercel Analytics (privacy-respecting) and Sentry.

---

## 12. Tech stack

**Frontend:**

- Next.js 15 (App Router)
- TypeScript strict mode
- Tailwind CSS
- shadcn/ui components
- Framer Motion for transitions
- React Hook Form + Zod

**Backend (Next.js Route Handlers only, no separate service):**

- Node runtime for AI routes
- Edge runtime for static data routes
- `node-ical` for parsing
- `ics` (npm) for export generation
- Server-side Vercel Blob for the enriched feed artifact

**AI:**

- Anthropic SDK (Claude Sonnet 4, Haiku 4.5 for batch enrichment)
- OpenAI SDK (Whisper)

**Infra:**

- Vercel hosting
- Vercel Cron for ingest
- Vercel Blob for `events.enriched.json`
- Sentry for errors
- Vercel Analytics for privacy-respecting metrics

**V2 additions:**

- Google Maps Platform Directions API

**Dev tooling:**

- pnpm
- ESLint + Prettier
- Vitest unit tests
- Playwright smoke tests (matches Anchor pattern)
- GitHub Actions CI

---

## 13. Infrastructure and deployment

**Project name.** `signal-map`.

**Production domain.** `techweek.symposiumstudios.ai` (subdomain decision pending; subroute `symposiumstudios.ai/tech-week` is the alternative).

**Environments.**

- Production: main branch auto-deploys.
- Preview: per-PR Vercel previews.
- Local: `.env.local`.

**Required env vars.**

- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY` (Whisper)
- `BLOB_READ_WRITE_TOKEN` (Vercel Blob)
- `ADMIN_TOKEN` (for admin route gating)
- `SENTRY_DSN`
- V2: `GOOGLE_MAPS_API_KEY`

**Cron.** Vercel Cron at `/api/cron/ingest` every 6 hours pre-Tech-Week, every hour during.

---

## 14. Analytics and observability

**Product analytics (Vercel Analytics, anonymous).**

- Intake completion rate (text vs voice).
- Events viewed per session.
- Filter usage distribution.
- Shortlist conversion (% of intake users with one or more shortlists).
- Schedule generation rate.
- ICS export rate.

**Error monitoring.** Sentry on all API routes and client errors with source maps.

**AI telemetry.** Per-route call counts, latencies, token usage. Daily spend report.

**Ops dashboard.** `/tech-week/admin/ops` showing daily AI spend, error count, active sessions, last successful ingest timestamp, event count.

---

## 15. Distribution and launch

### 15.1 T minus 10 days

- V1 feature-complete.
- Initial enrichment run on the full Carly feed.
- Marcus's route file populated.
- Soft launch to 15 personal contacts attending Tech Week.

### 15.2 T minus 7 days

- Iterate on soft-launch feedback.
- Public post on X and LinkedIn with short demo video.
- Outreach to Carly team, both as courtesy and as potential featuring partner.
- Outreach to a16z Tech Week team.
- Outreach to host orgs whose events score high for Marcus and whose pages might link back.

### 15.3 During Tech Week

- Hourly ingest cron.
- Daily morning broadcast on Marcus's accounts highlighting that day's top signal.
- Real-time issue triage. V2 routing ships mid-week only if V1 traction warrants.

### 15.4 T plus 7 days

- Recap post: traction numbers, what worked.
- V3 directionality decision.

---

## 16. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Carly feed format changes mid-Tech-Week | Medium | High | Defensive parser with field validation. Sentry alert on parse failures. Manual override path. |
| Carly events go stale (cancellations) | High | Medium | Trust Carly's freshness. Display "last ingested" timestamp. Manual override file for known-cancelled events. |
| Enrichment cost spiral | Low | Medium | Haiku for batch, content-hash gating, hard daily cap. |
| Per-user relevance cost spiral | Medium | Medium | Two-pass design. Pass 1 free. Pass 2 lazy + cached + rate-limited. |
| Voice transcription quality on names | High | Low | Editable transcription before submit. |
| Privacy gaffe on Marcus route | Low | High | No real-time data in schema. Manual review of marcus-route.json on every PR. |
| Scope creep beyond Tech Week | High | Medium | V3 explicitly parked. Post-Tech-Week decision gate. |
| Anchor build conflict | High | Medium | Spec only now. Directive fires after Anchor V4.1 Opus run completes. |

---

## 17. Open questions

1. **Domain.** `techweek.symposiumstudios.ai` subdomain or `symposiumstudios.ai/tech-week` subroute? Recommendation: subdomain, easier post-event archive.
2. **Carly courtesy outreach.** Notify Carly before launch? Recommendation: yes, both as good practice and as a potential featuring path. Frame as "intelligence layer on top, not replacement."
3. **Enrichment storage.** Vercel Blob URL vs checked-in JSON in the repo? Recommendation: Blob for V1 (avoids repo bloat with 1,000+ events times ~1KB each).
4. **Schedule optimization preference UX.** Slider, dropdown, or natural-language ("a chill week with breathing room")? Recommendation: dropdown with 4 presets for V1, NL in V1.5.
5. **Anchor sequencing.** Fire directive parallel to Anchor V5.3 or strictly after V4.1 Opus run? Recommendation: after V4.1 to preserve Anchor focus.
6. **Whisper provider.** Hosted OpenAI for V1 vs whisper.cpp on Fly later. Recommendation: hosted for V1.
7. **Vercel Cron vs GitHub Actions for ingest.** Vercel Cron is simpler; GitHub Actions gives more flexibility if ingest grows.

---

## 18. V1 acceptance criteria (release gate)

V1 ships when all of the following are true:

- Carly ICS parses cleanly with zero unhandled VEVENT records.
- Dedup removes the known duplicate pattern (UID collision tolerated, content collision dedup'd).
- 100% of events have neighborhood extracted (or "Unknown" if LOCATION lacks a comma).
- 100% of events have host_org extracted (or "Unknown" if DESCRIPTION lacks "Hosted by ").
- 100% of events have enrichment fields populated.
- Text intake completes end-to-end and produces a usable Profile.
- Voice intake works on iOS Safari, Chrome desktop, Chrome Android.
- Natural-language search returns sensible parses on 8 of 10 representative queries.
- Personalized blurbs feel personalized in qualitative review by Marcus plus two trusted reviewers.
- Shortlist persists across sessions on the same device.
- Single-event and bulk ICS exports import cleanly into Apple Calendar, Google Calendar, and Outlook.
- Schedule generation completes in under 8 seconds on a 20-event shortlist.
- Marcus's public route renders correctly with no real-time location data.
- All API routes return errors gracefully (no 500s on invalid input).
- Sentry shows zero unhandled exceptions on smoke-test paths.
- Lighthouse performance score above 85 on mobile.

---

## 19. Explicit non-goals

- Not a ticketing platform.
- Not an event creation system.
- Not a competitor to Carly (intentionally an intelligence layer above it).
- Not a user-matching or social system.
- Not a real-time location system.
- Not a long-term event database.

---

## 20. Next actions (pre-directive)

1. Resolve the seven open questions in section 17.
2. Confirm domain decision and DNS access.
3. Confirm Anchor sequencing position.
4. Run a one-off Haiku enrichment dry-run on 100 events from the Carly feed to validate the prompt and tag vocabulary before locking 5.2.
5. Generate the AUTONOMY_LAYER companion file for the build.
6. Convert this spec into the META_PROMPT + AUTONOMY_LAYER + directive triplet for CC.

---

*End of specification, v1.1. Carly-aware. Ready for review.*
