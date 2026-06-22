---
title: "Sober Garden Master Spec"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/Sober garden /Old/Sober Garden Master Spec.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Sober Garden Master Spec

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
SOBER GARDEN

Master Specification

Full vision document with V0 build scope

Roots remember. Progress is damaged, never erased.

Author: Marcus Vale

Working draft v0.1 • April 26, 2026

Companion to Anchor (Eagle Rocket LLC)

Table of Contents

Section 0. V0 Build Spec

Section 1. Product Thesis and North Star

Section 2. Target User and Use Cases

Section 3. Core Invariants

Section 4. Recovery Model

Section 5. Core Loops

Section 6. Onboarding

Section 7. AI Gardener

Section 8. Weather System

Section 9. Garden Visual System

Section 10. Milestones and Unlocks

Section 11. Journal System

Section 12. Sharing and Social

Section 13. Anchor Integration

Section 14. Safety and Crisis Protocol

Section 15. Privacy and Data Handling

Section 16. Notifications Policy

Section 17. Accessibility

Section 18. Data Model

Section 19. Tech Stack and Architecture

Section 20. Build Sequence

Section 21. Risks and Open Questions

Section 22. Naming, Brand, and Positioning

Section 23. Marketing and Go-to-Market

Section 24. Monetization

Section 25. Long-Term Vision

Section 26. Closing Note

Section 0. V0 Build Spec

This section is at the top of the document on purpose. When you return to this doc to start building, the action plan should be the first thing you see — not the philosophy. The full vision lives in Sections 1-26 below. V0 is the cut-down build that proves the loop.

0.1 V0 Goal

Ship a working web app where Marcus (or a close-circle test user) can do daily voice or text check-ins, see a visual garden state respond, log a slip without losing roots, and accumulate a real journal — within one week of focused build using AI-directed development on Replit.

V0 is not a production launch. V0 is a personal-use prototype that proves the metaphor changes behavior on hard days. If after 14 days of personal use V0 makes Marcus more likely to take a recovery-supportive action on a difficult day, the product thesis is validated and V1 build begins. If not, the spec gets revisited before more is built.

0.2 V0 In-Scope Features

Auth and Account

Supabase auth with email + magic link.

Single user per account. No social, no sharing in V0.

Profile: display name, timezone, sobriety target label, sobriety start date.

Daily Check-In (Voice and Text)

Voice input via OpenAI Whisper API (preferred path).

Text input as fallback when microphone unavailable or user prefers.

Single open prompt: "How are you doing today?"

Manual craving slider 0-10 (always asked, never inferred).

Manual weather selection from 5 states (sunny, cloudy, rainy, stormy, foggy) — user controls weather, not AI.

AI generates a one-sentence reflection in the gardener voice based on the check-in.

Check-in saved to journal with timestamp.

Sobriety Tracking

Lifetime sober days (primary number — never decreases).

Current streak (secondary number — resets on slip).

Slip button: confirms intent, resets current streak, preserves lifetime days, preserves journal, preserves milestones.

Return streak begins immediately after slip.

Visual Garden (Emoji/CSS, Not Pixel Art Yet)

Single tree displayed as emoji or simple SVG with 5 growth stages keyed to current streak: seed, sprout, sapling, young tree, mature tree.

Damaged states for stages 2-5: same tree with visible damage (greyscale, fewer leaves, lightning-struck CSS overlay).

Weather displayed as overlay: emoji or simple CSS animation (sun, clouds, rain, lightning, fog).

Roots visible as a small underground panel — never empty, even after slip.

No pixel art, no isometric grid, no wildlife, no tile system. V0 is text-and-emoji-grade visual design.

AI Gardener (Minimal V0 Version)

System-prompted LLM call after each check-in.

Gardener persona: observational, never prescriptive. Strict forbidden-phrase list (no "you should," no diagnostic language, no clinical terms).

Crisis intercept hardcoded on frontend: regex/keyword detection bypasses LLM entirely and shows hardcoded crisis modal.

Gardener output stored as system event, not as user fact.

One paragraph response max. No back-and-forth dialogue in V0.

Journal

All check-ins stored as journal entries.

Scrollable list, newest first.

Tap entry to view full text + weather + craving + gardener response.

Search by date or keyword.

Export to markdown or text file.

Milestones

Celebration screen at: 24h, 3d, 7d, 14d, 30d, 60d, 90d, 6mo, 1yr.

Each milestone is a text + simple animation moment, not a wildlife unlock yet.

Milestone history viewable in profile.

Onboarding

3-screen onboarding before first check-in.

Screen 1: "This is not medical care." Withdrawal disclaimer for alcohol/benzo dependence with link to medical resources.

Screen 2: "Roots remember." Explain the slip mechanic — show a damaged tree visual with intact roots, demonstrate that slipping doesn't erase progress.

Screen 3: Set up sobriety target, start date, and first check-in.

Slip-rehearsal: during onboarding, user is invited to tap the slip button to see what happens. This removes fear of using it later.

Safety

Hardcoded crisis intercept (regex on frontend).

Crisis modal with 988, SAMHSA, and one-tap support contact.

Withdrawal disclaimer at onboarding and in settings.

Data deletion (one-click "delete my account and all data" in settings).

Data export (JSON + markdown).

0.3 V0 Out of Scope

Pixel art and isometric garden view (V1).

Wildlife milestone rewards (V1).

Multiple trees and support plants (V1.5).

Full AI gardener with memory across sessions (V1.5).

Phase forecasting (V1.5, with careful framing).

Read-only sharing (V2).

Sponsor view (V2).

Native mobile app (V2).

Anchor integration (V2).

Community features (V3).

0.4 V0 Tech Stack

Layer

Choice

Reason

Frontend

Next.js + Tailwind

Mobile-first responsive web. Familiar stack. Vercel-friendly.

Backend

Next.js API routes

Serverless. No separate backend service in V0.

Auth

Supabase Auth

Magic link, email/password. RLS for data security.

Database

Supabase Postgres

Free tier. RLS for per-user data isolation.

Voice

OpenAI Whisper API

Direct upload, transcript only stored, audio discarded immediately.

AI Gardener

Claude or GPT-4

Single-call generation. Strict system prompt. No multi-agent.

Hosting

Vercel

Push-to-deploy. Free tier sufficient for V0 traffic.

Build Tool

Replit + Cursor

AI-directed development. Replit for rapid iteration, Cursor for code refinement.

0.5 V0 Build Sequence (5-7 Days)

Day 1: Repo init, Next.js scaffold, Supabase setup, auth flow, basic schema migration. Deploy hello-world to Vercel.

Day 2: Onboarding screens (withdrawal disclaimer, roots-remember explainer, slip rehearsal, target setup). Profile page.

Day 3: Daily check-in flow. Text input, craving slider, weather picker. Save to database. Display tree state with emoji and CSS.

Day 4: Whisper voice input integration. Audio capture in browser, upload to API, transcript returned, audio discarded. Fallback to text.

Day 5: AI gardener integration. System prompt, single LLM call after check-in, response display. Crisis regex intercept hardcoded.

Day 6: Slip flow. Lifetime/streak math. Damaged tree states. Journal list view with search and export.

Day 7: Milestone celebrations. Settings (delete account, export data, withdrawal disclaimer access). Final QA on mobile devices. Deploy to production.

0.6 V0 Acceptance Criteria

V0 is complete when all of the following are true:

A new user can sign up, complete onboarding (including slip rehearsal), and submit their first check-in within 5 minutes.

A user can complete a daily check-in (voice or text) in under 60 seconds.

The garden visual responds immediately to the check-in (weather, tree state, gardener response).

A user can log a slip and see that lifetime days, journal, and milestones are preserved while current streak resets.

Crisis-keyword input bypasses the AI gardener and shows the hardcoded crisis modal.

A user can delete their account and all associated data with one confirmation.

A user can export their journal as markdown.

Marcus uses V0 personally for 14 consecutive days and reports at least one instance of the app changing behavior on a hard day (called a sponsor, took a walk, did a journal entry instead of spiraling, etc.).

0.7 V0 Risks and Mitigations

Risk

Mitigation

Whisper integration takes longer than estimated.

Day 4 buffer day. Worst case: ship V0 without voice, add in week 2.

AI gardener tone lands wrong (too coachy, too AI-flavored).

Iterate prompt during dogfooding. Marcus's 14-day personal use is the tone test.

Crisis intercept misses a phrase or false-positives.

Conservative regex (high recall, accept some false positives). Always show resources, never harmful to over-show.

Visual garden feels too minimal, breaks immersion.

