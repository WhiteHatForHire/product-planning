---
name: feed-diagnostic
category: diagnostics
trigger: Before any wave that depends on an external feed, API, or scraped data source structure.
---

# Feed Diagnostic

## Purpose
Validate the shape and data quality of any external data feed (ICS, RSS, JSON API, scraped HTML, CSV export, third-party webhook) before any wave that consumes it. Prevent surprises mid-ingest.

## When to invoke
- Before the first ingest pipeline phase that consumes a new external feed
- After any reported upstream format change
- Before adding new fields derived from upstream data
- When debugging missing or malformed records downstream
- After any upstream provider migration, API version bump, or schema change

## Inputs
- Feed source URL or endpoint
- Expected field set (the fields the project actually relies on downstream)
- Authentication if required
- Last-known baseline counts and field-presence rates (if any prior run)

## Process
1. Fetch the feed. Use the actual parser the project will use, not a one-off shim.
2. Count total records.
3. For each field in the expected set, count presence (% of records containing it).
4. Run a uniqueness pass on whatever the project treats as a primary key (UID, id, slug, content hash). Report duplicate count and pattern.
5. Sample 10 records for manual eyeballing of field content quality.
6. Detect format anomalies relevant to the source type (see worked examples below).
7. For each field downstream code branches on, extract the cardinality and the top-N values. Report.
8. Run a sanity check against the last-known baseline if one exists: total record count delta, field-presence drift, new unexpected fields.
9. Domain-specific extraction patterns — fill in per project. Examples: timezone parsing from time-bearing fields, neighborhood extraction from location strings, host org extraction from description text. The project's own SKILL variant can hardcode these.
10. Produce diagnostic report.

## Output
A markdown report with:
- Total record count
- Field presence percentages
- Duplicate-key count + sample
- Format anomaly list
- Cardinality and top-N values for branchable fields
- Baseline drift summary
- 10-record sample with full fields
- Recommended ingest pipeline assertions to add (defensive parsing, schema guards, dead-letter routing)

## Stop conditions
- Halt if total record count is dramatically different from the last known baseline (over 25% delta in either direction). Investigate before ingesting.
- Halt if any required field has under 90% presence. Adjust ingest pipeline to handle missing-field cases.
- Halt if time-bearing data has missing or inconsistent timezone information. Time data cannot be trusted downstream.
- Halt if the primary key has any duplicates and the project has no dedup strategy.

---

## Example: ICS feed

Worked example for projects ingesting an ICS (iCalendar) feed. The generic process above applies; this section makes the steps concrete.

**Parser**: `node-ical` (Node.js), `ics.js`, `icalendar` (Python), or equivalent.

**Expected field set** (typical):
- `UID` — primary key
- `DTSTART`, `DTEND` — time bounds
- `SUMMARY` — title
- `DESCRIPTION` — body
- `LOCATION` — venue/address
- `URL` — canonical link

**Format anomalies to detect**:
- Smart quotes (`"` `"` `'` `'`) where straight quotes are expected
- Em-dashes and en-dashes in titles
- Truncated SUMMARY (some upstreams cap at 80 chars)
- Missing `TZID` on `DTSTART` / `DTEND` (a major source of time bugs)
- Inconsistent timezone usage across records
- Virtual-event flag patterns (e.g., `LOCATION` prefixed with "Virtual" or "Online")
- HTML or markdown leakage into plain-text fields
- Duplicate UIDs across records (some upstreams reuse UIDs for series)

**Domain-specific extraction patterns**:
- Timezone: assert `TZID` matches the project's expected timezone (e.g., `America/New_York`); flag any record missing TZID
- Neighborhood: split `LOCATION` on the first comma, normalize trailing whitespace
- Host org: regex `Hosted by (.+?)(?:\\.|$)` against `DESCRIPTION`
- Virtual flag: `LOCATION.startsWith("Virtual")` or contains explicit "Online"

**Stop conditions specific to ICS**:
- Halt if `TZID` is missing on any record and the project assumes a fixed timezone.
- Halt if duplicate UIDs are present and the project has no UID-collision strategy.

---

## Related
- `AUTONOMY_LAYER.md` section 1.13 (spec-reality reconciliation)
- `skills/diagnostics/api-surface-diagnostic` (analogous skill for internal APIs)
