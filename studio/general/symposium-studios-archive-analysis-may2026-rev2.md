---
title: "Symposium Studios Archive Analysis May2026 Rev2"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/Symposium_Studios_Archive_Analysis_May2026_Rev2.docx"
status: archive
privacy: private/internal
tags:
  - archive
---

# Symposium Studios Archive Analysis May2026 Rev2

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
SYMPOSIUM STUDIOS

Archive Analysis and Post-Anchor Prioritization

May 12, 2026  |  Rev. 2  |  Charlie / Eagle Rocket LLC  |  Internal Reference

This document captures the full strategic read of the Symposium Studios folder and Software Projects (pre-Symposium) archive uploaded on May 12, 2026. It covers what is in the folders, what has legs, a ranked post-Anchor build sequence, and two critical upstream actions that must happen before the next major build phase begins.

Rev. 2 changes: V5.4 polish no longer blocks mobile; “web core complete” is the new gate. The personal-agent layer is referred to as the Personal Agent Substrate (not Hermes) until the verification spike resolves. Sublet Radar must run a manual validation phase before any substrate-based build. Ship-status claims for individual surfaces softened to avoid making the archive doc a false source of truth.

1. What Is in the Two Folders

Symposium Studios

The Symposium folder is the active studio. Most of its mass is Anchor. The genuinely new material worth attention is the Directed Emergence theory doc and the Hermes MVP spec.

Item

What it is

Status

Anchor (all versions)

Production sobriety app. V5 roadmap, V4.1 Practice spec, active directives, design audits, builder's log, Expo conversion guide.

Active. Primary product.

NYC Sublet Radar

Six-agent white-hat sublet hunting system. Hermes-orchestrated VPS daemon. Well-scoped doctrine doc v0.1.

Spec complete. Not built.

Governed Emergent Systems

943-line theory doc naming the studio's game discipline 'Directed Emergence.' Apollo / Hermes / Dionysus architecture vocabulary. Ties Cave, Long Border, AI Village, Virtue Board into one framework.

Key IP. Not yet published.

Hermes OS MVP

2,200-line spec for a VPS-based archive daemon controlled via Telegram. Private GitHub repo. Nightly journal processing, build review routing, weekly synthesis.

Spec complete. Not built.

The Cave

Browser text experience: Socrates + deterministic state engine + AI narrator. Governed emergence tech demo. Architecture visible via debug panel.

Shipped (Vercel).

Green Ford V2

Micro-RTS auto-battler. Deployed at micro-rts-prototype.vercel.app.

Shipped.

The Long Border

Single-lane economy auto-battler. Spec + V2 autonomous build directive.

Shipped or near-shipped.

The Virtue Board

Timed Greek ethics quiz. AI-generated clue boards.

Shipped.

AI Village

Top-down village adventure. AI NPC dialogue. Social fetch-quest deduction.

Spec complete. Status unclear.

Symposium Studios Overview

Business doc skeleton with five IP tracks, operating model, apprenticeship model, proof engine.

V0 skeleton. Useful reference.

Build Pattern Notes

Platform-agnostic agentic build patterns. Internal doctrine.

Active.

Skills Docket

Four skills Marcus has identified as high-value to build: PR Review Checklist, Parallel Agent Coordination, Deployment Preflight, Mobile App Store / TestFlight.

Not built.

Not Safe For Laundry

Premium detergent micro-brand market analysis. Liquid Death comp. Off-thesis.

Park.

Software Projects (Pre-Symposium)

The Software folder is the pre-Symposium archive. It contains the Director Model origin essay, the Master Playbook, the Jamie Stern case study, and a project planning bin of specs that were never built. Most of these are parked correctly.

Item

What it is

Status

The Director Model essay

Field notes on solo building in the agentic era. The foundational case study essay for the Marcus Vale positioning.

Published or near-published. Strong.

Maxwell's Master Playbook v2

2,046-line fCTO career roadmap. Market analysis, three paths, 90-day roadmap, portfolio strategy.

Reference doc. Active.

Jamie Stern case study

Anchor-adjacent proof artifact. 20 PRs, one day, real client codebase.

Complete. Portfolio-ready.

Arbiter

AI Operator Assessment Platform. B2B. Management consulting and professional-services wedge. US market.

Spec complete. Strong concept. Deferred.

Four Modes App

Voice-first season-reading tool built on the Four Modes framework. Periodic reflective instrument.

Spec complete. Downstream of manuscript.

Manuscript Forge

Distillation engine for memoir source material. Classifies, tags, structures fragments into chapter packets.

Spec complete. Folds into Hermes.

The Propylaea

Voice-first virtue encounter. Interpretive character reading and practice path. Seven prompts, seven dimensions.

Spec complete. Deferred.

