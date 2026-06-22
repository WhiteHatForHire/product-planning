---
title: "OpenClaw Briefing and Alerts Projects"
source_archive: "Software Projects"
source_path: "####Software Projects/Techne /AI agents /Open claw /OpenClaw Briefing and Alerts Projects.docx"
status: reference
privacy: working
tags:
  - planning
---

# OpenClaw Briefing and Alerts Projects

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
🦞

OpenClaw

Two-Project Build Guide

Project 1: Daily Morning Briefing Agent

Project 2: Pre-Event Calendar Alert Agent

Google Calendar · Notion · Telegram / WhatsApp · Full Config Files Included

Overview & What You're Building

This guide walks you through two complete OpenClaw projects from scratch. Every config file, every Markdown file, and every MCP connection is written out in full — copy-paste ready. You will not need to guess at any setting.

Project

What It Does

Triggers

Morning Briefing

Sends you a structured daily rundown at a set time every morning covering Google Calendar events, Notion tasks, and key priorities

Daily cron — e.g. 8:00am every day

Pre-Event Alert

Fires a WhatsApp or Telegram message 10 minutes before any Google Calendar event starts, with the event name, time, and location

Continuous cron — checks every 5 minutes

What You Will Have When Done

✅  A 'chief of staff' agent who briefs you every morning before you open your laptop

✅  Real-time calendar nudges so you never miss a meeting or appointment

✅  Your Notion tasks pulled into every briefing automatically

✅  Everything delivered to your phone via WhatsApp or Telegram — no new app needed

✅  All config files written, validated, and ready to use

Services You Will Connect

Service

Role

Connection Method

Time to Set Up

Google Calendar

Source for all events and schedule

MCP server via OAuth

~10 min

Notion

Source for tasks and to-do lists

MCP server via API key

~5 min

Telegram

Delivery channel (recommended)

Bot token via BotFather

~5 min

WhatsApp

Alternative delivery channel

QR code linked device

~3 min

OpenClaw

Orchestration and scheduling engine

Already installed

—

Notion vs Apple Notes

You mentioned moving to Notion — great call. Notion has an official MCP integration that connects cleanly to OpenClaw.

Apple Notes has no public API. It can only be accessed via AppleScript on a local Mac, which breaks if OpenClaw runs on a VPS.

Notion is free for personal use and takes 5 minutes to connect. Everything in this guide is built around Notion.

⚙️  PHASE 1 — FOUNDATIONS: MCP Connections & Channels

Before building either project, get all three external services connected. This is the infrastructure phase. Do this once and both projects inherit it.

Step 1A — Connect Google Calendar via MCP

Google Calendar is the data source for both projects. You connect it once and both agents use it.

STEP

1

Install the Google Calendar MCP server

Run this in your terminal. This installs the official MCP server package that OpenClaw will use to talk to Google Calendar.

npm install -g @modelcontextprotocol/server-google-calendar

STEP

2

Authenticate with Google

Run the OpenClaw credentials command. This opens a browser window for OAuth — sign in with your Google account and grant calendar read access.

openclaw credentials add google

# A browser window opens — sign in and click Allow

# Your token is saved to ~/.openclaw/credentials/google.json

STEP

3

Add Google Calendar to openclaw.json

Open ~/.openclaw/openclaw.json and add the Google Calendar MCP server entry under mcp_servers. Copy this exactly.

// ~/.openclaw/openclaw.json

{

"mcp_servers": [

{

"name": "google-calendar",

"command": "npx",

"args": ["-y", "@modelcontextprotocol/server-google-calendar"],

"env": {

"GOOGLE_CREDENTIALS_FILE": "~/.openclaw/credentials/google.json",

"CALENDAR_READ_ONLY": "true"

}

}

]

}

STEP

4

Test the connection

Restart OpenClaw and verify Google Calendar is reachable.

openclaw restart

openclaw run "List my Google Calendar events for today"

# Should return today's events — if it does, you're connected

Step 1B — Connect Notion via MCP

Notion will be your task and to-do source. The connection uses an internal integration token, which gives OpenClaw read access to the databases you specify.

STEP

1

Create a Notion Integration

