---
title: "DIRECTIVE V5"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/DIRECTIVE_ V5.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# DIRECTIVE V5

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
DIRECTIVE: V5.0 SOS Mode — safety screen, offline cache, header shortcut

Apply AUTONOMY_LAYER.md (Anchor edition v1.2, repo root) before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there.

Header

Surfaces:          artifacts/recovery-checkin/src/components/SosScreen.tsx (new)

artifacts/recovery-checkin/src/components/SosButton.tsx (new)

artifacts/recovery-checkin/src/lib/sosCache.ts (new)

artifacts/recovery-checkin/src/lib/sosLinks.ts (new — tel:/sms: helpers)

artifacts/recovery-checkin/src/pages/settings.tsx (extend)

artifacts/recovery-checkin/src/App.tsx or router (extend — route + header button)

artifacts/api-server (event_log sos_opened append)

Production impact: UI change (new SOS screen, header button, settings section, /sos route) + API change (sos_opened event)

Council of Models: no

Auto-merge:        no

Credentials:       gh, pnpm

Agent:             CC Cloud

Role

You are implementing V5.0 SOS Mode. This adds a persistent SOS shortcut in the app header, a dedicated SOS screen at /sos, an offline safety cache for dynamic user data, and a Settings → Safety section.

No AI inside this feature. No composeSystemPrompt call. No model call. No risk classifier. Static locked copy hardcoded in the bundle plus cached user contact/meeting data from localStorage only.

Zero V4 dependency. This directive does not require V4 Extend to be merged first.

You open one PR and stop.

Stack

See AUTONOMY_LAYER.md section 0.1.

Deployment posture

PR-only. Auto-merge: no. Marcus reviews and merges.

CD redeploys api-server on merge (sos_opened event). Vercel auto-deploys frontend on merge.

No migration required.

Design data

Architecture boundary — static vs cached

Static copy is hardcoded in the frontend bundle. Not stored in localStorage. Not fetched from the API. The following content lives in the component code:

Grounding text

Tell-on-myself section header and subtext

Prefilled SMS message text

Crisis card content (all five lines)

Empty state messages

Staleness banner template

localStorage stores only dynamic safety data:

interface SosCache {

sober_contacts: Array<{ name: string; phone: string }>;

meeting_links: Array<{ label: string; url: string }>;

cached_at: string; // ISO timestamp

}

Nothing else. No grounding text. No crisis card. No profile data beyond contacts and meeting links.

Cache refresh rules

On every successful stable_profile load, write the SOS cache — but conservatively:

Only overwrite the SOS cache after stable_profile is successfully parsed.

If the response is malformed or partial, do not overwrite an existing valid cache.

Empty arrays (sober_contacts: [], meeting_links: []) are valid and should be written only when the profile explicitly contains empty arrays — not when the field is missing or undefined.

A transient API shape issue must not erase a user's offline contact list.

SOS route

Add a route for the SOS screen using the existing app routing convention.

Preferred path: /sos — unless the existing app has an established route naming pattern that makes another path more appropriate (spec-reality reconciliation task).

The SOS button in the header navigates to this route. "Open SOS support" in Settings → Safety also navigates to this route.

SOS button placement

Persistent app-header action, top right. Visible on Home, Check-In, Chat, and Settings surfaces.

Label: SOS

Style: quiet text pill or small button. Not red by default. Not floating. Not competing with bottom nav.

Toggleable via Settings → Safety → "Show SOS shortcut" (default on)

If hidden via toggle: SOS button disappears from header, but Settings → Safety → "Open SOS support" still navigates to the SOS screen and is always visible regardless of toggle state

"Show SOS shortcut" preference storage: store in localStorage unless there is an existing app_settings preference pattern that is clearly already used for client UI preferences (confirm during spec-reality reconciliation). Do not add a database field or migration for this preference in V5. This is a purely client-side display preference.

SOS screen content — VERBATIM

No AI. No dynamic content. Static locked copy hardcoded in the bundle, plus cached user data.

Section 1 — Grounding text (top, first thing seen):

Put both feet on the floor. Take one breath. You only need to do the next honest thing.

Section 2 — Tell on myself:

Header: Tell on myself Subtext: Send a simple message before this gets bigger.

Show all contacts from the SOS cache (sober_contacts) as selectable contact rows.

Filter out contacts with no usable phone number before rendering