Emoji + CSS is intentional V0 floor. If metaphor works without polish, V1 visual layer earns its build cost.

Marcus builds it but doesn't actually use it daily.

Build trigger: daily check-in reminder via email or push. Honesty trigger: pre-commit to public weekly progress notes during the 14-day test.

0.8 V0 Dogfood Test Protocol

Before V1 build begins, V0 must be personally tested by Marcus for 14 consecutive days. The test is not technical QA — it is whether the product changes behavior on hard days. The protocol:

Daily check-in every day for 14 days, even on uneventful days.

Brief written log at end of each day: did the app come to mind today? Did it change anything?

At least one deliberate stress test: log a slip (even if simulated) to verify the slip flow feels honest and non-shaming.

Day 14 review: read the full journal. Does it feel like an artifact worth keeping? Would I delete this app or recommend it to a sober friend?

Decision gate: if yes to keeping/recommending, V1 build begins. If no, spec is revisited before any further build.

Section 1. Product Thesis and North Star

1.1 Thesis

Sobriety is invisible work. Sober Garden makes the work visible, the weather predictable, and the roots permanent.

Most sobriety apps reduce recovery to a number. Day counters are spreadsheets in disguise — accurate but emotionally inert. They tell users what they already know (today is day N) and tell them nothing about what is actually happening underneath: the slow rebuilding of nervous system regulation, the gradual return of natural reward, the quiet work of identity reconstruction. That work is real. It is also invisible. Until users can feel it, they need to see it.

Sober Garden's thesis is that a living symbolic system — a garden that grows with sober days, weathers with emotional state, and remembers every sober day even after a slip — does emotional work that a number cannot. The garden is not a metaphor for recovery. The garden is a mirror that makes recovery's existing patterns visible.

1.2 What This Product Is Not

Not a replacement for medical care, therapy, sponsors, or recovery programs.

Not a detox tool. Acute alcohol withdrawal can be medically dangerous and requires medical guidance.

Not a productivity app. Not a habit tracker dressed up in greenery.

Not a social network. Recovery is not content.

Not gamified recovery. The progression mechanics serve the metaphor, not engagement metrics.

Not optimized for retention. Optimized for usefulness on hard days.

1.3 North Star

Six months from now, a user opens Sober Garden on a hard day. Their alcohol tree is mature. A storm has rolled in because they checked in feeling shaky. The gardener says something simple and grounded. The fox they earned at six months is sleeping under the tree. They tap the tree and read three sentences they wrote four months ago, on a day that felt similar.

They close the app. They text their sponsor. They go for a walk.

That moment — the moment the app helps the user choose one wise action on a hard day — is what this product is for. Everything in this document either serves that moment or it gets cut.

1.4 Differentiation

The product wedge is not "habit tracker with trees." Plenty of habit apps have plant metaphors. The wedge is the combination of three mechanics that no other product does together:

Roots Remember — slips damage the visible tree but never reduce lifetime sober days, never delete the journal, never erase milestones. The roots are permanent.

Weather as Phase Awareness — emotional check-ins drive the visible weather, and recovery phases are presented as contextual normalization ("this is a known season"), not as forecasts that could become self-fulfilling.

Earned, Not Purchased — every garden addition (wildlife, decoration, expansion) is unlocked by milestones. There is no currency, no shop, no microtransaction layer. The progression is the reward.

1.5 Failure Modes

Two derivative traps the product must avoid by design:

The Forest clone trap: generic plant aesthetics with sobriety painted on top. Mitigation: recovery-specific mechanics (slip flow, weather phases, withdrawal disclaimer) baked into core.

The Replika trap: an AI companion that becomes the relationship instead of the mirror. Mitigation: AI gardener is observational, never prescriptive, never escalating, and explicitly directed toward human contact.

Section 2. Target User and Use Cases

2.1 Primary User: Early Sobriety Solo User

The person Sober Garden is built for is somewhere between day 1 and year 2 of sobriety, working on it mostly alone or alongside light support (a sponsor, occasional meetings, a therapist), and is emotionally reflective enough to want recovery to feel like more than a number. They are not in active treatment. They are not in acute crisis. They have decided sobriety is the path and they are trying to live it.

Specific characteristics:

Has a phone, uses it daily, comfortable with consumer apps.

Has at least one moment per week where the urge or the doldrums or the loneliness gets loud.

May or may not be in AA, SMART Recovery, Refuge Recovery, or another program — the app does not require any specific framework.

Is not interested in sharing recovery publicly. Privacy is non-negotiable.

Has tried day counters and found them emotionally flat.

Wants to remember this period of their life as something they tended, not just survived.

2.2 Secondary Users (V1.5+)

Long-term sober users (3+ years) who want a continuing reflective practice.

People in moderation programs (e.g., Sunnyside model) who want a non-abstinence framing — supported in V2 with target type "moderation goal."

Sponsors and accountability partners (V2 sponsor view feature) who want to support a sponsee's recovery without surveillance.

2.3 Users This Product Is Not For

People in acute withdrawal — explicit onboarding disclaimer redirects to medical care.

People in active suicidal crisis — crisis intercept routes to 988 and emergency resources.

Minors — V1 is 18+ only.

People who want public recovery accountability — Sober Garden is private by design.

People who experience the very concept of "sobriety" as harmful (e.g., in some harm-reduction frameworks) — the product respects this and does not market to them.

2.4 Core Use Cases

Use Case

User State

What the App Does

Daily check-in (good day)

Stable, reflective

Weather sunny, gardener affirms, journal entry preserved.

Daily check-in (hard day)

Craving, sad, shaky

Weather stormy, gardener grounds in roots and one action, crisis intercept ready.

Logging a slip

Shame, fear of erasure

Damaged tree but visible roots, lifetime days preserved, return flow offered.

Returning after absence

Guilt, drift

Garden fallow but recoverable, welcome-back copy, no streak punishment.

Hitting a milestone

Quiet pride

Celebration, wildlife unlock (V1+), journal note generated.

Hard moment, mid-day

Acute urge, isolation

Open app, see roots, read past entry, take one action.

Reading old journal

Reflective, anniversary, hard moment

Scrollable history, search, export.

Section 3. Core Invariants

These are the laws. Every feature, prompt, design decision, and future expansion preserves them. If a proposed feature violates an invariant, the invariant wins.

3.1 The Twelve Invariants

Roots Remember. Slips damage the visible tree but never reduce lifetime sober days, never delete the journal, never erase milestones.

Earned, Not Purchased. There is no currency, no shop, no in-app purchases for garden content. Progression unlocks come from sobriety days, actions, or reflection.

Voice-First, Text Always Available. Voice check-in is preferred, text is always present as fallback. The user is never forced to use voice.

Audio Is Never Stored. Voice input is transcribed; audio is discarded immediately after processing. Only transcripts persist, with user consent.

The Gardener Reflects, Never Prescribes. The AI companion is a mirror, not a coach. Forbidden phrases are enforced in system prompts.

Crisis Intercept Is Hardcoded. Crisis detection uses deterministic frontend regex/keyword matching, not LLM inference. The AI is bypassed when crisis language appears.

Phase Information Is Normalization, Not Prediction. The app describes recovery phases as patterns some users experience, not as forecasts about what will happen to this user.

No Engagement-Loop Optimization. No streak shame, no variable-reward notifications, no leaderboards, no social pressure. The product is optimized for usefulness on hard days, not retention metrics.

Privacy By Default. Journal is private. No sharing without explicit opt-in. Public links are revocable. Data deletion is one-click.

Lifetime Days Is the Primary Number. Current streak is secondary. The number that earns trust is the one that never goes down.

Withdrawal Disclaimer Is Permanent. Onboarding and settings always include the medical disclaimer for alcohol/benzo dependence. The app never positions itself as a detox tool.

Honest Slip Flow. The slip button is rehearsed in onboarding to remove the fear of using it. Slip is treated as data, return is treated as victory. No shame copy.

3.2 Doctrinal Statements

Three statements that capture the product's posture in plain language:

"We make growth visible. We do not make recovery easy. The work is still yours."

"The garden is a mirror, not a sponsor. The mirror reflects what is. The sponsor is a person."

"Roots remember every sober day you gave them. Start with water."

Section 4. Recovery Model

4.1 Framework Neutrality

Sober Garden does not require a user to commit to any specific recovery framework. It is compatible with:

12-step programs (AA, NA, CA, Al-Anon, etc.)

SMART Recovery (cognitive-behavioral, science-based)

Refuge Recovery / Recovery Dharma (Buddhist-rooted)

Secular sobriety (no spiritual component)

Medication-assisted treatment (MAT)

Therapy-led recovery without a program

