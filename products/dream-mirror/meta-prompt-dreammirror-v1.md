---
title: "META PROMPT DreamMirror v1"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Dream Mirror /Dream Mirror OS/META_PROMPT_DreamMirror_v1.md"
status: active
privacy: working
tags:
  - product
---

# META PROMPT DreamMirror v1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# META_PROMPT.md — DreamMirror Edition v1.0

**Use:** Prepend this to every autonomous agent directive session for DreamMirror.  
**Do not modify this file during a session.** If a change is needed, update the file and start a new session.

---

## Project Identity

**Product:** DreamMirror  
**Public URL:** TBD (V0 beta)  
**Owner:** Marcus Vale / Eagle Rocket LLC  
**Human method founder:** Yuni  
**Director identity:** Charlie (Marcus's AI showrunner layer)

DreamMirror is a voice-first, AI-assisted dream reflection platform. It helps users capture dreams, structure the narrative, identify emotional tone, extract symbolic candidates, connect themes to waking life, track recurring patterns over time, and optionally book a session with Yuni.

The product is **reflective, not predictive.** It does not diagnose. It does not tell fortunes. It returns users to agency through grounded, emotionally honest reflection.

---

## Stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite + TypeScript + Tailwind CSS + Shadcn UI |
| Backend | Express + TypeScript |
| Database | Supabase Postgres |
| Auth | Supabase Auth |
| Security | Row-Level Security (RLS) on all user data tables |
| Frontend deploy | Vercel |
| Backend deploy | Fly.io |
| AI calls | Server-side only, provider-abstracted |

Stack is locked per ADR v1.0. No deviations without Marcus's explicit sign-off.

---

## Repository Structure (Target)

```
/
├── apps/
│   ├── web/          # React + Vite frontend
│   └── api/          # Express + TypeScript backend
├── packages/
│   └── shared/       # Shared types, schema definitions
├── supabase/
│   ├── migrations/   # All schema migrations as explicit SQL
│   └── seed/         # Seed data for development
└── docs/
    ├── ADR_DreamMirror_v1.md
    ├── AUTONOMY_LAYER_DreamMirror_v1.md
    ├── META_PROMPT_DreamMirror_v1.md
    ├── DIRECTOR_PRIMER_DreamMirror_v1.md
    └── PROMPT_LIBRARY_DreamMirror_v1.md
```

---

## Standing Protocol

The full behavioral protocol for all agent sessions is in `AUTONOMY_LAYER_DreamMirror_v1.md`. Read it before beginning any work. The most critical rules to internalize:

- RLS on every user data table, before any user-facing feature ships
- No auto-merge on prompts, UI copy, safety logic, or schema migrations
- All AI calls server-side, all API keys server-side
- `model_version`, `prompt_version`, and `token_cost_by_stage` stored on every analysis record
- Safety Agent runs on every analysis output before it reaches the user
- MCP write safety preflight (§1.12) before any production write
- Spec-reality reconciliation (§1.13) before starting any directive

---

## Current Phase

**Phase:** V0 — prove the behavioral loop  
**Target:** ~50 beta users  
**Success definition:** Users capture at least 3 dreams, read the analysis output, and return because the system helped them notice something meaningful.

The loop is: wake → capture → reflect → save → notice pattern → return.

Do not build outside the loop in V0.

---

## PR Conventions

- Branch naming: `feature/`, `fix/`, `chore/`, `schema/`
- PR title format: `[scope] Brief description`
- PR description must include: what changed, what was tested, and any gaps or flags for Marcus
- Do not auto-merge: prompts, UI copy, safety logic, RLS policies, schema migrations
- All other PRs may be merged after CI passes and smoke test is clean

---

## How to Use This File

This file is prepended to every directive before firing at an agent. It gives the agent the minimum project context needed to understand what they are building, for whom, and under what constraints. The directive that follows this file contains the specific task. The AUTONOMY_LAYER contains the standing behavioral rules.

When in doubt, the order of authority is:

1. AUTONOMY_LAYER (standing protocol — always wins)
2. META_PROMPT (project context — session-stable)
3. Directive (task-specific — governs the current session)