Each contact tap opens the native SMS composer addressed to that contact with this prefilled message (URL-encoded):

I'm in a risky moment and I don't want to keep it to myself. Can you check in with me?

Rules:

Do not assume a primary contact

Do not auto-select the first contact

The user chooses who to contact in the moment

If only one contact exists, show that one contact as a clear tap target — do not auto-fire the SMS

Empty state when no contacts: "Add a sober contact in your profile to use this." Link to the existing profile/memory/settings surface where sober contacts are edited. Do not invent a new profile editor.

Section 3 — Call or text a sober contact:

Show all contacts from the SOS cache as call and text action buttons (tel: and sms: links). No prefilled message for this section — direct dial/text only.

Filter out contacts with no usable phone number before rendering

Empty state when no contacts: same as Section 2.

Section 4 — Find a meeting:

Show all meeting links from the SOS cache as tappable rows (label + URL).

Filter out meeting links missing either label or URL before rendering

Empty state when no links: "Add meeting links in your profile." Link to the existing profile/memory/settings surface where meeting links are edited. Do not invent a new profile editor.

If offline: show cached links. Add note below the section: "Links shown from your saved list. You'll need a connection to open them."

Section 5 — Crisis and support lines card (hardcoded, verbatim):

Crisis and support lines

988 Suicide & Crisis Lifeline

Call, text, or chat 988 (US)

Available 24/7

SAMHSA National Helpline

1-800-662-HELP (4357)

Free, confidential, 24/7 treatment referral and support for mental health and substance use

Outside the US?

Search "crisis line [your country]" or contact local emergency services.

Staleness banner

If cached_at is more than 7 days old, show a small non-blocking note at the top of the SOS screen (below grounding text):

Last updated [formatted date]. Open Anchor online to refresh your safety info.

Do not block access when stale. The screen must work even with old cached data.

sosLinks.ts — helper functions

New file: artifacts/recovery-checkin/src/lib/sosLinks.ts

Build helpers for generating tel: and sms: URLs:

// Returns tel: URL for a phone number, or null if phone is unusable

export function telUrl(phone: string): string | null;

// Returns sms: URL with URL-encoded prefilled body, or null if phone is unusable

export function smsUrl(phone: string, body: string): string | null;

// Returns true if a contact has a usable phone number

export function hasUsablePhone(contact: { phone: string }): boolean;

// Returns true if a meeting link has both label and URL

export function hasUsableMeetingLink(link: { label: string; url: string }): boolean;

URL-encode the prefilled SMS body. Test with the actual prefilled message text (apostrophes, spaces need encoding).

event_log: sos_opened

Append sos_opened to event_log on every SOS screen route entry/open.

Log once per SOS screen route entry — not on ordinary re-renders or component updates

Match the existing event_log append pattern (spec-reality reconciliation task)

Payload:

{

kind: 'sos_opened',

timestamp: string, // ISO

}

Do not log: which contact was tapped, which meeting link was opened, contact names, phone numbers, or meeting URLs.

No AI inside SOS Mode — hard constraint

The agent must not add any of the following:

composeSystemPrompt call

OpenAI API call

Risk classifier call

Dynamic copy generation

Any model inference of any kind

If any implementation path appears to require AI, that is out of scope. Log as BLOCKER and surface in BLOCKERS_FOR_MARCUS.md.

Working files

Per AUTONOMY_LAYER.md section 0.4:

ISSUE_EXECUTION_PLAN.md — phases A through F with goals

docs/run-notes/session-2026-05-11-sos-mode.md — append-only log per section 1.12

BLOCKERS_FOR_MARCUS.md — only if a blocker surfaces

Phase plan

Each phase follows AUTONOMY_LAYER.md section 3: pre-flight → smoke-first → implement → health check → commit.

Phase A — sosCache.ts + sosLinks.ts

Goal: Cache read/write/clear/staleness logic works. tel: and sms: URL helpers work. Unit tested.

Spec-reality reconciliation (section 1.13):

Confirm existing localStorage usage patterns in the frontend

Confirm test runner for artifacts/recovery-checkin (likely Vitest — verify)

Locate where stable_profile is loaded to know where to wire the cache refresh

Smoke (write first, expect red):

Unit tests:

writeSosCache(data) writes correctly shaped object to localStorage

readSosCache() returns null when nothing cached

readSosCache() returns data when cache exists

