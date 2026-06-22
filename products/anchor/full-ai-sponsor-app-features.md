---
title: "Full AI sponsor app features"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/Full AI sponsor app features.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Full AI sponsor app features

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Overview spec

ANCHOR — V3 PRODUCT SPEC

Recovery Companion App — Post V2D Vision

-----

NORTH STAR DESIGN PRINCIPLE

The app should reduce isolation and increase wise action, not merely provide comforting conversation.

Every meaningful interaction should end in either a concrete action, a human contact step, or both.

This is not a sealed AI cocoon. It is a bridge back to reality.

-----

WHAT THIS IS

Anchor is a recovery companion app with persistent memory, voice input, daily check-ins, sponsor-adjacent conversation, and proactive outreach.

It is not a replacement sponsor.

It does not have lived sobriety, moral authority earned through suffering, or human presence.

What it has:

- Memory across time

- Availability at 3am

- No judgment

- Pattern recognition

- Action bias

- The ability to shorten the distance between dysregulation and wise action

The healthiest framing:

Not “AI instead of a sponsor.”

“AI to help you get back to wise action and real human contact faster.”

-----

CRISIS POSTURE

This must be stated plainly because it shapes dozens of design decisions downstream.

What this app is not:

- Not a crisis intervention service

- Not a mental health emergency resource

- Not a substitute for professional care

- Not equipped to handle acute psychiatric emergencies

What this app must do in high-risk moments:

- Detect elevated risk signals in check-in data and conversation

- Immediately surface human contact options — sponsor, fellow, crisis line

- Never stay in AI conversation mode when someone is in genuine crisis

- Route toward real contact every time, without exception

- Display 988 Suicide and Crisis Lifeline in any session where suicidal ideation is expressed

- Display SAMHSA National Helpline (1-800-662-4357) as a persistent resource in Settings

Design rule derived from this:

- The app should never be the last line of support

- At moderate or high risk: at least one human contact shortcut must be visible

- At crisis level: AI response stops, human contact options fill the screen

- Every AI prompt must include instructions to escalate to human contact at crisis signals

This is not a legal disclaimer. It is a product design commitment.

-----

PRODUCT PILLARS

1. Persistent layered memory — it knows you over time

1. Sponsor-adjacent conversation — real back and forth, not just a form

1. Commitment and follow-up loop — reflection must end in action

1. Human handoff — always routes toward real contact at elevated risk

1. Voice input — speak when typing is too much

1. Proactive outreach — it reaches out, not just the other way around

1. User memory control — see, edit, and trust what it remembers

-----

PILLAR 1: PERSISTENT LAYERED MEMORY

Three memory layers stored in the database and injected into every AI call.

Layer 1 — Stable Profile

What tends to stay true. Updated infrequently, user can edit directly.

- What they are in recovery from

- Sobriety dates and tracker names

- Known recurring triggers

- Preferred support style

- Trusted people and resources

- Saved sober contacts (name + phone)

- Saved meeting links

- Recurring commitments

- Personal boundaries and preferences

- Anything the user pins as important

Layer 2 — Recent State Summary

Last 7 to 30 days. Auto-updated after every check-in via a lightweight summarization call.

- Average mood, craving, energy, sleep

- Current pressure points and themes

- Recent trigger patterns

- Wins and resets

- Commitments made and whether followed through

- Missed check-in clusters

Layer 3 — Event Log

Clear factual timestamped events. Never compressed, always readable.

- Tracker resets with notes

- Major wins the user flagged

- Commitments made and outcomes

- Missed check-in streaks

- Notable chat sessions summarized in one line

- Sobriety milestones

Technical approach:

- Three database columns: stable_profile (jsonb), recent_summary (text), event_log (jsonb array)

- After every check-in: run a background summarization call to update recent_summary

- Inject all three layers into every AI system prompt in compressed form

- Keep total injected memory under 1500 tokens

- User can view all three layers in a Memory screen under Settings

-----

PILLAR 2: SPONSOR-ADJACENT CONVERSATION

A dedicated Chat tab for real back-and-forth conversation at any time.

What you can do in chat:

- Talk through a craving in real time

- Process a difficult situation

- Ask for a step or tradition reflection

- Get accountability on a commitment

- Just check in verbally without filling out the form

- Say “I’m about to relapse” and get an immediate response

Conversation behavior:

- Sponsor has access to all three memory layers

- Responds in a consistent tone: calm, plain-speaking, warm, direct, non-shaming

- References what the user actually shared — no generic responses

- Varies language — never repeats clichés

- Occasionally asks one short reflective question

- Always ends with either a concrete action or a human contact suggestion

- Never becomes purely soothing without routing toward action or contact

Tone definition (not a character, a disciplined support mode):

- Calm, not clinical

- Honest, not harsh

- Action-oriented, not advice-giving

- Recovery-literate, not wellness-generic

- Humble about its role and limitations

Crisis handling:

- If user expresses suicidal ideation, crisis, or imminent relapse:

- Respond with direct care

- Immediately surface human contact options: call sponsor, call a fellow, crisis line

- Do not stay in chat mode — route to real contact

- Include crisis line: 988 Suicide and Crisis Lifeline

Technical approach:

- POST /api/chat endpoint

- Conversation history maintained in frontend state per session

- System prompt injects all three memory layers plus last check-in

- gpt-4o-mini for cost efficiency

- Session summary saved to event log after conversation ends

- Conversation history resets daily unless user opts to continue

-----

PILLAR 3: COMMITMENT AND FOLLOW-UP LOOP

After every check-in or chat session the app should not just say useful things. It should help the user choose one concrete next action and then follow up on it.

How it works:

- At the end of every check-in result card: “What’s your one next move?”

- Show 3-5 suggested actions based on the AI output plus a free text option

- Example actions: text a sober person, drink water and eat, go for a walk, open the meeting link, go to bed now, call your sponsor, delete the app for tonight, shower and leave the room

- User taps one or types their own

- Commitment is saved with timestamp

Follow-up:

- At a configurable time later that day (default 4 hours), send a push notification or in-app prompt: “Did you do it?”

- Three response options: Yes, Not yet, Need a smaller version

- If “Not yet” or “Need a smaller version”: offer a scaled-down version of the same action

- If “Yes”: brief acknowledgment, log it as completed in the event log

- Commitment completion rate visible in Insights

One-tap action shortcuts for elevated risk:

- If risk level is high: surface these shortcuts immediately on the result card

- Text [saved sober contact name]

- Call [saved sober contact name]

- Open [saved meeting link]

- “Tell on myself” — pre-written message template the user can send to their sponsor

-----

PILLAR 4: HUMAN HANDOFF

The most important ethical design principle in the product.

At elevated risk states the app always routes toward real human contact. It never becomes the endpoint.

Human contact features:

- Saved sober contacts stored in stable profile (name + phone number)

- One-tap text shortcut to saved contacts from result card and chat

- One-tap call shortcut

- Saved meeting links (user adds in Settings)

- “Tell on myself” message template — brief honest message the user can send to their sponsor with one tap

- Template example: “Hey. Having a hard time right now. Craving is up. Just telling on it.”

Design rule:

- Any result card with moderate or high attention level must surface at least one human contact shortcut

- Chat responses at elevated risk must include a human contact suggestion before ending

- The app should never be the only suggested resource

-----

PILLAR 5: VOICE INPUT

Give the user a microphone button so they can speak instead of type.

Where voice input appears:

- Notes field on check-in form

- Grateful field on check-in form

- Chat input field

How it works:

- User taps microphone button, speaks, taps again to stop

- Uses OpenAI Whisper API for transcription

- Transcribed text appears in the field for review before submitting

- Works on mobile web via MediaRecorder API

- Graceful fallback to text input if mic permission denied or unavailable

Voice output (text to speech) — defer to later:

- TTS is cool but less essential than voice input

- Voice input lowers friction in live activated states

- TTS is a polish feature — add after V3D

- When added: use OpenAI TTS API, “onyx” voice, only read reminder and sponsor note sections

Cost at personal scale:

- Whisper: $0.006 per minute — essentially free

- TTS when added: $0.015 per 1000 characters — essentially free

-----

PILLAR 6: PROACTIVE OUTREACH

The sponsor reaches out. The user does not always have to initiate.

Daily check-in reminder:

- Email sent at user-configured time each day

- If no check-in logged by that time, send a gentle nudge

- One-line prompt from the sponsor referencing recent patterns

- Example: “You haven’t checked in yet today. Your sleep has been low this week — how are you doing?”

Missed check-in follow-up:

- If user misses 2 or more days: warmer tone

- “Haven’t heard from you in a couple days. No pressure. Just checking in.”

Weekly summary email:

- Sent Sunday evening or Monday morning

- Contains: check-in streak, average mood and craving for the week, sobriety tracker status, one sponsor observation

- Plain text, not a newsletter

- One suggested focus for the coming week based on patterns

Commitment follow-up:

- If a daily commitment was logged and not marked complete: follow up via in-app notification at configured time

Technical approach:

- Use Resend or SendGrid free tier for email

- User sets email address and reminder time in Settings

- Node-cron job runs daily to check for missing check-ins and send reminders

- Weekly summary generated by OpenAI from recent_summary memory layer

- Push notifications via Web Push API for in-app follow-ups (PWA only)

WhatsApp — defer:

- Possible via Twilio but adds complexity and cost

- Defer until email is proven useful and used consistently

-----

PILLAR 7: USER MEMORY CONTROL

The user must be able to see and control what the app remembers. Without this, memory feels creepy or brittle over time.

Memory screen in Settings:

- View stable profile — all stored facts about the user

- Edit any field in the stable profile

- Pin a fact as important (will always be included in AI context)

- Delete any specific memory

- View recent state summary — the compressed last 30 days

- View event log — timestamped list of notable events

- Pause memory for one conversation (app will not inject memory into that session)

- Full memory reset option — clears all three layers but preserves raw check-in data

-----

ONBOARDING AS SPONSOR INTAKE

First time the app opens, instead of a simple setup flow, the user goes through a sponsor intake conversation.

The sponsor introduces itself and asks:

- What are you in recovery from?

- How long have you been sober? (sets initial tracker)

- What’s your biggest challenge right now?

- What does support look like for you?

- Who are your sober contacts? (save up to 3 names and numbers)

- Do you have regular meeting links? (save them now)

- What time do you want your daily check-in reminder?

- What’s your email for your weekly summary?

Responses populate the stable profile immediately.

Sponsor references this context in every future interaction.

Onboarding can be returned to and updated in Settings at any time.

-----

FULL SCREEN MAP

Tab 1: Home

- Sobriety counters (live)

- Today’s check-in status

- Latest sponsor note or pattern observation

- Active commitment for today with follow-up status

- Quick access to Chat and Check-In

- Human contact shortcuts if risk was elevated yesterday

Tab 2: Check-In

- Full and quick check-in (existing system)

- Voice input on notes and grateful fields

- Commitment selection at end of result card

- Human contact shortcuts on elevated result

Tab 3: Chat

- Full sponsor conversation

- Voice input

- Memory-aware responses

- Human handoff shortcuts always visible

- Session summary saved after conversation

Tab 4: Progress

- Check-in history (existing)

- Charts: mood, craving, energy, sleep, focus (existing)

- Calendar heatmap (existing)

- Streak stats (existing)

- Commitment completion rate

- Recovery habit frequency

Tab 5: Trackers

- Sobriety tracker system (existing)

- Reset history

Settings:

- Memory screen (view, edit, pin, delete)

- Saved sober contacts

- Saved meeting links

- Email and reminder time

- Commitment follow-up timing

- Voice preferences

- Export data

- Reset onboarding

- App version

-----

TECHNICAL STACK

Keep:

- Node.js + Express

- PostgreSQL

- OpenAI gpt-4o-mini for chat and check-ins

- Existing frontend

Add:

- OpenAI Whisper API for voice input

- Resend or SendGrid for email

- Node-cron for scheduled outreach

- Web Push API for in-app notifications (PWA)

- Three-layer memory schema in database

Defer:

- OpenAI TTS (voice output)

- Twilio / WhatsApp

- Native iOS or Android

- Therapist portal

- Social features

-----

BUILD ORDER

V3A — Memory system and intake

- Three-layer memory database schema

- Sponsor intake onboarding conversation

- Memory injected into all AI calls

- Memory controls screen in Settings

- Responses immediately feel longitudinal and personal

V3B — Chat interface

- Dedicated Chat tab

- Full conversation with sponsor

- Memory-aware, action-ending responses

- Human handoff shortcuts in chat

- Text input first

V3C — Commitment and follow-up loop

- Commitment selection after every check-in and chat

- Follow-up notification system

- Human contact shortcuts on elevated risk

- Saved contacts and meeting links in Settings

V3D — Voice input

- Whisper API integration

- Microphone button on notes, grateful, and chat fields

- Mobile web MediaRecorder implementation

V3E — Proactive outreach

- Daily reminder emails

- Missed check-in follow-ups

- Weekly summary email

- User sets email and reminder time

V3F — Polish and TTS

- Text to speech on sponsor responses

- Onboarding refinement

- Transition animations

- Full UX audit

-----

SUCCESS CRITERIA

Not vanity metrics. Behavioral ones.

The product is working if:

- Daily check-in consistency increases over time

- Follow-through rate on one concrete action per day is above 50%

- Contact with sober people or meetings increases or stays consistent

- Missed check-in drift decreases — fewer multi-day gaps

- Sobriety tracker resets decrease over time

- The user reports feeling more guided into action, not just more soothed

- The user reaches for the app before reaching for the behavior

The product is failing if:

- The user feels comforted but takes no action

- The app replaces human contact instead of increasing it

- The user avoids real sponsors or fellows because the app feels easier

- Check-ins become performative rather than honest

- The user opens the app during cravings but does not call anyone or go anywhere

These criteria should be reviewed personally every 30 days during V3 development.

-----

WHAT THIS IS NOT

- Not a replacement for a human sponsor

- Not a therapy app

- Not a crisis intervention service

- Not a social platform

- Not a gamified wellness product

- Not a sealed comfort loop

-----

WHAT THIS COULD BECOME

After V3 is complete this is a genuinely differentiated product.

A persistent recovery companion that knows your history, speaks plainly, reaches out when you go quiet, helps you choose the next right action, and always points back toward real human contact.

That is a real product. That is something people in recovery would actually use.

The check-in system is the foundation.

The memory is the relationship.

The action bias is the ethics.

The human handoff is the soul.

V3A patch

# V3A REVISION PATCH

Apply these targeted fixes to the already-running V3A implementation.

Do NOT rebuild from scratch. Do NOT touch any existing UI or functionality.

Make only the changes listed below. Report exactly what was changed.

-----

CONTEXT

V3A has already been deployed. The following patches address:

1. Summarization running too frequently (performance)

1. Missing last_checkin_local_date field (required by V3E scheduler)

1. Onboarding step count ambiguity (lock at 9)

1. Confirm shared helper functions exist for downstream phases

-----

PATCH 1: REDUCE BACKGROUND SUMMARIZATION FREQUENCY

Current behavior: recent_summary regenerates after every check-in.

Problem: On daily check-in habits, this summarizes nearly identical data every day.

Find the background summarization logic in the check-in handler.

Replace it with this condition:

Only trigger background recent_summary regeneration if the event_log

has accumulated 3 or more new entries since the last summarization.

To track this, add a field to user_memory:

last_summarized_at_event_count integer default 0

Add this column to the user_memory table if it does not exist:

ALTER TABLE user_memory ADD COLUMN IF NOT EXISTS last_summarized_at_event_count integer default 0;

Logic after appending a new event_log entry:

1. Count current event_log length (array length).

1. Read last_summarized_at_event_count from user_memory.

1. If (current_length - last_summarized_at_event_count) >= 3:

- Run background summarization.

- On success, update last_summarized_at_event_count = current_length.

1. If fewer than 3 new entries, skip background summarization.

This reduces summarization from daily to roughly every 3 check-ins.

The V3E weekly summary cron will also update recent_summary from event_log.

Wrap background summarization in safeBackgroundTask() if that helper exists.

If not, wrap in the existing try/catch pattern.

-----

PATCH 2: ADD last_checkin_local_date TO user_memory

The V3E scheduler needs to know if the user checked in today without

querying the full check_ins table every 15 minutes.

Add this column to user_memory:

ALTER TABLE user_memory ADD COLUMN IF NOT EXISTS last_checkin_local_date varchar;

After every successful check-in, update this field:

- Compute the user’s local date using stable_profile.timezone.

- If timezone is missing or invalid, default to America/New_York.

- Store as a strict YYYY-MM-DD string.

- Update user_memory.last_checkin_local_date = userLocalDate.

Do this in the same place where event_log is appended after check-in.

Keep it in the same try/catch block — if it fails, log server-side and continue.

Do not block the check-in response on this update.

-----

PATCH 3: CONFIRM AND LOCK ONBOARDING AT 9 STEPS

Inspect the current onboarding implementation.

Confirm:

- Step count is 9 (includes recovery_program at step 5 and sobriety_why at step 6).

- Progress bar reads “Step X of 9” on all steps.

- All 9 steps save to stable_profile correctly.

If any step references “8 of 8” or similar, update the label to the correct step of 9.

Do not change the step content or order — only fix label strings if wrong.

If recovery_program and sobriety_why steps are missing:

- This is a more significant issue. Report it but do not attempt to add them

in this patch. Flag for manual fix before running V3B.

-----

PATCH 4: CONFIRM SHARED HELPERS EXIST

Inspect the codebase and confirm whether the following functions exist as

named, reusable functions (not just inline code blocks):

1. getCurrentUserId() — returns process.env.APP_USER_ID || “dev_user”

1. A memory loader (loads user_memory row safely with defaults)

1. A memory context builder (builds the injected memory block string)

1. An event log appender (loads, normalizes, appends, caps at 90, saves)

1. A risk classifier (returns strict JSON { risk: “low|moderate|high|crisis” })

For each one:

- If it exists as a named function: confirm it is used consistently. Report its location.

- If it exists only as inline code: extract it into a named helper in a shared file

(e.g., utils/v3helpers.js or similar). Update all call sites.

- If it does not exist: create it now.

These helpers MUST exist before V3B is run.

Requirements for each helper:

getCurrentUserId():

Returns: process.env.APP_USER_ID || “dev_user”

Never hardcodes “maxwell” or any other user ID.

loadUserMemory(userId):

Queries user_memory by user_id.

If no row exists, creates a default row with empty stable_profile,

empty recent_summary, and empty event_log array.

Returns the row. Never throws. Never returns null.

normalizeStableProfile(stableProfile):

Takes a stable_profile JSONB object (possibly partial or null).

Returns a complete object with all expected keys set to safe empty values:

recovery_focus: [], sobriety_start_dates: {}, known_triggers: [],

support_style: “”, recovery_program: “”, sobriety_why: “”,

sober_contacts: [], meeting_links: [], recurring_commitments: [],

pinned_facts: [], email: “”, reminder_time: “08:00”,

timezone: “America/New_York”, commitment_followup_hours: 4,

reminder_enabled: true, weekly_summary_enabled: true

Never returns null fields.

buildMemoryContext(userMemory, options):

Builds the memory injection string for AI system prompts.

options: { pauseMemory: bool }

If pauseMemory is true, returns an empty string.

If userMemory is missing or stable_profile is empty, returns an empty string.

Never includes phone numbers.

Keeps output under 1500 tokens.

Always includes pinned_facts first if they exist.

Format:

MEMORY CONTEXT:

Recovery focus: [values]

Recovery program: [value]

Sobriety why: [value]

Known triggers: [values]

Support style: [value]

Pinned facts: [values]

Sober contacts: [names only, no phone numbers]

Recent patterns last 30 days: [recent_summary, truncated if needed]

Recent events: [last 5 event_log entries as plain text]

appendEventLog(userId, event):

Loads current user_memory for userId.

Reads event_log. If missing or malformed, resets to [].

Appends the new event object.

Caps array at 90 entries (removes oldest).

Saves updated user_memory with updated_at = now().

Wraps everything in try/catch.

If anything fails, logs server-side.

Never throws. Never crashes the main request.

Event shape: { timestamp: “ISO8601”, type: string, summary: string }

classifyRisk({ source, input, history, memorySummary }):

source: “checkin” or “chat”

Calls gpt-4o-mini with the input.

Uses structured JSON output or JSON mode.

Returns strict JSON: { risk: “low” | “moderate” | “high” | “crisis” }

If parsing fails or value is outside enum: returns { risk: “moderate” }, logs server-side.

Never throws. Fallback is always { risk: “moderate” }.

Definitions (same for both sources):

low: normal, no acute risk

moderate: elevated distress or craving, no imminent danger

high: strong craving, relapse risk, severe dysregulation, may use soon

crisis: suicidal ideation, intent to harm self/others, overdose risk,

acute medical danger, immediate physical danger

Important: imminent relapse alone = high, not crisis.

-----

PATCH 5: CONFIRM PHONE NUMBER EXCLUSION FROM AI PROMPTS

Search the codebase for all locations where AI system prompts are built.

Confirm that sober_contacts phone numbers are never included in any AI prompt.

Contact names may appear. Phone numbers must not.

If any AI prompt includes phone numbers, remove them immediately.

Phone numbers may only appear in:

- Frontend handoff banners (rendered directly to the user)

- Crisis resource cards (rendered directly to the user)

- SMS/tel URI generation (user-facing only)

-----

REPORT AT THE END

When finished, report:

1. Whether last_summarized_at_event_count column was added

1. Whether summarization now triggers only on 3+ new events

1. Whether last_checkin_local_date column was added

1. Whether last_checkin_local_date updates after each check-in

1. Whether onboarding is confirmed at 9 steps (or flag if steps are missing)

1. Which shared helpers now exist as named functions and their file locations

1. Which helpers were created new vs. extracted from inline code

1. Whether phone numbers are confirmed absent from all AI prompts

1. Any issues found that require manual attention before V3B

1. Files changed

Do not run V3B until items 6 and 9 are resolved.

Architecture clean up pre V3B

# V3 SHARED ARCHITECTURE CLEANUP

Run this prompt BEFORE V3B.

Do NOT add any new product features.

Do NOT change any UI.

This is a codebase consolidation pass only.

-----

PURPOSE

V3B through V3F all depend on shared logic for memory loading, risk classification,

event logging, and human handoff. If each phase implements these separately, the

codebase becomes fragile and inconsistent.

This prompt ensures all shared infrastructure exists as named, reusable functions

before building on top of it.

-----

PRE-FLIGHT

Inspect the current V3A implementation and report briefly:

1. Current file structure

1. Whether each shared helper listed below already exists as a named function

1. Whether getCurrentUserId() is used consistently everywhere

1. Whether any user ID is hardcoded other than via getCurrentUserId()

1. Any schema issues found in user_memory or app_settings

Then proceed with the work below.

-----

GOAL: CREATE OR CONSOLIDATE THESE SHARED HELPERS

Place all helpers in a single shared file (e.g., utils/v3helpers.js).

Export each function individually.

Import them wherever needed.

Do not leave duplicate implementations in route files.

-----

1. getCurrentUserId()

Returns: process.env.APP_USER_ID || “dev_user”

Never hardcodes any user name.

Confirm it is imported and used at every location where user_id is referenced.

Remove any inline fallback patterns that duplicate this logic.

-----

