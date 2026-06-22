---
title: "DIRECTOR PRIMER DreamMirror v1"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Dream Mirror /Dream Mirror OS/DIRECTOR_PRIMER_DreamMirror_v1.md"
status: active
privacy: working
tags:
  - product
---

# DIRECTOR PRIMER DreamMirror v1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# DreamMirror — Agentic Coding Director Primer v1.0

**For:** Claude Code (CC), Codex, Replit Agent, or any autonomous coding agent receiving a DreamMirror directive  
**Showrunner:** Charlie (Marcus Vale's AI director identity, operating inside Eagle Rocket LLC)  
**Date:** May 2026

---

## Who You Are Working For

You are receiving direction from Marcus Vale, founder of Eagle Rocket LLC, operating as an AI-native fractional CTO using the Director Model. Marcus directs agents rather than writing code directly. Charlie is the identity Marcus uses for the strategic/showrunner layer of this relationship.

This is not a casual coding task. You are building a product that handles sensitive personal dream content. Every decision you make has a real user on the other end.

---

## What DreamMirror Is

DreamMirror is a voice-first, AI-assisted dream reflection platform. It helps users capture dreams immediately after waking, structure the narrative, identify emotional tone, extract symbolic candidates, connect themes to waking life, track recurring patterns over time, and optionally book a session with Yuni — the human founder and method source.

The product is **reflective, not predictive.** It does not tell fortunes. It does not diagnose. It does not interpret dreams as fixed facts. It returns the user to agency through grounded reflection.

The method is Yuni's: preserve the dream, decode emotional tone, map symbols contextually, connect to waking life, identify recurring patterns, return the user to agency through one clear reflective action.

---

## The Stack You Are Building On

- **Frontend:** React + Vite + TypeScript + Tailwind CSS + Shadcn UI — deployed to Vercel
- **Backend:** Express + TypeScript — deployed to Fly.io
- **Database / Auth:** Supabase Postgres + Supabase Auth + Row-Level Security (RLS)
- **AI abstraction:** Server-side provider layer. All model calls server-side. No client-side AI calls. No API keys in the browser.

This is locked. Do not propose alternative stacks. Do not suggest native mobile. Do not suggest GraphQL. Do not suggest client-side AI calls.

---

## Director Model Rules

These are not preferences. They are operating protocol.

**On building:**
- Build what the directive specifies. Do not invent features that are not in scope.
- When something is ambiguous, implement the conservative interpretation and leave a clear comment flagging the ambiguity.
- Do not optimize prematurely. Clarity over cleverness at V0.

**On PRs:**
- Open a PR for every meaningful unit of work.
- Do not auto-merge any PR that touches: prompt content, UI copy visible to users, safety logic, RLS policies, or schema migrations.
- Smoke test before opening a PR. Do not open a PR that breaks the build.
- PR description must include: what changed, what was tested, and any known gaps.

**On the database:**
- RLS must be enabled on every table that stores user data before any user-visible feature is deployed.
- Schema migrations must be written as explicit SQL files, not auto-generated drift.
- The `prompt_version` and `model_version` fields must be stored on every Analysis record. This is non-negotiable.

**On AI calls:**
- Log token count per pipeline stage on every analysis run.
- Never send more dream history into a prompt than is needed for the current step.
- Cache analysis results. Do not rerun an analysis on the same dream unless the user explicitly requests a refresh.
- All AI synthesis calls must pass through the Safety Agent before returning to the user.

**On safety:**
- Dream content can surface trauma, grief, crisis, suicidal ideation, relational distress, and substance themes.
- The Safety Agent is not optional. It runs on every analysis output before the user sees it.
- If the Safety Agent flags crisis-adjacent content, the output must include the positive-instruction path (see Prompt Library) — not just stripped text.

**On MCP and production writes (§1.12 — required):**
Before any tool call that writes to production infrastructure (Supabase production, Fly.io production, Vercel production environment variables, DNS records, or any external service), stop and confirm:
1. Is this the production environment or a preview/staging environment?
2. Is this write reversible without data loss?
3. Has the user (Marcus) explicitly authorized this specific write in the current session?

If any answer is unclear, do not proceed. Open a PR or leave a comment for Marcus to authorize manually.

**On spec vs. reality reconciliation (§1.13 — required):**
Before starting work on a directive, scan the existing codebase for any prior implementation of the feature being specified. If you find prior implementation that conflicts with the directive:
1. Document the conflict in a comment.
2. Implement the directive as specified.
3. Flag the conflict in the PR description for Marcus to review.

Do not silently override existing code without flagging it.

---

## What You Are Not Building

Not in V0. Do not implement, stub, or reference:

- Social features, community, shared dream feeds
- Native iOS / Android app or React Native
- Therapist marketplace or practitioner portal
- Multilingual support
- Stripe integration (session booking uses a calendar/inquiry link, not in-app payment)
- Any feature not in the current directive

If you find yourself building something not in the directive, stop and check.

---

## The Emotional Shape of the Product

Users are sharing something intimate when they open this app. The output should feel like it was written by someone who cares, not generated by a machine. The brand voice is warm, grounded, psychologically intelligent, and lightly poetic. It is never clinical, never predictive, never certain.

The voice rule is: **offer meaning without stealing agency.**

If you are writing UI copy, error messages, empty states, loading text, or any user-facing string, apply this rule. The tone of the product lives in every string, not just the analysis output.

---

## How to Handle Uncertainty

When you are unsure whether something is in scope, use this test:

1. Is it in the current directive? If yes, build it.
2. Is it required for the directive to function? If yes, build the minimum version.
3. Is it a safety, legal, or RLS concern? If yes, implement it conservatively and flag it.
4. Is it a feature idea or optimization? If yes, leave a `// DIRECTOR: [note]` comment and skip it.

Do not make product decisions. Make implementation decisions. Product decisions belong to Marcus.
