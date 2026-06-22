---
title: "5 9 26 Anchor Desktop Design Audit and Redesign Brief"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Audits/5_9_26 Anchor Desktop Design Audit and Redesign Brief.docx"
status: reference
privacy: working
tags:
  - product
---

# 5 9 26 Anchor Desktop Design Audit and Redesign Brief

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Full Audit + Addendum

Anchor Desktop Design Audit and Redesign Brief

Audit date: May 9, 2026 Audit scope: 9 desktop pages at 1280px+ Output target: engineering handoff (CC, Codex, or human implementer) Version: merged from internal audit and external review

1. Overall Diagnosis

Anchor's desktop layout is a mobile app put on a treadmill. The viewport widened, but nothing about the information architecture, component density, or interaction model changed to take advantage of it. Every page is a single, narrow column scrolling vertically through stacked cards. On a 1280+ display, the body content typically occupies 40 to 60 percent of the horizontal canvas and the rest is matte black. This is the dominant problem and it leaks into everything else.

The second problem is that the dark theme is competent but the card system is undisciplined. Almost every piece of content is wrapped in a rounded rectangle with the same elevation, the same border radius, the same internal padding. There is no visual hierarchy between a primary CTA, a passive readout, a section header, and an empty state. The eye has nowhere to land. This is what makes the product feel "wellness startup-ish" rather than "thoughtful digital sponsor". The fix is not more visual flair, it is fewer cards and clearer hierarchy.

The third problem is that desktop affordances Anchor would actually benefit from, master-detail views, persistent context panels, metadata rails, keyboard navigation, multi-column data display, are entirely absent. The Chat page on a desktop screen with no session list, no grounding context panel, and a narrow center column of bubbles is the clearest example. The History detail page with the AI summary stacked above the raw log instead of beside it is another. The History list page with no preview pane is a third. These are not polish issues. They are the difference between a desktop app and a stretched phone screenshot.

2. Per-Page Audit

Home (/app)

Layout. The page uses maybe 35 percent of vertical canvas before the fold and the rest is empty. Three tracker cards sit in a row but each one is a giant horizontal block carrying very little data. The "Latest check-in" card is oversized for the four data points it holds. The two CTAs (Check in again, Chat with my coach) stack full-width when they should be a primary/secondary pair.

Navigation. Top tabs are fine for desktop in principle, but Settings is hidden behind a cog icon in the top-right, and Memory is invisible from this page. The active state on tabs is a thin underline that works but is easy to miss.

Information hierarchy. The "ANCHOR / Saturday, May 9 / Today" stack is doing too much for what it conveys. Streaks are not the hero, the latest check-in is not the hero, the next action is not the hero. Nothing is the hero. The "4 total check-ins" footer is the kind of metadata that belongs in a tooltip, not on the home page.

Visual design. Tracker cards with colored left borders are the strongest design move on this screen. Everything else is the same dark gray rectangle. Typography is legible but undifferentiated.

Desktop patterns missing. Persistent sidebar nav. A "next action" panel. A right rail showing today's data context. Hover states on tracker cards to drill into a tracker. Quick keyboard shortcut to start a check-in (C).

Three most damaging problems.

No primary call to action visually dominates. Check-in is the daily ritual and it should be unmistakably the thing to do, not a button equal in weight to "chat with my coach".

The page does not function as a dashboard. It shows status but does not orient the user about what matters today (a craving spike yesterday, a missed meeting, a streak about to roll).

Settings and Memory are both reachable only from a cog icon, which is a discoverability failure for two of Anchor's most important surfaces.

Check-In (/checkin)

Layout. A 30-plus question form rendered as a single column with mixed widths. Some questions are paired in two columns (Mood/Energy, Meeting/Sober person), others sit alone in a single column with an empty right side (Hours slept full-width, Ate enough today alone in left column). The form has no visible progress, no section grouping headers, no live preview of the AI's read on the data, and the submit button is at the very bottom of a long scroll.

Navigation. The "Midday check-in" pill near the top is the only sense of context. There is no way to skip sections, no way to jump to "feelings" if that is all you want to log, and no way to see how far through the form you are.

Information hierarchy. All sliders carry equal visual weight. The four numeric ratings, the seven yes/no behaviors, the trigger pills, and the two free-text fields are presented as if they are equally important. Mood and craving are the highest-signal data points and they should anchor the form, not blend in.

Visual design. Slider colors (green for high mood, yellow for mid focus, red implied for high craving) are working. Trigger pills are good. The yes/no toggles styled as paired cards are visually heavy for binary inputs.

Desktop patterns missing. A right summary rail that previews the AI's risk read in real time as the user fills the form. Keyboard shortcuts (1 to 10 for sliders, Y/N for binaries, Tab between fields, Cmd+Enter to submit). Section headers (Vitals, Behaviors, Feelings, Reflection). A two-column form layout that respects question grouping.

Three most damaging problems.

"Ate enough today?" sits alone in the left column with the right column empty. This is the visual fingerprint of a mobile form refusing to use the desktop grid.

The submit button is at the bottom of a long scroll. On desktop, a sticky action surface is table stakes.

There is no progress, section structure, or live feedback, so the form feels like a survey instead of a daily ritual where the AI is forming an interpretation alongside the user.

Chat (/chat)

Layout. This is the worst offender for the mobile-stretched problem. A narrow center column of chat bubbles on a 1280+ canvas, with the AI bubbles full-width within that column and the user bubbles right-aligned green. The two side margins are empty black. There is no session history list, no context panel, no suggested prompts.

Navigation. Top tabs only. The "+" icon in the top-right presumably starts a new session but is unlabeled. There is no way to see past chat sessions or scope the current one.

Information hierarchy. The chat itself has clean turn structure with timestamps, but the AI's responses appear without any indication of what data they are grounded in. The user sent "I just completed a check-in and want to talk through it" twice in a row, which the screenshot suggests is either a UI bug or an interaction model that lets duplicates through silently.

Visual design. Bubbles look fine. The audio playback icons on AI responses are a nice touch. The "Say something" input is generic.

Desktop patterns missing. Session sidebar (most chat apps have this). Context panel showing today's check-in data so the user understands what the AI knows. Suggested prompts based on recent state ("ask about your craving spike yesterday"). Slash commands. Copy / regenerate / thumbs on AI messages.

Three most damaging problems.

The page is structurally identical to the mobile chat. There is no session list and no context panel. On desktop this is the page that most loudly says "this is a stretched phone".

The AI is grounding its responses in the user's data, but the user has no way to see what data is in scope. This is opaque and undermines trust in a recovery context.

Duplicate user messages appear to send through without warning. Either it is a bug or the interaction model is too forgiving.

History List (/history)

Layout. Two-column grid of check-in cards. Each card shows date, time, time-of-day pill, mood and craving numbers, a colored dot, and a truncated summary. Selecting a card requires a full page navigation to the detail view.

Navigation. Top tabs only. "Log missed" sits in the top-right as a secondary action, which is the correct place for it.

Information hierarchy. Cards are evenly weighted. There is no grouping by date (four check-ins on May 9 are four separate cards), no filtering, no search, no preview pane, and no sense of timeline.

Visual design. Cards are clean. Mood/craving with the colored dot is readable. High-risk and low-risk entries do not differ enough at a glance.

Desktop patterns missing. Master-detail (list on the left, preview on the right). Filters (date range, risk level, time-of-day, mood band). Search (free-text in notes). Grouping by date. Sticky date headers on scroll. A timeline or calendar view toggle.

Three most damaging problems.

No master-detail. Every entry inspection requires a full page navigation, then back, then forward to the next one. This is the wrong interaction model for a desktop log.

No grouping by date and no filtering. Past a few weeks of data this page becomes unscannable.

Risk and time-of-day are visually weak compared to their importance for scanning.

History Detail (/history/5)

Layout. Single-column reading view. The AI's structured summary (Where you were, Factor, Craving Risk, Moves, Support, Reminder) is one tall card. The Raw Log (Mood, Energy, Craving, Sober Today, Notes) is a second tall card stacked below it, taking equal visual weight to the interpretation.

Navigation. Back link only. There is no prev/next between check-ins, no breadcrumb, no jump-to-day.

Information hierarchy. "Listen to full summary" is a giant full-width button that is doing about ten times its weight. The Edit button is small in the top-right. The MIDDAY pill has no function. The raw log competes with the interpreted summary instead of supporting it.

Visual design. Reading width is too wide for comfortable line length. The body text spans the full content area at 1280+ which produces 130-character lines.

Desktop patterns missing. A metadata rail separating interpretation (main read) from raw values (reference data). Prev/next navigation between check-ins. Sticky header with date and edit/delete. A small inline timeline strip showing this entry in context.

Three most damaging problems.

Interpreted insight and raw data are not structurally separated. The summary is the read, the numbers are the lookup, and they should not carry equal visual weight.

No prev/next between check-ins. Reviewing a streak of entries is currently a back-and-tap loop.

"Listen to full summary" is a huge overweight CTA that crowds the actual reading content.

Trackers (/trackers)

Layout. Two-column grid with three cards (Nicotine, Weed, Alcohol). Each card is a horizontal pill showing name and time elapsed. About 70 percent of the page is empty black.

Navigation. Top tabs and an "+ Add" button in the top-right.

Information hierarchy. All three trackers are equally weighted. There is no current vs. longest, no relapse history, no progress indicator.

Visual design. The colored left borders are good, but the cards carry a single line of data and no visual texture.

Desktop patterns missing. Each card should expand to show streak history, total resets, longest run, and a sparkline. Click-through to a tracker detail view. Aggregate view (combined sober time, total trackers active).

Three most damaging problems.

The page shows three lines of data on a desktop screen. This is the worst data density on the entire product.

No drill-in. Tracker cards do nothing on click.

No history or context. A user cannot see when they last reset, how many resets, or how this streak compares to past ones.

Insights (/insights)

Layout. Long single-column scroll. KPI tiles in a 4+3 row, then commitments empty state, then time range toggle, then mood and craving empty state cards, then a giant calendar with a single green cell, then sleep/energy/focus empty states, then a recovery habits list with mostly 0%, then a sobriety trackers section.

Navigation. Top tabs and an "Export my data" button in the top-right.

Information hierarchy. All seven KPI tiles are equal weight. There is no hero metric. The empty states are scattered through the page rather than consolidated.

Visual design. The calendar is enormous and shows one green day. The recovery habits list with 0% progress bars makes the user feel worse than no data would.

Desktop patterns missing. A real dashboard layout (hero metric, KPI row, two charts side-by-side, calendar/heatmap, drill-in). A contribution-graph style heatmap instead of a single-month calendar. Time range as a sticky control. Better empty states.

Three most damaging problems.

With low data, the page shows a graveyard of "Not enough data yet" cards. Empty states should consolidate into a single "log more days to see trends" prompt.

The KPI row is undifferentiated. "Total logged" and "7-day avg mood" are not equally important and should not look identical.

The calendar takes up roughly a third of the page to show one cell of data. A heatmap covering 90 days at the same total area would be far more useful.

Settings (/settings)

Layout. Single column scroll. Theme picker as a 3x2 grid of cards is visually loud at the top. Memory and Export are buried as text links. Toggles and dropdowns sit in stacked rows. Email and Reminders section repeats data already shown in Memory (timezone, reminder time).

Navigation. Back link only. There is no settings sidebar grouping (Appearance / Memory / Email / Account).

Information hierarchy. The theme picker dominates the page but is the least frequently changed setting. "Save" only saves the email block, not the toggles, which is confusing scope.

