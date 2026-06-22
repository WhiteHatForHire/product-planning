---
title: "tech week signal map spec v1"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Kairos app /tech week signal map spec v1.docx"
status: active
privacy: working
tags:
  - product
---

# tech week signal map spec v1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
NYC Tech Week

Signal Map

Product Specification v1.0

Owner

Marcus Vale / Symposium Studios (Bisel Legacy Global LLC)

Repository

https://github.com/WhiteHatForHire/nyc-techweek-scheduler

Production domain

techweek.symposiumstudios.ai (decision pending)

ICS export endpoint

/api/events/:id/ics  |  /api/shortlist/ics?profile_id=...

Target launch window

Pre NYC Tech Week 2026, soft launch ~10 days prior

Status

Spec approved, pre-directive

Last updated

2026-05-16

0. Telos and Positioning

Convert the noisy NYC Tech Week event firehose into a decision-ready, personalized schedule. Reduce attendee decision fatigue. Demonstrate the Symposium Studios agentic delivery thesis on a public, time-bounded artifact.

Positioning line:

A personalized signal map for NYC Tech Week. Tell it who you are, it tells you which events matter for you. Built by Symposium Studios as a live prototype of agentic event intelligence.

Strategic intent. This is a Symposium proof artifact first, a useful tool second. It exists to:

Open conversations with founders, operators, and investors at Tech Week.

Demonstrate the Symposium pattern (messy inputs, AI enrichment, decision-ready output) in public.

Provide a working live demo Marcus can reference in fCTO conversations and partnership pitches.

The product must be polished enough to feel finished, not a demo with rough edges. One excellent thing beats five half-built ones.

What this is not:

Not a year-round events platform.

Not a social network or real-time location tracker.

Not a ticketing or RSVP system.

Not a competitor to Luma, Partiful, or the a16z official feed.

1. Target Users

Primary: The signal-seeking attendee

A founder, operator, investor, or builder with a specific goal. Examples:

Technical founder building agentic infra, looking for AI workflow rooms and devtools peers.

Investor scanning for agentic commerce and workflow automation deal flow.

Operator or exec hunting for fractional CTO or technical leadership signal.

Sober attendee filtering out alcohol-forward parties.

Time-constrained attendee with one open afternoon, optimizing for highest-value rooms.

Secondary: The curious browser

No deep goal yet. Wants to see what is happening. May convert to primary once they complete intake.

Anti-persona

Casual social attendees who want to party. This tool is not for them and that is fine.

2. Phasing Overview

V1 ships everything except maps-based routing. V2 adds the routing layer. V3 is polish and post-Tech-Week extensions.

Phase

Scope

Target

V1

Intake (text + voice), Explore, Shortlist, Schedule generation, personalized relevance blurbs, ICS export, Marcus public route, natural-language filter parsing

Pre-launch

V2

Maps Directions integration, transit preferences, per-leg commute time, tight-connection warnings, route ordering

Mid-week if traction warrants

V3

Shareable public schedules, post-event reflection, year-round event database evaluation

Post-Tech-Week, decision gated

3. V1 Feature Specification

3.1 Intake

Purpose: capture enough about a user to generate personalized relevance scoring and event blurbs.

Modality

Text intake. Text intake:

A single freeform textarea: "Tell me about yourself: who you are, what you're building, and what you're looking for at Tech Week."

Plus structured toggles: sober-friendly preference, transit mode defaults, free days.

Voice intake. Voice intake:

A mic button adjacent to the textarea. User taps, speaks, audio uploads, Whisper transcribes.

Transcription appears in the textarea, editable before submit.

Voice modality ships in V1, not deferred.

Profile shape (parsed from intake)

role, company, stage, what_building, looking_for[], domains_of_interest[], sober_friendly, alcohol_preference, transit_modes[], available_days[], notes

Acceptance criteria

Text intake completable in under 60 seconds.

Voice intake transcribes within 5 seconds on a 30-second clip.

The parsed profile is editable before saving.

Profile updates invalidate cached relevance blurbs.