1. loadUserMemory(userId)

Queries user_memory WHERE user_id = userId.

If no row exists: INSERT a default row with:

- stable_profile = default schema (see below)

- recent_summary = “”

- event_log = []

- last_summarized_at_event_count = 0

- last_checkin_local_date = null

Returns the row. Never throws. If database query fails, returns a safe in-memory default.

Default stable_profile shape:

{

“recovery_focus”: [],

“sobriety_start_dates”: {},

“known_triggers”: [],

“support_style”: “”,

“recovery_program”: “”,

“sobriety_why”: “”,

“sober_contacts”: [],

“meeting_links”: [],

“recurring_commitments”: [],

“pinned_facts”: [],

“email”: “”,

“reminder_time”: “08:00”,

“timezone”: “America/New_York”,

“commitment_followup_hours”: 4,

“reminder_enabled”: true,

“weekly_summary_enabled”: true

}

-----

1. normalizeStableProfile(stableProfile)

Takes any stable_profile object (possibly partial, null, or undefined).

Returns a complete object with all expected keys filled in with safe defaults.

Never returns null or undefined for any key.

Merges incoming values over defaults — does not overwrite valid values.

-----

1. buildMemoryContext(userMemory, options)

options: { pauseMemory: bool }

If pauseMemory is true: return “”

If userMemory is null/missing: return “”

If stable_profile is empty (all default values): return “”

Otherwise build and return this string:

MEMORY CONTEXT:

Recovery focus: [stable_profile.recovery_focus joined with comma]

Recovery program: [stable_profile.recovery_program]

Sobriety why: [stable_profile.sobriety_why]

Known triggers: [stable_profile.known_triggers joined with comma]

Support style: [stable_profile.support_style]

Pinned facts: [stable_profile.pinned_facts joined with newline, always first if present]

Sober contacts: [sober_contacts names only — no phone numbers, ever]

Recent patterns last 30 days: [recent_summary, truncated from end if needed]

Recent events: [last 5 event_log entries formatted as plain text one-liners]

Rules:

- Total output must stay under 1500 tokens (approximately 6000 characters)

- Truncate recent_summary from the end if needed to stay within limit

- NEVER include phone numbers in this output

- If a field is empty, omit that line from the output

-----

1. appendEventLog(userId, event)

event shape: { timestamp: “ISO8601”, type: string, summary: string }

Process:

1. Load user_memory for userId

1. Read event_log. If null/missing/malformed: reset to []

1. Append event

1. If array length > 90: remove oldest entries until length = 90

1. Save updated event_log to user_memory

1. Update user_memory.updated_at = now()

1. Wrap steps 1-6 in try/catch

1. On error: log server-side, do nothing else

1. Never throw. Never crash the calling request.

-----

1. classifyRisk({ source, input, history, memorySummary })

source: “checkin” | “chat”

input: the user’s current text (latest message or check-in notes)

history: array of recent messages if available, otherwise []

memorySummary: recent_summary string if helpful, otherwise “”

Process:

1. Build a classification prompt from input, history (last 4 turns max), and

a brief memorySummary excerpt (max 200 chars)

1. Call gpt-4o-mini with JSON mode or structured output

1. Require strict response: { “risk”: “low” | “moderate” | “high” | “crisis” }

1. Parse result

1. If parsing fails or value is outside enum: return { risk: “moderate” }, log server-side

1. Return parsed result

1. Wrap entire function in try/catch. On any error: return { risk: “moderate” }, log server-side

Classifier definitions (canonical — use these everywhere, no variations):

- low: normal interaction, no acute risk

- moderate: elevated emotional distress or craving, no imminent danger

- high: strong craving, relapse risk, severe dysregulation, may use/drink/act out soon

- crisis: suicidal ideation, intent to harm self, intent to harm others,

overdose risk, acute medical danger, immediate physical danger

IMPORTANT: Imminent relapse alone = high, NOT crisis.

Crisis is reserved for self-harm, harm to others, overdose, medical danger,

or immediate physical danger.

-----

1. buildHandoffPayload(stableProfile)

Returns:

{

“contacts”: [ { “name”: “…”, “phone”: “…” } ],

“meeting_links”: [ { “label”: “…”, “url”: “…” } ],

“tell_on_myself_message”: “Hey. Having a hard time right now. Just telling on it.”

}

Reads sober_contacts and meeting_links from stableProfile.

If contacts or links are missing/malformed, returns safe empty arrays.

This payload is for FRONTEND RENDERING ONLY.

Phone numbers in this payload are for tel: URI buttons — NOT for AI prompts.

Never pass this payload directly into an AI system prompt.

-----

1. safeBackgroundTask(label, asyncFn)

Takes a label string and an async function.

Runs asyncFn asynchronously after the current request returns.

Wraps in try/catch.

On error: logs label + error message server-side.

Never throws. Never creates unhandled promise rejections.

Never blocks the main request/response cycle.

Usage pattern:

safeBackgroundTask(“regenerate_summary”, async () => {

// background work here

});

-----

V3 INVARIANTS CONFIRMATION

After creating the helpers, confirm these invariants hold throughout the codebase:

1. getCurrentUserId() is used at every user_id reference — no hardcoded IDs

1. stable_profile is the single source of truth for all user preferences:

email, reminder_time, timezone, commitment_followup_hours,

reminder_enabled, weekly_summary_enabled

1. app_settings stores only: onboarding_version, migration flags, and

email send-tracking dates (last_daily_reminder_sent_date, etc.)

1. Phone numbers never appear in any AI prompt, only in frontend payloads

and crisis resource cards

1. event_log cap is 90 entries — applied consistently in all appends

1. All background async operations use safeBackgroundTask or equivalent

1. No unhandled promise rejections exist in the codebase

Search the codebase for any violation of these invariants and fix them.

-----

DO NOT:

- Change any UI

- Change any routes (only refactor inline logic into helpers)

- Change database schema (unless repairing a V3A bug)

- Add any product features

- Remove any existing functionality

-----

REPORT AT THE END

1. All helpers created or confirmed, with file location

1. Which helpers were newly created vs. extracted from inline code

1. List of call sites updated to use shared helpers

1. Whether all V3 invariants are confirmed

1. Any issues found that need attention before V3B

1. Files changed

V3A

# V3A

Upgrade the existing recovery check-in app to V3A only.

Important constraints:

- Do NOT build chat, voice, outreach, or commitment loop yet

- Focus only on the three-layer memory system, sponsor intake onboarding,

memory injection, crisis-safe AI handling, and memory controls

- Extend what exists

- Do not rebuild from scratch

- Keep all existing dark theme, UI, and functionality intact

- This is a no-auth development fork, so do not assume production multi-user security yet

- Do not scatter a hardcoded user ID throughout the codebase

-----

PRE-FLIGHT REQUIREMENT

Before making changes, inspect the existing app structure and database usage.

Return briefly in the Replit chat:

1. Current app structure

1. Current database tables and columns you detect

1. Files you expect to modify

1. Any risks or conflicts with this V3A spec

1. A short implementation plan

Then proceed with implementation.

-----

USER ID RULE

Create one helper function:

getCurrentUserId()

For now, because auth is disabled, it should return:

process.env.APP_USER_ID || “dev_user”

Use this helper everywhere user_id is needed.

Do NOT hardcode “maxwell” throughout the app.

-----

V3 SHARED HELPERS

Create a shared utilities file (e.g., utils/v3helpers.js) and implement

the following named helper functions. These will be reused by all future

V3 phases. Do not implement them as inline code only.

1. getCurrentUserId()

Returns: process.env.APP_USER_ID || “dev_user”

1. loadUserMemory(userId)

Queries user_memory by user_id.

If no row exists, creates a default row with empty stable_profile,

empty recent_summary, and empty event_log array.

Returns the row. Never throws. Never returns null.

1. normalizeStableProfile(stableProfile)

Takes a stable_profile JSONB object (possibly partial or null).

Returns a complete object with all expected keys set to safe empty values:

recovery_focus: [], sobriety_start_dates: {}, known_triggers: [],

support_style: “”, recovery_program: “”, sobriety_why: “”,

sober_contacts: [], meeting_links: [], recurring_commitments: [],

pinned_facts: [], email: “”, reminder_time: “08:00”,

timezone: “America/New_York”, commitment_followup_hours: 4,

reminder_enabled: true, weekly_summary_enabled: true

Never returns null fields.

1. buildMemoryContext(userMemory, options)

Builds the memory injection string for AI system prompts.

options: { pauseMemory: bool }

If pauseMemory is true, returns an empty string.

If userMemory is missing or stable_profile is empty, returns empty string.

Never includes phone numbers in the output.

Keeps output under 1500 tokens.

Always includes pinned_facts first if they exist.

Truncates recent_summary from the end if needed to stay under limit.

Format:

MEMORY CONTEXT:

Recovery focus: [values]

Recovery program: [value]

Sobriety why: [value]

Known triggers: [values]

Support style: [value]

Pinned facts: [values]

Sober contacts: [names only, no phone numbers]

Recent patterns last 30 days: [recent_summary]

Recent events: [last 5 event_log entries as plain text]

1. appendEventLog(userId, event)

Loads current user_memory for userId.

Reads event_log. If missing or malformed, resets to [].

Appends the new event object.

Caps array at 90 entries (removes oldest).

Saves updated user_memory with updated_at = now().

Wraps everything in try/catch.

If anything fails, logs server-side. Never throws.

Event shape: { timestamp: “ISO8601”, type: string, summary: string }

1. classifyRisk({ source, input, history, memorySummary })

source: “checkin” or “chat”

Calls gpt-4o-mini with the input.

Uses structured JSON output or JSON mode.

Returns strict JSON: { risk: “low” | “moderate” | “high” | “crisis” }

If parsing fails or value outside enum: returns { risk: “moderate” }, logs server-side.

Never throws. Fallback is always { risk: “moderate” }.

Definitions (same for all sources):

low: normal, no acute risk

moderate: elevated distress or craving, no imminent danger

high: strong craving, relapse risk, severe dysregulation, may use soon

crisis: suicidal ideation, intent to harm self/others, overdose risk,

acute medical danger, immediate physical danger

Important: imminent relapse alone = high, not crisis.

1. buildHandoffPayload(stableProfile)

Returns: { contacts, meeting_links, tell_on_myself_message }

Reads sober_contacts and meeting_links from stableProfile only.

contacts: array of { name, phone } — phone included for frontend rendering only

tell_on_myself_message: “Hey. Having a hard time right now. Just telling on it.”

If contacts or links are missing/malformed, returns safe empty arrays.

Never includes phone numbers in AI prompts — this payload is for frontend only.

1. safeBackgroundTask(label, asyncFn)

Wraps any async background operation in try/catch.

Logs label + error server-side on failure.

Never throws. Never creates unhandled promise rejections.

Usage: safeBackgroundTask(“summarize_memory”, async () => { … })

-----

V3A GOALS

1. Add three-layer memory database schema

1. Replace existing V2 onboarding entirely with a new V3 sponsor intake flow (9 steps)

1. Inject memory into all existing AI calls so responses feel longitudinal

1. Add a Memory screen in Settings for user control

1. Add structured crisis handling that does not break existing JSON parsing

1. Future-proof the stable profile for later personalization

1. Keep the app stable even if background memory updates or risk classification fail

-----

DATABASE: CREATE THIS NEW TABLE IF IT DOES NOT EXIST

Table: user_memory

- id serial primary key

- user_id varchar default ‘dev_user’

- stable_profile jsonb

- recent_summary text

- event_log jsonb

- last_summarized_at_event_count integer default 0

- last_checkin_local_date varchar

- updated_at timestamp with time zone default now()

Important:

- event_log should be stored as a JSON array

- If user_memory does not exist for the current user, create a default row gracefully

- Never allow missing memory to crash check-ins

- Never allow malformed memory to crash check-ins

- last_summarized_at_event_count tracks when summarization last ran (by event count)

- last_checkin_local_date stores the user’s local YYYY-MM-DD of their most recent check-in

-----

DATABASE: SAFE MIGRATION FOR ONBOARDING VERSION

The existing app_settings table may already have first_open_completed boolean from V2B.

Do not destructively rename or drop existing columns without checking first.

For onboarding_version:

- If app_settings.onboarding_version does not exist, add it as integer default 0

- If first_open_completed exists and onboarding_version is 0 or null, backfill:

first_open_completed = true  → onboarding_version = 2

first_open_completed = false/null → onboarding_version = 0

- Do NOT drop first_open_completed during this phase

- Update app logic to use onboarding_version going forward

- A value of 0 means no onboarding completed

- A value of 2 means V2 basic onboarding was completed, now obsolete

- A value of 3 means the new V3 sponsor intake is completed

- On app load: if onboarding_version < 3, show the new V3 intake flow

-----

STABLE PROFILE SCHEMA

Use this jsonb shape as the default stable_profile:

{

“recovery_focus”: [],

“sobriety_start_dates”: {},

“known_triggers”: [],

“support_style”: “”,

“recovery_program”: “”,

“sobriety_why”: “”,

“sober_contacts”: [],

“meeting_links”: [],

“recurring_commitments”: [],

“pinned_facts”: [],

“email”: “”,

“reminder_time”: “08:00”,

“timezone”: “America/New_York”,

“commitment_followup_hours”: 4,

“reminder_enabled”: true,

“weekly_summary_enabled”: true

}

Notes:

- sober_contacts entries: { “name”: “”, “phone”: “” }

- meeting_links entries: { “label”: “”, “url”: “” }

- commitment_followup_hours, reminder_enabled, and weekly_summary_enabled

are stored here, NOT in app_settings. stable_profile is the single source

of truth for all user preferences.

- recovery_program and sobriety_why are stored now for later personalization

-----

EVENT LOG ENTRY SHAPE

Each event_log entry:

{

“timestamp”: “ISO8601”,

“type”: “checkin_summary|tracker_reset|commitment|milestone|missed_checkins|chat_session”,

“summary”: “one line plain text”

}

-----

MEMORY UPDATE AFTER EVERY CHECK-IN

After every successful check-in and normal AI response:

1. Build a one-line event_log entry:

“YYYY-MM-DD: [risk level], mood [N], craving [N], trigger: [key trigger], [short summary]”

1. Use appendEventLog(userId, event) from shared helpers to save it.

1. Update user_memory.last_checkin_local_date with the user’s local YYYY-MM-DD.

Compute using stable_profile.timezone (default America/New_York if missing).

1. Check if background summarization should run:

- Count current event_log length after appending.

- Read last_summarized_at_event_count from user_memory.

- If (current_length - last_summarized_at_event_count) >= 3:

Run background summarization via safeBackgroundTask().

On success, update last_summarized_at_event_count = current_length.

- If fewer than 3 new entries since last summarization, skip.

This reduces summarization from daily to approximately every 3 check-ins.

-----

BACKGROUND SUMMARIZATION SAFETY

Use safeBackgroundTask(“summarize_memory”, async () => { … }) from shared helpers.

Background summarization system prompt:

“Summarize these recovery check-in events in plain text under 800 tokens.

Note patterns, trends, recurring triggers, wins, resets, and current pressure

points. Be factual and specific.”

On success: update recent_summary and last_summarized_at_event_count.

On failure: keep existing recent_summary unchanged. Log server-side.

Never block the UI. Never crash the server.

-----

MEMORY INJECTION INTO AI CALLS

Use buildMemoryContext(userMemory, { pauseMemory }) from shared helpers.

Inject the returned string at the top of the system prompt before all other instructions.

If buildMemoryContext returns an empty string, skip injection and proceed normally.

-----

UPDATED AI SYSTEM PROMPT INSTRUCTION

Keep all existing sponsor tone and JSON output requirements from V2.

After the memory block, add:

“Reference the memory context above when relevant. If you notice a pattern worth

naming, name it specifically. If the person has shared triggers before that match

today’s state, acknowledge it. If their sobriety why is relevant, remind them

without being sentimental. Make the response feel like it comes from someone who

has been paying attention over time.”

-----

CRISIS HANDLING: STRUCTURED PAYLOAD, DO NOT BREAK JSON

Use classifyRisk({ source: “checkin”, input, history, memorySummary }) from shared helpers.

Run classification before the normal check-in AI call.

Parse result defensively. Default to “moderate” on any failure.

Classifier definitions:

- low: normal check-in, no acute risk

- moderate: elevated emotional or craving risk, but no imminent danger

- high: strong craving, relapse risk, severe dysregulation, or user says they may use soon

- crisis: suicidal ideation, intent to harm self, intent to harm others, overdose risk,

acute medical danger, or immediate physical danger

Important: imminent relapse alone = high, not crisis.

If crisis detected, skip normal check-in AI call and return:

{

“crisis”: true,

“risk_level”: “crisis”,

“crisis_message”: “I’m really glad you said this out loud. This is bigger than an app

conversation. Please contact a real person right now.”,

“resources”: {

“lifeline”: “988 Suicide and Crisis Lifeline: call or text 988”,

“samhsa”: “SAMHSA National Helpline: 1-800-662-4357”,

“sober_contacts”: [ { “name”: “Name”, “phone”: “Phone” } ]

}

}

Frontend behavior for crisis payload:

- On receiving any check-in response, check crisis === true FIRST.

- If true, render full crisis resource card and stop.

- Do not render the normal result card.

- Show 988 Suicide and Crisis Lifeline prominently.

- Show SAMHSA National Helpline prominently.

- Show saved sober contacts with tap-to-call buttons if available.

- Do not show charts, scores, or normal coaching language.

If low, moderate, or high: continue with normal check-in AI call.

Preserve existing JSON response shape.

Append to all normal AI system prompts:

“If the person expresses suicidal ideation, intent to harm themselves, intent to

harm others, overdose risk, acute medical danger, or immediate physical danger:

do not treat this as a normal coaching moment. Route to the structured crisis

resource flow with 988, SAMHSA, and saved sober contacts.”

-----

CHECK-IN LOADING STATE

Show one continuous grounding loading state from submit until final response.

Display text such as: “Reading your check-in…” “Checking risk level…” “Writing your response…”

Requirements:

- Do not flicker between separate loading states

- Disable duplicate submits while processing

- Re-enable submit button after success or error

- If classifier defaults to moderate due to error, do not show a scary message

-----

SPONSOR INTAKE ONBOARDING: 9-STEP FLOW — REPLACES V2 ONBOARDING

IMPORTANT: This is a 9-step onboarding flow. Do not implement it as 8 steps.

Steps 5 (recovery_program) and 6 (sobriety_why) are required.

On every app load:

- Check app_settings.onboarding_version

- If onboarding_version < 3, show the V3 intake flow before the home screen

- This replaces and supersedes V2B onboarding completely

- Delete or hide any V2 onboarding UI

- Preserve dark theme

- Not a chat. Not a modal. A sequential screen flow with a progress bar.

Step 1: Welcome

- Progress: Step 1 of 9

- Text: “This is Anchor. Your private recovery companion. Let’s get set up.”

- Button: “Get started”

Step 2: Recovery focus

- Progress: Step 2 of 9

- Question: “What are you in recovery from?”

- Multi-select pill buttons: Alcohol, Weed, Nicotine, Porn, Gambling, Sugar, Codependency, Other

- “Other” reveals a text input

- Required. Must select at least one to proceed.

Step 3: Sobriety start

- Progress: Step 3 of 9

- Question: “When did your sobriety begin?”

- Date picker plus time picker

- If user picks a date, store it in frontend onboarding state.

Do NOT create the sobriety tracker yet. Defer tracker creation to Step 9 completion.

This prevents duplicate trackers if user navigates back and changes the date.

- Skip link: “I’ll set this up later”

Step 4: Support style

- Progress: Step 4 of 9

- Question: “What kind of support helps you most?”

- Single select: Direct and honest, Gentle and encouraging, Just the facts, Mix of all three

Step 5: Recovery approach

- Progress: Step 5 of 9

- Question: “What kind of recovery approach fits you best right now?”

- Single select: AA / NA, SMART Recovery, Refuge Recovery, Secular / no program, Other, Not sure yet

- “Other” reveals a text input

- Optional. Skip link: “I’ll choose later”

- Saves to stable_profile.recovery_program

Step 6: Sobriety why

- Progress: Step 6 of 9

- Question: “Why are you doing this?”

- Textarea placeholder: “A sentence or two you want Anchor to remember on hard days.”

- Optional. Skip link: “I’ll add this later”

- Saves to stable_profile.sobriety_why

Step 7: Sober contacts

- Progress: Step 7 of 9

- Question: “Who are your sober contacts?”

- Add up to 3 contacts: name field, phone field

- Optional. Skip link: “I’ll add these later”

Step 8: Meeting links

- Progress: Step 8 of 9

- Question: “Do you have regular meeting links?”

- Add up to 3 meetings: label field, URL field

- Optional. Skip link: “I’ll add these later”

Step 9: Reminder setup and complete

- Progress: Step 9 of 9

- Question: “When do you want your daily check-in reminder?”

- Time picker, default 8:00 AM

- Email input field, optional, placeholder “For weekly summaries”

- Text: “You’re set. Check in daily. This stays between you and Anchor.”

- Button: “Go to dashboard”

- On completion:

1. Save all collected inputs to stable_profile in user_memory table

1. If Step 3 sobriety date was selected, create sobriety tracker NOW (idempotent)

1. Set onboarding_version = 3 in app_settings

Navigation:

- Back button on all steps after Step 1

- Back navigates to previous step without losing entered data

- Step 1 has no Back button

- Skip links preserve existing data and set skipped fields to safe empty values

Error handling:

- If app crashes mid-onboarding, on next load detect onboarding_version < 3 and restart

- If any step save fails, log server-side, allow user to continue

- Missing skipped fields become empty strings or empty arrays, not null errors

-----

MEMORY CONTROLS SCREEN

Add a “Memory” option in Settings.

Section 1: Your Profile

- Display all stable_profile fields in readable labeled format

- Edit, pin, delete buttons on fields where appropriate

- Pin behavior: adds readable version to stable_profile.pinned_facts

pinned_facts are always injected into AI context first

Avoid duplicate pinned facts

Section 2: Recent Patterns

- Display recent_summary as plain text

- Label: “What Anchor knows about your last 30 days”

- Read only

Section 3: Event Log

- Scrollable list of event_log entries with timestamp and summary

- Delete button on individual entries

- Deleting updates user_memory.event_log only

- Does not delete raw check-in data

Section 4: Controls

- “Pause memory for next session” toggle

Frontend session flag only. Resets on next app open.

Does not modify database.

- “Reset all memory” button

Requires typed confirmation: “reset”

Clears stable_profile to default empty values

Clears recent_summary

Clears event_log

Does NOT delete raw check-in data

Does NOT delete tracker data

Does NOT delete app_settings

Does NOT reset onboarding_version

Optional: “Reset onboarding” button in Settings

- Requires typed confirmation: “reset”

- Sets app_settings.onboarding_version = 0

- Does not delete raw check-in data

- On next app load, shows V3 intake from Step 1

-----

ERROR HANDLING

- If user_memory load fails, continue without memory injection, log server-side

- If background summarization fails, keep existing recent_summary, log server-side

- If stable_profile is missing a field, treat as empty string or empty array

- If event_log is malformed, reset to [] and log server-side

- If risk classifier fails, default to moderate, log server-side warning

- If memory save fails during onboarding, log server-side, allow user to continue

