---
title: "Anchor Mobile — Phase A Expo Scaffold + NativeWind + EAS Config"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase A_ Expo Scaffold + NativeWind + EAS Config.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase A Expo Scaffold + NativeWind + EAS Config

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase A: Expo Scaffold + NativeWind + EAS Config

Apply AUTONOMY_LAYER.md before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1 for the web stack. Mobile stack addition (Phase A scope only):

Runtime: Expo managed workflow (React Native, TypeScript)

Workspace: artifacts/mobile-app (new — does not exist yet)

Build: EAS Build (eas-cli, authenticated)

Style: NativeWind v4 (Tailwind for React Native)

Platform: iOS only for V1

Surfaces:          artifacts/mobile-app (new workspace — scaffold only)

Production impact: none

Council of Models: no

Auto-merge:        no

Credentials:       gh, eas (authenticated prior to this directive)

Agent:             CC Local

Role

You are scaffolding the Anchor iOS mobile app as a new Expo managed workflow workspace inside the existing Anchor monorepo. You will create artifacts/mobile-app, configure app.json, install NativeWind, configure EAS, and verify the blank scaffold loads. You are not implementing any features. You are not touching the web app (artifacts/recovery-checkin) or the API server (artifacts/api-server). This phase ends with a PR open for Marcus to review. Do not auto-merge.

Deployment Posture

Auto-merge: no. This is a new major workspace with no existing CI coverage for mobile. Open a PR and stop. Marcus reviews and merges.

No migrations. No Fly secrets. No Vercel env changes. No production impact.

Design Data

Bundle ID

com.sobrietyanchor.app

Deep link scheme

anchor

Handles: anchor://auth/callback

Color tokens (NativeWind theme extension)

background: "#0a0a0a"

surface:    "#141414"

primary:    "#6366f1"

muted:      "#3f3f46"

text:       "#f4f4f5"

subtle:     "#a1a1aa"

app.json (full content — write verbatim)

{

"expo": {

"name": "Anchor",

"slug": "anchor",

"version": "1.0.0",

"orientation": "portrait",

"icon": "./assets/icon.png",

"userInterfaceStyle": "dark",

"splash": {

"image": "./assets/splash.png",

"resizeMode": "contain",

"backgroundColor": "#0a0a0a"

},

"ios": {

"supportsTablet": false,

"bundleIdentifier": "com.sobrietyanchor.app",

"buildNumber": "1"

},

"scheme": "anchor",

"platforms": ["ios"],

"assetBundlePatterns": ["**/*"],

"newArchEnabled": true

}

}

Note: eas init will append expo.extra.eas.projectId after Task 8. Do not pre-populate it.

eas.json (full content — write verbatim)

{

"cli": {

"version": ">= 16.0.0"

},

"build": {

"development": {

"developmentClient": true,

"distribution": "internal",

"ios": {

"simulator": true

}

},

"preview": {

"distribution": "internal"

},

"production": {

"autoIncrement": true

}

},

"submit": {

"production": {}

}

}

tailwind.config.js (full content — write verbatim)

/** @type {import('tailwindcss').Config} */

module.exports = {

content: [

"./app/**/*.{js,jsx,ts,tsx}",

"./components/**/*.{js,jsx,ts,tsx}"

],

presets: [require("nativewind/preset")],

theme: {

extend: {

colors: {

background: "#0a0a0a",

surface: "#141414",

primary: "#6366f1",

muted: "#3f3f46",

text: "#f4f4f5",

subtle: "#a1a1aa"

}

}

},

plugins: []

};

babel.config.js (full content — write verbatim)

module.exports = function (api) {

api.cache(true);

return {

presets: [

["babel-preset-expo", { jsxImportSource: "nativewind" }],

"nativewind/babel"

]

};

};

metro.config.js (full content — write verbatim)

const { getDefaultConfig } = require("expo/metro-config");

const { withNativeWind } = require("nativewind/metro");

const config = getDefaultConfig(__dirname);

module.exports = withNativeWind(config, { input: "./global.css" });

global.css (full content — write verbatim)