isCacheStale(cachedAt) returns false for fresh cache (< 7 days)

isCacheStale(cachedAt) returns true for cache older than 7 days

clearSosCache() removes the cache

writeSosCache does not overwrite when passed undefined contacts (conservative rule)

telUrl returns correct tel: string for a valid phone

telUrl returns null for empty/unusable phone

smsUrl returns correctly URL-encoded sms: string with body

hasUsablePhone returns true/false correctly

hasUsableMeetingLink returns true/false correctly

Implementation:

Build sosCache.ts and sosLinks.ts per design data

Wire writeSosCache into the stable_profile load path with conservative overwrite rule

Acceptance (AUTOMATED): 12 unit tests pass, typecheck clean.

Commit:

feat(sos): sosCache + sosLinks helpers

localStorage cache for dynamic SOS data (contacts, meeting links,

cached_at). 7-day staleness detection. Conservative overwrite: does

not clear valid cache on malformed/partial profile response.

tel:/sms: URL helpers with encoding and usability filters.

Phase: A

Deferrals: 0

Tests: 12 unit tests pass

Phase B — SosScreen.tsx + /sos route

Goal: SOS screen renders with all five sections. Works offline. Staleness banner appears when stale. Route wired.

Spec-reality reconciliation:

Locate routing file and confirm route naming convention

Confirm component conventions (shadcn Card, spacing, mobile-first layout)

Locate existing event_log append pattern and match it exactly

Smoke (write first, expect red):

Playwright e2e:

Navigating to /sos renders all five sections

Grounding text is the first visible content

Tell-on-myself shows cached contacts; tapping one opens sms: link with correct URL-encoded prefilled message

Crisis card shows verbatim content (988, SAMHSA, outside US)

Empty state renders correctly when no contacts cached

Staleness banner appears when cache is older than 7 days (seed a stale cache in test setup)

sos_opened event is logged on route entry (verify via intercepted API call or event_log read)

Implementation:

Build SosScreen.tsx with the five sections in locked order

Use readSosCache() for contacts and meeting links

Use sosLinks.ts helpers for all tel: and sms: URLs

Filter contacts via hasUsablePhone, filter meeting links via hasUsableMeetingLink

Show staleness banner if isCacheStale() returns true

Log sos_opened once on route entry — not on re-renders

Wire the route using existing routing convention

Static content hardcoded — do not read grounding text or crisis card from localStorage

Acceptance (AUTOMATED): 7 e2e specs pass, typecheck clean.

HUMAN_REVIEW (MANUAL_PLAYTEST_REQUIRED):

Screen feels calm, not alarming

Grounding text is the first thing visible

Layout works on mobile

Tell-on-myself SMS draft is correct on a real device

Commit:

feat(sos): SOS screen at /sos

Five sections in order: grounding text, tell on myself, call/text

contact, find a meeting, crisis card. Static copy hardcoded. Dynamic

data from sosCache. Staleness banner after 7 days. sos_opened logged

on route entry. No AI.

Phase: B

Deferrals: 0

Tests: 7 e2e specs pass

Phase C — SosButton.tsx in app header

Goal: SOS button appears in the app header top right on all major surfaces. Navigates to /sos. Toggleable via Settings preference stored in localStorage.

Spec-reality reconciliation:

Locate app header/chrome component

Confirm how per-surface header actions are added

Confirm if any existing app_settings preference pattern is used for client UI preferences — if yes, match it; if no existing pattern, use localStorage

Smoke (write first, expect red):

Playwright e2e:

SOS button visible in header on Home, Check-In, Chat, Settings by default

Tapping SOS button navigates to /sos

SOS button hidden when "Show SOS shortcut" preference is off

Button reappears when preference is turned back on

Implementation:

Build SosButton.tsx

Wire into app header/chrome

Read "Show SOS shortcut" preference from localStorage (or existing app_settings pattern if found during reconciliation)

Acceptance (AUTOMATED): 4 e2e specs pass, typecheck clean.

Commit:

feat(sos): SOS header button — persistent top-right shortcut

Quiet text pill "SOS" top right. Navigates to /sos. Visible on all

major surfaces. Toggleable via Settings → Safety. Preference stored

in localStorage. Default on.

Phase: C

Deferrals: 0

Tests: 4 e2e specs pass

Phase D — Settings → Safety section

Goal: Safety section added to settings page with three items. All copy verbatim.

