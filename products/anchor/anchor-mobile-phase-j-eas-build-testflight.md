---
title: "Anchor Mobile — Phase J EAS Build + TestFlight"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase J_ EAS Build + TestFlight.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase J EAS Build + TestFlight

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase J: EAS Build + TestFlight

Apply AUTONOMY_LAYER.md before executing. Phase I must be merged to main before Phase J starts.

Surfaces:          artifacts/mobile-app/eas.json (refine)

artifacts/mobile-app/app.json (privacy, version)

artifacts/mobile-app/assets/ (icon, splash, screenshots)

App Store Connect (external)

Production impact: external app distribution to TestFlight

Council of Models: no

Auto-merge:        no

Credentials:       gh, eas, Apple Developer, App Store Connect

Agent:             CC Local (EAS credentials, Apple cert provisioning)

Role

Produce the first TestFlight build. Configure production EAS profile, refine icon and splash assets, write App Store metadata, run EAS Build for iOS, submit to TestFlight via EAS Submit. Internal testing distribution to Marcus's Apple ID. App Store submission is gated on TestFlight validation and is NOT part of Phase J.

Deployment Posture

Auto-merge: no. External distribution. Marcus must approve before submission. Code-level changes (eas.json, app.json, assets) merge via PR. EAS Build and EAS Submit run by Marcus from CC Local after PR merges.

Design Data

App Store metadata

App name:        Anchor

Subtitle:        Sobriety self-governance

Category:        Health & Fitness

Age rating:      4+

Privacy policy:  https://sobrietyanchor.com/privacy

Support URL:     https://sobrietyanchor.com/support

or support@sobrietyanchor.com

Primary lang:    English (US)

App description (verbatim — Marcus may refine)

Anchor is a quiet, judgment-free companion for sobriety self-governance.

Daily check-ins, a steady chat that meets you where you are, an SOS

screen for hard moments, and reminders that respect your pace.

Anchor is not a substitute for medical care, therapy, or a recovery

program. It's a tool that lives between sessions, supporting the work

you're already doing.

What's inside:

• Daily check-ins to track how you're really doing

• A supportive chat that understands recovery context

• SOS resources that work even when you're offline

• Reminders that aren't alarms

Anchor is built by someone in recovery, for people in recovery.

Icon and splash

artifacts/mobile-app/assets/icon.png — 1024x1024 PNG, no transparency, no rounded corners (iOS applies them)

