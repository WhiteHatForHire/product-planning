---
title: "VNext Phase 2 — Time of Day Routing Implementation Plan"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/VNext Phase 2 — Time-of-Day Routing_ Implementation Plan.docx"
status: archive
privacy: private/internal
tags:
  - product
  - archive
---

# VNext Phase 2 — Time of Day Routing Implementation Plan

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
VNext Phase 2 — Time-of-Day Routing: Implementation Plan

Goal

Replace the user-chosen quick | full toggle in checkin.tsx with server-determined routing into the four-value enum (morning | midday | evening | manual) based on the user's local time. Fix the timezone bug in GET /api/checkin/today so "today" means the user's today, not the API server's.

Premise from Phase 1

Phase 1 migrations (branch feat/vnext-phase1-schema, commit f19341b) leave the DB additive. The check_in_type column accepts any string. Phase 2 must ship and be verified in production before migration 0004 is applied. Until 0004 lands, the backfill UPDATEs in 0001 must be re-run on the day of cutover. This is documented in lib/db/migrations/manual/README.md.

Files to touch

File

Change

artifacts/api-server/src/utils/v3helpers.ts

Extend getLocalDate to return { date, hour }; add getCheckInWindow(timezone)

artifacts/api-server/src/utils/emailScheduler.ts

Export the existing resolveTimezone so other modules can reuse it

artifacts/api-server/src/routes/checkin.ts

New GET /api/checkin/window; fix GET /api/checkin/today timezone bug; overwrite client-supplied checkInType with server-computed window

artifacts/recovery-checkin/src/pages/checkin.tsx

Remove quick/full toggle; call /api/checkin/window on mount; pass user timezone in headers

artifacts/recovery-checkin/src/pages/checkin-backfill.tsx

Always send checkInType: "manual"; no window selector

artifacts/recovery-checkin/src/pages/checkin-edit.tsx

Update enum on edit form schema

No new files. All work fits into existing modules.

Functions to write or extend

1. Extend getLocalDate() in v3helpers.ts

Current signature returns a string. Change to return date, hour, and weekday from a single epoch read to avoid drift between two new Date() invocations.

New function: getLocalParts(timezone: string): { date: string; hour: number; weekday: number }

Use Intl.DateTimeFormat with formatToParts(). Keep existing getLocalDate as a thin wrapper (getLocalDate(tz) => getLocalParts(tz).date) to protect all existing callers. Same try/catch fallback to America/New_York.

2. Add getCheckInWindow() in v3helpers.ts

New export: getCheckInWindow(timezone: string): "morning" | "midday" | "evening"

Call getLocalParts(timezone) and switch on hour:

5 <= hour < 11 returns morning

11 <= hour < 16 returns midday

hour >= 16 or hour < 5 returns evening

The before-5am arm is deliberate. Someone checking in at 2am is closing out yesterday, not opening today. "manual" is never returned by this function. It is reserved for backfills and edits where the server does not infer a time window.

3. Promote resolveTimezone() to a shared util

Currently file-private in emailScheduler.ts. Preferred path: move to v3helpers.ts next to the new time helpers, re-import from emailScheduler.ts. Alternatively, export in place and import from routes/checkin.ts. Either way, no third copy of the validator.

4. New endpoint: GET /api/checkin/window

Response shape: { window: "morning" | "midday" | "evening", localDate: string, localHour: number, timezone: string }

Auth via requireAuth. Read timezone from loadUserMemory(userId).stableProfile.timezone. Fall back to America/New_York. Pass through resolveTimezone() so an invalid stored value cannot crash the route. Return resolved values so the frontend can display "Evening check-in" without re-deriving on the client.

5. Modify POST /api/checkin

Ignore any checkInType sent by the client (defense in depth). For normal check-ins, compute checkInType = getCheckInWindow(timezone) server-side. For backfills where backfillDate is present, force checkInType = "manual" regardless of hour. Backfills do not represent a real moment in time. Also persist timezone into the new check_ins.timezone column added by migration 0001.

6. Fix GET /api/checkin/today timezone bug

Current code uses new Date(); setHours(0,0,0,0) which is server-local midnight. Replace with: load user timezone, compute DateTime.now().setZone(tz).startOf("day") via Luxon (already imported in emailScheduler.ts, no new dependency), convert to JS Date for the comparison. hasCheckedInToday now means "since the user's local midnight."

Frontend changes

checkin.tsx

Update form schema from z.enum(["quick", "full"]) to z.enum(["morning", "midday", "evening", "manual"]). Remove the manual type toggle buttons and the type UI state they drive. Replace with a read-only badge showing the window returned from /api/checkin/window (example: "Evening check-in"). Fetch /api/checkin/window on mount. Disable the submit button while loading. Pass timezone in a request header (X-User-Timezone: Intl.DateTimeFormat().resolvedOptions().timeZone) as a fallback for new users whose profile timezone is not yet set. Server treats stored profile as authoritative when present.

checkin-backfill.tsx

Always send checkInType: "manual". No window selector in the backfill UI.

checkin-edit.tsx

Update enum on the edit form schema. Editing an existing row preserves whatever check_in_type is already on disk. The user is not re-routed to a different window mid-edit.

Order of operations

Step 1 — Backend utility layer, no behavior change yet. Land getLocalParts, getCheckInWindow, exported resolveTimezone, and the new GET /api/checkin/window endpoint. Old POST /checkin still accepts quick/full. Deploy to Fly.

Step 2 — Fix GET /api/checkin/today timezone bug. Can ship in the same PR as step 1 or as a follow-up. Independent of the routing change and unblocks correctness on its own. Deploy.

Step 3 — Frontend cutover. Ship checkin.tsx, checkin-backfill.tsx, and checkin-edit.tsx updates. Deploy to Vercel.

Step 4 — Server-side enforcement. Modify POST /checkin to overwrite checkInType server-side. Deploy. After this point, no new quick/full rows can be written.

Step 5 — Verify in production. Run: SELECT array_agg(DISTINCT check_in_type) FROM check_ins;. Should return only the four new values. If quick or full still appears, old rows exist from the step 3-4 gap. Re-run the 0001 backfill UPDATEs.

Step 6 — Apply migration 0004. Adds the CHECK constraint. Pre-flight query in the migration header documents this verification step.

Steps 1 and 2 are safe to ship together. Steps 3 and 4 must be ordered — frontend before stricter backend, so users are not briefly broken. Step 6 is gated on step 5 passing.

Out of scope for Phase 2

domain_scores and detected_deltas columns added by migration 0001 are populated in Phase 5 (delta intelligence). The daily_summary aggregator table is populated by a scheduled job, not by check-in writes. Drizzle TS schema sync happens after 0004 lands in its own change, as documented in lib/db/migrations/manual/README.md.

Known decision debt

The morning/midday/evening window boundaries (5am/11am/4pm) are defaults, not hardened values. Real user data should inform whether these windows match actual check-in behavior before they are locked. Phase 2 ships the defaults. Adjustment is a post-VNext concern.

The composite score weighting (morning 25%, midday 25%, evening 50%) is a hypothesis. Do not harden it until at least 30 days of multi-check-in data exists.
