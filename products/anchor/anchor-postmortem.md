---
title: "anchor postmortem"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/anchor postmortem.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# anchor postmortem

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
PROJECT POSTMORTEM

Anchor — AI-Powered Recovery Companion App

Built by Marcus Vale  ·  April 23, 2026  ·  3 hours  ·  $14.00

Executive Summary

On April 23, 2026, a production-ready AI-integrated recovery companion app was designed, specified, built, tested, and shipped in a single three-hour work session at a total cost of $14. The app — named Anchor — includes a persistent PostgreSQL database, OpenAI GPT-4o-mini integration with structured JSON output, a sobriety tracking system with live counters, an insights dashboard with trend charts and calendar heatmap, a PWA-installable frontend, and a sponsor-toned AI that references user-specific patterns in its responses.

No code was written by hand. Every line was directed through AI agent prompting using a structured specification methodology developed over the course of the session. The total build cost — including all AI agent credits, API calls, and platform fees — was $14.

For reference: a comparable project scoped through a traditional development agency in 2020 would have cost $25,000–$30,000 and taken two to three months.

The Numbers

Total build time

3 hours 11 minutes

Start to fully working app

Total cost

$14.00

All-in: agent credits + API calls

Lines of code written by hand

0

100% AI-directed

Database tables created

7

check_ins, trackers, resets, settings, more

OpenAI API integration

GPT-4o-mini

Chat Completions, structured JSON

Iterative build phases

8

V1 → V2A → V2B → V2C → V2D + fixes

Revision prompts run

12+

UI fixes, AI prompt upgrades, tracker fixes

AI models consulted

3

Claude, ChatGPT, Gemini

Equivalent agency cost (2020)

$25,000–$30,000

3 month timeline

Cost reduction

99.95%

Same output, different paradigm

What Was Built

Anchor is a mobile-first progressive web app for daily recovery check-ins and sobriety tracking. It runs in any browser, installs to the iPhone home screen as a PWA, and connects to OpenAI's API for sponsor-toned AI responses.

Check-In System

Full check-in: 14 input fields including mood, energy, craving, focus, hours slept, sober today, meeting attended, contacted a sober person, called a fellow, exercised, ate enough, trigger tags, notes, and a gratitude field

Quick check-in: 5-field rapid version that prefills from last entry

Structured JSON AI output with 7 fields: state summary, risk level, main risk factor, next moves, recovery support prompt, grounding reminder, sponsor note

Color-coded sliders: red to green for mood/energy/focus, inverted green to red for craving

Gratitude field animation: golden glow on blur as a quiet moment of acknowledgment

Sober today = No triggers yellow warning state on contact and fellowship fields

24 trigger tag options as multi-select pill buttons

AI Integration

OpenAI GPT-4o-mini via Chat Completions API

Sponsor-toned system prompt: plain-speaking, warm, non-shaming, action-oriented

AI references specific trigger tags, notes, and field values — not generic responses

Structured JSON parsed and rendered as distinct UI card sections

Sponsor note field: optional deeper observation that only renders if non-empty

Crisis handling instruction in every system prompt routing to 988 and SAMHSA

Sobriety Tracker System

Multiple named sobriety trackers running simultaneously

Live counter per tracker: days and hours, updates every 60 seconds

Detail view: full counter including minutes and seconds

Reset flow: neutral language, optional note, logged to tracker_resets table

Archive capability: hide inactive trackers without deleting

10-color picker: colored circle grid with checkmark on selected

Date-shift banner on home: non-blocking prompt on first open of each day

Insights Dashboard

Streak stats: current streak, longest streak, total check-ins, 7-day averages for mood, craving, and sleep

Trend charts: mood, energy, craving, focus, sleep — 7/30/90 day toggle

Calendar heatmap: monthly grid colored by risk level, tappable to open that day's detail

Recovery habit frequency: meeting, sober contact, fellow called, exercise, ate enough as percentage bars

Sobriety tracker history with current duration and longest streak per tracker

Export: check-ins and tracker data as CSV downloads

Home Dashboard

Sobriety counter grid: all active trackers shown as compact cards with color accents

Today's check-in status: shows latest result summary if already checked in

Quick stats row: today's mood, craving, sober status, hours slept

Full check-in and quick check-in access from home

Technical Infrastructure

Backend: Node.js + Express

Database: PostgreSQL via Replit's built-in database

Frontend: Plain HTML, CSS, vanilla JavaScript — mobile-first

AI: OpenAI JavaScript SDK, Chat Completions, structured JSON output

PWA: Web manifest + service worker, installable via Add to Home Screen on iOS and Android

History: Full check-in history with reverse chronological list, tappable detail views, edit and backfill capability

