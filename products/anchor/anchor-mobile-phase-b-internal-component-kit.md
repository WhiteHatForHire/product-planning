---
title: "Anchor Mobile — Phase B Internal Component Kit"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase B_ Internal Component Kit.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase B Internal Component Kit

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase B: Internal Component Kit

Apply AUTONOMY_LAYER.md before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1 for the web stack. Mobile stack (from Phase A):

Runtime: Expo managed workflow (React Native, TypeScript)

Workspace: artifacts/mobile-app

Style: NativeWind v4 (Tailwind for React Native), dark mode only

Platform: iOS only for V1

Phase A must be merged to main before Phase B starts.

Surfaces:          artifacts/mobile-app/components/ (new directory)

artifacts/mobile-app/tailwind.config.js (color additions)

artifacts/mobile-app/App.tsx (component showcase)

Production impact: none

Council of Models: no

Auto-merge:        no

Credentials:       gh

Agent:             CC Cloud (no credentials beyond gh — code-only work)

Role

You are building the internal component kit for the Anchor iOS mobile app. Nine components, TypeScript, NativeWind-styled, dark mode only. These are structural primitives that all feature surfaces in Phase D onward will consume. No business logic. No API calls. No auth. No state beyond local component state. You will also build a single demo screen (App.tsx) that showcases every component so Marcus can visually playtest them. This phase ends with a PR open for review.

Deployment Posture

Auto-merge: no. Components are visual surfaces. Visual review is HUMAN_REVIEW per AUTONOMY_LAYER section 1.5 and cannot be automated. Marcus reviews on simulator before merge.

No migrations. No Fly secrets. No Vercel env. No production impact.

Design Data

Components to build (in artifacts/mobile-app/components/)

Screen.tsx

Card.tsx

Button.tsx

TextField.tsx

Banner.tsx

SOSCard.tsx

CheckInOption.tsx

MessageBubble.tsx

NavBar.tsx

Plus:

index.ts — barrel export for all components

tests/ — one render test per component

Color tokens — extend tailwind.config.js

Add to existing theme.extend.colors:

danger:  "#ef4444"

warning: "#f59e0b"

success: "#10b981"

info:    "#6366f1"

Existing tokens preserved: background, surface, primary, muted, text, subtle.

Component specifications

All components export as named exports plus default export. All accept optional className prop (NativeWind) for additional styling. All include TypeScript types exported alongside.

Screen.tsx

Safe-area-aware wrapper with dark background. Every feature screen wraps content in this.

Props:

children: React.ReactNode

className?: string

scrollable?: boolean   // default false — uses ScrollView if true

padded?: boolean       // default true — applies px-4 py-6

Base styles:

bg-background flex-1

Adds SafeAreaView from react-native-safe-area-context

Implementation notes:

- Use SafeAreaView from react-native-safe-area-context

- If scrollable: wrap children in ScrollView with showsVerticalScrollIndicator=false

- StatusBar style="light" (dark mode)

Card.tsx

Rounded container with surface color background.

Props:

children: React.ReactNode

className?: string

onPress?: () => void   // if provided, wraps in Pressable

Base styles:

bg-surface rounded-2xl p-4

Implementation notes:

- If onPress provided: wrap in Pressable with active:opacity-80

- Otherwise: plain View

Button.tsx

Props:

label: string

onPress: () => void

variant?: "primary" | "secondary"   // default primary

disabled?: boolean

loading?: boolean

className?: string

Variant styles:

primary:   bg-primary

secondary: bg-transparent border border-primary

Label color:

primary:   text-white

secondary: text-primary

Base styles:

rounded-xl py-3 px-6 items-center justify-center

active:opacity-80

disabled:opacity-40

Implementation notes:

- If loading: show ActivityIndicator instead of label, color matches label color

- If disabled or loading: onPress is a no-op

- Use Pressable, not TouchableOpacity (modern API)

- Minimum tap target 44px (py-3 + label is roughly that — verify)

TextField.tsx

Props:

label: string

value: string

onChangeText: (text: string) => void

placeholder?: string

error?: string

secureTextEntry?: boolean

keyboardType?: "default" | "email-address" | "numeric"

autoCapitalize?: "none" | "sentences"

className?: string

Layout:

Label (text-subtle text-sm mb-2)

TextInput (bg-surface rounded-xl px-4 py-3 text-text border border-muted)

Error state: border-danger

Focus state: border-primary

