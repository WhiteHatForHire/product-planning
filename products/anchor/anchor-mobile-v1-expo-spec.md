---
title: "Anchor Mobile V1 — Expo Spec"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Anchor Mobile V1 — Expo Spec.docx"
status: active
privacy: working
tags:
  - product
---

# Anchor Mobile V1 — Expo Spec

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile V1 — Expo Spec

Version 0.1 — Locked decisions Status: PARKED — build after V5.2 ships Owner: Marcus / Eagle Rocket LLC

Goal

Prove the Director Model generalizes to native mobile shipping. Build Anchor for iOS using Expo managed React Native, ship to TestFlight, prepare App Store submission. User acquisition is a secondary benefit. The primary milestone is technical: Marcus directs agents to build, test, and ship a native iOS app with auth, deep linking, push notifications, and App Store compliance.

This is a proof-of-work gate, not a feature race.

Timing

Do not start until V5.2 (Data Export + Memory Search Lite) is stable on main. Mobile work must not interrupt the Anchor web stabilization cycle. After V5.2 merges and any immediate post-launch fixes land, mobile becomes the next technical proof gate.

Architecture

Option B: separate React Native Expo app, same backend.

Not Option A (Expo Router unified codebase) — too much rewrite risk, destabilizes working web app. Not Option C (WebView/Capacitor wrapper) — does not prove native capability.

One Expo managed React Native app in a new workspace inside the existing monorepo. Points to the same production Fly/Express backend and Supabase auth. No backend changes required to support mobile V1.

Codebase structure

Workspace: artifacts/mobile-app (consistent with existing artifacts naming convention).

Same monorepo, same git history, same backend contracts. Do not split into a separate repo.

When ready: pnpm workspace entry added for artifacts/mobile-app.

Backend

No changes. Express API on Fly stays as-is. All mobile API calls point to the same production endpoints the web app uses. No mobile-specific endpoints in V1 unless auth deep linking requires a small new route (unlikely).

Platforms

iOS only for V1. Android deferred.

Apple Developer account: already set up. Google Play account: exists but parked.

Reason: iOS/TestFlight/App Store is the capability milestone. Surface area stays narrow.

V1 feature scope

Non-negotiable for V1

Auth (magic link / email OTP + Sign in with Apple)

Home

Check-In

Chat

SOS (with offline cache)

Minimal Settings: logout, privacy/terms links, account/delete-account path, notification preference

Daily check-in push notification (one notification type, no alarmist nudges)

Deferred to V2 mobile

Practice Mode

Pattern Insight card

Data Export

Memory Search

Insights screen

Full Settings and customization

Advanced voice differentiation UI

Android

Auth

Supabase auth stays. Mobile requires deep link handling for magic links, OTP email confirmations, password reset flows, and OAuth callbacks.

Deep link scheme: anchor://auth/callback — configure in app.json as the Supabase redirect URL.

V1 auth stack (email-only first):

Email magic link or email OTP

This is the cleanest V1 path. Avoids Sign in with Apple entitlement and cert complexity. Avoids requiring Google sign-in which would mandate Apple sign-in per App Store guideline 4.8.

If Google sign-in is added post-V1:

Sign in with Apple must be added simultaneously (App Store 4.8 requires privacy-preserving equivalent when any third-party social login is offered).

Decision: email-only for V1 mobile. Revisit Google + Apple sign-in in V2.

Supabase deep linking:

Set redirectTo in Supabase magic link sends to anchor://auth/callback

Configure expo-linking and Supabase onAuthStateChange to handle the URL on app open

Test on physical device, not just simulator (deep links can behave differently in simulator)

Offline and storage

SOS offline cache — migrate from localStorage to mobile storage.

Store in AsyncStorage (non-sensitive display content):

sober contact name + phone

meeting label + URL

grounding text

tell-on-myself message

crisis card copy

cached_at timestamp

Use expo-secure-store only for sensitive items that need OS keychain (tokens, not SOS display content).

No broad stable_profile cache in V1. SOS offline only.

All other data requires network. No offline mode for Home, Check-In, or Chat in V1.

Push notifications

Daily check-in reminder only.

No crisis prompts. No milestone alerts. No commitment follow-ups. No "you seem at risk" style notifications. Anchor should not send alarmist or predictive nudges via push.

Implementation: Expo Notifications. Configure via EAS and Expo push notification service.

Notification permission request: prompt once after first successful auth, before the first Home load. If user declines, respect it. Provide a re-enable path in Settings.

Notification content: simple, non-shaming, time-consistent.

Title: "Anchor"

Body: "Time for your daily check-in."

No data payloads that could expose sensitive content on lock screen.

User-configured reminder time in Settings (stored in stable_profile or app_settings). Default: 9:00 AM local time.