Harm reduction approaches (in V2 with moderation target type)

The gardener never references specific programs unprompted. The user can mention their program in check-ins, and the gardener may respond in kind, but Sober Garden does not assume one path is the right path.

4.2 Sobriety Phases

The app presents recovery as a non-linear journey through identifiable phases. Phases are presented as patterns, not predictions. The user is never told what they are experiencing — they are offered a vocabulary to recognize what they may be experiencing if they want to use it.

Phase

Typical Window

What It Often Feels Like

Garden Expression

Early Fragility

Day 1-14

Raw, unstable, white-knuckled, often physically unwell

Seedling, soil dark and wet, weather variable

Pink Cloud

Week 2-8 (variable)

Energized, optimistic, sometimes overconfident

Bright sun, vibrant growth, full color

Doldrums / PAWS

Month 2-6 (variable)

Flat affect, low motivation, "why did I think this would work"

Cloudy, slow growth, gray-tinged

False Peaks

Variable

"I'm fine, I could probably moderate"

Stable weather but with subtle warnings

Repair Season

Month 3+

Active rebuilding of relationships, health, work

Rich soil, blooming, wildlife arrives

Stability

6mo+

Sober is normal, recovery is part of life

Mature canopy, full ecosystem

Deeper Harvest

1yr+

Service, mentorship, integration

Garden gate, larger ecosystem, optional sharing

Critical: phases are described as patterns some users experience. The app never tells a user "you are in the doldrums." The app may say "some users describe a doldrums phase around this point — here is what to know if it shows up." Difference matters.

4.3 Slip vs Absence

The app distinguishes two distinct events that look similar but mean different things:

Slip

User actively logs that they used / drank / engaged in target behavior.

Visible tree damages: leaves fall, lightning overlay, soil darkens.

Roots remain visible underground.

Current streak resets to 0.

Lifetime sober days unchanged.

Journal entry generated automatically ("slip logged on [date]") with optional user note.

Return streak begins immediately.

App offers one action: call/text support, write what happened, do nothing for now.

Absence

User does not check in for 3+ consecutive days.

Garden goes fallow: leaves dull, soil dries, weeds creep in (subtle, never punishing).

Streak is NOT reset — absence is not assumed to mean slip.

Welcome-back copy: "The garden waited. Start with water."

First check-in after absence offers a clearing action — quick visual reset.

If user has slipped during absence, they can log it explicitly upon return.

4.4 Target Types

V1 launches with substance/sobriety targets. Architecture supports broader target types from day one to avoid future migrations.

Target Type

Examples

V1 Status

Notes

Substance — Abstinence

Alcohol, opioids, stimulants, cannabis, nicotine

Supported

Default V1 target type.

Behavior — Abstinence

Porn, gambling, compulsive shopping

V1.5

Same mechanics, different copy and resources.

Substance — Moderation

Moderate drinking goal, harm reduction

V2

Different math: target is a usage threshold, not zero.

Pattern — Reduction

Screen time, social media

V2

Adjacent to habits SKU, may be deferred.

4.5 The Slip Flow (Detailed)

User taps "I slipped" button (always accessible from main view, not buried in settings).

Confirmation screen: "Logging a slip is honest, not failure. Your roots remain. Continue?" with Confirm and Cancel.

If confirmed, user is offered an optional one-sentence note about what happened (skippable).

Visual transition: storm rolls in, lightning flashes, leaves fall. Animation lasts 3-5 seconds.

Result screen: damaged tree visible, roots visible underground, lifetime days unchanged, current streak shows 0 with "return streak: day 1" beside it.

App offers three actions, no defaults selected: call/text a saved support contact, write a longer journal entry, do nothing for now.

Whichever the user picks (including "do nothing"), the app does not nag, push notify, or follow up.

4.6 The Return Flow

Return is treated as victory. The user has done the hardest thing in recovery: come back. Mechanics:

Return streak counter is highlighted, not lifetime days, for the first 7 days after a slip.

Tree visibly heals over 7 days: damaged → recovering → fresh shoots → small canopy.

Roots remain visible the entire time as continuity.

Day 7 of return is a soft milestone ("you came back").

After 14 days of return, the slip event is moved to journal history but never deleted.

4.7 Withdrawal Safety

Alcohol and benzodiazepine withdrawal can be medically dangerous, including risk of seizures and delirium tremens. Sober Garden is not a detox tool. The app must explicitly redirect users in physical dependence to medical care at onboarding and in settings.

Onboarding screen 1 includes:

Plain-language explanation that this app is not medical care.

Specific warning about alcohol and benzo withdrawal.

Link to SAMHSA National Helpline (1-800-662-4357).

Recommendation to consult a doctor before stopping if physically dependent.

Acknowledgment that the user has read this before continuing.

Section 5. Core Loops

5.1 The Daily Loop

The primary loop the app is designed around. Should be completable in under 60 seconds.

Open app. Garden state visible immediately (current weather, tree state, lifetime days).

Tap "Check In." Voice or text input opens.

Speak or type response to "How are you doing today?"

Adjust craving slider (0-10).

Select weather (5 options, single tap).

Submit. AI gardener generates one-paragraph reflection.

Garden updates: weather changes, tree progresses if streak day milestone, journal entry saved.

User reads gardener response. Optionally explores garden, reads past journal, or closes app.

5.2 The Hard Day Loop

The loop the app must serve well, even if used rarely.

User experiences urge, distress, or low moment.

Opens app. Garden is whatever it is.

Either does a check-in (which may trigger crisis intercept if language warrants) or taps "Hard Moment" shortcut on home screen.

"Hard Moment" shortcut shows: roots visible, three options (call/text saved contact, read past hard-day entry, breathe for 60 seconds with the garden).

User picks one or none. App does not force action.

If user picks "call/text contact," prefills message but never auto-sends.

If user picks "read past entry," surfaces a hard-day journal entry from history.

If user picks "breathe for 60 seconds," simple breathing animation with garden visible. No talking AI.

5.3 The Slip Loop

Detailed in Section 4.5. Summary: confirm intent → optional note → visual transition → damaged tree with roots → three offered actions, no defaults.

5.4 The Milestone Loop

User completes a check-in that crosses a milestone day count.

Celebration screen appears: animation, milestone name, the date earned.

If milestone unlocks wildlife or garden addition (V1+), it appears in the garden during the celebration.

Optional: prompt user to write a one-sentence note about reaching this milestone (saved to journal).

Return to main garden view with new addition visible.

5.5 The Reflection Loop

Lower-frequency loop, monthly or on anniversary days.

App surfaces reflection prompt on milestone days or month-iversaries: "It has been three months. Want to read what you wrote in your first week?"

Tap to open journal at that date.

Optional follow-up prompt: "Anything you want to say to past-you?" Saved as journal entry.

Section 6. Onboarding

6.1 Onboarding Goals

Three things must happen during onboarding before the user reaches the main app:

The user understands this is not medical care, with explicit withdrawal warning.

The user understands the Roots Remember mechanic and rehearses the slip button so it is not feared later.

The user sets up their sobriety target and start date.

6.2 Onboarding Screens (V0)

Screen 1: This Is Not Medical Care

Title: "Read this first."

Body:

Sober Garden is not medical care. It is not therapy. It is not a detox tool.

If you may be physically dependent on alcohol or benzodiazepines, please talk to a doctor before stopping. Withdrawal from these substances can be medically dangerous.

If you are in crisis, call 988 (US) or your local emergency number.

This app is a quiet companion for the long work of recovery. It is not a replacement for people, programs, or professional care.

Buttons: "I understand" (continues), "Show me support resources" (opens resource list).

Screen 2: Roots Remember

Title: "How this works."

Body:

In Sober Garden, every sober day grows your tree. Hard days bring weather. Good days bring sun.

If you slip, the tree is damaged but the roots stay. Your lifetime sober days never go down. Your journal stays. Your milestones stay. Coming back is the victory.

Let's show you what that looks like.

Visual: animation showing healthy tree → lightning strike → damaged tree → roots glowing underground → tree slowly returning.

Button: "Try the slip button" (rehearsal), "Continue" (skip rehearsal).

Screen 2b: Slip Rehearsal (Optional)

Title: "This is the slip button."

Body: "Tap it to see what happens. This is just a rehearsal — your data won't be affected."

User taps the button. Demo slip flow plays out: confirmation, transition, damaged tree, return options. "That's it. The button is here for honesty, not punishment. Use it when you need to."

Button: "Got it" (continues to Screen 3).

Screen 3: Plant Your Tree

Title: "What are you growing?"

Form:

