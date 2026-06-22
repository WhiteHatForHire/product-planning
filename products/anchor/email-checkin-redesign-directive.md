---
title: "email checkin redesign directive"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/email-checkin-redesign-directive.md.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# email checkin redesign directive

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Daily Check-In Email Redesign — Directive

Status: READY TO FIRE Branch: feat/email-checkin-redesign

Header block

Field

Value

Surfaces

Resend email template, daily reminder scheduler, email send pipeline in api-server

Production impact

API change + email template change (user-facing)

Council of Models

no

Auto-merge

no (user-facing copy + email template)

Credentials

gh, DATABASE_URL (read-only for testing data fetch), RESEND_API_KEY (Phase D test send)

Agent

CC Local (preferred — needs Resend test send capability) OR CC Cloud (code-only, defer manual test send to Marcus)

Role statement

You are replacing the current daily check-in email — a one-line plain-text message with no branding — with a properly designed, mobile-responsive HTML email that shows the user their actual sobriety data (all focus day counts), references their last check-in gently, and provides a clear primary CTA to open Anchor and check in. The new email matches Anchor's voice (grounded, low-pressure, non-performative) and includes crisis resources in the footer.

Apply AUTONOMY_LAYER.md before executing

Apply AUTONOMY_LAYER.md (v1.3, repo root) before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1.

Deployment posture

Per section 1.8:

Agent does NOT merge. Open PR, stop.

Agent does NOT deploy. Fly + Vercel auto-deploy on merge.

No schema changes. No new tables.

No flyctl secret changes (RESEND_API_KEY already configured).

One MANUAL_REQUIRED item to flag in PR body: configure auto-responder on support@sobrietyanchor.com inbox (external to repo).

Working files protocol

Per section 0.4. Create:

docs/run-notes/session-YYYY-MM-DD-email-checkin-redesign-plan.md

AUTONOMOUS_RUN_LOG.md (append)

BLOCKERS_FOR_MARCUS.md (if needed)

Design data

Subject line (verbatim)

If user has first name: Anchor — {firstName}, your check-in is open If user has no first name: Anchor — your check-in is open

From

Name: Anchor

Address: support@sobrietyanchor.com

Email content variables (compute server-side before send)

firstName: from stable_profile.first_name, or null

focuses: array of { focusLabel, dayCount } for every active tracker the user has

lastCheckInLabel: human string like "yesterday evening" / "2 days ago" / "earlier today" / "no recent check-in"

todayLabel: like "Tuesday, May 13" (user timezone)

appUrl: https://sobrietyanchor.com/app

checkInUrl: https://sobrietyanchor.com/checkin

chatUrl: https://sobrietyanchor.com/chat

historyUrl: https://sobrietyanchor.com/history

settingsUrl: https://sobrietyanchor.com/settings

unsubscribeUrl: signed token URL that disables daily reminders

HTML template (verbatim layout, copy locked)