- If Memory screen fetch fails, show: “Memory is unavailable right now. Try again.”

- No async background operation should ever create an unhandled promise rejection

- No background memory operation should ever crash the Express/Replit server

-----

SECURITY AND PRIVACY

- This no-auth V3A fork is for private development only

- Do not expose phone numbers in AI memory context

- AI memory context may include sober contact names only, not phone numbers

- Crisis resource card may display phone numbers (rendered directly to user)

- Do not send emails in V3A

- Do not build outreach in V3A

-----

ACCEPTANCE TESTS

1. App starts normally in Replit preview

1. Existing V2 functionality still works

1. Existing dark theme remains intact

1. Existing check-in form still works

1. Existing history/progress/tracker screens still work

1. If onboarding_version < 3, V3 intake appears (9 steps)

1. Completing V3 intake saves stable_profile into user_memory

1. Completing V3 intake sets onboarding_version = 3

1. V2 onboarding no longer appears

1. Onboarding progress bar correctly reads “Step X of 9” on all steps

1. Back button works without losing entered data

1. Sobriety tracker is created only once at Step 9 completion

1. Memory screen appears in Settings

1. Stable profile displays correctly in Memory screen

1. Recent summary and event log display correctly, even if empty

1. Reset memory works and does not delete raw check-ins

1. Pause memory for next session prevents memory injection for that session

1. Check-in AI calls receive memory context when memory exists

1. Check-in AI calls still work when memory is empty

1. After check-in, event_log receives a one-line summary

1. last_checkin_local_date updates after each check-in

1. Background summarization runs only after 3+ new events, not every check-in

1. Background summarization errors are caught and do not crash the server

1. Crisis classifier returns strict JSON: { “risk”: “low|moderate|high|crisis” }

1. Malformed classifier output defaults to moderate and logs server-side

1. Crisis classifier triggers structured crisis payload for suicidal ideation/self-harm

1. Crisis payload renders crisis resource card, not normal result card

1. High relapse risk without self-harm is treated as high, not crisis

1. All shared helper functions exist in a shared utilities file

1. No hardcoded “maxwell” user ID anywhere

-----

AT THE END

When finished, report back with:

1. Exactly what was implemented

1. Files changed

1. Database migrations added

1. Shared helper functions created and their file location

1. Whether onboarding is 9 steps with correct progress labels

1. Whether sobriety tracker creation is deferred to Step 9 completion

1. Whether summarization only triggers on 3+ new events

1. Whether last_checkin_local_date is updated after check-ins

1. Whether old V2 onboarding is fully replaced

1. Whether structured crisis handling is implemented

1. Whether classifier output is strict JSON

1. Whether background summarization errors are safely caught

1. Any environment variables needed in Replit Secrets

1. Any known issues or skipped items

1. Exact next step: run V3A Revision Patch, then V3 Shared Architecture Cleanup, then V3B

Run as a persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.

V3A revision patch 2

# V3A POST-LAUNCH FIXES

Apply these targeted fixes to the already-running V3A implementation.

Do NOT rebuild from scratch. Do NOT add new product features.

Do NOT touch V3B, V3C, V3D, V3E, or V3F functionality.

Make only the changes listed below. Report exactly what was changed.

This is a patch pass only. Scope is strictly:

- Onboarding Step 3: per-addiction sobriety dates

- Duplicate tracker prevention

- Onboarding copy warmth improvements

- Memory screen phone number display audit

- Minor UI/UX polish from visual review

-----

PRE-FLIGHT

Before making any changes, inspect:

1. Current onboarding Step 2 and Step 3 implementation

1. How sobriety trackers are currently created (where, when, with what data)

1. Whether duplicate tracker prevention logic exists

1. Current onboarding copy on all 9 steps

1. How the Memory screen renders sober_contacts

Report briefly, then proceed.

-----

FIX 1: PER-ADDICTION SOBRIETY DATE PICKER IN STEP 3

PROBLEM:

Step 3 currently shows one single sobriety date picker regardless of how many

recovery focus items the user selected in Step 2. If a user selected Alcohol,

Nicotine, Porn, and Codependency, they get one date for everything. This is wrong —

each addiction can have a completely different sobriety start date.

FIX:

Replace the single date/time picker in Step 3 with a per-item date picker.

For each item selected in Step 2 (recovery_focus array), show:

- A clear label: “When did you stop [item]?”

Examples:

“When did you stop drinking alcohol?”

“When did you stop using nicotine?”

“When did you stop watching porn?”

“When did you stop using weed?”

“When did you step back from codependency?” (for codependency, softer phrasing)

“When did you stop gambling?”

“When did you stop eating sugar?” (for sugar, softer phrasing)

“When did you start this?” (for custom “Other” entries)

- A date picker (date + time) defaulting to today’s date/time

- A small “I’ll set this later” skip link PER ITEM (skipping one item does not skip all)

Store each selected date in frontend onboarding state as:

sobriety_dates: {

“Alcohol”: { date: “ISO8601”, skipped: false },

“Nicotine”: { date: “ISO8601”, skipped: true },

…

}

At Step 9 completion:

- For each item in sobriety_dates where skipped = false:

Create one sobriety tracker with:

name = item label (e.g. “Alcohol”)

start_date = selected date

- For items where skipped = true: do not create a tracker

- Tracker creation must be IDEMPOTENT (see Fix 2)

Progress bar and step count remain “Step 3 of 9” — this is still one step,

just with multiple pickers inside it.

If Step 2 selected only one item, show only one picker (same as before, just cleaner).

If the user navigates Back from Step 4 to Step 3, restore previously entered dates.

Do not reset the pickers on back navigation.

-----

FIX 2: DUPLICATE TRACKER PREVENTION (IDEMPOTENCY)

PROBLEM:

If a user completes onboarding, resets onboarding, and completes it again, or if

they navigate back through Step 3 and change dates, duplicate trackers can be created.

Currently two Alcohol trackers exist in the database from exactly this scenario.

FIX:

At Step 9 completion, before creating any tracker:

1. Query existing sobriety_trackers for the current user.

1. For each tracker to be created from onboarding:

- Check if a tracker already exists with the same name (case-insensitive) for this user.

- If one exists: UPDATE its start_date to the new selected date. Do not insert a new row.

- If none exists: INSERT the new tracker.

1. Never insert duplicate trackers for the same addiction name + user combination during onboarding.

Also clean up the database NOW:

- Find any duplicate sobriety trackers for the current user (same name, same user_id).

- Keep the one with the most recent created_at.

- Delete the older duplicate(s).

- Log what was deleted server-side.

This cleanup should run once as a migration, not on every request.

Note: permanent tracker deletion is also being added in Fix 8 below, which gives

the user a manual delete option going forward so this situation can be self-corrected

without needing a database migration.

-----

FIX 3: ONBOARDING COPY WARMTH IMPROVEMENTS

PROBLEM:

Several onboarding step labels and subtext read as clinical, flat, or form-like.

The Anchor tone should be warm, plain-spoken, and calm — not a therapy intake form.

Review and update the following:

Step 1 — Welcome

Current: “This is Anchor. Your private recovery companion. Let’s get set up.”

Keep as-is. This is good.

Step 2 — Recovery focus

Current question: “What are you in recovery from?”

Keep as-is. Direct and clear.

Subtext if any: Keep minimal, no clinical language.

Step 3 — Sobriety start (after Fix 1 above)

Per-item label pattern:

“When did you stop drinking alcohol?” ✓

“When did you stop using nicotine?” ✓

“When did you step back from codependency?” ✓ (softer)

“When did you stop using weed?” ✓

“When did you stop watching porn?” ✓

“When did you stop gambling?” ✓

“When did you cut back on sugar?” ✓ (softer)

“When did you start this?” for Other ✓

Current subtext: “We’ll create a tracker automatically.”

Replace with: “We’ll track it from here.”

Skip link: “I’ll set this up later” — keep as-is, but make it per-item

Step 4 — Support style

Current question: “What kind of support helps you most?”

Keep as-is.

Step 5 — Recovery approach

Current question: “What kind of recovery approach fits you best right now?”

Keep as-is.

Skip link: “I’ll choose later” — keep as-is.

Step 6 — Sobriety why

Current question: “Why are you doing this?”

Current placeholder: “A sentence or two you want Anchor to remember on hard days.”

Both are good. Keep as-is.

Step 7 — Sober contacts

Current question: “Who are your sober contacts?”

Keep as-is.

Step 8 — Meeting links

Current question: “Do you have regular meeting links?”

Current subtext: “Online meetings, zoom links, etc.”

Subtext is fine. Keep as-is.

Step 9 — Reminder setup

Current question: “When do you want your daily check-in reminder?”

Keep as-is.

Current label: “EMAIL (OPTIONAL)” — change from ALL CAPS label to sentence case: “Email (optional)”

Current footer text: “You’re set. Check in daily. This stays between you and Anchor.”

Keep as-is. This is good.

General onboarding copy rules:

- Do not use motivational clichés

- Do not imply Anchor is a human sponsor

- Do not use clinical intake language

- Warm, plain-spoken, respectful

-----

FIX 4: MEMORY SCREEN — PHONE NUMBER DISPLAY AUDIT

PROBLEM:

The Memory screen (Your Profile section) currently displays sober contact phone

numbers in plain text (e.g. “13055258213” visible next to “Andrew”). This is fine

for the user viewing their own data, but we need to confirm phone numbers are NOT

leaking into AI system prompts.

TWO PARTS:

Part A — Memory screen display (this is acceptable, no change needed)

Phone numbers ARE allowed to appear in the Memory screen because the user is

viewing their own stored data. This is correct behavior. No change needed here.

Part B — AI prompt audit (critical check)

Search every location in the codebase where buildMemoryContext() constructs

the memory injection string, and everywhere AI system prompts are assembled.

Confirm that:

- sober_contacts in AI prompts contains NAMES ONLY, never phone numbers

- The memory context string does NOT include any phone number strings

- buildHandoffPayload() returns phone numbers only for frontend rendering

- No AI call (check-in, chat, summarization, classification) receives phone numbers

If any phone numbers are found in AI prompt construction: remove them immediately.

Log the fix server-side.

If already clean: confirm and report.

-----

FIX 5: HOME SCREEN — TRACKER DISPLAY POLISH

PROBLEM:

The tracker grid on Home is showing all trackers including any duplicates.

After Fix 2 cleans up duplicates, this should resolve itself.

Additional polish:

- Trackers should be sorted by sobriety duration DESCENDING (longest first)

so the user sees their strongest win at the top-left

- If a user has more than 6 trackers, the grid should scroll or paginate cleanly

without breaking layout

- Each tracker card should show days and hours (current behavior looks correct)

- Confirm live counter updates every 60 seconds (check the existing interval logic)

No new database changes for this fix. Layout and sort only.

-----

FIX 6: SETTINGS LABEL CASING

PROBLEM:

“EMAIL (OPTIONAL)” in Step 9 uses all-caps label style which feels harsh.

Check all Settings and onboarding field labels for inconsistent casing.

Fix any field labels that are in ALL CAPS when they should be sentence case or

title case. Examples to check:

- “EMAIL (OPTIONAL)” → “Email (optional)”

- “REMINDER TIME” → check if this matches surrounding labels

- “DATE” and “TIME” in Step 3 → fine as short field labels, keep as-is

Do not change section headers that are intentionally all-caps for visual hierarchy

(e.g. “YOUR PROFILE”, “EVENT LOG”, “CONTROLS” in the Memory screen — these are

deliberate design choices and should stay).

-----

FIX 7: STEP 3 BACK NAVIGATION DATA PRESERVATION

PROBLEM:

When a user taps Back from Step 4 to Step 3, the sobriety date pickers should

restore the previously entered values. Currently there is a risk the pickers

reset to today’s date on back navigation.

FIX:

Store all onboarding step data in a single frontend onboarding state object.

Never reset a step’s data when navigating back to it.

The state object should persist for the full onboarding session.

When the user taps Continue on any step, save that step’s data to the state object.

When the user taps Back, render the previous step with data from the state object

pre-populated.

This applies to all 9 steps, not just Step 3. But Step 3 is the highest-risk step

because date pickers default to “today” on reset, which would silently change

the user’s entered sobriety date.

-----

FIX 8: ADD DELETE OPTION TO SOBRIETY TRACKERS

PROBLEM:

When a user opens a tracker, the only removal option is Archive. There is no way

to permanently delete a tracker. This means duplicate trackers, test trackers, or

unwanted trackers can only be hidden — not removed. Users should be able to

permanently delete a tracker they no longer want.

FIX:

Add a Delete button to the tracker detail/edit view, alongside the existing Archive option.

UI placement:

- Show “Archive” and “Delete” as two distinct options

- Archive: existing behavior, hides tracker from main view but preserves data

- Delete: permanently removes the tracker and all its reset history

- Delete button should be visually distinct from Archive — use a destructive color

(e.g. red or muted red) to signal permanence

- Do not make Delete the primary action — it should be clearly secondary/destructive

Delete confirmation:

- Tapping Delete shows a confirmation prompt before anything is removed

- Confirmation text: “This will permanently delete this tracker and all its history.

This cannot be undone.”

- Two options: “Cancel” and “Delete permanently”

- Only proceed on explicit “Delete permanently” tap

- Do not use a typed confirmation for this — a tap confirmation is sufficient

since tracker deletion is less catastrophic than memory reset

Backend:

- Add DELETE /api/trackers/:id endpoint

- Verify the tracker belongs to getCurrentUserId() before deleting

- Delete the tracker row and any associated tracker_resets rows for that tracker

- Return { “deleted”: true } on success

- Return 404 if tracker not found or does not belong to current user

- Wrap in try/catch, log server-side on error

- Use getCurrentUserId() — no hardcoded user IDs

After successful delete:

- Remove the tracker card from the Home dashboard immediately

- Remove the tracker from the Trackers tab immediately

- Do not require a page refresh

- Show a brief confirmation: “Tracker deleted.”

No new database tables needed. This is a DELETE operation on existing tables.

-----

SECURITY CHECK

Confirm these are still true after all fixes above:

- Phone numbers are not in any AI prompts

- getCurrentUserId() is used for all tracker queries and mutations

- No hardcoded “maxwell” was introduced

- Duplicate tracker cleanup ran safely and was logged

-----

REPORT AT THE END

When finished, report:

1. Whether per-addiction date pickers are implemented in Step 3

1. How many pickers show when 4 items are selected in Step 2

1. Whether tracker creation at Step 9 is now idempotent

1. Whether duplicate tracker cleanup ran and what was deleted

1. Which onboarding copy was updated

1. Whether phone numbers are confirmed absent from all AI prompts

1. Whether tracker sort order on Home is now longest-first

1. Whether EMAIL (OPTIONAL) label casing was fixed

1. Whether back navigation preserves Step 3 date picker values

1. Whether Delete button appears on tracker detail view with confirmation

1. Whether DELETE /api/trackers/:id endpoint works and verifies ownership

1. Whether deleting a tracker removes it from Home and Trackers tab immediately

1. Files changed

1. Any issues that could not be fixed cleanly

Do not run V3B until this report is clean.

V3B

# V3B

Upgrade the existing recovery check-in app to V3B only.

Important constraints:

- Do NOT build voice input, commitment loop, or outreach yet

- Focus only on the Chat tab and sponsor conversation interface

- Memory system from V3A must already be in place

- Shared helpers from V3 Architecture Cleanup must already exist

- This builds directly on top of V3A memory, onboarding, user ID, and crisis architecture

- The app uses plain HTML, CSS, and vanilla JavaScript

- Do NOT convert the app to React

- Extend what exists. Do not rebuild from scratch.

- Keep all existing dark theme, UI, and functionality intact

- This is still a no-auth development fork

-----

PRE-FLIGHT

Inspect the current implementation. Confirm in 5 bullets:

1. Relevant files to modify

1. Existing V3 shared helpers available to reuse

1. Database/schema impact

1. Conflicts with prior V3A phase

1. Implementation plan

Then proceed.

-----

V3 INVARIANTS

Preserve all V3 invariants throughout this phase:

- Use getCurrentUserId() everywhere. No hardcoded user IDs.

- stable_profile is the source of truth for all user preferences

- Phone numbers never appear in AI prompts — only in frontend handoff/crisis payloads

- event_log cap is 90 entries

- All background async operations use safeBackgroundTask()

- No unhandled promise rejections

-----

USER ID RULE

Use the existing getCurrentUserId() helper from V3 shared utilities.

Do NOT create a second user ID pattern for chat.

Do NOT hardcode “maxwell” anywhere.

-----

V3B GOALS

1. Add a dedicated Chat tab with full sponsor conversation

1. Add memory-aware sponsor responses referencing user history

1. Add structured risk classification before normal chat response

1. Add human handoff shortcuts at moderate and high risk

1. Add structured crisis handling that skips normal chat and shows crisis resources

1. Save one-line session summaries to chat_sessions and user_memory.event_log

1. Do not store full conversation history in the database

-----

DATABASE: ADD THIS TABLE IF IT DOES NOT EXIST

Table: chat_sessions

- id serial primary key

- user_id varchar default ‘dev_user’

- started_at timestamp with time zone default now()

- ended_at timestamp with time zone nullable

- message_count integer default 0

- session_summary text

- risk_level_detected varchar nullable

Important:

- Full conversation history is NOT stored in the database

- History lives only in frontend JavaScript variables for the current session

- Only the one-line session summary is persisted

- Use getCurrentUserId() when inserting rows

-----

NAVIGATION UPDATE

Add Chat as the third tab in bottom navigation.

New tab order:

1. Home

1. Check-In

1. Chat

1. History

1. Trackers

1. Insights

Chat tab icon: simple inline SVG speech bubble. No external icon library.

-----

CHAT INTERFACE

Build a clean mobile-first chat UI in plain HTML, CSS, and vanilla JavaScript.

Layout:

- Full height chat view, no page scroll inside chat screen

- Message list scrolls internally

- User messages: right-aligned, slightly darker bubble, white text

- Sponsor messages: left-aligned, slightly lighter dark bubble, white text, no avatar

- Timestamp on each message: time only, no date

- Auto-scroll to bottom on new message

- Input area fixed to bottom: text input field, send button

- “New conversation” button/icon in top right

- New conversation prompts for confirmation before clearing

Message behavior:

- User message appears immediately after send

- Send button disabled while processing

- Duplicate sends blocked while processing

- Typing indicator with three animated dots while awaiting response

- Do not stream responses

- Auto-scroll to latest message after each response

- If API call fails, preserve user’s message and existing history

-----

CHAT LOADING STATE

While risk classification and response generation are running:

- Show one continuous typing/loading state

- Do not flicker between classifier and response states

- Do not expose classifier status to user

- Disable duplicate sends while processing

- Keep user’s message visible immediately after sending

- Preserve chat history if API call fails

- Re-enable send button after success or error

-----

EMPTY STATE AND OPENING MESSAGE

When Chat tab opens for a new session:

- Always use a static opening message. Do NOT make an OpenAI call to personalize it.

- Static opener: “Good to see you. How are you doing today?”

- Personalized opening messages can be added in a later phase.

- This saves one OpenAI call per chat open and avoids the “AI says something

too specific before I’ve typed anything” problem.

- Do not store this static opener in the database.

-----

CHAT API ENDPOINT

POST /api/chat

Request body:

{

“message”: “user message text”,

“history”: [

{ “role”: “user”, “content”: “…” },

{ “role”: “assistant”, “content”: “…” }

],

“memory_paused”: false

}

Normal response:

{

“crisis”: false,

“reply”: “sponsor response text”,

“risk_level”: “low|moderate|high”,

“show_handoff”: true,

“handoff”: {

“contacts”: [ { “name”: “Name”, “phone”: “Phone” } ],

“meeting_links”: [ { “label”: “Label”, “url”: “URL” } ],

“tell_on_myself_message”: “Hey. Having a hard time right now. Just telling on it.”

}

}

If show_handoff is false, handoff may be null or empty.

Crisis response:

{

“crisis”: true,

“reply”: “”,

“risk_level”: “crisis”,

“show_handoff”: true,

“crisis_message”: “I’m really glad you said this out loud. This is bigger than an app

conversation. Please contact a real person right now.”,

“resources”: {

“lifeline”: “988 Suicide and Crisis Lifeline: call or text 988”,

“samhsa”: “SAMHSA National Helpline: 1-800-662-4357”,

“sober_contacts”: [ { “name”: “Name”, “phone”: “Phone” } ]

}

}

-----

BACKEND LOGIC

Use this exact sequence:

1. Load user_memory using loadUserMemory(getCurrentUserId())

1. Build memory context using buildMemoryContext(userMemory, { pauseMemory: req.body.memory_paused })

1. Run classifyRisk({ source: “chat”, input: message, history: last 4 turns, memorySummary })

1. If crisis:

- Skip normal response generation

- Return structured crisis payload immediately

- Use buildHandoffPayload(stableProfile) to populate sober_contacts in resources

1. If low, moderate, or high:

- Build messages array: system prompt + memory context + conversation history + latest message

- Call gpt-4o-mini for sponsor response

- Set show_handoff = (risk_level === “moderate” || risk_level === “high”)

- If show_handoff: use buildHandoffPayload(stableProfile) to populate handoff

- Return structured JSON response

1. If classifier fails:

- Default risk to “moderate”

- Set show_handoff = true

- Continue normal response

- Log server-side

1. Never block user from receiving a response due to classifier failure

Important:

- Use classifyRisk() from shared helpers — do NOT re-implement the classifier

- Use buildMemoryContext() from shared helpers — do NOT re-implement memory injection

- Use buildHandoffPayload() from shared helpers — do NOT re-implement handoff logic

- Do not classify “imminent relapse” as crisis by default

- Do not generate a normal response and then throw it away for crisis cases

-----

MEMORY CONTEXT FOR CHAT

Use buildMemoryContext(userMemory, { pauseMemory }) from shared helpers.

Same function, same output, same rules as check-in injection.

No second implementation.

On first message of a session: inject FULL memory context (all fields).

On subsequent messages in the SAME session: inject only stable_profile summary

(recovery focus, support style, pinned facts). Rely on frontend history for context.

This reduces token overhead by ~60% on multi-turn conversations.

-----

CHAT SYSTEM PROMPT

“You are a seasoned, plain-speaking recovery companion with knowledge of AA, NA,

SMART Recovery, secular recovery, and practical relapse prevention. You are not a

human sponsor, therapist, or crisis service. You are a recovery support tool that

helps the person return to wise action and real human contact.

You have access to this person’s memory context. Reference it when relevant, but

do not force it into every response. If you notice a pattern worth naming, name it

specifically. If their recovery program or sobriety why is relevant, use it naturally.

Speak directly, with warmth and without shame. Reference what they actually share

in this conversation. Vary your language. Do not repeat canned recovery clichés.

Occasionally ask one short reflective question when it fits naturally.

Always end your response with either a concrete suggested action or a human contact

suggestion. Never leave someone in pure reflection without a next step.

If the person expresses suicidal ideation, intent to harm themselves, intent to harm

others, overdose risk, acute medical danger, or immediate physical danger: do not

treat this as a normal coaching moment. The app should route to the structured crisis

resource flow with 988, SAMHSA, and saved sober contacts. Do not provide extended advice.

Imminent relapse alone should be treated as high risk rather than crisis unless there

