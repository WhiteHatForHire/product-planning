---
title: "Anchor Mobile — Phase C Auth Flow (Supabase Magic Link)"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase C_ Auth Flow (Supabase Magic Link).docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase C Auth Flow (Supabase Magic Link)

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase C: Auth Flow (Supabase Magic Link)

Apply AUTONOMY_LAYER.md before executing. Stack: see AUTONOMY_LAYER.md section 0.1 (web) + Phase A mobile additions. Phase B must be merged to main before Phase C starts.

Surfaces:          artifacts/mobile-app/app/auth/ (new)

artifacts/mobile-app/lib/supabase.ts (new)

artifacts/mobile-app/lib/auth-storage.ts (new)

artifacts/mobile-app/App.tsx (auth gate wrapper)

Production impact: none (mobile uses existing Supabase project, no schema)

Council of Models: no

Auto-merge:        no

Credentials:       gh, EXPO_PUBLIC_SUPABASE_URL, EXPO_PUBLIC_SUPABASE_ANON_KEY

Agent:             CC Local (needs Supabase env vars + device for deep link test)

Role

Implement Supabase email-only authentication for the Anchor iOS app. Email magic link or email OTP only — no Apple/Google sign-in in V1 per spec. Deep link handler returns the user to the app from the magic-link email. Sessions persist via expo-secure-store. Session restored on cold launch. Sign-out clears the session. Phase C does not implement onboarding — that comes in a later phase. After auth, user lands on a placeholder Home screen.

Deployment Posture

Auto-merge: no. Auth is a load-bearing safety surface. No migrations. No Supabase dashboard changes (anchor://auth/callback already added per pre-build verification). No production data risk in V1 — mobile users are net-new logins against the existing Supabase project.

Design Data

Environment variables

Required in artifacts/mobile-app/.env (not committed) and EAS secrets:

EXPO_PUBLIC_SUPABASE_URL=<from web app env>

EXPO_PUBLIC_SUPABASE_ANON_KEY=<from web app env>

Mirror these on EAS:

eas secret:create --scope project --name EXPO_PUBLIC_SUPABASE_URL --value <value>

eas secret:create --scope project --name EXPO_PUBLIC_SUPABASE_ANON_KEY --value <value>

Add to artifacts/mobile-app/.gitignore:

.env

.env.local

Dependencies to install

npx expo install @supabase/supabase-js expo-secure-store expo-linking expo-router

If expo-router is not already installed by Phase A scaffold, install it now and migrate from App.tsx to expo-router app/ directory.

Deep link scheme

Already set in Phase A app.json: scheme: "anchor" Callback URL: anchor://auth/callback

Token storage strategy

Use expo-secure-store for the Supabase session (refresh token, access token). Do NOT store tokens in AsyncStorage. The Supabase JS client accepts a custom storage adapter — implement one backed by SecureStore.

File: artifacts/mobile-app/lib/auth-storage.ts (verbatim)

import * as SecureStore from "expo-secure-store";

export const SecureStorageAdapter = {

getItem: (key: string) => SecureStore.getItemAsync(key),

setItem: (key: string, value: string) => SecureStore.setItemAsync(key, value),

removeItem: (key: string) => SecureStore.deleteItemAsync(key),

};

File: artifacts/mobile-app/lib/supabase.ts (verbatim)

import "react-native-url-polyfill/auto";

import { createClient } from "@supabase/supabase-js";

import { SecureStorageAdapter } from "./auth-storage";

const supabaseUrl = process.env.EXPO_PUBLIC_SUPABASE_URL;

const supabaseAnonKey = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {

throw new Error(

"Missing EXPO_PUBLIC_SUPABASE_URL or EXPO_PUBLIC_SUPABASE_ANON_KEY"

);

}

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {

auth: {

storage: SecureStorageAdapter,

autoRefreshToken: true,

persistSession: true,

detectSessionInUrl: false,

},

});

Install react-native-url-polyfill if not present:

npx expo install react-native-url-polyfill

Screens

Three screens, expo-router file-based routing:

app/_layout.tsx          — root layout, auth state provider

app/index.tsx            — redirects to /auth/sign-in or /home based on session

app/auth/sign-in.tsx     — email entry

app/auth/check-email.tsx — "we sent you a link" instructions

app/auth/callback.tsx    — deep link landing, exchanges code for session

app/home/index.tsx       — placeholder Home screen ("You're signed in")

Screen content (verbatim copy)

sign-in.tsx

Title:        "Welcome to Anchor"

Subtitle:     "Enter your email to get a sign-in link."

Field label:  "Email"

Placeholder:  "you@example.com"

CTA:          "Send sign-in link"

Error states:

- Empty email: "Please enter your email."

- Invalid format: "That doesn't look like an email address."

- Network failure: "We couldn't send the link. Check your connection and try again."

check-email.tsx

Title:    "Check your email"

Body:     "We sent a sign-in link to {email}. Tap the link to continue."

Footer:   "Didn't get it? Check spam or wait a minute before trying again."

Action:   "Use a different email" (returns to sign-in)

callback.tsx

Body:     "Signing you in..."

Error:    "That link didn't work. Try requesting a new one."

Action:   "Back to sign-in"

home/index.tsx (placeholder for Phase C)

Title:    "Home"

Body:     "You're signed in."

Action:   "Sign out" (Button, secondary variant)

Auth flow contract

User opens app cold → app/_layout.tsx checks session via supabase.auth.getSession()

