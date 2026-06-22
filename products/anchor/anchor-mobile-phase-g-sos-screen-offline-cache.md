---
title: "Anchor Mobile — Phase G SOS Screen + Offline Cache"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase G_ SOS Screen + Offline Cache.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase G SOS Screen + Offline Cache

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase G: SOS Screen + Offline Cache

Apply AUTONOMY_LAYER.md before executing. Phase F must be merged to main before Phase G starts.

Surfaces:          artifacts/mobile-app/app/sos/ (new)

artifacts/mobile-app/lib/sos-cache.ts (new)

artifacts/mobile-app/lib/api.ts (extend with SOS fetch)

Production impact: none

Council of Models: no (no new copy — uses existing SOS content from backend)

Auto-merge:        no

Credentials:       gh

Agent:             CC Local (airplane-mode device testing)

Role

Port the Anchor SOS surface to iOS with offline-first caching. SOS is the "break glass" screen — must work without network. AsyncStorage caches the display content fetched from backend. On screen open: render from cache immediately, then refresh from network in the background. If offline: serve cache.

Deployment Posture

Auto-merge: no — safety surface. Cached content is non-sensitive display data (contact names, meeting URLs, grounding text). Uses AsyncStorage, NOT expo-secure-store (per Expo spec).

Design Data

Cache schema (AsyncStorage)

Single key: anchor:sos:cache

Value (JSON):

{

sober_contact: {

name: string,

phone: string   // E.164 preferred

} | null,

meeting: {

label: string,

url: string

} | null,

grounding_text: string,

tell_on_myself_message: string,

crisis_card: {

headline: string,

body: string,

resources: [{ label: string, action: "tel" | "url", value: string }]

},

cached_at: string   // ISO timestamp

}

API endpoint

GET /api/sos/content

Returns: { sober_contact, meeting, grounding_text, tell_on_myself_message, crisis_card }

Authenticated.

Confirm shape via spec-reality. Read web SOS implementation.

File: artifacts/mobile-app/lib/sos-cache.ts

import AsyncStorage from "@react-native-async-storage/async-storage";

const KEY = "anchor:sos:cache";

export type SOSContent = { ... };  // type matching schema above

export async function getCachedSOS(): Promise<SOSContent | null> {

try {

const raw = await AsyncStorage.getItem(KEY);

if (!raw) return null;

return JSON.parse(raw);

} catch (err) {

console.warn("[sos-cache] read failed:", err);

return null;

}

}

export async function setCachedSOS(content: SOSContent): Promise<void> {

try {

const withTimestamp = { ...content, cached_at: new Date().toISOString() };

await AsyncStorage.setItem(KEY, JSON.stringify(withTimestamp));

} catch (err) {

console.warn("[sos-cache] write failed:", err);

}

}

Install AsyncStorage:

npx expo install @react-native-async-storage/async-storage

Layout

artifacts/mobile-app/app/sos/index.tsx

Inside Screen (scrollable=true):

NavBar

title: "SOS"

leftAction: { label: "Close", onPress: router.back() }

Sober contact Card (only if sober_contact present)

Header: "Call someone"

Name (text-text font-medium)

Tap row → Linking.openURL("tel:" + phone)

Show phone number in subtle text

Meeting Card (only if meeting present)

Header: "Find a meeting"

Meeting label

Tap row → Linking.openURL(meeting.url)

Crisis Card (always visible — at the top or bottom, designer call)

Use SOSCard component

title: crisis_card.headline

subtitle: crisis_card.body

actionLabel: first resource label

onAction: tel/url based on first resource

Additional resource Cards (one per crisis_card.resources after the first)

Tappable, tel/url action

Grounding text Card

Header: "Ground yourself"

Body: grounding_text

Tell-on-myself Card

Header: "Tell on yourself"

Body: tell_on_myself_message

Tap row → opens chat with this message pre-filled (Phase F integration)

If Phase F integration not feasible from SOS context: copy to clipboard instead with toast "Copied — paste into chat"

Footer: "Last updated {relative time}" (text-subtle text-xs)

Loading logic

On mount:

Read cache → render immediately if present

Fire network request in background

On success: update cache + state

On failure: keep showing cached version, no error banner unless cache is also empty

Empty cache + no network

If cache is empty AND network fails:

Show static fallback content:

Title: "Hard moment?"

Body:  "You're not alone."

Resources:

- "Call 988" (Suicide & Crisis Lifeline)

- "Call SAMHSA: 1-800-662-4357"

These are public-domain emergency resources and are acceptable to hardcode as a last-resort fallback. Document this in a code comment.

Tap-to-call

Use Linking.openURL("tel:" + phone). On simulator, this will fail — that is expected per MOBILE-13.

Acceptance Criteria

AUTOMATED

sos-cache.ts read/write/null-handling unit tests

SOS screen renders from mocked cache

SOS screen renders network response on success

SOS screen falls back to cache when network fails

SOS screen shows static fallback when both cache and network empty

Crisis card always visible

Typescript passes

expo export passes

HUMAN_REVIEW

Airplane-mode test: open SOS offline, cached content renders (MANUAL_PLAYTEST_REQUIRED)

Tap-to-call works on physical device (MANUAL_PLAYTEST_REQUIRED)

Open meeting URL opens browser (MANUAL_PLAYTEST_REQUIRED)

Tell-on-myself integration with chat (MANUAL_PLAYTEST_REQUIRED)

Phase G Execution

PRE-FLIGHT

Standard. Confirm Phase F merged. Cut feat/mobile-phase-g-sos.

Spec-reality reconciliation:

Read web /api/sos/content handler

Read web SOS UI for layout reference

Confirm tell-on-myself flow on web (does it pre-fill chat?)

SMOKE ASSERTIONS

Cache read returns null on first load

Cache write then read returns same data

SOS renders all sections from mocked content

SOS falls back to cache when fetch rejects

Static fallback renders when cache empty + fetch rejects

IMPLEMENTATION

AsyncStorage install

sos-cache.ts module

SOS screen with caching logic

Tap-to-call wiring

Tell-on-myself integration

Static fallback

COMMIT

Atomic per concern.

Directive-Specific Repair Entries

MOBILE-16 — AsyncStorage write succeeds but read returns null A1: Verify the same KEY constant is used for both. Check for race condition on cold launch (read before write completes). A2: Add explicit await on first read after mount. DEFER: Log MEDIUM. Cache will rebuild on next fetch.

MOBILE-17 — tell-on-myself chat integration not possible A1: Phase F (chat) may not expose a way to pre-fill input from external context. If so, fall back to clipboard copy + toast. A2: Document as deferred. Phase F revisit can add this integration later. DEFER: LOW. Clipboard fallback is acceptable for V1.

GO

Begin Phase G pre-flight. Cut branch: feat/mobile-phase-g-sos. PR title: [Mobile] Phase G: SOS screen with offline cache No auto-merge.