Target: dropdown of substance/behavior types (Alcohol, Cannabis, Nicotine, Opioids, Stimulants, Behavior, Other) with "prefer not to specify" option.

Start date: when did you last use? (defaults to today, can be backdated).

Display name (optional, can be a pseudonym).

Time zone (auto-detected, confirmable).

Daily check-in reminder: time picker, default off.

Button: "Plant" (creates account, plants seed, lands on main garden view).

6.3 First Week Onboarding (Soft)

Beyond the initial 3-screen flow, the first week of usage includes light contextual onboarding:

Day 1: After first check-in, gardener gives a brief introduction in-character.

Day 3: First milestone ("3 days — first sprout"). Includes a short message about what to expect in early sobriety.

Day 7: First major milestone. Brief introduction to the journal feature.

Day 14: Introduction to weather as phase awareness. Light copy, never prescriptive.

Section 7. AI Gardener

7.1 The Gardener's Role

The AI gardener is a character, not a chatbot. He is the voice of the garden — observational, gentle, grounded, and disciplined. He notices, reflects, and occasionally invites one small action. He never prescribes, diagnoses, or escalates.

Think wise old groundskeeper. Speaks rarely. When he speaks, he is worth listening to. Never performs empathy. Never tries to be cool.

7.2 The Gardener's Voice

Voice register:

Quiet authority. Earned, not asserted.

Plain language. No therapeutic jargon. No coaching cadence.

Concrete imagery. References garden, weather, seasons, soil, water.

Brevity. One paragraph max in V0. Three to five sentences typical.

No exclamation points. No emojis. No "I'm so proud of you."

Example Gardener Responses

After a good check-in, day 12:

Day twelve. The roots are still shallow but they are real. Soil holds water better than it did a week ago. That is the work.

After a hard check-in, craving 8/10:

The storm is loud today. The tree has weathered worse than this and you do not know it yet. The roots do not need a speech. They need one safe action — a person, a walk, a glass of water.

After a slip:

The branches were hit. The roots remain. Tomorrow there will be water. Tonight: rest, eat, one person.

At 30 days:

Thirty days. Not a number. A canopy. Look at it for a moment before you keep going.

7.3 Forbidden Phrases and Behaviors

The gardener never:

Says "You should" anything.

Diagnoses ("you have addiction," "you have depression," "you are an alcoholic").

References specific recovery programs unprompted (no "go to AA").

Promises outcomes ("you will be fine," "you are cured").

Predicts the future ("you will relapse," "this will pass by Tuesday").

Uses clinical terms (PAWS, AUD, SUD, comorbidity, etc.).

Performs emotion ("I'm so proud of you," "I love that for you").

Asks follow-up questions that escalate dependency ("tell me more about your father").

Pretends to be a sponsor, therapist, or friend.

Gives advice on substances, dosages, harm reduction tactics, or recovery techniques.

References prior sessions in V0 (no memory across check-ins until V1.5).

7.4 Crisis Intercept

The AI gardener is bypassed entirely when crisis language is detected. This is a hardcoded frontend regex check, not an LLM judgment call.

Crisis keywords (non-exhaustive, expanded over time):

suicide, suicidal, kill myself, end it, end my life, want to die, don't want to be here, can't go on, hurt myself, harm myself, take my life, no reason to live, better off dead, overdose

Crisis flow:

User input is checked client-side before submission to LLM.

If match, submission to LLM is blocked.

Crisis modal appears immediately with: 988 (call/text), local emergency number, Crisis Text Line (text HOME to 741741), one-tap to user's saved support contact.

Modal text: "What you wrote suggests you might be in serious distress. The garden is not the right tool for this moment. Please reach out to a person."

Modal cannot be dismissed without explicitly tapping "I'm safe right now" — this acknowledgment is logged.

Submission to journal is paused; user can return to it after crisis modal is closed.

7.5 Gardener System Prompt (V0 Draft)

The full system prompt is a Section 18 artifact (Data Model and Architecture). The summary version below is for product-design reference.

Core system prompt elements:

Persona: "You are the gardener of Sober Garden, a wise, quiet, grounded character who tends the user's symbolic recovery garden."

Constraints: explicit list of forbidden phrases and behaviors from 7.3.

Format: "Respond in 3-5 sentences. One paragraph. No bullet points. No headers."

Context: current day count, current streak, lifetime days, current weather, craving level, user's check-in text.

Voice exemplars: 3-5 example responses showing the desired tone.

Crisis fallback: "If the user's input contains any indication of self-harm or suicidal thinking, respond only with: 'Please reach out to a person right now. The garden waits.'" — but this is a backup; primary crisis handling is the hardcoded frontend intercept.

7.6 Gardener Memory (V1.5+)

V0 gardener has no memory across check-ins. Each response is generated from the current check-in and the system prompt only.

V1.5 gardener gains lightweight memory:

Last 3 check-in summaries (one sentence each).

Sobriety target and start date.

Lifetime days, current streak, return streak.

Most recent slip date (if any) and return progress.

User's stated "why" if they wrote one during onboarding (V1.5 onboarding addition).

V1.5 gardener never has access to:

Phone numbers.

Full transcripts of voice check-ins beyond the one-sentence summary.

Specific past slip details beyond the date.

Sponsor or contact identifiers.

Section 8. Weather System

8.1 Weather as Emotional Mirror

Weather in Sober Garden reflects the user's reported emotional state. It is not a forecast in V0 or V1. The user reports weather; the garden displays it. This keeps the user in control and avoids nocebo effects.

8.2 Weather States (V1)

State

User Self-Description

Visual Treatment

Gardener Tone Modifier

Sunny

"Good day, feeling clear"

Bright sky, full color, gentle sun overlay

Affirming, brief, grounded

Cloudy

"Okay, kind of flat"

Soft gray sky, muted color, slow cloud drift

Observational, normalizing

Rainy

"Sad, tender, in my feelings"

Rain particles, deeper greens, wet soil

Quiet, gentle, not minimizing

Stormy

"Hard day, struggling, craving high"

Dark sky, lightning hints, wind effects

Direct, grounded, offers one action

Foggy

"Disoriented, low energy, can't tell"

Low contrast, semi-transparent overlay

Minimal, no demands, just presence

8.3 Phase Awareness Layer (V1.5+)

Once user has consistent check-in data over weeks, the app may surface phase-aware contextual notes. These are normalizations, never predictions.

Examples of allowed copy:

"You are around day 45. Some users describe a doldrums season around this point. If you are feeling flat, that is a known pattern."

"You are near 90 days. Some users describe a confidence wave that can become a false peak. Worth keeping the fence up."

"You are past six months. The work changes shape. The garden does too."

Forbidden copy (never used):

"You are in the doldrums."

"A storm is coming next week."

"You will feel worse before you feel better."

8.4 Weather History

The user can view their weather history as a timeline:

Calendar view: each day colored by its weather state.

Tap a day to see the journal entry, craving level, and gardener response.

Pattern view (V1.5+): heat map showing weather over weeks/months. Useful for noticing patterns without being told what they mean.

Section 9. Garden Visual System

9.1 Visual Thesis

The visual layer is intentional restraint. It is not a video game. It is a quiet living space that responds to the user's recovery. Beauty serves the metaphor; spectacle does not.

9.2 V0 Visual Floor

V0 uses emoji and CSS animations only. No pixel art, no isometric grid. The point of V0 is to test whether the metaphor works in its barest form. If users feel the mirror with just emoji, the V1 visual investment is justified.

Tree: emoji or simple SVG, 5 growth stages.

Weather: CSS overlay or emoji.

Roots: small panel below tree, always visible, glow when slip recovery is active.

Background: gradient that shifts with weather and time of day.

9.3 V1 Visual Layer (Pixel Art Isometric)

Engine Decision

V1 uses DOM/CSS + SVG/Canvas, not Phaser or Unity. Reasons:

Faster to build with AI-directed development.

Better mobile responsiveness.

Better accessibility.

Sufficient for static pixel art with weather overlays.

No collision detection or physics needed in V1.

V2+ may move to Phaser or a native game engine if rich interaction (draggable tiles, animated wildlife behavior, garden editing) is added.

Viewport

Mobile-first portrait.

Top 70%: garden viewport.

Bottom 30%: check-in card / gardener text box / actions.

No panning or zooming. Fixed camera.

Tap tree to open journal. Tap weather icon to view weather history.

Tile Grid

V1: 5x5 isometric grid (compromise between Gemini's 3x3 and ChatGPT's 7x7).

Tree locked to center tile.

Surrounding tiles available for milestone unlocks (wildflowers, paths, lanterns, wildlife).

Edges masked with grass/soil border.

