---
title: "V2 prompts"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/V2 prompts.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# V2 prompts

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
V2A

Upgrade the existing recovery check-in app to V2A only.

Important constraints:

- Do NOT attempt the full V2 roadmap yet

- Focus only on persistence, history, structured AI output, quick check-in mode, and mobile UI improvements

- Keep the current dark, calm, mobile-first design language

- Do not add native mobile features, PWA, charts, trackers, calendar heatmaps, or export yet

V2A GOALS

1. Save all check-ins to a database

1. Add a History page showing previous check-ins

1. Change the OpenAI output from freeform text to structured JSON

1. Add a Quick Check-In mode

1. Improve the mobile UI and slider usability

DATABASE

- Use Replit’s built-in PostgreSQL

- Create table: check_ins

- id (serial primary key)

- created_at (timestamp with timezone, default now())

- check_in_type (varchar: ‘full’ or ‘quick’)

- mood (integer 1-10)

- energy (integer 1-10)

- craving (integer 1-10)

- focus (integer 1-10, nullable)

- sober_today (boolean)

- hours_slept (decimal, nullable)

- meeting_today (boolean, nullable)

- contacted_sober_person (boolean, nullable)

- called_fellow (boolean, nullable)

- exercised_today (boolean, nullable)

- ate_enough_today (boolean, nullable)

- trigger_tags (text array, nullable)

- notes (text, nullable)

- grateful (text, nullable)

- ai_state_summary (text)

- ai_risk_level (varchar)

- ai_main_risk_factor (text)

- ai_next_moves (jsonb)

- ai_recovery_support_prompt (text)

- ai_reminder (text)

- user_id (varchar, default ‘maxwell’)

- Save every check-in after successful AI response

EXISTING FULL CHECK-IN FIELDS (keep these)

- mood (1-10 slider)

- energy (1-10 slider)

- craving (1-10 slider)

- focus (1-10 slider)

- sober today (yes/no)

- meeting attended or planned today (yes/no)

- notes (textarea)

- grateful (short text, optional)

ADD THESE NEW FULL CHECK-IN FIELDS

- hours slept (numeric input, 0-24, step 0.5)

- contacted a sober person today (yes/no)

- called a fellow today (yes/no)

- exercised today (yes/no)

- ate enough today (yes/no)

- trigger tags (multi-select pill buttons, pick any that apply):

fatigue, loneliness, comparison, boredom, conflict, resentment, anxiety, lust, financial stress, isolation

QUICK CHECK-IN MODE

- Show two clear options on the home or check-in screen: “Full Check-In” and “Quick Check-In”

- Quick check-in asks only: mood, energy, craving, sober today, notes

- Prefill quick check-in sliders from most recent saved check-in values if available

- All other fields are null for quick check-in entries

- Same AI call and result card as full check-in

OPENAI REQUIREMENTS

- Keep using the existing OpenAI API key from environment variable

- Keep using Chat Completions API with gpt-4o-mini

- Change output to structured JSON only

- Updated system prompt:

“You are a calm, practical recovery check-in coach. Be concise, non-shaming, and action-oriented. Respond ONLY with valid JSON, no markdown, no explanation, using this exact shape:

{

"state_summary": "1-2 sentence read of current state",

"risk_level": "low|moderate|high",

"main_risk_factor": "single most important thing to watch today",

"next_moves": ["action 1", "action 2", "action 3"],

"recovery_support_prompt": "one specific concrete suggestion for connection or support",

"reminder": "one short grounding line"

}”

- Parse and validate JSON before rendering

- If JSON parsing fails, show a safe fallback error message — do not crash

RESULT CARD

Render six clearly separated card sections:

1. “Where you’re at” — state_summary

1. “Something to watch” — main_risk_factor

1. “Attention level” — risk_level as colored dot: green=low, yellow=moderate, red=high. Display text as “low / moderate / elevated” not raw value

1. “Next moves” — next_moves as a simple list

1. “Support” — recovery_support_prompt

1. “Remember” — reminder in italics

HISTORY PAGE

- Add a History tab in the navigation

