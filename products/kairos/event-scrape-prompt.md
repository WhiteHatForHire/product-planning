---
title: "Event scrape prompt"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Kairos app /Event scrape prompt.docx"
status: reference
privacy: working
tags:
  - product
---

# Event scrape prompt

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
You are working as a senior data/tooling engineer.

Goal:

Generate a clean Excel workbook from this ICS calendar feed:

https://www.usecarly.com/calendars/nyc-tech-week-2026.ics

This is for planning NYC Tech Week 2026. I need the output to be useful for filtering, prioritizing, and building a schedule.

Do this autonomously. Do not ask follow-up questions unless the ICS feed is completely unreachable.

TASK

Create a standalone script that:

1. Fetches the ICS file from:

https://www.usecarly.com/calendars/nyc-tech-week-2026.ics

2. Parses all VEVENT entries.

3. Outputs a clean Excel file:

nyc-tech-week-2026-events.xlsx

4. Also output a CSV backup:

nyc-tech-week-2026-events.csv

5. Save both files in a clear output directory, preferably:

./outputs/nyc-tech-week/

6. Include a README or short notes file explaining how to rerun the script.

PREFERRED IMPLEMENTATION

Use Python unless there is a strong reason not to.

Recommended packages:

- requests

- icalendar

- python-dateutil

- openpyxl

- beautifulsoup4, optional, if useful for stripping HTML descriptions

If dependencies are missing, add a requirements.txt and clear install instructions.

Script name:

scripts/export_nyc_tech_week_ics.py

If this repo does not already have a scripts/ directory, create it.

DATA COLUMNS

The Excel and CSV should include these columns:

Required:

- event_id

- title

- start_datetime_local

- end_datetime_local

- date

- day_of_week

- start_time

- end_time

- duration_minutes

- timezone

- location_raw

- venue_name

- address

- neighborhood_guess

- description_clean

- rsvp_url

- source_url

- organizer

- categories

- uid

- status

Add these derived planning columns:

- day_bucket

- time_bucket

- is_morning

- is_afternoon

- is_evening

- possible_alcohol_event

- is_build_event

- is_agentic_ai_event

- is_founder_event

- is_investor_event

- is_healthcare_event

- is_devtools_event

- is_sober_or_wellness_event

- marcus_relevance_score

- marcus_relevance_reason

- priority_bucket

- notes

TIMEZONE

Normalize all dates/times to America/New_York.

The output should be sorted by:

1. date

2. start_datetime_local

3. title

DESCRIPTION CLEANUP

ICS descriptions may contain HTML, escaped characters, RSVP links, host text, and formatting noise.

Clean description_clean so it is readable in Excel:

- Strip HTML tags if present.

- Decode HTML entities.

- Collapse repeated whitespace.

- Preserve meaningful text.

- Do not over-truncate unless cells become unusably large.

- If very long, keep the first ~2000 characters.

URL EXTRACTION

Try to extract the best RSVP or source URL from:

- VEVENT URL field

- DESCRIPTION links

- any Partiful, lu.ma, tech-week.com, eventbrite, usecarly, or similar RSVP link

Set:

- rsvp_url to the most likely registration link

- source_url to the original event/source link if different or if available

LOCATION PARSING

location_raw should preserve the original ICS LOCATION field.

Try to derive:

- venue_name

- address

- neighborhood_guess

Do not hallucinate precise neighborhoods. Use simple heuristics only. If not clear, leave blank or use “Unknown”.

Examples:

- SoHo

- Midtown

- Flatiron

- Chelsea

- Tribeca

- Lower East Side

- East Village

- Williamsburg

- Brooklyn

- Financial District

- Meatpacking

- NoMad

- Union Square

If the location contains one of those neighborhood strings, use it. Otherwise leave blank.

MARCUS RELEVANCE SCORING

This calendar is for Marcus Vale / Symposium Studios.

Marcus’s current ICP and goals:

- agentic delivery systems

- AI-assisted software development

- internal AI tooling

- AI agents in production

- workflow automation

- founder-led companies

- small-to-mid organizations

- devtools

- AI product engineering

- fractional CTO / fCTO work

- consulting for owner-led companies

- teaching CTOs, dev leads, and founders how to use agents responsibly

- Anchor/recovery/wellness is a secondary interest

- sober-friendly events matter because Marcus is prioritizing sobriety

- avoid alcohol-forward events when possible

