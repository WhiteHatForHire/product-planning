---
title: "Initial prompt"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/Initial prompt.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Initial prompt

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Initial prompt

Build a recovery check-in web app. Stack: Node.js, Express, OpenAI JS SDK, plain HTML/CSS/JS.

SETUP

- npm install express openai

- Load OpenAI key from process.env.OPENAI_API_KEY

- Single entry point: server.js

- Serve frontend as static files from /public

BACKEND: POST /api/checkin

- Validate all required fields. Return 400 if missing or out of range.

- If OPENAI_API_KEY missing, return 500 with message: “API key not configured.”

- Build prompt from inputs and call OpenAI Chat Completions (NOT Responses API):

const completion = await openai.chat.completions.create({

model: “gpt-4o-mini”,

messages: [

{ role: “system”, content: SYSTEM_PROMPT },

{ role: “user”, content: buildUserPrompt(body) }

]

});

- Parse response as JSON. Return parsed object to frontend.

- Return 500 with generic message on any OpenAI failure. Never expose stack traces.

SYSTEM PROMPT (exact):

“You are a calm, practical recovery check-in coach. Be concise, non-shaming, and action-oriented. Respond ONLY with valid JSON, no markdown, no explanation, in this exact shape:

{

"stateSummary": "one or two sentence read of current state",

"attentionLevel": "low|medium|high",

"nextActions": ["action 1", "action 2", "action 3"],

"groundingReminder": "one short grounding line"

}”

USER PROMPT (built from inputs):

Mood: ${mood}/10

Energy: ${energy}/10

Craving: ${craving}/10

Focus: ${focus}/10

Sober today: ${soberToday}

Meeting attended: ${meetingAttended}

Grateful for: ${grateful}

Notes: ${notes}

DATABASE SCHEMA NOTE (no database in V1, but when added later, include these columns):

user_id, mood, energy, craving, focus, sober_today, meeting_attended, grateful, notes, state_summary, attention_level, next_actions, grounding_reminder, created_at

FRONTEND FORM (public/index.html)

Fields:

- mood: slider 1-10 with live numeric display

- energy: slider 1-10 with live numeric display

- craving: slider 1-10 with live numeric display

- focus: slider 1-10 with live numeric display

- sober_today: toggle or radio yes/no

- meeting_attended: toggle or radio yes/no

- grateful: short text input, optional, placeholder “One thing you’re grateful for today”

- notes: textarea, optional, max 1000 chars, placeholder “Context, triggers, wins, concerns”

- submit button

LOADING STATE

Show a visible loading indicator while awaiting response. Disable submit button during request.

RESULTS CARD

After response, show a card with four clearly labeled sections:

1. “Where you’re at” — stateSummary

1. “Something to watch” — attentionLevel rendered as a colored dot (green/yellow/red) with text “low / moderate / elevated” (not the raw value)

1. “Next moves” — nextActions as a simple list

1. “Remember” — groundingReminder in italics

Include a “Check in again” button that clears the card and resets the form.

DESIGN

- Single column, mobile-first

- Dark background, clean typography

- Large tap targets on sliders and toggles

- No wellness branding, no gradients, no icons

- Readable at arm’s length on a phone screen

ERROR HANDLING

- Show user-facing error messages inline (not alerts)

- Missing key: “The app isn’t configured yet. Add your API key.”

- API failure: “Something went wrong. Try again in a moment.”

- Validation failure: “Please fill in all required fields.”

Run as a persistent web server suitable for Replit preview.

When the app requires an API key, prompt me to add it to Replit Secrets rather than hardcoding it.