Single-column, dark background (#0F1115), light text (#E8EAED), one accent color for CTA (#4F8FFF or current Anchor accent).

Structure:

Header. "Anchor" wordmark linking to appUrl. Small, top-left aligned.

Date line. todayLabel. Subtle, secondary color (#9CA3AF).

Greeting (conditional).

If firstName: "Hi, {firstName}."

Else: omit greeting entirely

Day counts block. One line per focus. Format: Day {dayCount} — {focusLabel} Example: Day 47 — alcohol Day 12 — cannabis

If user has zero active focuses: omit the block entirely and skip to step 6.

Last check-in line. "Last check-in: {lastCheckInLabel}." If "no recent check-in", phrase it as: "It has been a while since your last check-in."

Primary CTA. Button labeled "Check in now" linking to checkInUrl.

Secondary links. Small, single row, separated by " · ":

"Chat with Anchor" → chatUrl

"View history" → historyUrl

Footer. Small, muted:

"If you are in crisis, reach 988 (US) or SAMHSA at 1-800-662-HELP."

"Anchor — sobrietyanchor.com"

"Settings · Unsubscribe"

Physical mailing address (Eagle Rocket LLC) for CAN-SPAM compliance.

Plain-text fallback (verbatim, exact)

{Hi, {firstName}.}  [omit if no firstName]

{todayLabel}

Day {dayCount} — {focusLabel}

Day {dayCount} — {focusLabel}

...

Last check-in: {lastCheckInLabel}.

Check in now: {checkInUrl}

Chat with Anchor: {chatUrl}

View history: {historyUrl}

If you are in crisis, reach 988 (US) or SAMHSA at 1-800-662-HELP.

Anchor — sobrietyanchor.com

Settings: {settingsUrl}

Unsubscribe: {unsubscribeUrl}

Voice constraints (enforce in template review)

The template must NOT contain any of these phrases:

"Don't break your streak"

"You're doing great"

"Keep going"

"We believe in you"

"Stay strong"

"Hey there!"

"Just checking in"

Any emoji

The template MUST contain:

The literal day counts as computed

The crisis resources line

The unsubscribe link

Phase plan

Each phase follows AUTONOMY_LAYER section 3: pre-flight, smoke first, implementation, health check, commit.

Phase A is the first data-consuming phase and MUST execute spec-reality reconciliation per section 1.13.

Phase A — Spec-reality reconciliation + email module location

Pre-flight: git status clean, cut branch from main: feat/email-checkin-redesign, credentials preflight per section 0.5, baseline test counts recorded, ANCHOR-1 build order (lib/db, lib/api-zod first).

Spec-reality reconciliation per section 1.13:

Locate existing email module path (likely artifacts/api-server/src/lib/email/ or similar)

Locate the current daily reminder scheduler invocation

Identify how user data is fetched for email composition (focuses, last check-in, firstName)

Identify how Resend client is currently invoked

Locate the unsubscribe token signing logic if it exists, or note its absence as a BLOCKER

Log all paths to AUTONOMOUS_RUN_LOG.md. No code changes in this phase. Documentation only.

Smoke first: not applicable (discovery phase).

Commit: chore(email): spec-reality reconciliation findings logged

Phase B — Email composer module

Pre-flight: prior commit exists.

Smoke first. Unit tests for composer:

Renders HTML with firstName present

Renders HTML with firstName absent

Renders all focuses in order

Omits day-counts block when zero focuses

Renders correct lastCheckInLabel for each case (today, yesterday, N days ago, never)

Plain text fallback matches verbatim spec

Required variables interpolated correctly

Forbidden phrases absent from output

Implementation: compose-email module taking the variables defined above and returning { html, text, subject }.

Health check: full api-server tests green.

Commit: feat(email): daily check-in email composer with all-focus day counts

Phase C — Wire into scheduler + Resend send

Pre-flight: prior commit exists.

Smoke first. Integration test asserting:

Daily reminder job calls the new composer with correct variables

Gated by EMAIL_OUTREACH_ENABLED

No send when flag disabled

Implementation: replace existing send logic in the scheduler with calls to the new composer, use Resend with from = "Anchor <support@sobrietyanchor.com>".

Health check: full api-server tests green, no regression in scheduler tests.

Commit: feat(email): wire new composer into daily reminder scheduler

Phase D — Manual test send + BUILD_REPORT + PR

Pre-flight: prior commit exists.

MANUAL_PLAYTEST_REQUIRED: Marcus runs a test send to his own address using a CLI script or scheduler-test endpoint with real data. Verifies rendering on mobile (Gmail iOS, Apple Mail, Outlook iOS) and desktop (Gmail web). Logs findings in BUILD_REPORT.

BUILD_REPORT. Write docs/run-notes/session-YYYY-MM-DD-email-checkin-redesign-build-report.md per section 5. Include:

All discovered file paths from Phase A

Per-client rendering verification (logged after Marcus's manual playtest)

Auto-responder setup as MANUAL_REQUIRED item (see below)

Confirmation no Neon migration required

Test counts (unit + integration)

Open PR: title feat: daily check-in email redesign.

PR body must include:

Phase summary

Changed files

Test counts

Manual playtest items

MANUAL_REQUIRED: configure auto-responder on support@sobrietyanchor.com inbox with the suggested copy below

Auto-merge: NO. Stop after PR open.

Suggested auto-responder copy (for Marcus, outside repo)

Set this up wherever you host email for sobrietyanchor.com. Not in the codebase.

Thanks for reaching out to Anchor.

This inbox is not monitored in real time. Replies are forwarded for review but you may not get a personal response.

If you are in crisis:

988 (US) — Suicide & Crisis Lifeline, call or text

SAMHSA — 1-800-662-HELP (4357), 24/7 support

For day-to-day support, the in-app chat with Anchor is the fastest way to be heard:

https://sobrietyanchor.com/chat

For product issues or account help, reach Marcus directly at [Marcus's personal email].

Take care.

— Anchor

Also configure forwarding on support@sobrietyanchor.com to Marcus's personal email so replies are reviewable.

Forbidden side quests

Do NOT change daily reminder send timing or frequency

Do NOT modify EMAIL_OUTREACH_ENABLED gate behavior

Do NOT add new email types (weekly summary, missed-check-in follow-up are separate)

Do NOT add open-tracking pixels or click-tracking that violate the recovery-app trust posture

Do NOT add streak language, motivational copy, or emojis to the template

Do NOT bundle unrelated cleanup with feature work per section 1.9

Self-repair playbook

Apply AUTONOMY_LAYER section 2. No new entries from this directive.

Deferred-issues format

Per AUTONOMY_LAYER section 4.

BUILD_REPORT format

Per AUTONOMY_LAYER section 5.

Hard stops

Per AUTONOMY_LAYER section 6.

GO

Begin Phase A pre-flight per AUTONOMY_LAYER section 3. Credentials preflight scope: gh, DATABASE_URL (read-only for testing data fetch), RESEND_API_KEY (for Phase D test send). Cut branch from main: feat/email-checkin-redesign. Create docs/run-notes/session-YYYY-MM-DD-email-checkin-redesign-plan.md and AUTONOMOUS_RUN_LOG.md at repo root.
