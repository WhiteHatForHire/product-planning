---
title: "Kairos Rescue 6 PR Run"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Kairos app /Active Directives/Kairos Rescue 6 PR Run.docx"
status: active
privacy: working
tags:
  - product
---

# Kairos Rescue 6 PR Run

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Apply .symposium/AUTONOMY_LAYER.md before executing.

Surfaces:          src/components/* (all), src/app/tech-week/* (all),

src/app/api/* (read where relevant),

src/lib/* (read + add), src/styles/* (or equivalent),

tailwind.config.* (or equivalent), package.json

Production impact: full product-quality rescue of public Tech Week artifact

Council of Models: non-blocking (agent applies internal review, documents

findings in docs/run-notes/, proceeds without waiting)

Auto-merge:        no (each phase PR awaits Marcus review at merge time;

agent opens PRs but does NOT merge any)

Credentials:       ANTHROPIC_API_KEY (runtime profile parse only)

Agent:             CC Cloud

Execution mode:    one agent run, six sequential PRs

## STACKED PR RULES

This is a stacked PR run. Each phase branch is intentionally cut from the

previous phase branch. Open all PRs sequentially. Do NOT merge any PRs.

Marcus will review and merge manually.

Do not rebase, squash, force-push, or rewrite earlier phase branches after

later phases are opened unless explicitly instructed.

Auto-proceed from phase to phase ONLY when that phase's smoke assertions

pass. If a phase fails after one fix attempt, halt the run and write

BLOCKERS_FOR_MARCUS.md with the exact failure, suspected cause, and

recommended next move. Do not push broken stacked PRs downstream.

## HARD GATE — VERIFY BEFORE PHASE A, AUTO-PROCEED IF PASSED

1. src/data/events.enriched.json exists on main

2. Spot check 10 random events: vibe accurate on ≥8, agentic_signal

differentiates clearly, founder_density populated, topic_tags

non-trivial on ≥8

3. Enrichment skip rate <5% of total events (51 of 1035 max)

If all three pass, proceed automatically to Phase A. If any fail, halt

and surface findings to BLOCKERS_FOR_MARCUS.md. Do not run UI work on

partial enrichment data.

## ROLE

Turn the Kairos NYC Tech Week 2026 event browser from a working prototype

into a credible public-facing Symposium Studios proof artifact. The current

UI reads like an internal admin dashboard. After this directive, it should

read as curated event intelligence for serious Tech Week operators.

Fix the broken discovery loop end-to-end:

discover → search/filter → shortlist → view schedule → resolve conflicts → export

## LOCKED PRODUCT DECISIONS (DO NOT RE-LITIGATE)

1. Drop agentic_signal 0-3 slider from user-facing UI.

2. Replace with computed Signal Match labels per card:

- "High signal" (strong, conservative — see Phase C labeling rules)

- "Good fit" (partial match)

- "Maybe useful" (weak match)

- No label if profile not completed or skipped

3. Optional reason line under label, deterministic from tag intersection.

Example: "Matches: agentic, founder, evening."

4. Profile intake is a soft first-visit prompt with immediate skip. MUST

NOT block browsing — event list renders behind/after dismissal.

Persists in localStorage as kairos.profile. Header has Reset button to

clear and re-open.

5. Calendar is a provider picker (Google / Apple / Outlook / Download .ics).

No OAuth. Choice persists in localStorage, changeable later.

6. Search is client-side Fuse.js over corpus of title, host_org,

neighborhood, borough (derived), description if any, topic_tags,

vibe, alcohol_forward, sober_friendly. Alias map applied.

7. NL parse route stays as enhancement only. Basic search works without

any API credits.

8. Filters: pill/chip toggles for topic, vibe. Borough accordions for

neighborhood (Manhattan, Brooklyn, Queens, Virtual, Other). Day and

time as visual segmented pickers. Selected filters as removable chips

with Clear All.

9. Shortlist persists in localStorage. Schedule page groups by day with

conflict warnings on overlapping events. Exports as .ics and via

CSS browser print (no PDF library dependency).

10. No Format or Audience filter dimensions in V1.

## LOCKED VISUAL DIRECTION

Dark theme, builder-class aesthetic. Reference class: Linear, Vercel

dashboard, Modal Labs, Cursor, claude.ai. Not consumer-app.

Design tokens (Phase A produces canonical values):

- Background: near-black with slight warm tone (~#0a0a0a)

- Card surface: slightly elevated dark gray (~#141414)

- Borders, not shadows, for elevation

- Text: high-contrast white for titles, medium gray for metadata

- Accent: amber for High Signal match labels

- Green reserved for sober-friendly indicator

- Red/orange for alcohol-forward warning, used sparingly

- Typography: Inter or Geist for body, Geist Mono or JetBrains Mono for

times, counts, tag chips

- Sharp corners or 4px max radius

- No gradients, no glass morphism, no shadows on cards

- Subtle hover elevation via border color shift

- Generous spacing, breathing room

## PHASE A — DESIGN FOUNDATIONS

Branch: feat/kairos-design-foundations (cut from main)

PR title: feat(design): dark theme foundations + sticky header shell

Pre-flight reads:

- .symposium/skills/review/public-surface-qa/SKILL.md (read fully)

- .symposium/skills/frontend-design/SKILL.md if present

- Current tailwind config, global styles, layout

- All existing components in src/components/

Internal Council of Models review (non-blocking):

Apply council-review on proposed design token set. Document findings

in docs/run-notes/phase-a-design-council.md. Proceed without waiting.

Implementation:

- Create design token system in tailwind config + CSS vars

- Replace light theme with locked dark palette

- Build sticky header shell: logo/title left, nav slots right (Shortlist

count, Schedule link, Reset profile)

- Build new EventCard component skeleton matching visual spec (visual

only, no functional changes)

- Mobile breakpoints: header collapses to sticky top action bar with

Filters, My Schedule (count), Search icon

- No horizontal overflow at 375px

Smoke assertions:

- Playwright: header sticky on scroll at desktop and mobile

- Playwright: no horizontal scroll at 375px

- Dark theme applied across /tech-week, /tech-week/shortlist,

/tech-week/schedule

Commit: feat(design): dark theme tokens + sticky header shell

Open PR. Do NOT halt. Proceed to Phase B.

## PHASE B — SEARCH REBUILD

Branch: feat/kairos-search-rebuild (cut from Phase A branch)

PR title: feat(search): client-side Fuse.js with alias matching

Pre-flight:

- pnpm add fuse.js

- Read /api/search/parse route

- Read events.enriched.json shape

Implementation:

- src/lib/search/corpus.ts: normalized search corpus per event from

title, host_org, neighborhood, borough (derive from neighborhood),

description if any, topic_tags, vibe, alcohol_forward, sober_friendly,

virtual flag

- src/lib/search/aliases.ts:

founders → founder, startup, operator, builder

agentic → agents, AI agents, LLM, automation, AI-native

evening → PM, night, happy-hour

breakfast → morning

no alcohol → breakfast, coffee, run, wellness, sober-friendly

- Fuse.js with weighted keys (title 2x, host 1.5x, tags 1.5x, rest 1x)

- Replace existing search box. Fix container clipping.

- Client-side, instant, no API call

- NL parse triggered only on queries >5 words OR explicit toggle

- Empty state: "No events match. Clear search or filters."

Smoke assertions:

- "founders" returns Founders Morning Run

- "agentic" returns events with agentic_signal >= 2

- "happy hour" returns events with vibe = happy-hour

- "Williamsburg" returns Brooklyn events with neighborhood match

- Search input no clip at 375px

- Search combines with filters

Commit: feat(search): client-side Fuse.js search with alias matching

Open PR. Do NOT halt. Proceed to Phase C.

## PHASE C — PROFILE INTAKE + SIGNAL MATCH

Branch: feat/kairos-intake-signal (cut from Phase B branch)

PR title: feat(personalization): profile intake prompt + Signal Match labels

Pre-flight:

- Read /api/intake/parse route

- Read existing intake component if any

Internal Council of Models review (non-blocking):

Apply council-review on Signal Match scoring rules. Document in

docs/run-notes/phase-c-signal-match-council.md. Proceed.

Implementation:

- Soft first-visit personalization prompt on /tech-week if no

kairos.profile in localStorage

- MUST NOT block browsing. Implementation options, agent picks one:

- Dismissible banner/card above events with "Personalize my map" CTA

- Lightweight modal that closes on backdrop click and shows event list

behind it on dismissal

- Prompt asks: role, what you're building, what you're hunting for

(capital / partners / hires / learning / customers), sober-friendly

preference, days available

- Free-text textarea + voice option if /api/intake/voice works

- Submit calls /api/intake/parse to extract structured profile, store

as kairos.profile

- Skip / dismiss: closes prompt, sets kairos.profile = { skipped: true }

- Header "Reset profile" link clears localStorage and re-opens prompt

- src/lib/signal-match.ts: deterministic scoring against profile

- Signal Match labeling rules (CONSERVATIVE, prefer under-labeling):

- Compute raw match strength per event from tag intersection

- "High signal" reserved for top ~20-30% of matched events at most,

OR events with explicit profile hunt match (e.g., user hunting

"capital" + event has investor_density "high")

- "Good fit" for clear partial matches

- "Maybe useful" for weak matches

- No label: weak or absent profile signal

- If many events would qualify as High signal, rank by strength and

reserve label for strongest. Avoid label inflation. Better to

under-label than over-label.

- EventCard renders Signal Match label using amber accent

- Optional reason line, max 4 matching tags

Smoke assertions:

- First visit shows personalization prompt

- Prompt is dismissible immediately, event list visible behind/after

- Skip / dismiss closes and persists skip

- Reset profile re-opens prompt

- After intake, /tech-week shows Signal Match labels

- If skipped or absent, no labels

- Card layout adapts when label absent

- High signal labels do not appear on majority of cards in any reasonable

profile (validate: complete intake, count High signal labels, must be

≤30% of matched events)

Commit: feat(personalization): profile intake + Signal Match

Open PR. Do NOT halt. Proceed to Phase D.

## PHASE D — FILTER REDESIGN

Branch: feat/kairos-filter-redesign (cut from Phase C branch)

PR title: feat(filters): pill toggles, borough accordions, mobile drawer

Pre-flight:

- Read current FilterPanel

- Review visual spec for chip styling

Implementation:

- Replace topic checkboxes with pill toggle chips

- Replace vibe checkboxes with pill toggle chips

- Day: segmented day picker (Sun May 31 through Sat Jun 6)

- Time of day: pill chips (Morning, Midday, Afternoon, Evening, Late)

- Neighborhood: borough accordions

- Manhattan (all Manhattan neighborhoods nested)

- Brooklyn

- Queens

- Virtual

- Other / Unknown

- Click borough to expand/collapse, click neighborhood chip to toggle

- Preferences: "Hide alcohol-forward" and "Only sober-friendly" stay

as binary toggles

- "Agentic events only" toggle — only renders if any event has

agentic_signal >= 2

- Selected filters as removable chips above results

- "Clear all" button

- Mobile: filters open in bottom sheet drawer triggered by Filters

button in sticky top action bar

- Mobile initial viewport shows title, count, search, action bar,

events. NOT filters.

Smoke assertions:

- Mobile initial viewport at 375px shows events, not filters

- Filters drawer opens and closes cleanly on mobile

- Selected filter chips appear and remove correctly

- Borough accordion expand/collapse works

- "Agentic events only" hidden when data does not support

Commit: feat(filters): pill toggles, borough accordions, mobile drawer

Open PR. Do NOT halt. Proceed to Phase E.

## PHASE E — CALENDAR PROVIDER PICKER

Branch: feat/kairos-calendar-picker (cut from Phase D branch)

PR title: feat(calendar): provider picker (Google, Apple, Outlook, .ics)

Pre-flight:

- Read existing Add to Calendar implementation

- Read /api/events/[uid]/ics route

Implementation:

- First Add to Calendar click opens provider picker modal:

- Google Calendar

- Apple Calendar

- Outlook

- Download .ics

- Choice saves to localStorage as kairos.calendar_provider

- Subsequent clicks use saved provider, no modal

- Google: open https://calendar.google.com/calendar/render?action=TEMPLATE

prefilled with title, dates, location, description, source URL

- Apple: download .ics file (existing route)

- Outlook: open https://outlook.live.com/calendar/0/deeplink/compose

prefilled

- Download .ics: existing route, force download

- "Change calendar preference" link in settings/header area

Smoke assertions:

- First click opens picker

- Picker choice persists across page reload

- Google link has correct query params (encoded title, dates)

- .ics download works for sample event

- Change preference clears stored choice

Commit: feat(calendar): provider picker with localStorage preference

Open PR. Do NOT halt. Proceed to Phase F.

## PHASE F — SHORTLIST + SCHEDULE LOOP

Branch: feat/kairos-shortlist-schedule (cut from Phase E branch)

PR title: feat(shortlist): full schedule loop with conflict warnings + print

Pre-flight:

- Read /tech-week/shortlist and /tech-week/schedule pages

- Read shortlist localStorage hooks

- Read /api/shortlist/ics route

Implementation:

- Sticky header shows "Shortlist (N)" badge with count from localStorage

- Mobile sticky bottom or top action bar includes My Schedule (N)

- /tech-week/schedule:

- Groups shortlisted events by day in chronological order

- Sorts by start time within each day

- Each event card: time, title, host, venue, neighborhood, RSVP

- Conflict detection: warn on overlapping events

- Remove from shortlist button

- Empty state: "Shortlist events to build your Tech Week map."

- Schedule export buttons:

- Export .ics (bulk download all shortlisted events)

- Print schedule — uses CSS print stylesheet + @media print rules

+ window.print(). Do NOT add @react-pdf/renderer or any PDF

library dependency in this PR.

- Print stylesheet hides navigation, filters, action bars. Renders clean

day-grouped schedule with times, titles, venues. Single page if events

fit, multiple pages with day headers if not.

- /tech-week/shortlist redirects to /tech-week/schedule (consolidate)

Smoke assertions:

- Shortlist count badge updates on add/remove

- Schedule renders grouped by day

- Overlapping events show conflict warning

- Bulk .ics download is parseable calendar file

- Browser print preview shows readable schedule with navigation hidden

- Empty state appears when shortlist empty

Commit: feat(shortlist): schedule loop with conflict warnings + exports

Open PR. Run final summary report.

## END-OF-RUN SUMMARY

After Phase F PR is open, write FINAL_REPORT.md at repo root with:

- All 6 PR URLs

- Council of Models findings from docs/run-notes/

- Any smoke assertions that did not pass per phase

- Any horizontal overflow at 375px (must be zero)

- Any TypeScript errors deferred (must be zero)

- Total events affected: 1035

## CROSS-PHASE ACCEPTANCE CRITERIA

Desktop:

- Dark theme matches locked visual spec

- "founders" search returns Founders Morning Run

- Search bar does not clip

- Filters grouped, borough accordions, selected chips visible

- Shortlist count visible in header

- Calendar provider picker works

- No leftover agentic slider in UI

Mobile (test at 375px):

- Initial viewport shows search, action bar, events (not filters)

- Filters open in drawer

- No horizontal overflow anywhere

- Cards readable and touch-friendly

- My Schedule reachable from sticky action bar

Personalization:

- First visit shows soft personalization prompt that does NOT block

browsing

- Skip / dismiss works and is remembered

- Reset profile re-opens prompt

- Signal Match labels appear after intake

- High signal labels never exceed ~30% of matched events

- Labels degrade gracefully when skipped or absent

## QA PER PR

Each PR description must include:

- Desktop screenshot of affected surface

- Mobile screenshot at 375px of affected surface

- Confirmation of which smoke assertions pass

- Any deferred items logged to docs/run-notes/

Marcus performs manual review on each PR before merging. No auto-merge.

## NON-GOALS

- No Google Calendar OAuth or write access

- No backend rewrite or database migration

- No Format or Audience filter dimensions

- No autonomous AI recommendations beyond Signal Match

- No social features, multi-user shortlists, accounts

- No PDF library dependency (CSS print only)

- No hard onboarding wall (intake must be dismissible immediately)

## HARD STOPS (HALT IMMEDIATELY)

- HARD GATE enrichment quality verification fails

- Any phase smoke assertion fails after one fix attempt — halt run,

write BLOCKERS_FOR_MARCUS.md, do not push to next phase

- Any phase introduces horizontal mobile overflow that cannot be fixed

- TypeScript errors that cannot be resolved without spec changes

GO. Begin with HARD GATE verification.