Visual design. Theme cards are fine. The red icon on the email field reads as an error but has no explanation. Toggles look standard.

Desktop patterns missing. A settings sidebar (Appearance, Memory, Email, Account, Data, Danger zone). Inline saves on toggles instead of a single Save button. A clear "what gets saved when I press Save" scope.

Three most damaging problems.

No sidebar nav. Settings on desktop almost always uses a left rail of categories and a right pane of fields. Anchor uses a flat scroll that mixes categories.

Memory is a text link buried mid-page. Memory is one of Anchor's most distinctive surfaces and deserves a prominent entry point, not a tertiary link.

The Save button has unclear scope. The user cannot tell if pressing Save persists everything on the page or only the email block above it.

Memory (/memory)

Layout. Long single-column scroll. Profile fields (10 of them) stacked vertically, each in its own card with an edit pencil. Recent Patterns as one big card with three sub-sections. Event Log as a stack of timestamped entries with delete buttons. Controls at the bottom with a destructive reset.

Navigation. Back link only. No way to jump to sections.

Information hierarchy. Every profile field is equal weight. Recovery focus, sober contacts, and meeting links are higher signal than email and timezone (which duplicate Settings) but they all look identical. The destructive reset is at the bottom of a long scroll where it could be missed or accidentally triggered.

Visual design. Edit pencils on every field are visually noisy. The patterns card with three labeled paragraphs is one of the cleaner moments on the page. The event log entries are dense and compact, but the page reads like a raw database admin view.

