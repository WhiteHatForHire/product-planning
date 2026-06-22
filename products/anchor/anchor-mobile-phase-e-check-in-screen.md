---
title: "Anchor Mobile — Phase E Check In Screen"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase E_ Check-In Screen.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase E Check In Screen

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase E: Check-In Screen

Apply AUTONOMY_LAYER.md before executing. Phase D must be merged to main before Phase E starts.

Surfaces:          artifacts/mobile-app/app/check-in/ (new)

artifacts/mobile-app/lib/api.ts (extend with check-in submit)

Production impact: none (mobile writes via existing API)

Council of Models: no (no new prompt fragments — backend handles)

Auto-merge:        no

Credentials:       gh

Agent:             CC Local (needs to test against real API)

Role

Port the Anchor web check-in flow to iOS. Form submission goes to the existing API endpoint. Result rendering (including crisis routing) uses the existing backend response shape — no new safety logic on the mobile side. Crisis routing UI uses the CrisisCard pattern from the web app, ported to RN components. No new copy. No new prompt fragments. Mobile is a UI layer over the existing backend's safety surface.

Deployment Posture

Auto-merge: no — touches a safety-adjacent surface (crisis routing render). Council of Models: no — backend safety logic is unchanged. Mobile renders backend output. If backend returns crisis=true, mobile shows CrisisCard.

Design Data

API endpoints consumed

POST /api/check-in

Body: { mood, energy, urge, notes, ... }

Returns: {

check_in: { id, ... },

ai_response: { summary, commitments? },

crisis: boolean,

crisis_response?: { headline, body, resources: [{ label, action: "tel" | "url", value }] }

}

If actual response shape differs: spec-reality reconciliation. Read the web check-in handler for ground truth before implementing the mobile render.

Form fields

Read the web check-in form to determine the exact field set. Likely:

Mood (CheckInOption group: "Steady", "Shaky", "Rough")

Energy (numeric scale 1–5 via segmented control or CheckInOption row)

Urge level (numeric scale 1–5)

Optional notes (TextField, multiline)

Match the web form exactly. Do not add or remove fields.

Layout

artifacts/mobile-app/app/check-in/index.tsx

Inside Screen (scrollable=true):

NavBar

title: "Check in"

leftAction: { label: "Cancel", onPress: router.back() }

Form sections (one Card per field group)

Section header (text-text font-medium mb-3)

Field(s) using CheckInOption, TextField, or custom segmented control

Submit Button (primary, full-width, sticky to bottom or below form)

Label: "Submit check-in"

Disabled until required fields filled

Loading state during submission

Result screen

artifacts/mobile-app/app/check-in/result.tsx

After successful submission, navigate here with the response as params or via context.

Two render paths based on response.crisis:

Normal result (crisis === false)

Inside Screen:

NavBar

title: "Check-in saved"

rightAction: { label: "Done", onPress: navigate to /home }

Summary Card

body: ai_response.summary

Commitments section (only if ai_response.commitments present)

Header: "Want to commit to one?"

List of CheckInOption-style pills, one per commitment

Tap saves the commitment (POST /api/commitments — verify endpoint in spec-reality pass)

After tap: pill shows "Saved" state, others disable

CTA Button: "Back to home" → /home

Crisis result (crisis === true)

Inside Screen:

NavBar

title: "We're here"

No rightAction — do not let user dismiss easily

SOSCard at the top

title: crisis_response.headline

subtitle: crisis_response.body

actionLabel: first resource's label (typically "Call 988")

onAction: tap-to-call or open URL based on resource.action

Additional resource Cards (one per remaining resource)

Each tappable, opens tel: or https: URL

Footer Button (secondary): "Back to home"

Commitment save endpoint

If commitments tap is implemented, verify endpoint. Likely:

POST /api/commitments

Body: { check_in_id, commitment_text }

If not implemented in backend yet: log to BLOCKERS_FOR_MARCUS.md and skip commitment save in V1 mobile. Show commitments as info only.

Crisis UX rules (carried from web)

Do not show chat input on the crisis result

Do not auto-dismiss

Resources must be prominent

988 (Suicide & Crisis Lifeline) and SAMHSA (1-800-662-4357) should appear if backend returns them — render whatever backend sends, do not hardcode

Acceptance Criteria

AUTOMATED

Form renders all fields from spec-reality

Submit disabled until required fields valid

Loading state during submit

Normal result renders summary

Crisis result renders SOSCard with backend-provided copy

Crisis result does not render commitments

Tests use mocked API responses for both branches

TypeScript passes

expo export passes

HUMAN_REVIEW

Form ergonomics on device (MANUAL_PLAYTEST_REQUIRED)

Crisis routing renders correctly with real veiled-language scenario (MANUAL_PLAYTEST_REQUIRED)

Commitment save UX (MANUAL_PLAYTEST_REQUIRED)

Real check-in submission against staging/prod API (MANUAL_PLAYTEST_REQUIRED)

Phase E Execution

PRE-FLIGHT

Standard. Confirm Phase D merged. Cut feat/mobile-phase-e-checkin.

Spec-reality reconciliation:

Read web check-in form to enumerate exact fields

Read web check-in API handler for response shape

Read web CrisisCard / crisis_response handling

Read web commitment save endpoint if present

SMOKE ASSERTIONS

Form validation logic

Mocked API response → normal render

Mocked API response → crisis render with SOSCard

Submit button enables/disables correctly

Crisis branch never shows commitments

IMPLEMENTATION

Form screen

Submit handler

Result screen with branching

Commitment save (if endpoint exists)

Telephone/URL action handlers

COMMIT

Atomic. Form, submit, result-normal, result-crisis, commitment save.

Directive-Specific Repair Entries

MOBILE-12 — Crisis branch renders user input field A1: Hard check: if response.crisis === true, do not render any input or chat-style affordance on result screen. Add explicit assertion in render logic. A2: Strip input rendering entirely from crisis branch. DEFER: HARD STOP — this is a safety boundary.

MOBILE-13 — Telephone action fails on simulator A1: Linking.openURL("tel:988") does not work on iOS simulator (expected). Test on physical device. A2: Add fallback message if Linking.canOpenURL returns false: "Dial 988 from your phone". DEFER: MANUAL_PLAYTEST_REQUIRED on device.

GO

Begin Phase E pre-flight. Cut branch: feat/mobile-phase-e-checkin. PR title: [Mobile] Phase E: Check-in form + result + crisis routing No auto-merge.