is acute danger, overdose risk, self-harm risk, harm to others, or immediate physical danger.

[MEMORY CONTEXT BLOCK INJECTED HERE]

Respond in plain conversational text. No JSON. No markdown unless truly useful.

No bullet points unless listing specific action options. Keep responses under 150 words

unless the situation genuinely calls for more.”

-----

CRISIS HANDLING IN CHAT

FRONTEND BEHAVIOR FOR CRISIS RESPONSES — CRITICAL:

On receiving ANY /api/chat response, check crisis === true FIRST.

If true: render full-screen crisis card immediately and stop.

Do NOT read or render the reply field.

Do NOT proceed with normal chat rendering.

Frontend crisis card:

- Replaces the entire chat UI with a full-screen crisis resource card

- Show 988 Suicide and Crisis Lifeline prominently

- Show SAMHSA National Helpline prominently

- Show saved sober contacts with tap-to-call buttons if available

- Include a small “Return to chat” link at the very bottom

- Do not automatically send messages or call anyone

- Do not continue normal chat conversation in crisis mode

-----

HUMAN HANDOFF SHORTCUTS

When show_handoff is true (moderate or high risk):

- Show a dismissable banner below the message list, above the input area

- Use buildHandoffPayload() data from the response

- Show saved sober contact names as tap-to-call buttons using tel: URI

- If meeting links exist, show “Find a meeting” button

- Show “Tell on myself” button

Tell on myself behavior:

- Opens native SMS via sms: URI

- Uses first saved sober contact phone number if available

- Pre-fills editable message: “Hey. Having a hard time right now. Just telling on it.”

- User edits and sends manually. Nothing is ever sent automatically.

If no contacts or meeting links exist:

- Show: “Add sober contacts in Settings to enable quick outreach.”

- Do not show empty buttons

-----

SESSION END AND SUMMARY

Only generate and save session summary when:

- User taps “New conversation” and confirms, AND

- At least 2 user messages and 2 assistant messages exist in the session

Do NOT auto-save on tab navigation.

Do NOT auto-save on app close.

Sessions shorter than 2+2 turns can be discarded without saving.

This prevents tiny low-value summaries from accidental tab taps.

Recommended endpoint:

POST /api/chat/session-summary

Request body:

{

“history”: [ { “role”: “user”, “content”: “…” }, … ],

“risk_level_detected”: “low|moderate|high|crisis”

}

Session summary system prompt:

“Summarize this recovery conversation in one sentence. Include: main topic,

risk level detected, concrete action suggested, and whether the user accepted

or resisted the action if visible. Plain text only.”

Save behavior:

- Insert into chat_sessions with getCurrentUserId()

- Use appendEventLog(userId, event) from shared helpers to append:

{ “timestamp”: “ISO8601”, “type”: “chat_session”, “summary”: “[one-line summary]” }

- Use safeBackgroundTask() for the summary generation

Session summary safety:

- Wrap entire task in safeBackgroundTask(“chat_session_summary”, …)

- If OpenAI fails: log server-side, skip saving, do not block new conversation

- Do not crash server. No unhandled promise rejections.

-----

SESSION DISPLAY ON RETURN

- When user returns to Chat tab mid-session: restore messages from frontend JS variables

- When user returns after new session started: show empty state with static opener

- Do not load prior session messages from database

- Prior session summaries exist in event_log but are not rendered as chat history

-----

ERROR HANDLING

- If /api/chat fails: show “Something went wrong. Try again.” Preserve history. Re-enable send.

- If memory injection fails: continue without memory. Log server-side.

- If classifier fails: default to moderate, show_handoff = true, log server-side.

- If classifier returns malformed JSON: default to moderate, log malformed output.

- If session summary fails: log error, skip silently, do not block new conversation.

- If opening static message fails to render: this is a frontend bug, not an API call.

- No async background operation should create an unhandled promise rejection.

-----

SECURITY AND PRIVACY

- No-auth dev fork — private development only

- Phone numbers excluded from all AI prompts

- Frontend receives phone numbers only for handoff buttons and crisis cards

- Do not send SMS automatically

- Do not store full chat history in the database

- Do not send emails in V3B

- Do not build outreach in V3B

-----

ACCEPTANCE TESTS

1. App starts normally in Replit preview

1. Existing V3A functionality still works

1. Existing dark theme intact

1. Chat tab appears as third tab in navigation

1. Chat UI renders correctly on mobile width

1. User messages appear right-aligned

1. Sponsor messages appear left-aligned

1. Timestamps appear on messages

1. Input area stays fixed to bottom

1. Send button disabled while processing

1. Duplicate sends blocked

1. getCurrentUserId() used — no hardcoded IDs

1. chat_sessions table exists

1. Full conversation history NOT stored in database

1. Static opening message used — no OpenAI call on chat open

1. Memory context injected in full only on first message of session

1. Subsequent messages inject only stable_profile summary

1. Risk classifier uses shared classifyRisk() helper

1. Memory context uses shared buildMemoryContext() helper

1. Handoff payload uses shared buildHandoffPayload() helper

1. Classifier returns strict JSON { “risk”: “…” }

1. Malformed classifier output defaults to moderate

1. crisis === true check is FIRST thing frontend does on response

1. Crisis state replaces chat UI with full-screen resource card

1. High relapse risk without self-harm = high, not crisis

1. Moderate and high risk show human handoff banner

1. Tell on myself opens native SMS draft, never sends automatically

1. Session summary saves only on confirmed “New conversation” with 2+2 turns

1. Session summary uses appendEventLog() shared helper

1. Session summary background failures caught, no server crash

-----

AT THE END

When finished, report: what was implemented, files changed, database migrations added,

shared helpers used (confirm not duplicated), known issues or skipped items,

environment variables needed, and exact next step for V3C. Keep under 300 words.

Run as a persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.

V3C

# V3C

Upgrade the existing recovery check-in app to V3C only.

Important constraints:

- Do NOT build voice input, email outreach, or push notifications

- Do NOT build chat-based commitments yet

- Focus only on:

1. Commitment selection after check-in result cards

1. Follow-up banner on Home

1. Human contact shortcuts on check-in result cards

1. “Tell on myself” SMS draft button

1. Commitment follow-up timing setting

1. Commitment completion rate on Insights

- V3A memory and V3B chat architecture must already be in place

- Shared helpers from V3 Architecture Cleanup must exist

- Contacts and meeting links already exist in stable_profile from V3A

- Do NOT create a separate contacts or meeting links table

- Read all contact and meeting data from user_memory.stable_profile

- Use getCurrentUserId() for all database operations

- Do NOT hardcode “maxwell” anywhere

- Extend what exists. Do not rebuild from scratch.

- Keep all existing dark theme, UI, and functionality intact

- Preserve V3A crisis handling exactly

- Preserve V3B chat behavior exactly

-----

PRE-FLIGHT

Inspect the current implementation. Confirm in 5 bullets:

1. Relevant files to modify

1. Existing V3 shared helpers available to reuse

1. Database/schema impact

1. Conflicts with prior phases

1. Implementation plan

Then proceed.

-----

V3 INVARIANTS

Preserve all V3 invariants throughout this phase:

- Use getCurrentUserId() everywhere. No hardcoded user IDs.

- stable_profile is the source of truth for ALL user preferences including

commitment_followup_hours (stored in stable_profile, NOT app_settings)

- Phone numbers never appear in AI prompts

- event_log cap is 90 entries

- All background async operations use safeBackgroundTask()

- No unhandled promise rejections

-----

V3C GOALS

1. Add commitment selection at the end of every normal check-in result card

1. Add follow-up banner on Home asking if user completed their commitment

1. Add human contact shortcuts on elevated-risk check-in result cards

1. Add “Tell on myself” message template to result cards

1. Add commitment follow-up timing setting to Settings (stored in stable_profile)

1. Show commitment completion rate on Insights page

1. Append commitment events to user_memory.event_log safely via appendEventLog()

1. Reuse all V3A/V3B shared helpers

-----

SCOPE NOTE

Implement commitment selection after check-in result cards ONLY.

Do NOT add chat-based commitment saving yet.

-----

DATABASE: ADD THIS TABLE IF IT DOES NOT EXIST

Table: commitments

- id serial primary key

- user_id varchar default ‘dev_user’

- created_at timestamp with time zone default now()

- check_in_id integer nullable

- commitment_text text not null

- followup_scheduled_at timestamp with time zone not null

- completed boolean default false

- completed_at timestamp with time zone nullable

- followup_response varchar nullable

- smaller_version text nullable

Allowed followup_response values: ‘yes’, ‘not_yet’, ‘smaller’

IMPORTANT:

- Do NOT add a foreign key constraint on check_in_id.

Leave it as a plain nullable integer with no references.

FK integrity can be added later when auth and user isolation are stable.

- Use getCurrentUserId() when inserting or querying

- Do not store full AI responses in commitments

- Do not store phone numbers in commitments

-----

COMMITMENT FOLLOW-UP TIMING: STORED IN stable_profile

IMPORTANT: Do NOT add commitment_followup_hours to app_settings.

It already exists in stable_profile as defined in V3A.

Read it from stable_profile when computing followup_scheduled_at.

Default value: 4 (hours)

Allowed values: 2, 4, 6, 8, 12

If value is missing, null, or invalid: default to 4.

The Settings UI for this preference saves to stable_profile via the existing

stable_profile update endpoint, NOT to app_settings.

-----

AI SCHEMA UPDATE: ADD suggested_commitments TO CHECK-IN RESPONSE

Add “suggested_commitments” to the existing normal check-in AI JSON output.

Update the check-in system prompt to include after existing output requirements:

“Also return suggested_commitments: an array of exactly 4 specific, concrete

actions based on the person’s current state. Not generic — reference what they

shared. Each item should be short enough to fit on a button (under 90 characters).

Examples: ‘Text your sponsor before you do anything else’, ‘Go for a 10-minute

walk now’, ‘Eat something and drink water’, ‘Open the meeting link and just show up’.

Return as: "suggested_commitments": ["action 1", "action 2", "action 3", "action 4"]”

Full updated normal check-in JSON shape:

{

“state_summary”: “…”,

“risk_level”: “low|moderate|high”,

“main_risk_factor”: “…”,

“next_moves”: [”…”, “…”, “…”],

“recovery_support_prompt”: “…”,

“reminder”: “…”,

“sponsor_note”: “…”,

“suggested_commitments”: [”…”, “…”, “…”, “…”]

}

BACKWARD COMPATIBILITY:

This change must be backward-compatible. If the existing check-in response

parser validates strict schema or enumerates expected keys, update it to

allow additional fields gracefully. The addition of suggested_commitments

must not break existing result card rendering.

This applies only to normal non-crisis responses.

Crisis payload shape is unchanged from V3A.

-----

SUGGESTED COMMITMENTS VALIDATION

If suggested_commitments is missing, not an array, empty, malformed, or has

fewer than 2 usable items, use fallback options:

- “Text a sober person now”

- “Go for a short walk”

- “Eat something and drink water”

- “Open a meeting or recovery resource”

If more than 4 items returned, show only first 4.

If fewer than 4, fill remaining slots with fallback options.

Never let missing or malformed suggested_commitments break the result card.

-----

CRISIS BYPASS RULE

V3C result-card features apply ONLY to normal check-in result cards.

If V3A crisis classifier returns crisis = true or risk_level = crisis:

- Do NOT render suggested commitments

- Do NOT render commitment section

- Do NOT render normal reach-out section

- Do NOT render normal result card

- Preserve the full-screen V3A crisis resource card UNCHANGED

- Do not alter V3A crisis behavior in any way

-----

COMMITMENT SELECTION: CHECK-IN RESULT CARD

After all existing normal result card sections, add a final section.

Section header: “What’s your one move right now?”

Display:

- 4 suggested_commitments as tappable pill buttons

- Small text input below pills with placeholder: “Or write your own…”

- Small low-emphasis “Skip for now” link below input

When user taps a pill or submits custom text:

- Immediately disable all commitment buttons

- Show saving state

- POST to /api/commitments with getCurrentUserId()

- commitment_text = selected text

- followup_scheduled_at = now() + stable_profile.commitment_followup_hours hours

(default 4 if missing or invalid)

- check_in_id = include if available, null if not

- On success: show confirmation text (fades in, stays visible):

“Noted. It’ll be waiting on Home when it’s time.”

- Keep buttons disabled after successful save

- Only one commitment per check-in result card

- On failure: re-enable buttons, show small inline error

NOTE ON WORDING: The confirmation text is exactly:

“Noted. It’ll be waiting on Home when it’s time.”

Do not use “Noted. I’ll check in with you later.” or any other variation.

Do not use wording that implies push notifications, email, or proactive outreach.

V3C follow-up is in-app Home banner ONLY. No push notifications. No email.

No browser notification API. No service worker. User sees it when they open Home.

-----

COMMITMENT API ENDPOINTS

POST /api/commitments

Request: { “check_in_id”: 123, “commitment_text”: “…” }

Response: { “saved”: true, “commitment”: { “id”: 1, “commitment_text”: “…”, “followup_scheduled_at”: “ISO8601” } }

GET /api/commitments/due

Returns oldest due incomplete commitment for current user.

Due = completed=false AND followup_scheduled_at <= now() AND created_at >= now() - 7 days

Response (due): { “has_due_commitment”: true, “commitment”: { “id”: 1, “commitment_text”: “…”, “created_at”: “…”, “followup_scheduled_at”: “…” } }

Response (none): { “has_due_commitment”: false }

POST /api/commitments/:id/respond

Request yes: { “response”: “yes” }

Request not_yet: { “response”: “not_yet” }

Request smaller: { “response”: “smaller”, “smaller_version”: “…” }

Response: { “saved”: true }

All endpoints use getCurrentUserId().

-----

FOLLOW-UP BANNER ON HOME

On every Home screen load, query GET /api/commitments/due.

Query logic:

- completed = false

- followup_scheduled_at <= now()

- created_at >= now() - interval ‘7 days’

- Do not limit to commitments created today

- If multiple due, show oldest first

- Show only one banner at a time

Banner text: “Earlier you said: [commitment_text]. Did you do it?”

Response buttons:

1. “Yes, done”

- completed = true, completed_at = now(), followup_response = ‘yes’

- Use appendEventLog(userId, event) from shared helpers:

{ type: “commitment”, summary: “User completed commitment: [text]” }

- Show brief varied acknowledgment from list:

“Good. That matters.” / “That counts.” / “Nice. You followed through.” / “That’s the work.”

- Dismiss banner

1. “Not yet”

- followup_response = ‘not_yet’

- Reschedule followup_scheduled_at = now() + 2 hours

- Dismiss banner

1. “Smaller version”

- Reveal small text input

- User types scaled-down version

- Save smaller_version, followup_response = ‘smaller’

- Reschedule followup_scheduled_at = now() + 2 hours

- Dismiss banner

- Use appendEventLog() to log smaller commitment

Dismiss (X button):

- Dismisses for current frontend session only

- Does NOT mark as complete

- Does NOT reschedule

- Does NOT modify database

- Banner may reappear on refresh

-----

EVENT LOG SAFETY

Use appendEventLog(userId, event) from shared helpers for ALL event log writes.

Do NOT implement separate event log logic in V3C.

After commitment events are appended, do NOT trigger recent_summary regeneration.

It is acceptable for recent_summary to update at next check-in or weekly summary.

event_log remains the source of truth for recent commitment activity.

-----

COMMITMENT COMPLETION RATE: INSIGHTS PAGE

Add to Insights page streak stats row:

“Commitments this week: X completed of Y made”

Compute server-side from commitments table using getCurrentUserId().

Y = commitments created during current week

X = commitments from Y where completed = true

If Y = 0, display: “No commitments logged this week yet.”

Simple stat card. No gamification. No badges. No streak celebration.

-----

HUMAN CONTACT SHORTCUTS: CHECK-IN RESULT CARD

Use buildHandoffPayload(stableProfile) from shared helpers.

Do NOT re-implement contact or meeting link loading.

Do NOT create a second handoff data model.

Phone numbers are in the payload for frontend rendering only — never for AI prompts.

When risk_level is moderate:

- Show “Reach out” section BELOW the commitment section

- Display each sober contact: tap-to-text (sms: URI) + tap-to-call (tel: URI)

- Display each meeting link as tap-to-open button

- Show “Tell on myself” button

When risk_level is high:

- Move “Reach out” section to TOP of result card, before all other sections

- Slightly larger tap targets

- Subtle highlight border around section

- Everything else same as moderate

If no contacts or meeting links saved:

- Show: “Add sober contacts in Settings to enable quick outreach.”

- Do not show empty buttons

-----

TELL ON MYSELF: CHECK-IN RESULT CARD

Default editable message:

“Hey. Having a hard time right now. [main_risk_factor from AI response if available]. Just telling on it.”

Implementation:

- Opens native SMS via sms: URI with body pre-filled

- Recipient: first saved sober contact phone number if available

- User edits in native SMS app before sending

- NOTHING is ever sent automatically

- Do not send SMS from server

If no contacts exist:

- Do not open sms: with empty recipient

- Show message text with a copy button

- Show: “Add sober contacts in Settings to enable one-tap texts.”

URI SAFETY:

- URL-encode sms body text

- Strip spaces and unsafe characters from phone numbers for tel: links

- Only render valid-looking meeting link URLs

- If sms: URI fails: show message text with copy button

- If tel: URI fails: show phone number with copy button

- If meeting URL is malformed: skip it, log console-side

-----

COMMITMENT FOLLOW-UP TIMING: SETTINGS

Add to existing Settings screen:

Label: “Check back on my commitment after”

Dropdown options: 2 hours, 4 hours (default), 6 hours, 8 hours, 12 hours

This setting saves to stable_profile.commitment_followup_hours (NOT app_settings).

Use the existing stable_profile update endpoint/flow.

Do not include “End of day” in V3C.

Do not build timezone-specific end-of-day logic.

-----

ERROR HANDLING

- If commitment save fails: show inline error, re-enable buttons, log server-side

- If follow-up banner query fails: catch error, skip banner silently

- If follow-up response save fails: show inline error in banner, do not dismiss

- If event_log update fails: log error, do not crash, do not block commitment save

- If sms: URI unsupported: show message text with copy button

- If tel: URI unsupported: show phone number with copy button

- If suggested_commitments missing: use fallback options, never crash result card

- If contacts/meeting_links malformed in stable_profile: treat as empty arrays

- No async operation in V3C should create an unhandled promise rejection

-----

SECURITY AND PRIVACY

- No-auth dev fork — private development only

- Phone numbers excluded from all AI prompts

- Frontend receives phone numbers only for handoff actions and crisis cards

- Do not send SMS automatically

- Do not send emails in V3C

- Do not store full AI responses in commitments

-----

ACCEPTANCE TESTS

1. App starts normally

1. Existing V3A and V3B functionality intact

1. commitments table exists with no FK on check_in_id

1. commitment_followup_hours is read from stable_profile, NOT app_settings

1. follow-up timing setting in Settings saves to stable_profile

1. suggested_commitments added to normal check-in AI schema

1. Existing parser updated to be backward-compatible with new field

1. Missing suggested_commitments falls back gracefully

1. Crisis responses do not render commitment UI

1. Commitment section appears at end of normal result cards

1. Confirmation text reads exactly: “Noted. It’ll be waiting on Home when it’s time.”

1. Duplicate commitment saves blocked

1. check_in_id saved when available, null when not

1. followup_scheduled_at computed from stable_profile.commitment_followup_hours

1. Home follow-up banner appears when commitment is due

1. Banner works for commitments created on prior days (not just today)

1. “Yes, done” marks complete + appends to event_log via appendEventLog()

1. “Not yet” reschedules by 2 hours

1. “Smaller version” saves and reschedules

1. Banner X dismisses for current session only, no DB change

1. Commitment completion rate appears on Insights

1. Moderate risk shows Reach out below commitment section

1. High risk shows Reach out at TOP of result card

1. buildHandoffPayload() used — no separate contact parsing

1. Phone numbers excluded from AI prompts

1. tel: URI used for calls

1. sms: URI used for texts

1. Tell on myself opens editable SMS draft, never sends automatically

1. If no contacts: show copyable message, no broken sms link

1. event_log updates do NOT trigger recent_summary regeneration

1. Event log failures caught, do not crash server

-----

AT THE END

When finished, report: what was implemented, files changed, database migrations added,

shared helpers confirmed reused (not duplicated), known issues or skipped items,

environment variables needed, exact next step for V3D. Keep under 300 words.

Run as a persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.

V3D

# V3D

Upgrade the existing recovery check-in app to V3D only.

Important constraints:

- Do NOT build email outreach, TTS, or any other features

- Focus only on voice input via OpenAI Whisper API on three specific fields

- V3A, V3B, and V3C must already be in place

- The app uses plain HTML, CSS, and vanilla JavaScript — not React

- Extend what exists — do not rebuild from scratch

- Keep all existing dark theme, UI, and functionality intact

-----

PRE-FLIGHT

Inspect the current implementation. Confirm in 5 bullets:

1. Relevant files to modify

1. Existing V3 shared helpers to reuse

1. Database/schema impact (none expected)

1. Conflicts with prior phases

1. Implementation plan

Then proceed.

-----

V3 INVARIANTS

Preserve all V3 invariants throughout this phase:

- Use getCurrentUserId() everywhere. No hardcoded user IDs.

- stable_profile is the source of truth for all user preferences

- Phone numbers never appear in AI prompts

- No raw voice transcripts stored in the database

- No audio files written to disk

- All background async operations use safeBackgroundTask()

- No unhandled promise rejections

-----

V3D GOALS

1. Add voice input to the check-in notes field

1. Add voice input to the check-in grateful field

1. Add voice input to the chat message input field

1. Handle all mobile browser mic permissions and format compatibility gracefully

-----

NO NEW DATABASE CHANGES NEEDED FOR THIS PHASE

-----

REQUIRED PACKAGES

None — use existing OpenAI SDK (already installed)

No new Replit Secrets needed — voice transcription uses existing OPENAI_API_KEY

-----

BACKEND ENDPOINT

POST /api/transcribe

- Accepts: multipart/form-data with one field named “audio” containing the audio file

- Calls OpenAI Whisper API:

model: whisper-1

language: en

response_format: json

- Returns: { “text”: “transcribed text here” }

- Max audio file size: 10MB — reject larger files with 400 error

- Request timeout: 15 seconds — return 500 if exceeded

- On any failure: return { “error”: “Transcription failed. Please try again or type instead.” }

- Use existing OpenAI SDK instance — no new client needed

- Use multer.memoryStorage() — do NOT write audio files to disk

- Do NOT log transcript content server-side

- Do NOT store transcript text in the database

-----

AUDIO FORMAT DETECTION (frontend)

Before starting any recording, detect supported formats:

const mimeType = MediaRecorder.isTypeSupported(‘audio/webm;codecs=opus’)

? ‘audio/webm;codecs=opus’

: MediaRecorder.isTypeSupported(‘audio/webm’)

? ‘audio/webm’

: MediaRecorder.isTypeSupported(‘audio/mp4’)

? ‘audio/mp4’

: null;

If mimeType is null: MediaRecorder not supported — hide all mic buttons silently, no error shown.

-----

MICROPHONE BUTTON — WHERE IT APPEARS

Add a microphone button to exactly THREE fields:

1. Notes textarea on the full check-in form

