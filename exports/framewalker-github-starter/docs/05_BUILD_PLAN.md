# Build Plan

## Phase 0: Static Prototype

Goal: Make the screen feel right before AI.

Build:

- static chapter screen
- placeholder image
- mission card
- HP/Mana bars
- inventory
- conditions
- narration
- input
- debug panel shell

Acceptance:

- user can see what the game is within 10 seconds
- UI feels like a cinematic adventure frame, not a dashboard

## Phase 1: Deterministic Engine

Goal: Make state real.

Build:

- initial state
- action primitive enum
- rule reducer
- state delta
- mission win/loss checks
- fixture actions

Acceptance:

- tests prove victory route
- tests prove alarm failure
- tests prove death failure
- tests prove captain-killed failure

## Phase 2: Parser Stub Then LLM Parser

Goal: Natural input maps to primitives.

Build:

- keyword parser fallback
- LLM parser route
- confidence and clarification handling

Acceptance:

- fixture inputs parse into expected actions
- low-confidence input asks clarification

## Phase 3: Narrator

Goal: Consequences feel alive but constrained.

Build:

- allowed facts generator
- narrator prompt
- fallback narration
- NPC line support

Acceptance:

- narrator does not invent new items/exits/win conditions
- narration reflects state changes

## Phase 4: Image Prompt Generator

Goal: Tech demo visual pipeline.

Build:

- frame type selection
- image prompt generator
- negative prompt
- prompt display in debug
- optional image API integration

Acceptance:

- prompts include continuity anchors
- prompts exclude text/UI/logos
- major frame states produce distinct prompts

## Phase 5: Polish Pass

Goal: Make it demo-ready.

Build:

- tighten UI
- add restart
- add transcript/history
- tune chapter rules
- tune prompts
- write README

Acceptance:

- 5-minute demo path works
- one win, one death, one alarm failure can be shown