Compute marcus_relevance_score from 0 to 100 using keyword/heuristic scoring.

Strong positive signals:

- agent

- agentic

- AI-assisted development

- build with agents

- MCP

- Claude

- Codex

- Replit

- Cursor

- Devin

- workflow

- automation

- internal tools

- DevEx

- developer tools

- CTO

- technical founder

- founder

- operator

- GTM automation

- customer support automation

- CX automation

- AI product

- AI engineering

- production AI

- LLM

- RAG

- memory

- evaluation/evals

- governance

- human-in-the-loop

- startup/founder rooms

- a16z / speedrun / Betaworks / Replit / Datadog / Postman / WorkOS / Cloudflare / Shopify / Microsoft / Google / Anthropic / Claude / Tavily / Airtable

Secondary positive signals:

- healthcare AI

- consumer health

- sober

- wellness

- longevity

- founder fitness

- operator dinners

- small curated rooms

- demo nights

- build days

Negative or lower-priority signals:

- alcohol-forward events

- whiskey

- wine

- cocktails

- open bar

- party-only events

- very generic networking

- fashion-only

- crypto-only unless AI/devtool relevant

- student-only

- recruiting-only unless AI engineering relevant

possible_alcohol_event should be true if title/description includes:

- happy hour

- cocktails

- whiskey

- wine

- beer

- open bar

- drinks

- bar

- nightlife

- party

- absinthe

But do not automatically make every happy hour low priority. Just flag it.

priority_bucket rules:

- “Must review” for score >= 80

- “Strong candidate” for 65–79

- “Maybe” for 45–64

- “Low priority” for below 45

marcus_relevance_reason:

Provide a short explanation like:

“Agentic AI + devtools + founder/operator audience”

or

“Sober/wellness signal, Anchor-adjacent”

or

“Generic happy hour, alcohol-forward, weak fit”

EXCEL FORMATTING

Use openpyxl to format the workbook.

Workbook sheets:

1. All Events

2. Must Review

3. Strong Candidates

4. By Day Summary

5. Potential Conflicts

All Events:

- Freeze top row.

- Add filters.

- Auto-size columns reasonably.

- Wrap text for description and notes.

- Make date/time columns readable.

- Apply light formatting to header row.

Must Review:

- Include only priority_bucket = “Must review”

- Sort by date/time.

Strong Candidates:

- Include “Must review” and “Strong candidate”

- Sort by date/time.

By Day Summary:

For each date:

- total events

- must review count

- strong candidate count

- morning count

- afternoon count

- evening count

- possible alcohol event count

Potential Conflicts:

List same-day events that overlap or start within 30 minutes of another “Must review” or “Strong candidate” event.

Include:

- date

- event A title

- event A time

- event A location

- event A score

- event B title

- event B time

- event B location

- event B score

- conflict_reason

QUALITY CHECKS

After generating files:

- Print total events parsed.

- Print number of events by day.

- Print number of Must Review / Strong Candidates.

- Print top 25 events by marcus_relevance_score.

- Print any parsing errors/warnings.

- Confirm the output paths.

ROBUSTNESS

Handle:

- missing DTEND

- all-day events

- malformed descriptions

- duplicate UIDs

- timezone-aware and timezone-naive datetimes

- recurring events if present

- folded ICS lines

If an event has DTSTART but no DTEND:

- set end equal to start + 60 minutes

- add note: “No DTEND found; defaulted to 60 min”

If recurring events exist:

- expand recurrences occurring between 2026-06-01 and 2026-06-07 if reasonable.

- If recurrence expansion is too complex, include the base event and add a warning in notes.

DO NOT

- Do not manually copy/paste the ICS content.

- Do not hardcode event rows.

- Do not hallucinate missing data.

- Do not skip events because they seem irrelevant.

- Do not overwrite unrelated files.

- Do not require a web app or database.

DELIVERABLES

Create:

- scripts/export_nyc_tech_week_ics.py

- requirements.txt if needed

- outputs/nyc-tech-week/nyc-tech-week-2026-events.xlsx

- outputs/nyc-tech-week/nyc-tech-week-2026-events.csv

- outputs/nyc-tech-week/README.md or NOTES.md

Then run the script and verify the files exist.

At the end, give me:

1. Path to the Excel file

2. Path to the CSV file

3. Total event count

4. Top 15 Marcus-relevant events by score

5. Any warnings or limitations
