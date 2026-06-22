---
title: "Anchor Mobile — Phase D Home Screen"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase D_ Home Screen.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase D Home Screen

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase D: Home Screen

Apply AUTONOMY_LAYER.md before executing. Phase C must be merged to main before Phase D starts.

Surfaces:          artifacts/mobile-app/app/home/ (extend)

artifacts/mobile-app/lib/api.ts (new)

artifacts/mobile-app/hooks/ (new)

Production impact: none (mobile reads from existing API)

Council of Models: no

Auto-merge:        no

Credentials:       gh

Agent:             CC Cloud (read-only API calls, no credentials needed)

Role

Implement the Home screen for the Anchor iOS app. Displays sobriety day count, active tracker durations, recent check-in summary, and primary CTAs to Check-In and Chat. Reads from the existing Anchor API on Fly. No new endpoints. No state mutations. This phase replaces the placeholder Home from Phase C.

Deployment Posture

Auto-merge: no — visual surface. No migrations. No API changes. No production write.

Design Data

API endpoints consumed (read-only)

All existing on Fly. Authenticated requests use Supabase session JWT in Authorization header.

GET /api/profile/stable

Returns: { sobriety_start_date, display_name, recovery_program, ... }

GET /api/trackers

Returns: { trackers: [{ id, label, started_at, is_primary }] }

GET /api/check-ins?limit=1

Returns: { check_ins: [{ id, created_at, mood, summary }] }

If the actual endpoint shapes differ, spec-reality reconciliation governs. Read the web app's existing API client (artifacts/recovery-checkin/src/lib/api.ts or equivalent) for ground truth.

File: artifacts/mobile-app/lib/api.ts

API client wrapping fetch with Supabase auth header injection.

Pattern:

- Reads supabase session via supabase.auth.getSession()

- If no session: throw AuthRequiredError (caller redirects to sign-in)

- Base URL from EXPO_PUBLIC_API_URL env var

- JSON parsing with error handling

- Logs every failure (no silent failures per AUTONOMY_LAYER section 1.10)

Add env var to .env.example:

EXPO_PUBLIC_API_URL=https://anchor-api-misty-river-3483.fly.dev

Hooks (custom React hooks)

hooks/useStableProfile.ts   — fetches /api/profile/stable, caches in memory

hooks/useTrackers.ts        — fetches /api/trackers

hooks/useRecentCheckIn.ts   — fetches /api/check-ins?limit=1

Each hook returns { data, loading, error, refetch }.

Use React Query (TanStack Query) if web app uses it. Otherwise plain useState + useEffect. Match the web pattern. Spec-reality governs.

Home screen layout

artifacts/mobile-app/app/home/index.tsx replaces the Phase C placeholder.

Layout top to bottom, inside Screen (scrollable=true):

NavBar

title: "Anchor"

rightAction: { label: "Settings", onPress: navigate to /settings }

(settings screen comes in Phase H — for now, log and navigate to a stub or to itself if no /settings route exists)

Day count Card

Large text: "{N} days"

Subtitle: "sober since {Month DD, YYYY}"

Calculated from stable_profile.sobriety_start_date

If no sobriety_start_date set: show "Welcome to Anchor" + a CTA "Set your start date" (links to onboarding — Phase H or later)

Trackers section (only if user has trackers)

Header: "Tracking"

List of Card rows, one per tracker

Each row: tracker.label (text-text) + duration ("X days") (text-subtle)

Recent check-in Card (only if a check-in exists)

Header: "Last check-in"

Body: check_in.summary or check_in.mood (whichever exists)

Timestamp: relative ("2 hours ago", "yesterday", etc.)

Primary CTAs (two Buttons stacked)

"Check in" (primary variant) → navigate to /check-in (Phase E)

"Open chat" (secondary variant) → navigate to /chat (Phase F)

Empty states

If user has no trackers: omit the section entirely (do not show "No trackers") If user has no check-ins: omit the section entirely If user has no sobriety_start_date: replace day count with onboarding CTA

Loading state

Show skeleton placeholders for each card while loading. Use Card with bg-muted/40 and fixed height. No spinners on the main surface.

Error state

If any API call fails: show a Banner (error variant) at the top of Screen: "We're having trouble loading your data. Pull down to retry."

Implement pull-to-refresh via ScrollView's refreshControl prop.

Date formatting

Use date-fns (already a web app dep). Install if not present:

pnpm add --filter @anchor/mobile-app date-fns

Functions:

formatDistance for relative times ("2 hours ago")

format(date, "MMMM d, yyyy") for sobriety start display

differenceInDays for day count math

Acceptance Criteria

AUTOMATED

artifacts/mobile-app/lib/api.ts exists with auth header injection

Three hooks exist at artifacts/mobile-app/hooks/

Home screen renders without crash given mocked data

Day count math is correct (unit test with fixed dates)

Empty states render correctly (no trackers, no check-ins, no sobriety date)

Error state renders Banner when hook returns error

TypeScript passes

expo export --platform ios passes

HUMAN_REVIEW

Visual layout on simulator (MANUAL_PLAYTEST_REQUIRED)

Pull-to-refresh feels right (MANUAL_PLAYTEST_REQUIRED)

Real data loads correctly against production API (MANUAL_PLAYTEST_REQUIRED)

Skeleton state does not flash visibly fast (MANUAL_PLAYTEST_REQUIRED)

Phase D Execution

PRE-FLIGHT

Standard. Confirm Phase C merged. Cut feat/mobile-phase-d-home.

Spec-reality reconciliation:

Read the web app's API client to confirm endpoint shapes and auth header format. Adopt repo reality. Log SPEC_REALITY_DELTA.

Confirm whether web uses TanStack Query or plain hooks.

Read the web Home screen to understand existing rendering logic before porting.

SMOKE ASSERTIONS

Write tests first:

Day count math (3 fixed-date scenarios)

Hook returns loading → data → error states

Home renders skeleton when loading

Home renders trackers section only when trackers present

Home renders check-in section only when check-in present

Home renders error Banner when API fails

IMPLEMENTATION

Create lib/api.ts with auth wrapper

Create three hooks

Build Home screen

Pull-to-refresh

Date utilities

COMMIT

feat(mobile): API client with Supabase auth header

feat(mobile): hooks for profile/trackers/check-ins

feat(mobile): Home screen with day count and CTAs

feat(mobile): empty and error states

test(mobile): Home screen unit tests

Directive-Specific Repair Entries

MOBILE-10 — API CORS or 401 on mobile but works on web A1: Verify Authorization header is being sent. Mobile and web should both use the same JWT. Check Supabase session.access_token is being read. A2: If API rejects mobile origin, check Fly app CORS config. Log to BLOCKERS_FOR_MARCUS.md if CORS changes needed. DEFER: HARD STOP if auth header fix doesn't resolve.

MOBILE-11 — API endpoint shape differs from spec A1: Spec-reality reconciliation. Read actual response. Adapt type and hook. Log SPEC_REALITY_DELTA. A2: Continue with adapted shape. DEFER: N/A — adapt and continue.

GO

Begin Phase D pre-flight. Cut branch: feat/mobile-phase-d-home. PR title: [Mobile] Phase D: Home screen No auto-merge.