Go to notion.so/my-integrations and create a new integration. Name it 'OpenClaw'. Copy the Internal Integration Token — it starts with 'secret_'.

# Go to: https://www.notion.so/my-integrations

# Click '+ New integration'

# Name: OpenClaw

# Capabilities: Read content (that's all you need)

# Copy the token — looks like: secret_xxxxxxxxxxxxxxxxxxxxxx

STEP

2

Share your databases with the integration

In Notion, open each database you want OpenClaw to read (e.g. Tasks, Projects). Click the '...' menu → Connections → OpenClaw. Do this for every database you want included in your briefing.

# For each Notion database you want in your briefing:

# 1. Open the database in Notion

# 2. Click '...' (top right) → Connections

# 3. Search for 'OpenClaw' and click Connect

#

# Recommended databases to connect:

#   - Tasks / To-Do

#   - Projects

#   - Daily Notes (if you have one)

STEP

3

Install the Notion MCP server and add to openclaw.json

Add the Notion entry to your mcp_servers array alongside Google Calendar.

// ~/.openclaw/openclaw.json — full mcp_servers section

{

"mcp_servers": [

{

"name": "google-calendar",

"command": "npx",

"args": ["-y", "@modelcontextprotocol/server-google-calendar"],

"env": {

"GOOGLE_CREDENTIALS_FILE": "~/.openclaw/credentials/google.json",

"CALENDAR_READ_ONLY": "true"

}

},

{

"name": "notion",

"command": "npx",

"args": ["-y", "@modelcontextprotocol/server-notion"],

"env": {

"NOTION_API_KEY": "secret_YOUR_TOKEN_HERE"

}

}

]

}

STEP

4

Test the Notion connection

Restart OpenClaw and confirm Notion tasks are readable.

openclaw restart

openclaw run "List my open tasks from Notion"

# Should return tasks from your connected databases

Step 1C — Connect Your Delivery Channel

Option A: Telegram (Recommended — 5 minutes)

Telegram is the fastest and most reliable channel for OpenClaw. Start here.

Open Telegram on your phone or desktop and search for @BotFather

Send the message: /newbot

Follow the prompts: give your bot a name (e.g. 'My Assistant') and a username (e.g. MyAssistantBot)

Copy the bot token BotFather sends you — it looks like: 7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxx

In the OpenClaw Web UI: Channels → Add Channel → Telegram → paste your token → Save

Start a conversation with your new bot in Telegram

Send 'hello' — your agent should reply within seconds

# Alternatively, add directly to openclaw.json:

{

"channels": [

{

"type": "telegram",

"token": "7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxx",

"name": "my-telegram",

"default_outbound": true

}

]

}

Option B: WhatsApp

Use this if you prefer WhatsApp. Connect it in addition to or instead of Telegram.

In the OpenClaw Web UI: Channels → Add Channel → WhatsApp

A QR code appears. Open WhatsApp on your phone.

Go to: Settings → Linked Devices → Link a Device

Scan the QR code. Channel status changes to Connected within 30 seconds.

Send yourself a WhatsApp message — your agent will respond.

// openclaw.json channels entry for WhatsApp:

{

"channels": [

{

"type": "whatsapp",

"name": "my-whatsapp",

"default_outbound": true

}

]

}

Which Channel to Use for Outbound Alerts

Set default_outbound: true on whichever channel you want alerts sent to automatically.

You can have both connected — Telegram for testing, WhatsApp for daily use.

The cron jobs and heartbeat tasks will use the default_outbound channel unless you specify otherwise.

🌅  PROJECT 1 — DAILY MORNING BRIEFING AGENT

Every morning at a time you set, your agent messages you a structured daily rundown. It pulls from Google Calendar for your schedule and Notion for your open tasks. The result is a concise, readable message you can scan in under 60 seconds — your AI chief of staff.

What the Morning Message Looks Like

📅  CALENDAR — 3 events today

9:00am  Weekly Team Standup (Google Meet)

2:00pm  Client Review — Acme Project

5:30pm  Gym (personal)

📌  TOP PRIORITIES (from Notion)

→ Finish homepage copy draft [due today]

→ Send invoice to Client B