3.2 Explore Mode

Purpose: browse events with structured filters and natural-language search.

Structured filters

Day (multi-select, Tech Week dates)

Time of day (morning, midday, afternoon, evening, late)

Neighborhood (Manhattan submarkets, Brooklyn submarkets)

Topic tags (agentic, devtools, founder, investor, infra, applied AI, design, healthcare, fintech, sober/wellness, etc.)

Priority bucket (Must Review, Strong Candidate, Maybe; computed from relevance score)

Alcohol-forward exclude toggle

Sober-friendly only-show toggle

RSVP status (open, waitlist, invite-only)

Natural-language search

Search bar above the filter panel. User types or speaks a query. A Claude API call parses the query into a structured filter object and applies it. System shows the parsed interpretation below the search bar (e.g., "Showing Tuesday afternoon events tagged agentic, alcohol-forward excluded, neighborhood = Manhattan") with a clear button.

Voice query

Same mic affordance as intake. Spoken query goes through Whisper, populates search bar, parsed and applied automatically.

Acceptance criteria

Filter changes update the event list in under 300ms (client-side filtering on a cached event set).

Natural-language queries return parsed filters in under 2 seconds.

Filter state is preserved in URL params (shareable filter URLs).

Empty states explain why no events match and suggest filter loosening.

3.3 Event Card

Each event card shows:

Header: title, host org, date and time in user-local timezone with NYC-time hint.

Location: venue name, neighborhood. Full address revealed on expand.

Relevance row: score (0-100), priority bucket badge, alcohol-forward warning, sober-friendly badge.

Why this fits you: 1-2 sentence personalized blurb generated from the user profile, cached per (profile_id, event_id) pair.

Tags: topic tags as pills.

Actions row: Add to Shortlist (toggle), Add to Calendar (downloads single-event ICS file), RSVP (external link), Share (copy URL).

Expandable description: full event details, host blurb, link to host page.

ICS export

The Add to Calendar button generates a valid .ics file for the single event. The ICS endpoint lives at:

GET /api/events/:id/ics

A bulk ICS export of the entire shortlist is also available:

GET /api/shortlist/ics?profile_id=...

Both endpoints produce .ics files that import cleanly into Apple Calendar, Google Calendar, and Outlook. Tested against all three as a V1 acceptance gate.

Acceptance criteria

Personalized blurbs render within 1 second on first viewport entry (lazy-generated, cached thereafter).

Add to Calendar produces a valid .ics file confirmed in Apple Calendar, Google Calendar, and Outlook.

All external links open in new tabs with rel=noopener noreferrer.

3.4 Shortlist

Purpose: a user-curated set of events the user is seriously considering. The shortlist is the input to schedule generation.

Add or remove from any event card or detail page.

Dedicated /tech-week/shortlist view in chronological order.

Per-event status toggle: Interested, Going, Maybe, Skipping.

Bulk Add-All-To-Calendar exports the entire shortlist as one ICS file.

Conflict indicator: overlapping events are visually flagged (red border or warning chip on both cards).

Acceptance criteria

Shortlist persists across sessions (anonymous via local storage; cross-device via magic-link).

Bulk ICS export contains all events with correct timezone metadata.

Conflict highlighting is unambiguous.

3.5 Schedule Generation

Purpose: given the shortlist, propose a coherent attended schedule that minimizes regret.

Inputs

User shortlist with statuses.

User profile (availability, transit modes, alcohol preference).

V1: time-overlap conflict detection only. No maps data.

Output shape

A ProposedSchedule object with: per-event decision (attend / skip / decide-later), rationale (1 sentence, Claude-generated), time pressure notes, summary narrative (2-3 sentences), and a list of conflicts resolved with the event kept and dropped plus reason.

UI

A day-by-day timeline view with each event slot showing the decision and rationale. User can accept the proposal, edit individual decisions, or regenerate with a different optimization preference (density, breathing room, prioritize networking, prioritize talks).

Acceptance criteria

Generation completes in under 8 seconds for a 20-event shortlist.