@tailwind base;

@tailwind components;

@tailwind utilities;

tsconfig.json (full content — write verbatim)

{

"extends": "expo/tsconfig.base",

"compilerOptions": {

"strict": true,

"paths": {

"@/*": ["./*"]

}

}

}

Acceptance Criteria

AUTOMATED

artifacts/mobile-app directory exists

artifacts/mobile-app/app.json exists and contains bundleIdentifier: "com.sobrietyanchor.app"

artifacts/mobile-app/app.json contains scheme: "anchor"

artifacts/mobile-app/app.json contains userInterfaceStyle: "dark"

artifacts/mobile-app/eas.json exists

artifacts/mobile-app/tailwind.config.js exists

artifacts/mobile-app/babel.config.js exists

artifacts/mobile-app/metro.config.js exists

artifacts/mobile-app/global.css exists

artifacts/mobile-app/tsconfig.json exists

nativewind is listed in artifacts/mobile-app/package.json dependencies

tailwindcss is listed in artifacts/mobile-app/package.json dependencies

expo.extra.eas.projectId is present in app.json after eas init

npx expo export --platform ios completes without error (dry build check)

HUMAN_REVIEW

Simulator loads blank scaffold with dark background (MANUAL_PLAYTEST_REQUIRED)

NativeWind color tokens are visually applied (MANUAL_PLAYTEST_REQUIRED)

Working Files

Create at the start of Phase A pre-flight:

docs/run-notes/session-YYYY-MM-DD-expo-phase-a-plan.md

AUTONOMOUS_RUN_LOG.md (append if exists, create if not)

BLOCKERS_FOR_MARCUS.md (append if exists, create if not)

Replace YYYY-MM-DD with today's date.

Phase A — Scaffold + Configure + Verify

PRE-FLIGHT

git status                        # must be clean — ANCHOR-14 if not

git log --oneline -1              # confirm base commit

pnpm install --frozen-lockfile    # ANCHOR-15 if fails

gh auth status                    # confirm gh authenticated

eas whoami                        # confirm eas authenticated — BLOCKER if fails