Desktop patterns missing. A multi-panel layout: profile categories on the left, field editing in the center, AI patterns and event log on the right. Inline editing instead of an edit pencil that opens a modal. A clearer separation between profile (your inputs) and memory (AI's outputs).

Three most damaging problems.

The page conflates "your profile" (inputs you set) and "what Anchor remembers" (AI's derived patterns and event log) in one scroll. These are two different mental models and should be visually separated.

Email, reminder time, and timezone are duplicated from Settings with no indication of source of truth. A user who edits one will not know if it propagates to the other.

The destructive reset is at the bottom of a long scroll with a confirmation textbox. The placement is fine but the entire Controls section deserves to be visually walled off, not just labeled.

3. Desktop Design Framework

Shell and Navigation

Replace the top tab bar with a hybrid shell: persistent left sidebar plus a slim top bar.

Left sidebar (240px wide, persistent at 1280+, collapsible to 64px icon-only at 1024 to 1280). Contents top to bottom: Anchor wordmark, daily streak summary (e.g., "Day 26 weed, 22 alcohol, 9 nicotine"), primary nav (Home, Check In, Chat, History, Trackers, Insights), secondary nav (Memory, Settings), user identity at the bottom (avatar, email, sign out menu).

Top bar (48px tall, persistent). Page title on the left, contextual actions on the right (e.g., on History the "Log missed" button; on Insights the "Export data" button; on Memory the "Pause memory" toggle).

Breakpoints.

1024 to 1279: sidebar collapses to 64px icon rail. Main content gets full remaining width.

1280 to 1439: sidebar expands to 240px. Main content gets remaining width up to a 1200 max content width.

1440 to 1599: sidebar 240px. Main content uses up to 1280 with optional right rail panel on pages that benefit (Home, History list, History detail, Check-In, Chat, Memory).

1600+: sidebar 240px, main content max 1280, right rail 320px. Total content frame caps at roughly 1840 with the rest as breathing room.

The shell stays consistent across every page. What changes per page is the body region (single column, master-detail, three column, dashboard grid, form plus rail).

Layout System

Adopt a 12-column grid in the main content region with a 24px gutter and 32px outer padding. Use the grid for actual structure, not as decoration.

Content width caps by page type.

Reading content (history detail main column, memory text fields, settings prose): 720px max line length to keep typography comfortable.

Forms (check-in, settings forms): 720 to 820px form column with a 320 to 360px summary rail beside it.

Dense data (insights, history list, trackers): up to 1280px with multi-column layouts.

Chat: messages column maxes at 720px, with sidebar and right rail filling the remainder.

When to use cards. Cards should earn placement. A card is justified when it groups related fields that share an action (a form section), when it represents a discrete entity (a check-in, a tracker, a session), or when it isolates a destructive action. A card is not justified for a single-line readout, a section header, or a list of toggles. The current product uses cards as the default container for everything, which flattens hierarchy. Replace many of the current cards with section headers, dividers (subtle background shifts, not horizontal rule lines), and inline controls. For dense data such as raw logs and event logs, prefer rows or tables over cards.

Visual Direction

Dark theme refinement. Keep the current Anchor Dark palette as the default. Introduce one additional surface tier so there are three: page background (deepest), section/grouped surface (one notch lighter), interactive surface (cards, inputs, buttons, slightly lighter still). Today the product mostly uses two tiers and the difference between them is subtle. Three tiers gives the eye somewhere to rest and lets cards actually function as cards.

Typography scale (desktop).

Display (page title): 32px/40, semibold.

H2 (section): 20px/28, semibold.

H3 (subsection): 16px/24, semibold.

Body: 15px/24, regular.

Body small (metadata): 13px/20, regular.

Label/caption: 12px/16, medium. Use sentence case as the default. Reserve uppercase for short, structural labels (KPI tile labels, danger zone). The current "WHERE YOU WERE / FACTOR / CRAVING RISK / MOVES / SUPPORT / REMINDER" all-caps treatment is overused and makes the AI summary look like form metadata instead of prose.

Data (numeric, in tiles): 28px/32, semibold, tabular-nums.

Switch all numeric displays to tabular-nums so streak counters, time elapsed, and KPI tiles stop wobbling on update.

Color use.

Green: primary action, positive state, sobriety affirmative.

Yellow: moderate state.

Red: high risk, destructive, error. Currently only used for destructive; expand carefully to craving risk badges.

Tracker accent colors (blue for weed, pink for alcohol, teal/green for nicotine): keep as left-border accent only. Do not let them bleed into other UI.

Eliminate any decorative use of color. Color is a signal, not an aesthetic choice.

Interactive affordance. Buttons need three clear states (rest, hover, active) and primary vs secondary should be unmistakable at a glance. Today the primary green CTAs and the secondary outline buttons read at similar visual weight; tighten the gap.

4. Per-Page Redesign Brief

Home (/app)

Recommended layout. Three-zone dashboard inside the persistent shell.

Left rail (in the persistent sidebar, no change to page).

Main content (8 of 12 columns at 1280, full width below sidebar): page header "Today" with date, then a "Latest check-in" hero card spanning the full main area showing mood, craving, energy, focus as a 4-up stat strip with sparkline trends, then a "Next move" card with the primary CTA (Check in again or Start today's check-in depending on state), then a "This week" glance row.

Right rail (4 of 12 columns at 1280+, hidden below 1280): tracker cluster showing all three trackers as compact cards with sparkline and last-reset, then a small calendar peek (this month, contribution-style colored cells), then a "Talk to your coach" prompt with a suggested context-aware question.

What moves. Trackers move from the top row of the body into the right rail. Settings cog moves into the persistent sidebar identity area. Memory gets a sidebar entry.

What gets promoted. The next action (check-in) becomes a single visually dominant CTA. The latest check-in becomes a richer summary, not just a card with four labels.

What gets deprioritized. "4 total check-ins" footer moves to a tooltip on the "This week" row. The duplicate "Chat with my coach" CTA on the latest check-in card disappears in favor of the right-rail coach prompt.

Single most important structural change. Adopt the persistent left sidebar shell so the home page can use its main content area for actual hero content instead of trying to be its own nav.

New components. Stat strip with sparkline (reusable on Insights). Tracker compact card (reusable on Trackers and right rails). Coach prompt card with suggested-question state.

Check-In (/checkin)

Recommended layout. Two-column form with a sticky right summary rail that previews the AI's read in real time.

Top bar (in shell): page title "Check-in / Midday", "Discard" link.

Main content split:

Left column (8 of 12 cols, max 820px): the form itself, grouped into four labeled sections.

Section "Vitals" (4 sliders): Mood and Energy in a sub-pair, Craving and Focus in a sub-pair. Two sliders per row.

Section "Behaviors" (yes/no row): Sober today, Meeting today, Contacted sober person, Called a fellow, Exercised today, Ate enough today. Render as a single horizontal row of 6 toggle cells, not 6 separate cards.

Section "Sleep" (single full-width slider).

Section "Feelings" (trigger pill cloud, full width within the form column).

Section "Reflection" (Grateful for, Notes, side by side at 6 cols each within the form column).

Right rail (4 of 12 cols, sticky): the "live read" panel.

Check-in type pill (Morning / Midday / Evening, auto-selected by time, editable).

Completion progress (sections complete, fields filled).

Selected triggers, summarized.

Live craving risk preview, recomputed as Mood/Craving/Behaviors change. Color-coded (green/yellow/red).

Sticky primary "Check In" submit button at the bottom of the rail.

What moves. Submit moves from the bottom of the page into the sticky right rail. The "Midday check-in" pill moves into the rail's check-in type selector. Section structure becomes visible.

What gets promoted. Section headers. The live risk preview, which makes the AI's interpretation visible to the user as they fill the form. This is a real desktop interaction win for a recovery context.

What gets deprioritized. The yes/no behaviors compress from six separate cards into one horizontal toggle row.

Single most important structural change. Add the sticky right rail with live risk preview. The form stops being a survey and becomes a conversation with the AI in progress.

New components. Sticky form rail with live risk preview. Behaviors row (6-cell horizontal toggle group). Section header component (reusable across forms).

Keyboard shortcuts to add. Number keys 1 to 10 for the focused slider. Y and N for the focused toggle. Tab/Shift-Tab to move between fields. Cmd/Ctrl+Enter to submit. Esc to focus the discard link.

Chat (/chat)

Recommended layout. Three-pane chat application inside the shell.

Left pane (left rail of main content, 280px): session list showing past chat sessions grouped by date, with a "New session" button at the top. Each session shows a one-line preview, date, and a small mood/risk indicator if grounded in a check-in.

Center pane (flex, max 720 message column inside): messages with timestamps, audio playback on AI bubbles, copy/regenerate/thumbs on hover for AI bubbles. Input pinned to bottom.

Right pane (320px, collapsible): "Today's context" panel showing the user's most recent check-in data (mood, craving, triggers, sober today). This is what the AI is grounding its responses in. Below that, a "Suggested prompts" list based on recent state.

What moves. The "+" icon for new session moves into the session list left pane as a labeled "New session" button.

What gets promoted. Session history becomes a first-class surface. The grounding context becomes visible to the user.

What gets deprioritized. The current "Chat" page header becomes the page title in the top bar of the shell.

Single most important structural change. Split the page into three panes. This single change is what makes Chat stop looking like a stretched mobile screen.

Bug to fix during this work. Duplicate user message submission ("I just completed a check-in and want to talk through it" appearing twice in a row) needs either client-side debouncing or a server-side dedupe on identical consecutive sends.

New components. Session list item (with mood/risk indicator). Today's context panel. Suggested prompt chip.

History List (/history)

Recommended layout. Master-detail.

Top bar: page title "History", "Log missed" button right-aligned.

Filter bar across the top of main content: date range picker, risk level multi-select, time-of-day multi-select, search input, sort dropdown.

Body split:

Left pane (5 of 12 cols, max 480px): chronological list of check-ins, grouped by date with sticky date headers on scroll. Each row shows time, time-of-day pill, mood/craving numbers, and a colored risk dot. Compact rows, not cards.

Right pane (7 of 12 cols): preview of the selected check-in. Shows the structured summary (Where you were, Factor, Craving Risk, Moves, Support, Reminder) and a link/button "Open full detail" that routes to /history/[id].

What moves. Card grid becomes a list-and-preview pattern. "Log missed" stays in the top bar.

What gets promoted. Date grouping. Risk visualization. The preview pane removes one click from every entry inspection.

What gets deprioritized. Truncated summaries with ellipsis disappear in favor of the full preview in the right pane.

Single most important structural change. Master-detail. The list becomes a scanning surface, the right pane becomes a reading surface, and full detail is one click away when needed.

New components. Filter bar (reusable on Insights). Sticky date header. Compact check-in list row. Preview pane.

History Detail (/history/5)

Recommended layout. Reading view with a metadata rail. Use this layout when the user navigates from list to full detail (rather than just using the preview pane).

Sticky top bar inside main content: prev arrow, date and time, time-of-day pill, next arrow, Edit button, Delete in an overflow menu, small "Listen to summary" icon button.

Body in a 12-col grid:

Main column (8 cols, max 720 reading width): the AI structured summary as readable prose. "Where you were" leads, then "Factor", "Moves", "Support", "Reminder". This is the read.

Right rail (4 cols): metadata. Mood, Energy, Craving as compact stat cells. Sober today, Hours slept. Selected triggers as inline pills. Date, time, check-in type. This is the lookup.

Below both columns, full width: collapsible "Raw log" section showing all field values verbatim. Default collapsed; expand for forensic detail.

What moves. Raw log moves from a competing equal-weight card into a secondary collapsible section. Mood/Craving/Sleep numbers move into the rail as quick-reference, leaving the main column free for the summary as prose. "Listen to summary" shrinks from a full-width megabutton to an icon button in the sticky header.

What gets promoted. The interpretation, in comfortable reading width. Prev/next navigation between entries.

What gets deprioritized. The MIDDAY pill becomes part of the title row in the sticky header. The raw log becomes available on demand rather than always-visible.

Single most important structural change. Separate interpreted insight from raw data. The summary is the read; the numbers are reference. They should not carry equal visual weight.

New components. Sticky entry header with prev/next. Metadata rail (compact stat cells, plus quick info). Collapsible raw log panel.

Trackers (/trackers)

Recommended layout. 3-up dashboard grid where each tracker becomes a richer card.

Grid: 3 columns at 1280+ (one card per tracker), 2 columns at 1024 to 1280, 1 column below.

Each tracker card shows: colored top border (not just left), tracker name, current streak (large numeric), longest streak, total resets, last reset date, a 30-day sparkline of streak history (or commitment density), and a "Log relapse" button as a secondary action plus a "View detail" link.

What moves. "+ Add" stays in the top bar.

What gets promoted. Each tracker carries real data instead of one line.

What gets deprioritized. The empty space below the cards (filled by richer cards).

Single most important structural change. Each tracker card carries a sparkline and historical context, not just elapsed time.

New components. Tracker detail card with sparkline. (This is the same card used in compact form on Home's right rail.)

Insights (/insights)

Recommended layout. True dashboard with hero, KPIs, charts, heatmap, and habits.

Top bar: page title, time range toggle (7d / 30d / 90d / All), Export.

Hero row (full width): a single primary metric card. Candidate: combined sober streak (e.g., "57 sober-days across 3 trackers this month") with a small trend indicator. Pick one hero number and commit to it.

KPI strip (4-up at 1280+, 2 rows of 4 at 1024): the existing tiles, but visually flatter (no heavy card chrome) and with consistent label/data ratios.

Two charts side-by-side (6 cols each): Mood line chart, Craving line chart. With low data, show a single consolidated empty state across both, not two side-by-side empty cards.

Calendar heatmap (full width): contribution-graph style, 90 days at a glance, color-coded by risk. This replaces the current giant single-month calendar.

Recovery habits (full width): horizontal bar chart with one bar per habit, 0 to 100% over the time range.

Sobriety trackers (full width): a compact mirror of the Trackers page, useful here for cross-reference.

What moves. The single-month calendar gets replaced by a 90-day heatmap.

What gets promoted. A hero metric. Time range as a sticky persistent control.

What gets deprioritized. The seven equal-weight KPI tiles become a compact KPI strip below the hero.

Single most important structural change. Pick a hero metric and make it visually dominant. Insights without a hero is just a stat pile.

New components. Hero metric card. Compact KPI tile. Heatmap component (90-day contribution graph).

Settings (/settings)

Recommended layout. Two-column settings with a left nav rail of categories.

Left settings nav (200px inside main content): Appearance, Memory, Email and Reminders, Account, Data, Danger zone.

Right pane: section content. Inline saves on toggles and dropdowns (no global Save button). The Email section keeps an explicit Save because email is multi-field, but the rest are immediate.

What moves. Memory becomes a top-level settings category and also a sidebar destination in the global shell. The theme picker shrinks to a horizontal row, not a 3x2 card grid that dominates the page.

What gets promoted. Account section (currently invisible). Data section (export, reset).

What gets deprioritized. The theme picker no longer leads the page.

Single most important structural change. Add the settings nav rail and use inline saves. The current single-Save-button-with-unclear-scope problem disappears.

Bug to fix during this work. The red icon next to the email field has no tooltip or explanation. Either explain what it means or remove it.

Source-of-truth call. Email, reminder time, and timezone live here in Settings only. Memory page no longer holds these fields. (See Memory redesign below.)

New components. Settings nav rail. Inline-save toggle row.

Memory (/memory)

Recommended layout. Profile inspector with three zones, plus a separated danger zone.

Top bar: page title "Memory", "Pause memory" toggle right-aligned.

Main content in a 12-col grid:

Left (3 of 12 cols): profile category nav. Categories: Recovery focus, Program and support, Sober contacts, Meeting links, Why I'm doing this. Vertical list, clickable to scroll or focus the corresponding panel.

Center (5 of 12 cols): selected profile fields, inline-editable. No edit pencils. Fields appear as labeled text with an edit affordance on hover. Each category renders its fields here.

Right (4 of 12 cols): "What Anchor has noticed". The current Recent Patterns block (Top triggers, Mood trend, Pattern to notice). Plus a brief "summary of you" paragraph at the top. Below patterns, a compact event log showing the last 10 entries with "View all" link to expand.

Below the three columns, full-width: a clearly visually walled Danger zone containing "Reset all memory" with the confirmation textbox.

What moves. Email, reminder time, and timezone leave Memory and live only in Settings (single source of truth). The Pause memory toggle moves to the top bar. Edit pencils disappear in favor of inline editing.

What gets promoted. AI patterns become a parallel right-column panel rather than a section buried below profile fields. The mental model split between "your inputs" (left and center) and "AI's outputs" (right) becomes the page's organizing principle.

What gets deprioritized. The full event log becomes a "View all" expansion rather than always-visible. Edit pencils are gone.

Single most important structural change. Separate profile (your inputs) from memory (AI's outputs) into parallel zones. Make the page feel like a profile inspector, not a database admin view.

New components. Profile category nav. Inline-editable profile field. Patterns panel. Compact event log with "View all" expansion. Danger zone wrapper.

5. Priority Order

Sequence the redesign by impact, with shell paired to the highest-frequency surface because every page depends on the shell.

Block 1: Shell + Check-In. Ship together. The shell (sidebar plus top bar, breakpoint behavior, settings/memory entries in the sidebar) is foundational and every other page assumes it exists. Check-In is the daily ritual and the highest-frequency interaction in the product. Pairing them means the first user-visible release establishes both the new app frame and the most-used flow with its sticky risk-preview rail. This is the work block that makes Anchor feel like a desktop product.

Block 2: Home. Depends on the shell. Sets the first impression after login. With the shell already in place, Home becomes a real dashboard rather than a centered content stack. Highest visibility per unit of engineering work.

Block 3: Chat. Most damaging visual problem in the product today. The three-pane redesign with session list and grounding-context panel is the change that makes the AI feel like it knows you. Also the page where fixing the duplicate-message bug lands.

Block 4: History list and detail (paired). Now structurally coupled because the list uses master-detail with a preview pane and the detail page is the "open full" target. Ship them together. Master-detail plus the metadata-rail reading view are the two changes that turn History from a log into a recovery archive.

Block 5: Insights. Becomes the killer page once data fills in. Worth landing the dashboard structure now even with low data, because the structure itself shapes how users perceive whether the product is "working".

Block 6: Memory. Highest-stakes feature in the product (AI behavior is shaped by it) and currently the most underbuilt surface. The profile inspector redesign makes the model visible and changes how users trust the AI.

Block 7: Settings. Meta surface. Sidebar pattern fixes it structurally. Lower frequency, lower stakes. Worth doing after Memory because Memory and Settings will share the inline-save and field-editing patterns. Also where the email/timezone source-of-truth consolidation lands.

Block 8: Trackers. Smallest surface, smallest payoff, easiest change. The richer-card design with sparkline is mostly a single component build. Can ship as cleanup work alongside any other block when an engineer has slack.

A pragmatic order-of-operations note. Block 1 (shell + check-in) is the only hard dependency. After that, blocks 2 through 8 can ship in any order based on engineering bandwidth. The recommended order above is by user-facing impact per block, not by dependency.

6. Addendum: Two Pages Missing from Original Audit

Addendum date: May 9, 2026 Surfaces: Check-in detail (/checkin/complete) and Tracker detail (/trackers/[id]) These surfaces fold into existing implementation blocks. Priority order in section 5 is unchanged.

Check-in Detail (/checkin/complete) — Per-Page Audit

Layout. Single-column stack. Page header "Check-in Complete / Here's your reflection." Then a giant full-width "Listen to full summary" button. Then one tall card containing the AI's reflection (Where you're at, Something to watch, Craving risk, Next moves, Support, Remember, From your sponsor). Then a disabled "Chat with my coach" CTA. Then a "Check in again" CTA at the bottom.

Navigation. No breadcrumb, no back button, no done button. The user is in a transitional state (just completed a check-in) but the page does not give them a clear way out except by tapping a nav tab.

Information hierarchy. The reflection itself is the value, but it competes with the giant "Listen to full summary" button at the top and two competing CTAs at the bottom. The "Chat with my coach" CTA is disabled, which is the single most confusing element on the page. The "Check in again" CTA implies the primary next action is to log another check-in, which is rarely true immediately after submitting one.

Visual design. Same issues as History detail: full-content-width prose at uncomfortable line lengths, all-caps section labels that read as form metadata rather than reflective writing, equal-weight container card.

Desktop patterns missing. Metadata rail showing the values the user just submitted (mood, energy, craving, focus, behaviors, triggers). An active coach hand-off CTA with grounding context already loaded. A clear "done" affordance to return to home. Comparison context (how this check-in compares to the last few).

Three most damaging problems.

"Chat with my coach" is disabled at the precise moment a user would benefit most from talking the reflection through. This is either a wiring bug (chat not ready post-submit) or a UX choice that must be reversed.

"Check in again" as the primary bottom CTA implies the right next action is another check-in immediately. The right defaults are "back to home" or "talk to coach", not another submission.

The user has no quick reference of what they actually submitted. They answered 30+ questions and the only acknowledgment is the AI's prose interpretation, making it hard to verify the AI's read.

Tracker Detail (/trackers/[id]) — Per-Page Audit

Layout. Single tracker card with name, colored left border, and a real-time elapsed counter ticking in seconds. Then a 3-up row of Edit / Reset / Archive buttons. Then Delete Tracker below in red. About 80 percent of the page is empty.

Navigation. Back link only. No way to navigate to neighboring trackers, no breadcrumb, no relationship to the trackers list.

Information hierarchy. The elapsed time is the hero, which is correct. Everything else is buttons. No current/longest comparison, no past streaks, no relapse log, no notes. This is functionally a slightly-larger version of the list card.

Visual design. Real-time second counting is a design decision that has not been made deliberately. Some users in recovery find ticking seconds grounding; others find it anxiety-producing. The colored left border is consistent with the list view.

Desktop patterns missing. Streak history chart. Relapse log with dates. Stats strip (longest streak, total resets, average streak length). Prev/next tracker navigation. A destructive-action zone that separates Edit (safe) from Reset / Archive / Delete (varying degrees of destructive).

Three most damaging problems.

The page is structurally empty. A tracker drill-in should show history and context, but this view shows almost nothing beyond the list card.

Edit, Reset, Archive, and Delete sit as four equal-weight actions, but they have three different severities: safe (Edit), streak-destructive (Reset), hide (Archive), permanent (Delete).

Real-time second counting has not been deliberately decided. Default behavior should probably be days and hours visible, seconds available on hover or as a user preference.

Check-in Detail (/checkin/complete) — Redesign Brief

Recommended layout. Reading view with metadata rail. Same structural pattern as History detail, tuned for the post-submission moment.

Sticky top bar inside main content: "Check-in complete" title, a "Done" button on the left (returns to home), and a small "Listen to summary" icon button on the right.

Body in a 12-col grid:

Main column (8 cols, max 720 reading width): AI reflection as readable prose. "Where you're at" leads, then "Something to watch", "Next moves", "Support", "Remember", "From your sponsor". This is the read. Section labels convert from all-caps to sentence case.

Right rail (4 cols, sticky): the values the user just submitted. Mood, Energy, Craving, Focus as compact stat cells. Sober today, Hours slept. Selected triggers as inline pills. Time of day pill. This is acknowledgment that the AI saw what they put in.

Below both columns, full-width action band:

Primary CTA: "Talk through this with my coach" (active, not disabled, with a small chip showing "Today's reflection" as the grounding context the chat will inherit).

Secondary CTA: "Back to home".

Tertiary text link: "Or check in again" for the unusual case of multiple check-ins per session.

What moves. "Listen to full summary" shrinks from a full-width megabutton to an icon button in the sticky top bar. "Chat with my coach" becomes the primary action and is enabled. "Check in again" demotes to a tertiary text link.

What gets promoted. The coach hand-off. The user's submitted values in the right rail.

What gets deprioritized. The listen megabutton. The check-in-again CTA as primary.

Single most important structural change. Enable the coach CTA and add the metadata rail. The post-submission moment is when AI engagement matters most and when showing the user their own data builds trust in the AI's interpretation.

Bug to fix during this work. Investigate and fix the disabled "Chat with my coach" state. If it is a race condition (chat session not ready before redirect), fix the readiness check. If it is intentional product logic, reverse it.

Implementation block. Ships with Block 1.B (check-in redesign).

New components. Reuses History detail components (sticky entry header, metadata rail, prose reading column). Adds a "Sponsor message" subcomponent unique to fresh check-ins. Adds a coach hand-off action chip.

Tracker Detail (/trackers/[id]) — Redesign Brief

Recommended layout. Detail view with hero, stats strip, history zone, and separated action zone.

Top bar: tracker name (left), prev/next tracker navigation (right).

Hero zone (full width): tracker name with colored top border (not just left), elapsed time as hero number, "Since [date] at [time]" timestamp below.

Stats strip (4-up row, full width below hero): longest streak, total resets, average streak length, total attempts.

Main content split (12-col grid):

Left (8 cols): streak history chart. One bar per past streak attempt, duration as the y-axis, current streak highlighted in the tracker's accent color. Hover for date range and reset reason if available.

Right (4 cols): reset log. Compact list of past resets with date, streak duration for that run, and any note if captured. Most recent at top.

Below both columns, action zone with three clearly separated regions:

Safe actions: Edit (rename, change color, change start date).

Reset zone (neutral styling): "Mark a relapse" with an optional note field for what happened.

Destructive zone (walled off with danger token): Archive (with label "Stop tracking, keep history") and Delete (with label "Remove permanently, including history"). Two separate buttons, not one.

What moves. Edit / Reset / Archive / Delete reorganize from a flat row into three labeled zones. The elapsed time gains context from the history chart and stats strip.

What gets promoted. Historical context (chart, reset log). Action severity clarity.

What gets deprioritized. The flat four-button row.

Single most important structural change. Add the streak history chart and reset log. A tracker drill-in without history is just a bigger version of the list card.

UX call required before implementation. Real-time second counting: default to days and hours only, with seconds available on hover or as a user preference. Confirm this direction before CC implements.

Implementation block. Ships with Block 8 (Trackers redesign).

New components. Streak history chart (bar chart, one bar per streak). Reset log row. Tracker stats strip. Three-zone action region. Prev/next tracker navigation.

Prompt

You are implementing the desktop redesign of Anchor (sobrietyanchor.com).

FIRST ACTION before any code work. Create the file docs/desktop-audit.md and save the audit content (everything below the BEGIN AUDIT CONTENT delimiter) to it verbatim. Commit as "docs: add desktop redesign audit". This file is the source of truth for the redesign and you will reference it across this session and future sessions.

After the audit is committed, your scope for this session is Block 1.A only: build the new desktop shell.

Out of scope for this session. Any per-page redesign. The check-in form, history pages, insights, settings, memory, trackers, chat, and home all stay structurally untouched. They render inside the new shell with their existing layout. Block 1.B (check-in redesign) and beyond are future sessions.

Specifically, deliver:

1. A persistent left sidebar component matching section 3 of the brief. 240px wide at 1280+, collapses to a 64px icon-only rail at 1024 to 1279. Contents top to bottom: Anchor wordmark, daily streak summary, primary nav (Home, Check In, Chat, History, Trackers, Insights), secondary nav (Memory, Settings), user identity at the bottom (avatar, email, sign out menu).

2. A persistent top bar component. 48px tall. Page title on the left, contextual actions slot on the right (per-page actions like "Log missed" on History or "Export data" on Insights are wired up later; for this session the slot exists and is empty).

3. An app shell layout wrapper that applies sidebar plus top bar to every authenticated route.

4. Replace the existing top-tab nav on every page with the new shell.

5. Mobile behavior preserved. Below 1024, the shell collapses to the existing mobile layout. Do not break mobile.

6. The settings cog on Home and the back-link nav on Settings, Memory, and history detail are no longer needed for primary nav since the sidebar handles it. Keep page-level back links where they aid in-page navigation; remove ones that are redundant with sidebar nav.

Work loop. Follow this in order, do not skip steps.

1. Save and commit docs/desktop-audit.md (content below the delimiter, verbatim).

2. Read docs/desktop-audit.md in full. Confirm in your reply that you understand the shell spec in section 3 and the breakpoint behavior. Quote the breakpoint rules back to me.

3. Survey the existing codebase. Find the current top-tab nav component, the current layout wrapper, the routing structure, the design token system, and the existing styling approach (Tailwind, CSS modules, styled-components, etc.). Report what you find before writing code.

4. Propose an implementation plan as a numbered list of file changes (new files, modified files, deleted files). Wait for my approval before executing. Do not start coding until I say go.

5. Execute the approved plan. Commit in logical chunks: sidebar component, top bar component, layout wrapper, route integration, top-tab removal. One concern per commit.

6. Verify. Load every authenticated route at 1024, 1280, 1440, and 1600 viewport widths. Confirm the shell renders, nav works, and page content is unchanged. Run the Playwright smoke suite (111 tests, per V3 baseline). Report pass/fail.

Constraints.

- Do not add features. Do not redesign individual pages. Do not change the dark theme. Do not touch the check-in form, history pages, or any per-page surface beyond replacing the nav.

- If anything in the brief is ambiguous for this scope, ask me before deciding. Do not interpret unilaterally.

- Use the existing design tokens and styling system. Do not introduce new dependencies without asking.

- No em dashes in any user-facing copy you write (in nav labels, alt text, etc.). Use periods, commas, or restructure.

Definition of done.

- docs/desktop-audit.md committed as its own commit.

- Every authenticated route renders inside the new shell at 1024, 1280, 1440, 1600.

- Old top-tab nav is removed from the codebase.

- Mobile layout below 1024 is unchanged from current behavior.

- Memory and Settings are reachable from the sidebar (no longer behind the cog).

- All 111 Playwright smoke tests pass.

- A summary commit message or PR description listing what changed.

================ BEGIN AUDIT CONTENT ================

# Anchor Desktop Design Audit and Redesign Brief

Audit date: May 9, 2026

Audit scope: 9 desktop pages at 1280px+

Output target: engineering handoff (CC, Codex, or human implementer)

Version: merged from internal audit and external review

## 1. Overall Diagnosis

Anchor's desktop layout is a mobile app put on a treadmill. The viewport widened, but nothing about the information architecture, component density, or interaction model changed to take advantage of it. Every page is a single, narrow column scrolling vertically through stacked cards. On a 1280+ display, the body content typically occupies 40 to 60 percent of the horizontal canvas and the rest is matte black. This is the dominant problem and it leaks into everything else.

The second problem is that the dark theme is competent but the card system is undisciplined. Almost every piece of content is wrapped in a rounded rectangle with the same elevation, the same border radius, the same internal padding. There is no visual hierarchy between a primary CTA, a passive readout, a section header, and an empty state. The eye has nowhere to land. This is what makes the product feel "wellness startup-ish" rather than "thoughtful digital sponsor". The fix is not more visual flair, it is fewer cards and clearer hierarchy.

The third problem is that desktop affordances Anchor would actually benefit from, master-detail views, persistent context panels, metadata rails, keyboard navigation, multi-column data display, are entirely absent. The Chat page on a desktop screen with no session list, no grounding context panel, and a narrow center column of bubbles is the clearest example. The History detail page with the AI summary stacked above the raw log instead of beside it is another. The History list page with no preview pane is a third. These are not polish issues. They are the difference between a desktop app and a stretched phone screenshot.

## 2. Per-Page Audit

### Home (/app)

**Layout.** The page uses maybe 35 percent of vertical canvas before the fold and the rest is empty. Three tracker cards sit in a row but each one is a giant horizontal block carrying very little data. The "Latest check-in" card is oversized for the four data points it holds. The two CTAs (Check in again, Chat with my coach) stack full-width when they should be a primary/secondary pair.

**Navigation.** Top tabs are fine for desktop in principle, but Settings is hidden behind a cog icon in the top-right, and Memory is invisible from this page. The active state on tabs is a thin underline that works but is easy to miss.

**Information hierarchy.** The "ANCHOR / Saturday, May 9 / Today" stack is doing too much for what it conveys. Streaks are not the hero, the latest check-in is not the hero, the next action is not the hero. Nothing is the hero. The "4 total check-ins" footer is the kind of metadata that belongs in a tooltip, not on the home page.

**Visual design.** Tracker cards with colored left borders are the strongest design move on this screen. Everything else is the same dark gray rectangle. Typography is legible but undifferentiated.

**Desktop patterns missing.** Persistent sidebar nav. A "next action" panel. A right rail showing today's data context. Hover states on tracker cards to drill into a tracker. Quick keyboard shortcut to start a check-in (C).

**Three most damaging problems.**

1. No primary call to action visually dominates. Check-in is the daily ritual and it should be unmistakably the thing to do, not a button equal in weight to "chat with my coach".

2. The page does not function as a dashboard. It shows status but does not orient the user about what matters today (a craving spike yesterday, a missed meeting, a streak about to roll).

3. Settings and Memory are both reachable only from a cog icon, which is a discoverability failure for two of Anchor's most important surfaces.

### Check-In (/checkin)

**Layout.** A 30-plus question form rendered as a single column with mixed widths. Some questions are paired in two columns (Mood/Energy, Meeting/Sober person), others sit alone in a single column with an empty right side (Hours slept full-width, Ate enough today alone in left column). The form has no visible progress, no section grouping headers, no live preview of the AI's read on the data, and the submit button is at the very bottom of a long scroll.

**Navigation.** The "Midday check-in" pill near the top is the only sense of context. There is no way to skip sections, no way to jump to "feelings" if that is all you want to log, and no way to see how far through the form you are.

**Information hierarchy.** All sliders carry equal visual weight. The four numeric ratings, the seven yes/no behaviors, the trigger pills, and the two free-text fields are presented as if they are equally important. Mood and craving are the highest-signal data points and they should anchor the form, not blend in.

**Visual design.** Slider colors (green for high mood, yellow for mid focus, red implied for high craving) are working. Trigger pills are good. The yes/no toggles styled as paired cards are visually heavy for binary inputs.

**Desktop patterns missing.** A right summary rail that previews the AI's risk read in real time as the user fills the form. Keyboard shortcuts (1 to 10 for sliders, Y/N for binaries, Tab between fields, Cmd+Enter to submit). Section headers (Vitals, Behaviors, Feelings, Reflection). A two-column form layout that respects question grouping.

**Three most damaging problems.**

1. "Ate enough today?" sits alone in the left column with the right column empty. This is the visual fingerprint of a mobile form refusing to use the desktop grid.

2. The submit button is at the bottom of a long scroll. On desktop, a sticky action surface is table stakes.

3. There is no progress, section structure, or live feedback, so the form feels like a survey instead of a daily ritual where the AI is forming an interpretation alongside the user.

### Chat (/chat)

**Layout.** This is the worst offender for the mobile-stretched problem. A narrow center column of chat bubbles on a 1280+ canvas, with the AI bubbles full-width within that column and the user bubbles right-aligned green. The two side margins are empty black. There is no session history list, no context panel, no suggested prompts.

**Navigation.** Top tabs only. The "+" icon in the top-right presumably starts a new session but is unlabeled. There is no way to see past chat sessions or scope the current one.

**Information hierarchy.** The chat itself has clean turn structure with timestamps, but the AI's responses appear without any indication of what data they are grounded in. The user sent "I just completed a check-in and want to talk through it" twice in a row, which the screenshot suggests is either a UI bug or an interaction model that lets duplicates through silently.

**Visual design.** Bubbles look fine. The audio playback icons on AI responses are a nice touch. The "Say something" input is generic.

**Desktop patterns missing.** Session sidebar (most chat apps have this). Context panel showing today's check-in data so the user understands what the AI knows. Suggested prompts based on recent state ("ask about your craving spike yesterday"). Slash commands. Copy / regenerate / thumbs on AI messages.

**Three most damaging problems.**

1. The page is structurally identical to the mobile chat. There is no session list and no context panel. On desktop this is the page that most loudly says "this is a stretched phone".

2. The AI is grounding its responses in the user's data, but the user has no way to see what data is in scope. This is opaque and undermines trust in a recovery context.

3. Duplicate user messages appear to send through without warning. Either it is a bug or the interaction model is too forgiving.

### History List (/history)

**Layout.** Two-column grid of check-in cards. Each card shows date, time, time-of-day pill, mood and craving numbers, a colored dot, and a truncated summary. Selecting a card requires a full page navigation to the detail view.

**Navigation.** Top tabs only. "Log missed" sits in the top-right as a secondary action, which is the correct place for it.

**Information hierarchy.** Cards are evenly weighted. There is no grouping by date (four check-ins on May 9 are four separate cards), no filtering, no search, no preview pane, and no sense of timeline.

**Visual design.** Cards are clean. Mood/craving with the colored dot is readable. High-risk and low-risk entries do not differ enough at a glance.

**Desktop patterns missing.** Master-detail (list on the left, preview on the right). Filters (date range, risk level, time-of-day, mood band). Search (free-text in notes). Grouping by date. Sticky date headers on scroll. A timeline or calendar view toggle.

**Three most damaging problems.**

1. No master-detail. Every entry inspection requires a full page navigation, then back, then forward to the next one. This is the wrong interaction model for a desktop log.

2. No grouping by date and no filtering. Past a few weeks of data this page becomes unscannable.

3. Risk and time-of-day are visually weak compared to their importance for scanning.

### History Detail (/history/5)

**Layout.** Single-column reading view. The AI's structured summary (Where you were, Factor, Craving Risk, Moves, Support, Reminder) is one tall card. The Raw Log (Mood, Energy, Craving, Sober Today, Notes) is a second tall card stacked below it, taking equal visual weight to the interpretation.

**Navigation.** Back link only. There is no prev/next between check-ins, no breadcrumb, no jump-to-day.

**Information hierarchy.** "Listen to full summary" is a giant full-width button that is doing about ten times its weight. The Edit button is small in the top-right. The MIDDAY pill has no function. The raw log competes with the interpreted summary instead of supporting it.

**Visual design.** Reading width is too wide for comfortable line length. The body text spans the full content area at 1280+ which produces 130-character lines.

**Desktop patterns missing.** A metadata rail separating interpretation (main read) from raw values (reference data). Prev/next navigation between check-ins. Sticky header with date and edit/delete. A small inline timeline strip showing this entry in context.

**Three most damaging problems.**

1. Interpreted insight and raw data are not structurally separated. The summary is the read, the numbers are the lookup, and they should not carry equal visual weight.

2. No prev/next between check-ins. Reviewing a streak of entries is currently a back-and-tap loop.

3. "Listen to full summary" is a huge overweight CTA that crowds the actual reading content.

### Trackers (/trackers)

**Layout.** Two-column grid with three cards (Nicotine, Weed, Alcohol). Each card is a horizontal pill showing name and time elapsed. About 70 percent of the page is empty black.

**Navigation.** Top tabs and an "+ Add" button in the top-right.

**Information hierarchy.** All three trackers are equally weighted. There is no current vs. longest, no relapse history, no progress indicator.

**Visual design.** The colored left borders are good, but the cards carry a single line of data and no visual texture.

**Desktop patterns missing.** Each card should expand to show streak history, total resets, longest run, and a sparkline. Click-through to a tracker detail view. Aggregate view (combined sober time, total trackers active).

**Three most damaging problems.**

1. The page shows three lines of data on a desktop screen. This is the worst data density on the entire product.

2. No drill-in. Tracker cards do nothing on click.

3. No history or context. A user cannot see when they last reset, how many resets, or how this streak compares to past ones.

### Insights (/insights)

**Layout.** Long single-column scroll. KPI tiles in a 4+3 row, then commitments empty state, then time range toggle, then mood and craving empty state cards, then a giant calendar with a single green cell, then sleep/energy/focus empty states, then a recovery habits list with mostly 0%, then a sobriety trackers section.

**Navigation.** Top tabs and an "Export my data" button in the top-right.

**Information hierarchy.** All seven KPI tiles are equal weight. There is no hero metric. The empty states are scattered through the page rather than consolidated.

**Visual design.** The calendar is enormous and shows one green day. The recovery habits list with 0% progress bars makes the user feel worse than no data would.

**Desktop patterns missing.** A real dashboard layout (hero metric, KPI row, two charts side-by-side, calendar/heatmap, drill-in). A contribution-graph style heatmap instead of a single-month calendar. Time range as a sticky control. Better empty states.

**Three most damaging problems.**

1. With low data, the page shows a graveyard of "Not enough data yet" cards. Empty states should consolidate into a single "log more days to see trends" prompt.

2. The KPI row is undifferentiated. "Total logged" and "7-day avg mood" are not equally important and should not look identical.

3. The calendar takes up roughly a third of the page to show one cell of data. A heatmap covering 90 days at the same total area would be far more useful.

### Settings (/settings)

**Layout.** Single column scroll. Theme picker as a 3x2 grid of cards is visually loud at the top. Memory and Export are buried as text links. Toggles and dropdowns sit in stacked rows. Email and Reminders section repeats data already shown in Memory (timezone, reminder time).

**Navigation.** Back link only. There is no settings sidebar grouping (Appearance / Memory / Email / Account).

**Information hierarchy.** The theme picker dominates the page but is the least frequently changed setting. "Save" only saves the email block, not the toggles, which is confusing scope.

**Visual design.** Theme cards are fine. The red icon on the email field reads as an error but has no explanation. Toggles look standard.

**Desktop patterns missing.** A settings sidebar (Appearance, Memory, Email, Account, Data, Danger zone). Inline saves on toggles instead of a single Save button. A clear "what gets saved when I press Save" scope.

**Three most damaging problems.**

1. No sidebar nav. Settings on desktop almost always uses a left rail of categories and a right pane of fields. Anchor uses a flat scroll that mixes categories.

2. Memory is a text link buried mid-page. Memory is one of Anchor's most distinctive surfaces and deserves a prominent entry point, not a tertiary link.

3. The Save button has unclear scope. The user cannot tell if pressing Save persists everything on the page or only the email block above it.

### Memory (/memory)

**Layout.** Long single-column scroll. Profile fields (10 of them) stacked vertically, each in its own card with an edit pencil. Recent Patterns as one big card with three sub-sections. Event Log as a stack of timestamped entries with delete buttons. Controls at the bottom with a destructive reset.

**Navigation.** Back link only. No way to jump to sections.

**Information hierarchy.** Every profile field is equal weight. Recovery focus, sober contacts, and meeting links are higher signal than email and timezone (which duplicate Settings) but they all look identical. The destructive reset is at the bottom of a long scroll where it could be missed or accidentally triggered.

**Visual design.** Edit pencils on every field are visually noisy. The patterns card with three labeled paragraphs is one of the cleaner moments on the page. The event log entries are dense and compact, but the page reads like a raw database admin view.

**Desktop patterns missing.** A multi-panel layout: profile categories on the left, field editing in the center, AI patterns and event log on the right. Inline editing instead of an edit pencil that opens a modal. A clearer separation between profile (your inputs) and memory (AI's outputs).

**Three most damaging problems.**

1. The page conflates "your profile" (inputs you set) and "what Anchor remembers" (AI's derived patterns and event log) in one scroll. These are two different mental models and should be visually separated.

2. Email, reminder time, and timezone are duplicated from Settings with no indication of source of truth. A user who edits one will not know if it propagates to the other.

3. The destructive reset is at the bottom of a long scroll with a confirmation textbox. The placement is fine but the entire Controls section deserves to be visually walled off, not just labeled.

## 3. Desktop Design Framework

### Shell and Navigation

Replace the top tab bar with a hybrid shell: persistent left sidebar plus a slim top bar.

**Left sidebar (240px wide, persistent at 1280+, collapsible to 64px icon-only at 1024 to 1280).** Contents top to bottom: Anchor wordmark, daily streak summary (e.g., "Day 26 weed, 22 alcohol, 9 nicotine"), primary nav (Home, Check In, Chat, History, Trackers, Insights), secondary nav (Memory, Settings), user identity at the bottom (avatar, email, sign out menu).

**Top bar (48px tall, persistent).** Page title on the left, contextual actions on the right (e.g., on History the "Log missed" button; on Insights the "Export data" button; on Memory the "Pause memory" toggle).

**Breakpoints.**

- 1024 to 1279: sidebar collapses to 64px icon rail. Main content gets full remaining width.

- 1280 to 1439: sidebar expands to 240px. Main content gets remaining width up to a 1200 max content width.

- 1440 to 1599: sidebar 240px. Main content uses up to 1280 with optional right rail panel on pages that benefit (Home, History list, History detail, Check-In, Chat, Memory).

- 1600+: sidebar 240px, main content max 1280, right rail 320px. Total content frame caps at roughly 1840 with the rest as breathing room.

The shell stays consistent across every page. What changes per page is the body region (single column, master-detail, three column, dashboard grid, form plus rail).

### Layout System

Adopt a 12-column grid in the main content region with a 24px gutter and 32px outer padding. Use the grid for actual structure, not as decoration.

**Content width caps by page type.**

- Reading content (history detail main column, memory text fields, settings prose): 720px max line length to keep typography comfortable.

- Forms (check-in, settings forms): 720 to 820px form column with a 320 to 360px summary rail beside it.

- Dense data (insights, history list, trackers): up to 1280px with multi-column layouts.

- Chat: messages column maxes at 720px, with sidebar and right rail filling the remainder.

**When to use cards.** Cards should earn placement. A card is justified when it groups related fields that share an action (a form section), when it represents a discrete entity (a check-in, a tracker, a session), or when it isolates a destructive action. A card is not justified for a single-line readout, a section header, or a list of toggles. The current product uses cards as the default container for everything, which flattens hierarchy. Replace many of the current cards with section headers, dividers (subtle background shifts, not horizontal rule lines), and inline controls. For dense data such as raw logs and event logs, prefer rows or tables over cards.

### Visual Direction

**Dark theme refinement.** Keep the current Anchor Dark palette as the default. Introduce one additional surface tier so there are three: page background (deepest), section/grouped surface (one notch lighter), interactive surface (cards, inputs, buttons, slightly lighter still). Today the product mostly uses two tiers and the difference between them is subtle. Three tiers gives the eye somewhere to rest and lets cards actually function as cards.

**Typography scale (desktop).**

- Display (page title): 32px/40, semibold.

- H2 (section): 20px/28, semibold.

- H3 (subsection): 16px/24, semibold.

- Body: 15px/24, regular.

- Body small (metadata): 13px/20, regular.

- Label/caption: 12px/16, medium. Use sentence case as the default. Reserve uppercase for short, structural labels (KPI tile labels, danger zone). The current "WHERE YOU WERE / FACTOR / CRAVING RISK / MOVES / SUPPORT / REMINDER" all-caps treatment is overused and makes the AI summary look like form metadata instead of prose.

- Data (numeric, in tiles): 28px/32, semibold, tabular-nums.

Switch all numeric displays to tabular-nums so streak counters, time elapsed, and KPI tiles stop wobbling on update.

**Color use.**

- Green: primary action, positive state, sobriety affirmative.

- Yellow: moderate state.

- Red: high risk, destructive, error. Currently only used for destructive; expand carefully to craving risk badges.

- Tracker accent colors (blue for weed, pink for alcohol, teal/green for nicotine): keep as left-border accent only. Do not let them bleed into other UI.

Eliminate any decorative use of color. Color is a signal, not an aesthetic choice.

**Interactive affordance.** Buttons need three clear states (rest, hover, active) and primary vs secondary should be unmistakable at a glance. Today the primary green CTAs and the secondary outline buttons read at similar visual weight; tighten the gap.

## 4. Per-Page Redesign Brief

### Home (/app)

**Recommended layout.** Three-zone dashboard inside the persistent shell.

- Left rail (in the persistent sidebar, no change to page).

- Main content (8 of 12 columns at 1280, full width below sidebar): page header "Today" with date, then a "Latest check-in" hero card spanning the full main area showing mood, craving, energy, focus as a 4-up stat strip with sparkline trends, then a "Next move" card with the primary CTA (Check in again or Start today's check-in depending on state), then a "This week" glance row.

- Right rail (4 of 12 columns at 1280+, hidden below 1280): tracker cluster showing all three trackers as compact cards with sparkline and last-reset, then a small calendar peek (this month, contribution-style colored cells), then a "Talk to your coach" prompt with a suggested context-aware question.

**What moves.** Trackers move from the top row of the body into the right rail. Settings cog moves into the persistent sidebar identity area. Memory gets a sidebar entry.

**What gets promoted.** The next action (check-in) becomes a single visually dominant CTA. The latest check-in becomes a richer summary, not just a card with four labels.

**What gets deprioritized.** "4 total check-ins" footer moves to a tooltip on the "This week" row. The duplicate "Chat with my coach" CTA on the latest check-in card disappears in favor of the right-rail coach prompt.

**Single most important structural change.** Adopt the persistent left sidebar shell so the home page can use its main content area for actual hero content instead of trying to be its own nav.

**New components.** Stat strip with sparkline (reusable on Insights). Tracker compact card (reusable on Trackers and right rails). Coach prompt card with suggested-question state.

### Check-In (/checkin)

**Recommended layout.** Two-column form with a sticky right summary rail that previews the AI's read in real time.

- Top bar (in shell): page title "Check-in / Midday", "Discard" link.

- Main content split:

- Left column (8 of 12 cols, max 820px): the form itself, grouped into four labeled sections.

- Section "Vitals" (4 sliders): Mood and Energy in a sub-pair, Craving and Focus in a sub-pair. Two sliders per row.

- Section "Behaviors" (yes/no row): Sober today, Meeting today, Contacted sober person, Called a fellow, Exercised today, Ate enough today. Render as a single horizontal row of 6 toggle cells, not 6 separate cards.

- Section "Sleep" (single full-width slider).

- Section "Feelings" (trigger pill cloud, full width within the form column).

- Section "Reflection" (Grateful for, Notes, side by side at 6 cols each within the form column).

- Right rail (4 of 12 cols, sticky): the "live read" panel.

- Check-in type pill (Morning / Midday / Evening, auto-selected by time, editable).

- Completion progress (sections complete, fields filled).

- Selected triggers, summarized.

- Live craving risk preview, recomputed as Mood/Craving/Behaviors change. Color-coded (green/yellow/red).

- Sticky primary "Check In" submit button at the bottom of the rail.

**What moves.** Submit moves from the bottom of the page into the sticky right rail. The "Midday check-in" pill moves into the rail's check-in type selector. Section structure becomes visible.

**What gets promoted.** Section headers. The live risk preview, which makes the AI's interpretation visible to the user as they fill the form. This is a real desktop interaction win for a recovery context.

**What gets deprioritized.** The yes/no behaviors compress from six separate cards into one horizontal toggle row.

**Single most important structural change.** Add the sticky right rail with live risk preview. The form stops being a survey and becomes a conversation with the AI in progress.

**New components.** Sticky form rail with live risk preview. Behaviors row (6-cell horizontal toggle group). Section header component (reusable across forms).

**Keyboard shortcuts to add.** Number keys 1 to 10 for the focused slider. Y and N for the focused toggle. Tab/Shift-Tab to move between fields. Cmd/Ctrl+Enter to submit. Esc to focus the discard link.

### Chat (/chat)

**Recommended layout.** Three-pane chat application inside the shell.

- Left pane (left rail of main content, 280px): session list showing past chat sessions grouped by date, with a "New session" button at the top. Each session shows a one-line preview, date, and a small mood/risk indicator if grounded in a check-in.

- Center pane (flex, max 720 message column inside): messages with timestamps, audio playback on AI bubbles, copy/regenerate/thumbs on hover for AI bubbles. Input pinned to bottom.

- Right pane (320px, collapsible): "Today's context" panel showing the user's most recent check-in data (mood, craving, triggers, sober today). This is what the AI is grounding its responses in. Below that, a "Suggested prompts" list based on recent state.

**What moves.** The "+" icon for new session moves into the session list left pane as a labeled "New session" button.

**What gets promoted.** Session history becomes a first-class surface. The grounding context becomes visible to the user.

**What gets deprioritized.** The current "Chat" page header becomes the page title in the top bar of the shell.

**Single most important structural change.** Split the page into three panes. This single change is what makes Chat stop looking like a stretched mobile screen.

**Bug to fix during this work.** Duplicate user message submission ("I just completed a check-in and want to talk through it" appearing twice in a row) needs either client-side debouncing or a server-side dedupe on identical consecutive sends.

**New components.** Session list item (with mood/risk indicator). Today's context panel. Suggested prompt chip.

### History List (/history)

**Recommended layout.** Master-detail.

- Top bar: page title "History", "Log missed" button right-aligned.

- Filter bar across the top of main content: date range picker, risk level multi-select, time-of-day multi-select, search input, sort dropdown.

- Body split:

- Left pane (5 of 12 cols, max 480px): chronological list of check-ins, grouped by date with sticky date headers on scroll. Each row shows time, time-of-day pill, mood/craving numbers, and a colored risk dot. Compact rows, not cards.

- Right pane (7 of 12 cols): preview of the selected check-in. Shows the structured summary (Where you were, Factor, Craving Risk, Moves, Support, Reminder) and a link/button "Open full detail" that routes to /history/[id].

**What moves.** Card grid becomes a list-and-preview pattern. "Log missed" stays in the top bar.

**What gets promoted.** Date grouping. Risk visualization. The preview pane removes one click from every entry inspection.

**What gets deprioritized.** Truncated summaries with ellipsis disappear in favor of the full preview in the right pane.

**Single most important structural change.** Master-detail. The list becomes a scanning surface, the right pane becomes a reading surface, and full detail is one click away when needed.

**New components.** Filter bar (reusable on Insights). Sticky date header. Compact check-in list row. Preview pane.

### History Detail (/history/5)

**Recommended layout.** Reading view with a metadata rail. Use this layout when the user navigates from list to full detail (rather than just using the preview pane).

- Sticky top bar inside main content: prev arrow, date and time, time-of-day pill, next arrow, Edit button, Delete in an overflow menu, small "Listen to summary" icon button.

- Body in a 12-col grid:

- Main column (8 cols, max 720 reading width): the AI structured summary as readable prose. "Where you were" leads, then "Factor", "Moves", "Support", "Reminder". This is the read.

- Right rail (4 cols): metadata. Mood, Energy, Craving as compact stat cells. Sober today, Hours slept. Selected triggers as inline pills. Date, time, check-in type. This is the lookup.

- Below both columns, full width: collapsible "Raw log" section showing all field values verbatim. Default collapsed; expand for forensic detail.

**What moves.** Raw log moves from a competing equal-weight card into a secondary collapsible section. Mood/Craving/Sleep numbers move into the rail as quick-reference, leaving the main column free for the summary as prose. "Listen to summary" shrinks from a full-width megabutton to an icon button in the sticky header.

**What gets promoted.** The interpretation, in comfortable reading width. Prev/next navigation between entries.

**What gets deprioritized.** The MIDDAY pill becomes part of the title row in the sticky header. The raw log becomes available on demand rather than always-visible.

**Single most important structural change.** Separate interpreted insight from raw data. The summary is the read; the numbers are reference. They should not carry equal visual weight.

**New components.** Sticky entry header with prev/next. Metadata rail (compact stat cells, plus quick info). Collapsible raw log panel.

### Trackers (/trackers)

**Recommended layout.** 3-up dashboard grid where each tracker becomes a richer card.

- Grid: 3 columns at 1280+ (one card per tracker), 2 columns at 1024 to 1280, 1 column below.

- Each tracker card shows: colored top border (not just left), tracker name, current streak (large numeric), longest streak, total resets, last reset date, a 30-day sparkline of streak history (or commitment density), and a "Log relapse" button as a secondary action plus a "View detail" link.

**What moves.** "+ Add" stays in the top bar.

**What gets promoted.** Each tracker carries real data instead of one line.

**What gets deprioritized.** The empty space below the cards (filled by richer cards).

**Single most important structural change.** Each tracker card carries a sparkline and historical context, not just elapsed time.

**New components.** Tracker detail card with sparkline. (This is the same card used in compact form on Home's right rail.)

### Insights (/insights)

**Recommended layout.** True dashboard with hero, KPIs, charts, heatmap, and habits.

- Top bar: page title, time range toggle (7d / 30d / 90d / All), Export.

- Hero row (full width): a single primary metric card. Candidate: combined sober streak (e.g., "57 sober-days across 3 trackers this month") with a small trend indicator. Pick one hero number and commit to it.

- KPI strip (4-up at 1280+, 2 rows of 4 at 1024): the existing tiles, but visually flatter (no heavy card chrome) and with consistent label/data ratios.

- Two charts side-by-side (6 cols each): Mood line chart, Craving line chart. With low data, show a single consolidated empty state across both, not two side-by-side empty cards.

- Calendar heatmap (full width): contribution-graph style, 90 days at a glance, color-coded by risk. This replaces the current giant single-month calendar.

- Recovery habits (full width): horizontal bar chart with one bar per habit, 0 to 100% over the time range.

- Sobriety trackers (full width): a compact mirror of the Trackers page, useful here for cross-reference.

**What moves.** The single-month calendar gets replaced by a 90-day heatmap.

**What gets promoted.** A hero metric. Time range as a sticky persistent control.

**What gets deprioritized.** The seven equal-weight KPI tiles become a compact KPI strip below the hero.

**Single most important structural change.** Pick a hero metric and make it visually dominant. Insights without a hero is just a stat pile.

**New components.** Hero metric card. Compact KPI tile. Heatmap component (90-day contribution graph).

### Settings (/settings)

**Recommended layout.** Two-column settings with a left nav rail of categories.

- Left settings nav (200px inside main content): Appearance, Memory, Email and Reminders, Account, Data, Danger zone.

- Right pane: section content. Inline saves on toggles and dropdowns (no global Save button). The Email section keeps an explicit Save because email is multi-field, but the rest are immediate.

**What moves.** Memory becomes a top-level settings category and also a sidebar destination in the global shell. The theme picker shrinks to a horizontal row, not a 3x2 card grid that dominates the page.

**What gets promoted.** Account section (currently invisible). Data section (export, reset).

**What gets deprioritized.** The theme picker no longer leads the page.

**Single most important structural change.** Add the settings nav rail and use inline saves. The current single-Save-button-with-unclear-scope problem disappears.

**Bug to fix during this work.** The red icon next to the email field has no tooltip or explanation. Either explain what it means or remove it.

**Source-of-truth call.** Email, reminder time, and timezone live here in Settings only. Memory page no longer holds these fields. (See Memory redesign below.)

**New components.** Settings nav rail. Inline-save toggle row.

### Memory (/memory)

**Recommended layout.** Profile inspector with three zones, plus a separated danger zone.

- Top bar: page title "Memory", "Pause memory" toggle right-aligned.

- Main content in a 12-col grid:

- Left (3 of 12 cols): profile category nav. Categories: Recovery focus, Program and support, Sober contacts, Meeting links, Why I'm doing this. Vertical list, clickable to scroll or focus the corresponding panel.

- Center (5 of 12 cols): selected profile fields, inline-editable. No edit pencils. Fields appear as labeled text with an edit affordance on hover. Each category renders its fields here.

- Right (4 of 12 cols): "What Anchor has noticed". The current Recent Patterns block (Top triggers, Mood trend, Pattern to notice). Plus a brief "summary of you" paragraph at the top. Below patterns, a compact event log showing the last 10 entries with "View all" link to expand.

- Below the three columns, full-width: a clearly visually walled Danger zone containing "Reset all memory" with the confirmation textbox.

**What moves.** Email, reminder time, and timezone leave Memory and live only in Settings (single source of truth). The Pause memory toggle moves to the top bar. Edit pencils disappear in favor of inline editing.

**What gets promoted.** AI patterns become a parallel right-column panel rather than a section buried below profile fields. The mental model split between "your inputs" (left and center) and "AI's outputs" (right) becomes the page's organizing principle.

**What gets deprioritized.** The full event log becomes a "View all" expansion rather than always-visible. Edit pencils are gone.

**Single most important structural change.** Separate profile (your inputs) from memory (AI's outputs) into parallel zones. Make the page feel like a profile inspector, not a database admin view.

**New components.** Profile category nav. Inline-editable profile field. Patterns panel. Compact event log with "View all" expansion. Danger zone wrapper.

## 5. Priority Order

Sequence the redesign by impact, with shell paired to the highest-frequency surface because every page depends on the shell.

**Block 1: Shell + Check-In.** Ship together. The shell (sidebar plus top bar, breakpoint behavior, settings/memory entries in the sidebar) is foundational and every other page assumes it exists. Check-In is the daily ritual and the highest-frequency interaction in the product. Pairing them means the first user-visible release establishes both the new app frame and the most-used flow with its sticky risk-preview rail. This is the work block that makes Anchor feel like a desktop product.

**Block 2: Home.** Depends on the shell. Sets the first impression after login. With the shell already in place, Home becomes a real dashboard rather than a centered content stack. Highest visibility per unit of engineering work.

**Block 3: Chat.** Most damaging visual problem in the product today. The three-pane redesign with session list and grounding-context panel is the change that makes the AI feel like it knows you. Also the page where fixing the duplicate-message bug lands.

**Block 4: History list and detail (paired).** Now structurally coupled because the list uses master-detail with a preview pane and the detail page is the "open full" target. Ship them together. Master-detail plus the metadata-rail reading view are the two changes that turn History from a log into a recovery archive.

**Block 5: Insights.** Becomes the killer page once data fills in. Worth landing the dashboard structure now even with low data, because the structure itself shapes how users perceive whether the product is "working".

**Block 6: Memory.** Highest-stakes feature in the product (AI behavior is shaped by it) and currently the most underbuilt surface. The profile inspector redesign makes the model visible and changes how users trust the AI.

**Block 7: Settings.** Meta surface. Sidebar pattern fixes it structurally. Lower frequency, lower stakes. Worth doing after Memory because Memory and Settings will share the inline-save and field-editing patterns. Also where the email/timezone source-of-truth consolidation lands.

**Block 8: Trackers.** Smallest surface, smallest payoff, easiest change. The richer-card design with sparkline is mostly a single component build. Can ship as cleanup work alongside any other block when an engineer has slack.

A pragmatic order-of-operations note. Block 1 (shell + check-in) is the only hard dependency. After that, blocks 2 through 8 can ship in any order based on engineering bandwidth. The recommended order above is by user-facing impact per block, not by dependency.

================ END AUDIT CONTENT ================

Color redo

I already have the audit loaded (just committed it) and have surveyed App.tsx + layout.tsx. Let me complete the survey before proposing the plan.

Survey complete. Reporting findings + proposing plan now. Stopping for approval before any code.

Step 3: Survey findings

Routing. wouter v3. Routes are wrapped by <Layout> in App.tsx AppGate (lines 64-81). Authenticated routes: /app, /checkin, /checkin/edit/:id, /checkin/backfill, /history, /history/:id, /trackers, /trackers/:id, /chat, /insights, /settings, /memory.

Current nav. src/components/layout.tsx renders a bottom tab bar (not top tabs as the audit phrasing suggests — but functionally the same problem: stretched mobile chrome). Centered column maxed at 640px above 768px via --app-max-width. Settings page already special-cases the nav off via !isSettings.

Styling. Tailwind v4 (@theme inline, @plugin "@tailwindcss/typography"). Design tokens are HSL CSS vars in src/index.css: --background, --card, --primary, --muted-foreground, --border, etc. Six themes via [data-theme="..."] selectors. Font: DM Sans.

Component library. Full shadcn/ui set already installed (Radix primitives) including sidebar.tsx, dropdown-menu.tsx, avatar.tsx, tooltip.tsx, sheet.tsx. The shadcn sidebar.tsx exists but is the heavyweight collapsible-with-mobile-sheet variant; I'll roll a leaner custom sidebar against the spec rather than retrofit it.

Breakpoint hook. hooks/use-mobile.tsx is hardcoded to 768px. Insufficient for the new spec which needs 1024 / 1280 / 1440 / 1600. Will add a new desktop-breakpoint hook.

Settings cog on Home. src/pages/home.tsx lines 124-131 (the SVG gear linking to /settings).

Redundant back-links.

src/pages/settings.tsx line 232-238 — ← BACK to /app. Remove.

src/pages/memory.tsx line 301-303 (error state) and likely the main return. Remove.

src/pages/history-detail.tsx line 33-34 — ← Back to history. KEEP — list-to-detail nav, not redundant with sidebar (sidebar can't take you from /history/5 back to /history).

Sign-out flow. Does NOT currently exist anywhere in the codebase. The audit requires it in the sidebar identity section. Will implement: supabase.auth.signOut() then navigate("/login") via wouter, exposed through a DropdownMenu on the avatar.

Streak data. useTrackers() returns Tracker[] with name, color, startDatetime. lib/api.ts exports formatDurationCompact(). Sidebar will compose "Nd name" lines, hidden in collapsed 64px rail.

User email. Comes from supabase.auth.getSession(). No avatar field. Will use first-letter initials avatar.

Step 4: Implementation plan

Branch

Create feat/desktop-shell from fix/ts-cleanup HEAD (current main repo branch).

New files (5)

src/components/shell/page-context.tsx — React context: usePageMeta() returns { title, setTitle, actions, setActions }. Pages call useSetPageMeta({ title, actions }) in an effect.

src/components/shell/AppSidebar.tsx — 240px / 64px sidebar. Wordmark, streak summary, primary nav, secondary nav, identity footer with sign-out dropdown. Uses useTrackers, useLocation, supabase.auth. Controlled by a collapsed prop (driven by viewport width).

src/components/shell/AppTopBar.tsx — 48px top bar. <PageMetaContext>-driven title left, actions slot right.

src/components/shell/AppShell.tsx — desktop layout composer: <aside> (sidebar) + <div> (top bar + main scroll region). Handles the breakpoint width math (sidebar collapsed ≤1279, expanded ≥1280; main content max-width per spec).

src/hooks/use-desktop-breakpoint.tsx — useDesktopBreakpoint() returns { isDesktop, sidebarCollapsed } based on window.matchMedia('(min-width: 1024px)') and (min-width: 1280px).

Modified files (5)

src/components/layout.tsx — keep entire current implementation as the mobile branch. Wrap with conditional: render <AppShell> at lg: (≥1024), render existing column-with-bottom-nav at <lg. Use Tailwind hidden lg:flex / lg:hidden to swap. Drop the isSettings special-case (no longer needed at desktop; preserve on mobile).

src/App.tsx — wrap <Layout> (or a new <AuthShellProvider> step inside AppGate) with <PageMetaProvider> so pages can write title/actions. One-line change.

src/pages/home.tsx — remove cog (lines 124-131). Add useSetPageMeta({ title: "Today" }) so top bar shows it on desktop. The mobile bottom-nav layout is unchanged so the cog removal is OK on mobile too (Settings is reachable from sidebar on desktop; on mobile it's reachable via the bottom-nav... wait — Settings is NOT in the existing bottom nav. This is a real concern for mobile.)

src/pages/settings.tsx — remove the ← BACK link header (lines 232-238). Add useSetPageMeta({ title: "Settings" }).

src/pages/memory.tsx — remove ← BACK links (main return + error state). Add useSetPageMeta({ title: "Memory" }).

Deleted files

None.

Commit chunks (in order)

feat(shell): add page meta context for shell title and actions slot

feat(shell): add AppSidebar component with streak summary and sign-out

feat(shell): add AppTopBar component

feat(shell): add AppShell wrapper and desktop breakpoint hook

feat(shell): wire shell into Layout at lg breakpoint, preserve mobile

chore(shell): remove redundant settings cog and back-links from pages

Verify

pnpm --filter @workspace/recovery-checkin typecheck — must pass clean

pnpm --filter @workspace/recovery-checkin build — must pass clean

(Playwright smoke deferred unless you want me to run it after merge — running it on this worktree will hit a different state than CI)

Open question that affects the plan — needs your call

Mobile Settings/Memory access. The current bottom-nav has 6 tabs: Home, Check In, Chat, History, Trackers, Insights. Settings and Memory are NOT in it. Today on mobile, Settings is reached only via the cog on Home. Memory is reached only via a buried link in Settings.

If I remove the cog on Home as the brief says, mobile users lose access to Settings. Three options:

A. Keep the cog on Home for mobile only (lg:hidden it). Removes it on desktop where the sidebar covers it. My recommendation — preserves mobile behavior unchanged, satisfies the "below 1024 = unchanged" constraint literally, and is one extra line of Tailwind.

B. Add Settings and Memory to the mobile bottom-nav. Out of scope per "Mobile preserved below 1024 — existing mobile layout unchanged."

C. Remove the cog everywhere and accept that mobile users can't reach Settings (broken).

Going with A unless you say otherwise. Same logic applies to ← BACK on Settings/Memory: they're useful nav anchors on mobile (no sidebar there). I'll lg:hidden them rather than delete them outright.

Approve the plan as written (with mobile-preservation option A) and I'll execute. Or call out changes.

Audit Addendum

Anchor Desktop Design Audit Addendum

Addendum date: May 9, 2026 Addendum scope: 2 pages missed in the original audit (Check-in detail / post-submission, and Tracker detail) Output target: append to docs/desktop-audit.md

This addendum covers two surfaces that were not captured in the original 9-page audit. The format mirrors the main document. Each page gets an entry in section 2 (per-page audit) and section 4 (per-page redesign brief). The priority order in section 5 of the main audit does not change; these two surfaces fold naturally into existing implementation blocks.

Addendum to Section 2: Per-Page Audit

Check-in Detail (/checkin/complete)

Layout. Single-column stack. Page header "Check-in Complete / Here's your reflection." Then a giant full-width "Listen to full summary" button. Then one tall card containing the AI's reflection (Where you're at, Something to watch, Craving risk, Next moves, Support, Remember, From your sponsor). Then a disabled "Chat with my coach" CTA. Then a "Check in again" CTA at the bottom.

Navigation. No breadcrumb, no back button, no done button. The user is in a transitional state (just completed a check-in) but the page does not give them a clear way out except by tapping a tab.

Information hierarchy. The reflection itself is the value, but it competes with the giant "Listen to full summary" button at the top and two competing CTAs at the bottom. The "Chat with my coach" CTA is disabled, which is the single most confusing element on the page. The "Check in again" CTA implies the primary next action is to log another check-in, which is rarely true.

Visual design. Same issues as History detail: full-content-width prose at uncomfortable line lengths, all-caps section labels that read as form metadata rather than reflective writing, equal-weight container card.

Desktop patterns missing. Metadata rail showing the values the user just submitted (mood, energy, craving, focus, behaviors, triggers). A "talk through this" hand-off to chat with grounding context already loaded. Clear "done" affordance. Comparison context (how does this check-in compare to the user's last few).

Three most damaging problems.

"Chat with my coach" is disabled at the precise moment a user would benefit most from talking the reflection through. This is either a wiring bug (chat is not ready post-submit) or a UX choice that should be reversed. Either way it is the page's biggest issue.

"Check in again" as the primary bottom CTA implies the right next action is to log another check-in immediately, which is rarely the case. The right default actions are "continue" (back to home) or "talk to coach", not another check-in.

The user has no quick reference of what they actually submitted. They answered 30+ questions and the only acknowledgment is the AI's prose. They cannot easily verify the AI is reading their data correctly without scrolling back through the form.

Tracker Detail (/trackers/[id])

Layout. Single tracker card with name and a real-time elapsed counter ("9d 11h 38m 21s" with seconds ticking), then a 3-up row of Edit / Reset / Archive buttons, then Delete Tracker below in red. About 80 percent of the page is empty.

Navigation. Back link only. No way to navigate to neighboring trackers, no breadcrumb, no relationship to the trackers list.

Information hierarchy. The elapsed time is the hero, which is correct. Everything else is buttons. There is no current/longest comparison, no past streaks, no relapse log, no notes. This is functionally a slightly-larger version of the list card.

Visual design. Real-time second counter is dramatic and may be psychologically counter-productive for some users in recovery (watching every second tick reinforces the present moment in ways that some find grounding and others find anxiety-producing). The colored left border is good and consistent with the list view.

Desktop patterns missing. Streak history chart showing past attempts. Relapse log with dates and notes. Stats strip (longest streak, total resets, average streak length). Quick navigation to other trackers (prev/next or sidebar list). A clearer destructive-action zone separating Edit (safe) from Reset / Archive / Delete (varying degrees of destructive).

Three most damaging problems.

The page is structurally empty. A tracker drill-in is the place to put history and context, but this view shows less data than a serious sobriety app should. No streak history, no past resets, no comparison.

Edit, Reset, Archive, and Delete sit as four equal-weight actions, but Reset wipes the current streak, Archive removes the tracker from active view, and Delete removes the tracker entirely. Three different destructive actions of three different severities, presented as if they are the same.

Real-time second counting is a UX call that has not been made deliberately. Default behavior should probably show days and hours, with finer granularity available on demand. Watching seconds tick is not universally helpful in recovery.

Addendum to Section 4: Per-Page Redesign Brief

Check-in Detail (/checkin/complete)

Recommended layout. Reading view with metadata rail. Same structural pattern as History detail, tuned for the post-submission moment.

Sticky top bar inside main content: "Check-in complete" title, a "Done" button on the left (returns to home), and a small "Listen to summary" icon button.

Body in a 12-col grid:

Main column (8 cols, max 720 reading width): the AI reflection as readable prose. "Where you're at" leads, then "Something to watch", "Next moves", "Support", "Remember", "From your sponsor". This is the read.

Right rail (4 cols): the values the user just submitted. Mood, Energy, Craving, Focus as compact stat cells. Sober today, Hours slept. Selected triggers as inline pills. Time of day pill. This is acknowledgment that the AI saw what they put in.

Below both columns, full width: a primary action band.

Primary CTA: "Talk through this with my coach" (active, not disabled, with a small chip showing "Today's reflection" as the grounding context the chat will inherit).

Secondary CTA: "Back to home".

Tertiary text link: "Or check in again" for the unusual case of multiple check-ins per session.

What moves. "Listen to full summary" shrinks from a full-width megabutton to an icon button in the sticky top bar. "Chat with my coach" becomes the primary action and is enabled. "Check in again" demotes to a tertiary text link.

What gets promoted. The coach hand-off, since this is the moment to talk the reflection through. The user's submitted values in the rail.

What gets deprioritized. "Listen to full summary" as a megabutton. "Check in again" as a primary CTA.

Single most important structural change. Make this page the post-submission sibling of History detail. Same metadata-rail layout, action affordances tuned for "you just did this, what's next" rather than "you're reviewing the past".

Bug to fix during this work. The disabled "Chat with my coach" state must be resolved. Either it is a wiring bug (chat session is not ready post-submit; fix the readiness check) or an intentional disable that needs reversing (the post-check-in moment is precisely when coach engagement matters most). Investigate which during the survey step and fix accordingly.

New components. Reuses History detail components (sticky entry header, metadata rail, prose reading column). Adds a unique "Sponsor message" subcomponent for the "From your sponsor" section that does not exist on historical entries. Adds a coach hand-off chip showing the grounding context that will pass to chat.

Implementation block. Ships with Block 1.B (check-in redesign). The post-submission state is part of the check-in flow.

Tracker Detail (/trackers/[id])

Recommended layout. Detail view with hero, stats strip, history zone, and a separated action zone.

Top bar: tracker name (left), prev/next navigation between trackers (right).

Hero zone (full width): tracker name with colored top border (not just left), current elapsed time as the hero number, "Since [date] at [time]" timestamp directly below.

Stats strip (4-up row, full width below hero): longest streak, total resets, average streak length, attempts.

Main content split (12-col grid):

Left (8 cols): streak history chart. Each bar represents one streak attempt with its duration; current streak highlighted in the tracker's accent color. Hover for date range and reset reason if available.

Right (4 cols): reset log. Compact list of past resets with date, duration of that streak, and any note the user added. Most recent at top.

Below both columns, action zone with three clearly separated regions:

Safe actions (left): Edit (rename, change color, change start date).

Reset zone (center, neutral background): "Mark a relapse" with a clear secondary button. Includes a note field for "what happened" (optional).

Destructive zone (right, walled off with red text and danger styling): Archive (with explanatory text "Stop tracking, keep history") and Delete tracker (with explanatory text "Remove permanently, including history").

What moves. Edit / Reset / Archive / Delete reorganize from a flat row into three labeled zones with clear severity. The elapsed time gains context (history chart, stats strip). Prev/next tracker navigation appears in the top bar.

What gets promoted. Historical context (streak chart, reset log). Action severity clarity. Stats that show progress over time, not just the current streak.

What gets deprioritized. The lone elapsed-time pill becomes part of a richer hero rather than the entire page content. The four flat action buttons split into severity zones.

Single most important structural change. Add the streak history chart and reset log. A tracker drill-in without history is just a bigger version of the list card. With history, it becomes the recovery-affirming "here is what you have built and rebuilt" view that this page should be.

UX call to confirm with the user. Real-time second counting. The current page ticks seconds. Default behavior should probably be days and hours visible by default, with seconds available on hover or click (or a settings preference). Some users find ticking seconds grounding; others find it anxiety-producing. Worth a deliberate decision rather than the current accidental default.

New components. Streak history chart (horizontal bar chart, one bar per streak attempt). Reset log row. Tracker stats strip. Three-zone action region (safe / neutral / destructive). Prev/next tracker navigation in the top bar.

Implementation block. Ships with Block 8 (Trackers redesign). The list and detail are tightly coupled.

Addendum to Section 5: Priority Order

No changes to the block sequencing. These two surfaces fold into existing blocks.

Check-in detail joins Block 1.B (check-in redesign). Same metadata-rail pattern as History detail, plus the disabled-coach bug fix. Adds modest scope to Block 1.B but reuses components from the History detail work in Block 4.

Tracker detail joins Block 8 (Trackers redesign). Adds meaningful scope (the streak history chart is a real component build) but the page is small and the data structure already exists.

Both surfaces depend on Block 1 (shell) being in place. Beyond that, no new dependencies.