1. Grateful text input on the full check-in form

1. Chat message input field

Do not add mic buttons anywhere else.

-----

MICROPHONE BUTTON DESIGN

- Small circular button, positioned to the right of or directly below the field

- Icon: inline SVG microphone (no external library)

- Three visual states:

Default: dim, unobtrusive, matches dark theme

Recording: pulsing red dot indicator, button slightly highlighted

Loading: simple CSS spinner while transcription processes

- Minimum tap target: 44px x 44px

-----

RECORDING FLOW — STEP BY STEP

1. User taps mic button

1. Call navigator.mediaDevices.getUserMedia({ audio: true })

1. If permission denied or error:

- Show inline message below field: “Mic access needed. Enable it in your browser settings.”

- Message fades after 4 seconds

- Return button to default state

- Do not hide button permanently

1. If permission granted:

- Create MediaRecorder with detected mimeType

- Start recording

- Show recording indicator (pulsing red)

- Show subtle timer: “0:00”, “0:01”, etc.

1. User taps mic button again to stop

OR recording auto-stops at 60 seconds with message: “Max length reached”

1. Show loading spinner on button

1. Collect audio chunks into a Blob

1. Create FormData, append blob as “audio”

1. POST to /api/transcribe

1. On success:

- Append transcribed text to existing field value with a space separator

- Never replace existing text

- Focus the field so user can review and edit

- Return button to default state

1. On error:

- Show inline error below field (see error handling)

- Return button to default state

RECORDING LIMITS:

- Maximum recording time: 60 seconds (not 90, not 180)

- Auto-stop at 60 seconds

- Show timer during recording: “0:23” format

- Timer resets on each new recording

Only one active recording at a time globally.

Stop any existing recording before starting a new one.

Stop MediaStream tracks after recording completes (release mic).

-----

CHAT VOICE INPUT — SPECIFIC BEHAVIOR

- Mic button sits inside the chat input row, to the right of the text input

- After transcription: text appears in the chat input field

- User reviews and taps Send manually

- Transcription does NOT auto-send — this is intentional

- Chat mic button is disabled while chat is in a sending/waiting state

-----

CHECK-IN VOICE INPUT — SPECIFIC BEHAVIOR

- Notes and grateful mic buttons sit below each respective field

- Transcribed text APPENDS to any existing content with a space

- User can record multiple times — each appends to previous

- Mic buttons do not interfere with form submission

-----

MOBILE BROWSER COMPATIBILITY

- iOS Safari: requires HTTPS (Replit preview uses HTTPS — works)

- iOS Safari: may not support audio/webm — fallback to audio/mp4 handles this

- Android Chrome: supports audio/webm — primary format

- If MediaRecorder entirely unavailable: hide all mic buttons, no error, no fallback UI

-----

ERROR HANDLING

- Transcription timeout: “Taking too long. Please try again or type instead.”

- Network error during upload: “Couldn’t reach the server. Type instead for now.”

- Empty transcription (blank text returned): “Nothing was captured. Try again.”

- Mic permission denied: “Mic access needed. Enable it in your browser settings.”

- All inline errors appear below the relevant field

- All inline errors fade after 4 seconds

- No error should block form submission or chat sending

-----

SECURITY AND PRIVACY

- No audio files written to disk

- No transcript text stored in database

- No transcript text logged server-side

- multer.memoryStorage() only

- Existing OPENAI_API_KEY used — no new secrets needed

-----

AT THE END

When finished, report: what was implemented, files changed, whether voice input works

on all three target fields, whether 60-second limit is implemented, whether audio/webm

and audio/mp4 fallback detection is in place, whether transcription appends (not

replaces) existing content, whether chat voice does not auto-send, whether no audio

is written to disk, exact next step for V3E. Keep under 300 words.

Run as a persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.

V3E

# V3E

Upgrade the existing recovery check-in app to V3E only.

Important constraints:

- Do NOT build TTS, push notifications, SMS outreach, WhatsApp, or any other features

- Focus only on proactive email outreach:

1. Daily check-in reminder emails

1. Missed check-in follow-up emails

1. Weekly summary emails

1. Settings UI for email/reminder preferences

1. Test email button

- V3A through V3D must already be in place

- stable_profile is the single source of truth for email, reminder_time, timezone,

reminder_enabled, and weekly_summary_enabled

- Do NOT duplicate these fields into app_settings

- app_settings stores only: onboarding_version, migration flags, and

email send-tracking dates (last_daily_reminder_sent_date, etc.)

- Extend what exists. Do not rebuild from scratch.

- Preserve all prior V3 phase behavior

-----

PRE-FLIGHT

Inspect the current implementation. Confirm in 5 bullets:

1. Relevant files to modify

1. Existing V3 shared helpers to reuse

1. Database/schema impact

1. Conflicts with prior phases

1. Implementation plan

Then proceed.

-----

V3 INVARIANTS

Preserve all V3 invariants throughout this phase:

- Use getCurrentUserId() everywhere. No hardcoded user IDs.

- stable_profile is the source of truth for ALL user preferences

- Phone numbers never appear in AI prompts or emails

- event_log cap is 90 entries, appendEventLog() used for all appends

- All background async operations use safeBackgroundTask()

- No unhandled promise rejections

-----

V3E GOALS

1. Send daily check-in reminder email at user’s configured local time

1. Send missed check-in follow-up email if no check-in for 2+ days

1. Send weekly summary email every Sunday evening in user’s local timezone

1. Let user configure email, reminder time, timezone, and toggles in Settings

1. Let user send a test email from Settings

1. All emails plain text only

1. Prevent duplicate email sends

1. Keep all cron/scheduler errors from crashing the server

-----

SCHEDULER RELIABILITY NOTE

node-cron is acceptable for Replit preview/dev testing only.

For production reliability, email jobs require a reserved VM or external scheduler.

Implement node-cron for preview/dev testing and include clear code comments

explaining this limitation. Do not claim production-grade scheduling reliability.

-----

EMAIL OUTREACH FEATURE FLAG

IMPORTANT: Scheduled email sending must be gated behind an environment flag.

Check process.env.EMAIL_OUTREACH_ENABLED before executing any scheduled send.

If this variable is not exactly “true”, skip all scheduled sends silently.

Log a server-side note that outreach is disabled.

The Settings test email button may still work independently of this flag,

as long as Resend env vars are present.

This lets you test email manually without the scheduler accidentally sending.

Add EMAIL_OUTREACH_ENABLED to the list of Replit Secrets for V3E.

-----

REQUIRED PACKAGES

Install if missing:

npm install resend node-cron luxon

Use:

- resend for email sending

- node-cron for dev/preview scheduler

- luxon for timezone-aware date math

- existing OpenAI SDK/client for email body generation

-----

RESEND SETUP

Add to Replit Secrets:

- RESEND_API_KEY

- RESEND_FROM_EMAIL

- EMAIL_OUTREACH_ENABLED (set to “true” to enable scheduled sends)

If RESEND_API_KEY or RESEND_FROM_EMAIL is missing:

- Disable email sending gracefully

- Do not crash the server

- Settings test email returns clear error if env vars are missing

- Cron jobs log a server-side warning and skip sending

Resend call pattern:

const { Resend } = require(“resend”);

const resend = new Resend(process.env.RESEND_API_KEY);

await resend.emails.send({

from: process.env.RESEND_FROM_EMAIL,

to: userEmail,

subject: subject,

text: body

});

Do NOT expose RESEND_API_KEY to the frontend.

Do NOT send HTML emails — plain text only.

-----

DATABASE: ADD TO app_settings IF THEY DO NOT EXIST

Email send-tracking metadata ONLY (NOT user preferences):

- last_daily_reminder_sent_date varchar nullable

- last_missed_followup_sent_date varchar nullable

- last_weekly_summary_sent_week varchar nullable

Store local send dates as strict Luxon-generated YYYY-MM-DD strings.

Store weekly summary dedupe as local ISO week key, e.g. “2026-W17”.

Compare send dates string-to-string.

DO NOT add to app_settings:

- email (lives in stable_profile)

- reminder_time (lives in stable_profile)

- timezone (lives in stable_profile)

- reminder_enabled (lives in stable_profile)

- weekly_summary_enabled (lives in stable_profile)

- commitment_followup_hours (lives in stable_profile — added in V3C)

Do not destructively rename or drop existing app_settings columns.

If old tracking columns exist (e.g., last_reminder_sent_date), leave them

but do not rely on them for V3E. Use the new split tracking columns above.

-----

USER DATA LOADING RULE

Use getCurrentUserId() for all queries.

For this no-auth dev fork, process only the current dev user.

Do not build true multi-user batch sending.

For each scheduler run, load:

- user_memory for getCurrentUserId() → parse stable_profile for:

email, reminder_time, timezone, reminder_enabled, weekly_summary_enabled,

recent_summary, event_log

- app_settings for send-tracking fields (last_daily_reminder_sent_date, etc.)

- check_ins only if last_checkin_local_date is missing from user_memory

(last_checkin_local_date in user_memory is the fast path — see V3A Revision Patch)

Do not pass raw check-in notes, raw grateful text, full check-in objects,

full chat history, or raw voice transcripts into email generation.

-----

TIMEZONE HANDLING

Use luxon for all timezone math.

Read timezone from stable_profile.timezone.

If missing or invalid, default to “America/New_York” and log server-side warning.

const { DateTime } = require(“luxon”);

const userNow = DateTime.now().setZone(userTimezone);

Use user’s local timezone for:

- Today’s date (YYYY-MM-DD)

- Reminder time comparison

- Missed check-in day count

- Sunday evening weekly summary timing

- ISO week key for weekly summary dedupe

Reminder time format: “HH:mm” from stable_profile.reminder_time.

If missing or invalid, default to “08:00”.

-----

EMAIL VALIDATION

Validate email format before saving and before sending.

If invalid during scheduler run: skip sending, log server-side, do not crash.

If user enters invalid email in Settings: show inline error.

-----

CRON SCHEDULER SETUP

Set up node-cron in server startup file.

Wrap ALL cron logic in try/catch.

Cron errors must never crash the Express server.

Single scheduler, runs every 15 minutes:

*/15 * * * *

The scheduler calls these functions in order:

1. runMissedFollowupCheck()

1. runDailyReminderCheck()

1. runWeeklySummaryCheck()

Order matters — missed follow-up supersedes daily reminder for the same local date.

Weekly summary can still send on same day as a daily/missed email (different type).

Each function must:

- First check process.env.EMAIL_OUTREACH_ENABLED === “true”

- If not: log “email outreach disabled, skipping” and return

- Then proceed with its logic

-----

ONE OUTREACH EMAIL PER DAY RULE

Do not send both a missed follow-up AND a daily reminder to the same user on the

same local date.

If user has missed 2+ days:

- Missed follow-up supersedes the normal daily reminder

- Mark last_missed_followup_sent_date after sending

- Do not send daily reminder that same local date

Weekly summary and test email are exceptions to this rule.

-----

SCHEDULER FUNCTION 1: MISSED CHECK-IN FOLLOW-UP

Logic:

1. Check EMAIL_OUTREACH_ENABLED === “true”. If not: skip.

1. Check RESEND env vars exist. If not: skip.

1. Load stable_profile.email, reminder_time, timezone.

1. Validate email. If invalid or empty: skip.

1. Load app_settings.

1. Check reminder_enabled (from stable_profile) is true. If false: skip.

1. Get userNow in user timezone via luxon.

1. Compute userLocalDate as YYYY-MM-DD string.

1. If last_missed_followup_sent_date === userLocalDate: skip.

1. If last_daily_reminder_sent_date === userLocalDate: skip.

1. Build today’s reminder DateTime from userLocalDate + reminder_time.

1. Check if userNow is >= today’s reminder time AND < reminder time + 15 minutes.

1. If NOT inside the 15-minute reminder window: skip.

Do not send missed follow-up emails immediately after midnight.

1. Check last_checkin_local_date in user_memory.

If last_checkin_local_date is available and not null:

Compute days since last check-in using luxon.

If last_checkin_local_date is null: fall back to querying check_ins table.

1. If no check-ins exist at all for this user: skip entirely.

Do not attempt to detect onboarding timestamps. Missed follow-up is

only for users who have an established check-in history.

1. If days since last check-in >= 2 AND inside reminder window:

- Generate missed follow-up email body

- Send via Resend

- Update last_missed_followup_sent_date = userLocalDate

-----

SCHEDULER FUNCTION 2: DAILY REMINDER

Logic:

1. Check EMAIL_OUTREACH_ENABLED === “true”. If not: skip.

1. Check RESEND env vars exist. If not: skip.

1. Load stable_profile.email, reminder_time, timezone.

1. Validate email. If invalid or empty: skip.

1. Load app_settings.

1. Check reminder_enabled (from stable_profile) is true. If false: skip.

1. Get userNow in user timezone via luxon.

1. Compute userLocalDate as YYYY-MM-DD string.

1. If last_daily_reminder_sent_date === userLocalDate: skip.

1. If last_missed_followup_sent_date === userLocalDate: skip.

1. Check last_checkin_local_date in user_memory.

If it matches userLocalDate: skip (user already checked in today).

If null: fall back to querying check_ins table.

1. Build today’s reminder DateTime from userLocalDate + reminder_time.

1. If userNow >= reminder time AND < reminder time + 15 minutes:

- Generate daily reminder email body

- Send via Resend

- Update last_daily_reminder_sent_date = userLocalDate

Note: If server restarts and the 15-minute window has already passed without

sending, accept the miss. Do not attempt catch-up sends on restart. The next

day will try again.

-----

SCHEDULER FUNCTION 3: WEEKLY SUMMARY

Logic:

1. Check EMAIL_OUTREACH_ENABLED === “true”. If not: skip.

1. Check RESEND env vars exist. If not: skip.

1. Load stable_profile.email, timezone, recent_summary, event_log.

1. Validate email. If invalid or empty: skip.

1. Load app_settings.

1. Check weekly_summary_enabled (from stable_profile) is true. If false: skip.

1. Get userNow in user timezone via luxon.

1. Check userNow.weekday === 7 (Luxon: Sunday = 7).

1. Check userNow.hour === 18 AND userNow.minute < 15.

1. Compute local ISO week key, e.g. “2026-W17”.

1. If last_weekly_summary_sent_week === current ISO week key: skip.

1. Generate weekly summary from allowed data only (see below).

1. Send weekly summary via Resend.

1. Update last_weekly_summary_sent_week = current ISO week key.

Weekly summary allowed data:

- recent_summary

- last 7 event_log entries as plain text

- aggregate check-in stats for last 7 days (count, avg mood, avg craving,

avg sleep if available, avg energy if available)

- sobriety tracker status if available

Do NOT pass: raw notes, raw grateful text, full check-in objects,

full chat history, raw voice transcripts, phone numbers, contact details.

-----

EMAIL CONTENT RULES

All emails:

- Plain text only. No markdown. No HTML. No bullet points unless necessary.

- Direct, warm, non-shaming tone

- Do not use the word “journey”

- Do not imply Anchor is a human sponsor

- Do not imply Anchor is monitoring emergencies in real time

- Do not use dramatic or alarmist language

- Do not claim the app can guarantee safety

- End with simple invitation to open app or contact real person if needed

- Append this footer to every email:

“\n\n—Anchor\nTo change these emails, open the app settings.”

DAILY REMINDER EMAIL

Subject: “Check in with Anchor”

System prompt for body generation:

“Write a brief 2-3 sentence daily check-in prompt. Reference the user’s recent

patterns if provided. Tone: direct, warm, non-shaming. Do not use the word ‘journey’.

Do not imply you are a human sponsor. Do not imply real-time monitoring. End with

one short question. Plain text only.”

Input: recent_summary truncated to 500 chars + last 3 event_log entries

Fallback (if OpenAI fails): “Haven’t heard from you today. How are you doing? Check in when you’re ready.”

MISSED CHECK-IN EMAIL

Subject: “Checking in”

System prompt: “Write a brief 2-3 sentence message for someone who has not checked

in for [X] days. Last check-in: [risk level and one-line summary if available].

Tone: warm, zero pressure, zero shame. Do not imply you are a human sponsor.

Plain text only.”

Fallback: “Haven’t heard from you in a couple of days. No pressure. Just checking in.”

WEEKLY SUMMARY EMAIL

Subject: “Your week with Anchor”

System prompt: “Write a plain text weekly recovery summary. Include: check-in

consistency, average mood and craving if available, sobriety tracker status if

available, one honest observation about patterns, one suggested focus for the

coming week. Tone: direct, honest, sponsor-like, but do not imply you are a

human sponsor. Under 200 words. Plain text only, no markdown, no bullet points,

no headers. Do not use the word ‘journey’.”

Input: recent_summary + last 7 event_log entries + aggregate stats + tracker status

Fallback: “Here’s a quick look at your week. Keep checking in — consistency is the work.”

OpenAI generation fallback rule:

If OpenAI fails but send eligibility conditions are met: use fallback text and send.

If send eligibility is invalid: skip entirely.

-----

SETTINGS UI: EMAIL AND REMINDERS SECTION

Add “Email & Reminders” section to existing Settings screen.

Fields:

1. Email address — reads/writes stable_profile.email

1. Reminder time — reads/writes stable_profile.reminder_time (default “08:00”)

1. Timezone — reads/writes stable_profile.timezone (default “America/New_York”)

Include: America/New_York, America/Chicago, America/Denver, America/Los_Angeles,

America/Phoenix, Pacific/Honolulu, Europe/London, Europe/Paris, Asia/Dubai,

Asia/Singapore, Asia/Tokyo, Asia/Makassar, Australia/Sydney

1. Daily reminder toggle — reads/writes stable_profile.reminder_enabled

1. Weekly summary toggle — reads/writes stable_profile.weekly_summary_enabled

1. Send test email button

1. Save button

All fields read from stable_profile, NOT from app_settings.

All fields save to stable_profile via the existing stable_profile update flow.

Do NOT duplicate any of these fields into app_settings.

-----

SETTINGS API REQUIREMENTS

GET /api/email/settings

Returns:

{

“email”: “…”,

“reminder_time”: “08:00”,

“timezone”: “America/New_York”,

“reminder_enabled”: true,

“weekly_summary_enabled”: true,

“resend_configured”: true

}

Read email, reminder_time, timezone, reminder_enabled, weekly_summary_enabled

from user_memory.stable_profile.

Include resend_configured = true if RESEND_API_KEY and RESEND_FROM_EMAIL both exist.

Do not include any API keys.

POST /api/email/settings

Request: { email, reminder_time, timezone, reminder_enabled, weekly_summary_enabled }

- Validate email format if non-empty

- Validate reminder_time is HH:mm

- Validate timezone using luxon

- Save all five fields to user_memory.stable_profile

- Use getCurrentUserId()

- Return JSON success or validation errors

POST /api/email/test

- Load stable_profile.email for getCurrentUserId()

- Validate email exists and is valid

- Validate RESEND env vars exist

- Send plain text test email

- Test email subject: “Anchor test email”

- Test email body: “This is a test email from Anchor. Email reminders are connected.\n\n—Anchor\nTo change these emails, open the app settings.”

- Return { “sent”: true } on success, JSON error on failure

- Do NOT expose API keys to frontend

- Test emails must NOT update any scheduler tracking fields

-----

ERROR HANDLING

Resend errors: log concisely server-side, do not crash cron or Express.

OpenAI generation errors: use fallback text if send eligibility valid.

Scheduler errors: wrap each function in try/catch, no unhandled rejections.

Settings: inline errors for invalid email/timezone/reminder_time.

Missing Resend env vars: show inline error on test email only, do not crash server.

Data errors: if stable_profile missing, skip sending; if event_log malformed,

treat as []; if recent_summary missing, use fallback copy.

-----

SECURITY AND PRIVACY

- No-auth dev fork — private development only

- Do not expose Resend API keys

- Do not send phone numbers in emails

- Do not include raw transcript text from V3D in emails

- Do not include full chat history in emails

- Do not include raw notes or raw grateful text in emails

- Use recent_summary, event_log summaries, and aggregated stats only

- All email sending is server-side only

-----

ACCEPTANCE TESTS

1. App starts normally; all prior V3 functionality intact

1. resend, node-cron, luxon installed

1. app_settings has last_daily_reminder_sent_date (varchar)

1. app_settings has last_missed_followup_sent_date (varchar)

1. app_settings has last_weekly_summary_sent_week (varchar)

1. stable_profile is confirmed source of truth for email, reminder_time, timezone,

reminder_enabled, weekly_summary_enabled — these are NOT in app_settings

1. Email & Reminders section appears in Settings

1. Settings loads from stable_profile correctly

1. Settings saves to stable_profile correctly

1. Test email works when Resend env vars and email are valid

1. Test email returns clear error when Resend env vars missing

1. Test email does NOT update any scheduler tracking fields

1. Scheduler registered on server startup

1. Scheduler runs every 15 minutes

1. EMAIL_OUTREACH_ENABLED must be “true” for scheduled sends

1. Daily reminder skips if EMAIL_OUTREACH_ENABLED != “true”

1. Daily reminder uses user local timezone and 15-minute window

1. Daily reminder skips if check-in already exists for local today

1. Daily reminder skips if already sent today

1. Daily reminder skips if missed follow-up already sent today

1. Missed follow-up sends only after 2+ days without check-in

1. Missed follow-up sends only inside user’s 15-minute reminder window

1. Missed follow-up does not fire immediately after midnight

1. If no check-ins exist at all: missed follow-up skipped entirely

1. Missed follow-up supersedes daily reminder for same local date

1. Weekly summary uses user local Sunday evening

1. Weekly summary dedupes by ISO week key

1. Weekly summary uses only allowed data — no raw notes, no raw transcripts

1. All emails are plain text with footer

1. OpenAI failure falls back to plain text when send eligibility valid

1. Missing/invalid email skips sends

1. Missing Resend env vars skip scheduled sends without crashing

1. Cron errors caught, no server crash, no unhandled promise rejections

1. getCurrentUserId() used everywhere, no hardcoded IDs

-----

AT THE END

When finished, report: what was implemented, files changed, packages added,

database migrations added, whether stable_profile confirmed as source of truth

(not app_settings), whether EMAIL_OUTREACH_ENABLED flag is implemented,

whether scheduler runs on startup, known issues or skipped items, environment

variables required in Replit Secrets (including EMAIL_OUTREACH_ENABLED),

reminder that node-cron in Replit preview is for dev/testing only,

exact next step for V3F. Keep under 300 words.

Run as a persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.

Smoke tests

Add Playwright smoke tests for V3E email outreach features. Do not modify any existing tests. Append after test 32. These are permanent additions to the suite.

Test 33 — Email and Reminders section appears in Settings

Navigate to Settings. Assert that an “Email & Reminders” or equivalent section is visible containing at least an email input field, a reminder time field, and a timezone selector.

Test 34 — Settings loads email preferences from stable_profile

Navigate to Settings Email & Reminders section. Intercept GET /api/email/settings. Assert the response contains email, reminder_time, timezone, reminder_enabled, and weekly_summary_enabled fields. Assert the response does NOT contain RESEND_API_KEY or any API key string.

Test 35 — Settings saves email preferences to stable_profile

Enter a valid email address, set reminder_time to “09:00”, select a timezone. Tap Save. Intercept POST /api/email/settings. Assert the request body contains all five fields. Assert the response indicates success. Navigate away and back. Assert the saved values are still present.