Error handling: graceful degradation on all failure states, no stack traces exposed to browser

The Methodology: Director Model AI Development

This project was built using what might be called the Director Model — a structured approach to AI-native development where the human acts as architect and director rather than implementer. No code was written by hand. Instead, every build phase was driven by precisely specified agent prompts written in collaboration with multiple AI models.

How It Worked

Phase 0: Concept review — evaluated an initial spec from ChatGPT, identified technical errors (wrong API pattern, missing structured output, no parsing strategy), and rewrote from scratch

Phase 1: Spec writing — translated product intent into precise Replit Agent prompts with exact field definitions, API patterns, database schemas, and UI requirements

Phase 2: Iterative builds — ran 8 distinct build phases (V1 through V2D), each scoped narrowly to avoid agent confusion and credit waste

Phase 3: Revision loops — identified UI and AI output issues through real-device testing, wrote targeted single-concern fix prompts rather than broad correction requests

Phase 4: Cross-model consultation — used Claude for architecture and spec writing, ChatGPT for spec generation and validation, Gemini for product innovation input — running all three simultaneously

Phase 5: Documentation — produced full V3 roadmap, Expo mobile conversion guide, and this postmortem as parallel artifacts

Key Principles That Made It Work

Narrow scope per prompt: each agent prompt did one thing. Broad prompts produce broad failures.

Explicit over implicit: database column names, API endpoint paths, exact JSON shapes, pixel-level UI instructions — nothing left to the agent's discretion

Technical precision: specified the correct API (Chat Completions, not Responses API), correct model (gpt-4o-mini), correct output format — not what the first AI suggested

Revision discipline: never corrected mid-build. Let each phase complete, test on real device, then write a clean fix prompt

Forward planning: database schema included user_id from day one, future V3 memory columns documented before they were needed

What Comes Next

Anchor is not finished — it's at the end of its V2 foundation phase. The V3 roadmap is fully specified and ready to build. A React Native/Expo mobile conversion is planned for TestFlight distribution. An Apple Developer account was enrolled during this session.

V3 Roadmap (Fully Specified, Ready to Build)

V3A: Three-layer persistent memory system — stable profile, recent state summary, event log — injected into every AI call so responses feel longitudinal

V3B: Sponsor chat interface — real-time conversation with memory-aware AI, crisis routing, human handoff shortcuts

V3C: Commitment and follow-up loop — choose one next action after every check-in, app follows up hours later asking if you did it

V3D: Voice input — OpenAI Whisper API on notes, gratitude, and chat fields

V3E: Proactive email outreach — daily reminders, missed check-in follow-ups, weekly pattern summaries via Resend

V3F: Text-to-speech, final UX polish, full audit

2026 Innovation Roadmap

Predictive UX: craving spike prediction from behavioral pattern data, drift detection, overconfidence flagging

Apple Health integration: real sleep, HRV, and activity data replacing self-report

Pattern narrative: AI-written story of the user's recovery arc based on longitudinal data

Relapse response protocol: compassionate, structured response flow for reset moments

Emotion wheel check-in: richer emotional data than a 1-10 slider

Resentment and gratitude tracking: recovery-specific journaling layers

Mobile App

Fork existing Replit project

Replit Agent converts HTML frontend to React Native/Expo while backend stays intact

Development testing via Expo Go on iPhone

TestFlight distribution via EAS Build

Market Context

The recovery app market is crowded with products built on 2019 assumptions: streak counters, meeting finders, motivational quotes. None of them combine persistent AI memory, behavioral pattern prediction, sponsor-adjacent conversation, and human handoff routing in a single product.

Anchor's differentiation is not any single feature. It is the compounding effect of daily ritual + longitudinal memory + action bias + human routing. The app is designed to reduce isolation and increase wise action — not merely provide comforting conversation.

Potential monetization (post-validation): free tier for daily check-ins and basic tracker, Pro tier at $9–12/month for sponsor chat, voice input, memory system, email outreach, and full history. The use case is real, the daily ritual potential is high, and the origin comes from genuine lived experience rather than market opportunism.

What This Demonstrates

This project is a proof of concept for a specific kind of builder: someone who thinks in systems, communicates with precision, and directs AI tools rather than implementing code directly.

The traditional framing of software development — developer writes code, project takes months, agency charges tens of thousands — is not the only model. A sufficiently precise architect with access to the right AI tools can compress that timeline and cost by orders of magnitude without sacrificing output quality.

The question is not whether AI can build software. It demonstrably can. The question is whether the person directing it understands the domain well enough to specify correctly, catch errors, iterate precisely, and maintain architectural integrity across a multi-phase build.

That is the skill. That is what this session demonstrated.

Marcus Vale  ·  AI-Native Builder  ·  Fractional CTO