- Show all past check-ins in reverse chronological order

- Each row shows: date, time, check-in type (full/quick), mood, craving, risk level dot, 1-line state summary

- Tap a row to open full detail view with all input values and full AI output

- Handle empty history with a clean empty state message

- Add a back button on detail view

NAVIGATION

- Three tabs: Home, Check-In, History

- Home shows today’s status: whether a check-in exists today, last risk level, and quick stats

- Keep it simple — no bottom nav overengineering

UI FIXES

- Slider thumb: clearly visible draggable circle, minimum 24px, works correctly on iOS Safari

- Show live numeric value next to each slider label

- Yes/no inputs: pill toggle buttons, not dropdowns or checkboxes

- Trigger tags: tappable pill buttons that toggle on/off

- Sticky submit button at bottom on long forms

- Smooth scroll to result card after submission

- Loading state while waiting for AI response

- Keep dark theme, clean typography, no wellness branding

ERROR HANDLING

- Missing API key: “The app isn’t configured. Add your API key to Replit Secrets.”

- AI failure: “Something went wrong. Try again in a moment.”

- JSON parse failure: “Response couldn’t be read. Try submitting again.”

- Database save failure: show AI result but display small warning “Check-in not saved”

- Never expose stack traces to the browser

At the end:

- Summarize exactly what was implemented

- List any database migrations or setup steps needed

- Identify the exact next step for V2B

Run as persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.

V2B

Upgrade the existing recovery check-in app to V2B only.

Important constraints:

- Do NOT attempt charts, insights, PWA, or export yet

- Build only the sobriety tracker system, home dashboard, first-run onboarding, date-shift banner, and basic edit capability

- Keep the current dark, calm, mobile-first design language

- Extend what exists — do not rebuild from scratch

V2B GOALS

1. Add a full sobriety tracker system

1. Build a real home dashboard

1. Add first-run onboarding to set up trackers

1. Add the date-shift banner on home

1. Add basic edit capability for tracker dates and today’s check-in

DATABASE — ADD THESE TABLES

Table: sobriety_trackers

- id (serial primary key)

- name (varchar, required)

- category (varchar, nullable)

- start_datetime (timestamp with timezone, required)

- is_active (boolean, default true)

- color (varchar, nullable — hex color)

- notes (text, nullable)

- created_at (timestamp with timezone, default now())

- updated_at (timestamp with timezone)

- user_id (varchar, default ‘maxwell’)

Table: tracker_resets

- id (serial primary key)

- tracker_id (integer, foreign key → sobriety_trackers.id)

- reset_datetime (timestamp with timezone)

- prior_start_datetime (timestamp with timezone)

- note (text, nullable)

- created_at (timestamp with timezone, default now())

Table: app_settings

- id (serial primary key)

- user_id (varchar, default ‘maxwell’)

- last_opened_date (date)

- first_open_completed (boolean, default false)

- prompt_for_date_shift (boolean, default true)

SOBRIETY TRACKER FEATURES

- User can create named trackers with start date and start time down to the minute

- Live running counter per tracker showing days and hours (refresh every 60 seconds)

- Tracker detail view shows full counter including minutes and seconds

- Preset category suggestions: Alcohol, Weed, Nicotine, Porn, Masturbation, Gambling, Doomscrolling, Sugar, Custom

- Optional color per tracker for visual distinction

- Edit tracker: name, category, color, notes, start date/time

- Reset tracker: choose new start date and time, optional note (“what happened?”), log saved to tracker_resets — tone is neutral and factual, zero shame language

- Archive tracker: sets is_active = false, hidden by default but viewable via toggle

- Add tracker flow: name → category → start date → start time → color (optional) → notes (optional) → save

FIRST-RUN ONBOARDING

- Check app_settings.first_open_completed on every load

- If false, show a 3-step onboarding screen before anything else:

- Step 1: “This is your daily recovery check-in. Private, calm, and yours.” → Next

- Step 2: Set up your sobriety trackers. Show the add-tracker flow inline. Allow adding one or more trackers. Allow skipping.