All time conflicts are surfaced and resolved (no overlapping attend decisions).

Regenerate is deterministic given the same inputs.

3.6 Marcus's Public Route

Purpose: Marcus's own Tech Week plan, published as a public artifact and worked example for visitors. Lives at /tech-week/marcus.

Content

Day-by-day narrative (Monday: ecosystem day. Tuesday: agentic delivery thesis day. Wednesday: relationship and follow-up day. Thursday: harvest day. Friday: close loops.)

Per-event status: Planning, Applied, Backup, Skipping. The status Going is intentionally not exposed on the public view.

No hotel, no home base, no private meetings, no real-time location.

Brief "what I'm looking for this week" intro section, authored by Marcus, not AI-generated.

Privacy frame

Public schedule shows intent, not presence. Live status is never exposed in V1 or V2.

Acceptance criteria

Marcus can edit his route through an authenticated admin view at /tech-week/marcus/edit.

Public view is statically generated or aggressively cached, revalidated on each edit.

4. V2 Feature Specification: Route Planning

4.1 Transit preferences

Added to the profile structured form:

Default transit modes: Walk, Subway, Car/Rideshare, Bike. Multi-select.

Max walking distance per leg: slider, default 15 minutes.

Tight-connection threshold: slider, default 15 minutes of buffer.

Avoid late-night subway: toggle (default off).

4.2 Commute computation

On schedule generation, for each consecutive pair of attended events the system computes:

Origin and destination coordinates.

Preferred transit mode from profile (or best of allowed modes).

Estimated travel time via Google Maps Directions API.

Comparison against available buffer.

Classification: Comfortable, Tight, Infeasible.

4.3 UI integration

The proposed schedule timeline shows a transit chip between each event with mode icon, duration, and color-coded feasibility. Tight or infeasible connections show suggested resolutions.

4.4 Cost controls

Maps API calls cached per (origin_event_id, destination_event_id, mode) tuple. Schedule regeneration reuses cached commutes. Daily spend cap configured at deploy time with alerting at 80%.

Acceptance criteria

First-time schedule generation with 10 events makes at most 9 Maps Directions API calls.

Cached regeneration makes zero Maps calls.

Daily Maps API spend has a hard cap with an alert at 80%.

5. V3 Feature Notes (Parked)

V3 is deliberately unspecced. Revisit only if V1 and V2 demonstrate sustained user value beyond Tech Week.

Shareable public schedules with unique URLs.

Schedule-sharing analytics (anonymized aggregate most-shared events leaderboard).

Post-event reflection capture.

Year-round event database evaluation.

Multi-user collaborative shortlists.

Integration with X or LinkedIn for social-graph event signal.

6. Data Model

Drizzle ORM with Neon Postgres. Matches the Anchor stack.

events

id, slug, title, description, host_org, host_url, start_time, end_time (timestamptz), venue_name, address, neighborhood, latitude, longitude, rsvp_url, rsvp_status (open | waitlist | closed | invite-only | unknown), alcohol_forward (bool), sober_friendly (bool), tags (text[]), source (curated | a16z | partiful | luma | manual), source_url, created_at, updated_at

profiles

id, session_id (unique), email (nullable), raw_intake_text, intake_audio_url, parsed (jsonb), created_at, updated_at

event_user_state

id, profile_id (fk), event_id (fk), status (interested | shortlisted | going | maybe | skipping | planning | applied | backup), ai_relevance_score (0-100), ai_relevance_blurb, ai_blurb_generated_at, added_at — unique (profile_id, event_id)

generated_schedules

id, profile_id (fk), shortlist_snapshot (uuid[]), proposed (jsonb ProposedSchedule), optimization_preference, created_at

commute_cache (V2)

id, origin_event_id (fk), destination_event_id (fk), mode (walk | subway | car | bike), duration_seconds, raw_response (jsonb), cached_at — unique (origin_event_id, destination_event_id, mode)

Special user

