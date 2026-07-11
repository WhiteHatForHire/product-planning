# Practice Mirror - Start Here

## Product

Practice Mirror is an AI rehearsal room for hard conversations. It lets a user set up a real situation, rehearse against an AI counterpart, pause for coaching, and get a concrete after-action review.

This is the conversation-rehearsal candidate, not the older MIDI music-coaching concept preserved in `products/parked/other-ip/practice-mirror.md`.

## MVP goal

Build one polished web app where the user can:

- Define a scenario.
- Select a mode.
- Rehearse by text.
- Pause for coaching.
- Complete a session.
- Receive a review and better script.

Voice can wait. Text is enough for the first demo.

## Core product rule

Separate AI roles:

- Scenario designer creates roles, stakes, success criteria, and failure modes.
- Counterpart actor stays in role during the live conversation.
- Coach reviews after the run.
- Script polisher turns lessons into words the user can actually say.

Do not let the live counterpart turn into a generic advice chatbot.

## First build

Use a simple stack:

- Next.js or Vite React.
- Server-side AI calls.
- Local session persistence.
- No auth for the first demo.
- Seed scenarios for hard conversation, interview, sales call, apology, and sponsor call.

## Non-negotiables

- No coercion coaching.
- No harassment/stalking support.
- No legal/medical/employment authority claims.
- No pretending to know a real person's mind.
- The user can stop, reset, or delete a session.

## MVP success test

The demo works when the user can run a five-minute scenario and leave with:

- clearer wording
- a better read on risks
- one drill to repeat
- one final script

