---
name: ics-feed-diagnostic
category: diagnostics
trigger: Before any wave that depends on the Carly ICS feed structure.
---

# ICS Feed Diagnostic

## Purpose
Validate the Carly ICS feed shape and data quality before any wave that consumes it. Prevent surprises mid-ingest.

## When to invoke
- Before the ingest pipeline phase
- After any reported Carly format change
- Before adding new fields to `events.enriched.json`
- When debugging missing or malformed events

## Inputs
- Carly ICS URL (currently `https://www.usecarly.com/calendars/nyc-tech-week-2026.ics`)
- Expected field set (UID, DTSTART, DTEND, SUMMARY, DESCRIPTION, LOCATION, URL)

## Process
1. Fetch the feed.
2. Parse with `node-ical` (or equivalent).
3. Count total VEVENT records.
4. For each field in the expected set, count presence (% of events containing it).
5. Run dedup pass on UID. Report duplicate count and pattern.
6. Sample 10 events for manual eyeballing of field content quality.
7. Detect format anomalies: smart quotes, em-dashes, truncated titles, missing TZID, virtual flag patterns.
8. Verify timezone correctness (TZID=America/New_York expected).
9. Extract unique neighborhoods from LOCATION (split on first comma). Report count.
10. Extract unique host orgs from DESCRIPTION (regex on "Hosted by "). Report count.
11. Produce diagnostic report.

## Output
A markdown report with:
- Total event count
- Field presence percentages
- Duplicate UID count + sample
- Format anomaly list
- Unique neighborhood count + top 10
- Unique host org count + top 10
- 10-event sample with full fields
- Recommended ingest pipeline assertions to add

## Stop conditions
- Halt if total event count is dramatically different from the last known baseline (over 25% delta in either direction). Investigate before ingesting.
- Halt if any required field has under 90% presence. Adjust ingest pipeline to handle missing-field cases.
- Halt if TZID is missing on any event. Time data cannot be trusted.

## Related
- `AUTONOMY_LAYER.md` section 1.13 (spec-reality reconciliation)
- `skills/diagnostics/api-surface-diagnostic` (analogous skill for internal APIs)