→ Review PR #42 before 3pm

⚠️  HEADS UP

→ Gap between 10am–2pm — good focus block

→ Client Review has no prep notes — might want to add some

Project 1 Files — Copy These Exactly

File 1: ~/.openclaw/workspace/SOUL.md

This defines who your agent is and what it will and won't do. This is the base of every request.

# ~/.openclaw/workspace/SOUL.md

# Identity

You are a personal chief of staff and daily briefing assistant.

You are concise, structured, and always lead with what matters most.

You write for a phone screen — short lines, clear sections, easy to scan.

You never pad responses or add unnecessary commentary.

## What you do

- Deliver a structured morning briefing every day at the scheduled time

- Pull from Google Calendar for schedule and Notion for tasks

- Flag anything that needs attention or looks like a conflict

- Identify focus blocks (gaps in the calendar) and call them out

- Send pre-event reminders 10 minutes before any calendar event

## What you NEVER do

- Create, edit, or delete calendar events without explicit instruction

- Modify Notion tasks or databases without explicit instruction

- Send messages to anyone other than me

- Share my schedule or task list with anyone

- Add opinions, motivational quotes, or filler to briefings

## Tone

Direct. Informative. Zero fluff.

Talk to me like a sharp assistant who respects my time.

File 2: ~/.openclaw/workspace/USER.md

What the agent knows about you. Fill in your real details — the more specific, the better the briefing.

# ~/.openclaw/workspace/USER.md

## About Me

- Name: [Your name]

- Timezone: [e.g. America/New_York | Asia/Makassar for Bali]

- Working hours: [e.g. 9am-6pm local time]