Test 36 — Email validation rejects invalid format

Enter “notanemail” in the email field. Tap Save. Assert an inline validation error appears near the email field. Assert no POST request to /api/email/settings was made with the invalid value.

Test 37 — reminder_enabled and weekly_summary_enabled save to stable_profile not app_settings

Toggle reminder_enabled off. Save. Call GET /api/email/settings. Assert reminder_enabled is false in the response. Then call GET /api/app-settings or inspect via a debug endpoint if available. Assert reminder_enabled does NOT appear as a column value in app_settings. If no debug endpoint exists, assert the GET /api/email/settings response reads from stable_profile by verifying the field is present there via GET /api/memory or equivalent.

Test 38 — Test email button sends when Resend is configured

With RESEND_API_KEY and RESEND_FROM_EMAIL present in environment and a valid email saved. Tap the Send test email button. Assert the response returns { “sent”: true }. Assert no API key is present in the response body.

Test 39 — Test email button returns clear error when Resend not configured

Mock missing Resend environment variables or intercept the test email endpoint to simulate missing config. Tap Send test email. Assert an inline error message appears. Assert the app does not crash. Assert the error does not expose any API key string.

Test 40 — Test email does not update scheduler tracking fields

Note the current values of last_daily_reminder_sent_date and last_missed_followup_sent_date before sending test email. Send a test email. Assert those two tracking fields are unchanged after the test send.

Test 41 — Scheduler does not send when EMAIL_OUTREACH_ENABLED is not true

If a debug or admin endpoint exists to trigger the scheduler manually, call it with EMAIL_OUTREACH_ENABLED unset or set to “false”. Assert no email send attempt is made to Resend. Assert the server logs or response indicates outreach is disabled. If no trigger endpoint exists, assert that the scheduler setup code contains a check for process.env.EMAIL_OUTREACH_ENABLED === “true” by inspecting the source.

Test 42 — GET /api/email/settings reads from correct sources

Call GET /api/email/settings. Assert email, reminder_time, and timezone come from user_memory.stable_profile. Assert reminder_enabled and weekly_summary_enabled come from stable_profile. Assert last_daily_reminder_sent_date and last_missed_followup_sent_date are NOT present in the settings response — those are app_settings tracking fields only.

Test 43 — No Resend API key exposed to frontend

Intercept all API responses during a full Settings page load and a test email send. Assert that no response body contains the string value of RESEND_API_KEY. Assert no response body contains the pattern “re_” followed by alphanumeric characters which is the Resend key format.

Test 44 — commitment_followup_hours still in stable_profile after V3E

Call GET /api/email/settings or GET /api/memory. Assert commitment_followup_hours is present in stable_profile. Assert it does NOT appear as a standalone column in app_settings. This is a regression guard confirming V3C’s storage decision survived V3E’s database work.

V3F1

# V3F1: TEXT TO SPEECH

Upgrade the existing recovery check-in app with TTS only.

STACK CONTEXT:

This app uses React/TypeScript on the frontend and Node.js/Express

on the backend. Write frontend code as React components and hooks.

Do not write vanilla JS inside React components. Ignore any prior

references to “plain HTML, CSS, and vanilla JavaScript.”

Important constraints:

- Do NOT add new database tables or columns

- Do NOT add new product features

- Focus only on /api/speak and the two TTS surfaces:

check-in result card and chat

- V3A through V3E must already be in place

- Extend what exists. Do not rebuild from scratch.

- Preserve all prior V3 phase behavior

-----

PRE-FLIGHT

Inspect current implementation. Confirm in 5 bullets:

1. Relevant files to modify

1. Whether existing OpenAI SDK/client is available

1. Whether /api/speak already exists (do not duplicate if it does)

1. Conflicts with prior phases

1. Implementation plan

Then proceed.

-----

V3 INVARIANTS

Preserve all V3 invariants:

- getCurrentUserId() everywhere, no hardcoded IDs

- Phone numbers never in AI prompts

- No audio files written to disk

- No raw notes, no raw transcripts, no user messages sent to TTS

- All background async operations use safeBackgroundTask()

-----

TTS GOALS

1. Add /api/speak backend endpoint

1. Add Listen button to check-in result card (reminder/Remember

section only)

1. Add speaker icon to sponsor chat message bubbles only

1. Create global audio manager — one stream at a time, stops

on navigation

-----

NO DATABASE CHANGES

No new tables. No new columns. None.

-----

REQUIRED PACKAGES

No new packages. Use existing OpenAI SDK.

Optional environment variables (no new secrets required unless

OPENAI_API_KEY is missing):

- OPENAI_TTS_MODEL (default: “tts-1”)

- OPENAI_TTS_VOICE (default: “onyx”)

-----

BACKEND: POST /api/speak

Request: { “text”: “…”, “context”: “checkin|chat” }

Response: audio/mpeg on success, JSON error on failure

Backend behavior:

- Validate request body exists

- Validate text is a non-empty string; trim it

- Reject empty text with 400 JSON error

- Validate context field: if value is not “checkin” or “chat”,

return 400 { “error”: “Invalid context” } and log the invalid

value server-side

- Apply context-specific truncation:

checkin: max 500 characters

chat: max 1000 characters

invalid/unknown: max 800 characters

- Truncate at nearest sentence boundary before limit if possible

- If no sentence boundary: truncate at nearest word boundary

- Do NOT send: raw check-in notes, raw grateful text, raw voice

transcripts, full chat history, crisis resources, user messages

- Only convert existing sponsor-facing text already visible to

the user

OpenAI call:

- Model: process.env.OPENAI_TTS_MODEL || “tts-1”

Do NOT default to “gpt-4o-mini-tts”

- Voice: process.env.OPENAI_TTS_VOICE || “onyx”

- response_format: mp3

- Use client.audio.speech.create if SDK supports it

- Return audio bytes with Content-Type: audio/mpeg

- If configured model fails (unsupported model, 400

model-not-found, etc.): retry ONCE with “tts-1”.

Do not enter infinite retry loop.

If first model was already “tts-1”, do not retry.

Backend timeout: 20 seconds. On timeout: return 500 JSON error.

Catch all OpenAI errors. Log concisely server-side.

Do not log full text content.

Return: { “error”: “Audio unavailable” } on any failure.

Never crash the Express server on TTS failure.

Do NOT write audio to disk. Stream bytes directly to response.

-----

FRONTEND: GLOBAL AUDIO MANAGER

Create one shared audio manager as a React module or hook

that can be imported by both the result card and chat components.

On every tab switch, route change, new check-in submit, new chat

conversation, crisis screen render, Settings navigation, or major

view change:

- If activeAudio exists: call activeAudio.pause()

- Set activeAudio.currentTime = 0 where possible

- Revoke any active object URL

- Clear activeAudio and activeAudioUrl references

- Reset all Listen/speaker buttons to idle state

Do not let TTS continue playing invisibly after user leaves

the screen.

-----

IOS SAFARI AUDIO PLAYBACK

For mobile Safari compatibility:

- Instantiate the Audio object SYNCHRONOUSLY inside the user

tap handler BEFORE starting the async fetch to /api/speak

- Store as activeAudio in the audio manager

- After /api/speak resolves: create Blob URL, set activeAudio.src

- Then call activeAudio.play()

- If play() rejected: show small “Tap again to play” fallback

- Do not treat playback rejection as fatal error

- Always revoke Blob URLs after playback ends or is stopped

-----

GENERAL TTS RULES

- TTS is always user-initiated. Never autoplay.

- Only one audio stream at a time globally

- Starting a new stream stops any current audio

- Stop audio on: user taps Stop, playback ends naturally, user

changes tabs, user starts new chat conversation, user submits

new check-in, user opens crisis screen, user navigates to

any other screen

- Revoke object URLs after use

- If audio fails: show small inline error “Audio unavailable

right now.”

- Do not block the app if TTS fails

- Re-enable Listen/speaker button after success, error, or stop

-----

TTS ON CHECK-IN RESULT CARD

Add a small “Listen” button below the reminder/Remember section

ONLY.

Button: inline SVG play icon + label “Listen”

On tap:

- Instantiate Audio object synchronously before fetch (iOS rule)

- POST to /api/speak with reminder text, context = “checkin”

- Play returned audio

While playing: button label swaps to “Stop”. Tapping stops

playback.

After playback ends naturally: return button to “Listen”.

After user taps Stop: reset activeAudio.currentTime = 0,

return button to “Listen” so audio can be restarted cleanly.

Do NOT add TTS to: state_summary, next_moves,

recovery_support_prompt, raw notes, suggested_commitments,

or crisis cards.

-----

TTS ON CHAT BUBBLES

Add small inline SVG speaker icon to each SPONSOR message

bubble only.

- No label — icon only

- No speaker icon on user messages

- No speaker icon on crisis resource cards

- Position at bottom-right of sponsor bubble

- Subtle styling that matches dark theme

- Minimum tap target: 44px x 44px

On tap:

- Instantiate Audio object synchronously before fetch (iOS rule)

- POST to /api/speak with that sponsor message text only,

context = “chat”

- Only one audio stream at a time — tapping a new sponsor

message stops current playback

- Do not autoplay

- Do not send full chat history

-----

AT THE END

When finished, report: /api/speak implemented, TTS model and

voice defaults confirmed, Listen button on check-in reminder

section confirmed, speaker icon on sponsor chat messages

confirmed, TTS never auto-plays confirmed, one audio stream

at a time confirmed, audio stops on tab/view change confirmed,

audio not stored on disk confirmed, iOS Safari tap-handler

audio instantiation confirmed, context validation with 400

on invalid context confirmed, Stop button resets audio state

for clean restart confirmed, known issues or skipped items,

exact next step for V3F2. Keep under 300 words.

V3F2

V3F2: ONBOARDING + ANIMATION POLISH

Upgrade the existing recovery check-in app with onboarding refinement

and animation polish only.

Important constraints:

- Do NOT add new database tables or columns

- Do NOT add new product features

- Focus only on: onboarding refinement, tab fade, result card animations,

chat bubble animations, and direction-aware onboarding transitions

- V3F1 TTS must already be in place

- Plain HTML, CSS, vanilla JavaScript only

- Extend what exists. Do not rebuild from scratch.

- Preserve all prior V3 phase behavior

-----

PRE-FLIGHT

Inspect current implementation. Confirm in 5 bullets:

1. Current onboarding step count (should be 9)

1. Whether Back buttons already exist on all steps

1. Whether tab switching uses display:none / display:block or something else

1. Files to modify

1. Implementation plan

Then proceed.

-----

NO DATABASE CHANGES

No new tables. No new columns. None.

-----

ONBOARDING REFINEMENT

IMPORTANT: Inspect the current onboarding implementation first.

The onboarding is 9 steps. Do not assume it is 8.

Do not remove recovery_program or sobriety_why if they exist.

Progress bar:

- Show “Step X of 9” on all steps

- Visual progress bar fills incrementally

- N = 9. Do not hardcode wrong step count.

Navigation:

- Back button on all steps after Step 1

- Back navigates to previous step without losing entered data

- Step 1 has no Back button

- Skip links preserve existing data and set skipped fields to safe empty values

- Skipped array fields → []

- Skipped string fields → “”

Copy review:

- Review each step’s text for clinical, robotic, or cold language

- Rewrite any step that sounds like a form, legal document, or therapy intake

- Target tone: warm, plain-spoken, calm, respectful, not cheesy, not overly clinical

- Do not use motivational clichés

- Do not imply Anchor is a human sponsor, therapist, or crisis monitor

DIRECTION-AWARE TRANSITIONS:

Track navigation direction before swapping step content.

When user taps Next:

- Add class “slide-forward” or data-direction=“forward” to onboarding container

BEFORE swapping content

When user taps Back:

- Add class “slide-back” or data-direction=“back” to onboarding container

BEFORE swapping content

CSS uses that class/attribute to determine slide direction:

- Forward: step slides in from right

- Back: step slides in from left

- Duration: 250ms ease-out

- CSS only. No JavaScript animation libraries.

- Respect prefers-reduced-motion: disable slide, use opacity only

SOBRIETY TRACKER IDEMPOTENCY:

If the user navigates back to Step 3, changes the sobriety date, and advances again:

- Do NOT create duplicate trackers

- Sobriety date is stored in frontend onboarding state only

- Tracker is created/updated ONCE at Step 9 final completion

- On completion: check if an onboarding-created tracker exists. Update it.

If none exists, create it.

Reset onboarding (if already in Settings or easy to add):

- Requires typed confirmation: “reset”

- Sets app_settings.onboarding_version = 0

- Clears stable_profile to default empty values

- Does NOT delete: raw check-ins, trackers, commitments, chat summaries,

email tracking, event_log, user_memory row

-----

ANIMATION POLISH

All animations: CSS only. No JS animation libraries.

Durations: 150ms–300ms.

Respect prefers-reduced-motion: if user prefers reduced motion, disable

slide/rise animations, use simple opacity or no animation.

Tab switching:

- New tab content fades in (opacity 0 to 1, 200ms ease)

- Do NOT slide tabs. Fade only.

IMPORTANT — tab fade implementation:

If tab switching uses display:none / display:block, do not rely on a simple

opacity transition in the same frame. Use one of these:

Option A — CSS keyframes:

@keyframes fadeIn {

from { opacity: 0; }

to   { opacity: 1; }

}

Apply animation to active tab content on each switch.

Option B — requestAnimationFrame:

Set display: block.

Wait one animation frame.

Then add opacity-visible class.

Do not attempt a CSS transition on opacity in the same frame as display changes.

Check-in result card sections:

- Each section: opacity 0→1, translateY(6px)→0, 250ms ease-out

- Stagger: each section starts 70ms after previous, first section at 150ms

- Do NOT animate crisis card in a distracting way

- IMPORTANT: Render ALL result card sections into the DOM first.

Preserve their natural layout space. Animate opacity and transform only.

Do NOT animate height from 0 to auto.

Do NOT insert sections one by one after delays.

This prevents cumulative layout shift.

Set a reasonable min-height on the result card container during initial render.

Chat message bubbles:

- New messages: opacity 0→1, translateY(4px)→0, 150ms ease-out

- Apply to both user and sponsor bubbles

- Do not break auto-scroll

Commitment confirmation text:

- Fade in at 200ms

- Text must read: “Noted. It’ll be waiting on Home when it’s time.”

Do not change this wording.

Loading states:

- All spinners: consistent style — simple rotating circle, 20px, theme accent color

- History and Insights pages: skeleton loader rows during data fetch

- Skeleton pulse animation. Respect prefers-reduced-motion.

-----

AT THE END

When finished, report: onboarding step count confirmed at 9, Back buttons confirmed,

direction-aware transitions implemented, copy reviewed and warmed up, tracker

idempotency confirmed, tab fade avoids display:none transition failure, result card

animations avoid layout shift, reduced motion respected, known issues. Under 300 words.

# =============================================================

V3F3

V3F3: UX AUDIT

Perform a full UX audit on the existing Anchor app and fix identified issues.

Important constraints:

- Do NOT add new database tables or columns

- Do NOT add new product features

- Do NOT rebuild PWA from scratch if it doesn’t exist

- Do NOT rebuild chart systems

- Fix simple issues. List complex issues as known issues.

- V3F1 and V3F2 must already be in place

- Plain HTML, CSS, vanilla JavaScript only

-----

PRE-FLIGHT

Do a quick pass of the full app. List the top 10 issues you find across all screens

BEFORE making any changes. Then ask if you should proceed with fixes, or present

the list for review first. (For Replit: proceed directly with safe CSS/JS fixes.)

-----

NO DATABASE CHANGES. NO NEW TABLES. NO NEW COLUMNS.

-----

AUDIT SCOPE: FIX THESE IF FOUND

Navigation:

- Active tab is clearly visually distinct

- Tab labels readable at small sizes on narrow screens

- All tab tap targets at least 44px height

- No dead zones on tab bar

- Chat remains the third tab

- Bottom nav does not overlap content on short screens

Check-in form:

- All sliders work correctly on iOS Safari (thumb drag specifically)

- Pill toggle buttons have minimum 44px tap target height

- Trigger tag pills wrap cleanly at all widths without overflow

- Hours slept slider shows correct color gradient

- Form scrolls correctly without content hidden behind sticky submit button

- Sober today = No triggers correct warning state on relevant buttons

- Persistent warning state survives tab navigation before submit:

Do not rely only on original click event for warning styling.

Every time Check-In tab renders, derive warning UI from current form state object.

- V3D mic buttons remain only on notes and grateful fields

- V3D mic buttons do not interfere with form submission

Check-in result card:

- All normal result card sections render correctly

- sponsor_note section is completely hidden when string is empty

- risk_level colored dot displays correct color

- “Check in again” resets entire form and clears result card

- At high risk: Reach out section appears at TOP

- At moderate risk: Reach out section appears below commitment section

- Commitment section appears with suggested_commitments pills

- Duplicate commitment saves remain blocked

- Tell on myself opens editable SMS draft when contact exists, never sends

- Listen button appears only below reminder/Remember section

- TTS does not appear on crisis card

- Crisis card behavior remains unchanged

History:

- Entries in correct reverse chronological order

- Tapping entry opens detail view

- Back button on detail view works

- Empty history state is clear and friendly

Insights:

- All charts render on narrow mobile screens without horizontal scroll

- Calendar heatmap month navigation works

- Empty states show “Not enough data yet”

- Commitment completion rate stat displays correctly

- Streak stats correct

- No chart crashes on empty or partial data

Chat:

- Typing indicator appears while waiting

- Messages auto-scroll to bottom

- Crisis state replaces UI correctly

- Return to chat link works

- Human handoff banner at moderate and high risk

- Session summary saves on confirmed New Conversation

- Static opening message appears if memory is empty

- V3D chat mic disabled while chat is sending/waiting

- Speaker icon only on sponsor messages

- TTS does not auto-play

- Only one audio stream at a time

Sobriety trackers:

- Live counter updates every 60 seconds

- Reset flow saves correctly

- Archive toggle works

- Reset flow uses neutral language only

- Empty tracker state is clear

Home dashboard:

- Sobriety counters display correctly

- Date-shift banner only on first open of new day

- Commitment follow-up banner appears correctly when due

- Banners stack cleanly, no overlap

Memory screen in Settings:

- All three memory layers load and display correctly

- Edit, pin, delete work if implemented

- Reset all memory requires confirmation, clears correctly

- Memory pause still works

- No raw phone numbers in AI prompts (confirm)

Email settings in Settings:

- Email, reminder time, timezone save to stable_profile

- reminder_enabled and weekly_summary_enabled save to stable_profile (NOT app_settings)

- Test email works when Resend env vars configured

- Test email shows clear error when env vars missing

- No Resend API key exposed to frontend

Voice input:

- Mic appears only on three V3D fields

- One active recording at a time

- MediaStream tracks stop after recording

- 60-second recording limit works

- Voice input appends, does not replace

- Chat voice does not auto-send

- Voice errors friendly, do not erase text

PWA:

- If service worker exists: bump cache version string to “anchor-v3f-cache”

Ensure install/activate events purge old caches

Ensure updated CSS/JS/HTML are fetched after V3F changes

- If no service worker exists: do NOT create one. List as known issue.

- Offline state shows clear message (if service worker exists)

- App does not crash when offline

General:

- No JavaScript console errors on any screen

- All error messages are user-friendly

- No stack traces shown to user

- Version label in Settings: “Anchor v3.6”

- App handles: zero check-ins, zero trackers, zero memory, zero commitments,

no email configured, no saved sober contacts, no meeting links

- No hardcoded “maxwell” user ID

- getCurrentUserId() pattern intact

-----

AT THE END

When finished, report: all audit items checked, items fixed, items not fixed

(listed as known issues), whether service worker was found and bumped,

version label added, any console errors found and fixed, any remaining known

issues that cannot be fixed without major rebuild. State clearly: V3 is complete.

Keep under 300 words.

Playwright smoke tests v3

V3 Smoke Tests

Anchor V3 Smoke Test Inventory
 Captured from Replit Agent test-results screen
 Final tally: 64 passed, 1 failed, 1 skipped out of 66 tests

Summary

These smoke tests covered the core Anchor V3 application flows, including app loading, navigation, chat, memory/session behavior, commitments, crisis routing, voice transcription, email reminders, scheduler safety, source-of-truth preferences, TTS, and privacy invariants.

The only visible failed test was:

Test 26: chat voice transcription populates input but does not auto-send

This failed because the implemented product behavior appears to auto-submit chat voice transcription, while the test expected transcription to populate the input without sending. This is a product-decision mismatch, not necessarily a functional failure.

Test Inventory

Test

Name

Status

1

app loads and shows all six nav tabs

Passed

2

chat opens with static opener, input and send button

Passed

3

chat sends message and shows mocked assistant reply

Passed

4

chat session persists across page refresh

Passed

5

new conversation clears chat only after confirmation

Passed

6

theme selection applies and persists after refresh

Passed

7

trackers page loads and delete confirmation works

Passed

8

check-in page opens without crash

Passed

9

history and insights pages load without white screen

Passed

10

live /api/chat returns a real response

Skipped / live AI dependent

11

commitment section appears on normal check-in result card

Passed

12

commitment section does NOT appear on crisis result card

Passed

13

tapping a commitment pill saves and shows confirmation, no second save possible

Passed

14

home follow-up banner appears when commitment is due

Passed

15

banner X dismiss is session-only; banner reappears after reload

Passed

16

commitment timing setting saves commitment_followup_hours to stable_profile

Passed

17

commitments this week section is visible on insights page

Passed

18

reach out section appears before commitment for high risk, after for moderate

Passed

19

SMS link uses sms: URI with correct body text

Passed

20

crisis card shows no commitment section, reach-out section, or tell-on-myself

Passed

Chat, Crisis, Handoff, and Memory Tests

Test

Name

Status

10B

no OpenAI API call is made when Chat tab opens; static opener is local

Passed

10C

crisis response renders full-screen crisis card, not a chat bubble

Passed

10D

handoff banner appears below messages at moderate risk

Passed

10E

handoff banner appears below messages at high risk

Passed

10F

no handoff banner when risk is low

Passed

10G

navigating away from Chat does not trigger session-summary POST

Passed

10H

session summary POST sent on confirmed New Conversation with 2+ user and 2+ assistant turns

Passed

10I

session summary NOT sent on New Conversation with only 1 turn

Passed

10J

phone numbers in stable_profile contacts are not present in chat API request body

Passed

10K

recent_summary and event_log injected on first message; absent on second

Passed

Voice Transcription Tests

Test

Name

Status

21

mic button visible on check-in notes field with 44px tap target

Passed

22

mic button visible on check-in grateful field with 44px tap target

Passed

23

mic button visible on chat input row

Passed

24

mic buttons exist only on notes, grateful, and chat input

Passed

25

transcription appends to existing notes text

Passed

26

chat voice transcription populates input but does not auto-send

Failed

27

starting a second recording stops the first

Passed

28

recording shows MM:SS timer, confirming auto-stop mechanism

Passed

29

getUserMedia rejection shows inline error and leaves form usable

Passed

30

no audio storage route exists; GET /api/transcribe is 404/405/etc.

Passed

31

when MediaRecorder is undefined, mic buttons are hidden and form still works

Passed

32