Marcus's profile is seeded with a known session_id and admin flag. The /tech-week/marcus public view queries event_user_state filtered to his profile_id and renders planning, applied, backup, and skipping statuses only.

7. API Surface

All routes under /api/. Next.js App Router conventions.

Intake

POST /api/intake/text — body: { raw_text } — returns { profile_id, parsed }

POST /api/intake/voice — multipart audio upload — returns { transcription, profile_id, parsed }

PATCH /api/intake/:profile_id — updates parsed profile, invalidates cached blurbs

Events

GET /api/events — query params: filter set — returns paginated event list

POST /api/events/search — body: { natural_language_query, profile_id? } — returns { parsed_filters, events }

GET /api/events/:id — full event detail

GET /api/events/:id/ics — ICS file download for single event

Shortlist

GET /api/shortlist?profile_id=... — returns shortlist with statuses

POST /api/shortlist — body: { profile_id, event_id, status } — upsert

DELETE /api/shortlist/:id — remove

GET /api/shortlist/ics?profile_id=... — bulk ICS export for entire shortlist

Schedule

POST /api/schedule/generate — body: { profile_id, optimization_preference? } — returns ProposedSchedule

GET /api/schedule/:id — returns cached schedule

AI helpers

POST /api/ai/relevance — body: { profile_id, event_ids[] } — returns array of { event_id, score, blurb }. Batches under the hood. Used for lazy hydration of event cards.

Maps (V2)

POST /api/commute — body: { origin_event_id, destination_event_id, mode } — returns { duration_seconds, feasibility }. Reads commute_cache before hitting Maps API.

Admin (Marcus only)

PATCH /api/admin/events/:id — edit event

POST /api/admin/events — manual event creation

PATCH /api/admin/marcus-route — edit Marcus day narratives and event statuses

8. AI Integration

8.1 Models

Primary: Claude Sonnet 4 via Anthropic API for all structured generation (intake parsing, query parsing, relevance scoring, schedule generation).

Cost-optimization candidate: Claude Haiku 4.5 for high-volume batch scoring of 50+ event lists. Validate quality vs Sonnet on a sample before committing.

Transcription: OpenAI Whisper API (whisper-1 or gpt-4o-transcribe) for voice intake. Evaluate self-hosted whisper.cpp on Fly as a cost alternative if usage warrants.

8.2 AI call shapes

Intake parser: Profile schema in system prompt. Raw intake text as user content. Response is JSON validated against schema. Failure fallback: structured form for manual entry.

Query parser: Filter schema in system prompt. Natural-language query as user content. Response is JSON filter object. Failure fallback: keyword search.

Relevance scorer and blurb generator: Batched at 10-15 events per call. System prompt is user profile plus scoring rubric. Response is array of { event_id, score, blurb }.

Schedule generator: System prompt is user profile and shortlist with constraints (no time overlap, alcohol preference, energy curves). Response is ProposedSchedule shape.

8.3 Caching and invalidation

Relevance scores and blurbs cached per (profile_id, event_id). Invalidated on profile update or event content change.

Schedule generations stored per request; each generate call is a fresh proposal.

Query parses not cached (cheap, high variance).

8.4 Cost controls

Rate limit per session: 50 AI calls per hour.

Daily spend cap with alerting.

Fallback to keyword/structured-only mode if AI is unavailable or rate-limited.

9. Maps Integration (V2)

Provider: Google Maps Platform, Directions API.

Modes: Driving, Transit (subway), Walking, Bicycling.

Auth: server-side API key only. Never exposed to client.

Caching: commute_cache table. Target cache hit rate above 80% after first schedule generation per user.

Fallback: straight-line distance with mode-specific assumed speed if Maps API fails. Result marked as estimate in UI.

Cost cap: hard daily cap with alerting at 80% and shutoff at 100%.

10. Auth and Identity

V1 default: anonymous sessions

Session ID stored in HTTP-only cookie.

Profile and shortlist tied to session.

No login required to use the product.

Optional: magic-link sign-in

"Save my profile to access on another device" prompt after intake completion.

