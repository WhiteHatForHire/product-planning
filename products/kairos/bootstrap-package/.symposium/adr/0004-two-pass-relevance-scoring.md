# ADR 0004: Two-Pass Relevance Scoring (Free Pass 1, Lazy AI Pass 2)

**Date**: 2026-05-16
**Status**: Accepted
**Authors**: Marcus Vale / Symposium Studios

## Context

Kairos has approximately 1,035 events and an open user base. Naive per-event AI scoring for every user session would mean ~1,035 AI calls per user per session. At even Haiku prices, this becomes expensive at any meaningful scale, and would slow initial page render.

Most users will not view all 1,035 events. They will filter, scroll, and engage with maybe 20-40 events in a session.

## Decision

Adopt a two-pass relevance scoring approach:

- **Pass 1 (free, client-side, instant)**: Compute a coarse relevance score from the overlap between the user's profile (domains_of_interest, vibe preference, alcohol_preference) and the event's enrichment (topic_tags, vibe, alcohol_forward). Pure set intersection plus a few weighted modifiers. No AI call. Used for initial sort and rank.

- **Pass 2 (AI, lazy, cached)**: When an event card enters the user's viewport or is added to the shortlist, request a personalized score (0-100) and a 1-2 sentence "why this fits you" blurb from Claude. Batch at 20 events per call. Cache in localStorage keyed by event UID and profile hash.

## Consequences

### Positive
- Per-user runtime cost stays bounded. ~$0.01-0.05 per active session.
- Initial page render is fast. Pass 1 is free and synchronous.
- Pass 2 hydrates progressively as users scroll, feels responsive.
- Cache hits on repeat sessions are free.

### Negative
- Top-of-feed ordering is based on Pass 1 (coarse), not Pass 2 (personalized). Users may see slightly suboptimal initial ordering until they scroll.
- Two scoring systems to maintain.
- Cache invalidation on profile change is explicit (profile hash changes).

### Neutral
- Schedule generation uses Pass 2 results when available, falls back to Pass 1.

## Alternatives Considered

- **Pass 2 only, on-page-load**: rejected for cost and initial render time.
- **Pass 1 only**: rejected because the personalized blurbs are the product's killer feature. Without them, Kairos is just a filter.
- **Pre-computed Pass 2 for every (event, profile-archetype) tuple**: rejected. Profiles are too high-dimensional to enumerate archetypes without losing personalization.
- **Pass 2 with cheaper model (Haiku)**: deferred. Validate on a sample before committing.

## References

- Kairos spec v1.1, section 5.4 (Explore Mode)
- Kairos spec v1.1, section 10.3 (Cost Estimate)