Error text (text-danger text-xs mt-1) — only renders if error prop set

Implementation notes:

- Use TextInput from react-native

- placeholderTextColor="#a1a1aa" (subtle)

- Focus state tracked via local useState

Banner.tsx

Props:

message: string

variant?: "info" | "warning" | "error"   // default info

onDismiss?: () => void

className?: string

Variant background colors (with opacity):

info:    bg-info/10 border-info

warning: bg-warning/10 border-warning

error:   bg-danger/10 border-danger

Variant text colors:

info:    text-info

warning: text-warning

error:   text-danger

Base styles:

flex-row items-start justify-between

rounded-xl border px-4 py-3

Implementation notes:

- If onDismiss provided: render a Pressable "X" on the right

- X uses Text component with × character (no icon library in V1)

SOSCard.tsx

Specialized urgent-action card. Used on SOS screen.

Props:

title: string

subtitle?: string

actionLabel: string

onAction: () => void

className?: string

Layout:

bg-danger/15 border border-danger rounded-2xl p-5

Title: text-text text-lg font-semibold

Subtitle: text-subtle text-sm mt-1 (only if provided)

Button: primary-style button with bg-danger and text-white, full-width, mt-4

Implementation notes:

- This is a specialized component, not a Button variant

- Always visible, never disabled (SOS is always available)

CheckInOption.tsx

Selectable card used on check-in surface. Acts like a tappable radio option.

Props:

label: string

description?: string

selected: boolean

onPress: () => void

className?: string

Layout:

Pressable wrapper

Card-style: bg-surface rounded-xl p-4 border-2

Border: border-primary if selected, border-muted if not

Label: text-text text-base font-medium

Description: text-subtle text-sm mt-1 (only if provided)

Implementation notes:

- active:opacity-80

- The whole card is tappable

MessageBubble.tsx

Chat bubble component. User and assistant variants.

Props:

text: string

sender: "user" | "assistant"

className?: string

Layout:

Wrapper: flex-row, justify-end if user, justify-start if assistant

Bubble: max-w-[80%] rounded-2xl px-4 py-3

User:      bg-primary, text-white, rounded-br-sm

Assistant: bg-surface, text-text, rounded-bl-sm

Text: text-base

Implementation notes:

- Asymmetric corner (rounded-br-sm / rounded-bl-sm) signals direction

- No avatars in V1

- No timestamps in V1

NavBar.tsx

Top header for screens. Title-centered with optional left/right slots.

Props:

title: string

leftAction?: { label: string; onPress: () => void }

rightAction?: { label: string; onPress: () => void }

className?: string

Layout:

flex-row items-center justify-between px-4 py-3 border-b border-muted

Left slot: Pressable with leftAction.label (text-primary), or empty View for spacing

Center: title (text-text text-lg font-semibold)

Right slot: Pressable with rightAction.label (text-primary), or empty View

Implementation notes:

- If no leftAction or rightAction, render empty View (w-12) to keep title centered

- Bottom tab navigation comes in Phase D (React Navigation), not this phase

index.ts (barrel export)

export { Screen } from "./Screen";

export { Card } from "./Card";

export { Button } from "./Button";

export { TextField } from "./TextField";

export { Banner } from "./Banner";

export { SOSCard } from "./SOSCard";

export { CheckInOption } from "./CheckInOption";

export { MessageBubble } from "./MessageBubble";

export { NavBar } from "./NavBar";

export type { ScreenProps } from "./Screen";

export type { CardProps } from "./Card";

export type { ButtonProps } from "./Button";

export type { TextFieldProps } from "./TextField";

export type { BannerProps } from "./Banner";

export type { SOSCardProps } from "./SOSCard";

export type { CheckInOptionProps } from "./CheckInOption";

export type { MessageBubbleProps } from "./MessageBubble";

export type { NavBarProps } from "./NavBar";

App.tsx (component showcase)

Replace existing App.tsx scaffold with a showcase screen that renders every component in a vertical scroll. This is the visual playtest surface.

Showcase layout (in order):

NavBar with title "Components" and a rightAction "Done" (no-op onPress)

Section: "Buttons" — Card containing one primary Button, one secondary Button, one disabled Button, one loading Button

Section: "Text Field" — Card containing one TextField with label "Email", placeholder "you@example.com", and one TextField with label "Password", secureTextEntry, with a sample error message

Section: "Banners" — Card containing one info Banner, one warning Banner, one error Banner with onDismiss

