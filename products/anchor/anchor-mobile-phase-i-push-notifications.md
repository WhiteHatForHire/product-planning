---
title: "Anchor Mobile — Phase I Push Notifications"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase I_ Push Notifications.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase I Push Notifications

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase I: Push Notifications

Apply AUTONOMY_LAYER.md before executing. Phase H must be merged to main before Phase I starts.

Surfaces:          artifacts/mobile-app/lib/notifications.ts (new)

artifacts/mobile-app/app/_layout.tsx (permission prompt)

artifacts/mobile-app/app/settings/ (wire to scheduler)

Production impact: none (local notifications only in V1, no backend push)

Council of Models: no

Auto-merge:        no

Credentials:       gh

Agent:             CC Local (notification testing requires device)

Role

Implement local daily check-in reminder notifications. No backend push service in V1. Notifications are scheduled locally via expo-notifications on the user's device. One notification type. User-configurable time. Non-alarmist content. Respects notification permission.

Deployment Posture

Auto-merge: no. No backend changes. No EAS secrets beyond existing.

Design Data

Spec rules (carried from Expo spec)

Daily check-in reminder ONLY in V1

No crisis prompts via push

No "you seem at risk" alerts

No milestone alerts

No commitment follow-ups

Notification content is consistent and non-shaming

Permission prompted once after first successful auth, before first Home load

If declined, respect it. Provide re-enable path in Settings.

Dependencies

npx expo install expo-notifications expo-device

Notification content (verbatim)

Title: "Anchor"

Body:  "Time for your daily check-in."

No data payload that could expose sensitive content on lock screen.

Default schedule

Time: 9:00 AM local time

Frequency: daily

User can change time in Settings

File: artifacts/mobile-app/lib/notifications.ts

Exports:

requestPermission(): Promise<boolean>

- Calls Notifications.requestPermissionsAsync()

- Returns whether granted

scheduleDailyCheckIn(hour: number, minute: number): Promise<void>

- Cancels existing daily check-in notification

- Schedules new one with Notifications.scheduleNotificationAsync

using trigger { hour, minute, repeats: true }

- Content: { title: "Anchor", body: "Time for your daily check-in." }

- Identifier: "daily-check-in"

cancelDailyCheckIn(): Promise<void>

- Notifications.cancelScheduledNotificationAsync("daily-check-in")

getPermissionStatus(): Promise<"granted" | "denied" | "undetermined">

Permission prompt timing

In app/_layout.tsx after auth succeeds and before navigating to /home:

Check permission status

If undetermined: prompt

If granted: schedule default 9:00 AM reminder

If denied: skip silently, do not nag

Use AsyncStorage to track "has-prompted-notifications-once" so re-prompt only happens via Settings.

Settings integration

When user toggles "Daily check-in reminder" in Settings (from Phase H):

ON: check permission; if denied, deep-link to iOS Settings via Linking.openURL("app-settings:"); if granted, scheduleDailyCheckIn

OFF: cancelDailyCheckIn

When user changes time:

Re-schedule with new hour/minute

Notification handler

When user taps the notification, app should open and navigate to /check-in.

Handle via Notifications.addNotificationResponseReceivedListener in _layout.tsx.

iOS-specific config in app.json

Add to existing app.json (preserve Phase A content):

"plugins": [

[

"expo-notifications",

{

"icon": "./assets/notification-icon.png",

"color": "#6366f1"

}

]

]

Notification icon at ./assets/notification-icon.png — if missing, generate a placeholder or use the app icon. Log to BLOCKERS_FOR_MARCUS.md if Marcus wants a custom icon.

Acceptance Criteria

AUTOMATED

lib/notifications.ts exists with all four exported functions

Unit tests: schedule/cancel calls expo-notifications API correctly (mocked)

Permission check logic

Settings toggle wires to schedule/cancel

Notification response navigates to /check-in

Typescript passes

expo export passes

HUMAN_REVIEW

Permission prompt appears once after auth (MANUAL_PLAYTEST_REQUIRED)

Daily notification fires at configured time on device (MANUAL_PLAYTEST_REQUIRED)

Tapping notification opens /check-in (MANUAL_PLAYTEST_REQUIRED)

Settings deep-link to iOS Settings when denied (MANUAL_PLAYTEST_REQUIRED)

Notification content does not expose sensitive data on lock screen (MANUAL_PLAYTEST_REQUIRED — physical device only)

Phase I Execution

PRE-FLIGHT

Standard. Confirm Phase H merged. Cut feat/mobile-phase-i-notifications.

Spec-reality reconciliation:

Check whether expo-notifications version differs from current Expo SDK requirements

Check whether the assets directory has a notification icon

SMOKE ASSERTIONS

Mocked schedule call → correct args

Mocked cancel call → correct identifier

Permission check returns correct status

Settings toggle → schedule called

Settings toggle off → cancel called

IMPLEMENTATION

Install expo-notifications + expo-device

lib/notifications.ts

_layout.tsx permission prompt + listener

Settings wiring

app.json plugin config

COMMIT

Atomic per concern.

Directive-Specific Repair Entries

MOBILE-18 — Local notification does not fire on simulator A1: Local notifications on iOS simulator are flaky. Test on physical device. A2: Document MANUAL_PLAYTEST_REQUIRED for actual delivery validation. DEFER: Defer to device test.

MOBILE-19 — Notification permission undetermined after prompt A1: Verify Notifications.requestPermissionsAsync() was actually called and awaited. iOS sometimes returns "denied" if permission was previously denied. A2: Document the path: user must enable via iOS Settings. DEFER: LOW. Settings deep-link handles this.

GO

Begin Phase I pre-flight. Cut branch: feat/mobile-phase-i-notifications. PR title: [Mobile] Phase I: Local push notifications (daily check-in) No auto-merge.