transcription failure shows inline error and preserves notes content

Passed

Email and Reminder Tests

Test

Name

Status

33

Email and Reminders section appears in Settings

Passed

34

GET /api/email/settings returns required fields without exposing API keys

Passed

35

Settings saves email, reminder_time, timezone, and send-trips / send preferences

Passed

36

email validation rejects invalid email address

Passed / reconstructed from visible partial row

37

reminder_enabled and weekly_summary_enabled are in stable_profile, not app_settings

Passed

38

Send test email button triggers POST /api/email/test and shows success toast

Passed

39

Send test email shows error when Resend is not configured

Passed

40

sending test email does not update date fields

Passed

41

emailScheduler guards all three send functions with EMAIL_OUTREACH_ENABLED check

Passed

42

GET /api/email/settings contains preference fields, excludes tracking fields

Passed

43

no Resend API key appears in any API response

Passed

44

commitment_followup_hours is in stable_profile as regression guard

Passed

Text-to-Speech Tests

Test

Name

Status

45

/api/speak returns audio/mpeg for valid check-in context

Passed

46

/api/speak returns 400 for empty text

Passed

47

/api/speak returns 400 for invalid context

Passed

48

/api/speak rejects missing text field with 400

Passed

49

Listen button appears on result card reminder section

Passed

50

Listen button does NOT appear on crisis result card

Passed / reconstructed from visible partial row

51

Speaker icon appears on assistant chat messages, not on user messages

Passed

52

Speaker icon does NOT appear on the chat crisis card

Passed

53

TTS does not autoplay when result card renders

Passed

54

TTS does not autoplay when assistant chat reply appears

Passed

55

Only one concurrent /api/speak request at a time

Passed

56

Raw check-in notes are not sent to /api/speak; only reminder text is sent

Passed

Final Tally

Result

Count

Passed

64

Failed

1

Skipped

1

Total

66

Notes for Case Study

The V3 smoke-test suite demonstrates that Anchor had moved beyond a prototype into a working, testable recovery-support application. The tests covered not only happy-path UI behavior, but also privacy, safety, crisis routing, memory injection rules, human handoff behavior, TTS constraints, voice-transcription fallbacks, email safety flags, and source-of-truth persistence.

The most important engineering signal is that the tests were not limited to “does the page load?” They included recovery-specific invariants:

Crisis cards suppress normal product features.

Phone numbers are not sent into chat API request bodies.

Chat static opener does not trigger OpenAI.

Moderate and high risk states expose human handoff.

Low risk does not over-escalate.

Raw check-in notes are not sent to TTS.

API keys are not exposed in settings responses.

Email scheduler sends are guarded by EMAIL_OUTREACH_ENABLED.

TTS never autoplays.

Only one audio stream/request is allowed at a time.

Voice and recording failures leave the app usable.

The single failed test, Test 26, appears to represent a product-behavior disagreement rather than a catastrophic bug: the test expected chat voice transcription to populate the input without auto-sending, while the app behavior likely auto-sent the transcribed chat message. This should be resolved by choosing one product rule and aligning both implementation and tests around it.

Post launch prompts

V3F3.5

V3F3.5: RESULT CARD TTS + POST-CHECK-IN CHAT PATH

Make a small surgical UX revision to the existing Anchor V3 app.

Add:

A user-initiated Listen to full summary button on the normal check-in result card.

A Chat with my coach action after a normal check-in result.

A clear Chat action on Home if today’s check-in is already complete and Home currently lacks one.

A quick bottom-nav CSS audit only. Do not rebuild nav.

This is a V3F2 polish pass, not a V4 architecture change.

STACK CONTEXT

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has:

Check-in flow

Normal result card

Crisis result card

Chat tab

/api/speak

Remember-section TTS

Sponsor chat message TTS

Global audio manager

Bottom navigation

Existing V3 smoke test suite

Extend existing patterns. Do not rebuild from scratch.

STRICT CREDIT-SAVING RULES

Make the smallest safe change.

Do not refactor unrelated code.

Do not redesign the result card.

Do not redesign Home.

Do not redesign navigation.

Do not create a new TTS system.

Do not duplicate /api/speak.

Do not add packages.

Do not add database tables.

Do not add database columns.

Do not touch email, scheduler, reminders, or Resend.

Do not change voice transcription behavior.

Do not fix unrelated failing tests unless they are directly affected by this prompt.

Preserve all V3A through V3F behavior.

PRE-FLIGHT

Before editing, inspect and report briefly:

Result card component file

Existing TTS helper/audio manager file

Existing /api/speak frontend caller pattern

Home quick-action/check-in status component

Bottom nav CSS file and whether any obvious issue exists

Then proceed.

Keep the pre-flight report short.

V3 INVARIANTS

Preserve:

getCurrentUserId() everywhere on backend user-specific operations

No hardcoded user IDs

Phone numbers never enter AI prompts

Phone numbers never enter TTS payloads

Raw check-in notes never enter TTS

Raw grateful text never enters TTS

Raw voice transcripts never enter TTS

Hidden memory never enters TTS

Full chat history never enters TTS

Crisis cards suppress normal result actions

TTS is always user-initiated

Only one audio stream/request at a time globally

Starting new audio stops current audio

Audio stops on route/tab/view change

No audio files are written to disk

Existing /api/speak validation remains intact

Existing global audio manager remains the single playback source of truth

PART 1: LISTEN TO FULL SUMMARY

Add a second TTS button on the normal check-in result card:

Listen to full summary

The existing Remember-section Listen button must remain unchanged.

Placement:

Put it below the main visible sponsor/coach/report text.

Put it above or near the existing post-result actions.

Keep it visually secondary.

Minimum tap target: 44px height.

Match the existing dark theme.

Behavior:

User taps button.

Stop any current audio first.

Use the existing iOS-safe audio pattern already used by current TTS.

Instantiate Audio synchronously inside the tap handler before async fetch.

POST to existing /api/speak.

Use context "checkin".

While playing, button label becomes Stop summary.

Tapping again stops audio.

On end, error, navigation, or stop, reset to Listen to full summary.

On failure, show small inline error: “Audio unavailable right now.”

Never autoplay.

Text source rule:

The full-summary TTS may include only text already visibly rendered on the normal result card.

Allowed:

Visible state summary

Visible next move / recommendation

Visible Remember text

Visible sponsor/coach reflection/report

Visible non-crisis commitment prompt if already part of the visible normal result

Forbidden:

Raw check-in notes

Raw grateful text

Raw transcript

Hidden memory context

Full chat history

Phone numbers

Crisis resources

Crisis card text

Internal risk labels

Debug metadata

Invisible prompt context

Create a small frontend helper only if useful:

buildVisibleCheckinSummarySpeechText(result): string

This helper must assemble only visible result-card text.

Do not send raw form fields or backend prompt context to TTS.

PART 2: /api/speak LIMIT

Use existing /api/speak.

Request shape:

{

"text": "visible generated result text only",

"context": "checkin"

}

If current check-in TTS is limited to 500 characters and the summary is too short, increase only the checkin context limit to 1500 characters max.

If changed:

Keep truncation.

Preserve sentence-boundary truncation.

Preserve word-boundary fallback.

Do not exceed 1500 characters.

Do not change the chat limit unless absolutely necessary.

If current behavior already supports this cleanly, do not change /api/speak.

PART 3: CRISIS SAFETY

Do not show Listen to full summary on crisis result cards.

Do not add TTS to crisis cards.

Do not change crisis routing, crisis card copy, crisis resources, handoff behavior, or risk classification.

PART 4: CHAT WITH MY COACH

Add a post-result action on the normal check-in result card:

Chat with my coach

Behavior:

Navigate to Chat tab.

Do not auto-send a message.

Do not call OpenAI just from navigating.

Do not send the full check-in result into Chat.

Do not send raw notes.

Do not send hidden memory.

If easy and low-risk, prefill the chat input locally with:

I just completed a check-in and want to talk through it.

If prefill requires meaningful refactoring, skip prefill and only navigate to Chat.

The static Chat opener must remain local and must not call OpenAI.

PART 5: HOME QUICK ACTION

Inspect Home.

Goal:

Home should always provide an obvious path to:

Check In / Check in again

Chat

If Home already has both, do nothing.

If Home hides Chat after today’s check-in is complete, add a compact action:

Chat with my coach

Do not redesign Home.

Do not add SOS unless it already exists.

Do not add new dashboard sections.

PART 6: BOTTOM NAV AUDIT

Inspect bottom nav CSS for obvious causes of floating during scroll:

position: sticky vs position: fixed

Parent scroll container conflicts

100vh / 100dvh issues

iOS safe-area inset

z-index conflicts

Duplicate nav rendering

Missing bottom padding on main content

Fix only if there is an obvious minimal CSS issue.

Preferred behavior:

Bottom nav remains pinned to bottom viewport.

No duplicate nav.

Main content has enough bottom padding.

Safe-area inset is respected.

If no obvious issue is found, do not change nav. Report:

No reproducible bottom-nav bug found; no nav changes made.

TESTING INSTRUCTIONS

Do not create a large new test suite.

Add or update only the smallest number of targeted regression tests needed.

Recommended targeted tests:

Normal result card shows Listen to full summary.

Crisis result card does not show Listen to full summary.

Full-summary TTS does not send raw notes or raw grateful text to /api/speak.

Chat with my coach navigates to Chat without auto-calling OpenAI.

Home exposes Chat after today’s check-in is complete, only if this behavior was missing.

Reuse existing TTS and navigation test patterns.

Do not add more than 5 tests unless absolutely necessary.

Do not spend time fixing unrelated existing Test 26 unless this work directly touches that behavior.

Run only the relevant tests first:

Existing TTS tests 45 through 56

Existing chat static-opener test 10B

Existing crisis suppression tests 20, 50, and 52 if available

Any new targeted V3F2 tests

Only run the full smoke suite if the targeted tests reveal a broad regression.

MANUAL QA

Manually verify:

Normal check-in result still shows existing Remember Listen.

Normal result shows Listen to full summary.

Tapping it plays only after tap.

Button changes to Stop summary while playing.

Stop works.

Crisis result has no full-summary TTS.

Chat with my coach opens Chat.

Chat does not auto-send or auto-call OpenAI on navigation.

Home has a clear Chat action after check-in completion if it did not already.

Bottom nav does not obviously float or duplicate.

AT THE END

Report under 300 words:

Files changed

Whether /api/speak changed

Whether check-in TTS limit changed

Existing Remember Listen preserved

Listen to full summary implemented

Raw notes/grateful text not sent to TTS confirmed

Crisis cards exclude full-summary TTS confirmed

Chat with my coach implemented

Chat navigation does not auto-call OpenAI confirmed

Home quick action result

Bottom nav audit result

Targeted tests added/updated

Targeted tests run and results

Known issues

Exact next recommended prompt

Do not include a long implementation explanation.

V3F4

V3F4: RESULT SUMMARY PLACEMENT + HISTORY TTS + CONTEXTUAL COACH HANDOFF + NAV FIX

Make a focused polish revision to the existing Anchor V3 app.

This is not a V4 rebuild. Make the smallest safe changes.

Goals:

Move the normal-result Listen to full summary action higher on the Check-in Complete screen.

Add Listen to full summary to History detail pages.

Improve Chat with my coach so Chat receives safe visible check-in context and the coach can respond specifically to the check-in.

Fix the persistent mobile bottom-nav floating/overlap issue.

STACK CONTEXT

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has:

Check-in flow

Normal result card

Moderate/high-risk normal result cards with reach-out behavior

Crisis result card

History list and History detail pages

Chat tab

/api/chat

/api/speak

Existing Remember-section TTS

Existing full-summary TTS on result card from V3F2/V3F3

Existing sponsor chat message TTS

Global audio manager

Bottom navigation

Existing V3 smoke test suite

Existing V3F2/V3F3 targeted tests

Extend existing patterns. Do not rebuild from scratch.

STRICT RULES

Do NOT add database tables.

Do NOT add database columns.

Do NOT add packages.

Do NOT redesign the app.

Do NOT create a second TTS system.

Do NOT duplicate /api/speak.

Do NOT create a second chat system.

Do NOT change email, scheduler, reminders, or Resend.

Do NOT change voice transcription behavior.

Do NOT touch unrelated failing tests unless directly affected.

Preserve all V3A through V3F3 behavior.

PRE-FLIGHT

Before editing, inspect and briefly report:

Current Check-in Complete result-card layout and where FullSummaryListenButton is rendered.

History detail page component and whether it has access to the same visible generated fields.

Existing buildVisibleCheckinSummarySpeechText helper or equivalent.

Existing Chat prefill/sessionStorage behavior from V3F2/V3F3.

Bottom nav CSS, app shell layout, html/body/#root height rules, and scroll container structure.

Then proceed.

Keep pre-flight short.

V3 SAFETY INVARIANTS

Preserve:

getCurrentUserId() everywhere on backend user-specific operations.

No hardcoded user IDs.

Phone numbers never enter AI prompts.

Phone numbers never enter TTS payloads.

Raw check-in notes never enter TTS.

Raw grateful text never enters TTS.

Raw voice transcripts never enter TTS.

Hidden memory never enters TTS.

Full chat history never enters TTS.

TTS is always user-initiated.

Only one audio stream/request at a time globally.

Audio stops on route/tab/view change.

No audio files are written to disk.

Existing /api/speak validation remains intact.

Existing global audio manager remains the single playback source of truth.

Crisis cards suppress normal result actions and TTS.

PART 1: MOVE “LISTEN TO FULL SUMMARY” HIGHER ON RESULT PAGE

On the Check-in Complete page, move the Listen to full summary button from the bottom of the result card/actions area to near the top of the page.

Preferred placement:

Directly under:

Check-in Complete

Here’s your reflection.

Above the main result card content.

The button should feel like a page-level action for the whole reflection.

Copy:

Listen to full summary

Keep existing behavior:

User-initiated only.

Uses existing /api/speak.

Uses context "checkin".

Uses the visible generated result text only.

Stops existing audio before starting.

Button changes to Stop summary while playing.

Resets after stop/end/error.

No autoplay.

Do not duplicate the button at both top and bottom. Move it.

PART 2: ADD FULL-SUMMARY TTS TO HISTORY DETAIL PAGE

On each History detail page, add a Listen to full summary button.

Preferred placement:

Under the date/time area near the top of the History detail page.

Before the historical result content card.

Behavior:

Reuse the same FullSummaryListenButton component if possible.

Reuse the same visible-summary text builder if possible.

Use only visible generated historical check-in fields.

Use /api/speak with context "checkin".

User-initiated only.

No autoplay.

Same Stop summary behavior.

Same inline error behavior.

Allowed speech content:

Visible historical state summary / where-you-were text.

Visible factor / something-to-watch text.

Visible next move / recommendation.

Visible Remember text if rendered on History detail.

Visible sponsor/coach reflection if rendered on History detail.

Visible non-crisis commitment prompt if rendered on History detail.

Forbidden speech content:

Raw notes.

Raw grateful text.

Raw transcript.

Hidden memory context.

Phone numbers.

Crisis resource text.

Internal risk labels.

Debug metadata.

Invisible prompt context.

Crisis rule:

Do not show full-summary TTS on true crisis history details if crisis cards are stored/rendered in History.

It is okay to show full-summary TTS on low/moderate/high non-crisis check-in history entries.

PART 3: CONTEXTUAL “CHAT WITH MY COACH” HANDOFF

Improve the Chat with my coach action.

Current V3F2/V3F3 behavior pre-fills:

I just completed a check-in and want to talk through it.

Keep the user-visible prefilled message, but also pass safe visible check-in context to Chat so the coach can respond specifically.

Use sessionStorage or existing navigation state.

Store two local-only values when tapping Chat with my coach:

chatPrefill

I just completed a check-in and want to talk through it.

checkinContextForCoach

A safe visible summary assembled from the same visible generated result fields used for full-summary TTS.

Important:

checkinContextForCoach must contain only visible generated result text.

It must not contain raw notes.

It must not contain raw grateful text.

It must not contain raw transcript.

It must not contain hidden memory.

It must not contain phone numbers.

It must not contain crisis resources.

It must not contain debug metadata.

Chat behavior:

When Chat opens with checkinContextForCoach present:

The input may be prefilled with chatPrefill as it does now.

Do not auto-send the user message unless current product behavior explicitly requires it.

Do not call OpenAI merely from opening Chat.

When the user sends the prefilled message, include checkinContextForCoach in the /api/chat request as a bounded, explicit context field if the backend supports adding metadata safely.

If the backend does not support a separate metadata field, add a minimal backend-supported context pathway that does not show this context as visible user text.

The coach reply should be instructed to use that check-in context specifically.

Desired response style:

Start with a specific reflection from the check-in.

Mention 1–2 concrete details from the visible result.

Ask one grounded follow-up question.

Keep it brief.

Do not hallucinate details not in the check-in context.

Example coach behavior:

Here’s what I notice from your check-in: your mood is strong, but isolation and lust are showing up as risk factors. The key pattern may be that you’re stable overall, but disconnected. What feels most important to address first: the isolation, the lust trigger, or the financial stress?

Do not send the check-in context to OpenAI on Chat tab open.

Only include it when the user actually sends the chat message.

After the first send using this context, clear checkinContextForCoach so it does not attach forever.

If there is already a chat request context pattern, reuse it.

Do not send full chat history.

PART 4: MOBILE BOTTOM NAV FIX

The bottom nav still appears to float/overlap incorrectly on iOS Safari/mobile preview.

This is now a real observed issue, not just an audit.

Fix minimally.

Inspect:

App shell layout.

html, body, #root height/min-height.

Main scroll container.

Bottom nav positioning.

Whether the nav is inside a scrolling container.

Whether content scrolls behind the fixed nav.

iOS Safari dynamic viewport behavior.

100vh vs 100dvh / 100svh.

Safe-area inset usage.

Bottom padding on main content.

Preferred implementation:

Bottom nav should be fixed to the visual bottom of the app viewport.

Bottom nav should not appear halfway up the page while scrolling.

Bottom nav should not duplicate.

Main content should have enough bottom padding so content is not hidden behind nav.

Use safe-area-aware padding:

padding-bottom: calc(nav height + env(safe-area-inset-bottom));

where appropriate.

Prefer 100dvh or 100svh for app shell if current 100vh causes iOS Safari issues.

Avoid putting position: fixed nav inside a transformed or scrolling parent.

Avoid parent transform, filter, or perspective that creates a containing block for fixed children.

Keep changes minimal and localized.

Manual target:

On iPhone Safari preview, while scrolling Home, Check In, Chat, and History, the nav remains visually pinned to the bottom and does not float mid-screen.

TESTING INSTRUCTIONS

Do not create a large test suite.

Add or update only targeted tests.

Recommended tests:

Check-in Complete page shows Listen to full summary near the top, not duplicated at bottom.

History detail page shows Listen to full summary for normal non-crisis entries.

History full-summary TTS does not send raw notes or raw grateful text.

Chat with my coach stores safe visible check-in context for the next sent chat message.

Chat does not call OpenAI merely on tab open.

After the first contextual chat send, the stored check-in context is cleared.

Crisis result/history does not show full-summary TTS.

Bottom nav renders once.

Do not add more than 8 tests unless absolutely necessary.

Run relevant existing tests:

Existing TTS tests 45 through 56.

Existing V3F2/V3F3 tests 71 through 75.

Existing chat static-opener test 10B.

Existing crisis suppression tests 20, 50, and 52 if available.

New V3F4 tests.

Only run the full smoke suite if targeted tests indicate a broad regression.

MANUAL QA

Manually verify on mobile Safari/preview:

Complete a normal check-in.

Confirm Listen to full summary appears directly under Check-in Complete / Here’s your reflection.

Confirm it no longer appears duplicated at the bottom.

Tap it and confirm coherent audio.

Stop and restart it.

Open History detail for a normal check-in.

Confirm Listen to full summary appears near the top.

Confirm History audio works.

Submit a high-risk non-crisis check-in.

Confirm full-summary TTS appears if it is not a true crisis card.

Submit or mock a true crisis result.

Confirm no full-summary TTS appears on true crisis card.

Tap Chat with my coach.

Confirm Chat opens with the prefilled message.

Confirm Chat does not auto-send on open.

Send the message.

Confirm the coach reply references specific visible check-in details.

Confirm follow-up chat messages do not keep reusing stale check-in context.

Scroll Home, Check In, Chat, History, and History detail.

Confirm bottom nav remains pinned to the bottom.

AT THE END

Report under 300 words:

Files changed.

Whether /api/speak changed.

Whether /api/chat changed.

Whether TTS helper was reused.

Result-page TTS placement confirmed.

History detail TTS implemented.

Raw notes/grateful text not sent to TTS confirmed.

Crisis cards still suppress TTS confirmed.

Chat with my coach contextual handoff implemented.

Chat does not call OpenAI on open confirmed.

Context clears after first contextual send confirmed.

Bottom nav fix implemented and what changed.

Targeted tests added/updated.

Targeted tests run and results.

Known issues.

Exact next recommended prompt.

Keep report concise.

More cleanup

Here they are:

REPLIT PROMPT 2 — V3F2-post / V3F4 Review & Cleanup

STACK CONTEXT

React/TypeScript (Vite) + Tailwind CSS frontend. Node.js/Express backend. PostgreSQL on Replit. These additions were run by a separate AI agent without author review.

PRE-FLIGHT (do not skip)

•	Read src/lib/tts-helpers.tsx in full

•	Read src/pages/checkin.tsx — focus on FullSummaryListenButton placement and checkinContextForCoach sessionStorage write

•	Read src/pages/history-detail.tsx (or equivalent) — confirm TTS is present

•	Read src/pages/chat.tsx — confirm checkinContextForCoach read, one-shot clear, no auto-submit on prefill

•	Read artifacts/api-server/src/routes/chat.ts — confirm checkin_context accepted, capped at 800 chars, injected as system-level instruction only

REVIEW CHECKLIST — verify each is correctly implemented:

1.	FullSummaryListenButton renders below the header, above the result card — not inside any section

2.	TTS full summary excludes raw notes and grateful text

3.	TTS suppressed on crisis entries (no listen button rendered)

4.	“Chat with my coach” button navigates to /chat and writes checkinContextForCoach to sessionStorage — does NOT auto-submit

5.	chat.tsx reads checkinContextForCoach on first send only, passes as checkin_context to /api/chat, clears immediately after

6.	/api/chat accepts checkin_context as optional field, caps at 800 chars, injects as bounded system instruction — never stored, never in event_log

7.	History detail TTS present and scoped correctly

8.	Bottom nav renders exactly once — no duplicate nav

9.	src/components/layout.tsx uses h-[100dvh] + overflow-y-auto + inline shrink-0 nav pattern

IF anything is wrong or misaligned: fix it in place. Document what was broken and what you changed.

IF everything is correct: state that explicitly. No unnecessary changes.

SCOPE — do not touch:

•	Check-in voice behavior

•	Crisis routing logic

•	Memory system

•	Email scheduler

•	Any test files

AT THE END

Report: what was correct, what was fixed, what files changed. Under 300 words.

TARGETED TESTS FOR PROMPT 2

Run these tests after the prompt completes:

•	Test 72 — crisis card suppresses TTS

•	Test 73 — raw notes excluded from TTS

•	Test 74 — “Chat with my coach” navigates, prefills, does NOT auto-submit