Styling and components

NativeWind (Tailwind utility classes for React Native).

Closest mental model to current Tailwind styling. Easier for agents than Tamagui. Less generic-looking than React Native Paper.

Dark mode only for V1. Anchor's identity is dark, calm, quiet. Light mode support deferred.

Small internal component kit — build these first, use them everywhere:

Screen — safe-area-aware wrapper

Card

Button (primary + secondary variants)

TextField

Banner (info, warning, error)

SOSCard

CheckInOption

MessageBubble (chat surface)

NavBar (bottom tab or stack header)

Do not import a full third-party RN design system in V1. Own the components.

Build and distribution

Expo managed workflow — no bare workflow unless a native module forces it.

EAS Build — for all App Store and TestFlight binaries.

Distribution sequence:

Local Expo Go / development build on simulator

Physical iPhone via development build

TestFlight internal testing (mandatory gate before App Store)

App Store submission

EAS Submit for App Store submission when ready.

Do not submit to App Store until TestFlight has been validated on at least one physical device outside the development environment.

Testing

Manual QA for V1. No Detox or Appium.

V1 mobile QA checklist:

Expo development build on iOS simulator — all V1 surfaces load

Physical iPhone smoke — auth, Home, Check-In, Chat, SOS

Offline SOS test — airplane mode, SOS surfaces correctly with cached data

Deep link auth test — magic link email, tap on device, lands in app with session

Push notification test — notification arrives, taps open app to correct screen

TestFlight smoke — fresh install from TestFlight on a non-development device

Screenshots for App Store submission

Navigation

React Navigation (standard Expo-compatible library).

Bottom tab navigator for main surfaces: Home, Check-In, Chat, SOS. Stack navigator for auth flow. Modal for Settings.

SOS is always reachable from the tab bar. Not buried in navigation.

App Store metadata (prepare during build)

App name: Anchor

Subtitle: Sobriety self-governance

Category: Health & Fitness

Privacy policy URL: sobrietyanchor.com/privacy (must exist before submission)

Support URL: sobrietyanchor.com/support or support@sobrietyanchor.com

App description: to be written

Screenshots: required for 6.5" iPhone and 5.5" iPhone at minimum

Age rating: 4+ (no mature content per Apple's rating questions; check SAMHSA/988 content guidance)

Known pre-build tasks (before directive fires)

Confirm deep link scheme with Supabase (set redirect URL in Supabase project settings)

Create App ID / Bundle ID in Apple Developer portal (e.g., com.eaglerocket.anchor or com.sobrietyanchor.app)

Configure EAS account linked to Apple Developer account

Create provisioning profile and distribution certificate via EAS or manually

Confirm artifacts/mobile-app workspace added to pnpm-workspace.yaml

Build approach (when ready)

Single large directive, multiple phases, CC Local (needs Expo CLI and EAS credentials) plus CC Cloud for component phases.

Rough phase structure:

Phase A: Expo project scaffold, workspace entry, app.json config, NativeWind setup, deep link config

Phase B: Internal component kit (Screen, Card, Button, TextField, Banner, MessageBubble, SOSCard)

Phase C: Auth flow (Supabase magic link, deep link handler, session management)

Phase D: Home screen (day counts, recent check-in, primary CTA)

Phase E: Check-In screen (port existing check-in form to RN components)

Phase F: Chat screen (port existing chat UI to RN MessageBubble components, wire to same API)

Phase G: SOS screen (port existing SOS with offline cache via AsyncStorage)

Phase H: Minimal Settings (logout, notification preference, account deletion)

Phase I: Push notification setup (Expo Notifications, EAS config, daily reminder scheduler hook)

Phase J: EAS Build + TestFlight distribution config, QA checklist

Phase K: BUILD_REPORT + PR

Council of Models: required before merge for any AI-touching surfaces (Chat system prompt remains unchanged — mobile uses same backend, no new prompt surfaces). Not required for UI-only phases.

Auto-merge: no for any PR in this build.

What this does not include

Android build

Expo Router web+native unification

WebView wrapper

Realtime voice

Wearables or Apple Health

Practice Mode

Pattern Insight

Data Export or Memory Search

Accountability partner features

In-app purchases or subscriptions

Any new API endpoints (unless auth deep linking requires one)

Director Model positioning

Anchor Mobile V1 is the second major Director Model proof-of-work case study. Anchor Web proved: one solo founder using agents can build a production recovery app with real users in weeks, not months. Anchor Mobile proves: the same methodology generalizes to native iOS shipping, App Store compliance, and mobile-specific infrastructure (push notifications, deep links, offline storage, TestFlight distribution).

The narrative is clean: same Director Model, second domain, same result.