Councilflow

Deterministic AI synthesis workflow. Parallel model runs, human-in-the-loop gates, artifact-first output.

Spec complete. Partially superseded by existing Council pattern.

PatchBay

Gear vault and AI-matching for musicians. Inventory, trade conditions, musician-to-musician swap finding.

Explicitly quarantined. Do not open.

Sober Garden

Visual recovery companion. Garden metaphor. Companion to Anchor.

Spec complete (2,634 lines). Deferred.

Neskala

Bali bodywork matching service. Yuni-led concept. Villa partners, practitioner recruiting.

Different category. Yuni's call.

Angel at the Dock

AI-dialogue RPG. Growing up as the leveling system. Indonesia island setting.

Spec complete. Parked explicitly until Anchor ships.

VST / Music Toy

Web-first music toy and VST research brief. Browser prototypes in Tone.js, eventual Expo port.

Parked. Author OS lane.

OpenClaw Complete Guide

1,220-line guide to OpenClaw (Peter Steinberger's personal-agent gateway, 100k GitHub stars). Alternative to Nous Hermes.

Reference. Important for framework decision.

2. What Has Legs

The ranked read below separates the projects into tiers by a single question: does this earn priority over Anchor right now? Almost nothing does. But a few things compound on Anchor rather than competing with it.

Aristotle's note: your energeia sits at the intersection of AI direction, recovery-grade product judgment, Greek-philosophical operating frame, and the patience to build governed systems rather than slop. That is Anchor, the Directed Emergence games, Arbiter, and the Director Model itself. Phronesis says: ship Anchor, stand up Hermes carefully, build the sublet probe under tight time-boxing, package the Directed Emergence thesis publicly. Everything else is potentially good but not kairos.

Tier 0: Finish Anchor Web Core, Then Ship Mobile

This is the non-negotiable sequence, with one important refinement: “web core complete” is the bar that gates mobile, not “every V5 phase done.” V5.4 is a polish basket that can expand indefinitely. Mobile is a strategic capability milestone. They run in parallel after the core stabilizes, not in series.

Anchor Web Core Complete means: safety / SOS stable, relapse response stable, core check-in / chat / tracker flows stable, Practice either shipped or intentionally deferred, data / export path at least planned. That is the bar for mobile. V5.4 polish does not block mobile and does not block the personal-agent spike.

The Expo Conversion Guide in the folder is stale. It assumes a Replit / server.js / /public-folder architecture. Your current Anchor runs on Vercel + Fly + Neon with a Next.js app and a real CD pipeline. An agent fed the old guide will spend its first hour looking for files that do not exist. The guide must be rewritten before firing at CC.

Tier 1: Personal Agent Substrate, Then Sublet Radar

One flag that changes the ordering: Sublet Radar v0 needs a substrate. The two are the same first half of work. Standing up a personal agent substrate for archive / daemon use is also standing up the infrastructure Sublet Radar needs. They diverge after the substrate is proven.

Your docs contain two competing personal-agent frameworks that have not been reconciled. The Hermes MVP and the Sublet Radar doctrine commit to Nous Research's Hermes Agent framework. The Software folder contains a 1,220-line OpenClaw Complete Guide. OpenClaw is Peter Steinberger's VPS-based personal-agent gateway with 100k GitHub stars in its first week. The Hermes MVP doc never compares the two. A verification spike is required before either build starts, and the substrate must not be pre-named. Details in Section 4.

Sublet Radar must run a manual validation phase before any substrate-based build. Real inbox, twenty real listings, manual AI triage. Confirm the value before building automated infrastructure around it. The substrate existing does not earn the right to skip validation. Sublet Radar without validation is infrastructure cosplay.

Tier 2: Package the Directed Emergence Thesis Publicly

The theory doc (governed-emergent-systems.docx) is one of the most valuable things in the folder. It names the studio's game discipline, gives it a framework (Apollo / Hermes / Dionysus), and positions all five shipped games as proof artifacts. The Cave, Green Ford V2, Long Border, Virtue Board, and AI Village are already the case study. The actionable move is not building another game. It is writing a two-day public essay naming the discipline, with the games as links. This is positioning work, not build work.

Tier 2: Arbiter (Operator Assessment)

Of all the parked project specs, Arbiter has the clearest commercial pull. B2B, US consulting market, expensive buyer, AI governance angle. The concept is strong and the timing is right. But Arbiter needs a sales motion, not just a build. It earns priority when there is a real arena foothold and a buyer conversation to test against.

Tier 3: Deferred

Four Modes App: downstream of the manuscript landing. Do not build the app before the book frames it.

Manuscript Forge: folds into Hermes naturally as a skill, not a standalone Next.js app.

Sober Garden: real concept, wrong time. Anchor must have live users before a companion app earns a build.

Propylaea, Councilflow, Angel at the Dock: good specs, not kairos. Each has the right thought behind it, none earns a slot in the current sequence.

VST / music toys: Author OS lane. Real, but a different mode of work. Park until integration mode.

Hard Parks

Not Safe For Laundry: CPG is not your lane.

Neskala: Yuni's call. Different category entirely.

PatchBay: the doc itself says quarantined. Do not open until Anchor is stable and there is a deliberate decision.

Sublet Radar v1 productization: the doctrine explicitly warns against it. Hold at v0. The insight is 'filter plus human closer' as a durable consumer-agent shape. That thesis survives even if the sublet hunt itself ends at v0.

3. Expo Conversion Guide V2: What Needs to Rewrite

The existing guide (ANCHOR -- EXPO MOBILE CONVERSION GUIDE.docx) will mislead an agent. Below is the full delta between the old assumptions and current Anchor reality.

What Stays

The strategic shape: keep backend untouched, replace frontend with Expo, NativeWind for styling, Expo Router for navigation, iOS first, EAS for TestFlight.

The five-tab navigation structure: Home, Check In, History, Trackers, Insights. Verify against current production surface before locking.

Dark theme (#0D0D0D), white primary text, muted green accent (#4DB6AC).

Phase structure: scaffold, architecture separation, agent conversion prompt, local dev loop, TestFlight build.

What Needs to Change

Repo strategy

Not 'fork in Replit.' Mobile client is its own repo or a /mobile workspace in the existing monorepo. Mobile PRs are not Vercel-deployed. They are EAS-built. The CD pipeline on web does not extend to mobile out of the box.

API base URL handling

No 'Replit preview URL' anymore. Current Anchor has a production Vercel domain. The mobile app needs three configurable bases: local dev (pointing at Vercel preview deployments), staging, prod. Handled via expo-constants or .env.expo. Document the auth token flow explicitly: how does the mobile client get and refresh whatever Anchor uses on web (NextAuth session tokens, Supabase auth, or custom JWTs).

Screens in scope for mobile v0

Current Anchor surface is larger than the 2026-04 guide assumed. Reference the current repo state when scoping. Surfaces in or near production include: SOS Mode (V5.0), Practice Mode (V4.1), Chat, Onboarding, Settings, Memory, and Insights. Mobile v0 should scope to: Home, Check-In, Chat, SOS, History, Settings. Defer Practice and Insights to a v0.5 pass. Verify ship status of any specific surface against the actual repo before writing the directive. The archive analysis is not a source of truth on repo state.

V4 architecture lift

buildChatSystemPrompt / composeSystemPrompt lives on the server. Mobile just calls API endpoints. The guide must make this explicit so an agent does not try to port prompt-assembly code into React Native.

SOS Mode offline cache

V5.0 web spec uses localStorage. Mobile requires AsyncStorage (standard data) and SecureStore (phone numbers, which are sensitive). Document that delta explicitly. SecureStore is the right call on iOS.

Council of Models gate

The web build has a Council pattern for safety-adjacent copy. Mobile inherits this, specifically for the SOS screen and any place crisis copy is rendered client-side. The guide should reference your AUTONOMY_LAYER v1.2 so the agent knows the review discipline applies.

TestFlight pipeline

Apple Developer account, bundle identifier (com.eaglerocket.anchor or whatever is reserved), provisioning profiles, EAS credentials handling. This pairs with the Mobile App Store / TestFlight skill on your Skills Docket. Write them together: the skill captures durable knowledge, the conversion guide captures the Anchor-specific application.

Produce: ANCHOR_EXPO_CONVERSION_V2.md and the Mobile App Store / TestFlight skill in one focused doc session. Then fire the mobile build as an autonomous CC Cloud run.

4. The Personal Agent Substrate Verification Spike

The Hermes MVP spec and the Sublet Radar doctrine both commit to Nous Research's Hermes Agent framework without verifying it against the alternative that is sitting in your own Software archive: OpenClaw. The substrate must not be pre-named. Until the spike resolves, call this layer the Personal Agent Substrate, not Hermes.

The Two Frameworks

Dimension

Nous Research: Hermes Agent

OpenClaw (Steinberger)

Origin

Nous Research (AI research lab)

Peter Steinberger (PSPDFKit founder, prolific iOS dev)

Adoption signal

Research-lab framework, thinner public track record

100k GitHub stars in first week of release (Jan 2026)

Interface

Telegram gateway, CLI

WhatsApp, Telegram, Discord, Slack, iMessage

Capabilities

Cron, skills, memory, VPS-hosted, MCP integrations

Web browsing, file/shell access, calendar, email, code execution, skills

Docs quality

Assumed solid in your spec; unverified

1,220-line guide already in your archive

Your existing usage

Sublet Radar doctrine, Hermes MVP both assume it

Referenced in career planning doc only

Risk

May be research-grade with rough production edges

More battle-tested but potentially more footgun surface area

Spike Scope

One bounded session. Acceptance criteria: you walk out having made a deliberate framework decision, not a default one.

Stand up a throwaway Hetzner $5 VPS. SSH keys only, ufw, non-root user. Budget one hour.

Install Nous Hermes via the one-line installer in the MVP doc. Run hermes model in the foreground. Send a hello message. Run hermes gateway setup with a fresh BotFather token. Confirm the Telegram round-trip works. Run hermes gateway install and confirm it persists across loginctl enable-linger.

Read the current README on the Nous repo (not the docs cited in your MVP doc, which may be dated). Confirm: is cron actually shipped? Are skills real and stable? Is MCP integration shipped or roadmap?

Pull up OpenClaw. Read its skills model and security boundaries. Map it against your Tier 0/1/2/3 approval model from the Hermes MVP doc.

Make the call: Nous Hermes, OpenClaw, or a third path (thin Python + APScheduler + python-telegram-bot with no third-party orchestrator).

The lose condition is firing the full substrate build directive or the Sublet Radar build directive on an unverified framework. You are about to make this layer the persistent clerk for your archive, your journal, your build review packets, and eventually your sublet inbox. The substrate must be one you understand and can rebuild if it breaks. Until the spike concludes, do not refer to this layer by any framework's name. The naming itself smuggles in the decision.

5. Revised Build Sequence

The full post-Anchor sequence with dependencies made explicit.

Tier

Project

What it is

When

Why

1

Finish Anchor web core

Safety / SOS, relapse response, core check-in / chat / tracker stable. Practice shipped or intentionally deferred. Data export at least planned.

Now

The non-negotiable bar before mobile fires.

2

Expo Conversion V2 + TestFlight skill

Rewrite the stale conversion guide for current Vercel + Fly + Neon architecture. Write Mobile App Store / TestFlight skill in parallel.

Once web core is in sight

Prevents misdirected agent runs. Skill compounds across future mobile work.

3

Ship Anchor mobile to TestFlight

Expo + NativeWind + Expo Router. iOS first. Five tabs in v0 scope. SOS uses SecureStore.

After guide V2 lands

Next major platform leap. Does not wait for V5.4 polish.

4

Personal-agent framework spike

One bounded VPS session. Verify Nous Hermes against OpenClaw and a thin Python alternative. Make a deliberate call.

After mobile ship

Required before any substrate-based build. Do not skip.

5

Personal archive daemon on chosen substrate

Narrow scope: archive daemon only, private GitHub repo, Telegram gateway, no production credentials. Name follows the spike decision.

After spike resolves

Compounding infrastructure for everything downstream.

6

Sublet Radar manual validation

Real inbox set up. Twenty real listings. Manual AI triage. Confirm the value before automating.

Before any substrate build for sublets

Prevents infrastructure cosplay.

7

Sublet Radar v0 build

Only if validation passes. Six-agent architecture on the chosen substrate. Drafts only. Human sends.

If and only if step 6 confirms value

Real consumer-agent portfolio piece. Time-boxed evening sessions.

8

Directed Emergence public essay

Two-day writing project. Name the discipline, link the five game demos as proof artifacts.

Arena phase

Positioning work. Not a build.

9

Arbiter prototype

Operator assessment, B2B, US consulting wedge.

When a buyer conversation pulls it

Strong concept. Needs sales motion.

10

Everything else parked

Four Modes App, Manuscript Forge, Propylaea, Sober Garden, Angel at the Dock, VST / music toys, Councilflow, PatchBay.

Hold

Good specs, wrong moment.

6. One Thing the Studio Knows About Itself

The Symposium Studios Overview doc has this line, and it is the right internal pressure to maintain:

The studio needs a primary ship path so the IP lab does not dissolve into beautiful unfinished prototypes.

There are many beautiful unfinished specs in these two folders. That is a pattern to stay honest about, not a reason to feel behind. The right move is the same move it has always been: one flagship at a time, with the supporting experiments allowed only when they compound the flagship rather than compete with it.

The order is: finish Anchor web core, ship Anchor mobile, run the substrate spike, stand up the personal archive daemon, run sublet manual validation, build sublet v0 only if validation passes, package the Directed Emergence thesis. Then the arena sprint, which is where Arbiter and the fCTO positioning actually get tested.

Surrender to the sequence. The sequence is correct.

Symposium Studios  |  Archive Analysis  |  Rev. 2  |  May 12, 2026  |  Eagle Rocket LLC