•	Test 75 — Home quick action chat button works

•	Test 76 — full summary TTS placement (below header, above card)

•	Test 77 — history detail TTS present

•	Test 78 — raw grateful excluded from TTS

•	Test 79 — checkin_context sent on first send only

•	Test 80 — checkin_context cleared after first send

•	Test 81 — crisis suppresses TTS (second coverage)

•	Test 82 — bottom nav renders exactly once

All 11 should pass. Report any failures with root cause.

REPLIT PROMPT 3 — Chat Mode Detection Upgrade

STACK CONTEXT

React/TypeScript (Vite) + Tailwind CSS frontend. Node.js/Express backend. This is a system prompt update only — no new tables, no new routes, no schema changes.

PRE-FLIGHT (do not skip)

•	Open artifacts/api-server/src/routes/chat.ts

•	Read the full current chat system prompt

•	Confirm crisis routing logic is present and unchanged before editing

•	Confirm human handoff rules are present and unchanged before editing

•	Do not touch any frontend files

THE CHANGE — system prompt update only

Add mode detection to the chat system prompt. The assistant should silently detect which mode the conversation is in and respond accordingly. Modes:

•	Reflect — user is processing emotion, venting, or narrating an experience. Hold space. Ask one good question. Don’t push to action.

•	Plan — user is thinking through a decision or next step. Help them think clearly. Surface tradeoffs. Offer structure if asked.

•	Pattern — user is describing a recurring behavior or dynamic. Name it directly. Connect to known history from memory if relevant.

•	Handoff — user is expressing isolation, asking for support beyond what the coach can give, or showing signs they need a human. Route to named contact from memory. Make it the point, not a footnote.

•	Commitment — user states a concrete action they intend to take. Offer to save it: “Want to save that as a commitment?” Only offer once per action. Do not repeat.

Additional improvements:

•	Reduce repetitive question loops — do not end every response with a question

•	Vary response length to match the moment — short for venting, longer for planning

•	Never invent contact names. Only use names present in memory context.

PRESERVE WITHOUT CHANGE:

•	All crisis detection and routing logic

•	Human handoff rules at moderate and high risk

•	Banned phrases list

•	Memory injection behavior

•	Stoic/DBT voice orientation

•	Phone number exclusion rule

SCOPE — do not touch:

•	Any frontend files

•	Database schema

•	Any other backend routes

•	Test files

AT THE END

Paste the full updated system prompt so it can be reviewed before the next test run. Under 300 words summary of what changed.

TARGETED TESTS FOR PROMPT 3

These are new tests to write and run after the prompt completes. Add them to anchor-smoke.spec.ts:

•	Test 83 — when user message contains a concrete intended action, assistant response includes offer to save as commitment (“Want to save that as a commitment?”)

•	Test 84 — commitment offer does not repeat in the same session after already being offered once

•	Test 85 — crisis detection still fires correctly after system prompt update (existing crisis invariant re-confirmed)

•	Test 86 — human handoff still appears at moderate risk after system prompt update

•	Test 87 — banned phrases do not appear in any chat response after system prompt update

All 5 should pass. Report any failures with root cause.

Ready when you are.​​​​​​​​​​​​​​​​

Big fix B

Here it is:

REPLIT PROMPT — Bug Fix A

STACK CONTEXT

React/TypeScript (Vite) + Tailwind CSS frontend. Node.js/Express backend. PostgreSQL on Replit.

PRE-FLIGHT (do not skip)

•	Open src/pages/checkin.tsx — find all binary Yes/No fields

•	Open the Insights API route — find the commitments this week query

•	Open the Insights API route — find the Recovery Habits query

•	Read all three before touching anything

BUG 1 — “Ate enough today” defaults to Yes

All binary Yes/No fields on the check-in form must default to null (unselected). No field should have a pre-selected value on load. This includes: Sober today, Attended a meeting, Called a fellow, Exercised today, Ate enough today.

Fix the initial state so every binary field starts as null. The UI should show both buttons unselected until the user taps one.

BUG 2 — Commitments this week showing wrong count

The “Commitments this week” query is returning an incorrect number (showing 32). Fix the query to scope correctly to the current calendar week — Monday 00:00:00 through Sunday 23:59:59 in the user’s timezone. Use the timezone stored in stable_profile.

BUG 3 — Recovery Habits not counting correctly

The Recovery Habits section in Insights (Meeting attended, Sober person contacted, Fellow called, Exercised, Ate enough) is showing 0/3 days for fields that were marked Yes during check-ins. Investigate the query and fix the field mapping so it correctly counts days where each field was marked Yes within the last 30 days.

While fixing this, implement the multi check-in algorithm:

•	Binary fields (meeting, contact, fellow, exercise, ate enough, sober): last-value-wins per day — if checked in twice, use the most recent answer

•	Numeric fields (mood, craving, sleep, energy, focus): average across all check-ins for that day

SCOPE — do not touch:

•	Crisis routing

•	Memory system

•	Email scheduler

•	Chat system prompt

•	TTS

•	Any test files (tests come after)

AT THE END

Report exactly what queries changed and what the before/after logic is. Under 200 words.

TARGETED TESTS — run after prompt completes:

Add these to anchor-smoke.spec.ts and run them:

•	Test 88 — all binary fields on check-in form load with no value selected (null state)

•	Test 89 — commitments this week count reflects only commitments created in the current calendar week

•	Test 90 — Recovery Habits counts a day as Yes only when the most recent check-in for that day marked the field Yes

•	Test 91 — numeric fields (mood, craving, sleep) average across multiple check-ins on the same day

All 4 should pass. Report any failures with root cause.

Ready to paste.​​​​​​​​​​​​​​​​

But fix C

Here it is:

REPLIT PROMPT — Bug Fix B

STACK CONTEXT

React/TypeScript (Vite) + Tailwind CSS frontend. Node.js/Express backend. PostgreSQL on Replit. Email via Resend. Scheduler via node-cron.

PRE-FLIGHT (do not skip)

•	Open the Memory screen component — find where Recent Patterns summary is rendered

•	Open the API route that generates or returns the Recent Patterns summary

•	Open artifacts/api-server/src/routes/email.ts (or equivalent scheduler file)

•	Confirm EMAIL_OUTREACH_ENABLED env flag handling before touching anything

BUG 1 — Recent Patterns rendering raw markdown

The Recent Patterns section in Memory is displaying raw markdown characters (###, **bold**) as literal text. Fix one of two ways — pick the simpler one given the current implementation:

Option A: Render the string as markdown using a lightweight renderer (e.g. react-markdown if not already installed, or a simple regex strip if full rendering is overkill).

Option B: Change the AI prompt that generates the summary to return plain text only — no markdown, no headers, no bold. 3-5 sentences max. If this is an AI-generated field, Option B is preferred — simpler and more controllable.

Whichever option is chosen, the output must be readable prose with no raw markdown characters visible to the user.

BUG 2 — Email diagnostic endpoint

Add a new GET endpoint: /api/email-status

It must return a JSON object with:

•	outreach_enabled — boolean, true if EMAIL_OUTREACH_ENABLED === “true”

•	resend_key_present — boolean, true if RESEND_API_KEY is set and non-empty. Do NOT return the key value itself.

•	last_daily_reminder_sent — the value of last_daily_reminder_sent_date from app_settings for the current user

•	last_missed_followup_sent — the value of last_missed_followup_sent_date from app_settings

•	last_weekly_summary_sent — the value of last_weekly_summary_sent_week from app_settings

•	scheduler_running — boolean, true if the cron jobs are active

This endpoint is for diagnostics only. It requires no auth beyond the existing session pattern. It does not trigger any sends.

SCOPE — do not touch:

•	Check-in form

•	Insights queries (fixed in Bug Fix A)

•	Crisis routing

•	Memory system data

•	Chat system prompt

•	TTS

•	Any test files

AT THE END

Report: which Recent Patterns option was chosen and why, what the endpoint returns when hit, and paste a sample /api/email-status response. Under 200 words.

TARGETED TESTS — run after prompt completes:

Add these to anchor-smoke.spec.ts and run them:

•	Test 92 — Recent Patterns section contains no raw markdown characters (###, **, __)

•	Test 93 — /api/email-status returns 200 with all six expected fields present

•	Test 94 — /api/email-status does not expose the RESEND_API_KEY value in any field

All 3 should pass. Report any failures with root cause.

Save it for when you’re ready. Good work today.​​​​​​​​​​​​​​​​

UX bug fix

UX fixes

REPLIT PROMPT — UX Features A

STACK CONTEXT

React/TypeScript (Vite) + Tailwind CSS frontend. Node.js/Express backend. PostgreSQL on Replit. stable_profile (JSONB) is the single source of truth for all user preferences.

PRE-FLIGHT (do not skip)

•	Open the Memory screen component — confirm it currently renders as read-only

•	Open the onboarding component — find the recovery_program selection step

•	Open the Home page component — find the trackers section

•	Open utils/v3helpers.js (or equivalent) — confirm normalizeStableProfile() shape

•	Read all of the above before touching anything

FEATURE 1 — Memory screen inline editing

The Memory screen must allow inline editing of all stable_profile fields without resetting onboarding.

Editable fields:

•	recovery_focus (multi-select chips: Alcohol, Drugs, Sex/Porn, Codependency, Food, Gambling, Other)

•	recovery_program (program picker — see Feature 2)

•	support_style (text input)

•	sobriety_why (textarea)

•	sober_contacts (array — add, edit, remove each contact’s name and phone)

•	meeting_links (array — add, edit, remove each link — see Feature 4)

•	email, reminder_time, timezone

UX pattern: each field row has a tap-to-edit affordance. When tapped, the row expands inline with appropriate input controls and a Save / Cancel pair. Save persists to stable_profile via PATCH to the user_memory endpoint. Cancel reverts. No modals. No new screens.

Sober contacts and meeting links use a list pattern: each item has its own edit and remove control, plus an “Add new” button at the bottom of the list.

FEATURE 2 — Recovery program expansion

Replace the current recovery_program field with a structured shape:

recovery_program: {

primary: string,         // one of the 12 categories below

specific: string[]       // sub-program names if primary is "12-Step" or category-based

}

Primary categories (use these exact strings):

1.	“AA”

2.	“NA”

3.	“12-Step (other)”

4.	“Codependency / Relationships”

5.	“Sex / Love / Porn / Intimacy”

6.	“SMART Recovery”

7.	“Recovery Dharma”

8.	“Refuge Recovery”

9.	“Secular / No Program”

10.	“Gambling / Money / Work”

11.	“Food / Eating”

12.	“Other / Not sure yet”

When primary is one of: “12-Step (other)”, “Codependency / Relationships”, “Sex / Love / Porn / Intimacy”, “Secular / No Program”, “Gambling / Money / Work”, “Food / Eating”, or “Other / Not sure yet” — show a multi-select sub-picker for specific.

Sub-program lists per primary:

•	12-Step (other): Cocaine Anonymous, Crystal Meth Anonymous, Marijuana Anonymous, Heroin Anonymous, Pills Anonymous, Nicotine Anonymous

•	Codependency / Relationships: CoDA, ACA, Al-Anon, Nar-Anon, Families Anonymous

•	Sex / Love / Porn / Intimacy: SLAA, SAA, SPAA, SA, SCA, Porn Addicts Anonymous, COSA

•	Secular / No Program: LifeRing, Women for Sobriety, Secular AA, Moderation Management

•	Gambling / Money / Work: Gamblers Anonymous, Debtors Anonymous, Underearners Anonymous, Spenders Anonymous, Workaholics Anonymous

•	Food / Eating: Overeaters Anonymous, Food Addicts Anonymous, Food Addicts in Recovery Anonymous, Eating Disorders Anonymous, Anorexics and Bulimics Anonymous

•	Other / Not sure yet: SAMHSA, Psychology Today, Find a Helpline

This new shape applies to both onboarding and Memory edit. Migrate any existing string values: if recovery_program is a plain string, wrap it as { primary: <string>, specific: [] } on first read.

FEATURE 3 — “Find a meeting” routing

Create a URL catalog file: src/lib/recoveryResources.ts

Seed it with this map (key = primary or specific program name → official URL):

"AA": "https://aa-intergroup.org/"

"NA": "https://virtual-na.org/meetings/"

"Cocaine Anonymous": "https://ca-online.org/"

"Crystal Meth Anonymous": "https://www.crystalmeth.org/meetings/"

"Marijuana Anonymous": "https://marijuana-anonymous.org/find-a-meeting/"

"Heroin Anonymous": "https://heroinanonymous.org/meetings/"

"Pills Anonymous": "https://www.pillsanonymous.org/find-a-virtual-meeting"

"Nicotine Anonymous": "https://nicotine-anonymous.org/find-a-meeting/"

"CoDA": "https://coda.org/find-a-meeting/online-meetings/"

"ACA": "https://adultchildren.org/meeting-search/"

"Al-Anon": "https://al-anon.org/al-anon-meetings/"

"Nar-Anon": "https://www.nar-anon.org/virtual-meetings"

"Families Anonymous": "https://familiesanonymous.org/meetings/"

"SLAA": "https://slaafws.org/onlinemeetings/"

"SAA": "https://saa-recovery.org/meetings/"

"SPAA": "https://spaa-recovery.org/"

"SA": "https://www.sa.org/"

"SCA": "https://onlinesca.org/"

"Porn Addicts Anonymous": "https://www.pornaddictsanonymous.org/"

"COSA": "https://cosa-recovery.org/meetings/"

"SMART Recovery": "https://smartrecovery.org/meeting"

"Recovery Dharma": "https://recoverydharma.org/meetings/"

"Refuge Recovery": "https://www.refugerecovery.org/"

"LifeRing": "https://lifering.org/meeting-menu/online-meetings/"

"Women for Sobriety": "https://meetings.womenforsobriety.org/meetings/"

"Secular AA": "https://www.aasecular.org/online-meetings"

"Moderation Management": "https://moderation.org/organizer/moderation-management/"

"Gamblers Anonymous": "https://gamblersanonymous.org/find-a-meeting/"

"Debtors Anonymous": "https://debtorsanonymous.org/meeting-search-virtual/"

"Underearners Anonymous": "https://www.underearnersanonymous.org/meetings-underearners-anonymous/"

"Spenders Anonymous": "https://www.spenders.org/meetings"

"Workaholics Anonymous": "https://workaholics-anonymous.org/meetings/"

"Overeaters Anonymous": "https://oa.org/find-a-meeting/"

"Food Addicts Anonymous": "https://faacanhelp.org/meetings/virtual-meetings/"

"Food Addicts in Recovery Anonymous": "https://www.foodaddicts.org/find-a-meeting"

"Eating Disorders Anonymous": "https://eatingdisordersanonymous.org/meeting/"

"Anorexics and Bulimics Anonymous": "https://www.aba12steps.org/meeting-info"

"SAMHSA": "https://findtreatment.gov/"

"Psychology Today": "https://www.psychologytoday.com/us/therapists?category=addiction"

"Find a Helpline": "https://findahelpline.com/"

Behavior of “Find a meeting” button (in Reach Out card and anywhere else it appears):

•	Read recovery_program from stable_profile.

•	If primary matches a top-level key in the catalog AND specific is empty: open that URL in a new tab.

•	If specific has one entry: open that entry’s URL.

•	If specific has multiple entries: open a small inline picker showing each option as a button. Tapping a button opens that URL in a new tab.

•	Fallback if no match found or no program set: open https://aa-intergroup.org/.

Use target="_blank" and rel="noopener noreferrer" on all external links.

FEATURE 4 — Meeting links: simplified add/edit

Replace the current free-text meeting link entry with a structured form. Each meeting link entry has:

•	label (string, e.g., “Daily AA”)

•	day_of_week (enum: Mon, Tue, Wed, Thu, Fri, Sat, Sun, or “Daily”)

•	time (HH:MM, 24-hour)

•	timezone (auto-default to user’s stable_profile.timezone, but editable per link)

•	url (string, must start with https://)

Update the stable_profile shape:

meeting_links: [

{

label: string,

day_of_week: string,

time: string,

timezone: string,

url: string

}

]

Migrate existing entries: if a meeting_link is a plain string or missing fields, populate as best as possible and leave optional fields empty. Do not lose data.

Display in Memory screen: each link shows label, “Day at Time TZ”, and the URL with an Open button. Edit and Remove inline.

FEATURE 5 — Trackers home page scroll fix

The trackers section on the Home page has a scroll bar that cuts off some trackers. Fix the layout so all trackers are visible without an internal scroll bar. The page itself can scroll, but the trackers list must not have its own constrained scroll container.

SCOPE — do not touch:

•	Crisis routing

•	Memory injection logic in chat / check-in AI calls

•	Email scheduler

•	Chat system prompt

•	TTS

•	Recent Patterns rendering (handled in UX-B)

•	Theme system (handled in UX-B)

•	Insights queries

•	Check-in form

AT THE END

Report:

1.	Confirm stable_profile migration logic for both recovery_program and meeting_links is in place and non-destructive.

2.	Confirm recoveryResources.ts is created with all 39 URLs.

3.	Confirm Memory screen now allows inline edit for every listed field.

4.	Confirm “Find a meeting” routes correctly for at least 3 different program selections.

5.	Paste the new stable_profile shape.

Under 250 words.

TARGETED TESTS — run after prompt completes:

Add these to anchor-smoke.spec.ts and run them:

•	Test 95 — Memory screen renders edit affordance on every editable field

•	Test 96 — editing a sober contact name persists to stable_profile

•	Test 97 — adding a new sober contact appends to the array and persists

•	Test 98 — removing a sober contact removes it from the array

•	Test 99 — recovery_program with primary “AA” and empty specific opens aa-intergroup.org/ when “Find a meeting” is tapped

•	Test 100 — recovery_program with primary “Sex / Love / Porn / Intimacy” and specific containing 2+ items shows a picker

•	Test 101 — meeting_links entries with all 5 structured fields persist correctly

•	Test 102 — old-shape recovery_program (plain string) is migrated to new shape on first read without data loss

•	Test 103 — Home page trackers section displays all trackers without an internal scroll bar

•	Test 104 — “Find a meeting” with empty recovery_program falls back to aa-intergroup.org/

All 10 should pass. Report any failures with root cause.

That’s UX-A. Want UX-B (themes + Recent Patterns) now or save it for later?​​​​​​​​​​​​​​​​

REPLIT PROMPT — UX Features B

STACK CONTEXT

React/TypeScript (Vite) + Tailwind CSS frontend. Node.js/Express backend. PostgreSQL on Replit. This prompt is pure frontend except for the Recent Patterns generation prompt change.

PRE-FLIGHT (do not skip)

•	Open the theme system file (likely src/lib/themes.ts or similar) — read all current themes

•	Open the Memory screen component — find where Recent Patterns is rendered

•	Open the API route or service that generates the Recent Patterns summary — find the AI prompt being used

•	Read all of the above before touching anything

FEATURE 1 — Full theme contrast audit

Audit every existing theme for WCAG AA contrast compliance on:

•	Primary text on background

•	Secondary / helper text on background

•	Button text on button background

•	Input text on input background

•	Link text on background

•	Border / divider visibility

Minimum contrast ratios:

•	Normal text: 4.5:1

•	Large text (18pt+ or 14pt+ bold): 3:1

•	UI components and graphical objects: 3:1

Fix any violations by adjusting the offending color tokens. Do not redesign — only adjust values needed to pass contrast. Document each color change in the final report (which token, old value, new value, ratio before, ratio after).

FEATURE 2 — Add new themes

Add two new themes to the existing theme system:

New light theme: “Paper”

•	Warmer than the current default light theme

•	Off-white background (around #FAF7F2)

•	Soft brown/sepia accents

•	High readability, low harshness

•	Must pass WCAG AA contrast

New dark theme: “Midnight”

•	Deeper than the current default dark theme

•	Near-black background (around #0A0E14)

•	Cool blue-grey text

•	Soft indigo/violet accents for primary actions

•	Must pass WCAG AA contrast

Both themes must be selectable from the existing theme picker in Settings. Persist user selection in stable_profile under a new field theme_preference (string).

If theme_preference is missing from stable_profile, default to whatever the current default is. Do not break existing behavior.

FEATURE 3 — Recent Patterns: 3-bullet structured format

Replace the current free-form AI-generated wall of text with a structured 3-bullet format.

Update the AI prompt that generates the Recent Patterns summary. The prompt must instruct the model to return ONLY a JSON object with this exact shape:

{

"top_triggers": string,      // one sentence naming the most frequent trigger(s) this period and what they suggest

"mood_trend": string,        // one sentence describing mood/craving/sleep direction over the period

"pattern_to_notice": string  // one sentence naming one recurring pattern worth the user's attention

}

Constraints in the prompt:

•	Plain prose. No markdown. No bullets. No headers. No bold.

•	Each field is one sentence, 15-25 words.

•	Direct, observational. No coaching, no platitudes, no “you should.”

•	Use the same banned phrases list from the chat system prompt.

•	Never invent contact names. Only use names present in memory context.

Parse the JSON server-side. If parsing fails, fall back to a generic message: “Not enough recent activity to identify patterns yet.”

Render the result in the Memory screen as three labeled rows:

Top triggers

[top_triggers sentence]

Mood trend

[mood_trend sentence]

Pattern to notice

[pattern_to_notice sentence]

Use existing typography. Labels are small uppercase tracking-wide. Body text is regular weight.

If the user has fewer than 3 check-ins in the relevant window, do not generate the summary at all. Show: “Check in a few more times to see your patterns.”

SCOPE — do not touch:

•	Crisis routing

•	Memory injection logic in chat / check-in AI calls

•	Email scheduler

•	Chat system prompt

•	TTS

•	Insights queries

•	Check-in form

•	Memory editing UX (handled in UX-A)

•	Recovery program structure (handled in UX-A)

•	Find a meeting routing (handled in UX-A)

AT THE END

Report:

1.	List every color token changed in the contrast audit with before/after values and contrast ratios.

2.	Confirm “Paper” and “Midnight” themes added and selectable.

3.	Paste the new Recent Patterns AI prompt verbatim.

4.	Paste a sample successful JSON response from the AI for Recent Patterns.

5.	Paste the rendered Memory screen output for that sample.

Under 300 words.

TARGETED TESTS — run after prompt completes:

Add these to anchor-smoke.spec.ts and run them:

•	Test 105 — “Paper” theme appears in the theme picker and applies when selected

•	Test 106 — “Midnight” theme appears in the theme picker and applies when selected

•	Test 107 — theme_preference persists to stable_profile when changed

•	Test 108 — Recent Patterns renders three labeled sections (Top triggers, Mood trend, Pattern to notice)

•	Test 109 — Recent Patterns contains no raw markdown characters (#, **, __)

•	Test 110 — when user has fewer than 3 check-ins, Recent Patterns shows the “check in a few more times” message instead of AI summary

•	Test 111 — Recent Patterns AI prompt failure (malformed JSON) falls back to the generic “not enough activity” message without crashing

All 7 should pass. Report any failures with root cause.

That’s the full UX-B. You now have:

•	Bug Fix A (ready to run)

•	Bug Fix B (saved)

•	UX Features A (saved)

•	UX Features B (saved)

Run them in order. Don’t skip the test runs in between. Each one builds on the last.

Good night.​​​​​​​​​​​​​​​​