Section: "SOS Card" — SOSCard with title "Need help right now?", subtitle "Your support contact is one tap away", actionLabel "Call sober contact", onAction no-op

Section: "Check-In Options" — Card containing three CheckInOption items. Use local useState in App.tsx to track which is selected. Labels: "Steady", "A little shaky", "Rough day". Each with a short description.

Section: "Chat Bubbles" — Card containing one assistant MessageBubble ("How are you feeling right now?") and one user MessageBubble ("I'm holding steady.")

Wrap entire showcase in Screen component with scrollable=true.

Use placeholder strings only. No real user data. No API calls.

Acceptance Criteria

AUTOMATED

All 9 component files exist at artifacts/mobile-app/components/[Name].tsx

artifacts/mobile-app/components/index.ts exists and exports all 9

artifacts/mobile-app/tailwind.config.js contains danger, warning, success, info color tokens

artifacts/mobile-app/App.tsx renders the showcase (file structurally imports all 9 components)

TypeScript: npx tsc --noEmit passes in artifacts/mobile-app

Component render tests pass — one per component, verifies render without crash (jest-expo + @testing-library/react-native)

npx expo export --platform ios completes without error

HUMAN_REVIEW

Component visual quality on simulator (MANUAL_PLAYTEST_REQUIRED)

Color tokens render correctly (MANUAL_PLAYTEST_REQUIRED)

Tap targets are reachable (MANUAL_PLAYTEST_REQUIRED)

Safe-area handling on real device (MANUAL_PLAYTEST_REQUIRED)

Component API ergonomics — Marcus's judgment whether the prop shapes feel right before Phase D consumes them (MANUAL_PLAYTEST_REQUIRED)

Test Setup

Install dev dependencies (if not already present):

pnpm add -D --filter @anchor/mobile-app jest jest-expo @testing-library/react-native @types/jest react-test-renderer

Create artifacts/mobile-app/jest.config.js:

module.exports = {

preset: "jest-expo",

transformIgnorePatterns: [

"node_modules/(?!((jest-)?react-native|@react-native(-community)?|expo(nent)?|@expo(nent)?/.*|@expo-google-fonts/.*|react-navigation|@react-navigation/.*|@unimodules/.*|unimodules|sentry-expo|native-base|react-native-svg|nativewind))"

],

setupFilesAfterEach: []

};

Add to artifacts/mobile-app/package.json scripts:

"test": "jest",

"typecheck": "tsc --noEmit"

Each test file at artifacts/mobile-app/components/tests/[Name].test.tsx follows this pattern:

import { render } from "@testing-library/react-native";

import { [Name] } from "../[Name]";

describe("[Name]", () => {

it("renders without crashing", () => {

const { toJSON } = render(<[Name] {...minimalProps} />);

expect(toJSON()).toBeTruthy();

});

});

Use minimal valid props for each component.

Working Files

Create at the start of Phase B pre-flight:

docs/run-notes/session-YYYY-MM-DD-mobile-phase-b-plan.md

AUTONOMOUS_RUN_LOG.md (append to existing)

BLOCKERS_FOR_MARCUS.md (append to existing if needed)

Phase B — Components + Showcase + Tests

PRE-FLIGHT

git status                        # clean

git log --oneline -1              # confirm Phase A merged

git checkout main && git pull

pnpm install --frozen-lockfile    # ANCHOR-15 if fails

gh auth status

Cut branch from main:

feat/mobile-phase-b-component-kit

Verify Phase A artifacts exist:

[ -f "artifacts/mobile-app/app.json" ]

[ -f "artifacts/mobile-app/tailwind.config.js" ]

[ -f "artifacts/mobile-app/babel.config.js" ]

If any missing: HARD STOP. Phase A is not merged.

Spec-reality reconciliation per AUTONOMY_LAYER section 1.13:

Read artifacts/mobile-app/App.tsx as scaffolded by Phase A. Confirm whether it is App.tsx (blank-typescript template) or _layout.tsx + index.tsx (expo-router template). Phase A reported App.tsx. Verify before assuming.

Read artifacts/mobile-app/tailwind.config.js. Confirm existing color tokens before adding new ones — do not overwrite Phase A's color block.

Read artifacts/mobile-app/package.json. Note current dep list before adding jest/testing-library.

Log SPEC_REALITY_DELTA for any difference.

Create working files.

SMOKE ASSERTIONS — write tests first

