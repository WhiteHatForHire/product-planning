# CONTEXT.md — Kairos

Ubiquitous language for the Kairos project. Read first when joining a session. Update via PR when introducing or clarifying domain terms.

## Product terms

- **Kairos** — the product. Named for the Greek concept of the opportune moment. Tech Week is a kairos.
- **Signal Map** — the v1.0 working name for Kairos. Deprecated.
- **Carly feed** — the source-of-truth ICS at `https://www.usecarly.com/calendars/nyc-tech-week-2026.ics`. ~1,035 events. Kairos is an intelligence layer on top, not a competitor.
- **Profile** — the user's intake-derived structured representation: role, what they're building, what they're looking for, sober preferences, transit modes, available days.
- **Shortlist** — the user's curated set of events with statuses (interested, going, maybe, skipping).
- **Marcus's public route** — Marcus's own Tech Week plan, published at `/tech-week/marcus`. Day themes + per-event statuses. No real-time location.

## Scoring terms

- **Enrichment** — the one-time-per-event AI pass that adds tags, vibe, alcohol/sober flags, founder/investor density, agentic signal, and a one-line synopsis. Stored alongside the event in `events.enriched.json`.
- **Two-pass relevance scoring** — Pass 1 is free client-side tag intersection between profile and event enrichment. Pass 2 is lazy AI-generated personalized score + blurb, batched, cached.
- **Personalized blurb** — the 1-2 sentence "why this fits you" rendered on each event card. Pass 2 output.
- **Priority bucket** — Must Review, Strong Candidate, or Maybe. Computed from relevance score.
- **Agentic signal** — 0-3 score for how related an event is to agentic AI specifically.

## Event terms

- **Vibe** — the event's social/format classification: panel, talk, workshop, hackathon, mixer, happy-hour, dinner, breakfast, office-hours, demo, pitch, social, other.
- **Alcohol-forward** — events centered on drinks (Happy Hour, Mixer, Drinks). Inferred from title.
- **Sober-friendly** — events compatible with sober attendance (runs, breakfasts, coffee, workshops, hackathons). Inferred from title.
- **Founder density / investor density** — high/medium/low/unknown. Inferred from title and host.
- **Virtual event** — LOCATION starts with "Virtual". Flagged separately on event cards.

## Architecture terms

- **events.enriched.json** — the server-owned artifact (Vercel Blob) holding all parsed + enriched events. Rebuilt by the ingest pipeline.
- **Ingest pipeline** — fetches Carly ICS, parses, dedups, normalizes, enriches via Haiku batch, writes to Blob. Runs every 6 hours pre-Tech-Week, hourly during.
- **Profile hash** — a deterministic hash of the user's profile used as a cache key for personalized scoring.
- **Spec-reality reconciliation** — `AUTONOMY_LAYER.md` section 1.13. Always run before implementing against directive design data.

## Symposium terms

- **AUTONOMY_LAYER** — execution protocol. See `.symposium/AUTONOMY_LAYER.md`.
- **META_PROMPT** — spec-to-directive converter. See `.symposium/META_PROMPT.md`.
- **Skill** — an invocable named pattern with a SKILL.md. See `.symposium/skills/`.
- **Council of Models** — multi-model review (Claude, GPT, Gemini, Grok) for safety-adjacent or high-stakes content.
- **Director Model** — Marcus's pattern of directing agents rather than writing code directly.

## Anti-vocabulary (do not use these unless quoting)

- "Vibes" — use specific language: tone, energy, atmosphere, register.
- "Just" / "simply" — implies effort the agent should never imply.
- "AI-native" in client-facing copy — overused.
- "Signal Map" as the product name — superseded by Kairos.