- Step 3: “You’re set. Check in daily. Your data stays here.” → Go to dashboard

- After completion set first_open_completed = true

- Never show onboarding again after that

- Tone: calm, minimal, no marketing language

HOME DASHBOARD

Replace current home screen with a real dashboard. Layout top to bottom:

1. Greeting with current date

1. Sobriety counters row — compact cards showing tracker name and days count

1. Date-shift banner if applicable (see below)

1. “Start today’s check-in” with two options: Full or Quick

1. If already checked in today: show latest result summary (risk level dot + state summary) and a “Check in again” option

1. Quick stats row: today’s mood, today’s craving, sober today, hours slept

DATE-SHIFT BANNER

- On home load, check if today is a new day since app_settings.last_opened_date

- If new day, show a non-blocking dismissable banner: “Any sobriety dates shifted since your last visit?”

- Two options: “Update a tracker” or “All good”

- If “Update a tracker”: show list of active trackers, select one, go to reset flow

- If “All good” or dismissed: hide banner for the rest of today

- Update last_opened_date on every home screen load

- Must NOT be a blocking modal — banner only, always dismissable

BASIC EDIT CAPABILITY

- On the History detail view for today’s check-in only: show an Edit button

- Allow editing all input fields for today’s entry

- Do not re-run AI on edit — keep original AI output

- On any tracker: allow editing start date/time directly from the tracker detail view

- This is enough for V2B — full backfill editing comes in V2C

NAVIGATION

- Update to 4 tabs: Home, Check-In, History, Trackers

- Home is the default landing screen

- Trackers tab shows the full tracker list and management

UI NOTES

- Tracker cards: clean and motivating, not clinical

- Counter display format: “47 days 6 hours” — clean and readable

- Color accents on tracker cards should be subtle

- Reset flow: neutral language only, no red warnings, no shame

- Keep all existing dark theme and visual style

At the end:

- Summarize exactly what was implemented

- List any database migrations or setup steps needed

- Identify the exact next step for V2C

Run as persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.

V2C

Upgrade the existing recovery check-in app to V2C only.

Important constraints:

- Do NOT attempt PWA, full polish passes, or onboarding refinement yet

- Build only charts, calendar heatmap, insights page, export, and limited check-in edit/backfill

- Keep the current dark, calm, mobile-first design language

- Extend what exists — do not rebuild from scratch

V2C GOALS

1. Add an Insights page with trend charts and calendar heatmap

1. Add streak stats and recovery habit frequency

1. Add data export

1. Add limited check-in edit and backfill capability

INSIGHTS TAB

- Add a fifth tab to bottom navigation: Home, Check-In, History, Trackers, Insights

TREND CHARTS

Use Chart.js. All charts cover last 30 days by default with a toggle for 7 / 30 / 90 days.

Show these line charts:

- Mood over time

- Energy over time

- Craving over time

- Focus over time

- Hours slept over time

Each chart:

- Date on x-axis, value on y-axis

- Dark theme compatible colors

- Handles missing days as gaps in the line, not zeros

- Renders cleanly on mobile width — no horizontal scrolling

RECOVERY HABIT CHARTS

Show simple percentage bars for the last 30 days:

- % of days with meeting attended

- % of days with sober person contacted

- % of days with fellow called

- % of days with exercise

- % of days eating enough

CALENDAR HEATMAP

- Monthly calendar grid

- Days with check-ins get a colored cell based on risk level: green=low, yellow=moderate, red=high, grey=no check-in

- Tap a day to open that day’s check-in detail

- Current month shown by default with previous/next month navigation

STREAK STATS

Compute server-side and return as a single JSON payload. Show:

- Current check-in streak (consecutive days with at least one check-in)

- Longest check-in streak

- Total check-ins logged

- Average mood this week

- Average craving this week

- Average sleep this week

- For each sobriety tracker: current active duration and longest streak before any reset

INSIGHTS PAGE LAYOUT

Top to bottom:

1. Streak stats row (stat cards)

1. Mood and craving trend charts

1. Calendar heatmap

1. Sleep, energy, focus charts

1. Recovery habit frequency bars