Record: current HEAD SHA, pnpm workspace list output confirming artifacts/* glob is present.

Spec-reality reconciliation: this is Phase A of a new workspace. No existing mobile code to reconcile against. Confirm only that artifacts/mobile-app does NOT exist yet (expected). If it does exist, log SPEC_REALITY_DELTA and inspect contents before proceeding.

Cut branch from main:

feat/mobile-phase-a-expo-scaffold

Create working files:

docs/run-notes/session-YYYY-MM-DD-expo-phase-a-plan.md

AUTONOMOUS_RUN_LOG.md

SMOKE ASSERTIONS — write and run before scaffold

Create a shell-executable verification script at artifacts/mobile-app-preflight-check.sh (delete after Phase A completes):

#!/bin/bash

set -e

echo "SMOKE: artifacts/mobile-app must not exist yet"

[ ! -d "artifacts/mobile-app" ] && echo "PASS: directory absent" || (echo "FAIL: directory already exists" && exit 1)

Run it. Expect green. If it fails (directory exists), log SPEC_REALITY_DELTA and inspect before continuing.

IMPLEMENTATION

Step 1 — Scaffold

From monorepo root:

npx create-expo-app@latest artifacts/mobile-app --template blank-typescript

Step 2 — Replace app.json

Overwrite artifacts/mobile-app/app.json with the verbatim content from Design Data above.

Step 3 — Create eas.json

Write artifacts/mobile-app/eas.json with verbatim content from Design Data.

Step 4 — Install dependencies

From inside artifacts/mobile-app:

npx expo install nativewind tailwindcss react-native-reanimated react-native-safe-area-context

Step 5 — NativeWind configuration

Write the following files with verbatim content from Design Data:

artifacts/mobile-app/tailwind.config.js

artifacts/mobile-app/babel.config.js

artifacts/mobile-app/metro.config.js

artifacts/mobile-app/global.css

In App.tsx (or _layout.tsx if it exists), add as the first line:

import "./global.css";

Step 6 — tsconfig.json

Overwrite artifacts/mobile-app/tsconfig.json with verbatim content from Design Data.

Step 7 — EAS init

From inside artifacts/mobile-app:

eas init

Accept defaults. After completion, verify expo.extra.eas.projectId has been written into app.json. Log the project ID to AUTONOMOUS_RUN_LOG.md.

Step 8 — Dry build check

From inside artifacts/mobile-app:

npx expo export --platform ios

This validates the project compiles without a full EAS build. Log result to AUTONOMOUS_RUN_LOG.md.

Step 9 — Delete preflight script

rm artifacts/mobile-app-preflight-check.sh

HEALTH CHECK

Verify all AUTOMATED acceptance criteria:

[ -d "artifacts/mobile-app" ]

[ -f "artifacts/mobile-app/app.json" ]

grep -q "com.sobrietyanchor.app" artifacts/mobile-app/app.json

grep -q '"scheme": "anchor"' artifacts/mobile-app/app.json

grep -q '"userInterfaceStyle": "dark"' artifacts/mobile-app/app.json

[ -f "artifacts/mobile-app/eas.json" ]

[ -f "artifacts/mobile-app/tailwind.config.js" ]

[ -f "artifacts/mobile-app/babel.config.js" ]

[ -f "artifacts/mobile-app/metro.config.js" ]

[ -f "artifacts/mobile-app/global.css" ]

grep -q "nativewind" artifacts/mobile-app/package.json

grep -q "tailwindcss" artifacts/mobile-app/package.json

grep -q "projectId" artifacts/mobile-app/app.json

Log MANUAL_PLAYTEST_REQUIRED: simulator dark-background visual check.

COMMIT

feat(mobile): Phase A — Expo scaffold, NativeWind, EAS config

New workspace: artifacts/mobile-app

Bundle ID: com.sobrietyanchor.app

Scheme: anchor (deep link anchor://auth/callback)

Style: NativeWind v4, dark mode only

EAS: linked, eas.json configured for dev/preview/production

Phase: A

Deferrals: 0

Tests: automated file assertions passing

Council review: no

Directive-Specific Repair Entries

MOBILE-1 — eas init fails: not authenticated A1: Run eas whoami to confirm session. If expired, eas login and retry. A2: Log to BLOCKERS_FOR_MARCUS.md. Skip eas init. Continue without projectId. DEFER: Note projectId as missing in BUILD_REPORT. Marcus runs eas init manually after reviewing PR.

MOBILE-2 — npx expo export --platform ios fails on NativeWind config A1: Verify babel.config.js presets match verbatim spec. Check metro.config.js withNativeWind call. Verify global.css import exists in App.tsx. A2: Remove NativeWind config and test bare export. If bare passes, NativeWind config is the issue. Log diff to BLOCKERS_FOR_MARCUS.md. DEFER: HARD STOP if export fails after both attempts — scaffold is broken.

MOBILE-3 — create-expo-app generates unexpected structure A1: Run spec-reality reconciliation on generated structure. Log SPEC_REALITY_DELTA. Adapt file paths (e.g., _layout.tsx vs App.tsx) to match what was generated. Do not force a structure the template did not produce. A2: Accept generated structure. Update all file references in this directive to match reality. Log all adaptations to AUTONOMOUS_RUN_LOG.md. DEFER: Continue. Phase B will build on whatever structure Phase A produced.

Deferred-issues format: AUTONOMY_LAYER.md section 4 BUILD_REPORT format: AUTONOMY_LAYER.md section 5 Hard stops: AUTONOMY_LAYER.md section 6

GO

Begin Phase A pre-flight per AUTONOMY_LAYER.md section 3.

Credentials preflight scope: gh, eas.

Cut branch from main: feat/mobile-phase-a-expo-scaffold

Create docs/run-notes/session-YYYY-MM-DD-expo-phase-a-plan.md and AUTONOMOUS_RUN_LOG.md at repo root.

Open PR titled: [Mobile] Phase A: Expo scaffold + NativeWind + EAS config Do not auto-merge. Stop after PR is open.