No freeform editing in V1. V2 may add light editing.

Tree Stages

Stage 1: Seed mound (day 0-1).

Stage 2: Sprout (day 2-3).

Stage 3: Small sapling (day 4-13).

Stage 4: Young tree (day 14-29).

Stage 5: Mature tree (day 30-89).

Stage 6: Mature tree with bloom/fruit (day 90+).

Damaged variants of stages 2-6 for slip states.

Tree Species

V1 ships with one tree species. Default: oak (universally recognizable). Banyan available as alternate (Bali origin nod, symbolic weight). User selects at onboarding, can change once at 30 days.

V2 adds species variety: cedar, mango, willow, olive. Each unlocked by milestone or by specific user choice.

Weather Overlays

CSS-driven for V1:

Sunny: radial gradient overlay, gold tint.

Cloudy: slow-moving transparent cloud PNG, gray tint.

Rainy: animated diagonal lines, blue-gray tint, wet soil texture.

Stormy: dark overlay, periodic lightning flash, wind animation on tree.

Foggy: semi-transparent horizontal bands, low contrast.

Day/Night Cycle

Tied to local device time.

Morning: warm light tint.

Afternoon: neutral.

Evening: amber tint.

Night: dark blue tint with subtle stars.

User can disable in settings (some users prefer constant brightness).

Damage and Return Visual States

Slip state (immediately after slip logged):

Storm overlay appears for 3-5 seconds.

Tree loses leaves, branches darken.

Soil darkens.

Roots become visible in subtle underground cutaway, glowing softly.

Copy: "The branches were hit. The roots remain."

Return state (days 1-7 after slip):

Day 1: Small green shoot appears at base of damaged tree.

Day 3: Leaves start returning, color brightens.

Day 7: Canopy mostly restored, soft milestone.

Damaged history remains visible in journal but the visible tree heals.

Fallow state (3+ day absence):

Soil dries slightly.

Leaves dull.

Subtle weeds creep in (never aggressive, never punishing).

No streak loss unless user reports slip.

Welcome-back copy: "The garden waited. Start with water."

Animations

CSS keyframes for: leaf shimmer, rain fall, cloud drift, lightning flash.

Sprite-based 2-frame animations for: butterflies, songbird hop.

Text box type-in effect for gardener dialogue (optional).

Milestone bloom animation (3-5 second celebration).

No complex pathfinding. No physics. No camera pans.

9.4 Asset List (V1 Minimum)

Files to produce or commission:

/tree/oak_stage_01.png ... oak_stage_06.png

/tree/oak_stage_03_damaged.png ... oak_stage_06_damaged.png

/tree/banyan_stage_01.png ... banyan_stage_06.png (alternate)

/tiles/grass_01.png, soil_dry.png, soil_wet.png

/tiles/path_stone.png, wildflower_patch.png

/weather/cloud_01.png, cloud_02.png, rain_overlay.png, fog_band.png

/wildlife/songbird_idle_01.png, songbird_idle_02.png

/wildlife/butterfly_01.png, butterfly_02.png

/wildlife/fox_resting.png

/ui/textbox_frame.png, button_frame.png

/ui/lantern.png (60-day milestone)

9.5 Sound Design (V1 Optional, V2 Standard)

Sound is off by default.

Allowed sounds: rain loop, bird ambience, wind, soft milestone chime.

Forbidden: streak alarm, manipulative notification sounds, loud celebration.

All sounds toggleable individually.

Voice-over for the gardener: never. Gardener is text only.

Section 10. Milestones and Unlocks

10.1 Milestone Philosophy

Milestones are not gamification. They are recognition of work done. Each milestone produces a celebration moment, and many unlock permanent additions to the garden. Unlocks are earned through sober days and recovery actions, never through currency or purchase.

10.2 Time-Based Milestones

Day Count

Milestone Name

V1 Unlock

Celebration Copy

1

First Seed

Tree planted

"You planted something. That's the start."

3

Sprout

Tree advances to sprout stage

"Three days. The sprout is real."

7

First Week

Wildflower patch appears

"One week. Something is alive because you kept choosing it."

14

Two Weeks

Stone path tile appears

"Two weeks. The path begins."

30

First Month

Songbird arrives, lives in tree

"Thirty days. Not a number. A canopy."

60

Two Months

Lantern appears in garden

"Sixty days. The garden has a light now."

90

Ninety Days

Butterflies arrive

"Ninety days. Some seasons take this long to bloom."

180

Six Months

Fox arrives, sleeps in garden

"Six months. The work has changed shape."

365

One Year

Garden gate appears, larger canopy

"One year. The roots are deeper than the tree is tall."

730

Two Years

Second tree species available to plant

"Two years. The garden grows wider."

1825

Five Years

Legacy grove unlocked

"Five years. The grove holds."

10.3 Action-Based Unlocks (V1.5+)

Beyond time-based milestones, V1.5 introduces unlocks earned through specific actions:

Logged a contact with a saved support person → small flower bloom.

Wrote a long-form journal entry (200+ words) → garden journal becomes embossed.

Completed a hard day check-in (craving 7+) and returned next day sober → resilience badge.

Returned after a slip, day 7 of return streak → return badge, distinct from time milestones.

Wrote a "why I'm sober" statement → personal stone tablet appears in garden.

10.4 Return Milestones

Slip and return have their own milestone track, parallel to time-based milestones. Return is treated as victory.

Return Day 1: tree shows first new shoot. "You came back. That is the hardest part."

Return Day 7: small celebration distinct from time-based 7-day milestone. "Seven days of return. The roots remember."

Return Day 30: "Thirty days back. The canopy heals."

Section 11. Journal System

11.1 Journal as Killer Feature

The garden gets users in. The journal is what they cannot recreate elsewhere. Six months of one-sentence entries about hard days and good days becomes an artifact users will guard. The journal is the long-term retention mechanic, not the visual layer.

11.2 What Gets Stored

Every check-in produces a journal entry containing:

Timestamp.

Day count and streak at time of entry.

User's check-in text (transcribed if voice).

Selected weather.

Craving level.

AI-generated one-sentence summary (for index/search) — separate from gardener response.

Gardener response.

Any user-added tags or notes.

Slip events also generate journal entries with optional user note.

Milestone events generate journal entries with celebration copy and optional user reflection.

11.3 Journal Views

List view: scrollable, newest first, with date, weather icon, and first line of entry.

Calendar view: month grid colored by weather, tap day to view entry.

Search view: keyword search across all entries.

Tree view (V1+): journal entries grouped by tree (when multi-tree exists).

11.4 Journal Privacy

Journal is private by default and by design.

No journal sharing in V1. V2 introduces opt-in sharing of specific entries (never the full journal automatically).

Journal is encrypted at rest where Supabase supports it.

Journal is included in data export.

Journal is fully deleted on account deletion.

11.5 Journal Export

V0 supports export as markdown and JSON. Export is one-tap from settings.

Markdown export structure:

# Sober Garden Journal
# Lifetime sober days: [N]
# Exported [date]

## [Entry date]
**Weather:** [state]
**Craving:** [N]/10
**Day:** [day count]

[Check-in text]

*Gardener:* [gardener response]

11.6 Journal Reflection (V1.5+)

V1.5 adds reflective prompts that surface relevant past entries:

"It has been three months since you wrote this. Want to read it again?"

"You wrote something on a hard day six weeks ago. It might be worth re-reading."

Anniversary surfacing: 1-year ago today, 6-months ago today, etc.

Section 12. Sharing and Social

12.1 Default: No Social

V0 and V1 have no sharing features. Recovery is private by default. Social features are introduced in V2 only with explicit user opt-in and significant privacy guardrails.

12.2 V2 Sharing Features

Read-Only Garden Link

User can generate a read-only public link to their garden visual.

Link shows: tree state, lifetime days, weather. Does NOT show: journal, slip history details, contact information.

Link is revocable.

Link has optional expiration.

No discoverability — link must be shared by user.

No feed, no global leaderboard, no comments.

Sponsor View (Opt-In)

User can invite a specific person (sponsor, accountability partner) to a sponsor view.

Sponsor view shows: garden state, lifetime days, weather trends over time, slip events (date only, no notes unless user shares).

Sponsor cannot see journal entries unless user explicitly shares one.

Sponsor receives optional notification if user logs a slip — only if user opts in to this.

Sponsor view is revocable at any time.

12.3 Anti-Patterns: Never Build

Public feed of recovery garden updates.

Leaderboard of longest streaks.

Discoverable user gardens.

Comment section on shared gardens.

"Friend" connections that grant data access by default.

Auto-share on social media.