Write all 9 component test files at artifacts/mobile-app/components/tests/[Name].test.tsx using the pattern above. Run them. Expect 9 failures (components do not exist yet). Log baseline.

pnpm --filter @anchor/mobile-app test

IMPLEMENTATION

Step 1 — Update tailwind.config.js Add danger, warning, success, info to theme.extend.colors. Preserve existing tokens.

Step 2 — Install test deps Run install command from Test Setup section. Verify jest.config.js created.

Step 3 — Build components in order For each of the 9 components: implement per spec, run that component's test, confirm green before moving to the next. If a test fails: GENERIC-1, 2 attempts, then defer with it.skip and log.

Step 4 — Create index.ts barrel export

Step 5 — Build App.tsx showcase Replace existing App.tsx with the showcase layout. Import all 9 components from "./components". Use local useState for CheckInOption selection.

Step 6 — Typecheck Run npx tsc --noEmit from artifacts/mobile-app. Fix any errors.

Step 7 — Dry build check Run npx expo export --platform ios. Confirm green.

HEALTH CHECK

Verify all AUTOMATED criteria:

[ -d "artifacts/mobile-app/components" ]

ls artifacts/mobile-app/components/*.tsx | wc -l   # expect 9

[ -f "artifacts/mobile-app/components/index.ts" ]

grep -q "danger" artifacts/mobile-app/tailwind.config.js

grep -q "warning" artifacts/mobile-app/tailwind.config.js

grep -q "success" artifacts/mobile-app/tailwind.config.js

grep -q "info" artifacts/mobile-app/tailwind.config.js

grep -q "from \"./components\"" artifacts/mobile-app/App.tsx

cd artifacts/mobile-app && npx tsc --noEmit

cd artifacts/mobile-app && pnpm test

cd artifacts/mobile-app && npx expo export --platform ios

Log MANUAL_PLAYTEST_REQUIRED items:

Visual playtest of component showcase on simulator

Tap-target check on physical device (deferred until Phase J or earlier device build)

COMMIT

Atomic commits per concern (section 1.9). Suggested split:

chore(mobile): add danger/warning/success/info color tokens

chore(mobile): install jest, jest-expo, testing-library

feat(mobile): add Screen, Card, Button primitives

feat(mobile): add TextField, Banner

feat(mobile): add SOSCard, CheckInOption

feat(mobile): add MessageBubble, NavBar

feat(mobile): add component barrel export

feat(mobile): showcase screen in App.tsx

test(mobile): render tests for all 9 components

Or fewer if logical groupings emerge during build. Do not bundle component implementation with test setup in a single commit.

Directive-Specific Repair Entries

MOBILE-4 — NativeWind class not applying to a component A1: Verify babel.config.js still has nativewind/babel preset and jsxImportSource. Verify global.css is imported at App.tsx top. Restart Metro cache with npx expo start -c. A2: Check that the className prop is being passed through (not consumed and dropped). For nested components, may need to merge classes via cn() utility or direct concatenation. DEFER: Log MEDIUM. Note which component is affected. Visual review will catch it.

MOBILE-5 — jest-expo preset fails to transform a node_module A1: Add the offending package to transformIgnorePatterns regex in jest.config.js. A2: Switch test to use a different approach (e.g., snapshot via expo export instead of @testing-library render) for that one component. DEFER: it.skip with reason. Log MEDIUM.

MOBILE-6 — Component shape conflict with Phase D consumer A1: This phase does not have a Phase D consumer yet. If the agent detects a prop shape that seems inadequate (e.g., MessageBubble lacks timestamp prop), log to BLOCKERS_FOR_MARCUS.md but build per spec. Do not improvise. A2: N/A — spec is source of truth for this phase. DEFER: Log to BLOCKERS_FOR_MARCUS.md and continue per spec.

Deferred-issues format: AUTONOMY_LAYER.md section 4 BUILD_REPORT format: AUTONOMY_LAYER.md section 5 Hard stops: AUTONOMY_LAYER.md section 6

GO

Begin Phase B pre-flight per AUTONOMY_LAYER.md section 3.

Credentials preflight scope: gh.

Cut branch from main: feat/mobile-phase-b-component-kit

Create docs/run-notes/session-YYYY-MM-DD-mobile-phase-b-plan.md and append to AUTONOMOUS_RUN_LOG.md at repo root.

Open PR titled: [Mobile] Phase B: Internal component kit + showcase Do not auto-merge. Stop after PR is open.