Spec-reality reconciliation:

Locate existing settings sections and match conventions

Smoke (write first, expect red):

Playwright e2e:

Settings page shows Safety section with all three items

"Open SOS support" navigates to /sos

"Show SOS shortcut" toggle updates localStorage preference and hides/shows header button

"Clear safety cache" shows confirmation modal with verbatim copy

Confirming clears localStorage cache; cancelling does not

Implementation:

Settings → Safety section verbatim:

Safety

Open SOS support

[direct link — navigates to /sos, always visible]

Show SOS shortcut

[toggle, default on]

Helper: Show a small SOS button in the app header.

Clear safety cache

[destructive, requires confirmation]

Helper: Removes cached sober contacts and meeting links from this device. SOS can refresh them next time you open Anchor online.

Confirmation modal verbatim:

Clear safety cache?

This removes cached sober contacts and meeting links from this device. Your profile is not deleted. SOS will refresh this information next time you open Anchor online.

[Cancel]  [Clear cache]

Acceptance (AUTOMATED): 5 e2e specs pass, typecheck clean.

HUMAN_REVIEW (MANUAL_PLAYTEST_REQUIRED): section feels proportionate, not over-engineered.

Commit:

feat(settings): Safety section — SOS access, shortcut toggle, cache clear

Three items: Open SOS support (always visible), Show SOS shortcut

toggle (localStorage, default on), Clear safety cache (destructive

with verbatim confirmation modal).

Phase: D

Deferrals: 0

Tests: 5 e2e specs pass

Phase E — Health check sweep

All api-server unit tests pass

All recovery-checkin unit tests pass

All new Playwright e2e specs pass

Typecheck clean across affected workspaces

Build green

Phase F — BUILD_REPORT + PR

Generate BUILD_REPORT.md per AUTONOMY_LAYER.md section 5.

Commit working files + BUILD_REPORT.

Push branch. Direct git push preferred. MCP fallback with section 1.12 preflight if 403.

Open PR:

gh pr create \

--title "feat(sos): V5.0 SOS Mode — safety screen, offline cache, header shortcut" \

--body "$(cat BUILD_REPORT.md)"

Do NOT register auto-merge.

Log PR URL in run notes. Stop.

Directive-specific repair entries

SOS-1 — sms: link does not open native SMS on test runner A1: Playwright intercepts tel:/sms: links differently than a real device. If e2e can't verify the SMS opens, assert the correct href attribute instead of actually tapping. A2: Mark the SMS-open assertion as MANUAL_PLAYTEST_REQUIRED and skip in e2e. DEFER: Log as MEDIUM. Static href correctness is verifiable; real-device behavior is MANUAL_PLAYTEST.

SOS-2 — localStorage unavailable (private browsing, storage quota) A1: Wrap all localStorage calls in try/catch. Return null on read failure; silently skip on write failure. A2: Record a local diagnostic only if an existing client diagnostic pattern exists; otherwise note it in run notes. Do not add a new analytics/event_log event. Show the SOS screen without cached data — static content always renders. DEFER: SOS screen must never crash. Graceful degradation is required.

SOS-3 — Route path /sos conflicts with existing route A1: Check existing routes. If /sos is taken, use /safety or /sos-support. A2: Match whatever naming pattern is established for utility/safety routes. DEFER: Log SPEC_REALITY_DELTA and proceed with the next available clean path.

SOS-4 — sos_opened fires on re-renders (React Strict Mode double-invoke) A1: Use a ref to track whether the event has been logged in the current mount cycle. A2: Debounce the event log call with a short window (100ms). DEFER: Log as MEDIUM if both attempts produce noisy duplicate events. Document the known Strict Mode behavior.

Deferred-issues format

See AUTONOMY_LAYER.md section 4.

BUILD_REPORT format

See AUTONOMY_LAYER.md section 5.

Hard stops

See AUTONOMY_LAYER.md section 6.

GO

Run credentials preflight per AUTONOMY_LAYER.md section 0.5.

Cut branch from main:

git checkout main

git pull origin main

git checkout -b feat/v5-sos-mode

Create ISSUE_EXECUTION_PLAN.md and docs/run-notes/session-2026-05-11-sos-mode.md. Log session start, main SHA, phases A through F.

Execute Phase A. Run spec-reality reconciliation per section 1.13. Continue A → B → C → D → E → F without stopping.

End of directive.
