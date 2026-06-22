# ADR 0003: Carly ICS Feed as Source of Truth for Events

**Date**: 2026-05-16
**Status**: Accepted
**Authors**: Marcus Vale / Symposium Studios

## Context

NYC Tech Week 2026 has over 1,000 events. Kairos needs an event database. Building one from scratch (scraping Luma, Partiful, manual curation) is a significant engineering effort that does not advance the product's actual value proposition (intelligence layer, not aggregation).

Carly already aggregates Tech Week events into a public ICS feed at `https://www.usecarly.com/calendars/nyc-tech-week-2026.ics`. The feed contains UID, DTSTART, DTEND, SUMMARY, DESCRIPTION, LOCATION, URL. Approximately 1,035 events. Updated by Carly's team.

## Decision

Use the Carly ICS feed as the source of truth for Kairos events. Build no independent event ingestion. Kairos is positioned explicitly as an intelligence layer above Carly's aggregation.

The ingest pipeline:
1. Fetches the Carly ICS at intervals (every 6 hours pre-Tech-Week, hourly during).
2. Parses, dedups, normalizes.
3. Enriches via AI (tags, vibe, alcohol/sober flags, founder/investor density, agentic signal, one-line synopsis).
4. Writes to `events.enriched.json` in Vercel Blob.

Kairos credits Carly visibly on event cards and in the product footer. Outreach to Carly before public launch is recommended.

## Consequences

### Positive
- Engineering effort focused on AI enrichment and personalization, not aggregation.
- Carly's freshness becomes Kairos's freshness. No independent data quality burden.
- Clean positioning: Kairos is not a competitor to Carly. It is a complement.
- Outreach path to Carly opens potential featuring or partnership.

### Negative
- Dependency risk: if Carly removes or changes the feed mid-Tech-Week, Kairos degrades.
- Cannot include non-Carly events without separate ingestion (e.g., curated additions).
- Carly's coverage gaps become Kairos's coverage gaps.

### Neutral
- Carly's data quality choices (smart quotes, em-dashes, occasional duplicate UIDs) require defensive parsing on our side. Captured in `skills/diagnostics/ics-feed-diagnostic`.

## Alternatives Considered

- **Independent scraping of Luma + Partiful**: rejected for V1. Effort does not advance core product value. Reconsider only if Carly proves unreliable.
- **Carly + manual supplements file**: deferred. Could be added in V1.5 if specific high-value events are missing from Carly.
- **No event database, just live querying Carly**: rejected. Performance and reliability suffer; enrichment requires persistence.

## References

- Kairos spec v1.1, section 3 (Source Feed Analysis)
- ADR 0002 (File-First Architecture) — related decision
- `.symposium/skills/diagnostics/ics-feed-diagnostic/SKILL.md`
