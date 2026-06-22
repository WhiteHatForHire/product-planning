---
title: "Anchor Mobile — Phase H Minimal Settings"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase H_ Minimal Settings.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase H Minimal Settings

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase H: Minimal Settings

Apply AUTONOMY_LAYER.md before executing. Phase G must be merged to main before Phase H starts.

Surfaces:          artifacts/mobile-app/app/settings/ (new)

Production impact: none

Council of Models: no

Auto-merge:        no

Credentials:       gh

Agent:             CC Cloud

Role

Minimal Settings screen for V1. Logout, notification preference (time picker), account deletion path, privacy/terms links. No theme picker, no profile editing, no advanced customization — those defer to V2.

Deployment Posture

Auto-merge: no — touches auth (sign-out) and account deletion path.

Design Data

Settings items (in order)

Notifications section

Header: "Reminders"

Toggle: "Daily check-in reminder" (on/off)

Time picker: "Reminder time" (only visible if toggle on)

Default: on, 9:00 AM local time

Persists to backend via PATCH /api/profile/stable (or equivalent)

Account section

Header: "Account"

Row: "Email" (read-only, shows current user email)

Row: "Delete account" → opens deletion instructions screen

Legal section

Header: "Legal"

Row: "Privacy policy" → Linking.openURL("https://sobrietyanchor.com/privacy")

Row: "Terms" → Linking.openURL("https://sobrietyanchor.com/terms")

Sign-out

Button (secondary, full-width)

Label: "Sign out"

Tap: confirm via Alert.alert

Title: "Sign out?"

Body: "You'll need to sign in again to use Anchor."

Cancel + Confirm

On confirm: supabase.auth.signOut() + navigate to /auth/sign-in

Version footer (text-subtle text-xs, centered, py-6)

"Anchor 1.0.0" (read from app.json or Constants.expoConfig.version)

Time picker

Use @react-native-community/datetimepicker. Install:

npx expo install @react-native-community/datetimepicker

iOS picker is a wheel. Store as 24-hour HH:mm string in stable_profile or app_settings (read web app for the exact field name and format).

Account deletion screen

artifacts/mobile-app/app/settings/delete-account.tsx

Layout:

NavBar

title: "Delete account"

leftAction: { label: "Back" }

Body Card

Header: "Permanently delete your account"

Body: "This will remove your check-ins, chats, trackers, and profile. You won't be able to recover this data."

Instructions Card

"To delete your account, email support@sobrietyanchor.com from the email associated with your Anchor account. We'll process the request within 30 days."

Button: "Email support" (opens mail: link)

Linking.openURL("mailto:support@sobrietyanchor.com?subject=Delete%20my%20Anchor%20account")

No in-app delete button in V1. Apple guidelines require an in-app deletion path for new submissions — the email-to-support pattern qualifies as long as it's explicit and accessible. Phase J should verify against Apple's current submission requirements.

Layout: artifacts/mobile-app/app/settings/index.tsx

Inside Screen (scrollable=true):

NavBar

title: "Settings"

leftAction: { label: "Done", onPress: router.back() }

Sections rendered as Cards with section headers above

Acceptance Criteria

AUTOMATED

Settings renders all sections

Notification toggle persists (mocked API)

Time picker shows when toggle on

Sign-out triggers confirmation then calls supabase.auth.signOut()

Delete account screen renders mail link

Typescript passes

expo export passes

HUMAN_REVIEW

Time picker UX (MANUAL_PLAYTEST_REQUIRED)

Sign-out fully clears session (MANUAL_PLAYTEST_REQUIRED)

Mail link opens Mail app with prefilled subject (MANUAL_PLAYTEST_REQUIRED)

Privacy/terms links work (MANUAL_PLAYTEST_REQUIRED, must exist on sobrietyanchor.com — see BLOCKERS)

Pre-requisite — Marcus action

Before Phase H ships:

[ ] sobrietyanchor.com/privacy is live

[ ] sobrietyanchor.com/terms is live

[ ] support@sobrietyanchor.com email forwards correctly

If any of these are not done: log to BLOCKERS_FOR_MARCUS.md. Phase H can still ship but App Store submission (Phase J) will be blocked.

Phase H Execution

PRE-FLIGHT

Standard. Confirm Phase G merged. Cut feat/mobile-phase-h-settings.

SMOKE ASSERTIONS

Settings renders sections

Toggle state changes

Sign-out confirmation flow

Delete account screen renders

IMPLEMENTATION

Settings index screen

Time picker integration

Notification preference persistence

Sign-out flow

Delete account screen

Legal links

COMMIT

Atomic per concern.

GO

Begin Phase H pre-flight. Cut branch: feat/mobile-phase-h-settings. PR title: [Mobile] Phase H: Minimal Settings No auto-merge.