artifacts/mobile-app/assets/splash.png — 1284x2778 PNG, dark background matching app theme (#0a0a0a)

artifacts/mobile-app/assets/adaptive-icon.png — only needed for Android (defer)

artifacts/mobile-app/assets/notification-icon.png — 96x96 PNG, monochrome (used by expo-notifications)

If Marcus has not provided custom icons: use placeholders and log to BLOCKERS_FOR_MARCUS.md. The build can ship to internal TestFlight with placeholders.

Screenshots

App Store requires:

6.5" iPhone (iPhone 14 Plus / 15 Plus): 1284 x 2778

6.1" iPhone (iPhone 14 / 15): 1170 x 2532 (optional but recommended)

Capture from simulator after build:

Home screen with day count

Check-in form

Chat screen

SOS screen

Settings

Five screenshots. Store at artifacts/mobile-app/assets/screenshots/.

eas.json refinement

Confirm production profile is configured. Add submit config:

"submit": {

"production": {

"ios": {

"appleId": "<Marcus's Apple ID>",

"ascAppId": "<App Store Connect app ID — generated after first submit>",

"appleTeamId": "<Apple Team ID>"

}

}

}

Use eas.json variables or EAS secrets to avoid committing Apple ID directly.

Build commands

Production build (Marcus runs after PR merges):

cd artifacts/mobile-app

eas build --platform ios --profile production

This produces an .ipa for TestFlight submission.

Submit to TestFlight:

eas submit --platform ios --profile production

EAS will auto-detect the most recent build.

app.json finalization

Confirm:

version: "1.0.0"

ios.buildNumber: "1"

ios.bundleIdentifier: "com.sobrietyanchor.app"

ios.infoPlist (add minimum required keys):

 "ios": { ..., "infoPlist": { "NSCameraUsageDescription": "Anchor does not use the camera.", "ITSAppUsesNonExemptEncryption": false } }

Note: NSCameraUsageDescription only needed if any dependency declares camera usage in its podspec. expo-image-picker or similar would force this. If no such dep is in the project, omit and let App Store reject if needed — do not pre-emptively add permissions you don't need.

ITSAppUsesNonExemptEncryption: false declares the app uses only standard HTTPS encryption (no custom crypto). This skips an export compliance form during submission.

Acceptance Criteria

AUTOMATED

eas.json contains a valid production profile

app.json has version, buildNumber, bundleIdentifier set correctly

All required assets exist at artifacts/mobile-app/assets/

ITSAppUsesNonExemptEncryption is set to false

Typescript passes

expo export --platform ios passes

HUMAN_REVIEW (mostly Marcus actions)

Apple Developer Team ID confirmed and added to eas.json

App Store Connect app record created (Marcus does this from web)

Privacy policy live at sobrietyanchor.com/privacy

Terms live at sobrietyanchor.com/terms

support@sobrietyanchor.com email working

Screenshots captured from simulator

eas build --platform ios --profile production completes

eas submit --platform ios --profile production completes

TestFlight build appears in App Store Connect

Internal tester invitation sent to Marcus's Apple ID

TestFlight install on physical device

Smoke test on TestFlight install (all V1 surfaces work)

Pre-requisites — Marcus actions before Phase J ships

[ ] App Store Connect: create app record for com.sobrietyanchor.app

[ ] Apple Team ID confirmed

[ ] Privacy policy live

[ ] Terms live

[ ] Support email working

[ ] Internal tester group created in App Store Connect

Log status of each in BLOCKERS_FOR_MARCUS.md.

Phase J Execution

PRE-FLIGHT

Standard. Confirm Phase I merged. Cut feat/mobile-phase-j-testflight.

Verify Marcus pre-requisites are at least partially complete. Hard prerequisites (App Store Connect record, Apple Team ID) must be done before the EAS submit step.

IMPLEMENTATION (PR-level)

Refine eas.json with production submit config

Finalize app.json (version, infoPlist, buildNumber)

Add assets (icon, splash, notification-icon)

Add screenshots directory

Document App Store metadata in artifacts/mobile-app/STORE.md

Open PR

After PR merges, Marcus runs (from local terminal):

eas build --platform ios --profile production

eas submit --platform ios --profile production

Log build URL and submission status in AUTONOMOUS_RUN_LOG.md.

HEALTH CHECK

All required files present

No secret credentials committed

STORE.md captures metadata for App Store Connect

COMMIT

Atomic per concern.

Directive-Specific Repair Entries

MOBILE-20 — eas build fails on signing A1: Run eas credentials and confirm distribution certificate and provisioning profile exist for the bundle ID. If not, let EAS auto-generate during build. A2: If EAS auto-gen fails: log to BLOCKERS_FOR_MARCUS.md. Marcus generates manually in Apple Developer portal. DEFER: HARD STOP.

MOBILE-21 — eas submit fails: app record not found A1: Verify the app exists in App Store Connect with matching bundle ID. A2: Manually upload the .ipa via Transporter.app as a fallback. DEFER: BLOCKER. Cannot ship without App Store Connect record.

MOBILE-22 — TestFlight install crashes on launch A1: Reproduce on simulator with production build. Check device logs via Console.app on macOS. A2: Roll back to last passing eas build. Diff to find the regression. DEFER: HARD STOP.

GO

Begin Phase J pre-flight. Cut branch: feat/mobile-phase-j-testflight. Pre-flight Marcus checklist before PR work begins. Log gaps. PR title: [Mobile] Phase J: TestFlight build config + assets + metadata No auto-merge.

After PR merges, run eas build + eas submit. Log result.
