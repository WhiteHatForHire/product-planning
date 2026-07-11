---
title: "Practice Mirror"
status: build-candidate
privacy: working
tags:
  - product-candidate
  - rehearsal
  - social
  - ai
  - phronetics
---

# Practice Mirror

## One-line concept

Practice Mirror is an AI rehearsal room for hard conversations, social moves, interviews, sales calls, apologies, pitches, dates, sponsor calls, and emotionally loaded moments.

## Naming note

The imported archive also contains a MIDI music-coaching concept called Practice Mirror at `products/parked/other-ip/practice-mirror.md`. This folder is the current canonical candidate for the conversation-rehearsal product. The older MIDI concept should remain preserved as source material unless the name is later reassigned.

## Core thesis

People do not only need advice. They need practice before the moment arrives.

Practice Mirror lets the user define an upcoming situation, choose the other person's likely stance, rehearse the conversation, get scored on clarity and judgment, and leave with a better next attempt.

The strongest version is not a generic chatbot. It is a simulator with roles, stakes, success criteria, emotional dynamics, and post-run critique.

## MVP

### Session setup

The user enters:

- Situation
- Person or role they are speaking to
- Desired outcome
- Constraints
- What they are afraid of
- What they should not say
- Tone target

### Practice modes

- Hard conversation
- Interview
- Sales or client call
- Apology
- Boundary setting
- Asking for help
- Sponsor or recovery call
- Founder pitch
- Dating or social invitation

### Live session

- AI plays the counterpart
- User responds by text first, voice later
- AI stays in role and does not break character unless paused
- User can ask for a pause, hint, or reset
- Session has visible goal, stakes, and current emotional temperature

### After-action review

The app returns:

- What worked
- What weakened the user's position
- Missed opportunities
- Stronger phrasing
- Emotional read
- Risk flags
- One drill to repeat
- A cleaner final script

## Product shape

Main screen:

- Scenario selector
- Setup form
- Role card for counterpart
- Conversation window
- Goal/stakes panel
- Pause and coach controls

Review screen:

- Scorecard
- Transcript highlights
- Rewritten best pass
- Recommended next repetition

## AI architecture

Practice Mirror should split the AI roles:

- Scenario designer: turns the user's setup into roles, stakes, success criteria, and failure modes.
- Counterpart actor: plays the other person in the live simulation.
- Coach: reviews transcript after the run and gives concrete feedback.
- Script polisher: produces a concise version the user can actually say.

The counterpart actor should not coach during the run. The coach should not roleplay. This separation keeps the product from becoming mushy.

## Guardrails

- No manipulation coaching for coercion, stalking, harassment, threats, or evading consent.
- For legal, medical, employment, or crisis contexts, provide rehearsal and wording help, not authoritative professional advice.
- Do not claim to know what a real person will feel or do.
- Encourage directness, consent, and repair where appropriate.
- Let the user export or delete sensitive sessions.

## Why it fits

This connects directly to phronetics: practical judgment under pressure. It also pairs with Friend CRM, Anchor, career planning, and Symposium OS.

## Build priority

High. This is one of the cleanest new candidates because it has a tight MVP, obvious demos, strong emotional utility, and a clear AI-native reason to exist.