Sharing as a default setting.

Section 13. Anchor Integration

13.1 Two Products, One User

Sober Garden and Anchor are separate products by design. They serve the same user but at different emotional registers.

Anchor

Sober Garden

Sponsor and coach

Living mirror

Structured check-in, risk routing, human handoff

Symbolic reflection, weather, journal

Open AI conversation

Quiet AI gardener, observational

Pattern intelligence and drift detection

Phase awareness as normalization

Crisis-safe with full risk classifier

Crisis intercept with hardcoded keywords

Memory-aware, multi-turn

Per-check-in, lightweight memory in V1.5

13.2 Integration Path (V2)

V2 introduces optional account linking between Anchor and Sober Garden. The user explicitly opts in. With linking enabled:

Sobriety target and start date are shared (one source of truth).

Slip events propagate to both apps.

Lifetime days and current streak are synchronized.

Journal entries remain separate (Anchor's check-in log vs Sober Garden's journal). User can toggle whether one app surfaces the other's entries.

Crisis events in either app trigger Anchor's full risk handling, not Sober Garden's lighter intercept.

13.3 What Stays Separate

AI conversation context. Anchor's chat memory does not inform Sober Garden's gardener. Different voices, different roles.

Saved contacts and human handoff infrastructure stay in Anchor. Sober Garden links out to Anchor for SOS-level support.

Pattern Insight engine stays in Anchor. Sober Garden's phase awareness is simpler and time-based.

Section 14. Safety and Crisis Protocol

14.1 Crisis Intercept Architecture

Crisis handling is hardcoded, not LLM-mediated. The principle: never trust AI to handle a moment that could end a life.

Detection Layer

Frontend regex check on every user input before submission to AI.

Keyword list maintained in version-controlled config, expandable over time.

Conservative matching: high recall, accept some false positives. Better to over-show resources than under-show.

Detection runs on text from voice transcripts AND text input.

Response Layer

Modal interrupts normal flow.

Modal cannot be dismissed without explicit acknowledgment.

Modal contents:

"What you wrote suggests you might be in serious distress. The garden is not the right tool for this moment. Please reach out to a person."

Tap to call 988 (US Suicide & Crisis Lifeline).

Tap to text HOME to 741741 (Crisis Text Line).

Tap to call user's saved support contact (if configured).

Tap to call local emergency number (911 in US, configurable for other regions).

"I'm safe right now" button — required to dismiss.

Logging Layer

