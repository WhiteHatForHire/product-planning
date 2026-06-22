---
title: "Anchor Mobile — Phase F Chat Screen"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/Anchor Mobile — Phase F_ Chat Screen.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor Mobile — Phase F Chat Screen

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile — Phase F: Chat Screen

Apply AUTONOMY_LAYER.md before executing. Phase E must be merged to main before Phase F starts.

Surfaces:          artifacts/mobile-app/app/chat/ (new)

artifacts/mobile-app/lib/api.ts (extend with chat)

Production impact: none (mobile reads existing API; backend prompts unchanged)

Council of Models: no (no new prompt fragments — backend handles)

Auto-merge:        no

Credentials:       gh

Agent:             CC Local (real chat testing)

Role

Port the Anchor web chat to iOS. Same backend, same system prompt, same crisis classifier. Mobile renders MessageBubble components for user and assistant turns, sends to the existing /api/chat endpoint, handles streaming or non-streaming response based on spec-reality. Renders crisis card when backend returns crisis routing. Session persistence: conversation restored on app re-open (existing backend pattern).

Deployment Posture

Auto-merge: no — safety surface (chat is the primary AI-user interface). Council of Models: no — no prompt fragments modified. Mobile is rendering backend output only.

Design Data

API endpoints

POST /api/chat

Body: { messages: [{ role, content }], conversation_id? }

Returns: streaming or JSON depending on spec-reality

Response includes crisis routing fields if classifier fires

GET /api/chat/sessions/current

Returns: { conversation_id, messages: [...] }

Used to restore the active conversation on chat open

POST /api/chat/new

Returns: { conversation_id }

Clears the active conversation

Confirm endpoint shapes via spec-reality reconciliation. Read web chat client.

Streaming vs non-streaming

If web uses streaming (Server-Sent Events or chunked): mobile uses EventSource polyfill or react-native-sse.

If web uses non-streaming JSON: mobile uses plain fetch.

Adopt whatever web does. Do not invent a third path. Install:

npx expo install react-native-sse   # only if streaming

Layout

artifacts/mobile-app/app/chat/index.tsx

Screen, NOT scrollable=true (FlatList handles scroll):

NavBar

title: "Chat"

leftAction: { label: "Back", onPress: router.back() }

rightAction: { label: "New", onPress: confirm + new conversation }

Message list (FlatList, inverted)

Renders MessageBubble per message

Auto-scrolls to bottom on new message

Loading dots row when assistant is responding

Input bar (sticky to bottom, KeyboardAvoidingView wrapper)

TextField-like input (multiline, autoGrows up to 4 lines)

Send Button (primary, icon-less, label "Send")

Disabled while assistant is responding

Crisis branch

If backend response indicates crisis (same flag as Phase E):

Render the CrisisCard at the top of the screen, above the FlatList

Hide the input bar (do not allow further messaging while crisis card visible)

Show resource buttons (988, SAMHSA, etc. from backend response)

"Dismiss" button on crisis card returns to chat input only after explicit tap

"New conversation" confirmation

Tapping rightAction shows a confirmation:

Title: "Start a new conversation?"

Body:  "Your current chat will be saved but no longer visible."

Cancel: "Cancel"

Confirm: "Start new"

Use Alert.alert from react-native (system dialog).

Session restore on chat open

On mount:

Call GET /api/chat/sessions/current

If conversation exists: load messages into state

If empty: show static opener (web pattern — read web for exact opener text)

Static opener (verbatim from web)

Read web app for exact opener line. Likely something like:

"How are you feeling right now?"

Do not invent. Read web and match exactly.

Acceptance Criteria

AUTOMATED

Chat screen renders message list

Send button submits to mocked API

Response messages append to list

Crisis response renders CrisisCard and hides input

New conversation flow with Alert.alert

Session restore renders prior messages

Typescript passes

expo export passes

HUMAN_REVIEW

Streaming feels responsive (MANUAL_PLAYTEST_REQUIRED)

Keyboard avoidance works (MANUAL_PLAYTEST_REQUIRED)

Auto-scroll behavior (MANUAL_PLAYTEST_REQUIRED)

Crisis branch on real veiled language (MANUAL_PLAYTEST_REQUIRED)

Session restore across app cold launch (MANUAL_PLAYTEST_REQUIRED)

Phase F Execution

PRE-FLIGHT

Standard. Confirm Phase E merged. Cut feat/mobile-phase-f-chat.

Spec-reality reconciliation:

Read web chat client for streaming pattern

Read web /api/chat handler for request/response shape

Read web crisis card rendering logic

Read static opener verbatim

SMOKE ASSERTIONS

Message rendering (mocked list of mixed user/assistant turns)

Send submits to API

Crisis response branch

New conversation clears state

Session restore loads messages

IMPLEMENTATION

Chat client (lib/api.ts extension)

Chat screen with FlatList

Input bar with keyboard avoidance

Send + response handling (streaming or non-)

Crisis branch

New conversation flow

Session restore

COMMIT

Atomic per concern.

Directive-Specific Repair Entries

MOBILE-14 — Streaming truncates or stalls A1: Verify react-native-sse is installed and chunks are being parsed. A2: Fall back to non-streaming JSON. Log SPEC_REALITY_DELTA: "Mobile uses non-streaming; web uses streaming. Adapt later." Continue. DEFER: MEDIUM. Non-streaming works for V1.

MOBILE-15 — Crisis card not rendering despite backend flag A1: Verify the response parsing extracts crisis === true. Check whether backend nests it as crisis or crisis_response.active or similar. A2: Log SPEC_REALITY_DELTA. Adapt parser to actual shape. DEFER: HARD STOP — safety regression.

GO

Begin Phase F pre-flight. Cut branch: feat/mobile-phase-f-chat. PR title: [Mobile] Phase F: Chat with crisis routing and session restore No auto-merge.
