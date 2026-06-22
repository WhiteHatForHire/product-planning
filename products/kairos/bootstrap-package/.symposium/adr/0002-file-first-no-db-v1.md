# ADR 0002: File-First Architecture for Kairos V1 (No Database)

**Date**: 2026-05-16
**Status**: Accepted
**Authors**: Marcus Vale / Symposium Studios

## Context

Kairos V1 needs to ship in under two weeks before NYC Tech Week. The product is an intelligence layer over the Carly ICS feed: ingest events, enrich them with AI tags, let users filter and shortlist, generate proposed schedules.

Two architectural options:

1. Full backend with Postgres (matches the Anchor stack precedent).
2. File-first: events as a JSON blob in Vercel Blob, profile and shortlist in localStorage, Marcus's route as a checked-in JSON file.

## Decision

Adopt the file-first approach for V1. No database. Defer database adoption to V2 only if shareable schedules, cross-device sync, or analytics-at-scale become priorities.

## Consequences

### Positive
- Materially faster to ship. No Drizzle, no migrations, no Neon setup.
- Lower operational complexity. No database to maintain or back up during Tech Week.
- Profile data is genuinely private (lives in the user's browser, not in our database).
- Events are rebuildable from the source feed at any time. No data-loss risk.

### Negative
- No cross-device sync of profile or shortlist for V1.
- No server-side analytics on user behavior beyond Vercel Analytics.
- Schedule generations cannot be shared via URL (deferred to V3).
- If Marcus wants to add user accounts later, requires a migration of localStorage data to server.

### Neutral
- Marcus's public route is edited via PR, not via admin UI. Acceptable in V1.

## Alternatives Considered

- **Full Postgres + auth**: rejected for V1 due to timeline. Reconsidered for V2 if traction warrants.
- **Hybrid (events.json in repo, profile in Postgres)**: rejected as worst-of-both. Adds DB complexity without the benefit of full DB capabilities.
- **Vercel KV instead of Blob**: considered. Blob is sufficient for the single-artifact use case; KV adds complexity without benefit.

## References

- Kairos spec v1.1, section 4 (V1 Architecture Overview)
- ADR 0003 (Carly as Source of Truth) — related decision