Email entered, magic link sent via Resend, click links the email to the existing session_id.

Subsequent visits from any device with the link reattach to the same profile.

Admin auth (Marcus only)

Hardcoded email allowlist for /tech-week/marcus/edit and /api/admin/*.

Magic-link sign-in for the admin email.

11. Privacy and Safety

Principle: privacy is stewardship, not shame. Archive everything, expose only what serves the user.

No real-time location. Ever. Not in V1, not in V2.

No hotel or home base. Marcus's public view never reveals where he sleeps or works from.

No private meetings on public views. The public Marcus route shows status buckets only.

Voice audio retained for 30 days then deleted; transcription text retained against profile. Configurable per user.

Email retained for re-auth only. Never sold, never used for outbound marketing without explicit opt-in.

Data deletion: a delete-my-profile action wipes profile, shortlist, generated schedules, and audio files. Honored within 24 hours.

No PII required. A user can complete intake and use the entire product without providing any identifying information.

12. Tech Stack

Frontend

Next.js 15 (App Router)

TypeScript strict mode

Tailwind CSS

shadcn/ui components (matches Anchor stack)

Framer Motion for transitions

React Hook Form + Zod for forms and validation

Backend

Next.js Route Handlers (Node runtime for AI calls; Edge runtime for static reads)

Drizzle ORM

Neon Postgres (serverless)

AI and voice

Anthropic SDK (Claude Sonnet 4, Haiku 4.5 for batch scoring)

OpenAI SDK (Whisper for voice transcription)

Infrastructure

Vercel (hosting and cron for cache invalidation)

Resend (transactional email, magic links)

Sentry (error monitoring)

PostHog (product analytics, anonymous by default)

V2 additions

Google Maps Platform Directions API

Dev tooling

pnpm

ESLint + Prettier

Vitest for unit tests

Playwright for smoke tests (matches Anchor pattern)

GitHub Actions for CI

13. Infrastructure and Deployment

GitHub repository: https://github.com/WhiteHatForHire/nyc-techweek-scheduler

Hosting: Vercel. Project name signal-map. Production domain: techweek.symposiumstudios.ai (pending decision between subdomain and subroute).

Environments

Production: techweek.symposiumstudios.ai

Preview: per-PR Vercel previews against the dev Neon branch

Local: .env.local with local Postgres or Neon dev branch

Required secrets

ANTHROPIC_API_KEY

OPENAI_API_KEY (for Whisper)

DATABASE_URL (Neon)

RESEND_API_KEY

SENTRY_DSN

POSTHOG_KEY

ADMIN_EMAILS (comma-separated allowlist)

GOOGLE_MAPS_API_KEY (V2)

Deployment flow

main branch auto-deploys to production.

Feature branches get Vercel previews.

Database migrations via Drizzle, run as a deploy step.

Neon PITR for backups. Profile and shortlist data is high-value; events table is rebuildable.

14. Analytics and Observability

Product analytics (PostHog, anonymous)

Intake completion rate (text vs voice)

Events browsed per session

Filter usage distribution

Shortlist conversion rate (% of intake users who shortlist at least one event)

Schedule generation usage

ICS export rate

Returning sessions

Error monitoring (Sentry)

All API route exceptions

Client-side errors with source maps

AI call telemetry

Per-route call counts, latencies, and token usage

Daily spend report

Operational dashboard

A simple admin dashboard at /tech-week/admin/ops showing daily AI spend, Maps spend (V2), error count, and active sessions.

15. Distribution and Launch Plan

Pre-launch (T minus 10 days)

V1 feature-complete.

80% of Tech Week event database ingested and tagged.

Marcus's public route drafted and published.

Soft launch to ~15 personal contacts attending Tech Week. 48 hours of qualitative feedback.

Soft public launch (T minus 7 days)

Iterate on soft-launch feedback.

Post on X and LinkedIn with a short demo video.

Outreach to a16z Tech Week team with a working link.

Outreach to host orgs of top-relevance events for featured event treatment.

During Tech Week

Daily morning broadcast with that day's signal-map highlights.

Real-time tweaks to event database as changes emerge.

V2 routing layer ships mid-week only if V1 has clear traction (10+ active shortlists per day).

Post-Tech-Week (T plus 7 days)

Publish a recap post: traction numbers, what worked, what was learned.

Decide on V3 directionality based on signal.

Either retire gracefully (archive page) or extend to next event (SF, Berlin, etc.).

16. Risk Register

Risk

Likelihood

Impact

Mitigation

Event data staleness

High

Med

Manual review cadence (daily during week), prominent last-updated timestamps, user-reported corrections via feedback form

AI cost spiral on batch scoring

Med

Med

Haiku fallback for large lists, per-session rate limits, hard daily cap with shutoff

Maps API cost spiral (V2)

Med

High

Aggressive caching, hard daily cap, fallback to estimates

Privacy gaffe (Marcus location exposed)

Low

High

No real-time location in schema. Public route code-reviewed. Privacy checklist in PR gate.

Voice transcription quality on jargon

High

Low

Editable transcription before submit. No silent failure.

Organizers object to event data use

Med

Med

Curated + link-back to host pages. Honor opt-out within 24h. Complement framing.

Scope creep beyond Tech Week

High

Med

V3 explicitly parked. Post-Tech-Week decision gate.

Anchor build conflict

High

Med

Spec only now. Directive fires after Anchor V4.1 Opus run completes.

17. Open Questions

Resolve before converting this spec to a CC directive.

Event data source: curated only vs hybrid with public scrape (a16z, Luma, Partiful)? Recommendation: hybrid, curated primary.

Domain: techweek.symposiumstudios.ai subdomain vs symposiumstudios.ai/tech-week subroute? Recommendation: subdomain for clean separation and easier post-event archival.

Whisper provider: OpenAI hosted API (V1 simplicity) vs self-hosted whisper.cpp on Fly (cost)?

Schedule generation optimization preference UX: slider, dropdown, or natural-language input?

Tech Week 2026 canonical date range: confirm before event ingestion begins.

Anchor sequencing: fire this directive parallel to Anchor V5.3 merge, or strictly after V4.1 Opus run completes? Recommendation: after V4.1.

iCal subscription URL (live feed) vs ICS file download: subscription auto-updates as Marcus changes statuses. Recommendation: defer to V1.5 unless trivially cheap to implement.

18. V1 Acceptance Criteria (Release Gate)

V1 ships when all of the following pass:

Text intake works end-to-end and produces a usable profile.

Voice intake works end-to-end on iOS Safari, Chrome desktop, and Chrome Android.

At least 80% of confirmed Tech Week events ingested with tags, neighborhoods, and relevance fields populated.

Natural-language search returns sensible parses on 8 of 10 representative queries.

Personalized relevance blurbs feel personalized on qualitative review by Marcus plus two trusted reviewers. No generic failures.

Shortlist persists across sessions for anonymous users.

ICS export imports cleanly into Apple Calendar, Google Calendar, and Outlook.

Schedule generation completes in under 8 seconds on a 20-event shortlist.

Marcus's public route renders correctly with no real-time location data.

All API routes return errors gracefully. No 500s on invalid input.

Sentry shows zero unhandled exceptions on the smoke-test path.

Lighthouse performance score above 85 on mobile.

19. Explicit Non-Goals

This product does not sell tickets, broker RSVPs, or handle payment.

This product does not host events.

This product does not match users to each other.

This product does not provide real-time location, messaging, or chat.

This product does not store conversational history beyond profile data.

This product is not a CMS for event organizers.

20. Next Actions (Pre-Directive)

Resolve the seven open questions in section 17.

Confirm domain decision and acquire DNS configuration access.

Confirm Anchor V4.1 Opus run completes before firing this directive.

Generate the AUTONOMY_LAYER.md companion file (standard build harness).

Convert this spec into the directive format: META_PROMPT.md + AUTONOMY_LAYER.md + directive, fired at CC with Opus.

End of specification, v1.0. Ready for review.