- Primary location: [City you're in right now]

## My Schedule Preferences

- Morning briefing time: [e.g. 8:00am]

- I consider anything before [time] to be morning

- My most important work typically happens: [e.g. 9am-12pm]

- I prefer back-to-back meetings on: [e.g. Tuesday and Thursday]

## My Notion Setup

- Main task database: [e.g. 'Tasks' or 'To-Do']

- I use Status property values: [e.g. Not Started, In Progress, Done]

- Priority field name: [e.g. 'Priority' with values High / Medium / Low]

- Only include tasks with Status NOT equal to Done in briefings

## What I Consider High Priority

- Anything due today

- Anything marked Priority: High

- Any task with a deadline in the next 48 hours

## Briefing Preferences

- Max items per section: 5

- Show calendar location/link if available

- Flag events with no description or prep notes

- Identify the longest focus block in my day

File 3: ~/.openclaw/workspace/AGENTS.md

The operating rules — what the agent can access, how it makes decisions, and when it confirms before acting.

# ~/.openclaw/workspace/AGENTS.md

## Decision Rules

- Read-only actions (calendar lookup, Notion read): act immediately, no confirmation needed

- Any write action (creating events, editing tasks): show me what you'll do and wait for approval

- Sending me a message: always OK, do it

- Sending any message to anyone else: never, without explicit instruction

## Data Sources

- Google Calendar: read-only, all calendars I own

- Notion: read-only, connected databases only

- No other data sources unless I explicitly connect them

## Briefing Rules

- Always pull fresh data at the time of the briefing — never use cached data

- If Google Calendar is unreachable, say so and proceed with Notion data only

- If Notion is unreachable, say so and proceed with calendar data only

- Always include the day and date in the briefing header

- Timezone for all times: use my timezone from USER.md

## Alert Rules

- Pre-event alerts: send exactly 10 minutes before event start time

- Only alert for events on my primary calendar unless I say otherwise

- Do not send an alert for events I've declined

- Do not send duplicate alerts — track which events have been alerted

## Output Format for Briefing

Start with: Good morning [name] — [Day, Date]

Then sections in this order:

1. Calendar (📅) — all events today with time and title

2. Focus Block (🎯) — longest gap, if 90 min or more

3. Priorities (📌) — top 5 open Notion tasks by due date and priority

4. Heads Up (⚠️) — anything flagged: conflicts, events without notes, overdue tasks

End with a single-line summary of what to focus on first.

File 4: ~/.openclaw/workspace/HEARTBEAT.md

The proactive background instructions. This is what the agent checks automatically without you asking.

# ~/.openclaw/workspace/HEARTBEAT.md

## Morning Briefing

Every day at [YOUR TIME e.g. 8:00am], run the morning briefing:

- Fetch today's events from Google Calendar

- Fetch open tasks from Notion (Status != Done, or Status != Complete)

- Identify top priorities: due today + high priority

- Identify the longest focus block (gap of 90 min or more)

- Flag any events with no description

- Flag any tasks that are overdue

- Format and send the briefing to my default channel

## Pre-Event Alerts

Every 5 minutes, check for upcoming calendar events:

- Look for any event starting in the next 10-15 minutes

- If found and not yet alerted, send a notification message

- Mark the event as alerted so it doesn't fire again

- Include: event name, start time, location or meeting link if available

## Weekly Kickoff (Optional)

Every Monday at [YOUR TIME e.g. 8:30am], after the daily briefing, also send:

- This week's calendar overview (Monday through Friday)

- Any Notion tasks due this week

- A one-line framing of the week's main goal

File 5: ~/.openclaw/cron/jobs.json

This is the scheduler. Two jobs: the morning briefing (runs once daily) and the event-checker (runs every 5 minutes for alerts).

// ~/.openclaw/cron/jobs.json

{

"jobs": [

{

"name": "morning-briefing",

"description": "Daily morning rundown from Google Calendar and Notion",

"schedule": "0 8 * * *",

"task": "Run the morning briefing. Pull todays events from Google Calendar and open tasks from Notion. Format and send to my default channel.",

"enabled": true

},

{

"name": "pre-event-checker",

"description": "Checks every 5 minutes for events starting in the next 10 minutes",

"schedule": "*/5 * * * *",

"task": "Check Google Calendar for any events starting in the next 10 to 15 minutes that have not yet been alerted. If found, send a pre-event alert to my default channel.",

"enabled": true

}

]

}

Cron Schedule Quick Reference

"0 8 * * *"      → Every day at 8:00am

"0 7 * * 1-5"    → Weekdays only at 7:00am

"0 9 * * *"      → Every day at 9:00am

"30 7 * * *"     → Every day at 7:30am

"*/5 * * * *"    → Every 5 minutes (for pre-event checker)

Change the '8' to whatever hour you want your briefing.

Time is in 24-hour format and uses your system timezone.

File 6: ~/.openclaw/skills/morning-briefing/SKILL.md

Install or create this skill. It gives the agent precise instructions for how to build and format the briefing.

---

name: morning-briefing

description: Generates a structured daily briefing from Google Calendar and Notion tasks

---

# Morning Briefing Skill

## When to use

Use this skill whenever running the morning briefing cron job, or when the user

asks for a briefing, rundown, or summary of their day.

## Data to fetch

1. Google Calendar: all events for today (use the google-calendar MCP tool)

2. Notion: all tasks where Status is not Done/Complete (use the notion MCP tool)

## Format rules

- First line: Good morning [name from USER.md] — [Weekday, Month Day]

- Use emoji headers for each section

- Times in 12-hour format with am/pm

- If an event has a video link (Zoom/Meet/Teams), include it

- If an event has a location, include it

- Max 5 tasks in the Priorities section — rank by: due today first, then High priority

- Keep total message under 350 words — this is read on a phone

## Section order

1. 📅 CALENDAR — list all events with time and title

2. 🎯 FOCUS BLOCK — if there is a gap of 90 min or more, call it out

3. 📌 PRIORITIES — top tasks from Notion

4. ⚠️ HEADS UP — anything flagged (conflicts, no-prep events, overdue tasks)

5. One-line closer: 'First thing to tackle: [most important item]'

## Error handling

- If Google Calendar is unreachable: note it and show Notion data only

- If Notion is unreachable: note it and show calendar data only

- If both fail: send 'Could not fetch briefing data — please check MCP connections'

# Install the skill:

mkdir -p ~/.openclaw/skills/morning-briefing

# Then paste the content above into SKILL.md

# Or use the CLI:

openclaw skills create morning-briefing

⏰  PROJECT 2 — PRE-EVENT CALENDAR ALERT AGENT

Every 5 minutes, OpenClaw silently checks your Google Calendar. When it finds an event starting in the next 10-15 minutes that it hasn't already alerted you about, it fires a message to your phone. That's it. Simple, reliable, and completely automatic.

What the Alert Message Looks Like

⏰  Starting in 10 minutes:

Weekly Team Standup

9:00am — 9:30am

📍 Google Meet: meet.google.com/abc-defg-hij

---

⏰  Starting in 10 minutes:

Client Review — Acme Project

2:00pm — 3:00pm

📍 Conference Room B, 5th Floor

Project 2 shares most of its infrastructure with Project 1 — the same MCP connections, the same SOUL.md, the same channels. The only new pieces are the alert skill and a small memory file to track which events have already been alerted (so you don't get duplicate messages).

Project 2 Files

File 7: ~/.openclaw/skills/event-alert/SKILL.md

This skill defines exactly how the agent checks for upcoming events and formats the alert message.

---

name: event-alert

description: Checks Google Calendar for events starting in 10 minutes and sends a pre-event alert

---

# Pre-Event Alert Skill

## When to use

Use this skill when the pre-event-checker cron job runs (every 5 minutes).

Also use when the user asks to be reminded about upcoming events.

## How to check for upcoming events

1. Get the current time

2. Use the google-calendar MCP tool to fetch events starting between

'now + 8 minutes' and 'now + 15 minutes'

(This window catches events at the 10-min mark even if the cron runs slightly late)

3. For each event found:

a. Check ~/.openclaw/workspace/memory/alerted-events.md to see if this event ID

has already been alerted today

b. If not yet alerted: send the alert and add the event ID to alerted-events.md

c. If already alerted: skip it

## Alert message format

Line 1:  ⏰  Starting in 10 minutes:

Line 2:  (blank)

Line 3:  [Event Title]

Line 4:  [Start time] — [End time]

Line 5:  If location exists: 📍 [location]

Line 6:  If video link exists (Zoom/Meet/Teams URL): 📍 [link]

Line 7:  If no location: omit line 5-6

## Declined events

Do NOT send alerts for events where my RSVP status is Declined.

## All-day events

Do NOT send 10-minute alerts for all-day events.

These are handled in the morning briefing only.

## Multiple events

If two events are starting in the next 10-15 minutes, send one message per event.

Do not combine them into one message.

# Create and install the skill:

mkdir -p ~/.openclaw/skills/event-alert

# Paste the content above into SKILL.md

File 8: ~/.openclaw/workspace/memory/alerted-events.md

This file is how OpenClaw remembers which events it has already alerted you about, so you don't get duplicate messages. The agent writes to this file automatically. You create it empty — the agent does the rest.

# Create the file:

mkdir -p ~/.openclaw/workspace/memory

touch ~/.openclaw/workspace/memory/alerted-events.md

# The agent will auto-populate it with entries like:

# 2026-04-22: event_id_abc123 | Team Standup | 9:00am — alerted at 8:50am

# 2026-04-22: event_id_def456 | Client Review | 2:00pm — alerted at 1:50pm

#

# The agent clears old entries daily to keep the file lean

Why This File Matters

Without it: every time the cron runs (every 5 min), it finds the same upcoming event and sends you another alert. You'd get 2-3 duplicate messages per event.

With it: the agent checks the file, sees it already sent the alert, and skips it.

The agent manages this file automatically — you never need to touch it.

Cron Jobs — Final Complete Version

This is the final jobs.json with both projects' cron jobs combined. Replace your existing jobs.json with this.

// ~/.openclaw/cron/jobs.json — FINAL VERSION (both projects)

{

"jobs": [

{

"name": "morning-briefing",

"description": "Daily morning rundown from Google Calendar and Notion",

"schedule": "0 8 * * *",

"task": "Run the morning briefing skill. Fetch todays Google Calendar events and open Notion tasks. Format and send the briefing to my default channel.",

"timezone": "America/New_York",

"enabled": true

},

{

"name": "pre-event-checker",

"description": "Fires a 10-minute alert before any Google Calendar event",

"schedule": "*/5 * * * *",

"task": "Run the event-alert skill. Check Google Calendar for events starting in the next 10 to 15 minutes. If any are found and have not been alerted yet today, send a pre-event alert to my default channel and log the event ID to alerted-events.md.",

"timezone": "America/New_York",

"enabled": true

},

{

"name": "weekly-kickoff",

"description": "Monday morning weekly overview",

"schedule": "30 8 * * 1",

"task": "After the morning briefing, also pull this weeks Google Calendar events (Monday through Sunday) and any Notion tasks due this week. Send a brief weekly overview as a follow-up message.",

"timezone": "America/New_York",

"enabled": true

}

]

}

Change Your Timezone

Replace "America/New_York" with your timezone.

Bali / Indonesia: Asia/Makassar

London: Europe/London

LA / Pacific: America/Los_Angeles

Full list: en.wikipedia.org/wiki/List_of_tz_database_time_zones

📁  COMPLETE FILE STRUCTURE — EVERYTHING IN ONE VIEW

Here is every file you need, with its location. If all of these exist and are filled in, both projects are fully operational.

~/.openclaw/

│

├── openclaw.json                         ← MCP servers + channels config

│

├── cron/

│   └── jobs.json                         ← morning-briefing + pre-event-checker

│

├── credentials/

│   └── google.json                       ← Auto-created by: openclaw credentials add google

│

├── skills/

│   ├── morning-briefing/

│   │   └── SKILL.md                      ← Briefing format + data fetch instructions

│   └── event-alert/

│       └── SKILL.md                      ← Alert format + dedup logic

│

└── workspace/

├── SOUL.md                           ← Agent identity + hard limits

├── USER.md                           ← Your name, timezone, Notion setup

├── AGENTS.md                         ← Operating rules + decision logic

├── HEARTBEAT.md                      ← Proactive background instructions

├── MEMORY.md                         ← Long-term memory (agent-managed)

└── memory/

└── alerted-events.md             ← Event dedup log (agent-managed)

Complete openclaw.json — Copy This Entire File

This is your master config file with everything in it: model, MCP servers, and channels. Replace YOUR_ placeholders with your real values.

// ~/.openclaw/openclaw.json

{

"gateway": {

"host": "127.0.0.1",

"port": 18789

},

"auth": {

"enabled": true,

"token": "GENERATE_A_RANDOM_32_CHARACTER_STRING_HERE"

},

"models": [

{

"provider": "anthropic",

"model": "claude-opus-4-6",

"apiKey": "sk-ant-YOUR_ANTHROPIC_KEY_HERE",

"default": true

}

],

"channels": [

{

"type": "telegram",

"token": "YOUR_TELEGRAM_BOT_TOKEN_HERE",

"name": "my-telegram",

"default_outbound": true

}

// Uncomment below to also enable WhatsApp:

// {

//   "type": "whatsapp",

//   "name": "my-whatsapp",

//   "default_outbound": false

// }

],

"mcp_servers": [

{

"name": "google-calendar",

"command": "npx",

"args": ["-y", "@modelcontextprotocol/server-google-calendar"],

"env": {

"GOOGLE_CREDENTIALS_FILE": "~/.openclaw/credentials/google.json",

"CALENDAR_READ_ONLY": "true"

}

},

{

"name": "notion",

"command": "npx",

"args": ["-y", "@modelcontextprotocol/server-notion"],

"env": {

"NOTION_API_KEY": "secret_YOUR_NOTION_TOKEN_HERE"

}

}

]

}

🚀  BUILD ORDER — DO THESE STEPS IN SEQUENCE

Follow this exact order. Each step depends on the previous one working.

STEP

1

Install OpenClaw (if not done)

curl -fsSL https://openclaw.ai/install.sh | bash   →   openclaw doctor   →   openclaw status

STEP

2

Connect Google Calendar

openclaw credentials add google  →  Add MCP entry to openclaw.json  →  openclaw restart  →  test with: openclaw run 'list my events today'

STEP

3

Connect Notion

Create Notion integration at notion.so/my-integrations  →  Connect your databases  →  Add MCP entry to openclaw.json  →  test with: openclaw run 'list my open tasks from Notion'

STEP

4

Connect Telegram or WhatsApp

Create Telegram bot via @BotFather  →  Add channel entry to openclaw.json  →  Send 'hello' to your bot  →  Confirm it responds

STEP

5

Write SOUL.md, USER.md, AGENTS.md, HEARTBEAT.md

Copy the files from this guide into ~/.openclaw/workspace/  →  Fill in YOUR name, timezone, and Notion setup details in USER.md

STEP

6

Create the two skills

mkdir -p ~/.openclaw/skills/morning-briefing && mkdir -p ~/.openclaw/skills/event-alert  →  Paste SKILL.md content into each folder

STEP

7

Create alerted-events.md

touch ~/.openclaw/workspace/memory/alerted-events.md  →  This is the dedup log for pre-event alerts

STEP

8

Set up cron jobs

Copy the final jobs.json into ~/.openclaw/cron/jobs.json  →  Set your timezone and briefing time  →  openclaw restart

STEP

9

Test the morning briefing manually

openclaw run 'Run the morning briefing now'  →  Check your Telegram/WhatsApp for the message  →  Verify calendar and Notion data appear correctly

STEP

10

Test the pre-event alert

Create a test calendar event 12 minutes from now  →  Wait for the 5-minute cron to run  →  You should receive the alert on your phone

🎉 You're Done

If Step 9 and Step 10 both work, both projects are live.

From this point, OpenClaw runs autonomously. You don't need to do anything.

Every morning: briefing arrives at your set time.

Every event: alert fires 10 minutes before it starts.

Your phone is now your AI chief of staff's primary output device.

Troubleshooting

Problem

Likely Cause

Fix

Briefing never arrives

Cron not running or timezone wrong

Run: openclaw cron status  →  Check timezone in jobs.json matches your local timezone

'health offline' in Web UI

Gateway not started or token mismatch

Run: openclaw start  →  Check token in openclaw.json matches My OpenClaw page

Google Calendar returns no events

OAuth token expired or wrong credentials file path

Run: openclaw credentials refresh google  →  Check path in openclaw.json

Notion returns no tasks

Databases not shared with integration

In Notion: open each database → ... → Connections → connect OpenClaw integration

Duplicate event alerts firing

alerted-events.md missing or not writable

Run: touch ~/.openclaw/workspace/memory/alerted-events.md  →  chmod 644 that file

Telegram bot not responding

Bot token wrong or channel not saved

Re-check the token from BotFather — no spaces, full string  →  openclaw restart

Briefing has no Notion tasks

Notion filter too strict or wrong property names

Check Status property name in your Notion database matches what's in USER.md

Wrong timezone on event times

Timezone not set in jobs.json

Add: 'timezone': 'Your/Timezone' to each job in jobs.json

# Useful debug commands:

openclaw logs              # Live log stream — see every action the agent takes

openclaw cron status       # See all scheduled jobs and when they last ran

openclaw status            # Gateway health + connected channels

openclaw doctor            # Check all dependencies

openclaw skills list       # Confirm both skills are installed

# Run either project manually at any time:

openclaw run "Run the morning briefing now"

openclaw run "Check for upcoming events and send alerts if needed"

What to Build Next

Once both projects are running reliably for a week, these are the natural next expansions:

End-of-day summary — A 5pm message that wraps up the day: what got done in Notion, what's carrying over, and tomorrow's first two events. Add one cron job to jobs.json.

Weekly review — Every Friday at 4pm, a longer message reviewing the week's completed tasks from Notion and next week's calendar overview.

Smart conflict detection — Expand the event-alert skill to flag when two events overlap on the calendar, or when a meeting is back-to-back with no buffer.

Task nudges — If a Notion task is marked High Priority and has been sitting at 'In Progress' for more than 3 days, the agent messages you about it.

Email triage integration — Connect Gmail via MCP and add an email section to the morning briefing: count of unread, any marked urgent, any from key contacts.

Travel-aware briefing — If a calendar event says 'travel' or has a location that isn't your office, the agent includes commute/travel time in the focus block calculation.

🦞 Your AI Chief of Staff Is Live

Two agents. Zero effort after setup. Your phone does the rest.