1. Sobriety tracker reset history (list with dates and notes)

DATA EXPORT

- Export button on Insights page labeled “Export my data”

- Export check-ins as CSV with all fields

- Export sobriety tracker data as CSV including reset history

- Client-side download — no server storage needed

- Both exports trigger as separate file downloads

CHECK-IN EDIT AND BACKFILL

Edit existing check-ins:

- On any History detail view, show an Edit button (not just today — all entries)

- Allow editing all input fields

- Do not re-run AI on edit — keep original AI output

- Mark edited entries with a small “edited” badge in history

Backfill a missed check-in:

- Add “Log a missed check-in” button on the History page

- User picks a past date (yesterday or earlier, never future)

- Full check-in form appears with that date pre-selected

- AI generates a response normally

- Entry saves with the chosen date as created_at

- Mark backfilled entries with a small “backfilled” badge in history

ERROR HANDLING

- Charts should degrade gracefully with insufficient data — show a “Not enough data yet” message

- Export should handle empty data cleanly

- Edit and backfill should validate inputs the same way as normal check-ins

At the end:

- Summarize exactly what was implemented

- List any database migrations or setup steps needed

- Identify the exact next step for V2D

Run as persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.

V2D

Upgrade the existing recovery check-in app to V2D only.

Important constraints:

- This is the final polish and infrastructure phase

- Do not add new features or data models

- Focus only on PWA installability, UX polish, onboarding refinement, and settings

- Extend what exists — do not rebuild from scratch

V2D GOALS

1. Make the app installable as a PWA

1. Refine onboarding flow

1. Polish UI transitions and interactions throughout

1. Add a simple settings page

PWA — MAKE THE APP INSTALLABLE

- Add manifest.json with:

- name: use whatever the app is currently named

- short_name: short version of the name

- start_url: “/”

- display: “standalone”

- background_color: match current dark theme background

- theme_color: match current dark theme background

- icons: generate simple placeholder icons at 192x192 and 512x512

- Add service worker (sw.js) that:

- Caches the app shell for offline access

- Falls back to cached version when network is unavailable

- Shows a brief offline message if check-in submission fails due to no network: “You’re offline. Check-in will be available when reconnected.”

- Link manifest in HTML head

- Register service worker in main JS

- Verify “Add to Home Screen” works on iOS Safari and Android Chrome

ONBOARDING REFINEMENT

- Review the existing first-run onboarding from V2B

- Improve copy to feel warmer and more intentional

- Ensure the tracker setup step in onboarding actually works correctly end-to-end

- Add a “Reset onboarding” option in Settings for testing purposes

- Onboarding must still feel calm and minimal — no marketing language, no excessive animation

FINAL UI POLISH

- Review spacing throughout — consistent padding, no orphaned or misaligned elements

- Improve typography hierarchy — section labels, body text, and values should be clearly distinct

- Add subtle entrance animations on result card sections: stagger each section appearing on load

- Add loading skeletons on History and Insights pages while data fetches

- Confirm all tap targets are at least 44px height

- Confirm sliders work correctly on iOS Safari — fix if not

- Smooth transitions between tab changes

- Add a small version label visible somewhere (e.g. “v2.4” in footer or settings)

- Review and fix any rough edges left from V2A through V2C

SETTINGS PAGE

- Accessible from home screen via a gear icon or subtle menu option

- Settings contains:

- Export my data (moved here from Insights, or duplicated here)

- Reset onboarding (for testing — shows onboarding again on next open)

- Date-shift prompt toggle (on/off)

- App version label

- Nothing else — keep it minimal

ERROR AND EDGE CASE REVIEW

- Confirm app handles zero check-ins gracefully everywhere (History, Insights, Home)

- Confirm app handles zero trackers gracefully

- Confirm offline state shows cleanly without crashing

- Confirm all error messages are user-friendly and non-technical

At the end:

- Summarize exactly what was implemented

- Confirm PWA installability was verified

- Note any remaining known issues or future improvement areas

Run as persistent web server suitable for Replit preview.

Prompt me to add any required environment variables to Replit Secrets.