If session: navigate to /home

If no session: navigate to /auth/sign-in

On sign-in submit → supabase.auth.signInWithOtp({ email, options: { emailRedirectTo: "anchor://auth/callback" } })

Navigate to /auth/check-email

User taps email link → opens app at /auth/callback?token=...

callback.tsx calls supabase.auth.exchangeCodeForSession(url)

On success → navigate to /home

On failure → show error, allow return to sign-in

Sign-out from /home → supabase.auth.signOut() → navigate to /auth/sign-in

Deep link handler setup

In app/_layout.tsx, use expo-linking to listen for incoming URLs:

import * as Linking from "expo-linking";

import { useEffect } from "react";

useEffect(() => {

const sub = Linking.addEventListener("url", ({ url }) => {

if (url.includes("auth/callback")) {

// expo-router will handle navigation via the URL

// exchangeCodeForSession is called in callback.tsx

}

});

return () => sub.remove();

}, []);

Acceptance Criteria

AUTOMATED

artifacts/mobile-app/lib/supabase.ts and auth-storage.ts exist with verbatim content

All five screen files exist at the specified paths

TypeScript: npx tsc --noEmit passes

Render tests pass for each screen component (jest-expo)

Mock-based unit test: supabase.auth.signInWithOtp called with correct emailRedirectTo

expo export --platform ios completes without error

HUMAN_REVIEW

Magic link round-trip on physical device (MANUAL_PLAYTEST_REQUIRED)

Sign in → email received → tap link → app opens at /home

Cold launch session restoration (MANUAL_PLAYTEST_REQUIRED)

Sign-out clears session and navigates to sign-in (MANUAL_PLAYTEST_REQUIRED)

Error states display correctly (MANUAL_PLAYTEST_REQUIRED)

SecureStore actually persisting session across app restarts (MANUAL_PLAYTEST_REQUIRED)

Phase C — Auth + Deep Link + Session

PRE-FLIGHT

git status                         # clean

git checkout main && git pull

pnpm install --frozen-lockfile

Confirm Phase B merged. Verify components exist at artifacts/mobile-app/components/. Confirm Supabase env vars are documented (presence in artifacts/mobile-app/.env.example).

Cut branch: feat/mobile-phase-c-auth

Spec-reality reconciliation:

Read artifacts/mobile-app/App.tsx — does it already use expo-router, or blank-typescript template? Phase A and B may differ from this directive's assumption. If blank-typescript, this phase migrates to expo-router.

Confirm @supabase/supabase-js version matches web app version (avoid drift).

Check whether react-native-url-polyfill is already present.

SMOKE ASSERTIONS

Write before implementation:

Unit test (mocked supabase client): signInWithOtp called with emailRedirectTo === "anchor://auth/callback"

Render test: sign-in.tsx shows email field and submit button

Render test: check-email.tsx shows the email passed via params

Render test: callback.tsx renders loading state

Render test: home/index.tsx renders sign-out button

Run. Expect red. Implement until green.

IMPLEMENTATION

Install dependencies

Create lib/auth-storage.ts and lib/supabase.ts verbatim

Migrate to expo-router structure if not already

Implement sign-in.tsx

Implement check-email.tsx

Implement callback.tsx with exchangeCodeForSession

Implement home/index.tsx placeholder

Implement _layout.tsx with auth gate logic

Implement index.tsx redirect logic

Configure .env.example and .gitignore

HEALTH CHECK

cd artifacts/mobile-app

npx tsc --noEmit

pnpm test

npx expo export --platform ios

Log MANUAL_PLAYTEST_REQUIRED items.

COMMIT

Atomic per concern: deps, supabase client, each screen, layout, gate logic.

Directive-Specific Repair Entries

MOBILE-7 — Supabase env vars missing at runtime A1: Verify .env exists in artifacts/mobile-app/ and is loaded by Expo. Expo auto-loads .env files prefixed with EXPO_PUBLIC_. Restart Metro with -c flag. A2: Hard-code temporarily for local testing (NEVER commit). Log to BLOCKERS_FOR_MARCUS.md for Marcus to set EAS secrets. DEFER: HARD STOP — auth cannot work without these.

MOBILE-8 — Deep link does not open app from email A1: Verify scheme: "anchor" in app.json. On iOS simulator, deep links work via xcrun simctl openurl. Test with: xcrun simctl openurl booted anchor://auth/callback?token=test A2: Check that expo-linking is initialized in _layout.tsx. Verify emailRedirectTo in the signInWithOtp call. DEFER: MANUAL_PLAYTEST_REQUIRED — requires physical device test.

MOBILE-9 — exchangeCodeForSession returns error A1: Verify the URL passed to exchangeCodeForSession contains the access_token and refresh_token query params. Some Supabase flows use code= instead. Adapt to whichever Supabase actually sends. A2: Switch to verifyOtp if magic-link exchange fails. Log SPEC_REALITY_DELTA. DEFER: Log BLOCKER — auth completion is core.

GO

Begin Phase C pre-flight per AUTONOMY_LAYER.md section 3. Credentials preflight: gh, EXPO_PUBLIC_SUPABASE_URL, EXPO_PUBLIC_SUPABASE_ANON_KEY. Cut branch from main: feat/mobile-phase-c-auth Create docs/run-notes/session-YYYY-MM-DD-mobile-phase-c-plan.md. PR title: [Mobile] Phase C: Supabase auth + deep link + session Do not auto-merge.