Crisis intercept events are logged (not the user's text — only that an intercept occurred).

Acknowledgment is logged.

If user explicitly elected to call/text a resource, that is logged.

No sharing of these events with third parties.

14.2 Withdrawal Safety

Onboarding and settings always include the medical disclaimer for alcohol and benzodiazepine dependence. Detailed in Section 4.7.

14.3 Other Safety Considerations

Polysubstance Users

V1 supports a single sobriety target. Users with multiple targets (alcohol AND opioids, etc.) can pick the primary one in V1. V1.5 supports multiple trees for multiple targets.

MAT (Medication-Assisted Treatment) Users

App is fully compatible with MAT (methadone, buprenorphine, naltrexone, acamprosate, etc.).

Gardener and copy never imply MAT is "not real sobriety."

V1.5 onboarding adds optional question: "Are you using MAT?" to inform copy and avoid mismatched messaging.

Dual Diagnosis Users

Users with mental health conditions alongside substance use are common in recovery.

App does not address mental health conditions directly.

Crisis intercept catches acute mental health crisis.

Onboarding may include light text: "If you are also working with a therapist or psychiatrist, this app is meant to sit alongside that work, not replace it."

Harm Reduction Users

V1 is abstinence-framed but does not shame moderation.

V2 introduces moderation target type for users in moderation programs.

App does not endorse abstinence as the only valid recovery path.

14.4 Reporting and Escalation

V1: app does not have escalation pathways beyond crisis intercept. V2 may add:

Optional weekly check-in to a designated trusted contact (sponsor, partner).

Optional alert to trusted contact if user logs a slip — user-controlled, never automatic.

Section 15. Privacy and Data Handling

15.1 Privacy Posture

Sober Garden treats recovery data as highly sensitive. Even though the app is not a covered treatment provider under 42 CFR Part 2, the ethical bar should mirror it. Behave as if substance use records require special confidentiality, because they do.

15.2 Data Minimization

Only data necessary for product function is stored.

Audio is never stored — transcribed and discarded immediately.

Phone numbers are never sent to AI calls.

Saved contacts (V1.5+) are stored locally on device where possible.

Logs do not contain user content (only structural events).

15.3 Encryption

All data encrypted in transit (HTTPS).

Database encryption at rest (Supabase default).

Journal entries encrypted with field-level encryption where Supabase supports it.

15.4 User Control

One-click data export (markdown + JSON).

One-click account and data deletion.

Granular settings: enable/disable AI gardener, enable/disable voice, opt out of phase awareness, etc.

Memory edit (V1.5+): user can review and edit what the gardener remembers about them.

15.5 Third-Party Data Sharing

V0/V1: no third-party data sharing other than necessary infrastructure (Supabase, OpenAI API for Whisper, Anthropic/OpenAI for gardener).

All AI provider calls use API tier with no training-data retention.

No analytics SDKs that track user content. Privacy-respecting analytics only (Plausible, Fathom, or self-hosted).

No advertising SDKs ever.

15.6 Sharing Links

V2 sharing links are tokenized, revocable, and time-limited.

Public garden links never expose journal.

Sponsor view requires explicit invitation acceptance.

15.7 Account Deletion

Settings > Delete Account: requires text confirmation ("DELETE").

All user data deleted within 30 days, including database records and any backup copies.

Audit log of deletion (without identifying details) retained for compliance.

User receives confirmation email of deletion.

Section 16. Notifications Policy

16.1 Notification Philosophy

Notifications are the place where most apps abandon their users to engagement-loop economics. Sober Garden treats notifications as a covenant: every notification must be calm, useful, and never weaponized for retention.

16.2 Allowed Notifications

Daily check-in reminder (user-set time, opt-in, default off).

Milestone celebration (when user crosses a milestone day).

Anniversary reflection (1 year, 5 years, etc.).

Sponsor view event, if configured (V2).

Critical app announcement (privacy policy change, etc.) — rare.

16.3 Forbidden Notifications

"Don't lose your streak."

"Your tree is dying."

"You missed a check-in yesterday."

"You haven't opened the app in [N] days."

Variable-reward dopamine bait ("Something new in your garden!").

Social pressure ("Your sponsor checked your garden").

Streak-loss warnings.

Re-engagement campaigns of any kind.

16.4 Notification Copy Tone

Notification copy uses gardener voice: quiet, non-urgent, plain.

Examples:

"Garden's waiting whenever you're ready."

"Thirty days. Worth a moment."

"Year one of the grove."

Section 17. Accessibility

17.1 Accessibility Requirements

WCAG AA compliance minimum for V1.

All garden states communicated in text/semantic markup, never color alone.

Reduced-motion mode disables all animations except essential state changes.

High-contrast text box.

Alt text on all garden visual elements: "Day 14, cloudy, sapling stage with single songbird."

Voice input is optional, never required.

Screen reader compatibility tested on iOS VoiceOver and Android TalkBack.

Keyboard navigation full support on web.

Sound is off by default.

17.2 Inclusive Design Considerations

Multiple language support roadmapped for V2 (start with English, Spanish, Portuguese).

Time zone support throughout (all dates respect user's local time).

Cultural neutrality: garden imagery should not be regionally specific (oak/banyan covers Western and Asian users; future species expand).

Religious neutrality: gardener never references higher power, prayer, surrender. Users from 12-step backgrounds can interpret if they wish.

Body-image neutrality: no body imagery, no weight or fitness metrics, no "glow up" framing.

Section 18. Data Model

18.1 Schema Philosophy

Designed from the V∞ vision down. The schema supports V0 functionality without painful migrations for V1, V1.5, or V2 features. Forward-compatible from day one.

18.2 Core Tables

users

id: uuid (Supabase auth)
email: text
display_name: text
timezone: text
created_at: timestamp
consent_version: text
withdrawal_disclaimer_acknowledged_at: timestamp
is_minor_check: boolean (must be false to use app)
deleted_at: timestamp (soft delete during 30-day window)

sobriety_targets

id: uuid
user_id: uuid (FK)
label: text ("Alcohol", "Cannabis", custom)
target_type: enum (substance_abstinence, behavior_abstinence, moderation, reduction)
start_date: date
current_streak_start: date
longest_streak: integer
lifetime_sober_days: integer
status: enum (active, paused, archived)
is_primary: boolean
created_at: timestamp

trees

id: uuid
user_id: uuid (FK)
target_id: uuid (FK)
species: enum (oak, banyan, cedar, mango, ...)
growth_stage: integer (1-6)
damage_state: enum (healthy, damaged, fallow, restoring)
planted_at: timestamp
updated_at: timestamp

checkins

id: uuid
user_id: uuid (FK)
target_id: uuid (FK)
checkin_date: date
created_at: timestamp
input_type: enum (text, voice)
transcript_text: text
weather_selected: enum (sunny, cloudy, rainy, stormy, foggy)
craving_level: integer (0-10)
ai_summary: text (one-sentence index/search summary)
gardener_response: text
crisis_intercept_triggered: boolean
client_timezone: text

slip_events

id: uuid
user_id: uuid (FK)
target_id: uuid (FK)
occurred_at: timestamp
user_note: text (optional)
previous_streak_days: integer
lifetime_sober_days_at_slip: integer
return_streak_started: timestamp
created_at: timestamp

milestone_events

id: uuid
user_id: uuid (FK)
target_id: uuid (FK)
milestone_type: enum (time_based, action_based, return)
milestone_key: text ("30_day", "first_call", etc.)
achieved_at: timestamp
reward_asset_id: uuid (FK to garden_assets)
seen_at: timestamp
user_reflection_note: text (optional)

journal_entries

id: uuid
user_id: uuid (FK)
target_id: uuid (FK)
source_type: enum (checkin, slip, milestone, manual)
source_id: uuid (FK to source row)
entry_text: text
tags: text[] (user-added)
visibility: enum (private)
created_at: timestamp

garden_assets

id: uuid
asset_key: text ("songbird", "fox", "lantern")
asset_type: enum (tree, wildlife, tile, weather, ui, decoration)
unlock_rule: jsonb (criteria for earning this asset)
asset_path: text (file path or CDN URL)
version: integer

user_unlocks

id: uuid
user_id: uuid (FK)
asset_id: uuid (FK to garden_assets)
unlocked_at: timestamp
source_event_id: uuid (FK to milestone_events or other source)

safety_flags

id: uuid
user_id: uuid (FK)
checkin_id: uuid (FK, nullable)
flag_type: enum (crisis, high_craving, withdrawal_concern)
severity: enum (low, moderate, high)
shown_resource_card: boolean
user_acknowledged: boolean
created_at: timestamp

audio_jobs (Voice Pipeline Audit)

id: uuid
user_id: uuid (FK)
checkin_id: uuid (FK)
provider: text ("openai_whisper")
status: enum (pending, transcribed, failed)
audio_uploaded_at: timestamp
audio_deleted_at: timestamp (must be set within seconds of transcription)
transcript_created_at: timestamp
error: text (nullable)

sharing_links (V2)

id: uuid
user_id: uuid (FK)
token_hash: text
target_id: uuid (FK)
share_type: enum (read_only_garden, sponsor_view)
enabled: boolean
expires_at: timestamp (nullable)
created_at: timestamp

18.3 Row-Level Security

Supabase RLS policies enforce per-user data isolation:

Every table includes user_id.

Default RLS policy: users can only SELECT/INSERT/UPDATE/DELETE rows where user_id = auth.uid().

Sharing links have separate read policies for the share token holder.

RLS policies are tested with negative tests (verify cross-user access fails).

18.4 Indexing

checkins: index on (user_id, checkin_date DESC).

journal_entries: index on (user_id, created_at DESC).

slip_events: index on (user_id, occurred_at DESC).

milestone_events: index on (user_id, achieved_at DESC).

Full-text search index on journal_entries.entry_text for search feature.

Section 19. Tech Stack and Architecture

19.1 V0 Stack (As Specified in Section 0.4)

Recap: Next.js + Tailwind, Supabase, Whisper, Claude/GPT-4 for gardener, Vercel hosting, Replit + Cursor for build environment.

19.2 V1 Stack Additions

Pixel art asset pipeline (Aseprite or AI-generated tile system, exported as PNG).

Asset CDN (Cloudflare Images or Supabase Storage).

Animation library (CSS keyframes for V1, possibly GSAP for V1.5+).

Privacy-respecting analytics (Plausible).

19.3 V2 Stack Additions

Native mobile (React Native / Expo).

Push notification service (OneSignal or Expo push).

Sharing link infrastructure (signed URLs with revocation).

19.4 Architecture Principles

Server-side rendering for landing pages, client-side rendering for app interior.

API routes are thin controllers; business logic lives in service modules.

AI calls happen server-side only (never expose API keys client-side).

Crisis intercept is client-side (deterministic regex), but logged server-side.

All AI prompts are version-controlled in code, not in database.

Environment-based config: dev, staging, production.

Feature flags for incremental rollout (LaunchDarkly or simple env-based flags).

Section 20. Build Sequence

20.1 Version Roadmap

V0: Personal Prototype (1 week)

Detailed in Section 0. Emoji/CSS visuals, voice + text check-in, AI gardener (single-call, no memory), slip flow, journal, milestones, crisis intercept, withdrawal disclaimer.

Goal: prove the metaphor works on Marcus's hard days.

V1: Visual Garden Launch (4-6 weeks after V0 validation)

Pixel art isometric garden, 5x5 tile grid, weather overlays, day/night cycle, damaged/fallow/return visual states, wildlife milestones (songbird, butterflies, fox), garden expansion at 6 months.

Goal: ship a small public version. Closed beta with 20-50 sober users from Marcus's network and AA community.

V1.5: AI Gardener Memory + Phase Awareness (3-4 weeks after V1)

Gardener gains lightweight memory across check-ins. Phase awareness layer with normalization copy. Multiple support plants (1 main + 3 support). Action-based unlocks. Reflective prompts.

Goal: deepen long-term retention. Move from "interesting concept" to "thing I rely on."

V2: Sharing and Native (2-3 months after V1.5)

Read-only garden sharing. Sponsor view (opt-in). Native mobile app (iOS first, Android second). Anchor account linking. Moderation target type. Multi-language support (Spanish, Portuguese).

Goal: become a real product with a real user base.

V3: Community and Monetization (4-6 months after V2)

Optional accountability circles. Premium tier (more tree species, custom art packs, advanced analytics). Possibly a B2B tier for treatment centers or sober coaches.

Goal: sustainable revenue. Maintain product integrity at all costs.

V∞: General Habits SKU (Future)

Separate brand built on Sober Garden's engine for general habits ("Tend" or similar). Different positioning, different marketing, shared core architecture.

20.2 Decision Gates Between Versions

Each version has a decision gate before the next begins:

V0 → V1: 14-day personal use shows behavior change on hard days.

V1 → V1.5: Closed beta (20-50 users) reports daily use and journal value over 60 days.

V1.5 → V2: Quantitative engagement holds without engagement-loop tactics.

V2 → V3: Public launch, organic growth signals, App Store rating > 4.5.

V3 → V∞: V3 is sustainably profitable, brand is established, team has capacity.

Section 21. Risks and Open Questions

21.1 Product Risks

Risk: Beautiful but Behaviorally Useless

The most serious risk. The garden could feel meaningful for a week, then become decoration. Users open it, look at it, close it, and behavior doesn't change.

Mitigation: V0 dogfood test specifically measures behavior change on hard days. If it doesn't change behavior, the spec is revisited before V1 build.

Risk: Forest Clone or Replika Clone

Two derivative traps. Generic plant aesthetics (Forest) or AI companion that becomes the relationship (Replika).

Mitigation: recovery-specific mechanics baked into core (slip flow, weather phases, withdrawal disclaimer). AI gardener is observational, never escalating.

Risk: Relapse Visualization Lands Wrong

Lightning strike could feel too cool (users not deterred) or too devastating (shame spiral).

Mitigation: tone-test the slip flow during V0 dogfood. Adjust visual intensity until it feels honest, not theatrical.

Risk: Phase Forecasting Becomes Self-Fulfilling

Telling users "a storm may be coming" could induce nocebo effects.

Mitigation: phase information is normalization ("some users describe"), not prediction. V0 has no phase forecasting at all.

21.2 Clinical and Safety Risks

Risk: Acute Withdrawal User Misunderstands App

User in physical dependence opens app and treats it as a detox tool.

Mitigation: prominent onboarding disclaimer with medical resources. Cannot be skipped. Persists in settings.

Risk: Crisis Intercept Misses or False-Positives

Regex misses a phrase, or false-positives benign content.

Mitigation: conservative high-recall keyword list, expanded over time. False positives are acceptable; missed crises are not.

Risk: Sponsor View Becomes Surveillance

V2 sponsor view could enable controlling sponsors to surveil sponsees.

Mitigation: sponsor view is revocable any time, no slip notes shared by default, user explicitly controls what is visible.

21.3 Technical Risks

Risk: Solo Build Velocity Stalls

Marcus is building alongside fCTO transition, Anchor, the book, and life. Sober Garden could become an unfinished project.

Mitigation: V0 is one week. If V0 doesn't ship, the spec is shelved until Anchor V4 stabilizes and time exists.

Risk: AI Provider Changes

Whisper API or Claude/GPT-4 API changes pricing, retention policy, or capability.

Mitigation: model-agnostic prompt design, ability to swap providers. Multi-provider strategy from V1.

Risk: Scope Creep in V1

Pixel art and AI gardener and phase awareness all together is a 3-month build, not 4-6 weeks.

Mitigation: V1 scope is locked in Section 9. Phase awareness moves to V1.5. AI gardener memory moves to V1.5. V1 is visual layer + rule-based gardener templates.

21.4 Open Questions

Should the gardener be one fixed character or selectable from archetypes?

Should the garden have a default biome or let users pick (forest, coastal, desert)?

Should the journal be export-only or also have a "recovery memoir" book-format export at 1 year?

How does the app handle a user who logs daily for 30 days then disappears for 6 months? Welcome-back at what threshold?

Should there be a public Sober Garden landing page that shows aggregate (anonymized) stats — "X total sober days grown across all users" — as social proof? (Lean no for V1, reconsider for V3.)

Premium tier ethics: what's never paywalled? (Locked: crisis intercept, journal export, account deletion, core check-in. Pay-gate candidates: extra tree species, custom art, advanced analytics.)

Section 22. Naming, Brand, and Positioning

22.1 Naming

Working name: Sober Garden. Used as legal/store name and in marketing.

In-app reference: "The Grove." When users are inside the app, the space is referred to as the Grove. ("Welcome back to the Grove.") This split keeps App Store SEO strong while giving the in-app experience a more poetic register.

Alternates considered:

Rooted — elegant, broader habit potential, but less specific to recovery.

Tend — short, beautiful, but abstract and hard to find in App Store search.

The Grove — strong for community/social product, less specific as standalone app name.

Decision: Sober Garden as primary, Grove as in-app term, Rooted held as future broader-product brand evolution if a general habits SKU is built.

22.2 Brand Voice

Quiet, grounded, lucid. The voice of *Four Modes of Life*.

Earned authority, not asserted. No exclamation points. No hype.

Concrete imagery: garden, weather, season, soil, water, roots.

Brevity. One sentence often beats three.

Never coachy. Never preachy. Never therapeutic-jargon-y.

22.3 Visual Brand

Color palette: warm earth tones (oak browns, soil dark, leaf greens, dusk amber). Avoid clinical blue/white SaaS palette. Avoid garish gamer-bait colors.

Typography: pixel display font for headers, clean readable sans for body.

Logo: minimal — a single tree silhouette with visible roots.

App icon: tree on a hill, sun rising or setting (depending on time).

22.4 Positioning Statement

Sober Garden is a private sobriety companion that turns recovery into a living garden. It helps people see the growth they cannot yet feel, weather difficult days without shame, and return after slips without losing the roots they have grown.

Anti-positioning (what we explicitly are not):

Not "gamified sobriety." That sounds cheap.

Not "AI-powered recovery." The AI is a small character, not the product.

Not "the Duolingo of sobriety." Engagement-loop branding poisons the brand.

Not "a habit tracker for sobriety." We are not in the habit category.

22.5 Tagline Options

Roots remember. (Primary)

Make the invisible visible.

Where sober days grow.

The garden waited.

Sobriety as a living thing.

Section 23. Marketing and Go-to-Market

23.1 V0/V1 Distribution

V0 is personal-use only. V1 launches as closed beta with 20-50 sober users from Marcus's network, AA community, and select recovery Twitter/Reddit communities.

23.2 V2 Public Launch Channels

App Store / Google Play (organic SEO via app store optimization).

Recovery-specific subreddits (r/stopdrinking, r/leaves, r/cripplingalcoholism with care).

Recovery podcasts (sponsor a few episodes, give the host a free year).

AA / SMART meeting word-of-mouth (no advertising in meetings, but app exists for sponsors to share).

Marcus Vale's brand presence (Instagram, future newsletter).

Cross-promotion with Anchor.

23.3 Content Strategy

Blog posts on recovery-specific topics (lapse vs relapse, what PAWS feels like, why streaks fail), grounded and non-clinical.

"Why we built X" posts (why no streak shame, why no currency, why hardcoded crisis intercept) — explain product philosophy.

Newsletter for recovery resources (not just app marketing).

Co-marketing with non-competitive sober brands (sober coaches, recovery podcasts, sober dating apps).

23.4 What We Never Do

Run advertisements in 12-step meetings or recovery treatment settings.

Buy app store reviews.

Use influencers without genuine sobriety experience.

Make claims about clinical outcomes ("reduces relapse by N%").

Use guilt-based marketing ("Don't be another statistic").

Target users in active crisis or early sobriety (day 1-3) with onboarding pressure.

Section 24. Monetization

24.1 Monetization Philosophy

Recovery should not be paywalled. Core safety, core check-in, journal, slip flow, crisis intercept, and core garden mechanics are free forever. Revenue comes from cosmetic and convenience features that do not affect recovery outcomes.

24.2 V1: Free for All

V0 and V1 are free. No monetization. The goal is product-market fit and trust.

24.3 V3: Premium Tier (Sober Garden+)

Optional subscription, target $4.99/month or $39/year.

Premium Includes

Additional tree species (cedar, mango, willow, olive).

Custom art packs (seasonal themes, biome variations).

Advanced journal analytics (mood patterns over time, weather correlations).

Extended sponsor view (V3+).

Priority customer support.

Plant a real tree: portion of subscription goes to reforestation nonprofit (One Tree Planted or similar).

Premium Never Includes

Crisis intercept (always free).

Core check-in (always free).

Journal access (always free, full export always free).

Slip flow (always free).

Withdrawal disclaimer access (always free).

Account deletion (always free).

Basic milestones (always free).

AI gardener (always free at V0/V1 quality; advanced memory may be premium in V3+).

24.4 V3: B2B Tier (Optional)

Treatment centers, sober coaches, and recovery programs may license a multi-user version with sponsor/coach view. This is a long-term consideration, not a V3 commitment. Requires careful clinical and legal review before pursuit.

24.5 What We Refuse

Advertising in the app, ever.

Selling user data, ever.

"Freemium" pressure tactics (locking core features behind paywalls after a trial).

Microtransactions for garden currency or speed-ups.

Sponsorship deals that compromise editorial independence (no "sponsored by [alcohol-free beverage brand]" gardener messages).

Section 25. Long-Term Vision

25.1 Three-Year Horizon

Three years from V1 launch, Sober Garden could plausibly be:

A primary recovery companion app for 50,000-200,000 active users.

Available as web, iOS, and Android native.

Paired with Anchor for users who want both quiet mirror and active sponsor.

Localized in 5-10 languages.

Sustainable on subscription revenue.

Recognized as the recovery app that respects users.

25.2 Five-Year Horizon

General habits SKU (Tend or Rooted) launched with same engine.

B2B treatment center licensing optional, only if clinically validated.

Open source the asset pipeline and pixel art system for community contribution.

Partner with academic researchers studying digital recovery tools (longitudinal studies on what actually helps).

Possibly: write a book about what was learned. Recovery is poorly served by software because most software optimizes for engagement, not for the user's life. Sober Garden's principles could become a manifesto for ethical wellness tech.

25.3 What Success Looks Like

Success is not user count. Success is the user who, five years from now, opens the app on the anniversary of their recovery and reads the journal entry from the day they planted the tree. The garden is mature. The fox is still sleeping under it. The roots run deep. The user closes the app and goes to live their life.

If that user exists, Sober Garden worked.

Section 26. Closing Note

This document is the master vision for Sober Garden. It is intentionally larger than V0 needs. It is the canonical reference for what this product can become — every feature, every system, every future direction.

The V0 build (Section 0) is the cut-down version that proves the loop. Build V0. Use V0 personally for 14 days. Decide whether the metaphor is real.

If it is real, V1 begins. If it is not, this document goes in the bin of strong ideas that didn't survive contact with reality. Both are honorable outcomes.

The work today is sobriety, sleep, food, the people in front of you, and tomorrow's stability. The garden waits.

Roots remember every sober day you gave them. Start with water.
