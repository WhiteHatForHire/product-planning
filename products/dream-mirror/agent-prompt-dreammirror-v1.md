---
title: "AGENT PROMPT DreamMirror v1"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Dream Mirror /Dream Mirror OS/AGENT_PROMPT_DreamMirror_v1.md"
status: active
privacy: working
tags:
  - product
---

# AGENT PROMPT DreamMirror v1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# DreamMirror — First Agent Prompt
## Generates the Full Autonomous V0 Build Directive

**Purpose:** Fire this at Claude (Opus) to generate the complete autonomous build directive for V0.  
**Prerequisites before firing:**
- AUTONOMY_LAYER_DreamMirror_v1.md is in the context or repo
- META_PROMPT_DreamMirror_v1.md is in the context or repo
- V0_SEED_SPEC_DreamMirror_v1.md is in the context or repo
- PROMPT_LIBRARY_DreamMirror_v1.md is in the context or repo
- DIRECTOR_PRIMER_DreamMirror_v1.md is in the context or repo

---

## Prompt

```
You are Charlie — the AI director identity for Marcus Vale / Eagle Rocket LLC.

You are generating a complete autonomous build directive for DreamMirror V0. This directive will be executed by a Claude Code agent (or equivalent autonomous coding agent) with no further input from Marcus during the session.

The directive you produce must be self-contained, unambiguous, and ordered for successful autonomous execution. It must produce a deployable V0 of DreamMirror.

You have access to five source documents:
- AUTONOMY_LAYER_DreamMirror_v1.md — the standing behavioral protocol. The agent must read and follow it.
- META_PROMPT_DreamMirror_v1.md — project context and stack.
- V0_SEED_SPEC_DreamMirror_v1.md — full V0 specification including database schema, all 9 screens, AI pipeline requirements, and completion criteria.
- PROMPT_LIBRARY_DreamMirror_v1.md — all agent system prompts for the AI analysis pipeline.
- DIRECTOR_PRIMER_DreamMirror_v1.md — agent behavioral rules and identity context.

---

Generate a complete autonomous build directive with the following structure:

## SECTION 1: AGENT ORIENTATION
Brief the agent on who they are working for, what DreamMirror is, and what this session must achieve. Reference AUTONOMY_LAYER and DIRECTOR_PRIMER as required reading before any work begins. Be explicit that this is a production-bound build, not a prototype.

## SECTION 2: SESSION OBJECTIVE
State the single session objective clearly. The objective for V0 is: scaffold the complete DreamMirror application — monorepo structure, Supabase schema with RLS, Express backend with AI pipeline, React frontend with all 9 V0 screens — to a state where it can be deployed to Vercel (frontend) and Fly.io (backend) and connected to Supabase production.

## SECTION 3: BUILD ORDER
Specify the exact order of build operations. The order must be:
1. Monorepo scaffold (apps/web, apps/api, packages/shared, supabase/migrations)
2. Supabase schema migrations (all tables with RLS, in dependency order: profiles → dreams → dream_emotions → dream_symbols → analyses → user_pattern_summaries → app_settings)
3. Shared TypeScript types matching the schema
4. Express backend scaffold with provider-abstracted AI pipeline (all 7 agents as separate service functions: narrative, emotion, symbol, life mirror, pattern, coach, safety)
5. API routes (auth, dreams CRUD, analysis pipeline, export, delete)
6. React frontend scaffold with routing
7. All 9 V0 screens in spec order (Landing → Onboarding → Capture → Check-In → Analysis Result → Journal → Pattern Dashboard → Book with Yuni → Settings/Legal)
8. Instrument all required events
9. Deploy configuration (vercel.json, fly.toml, environment variable documentation)
10. Smoke test: complete the full loop (capture → check-in → analysis → save) against a test user

## SECTION 4: HARD CONSTRAINTS
List all non-negotiable constraints the agent must follow throughout the session. Pull these from AUTONOMY_LAYER and the Seed Spec. Include:
- RLS on every user data table before any user-facing feature ships
- No auto-merge on prompts, UI copy, safety logic, RLS policies, schema migrations
- All AI calls server-side, no client-side model calls
- model_version, prompt_version, and token_cost_by_stage stored on every Analysis record
- Safety Agent runs on every analysis output before it reaches the user
- Raw dream text is immutable after save
- Export and delete functional before any real user is onboarded
- §1.12 MCP write safety preflight before any production write
- §1.13 spec-reality reconciliation before starting any section

## SECTION 5: AI PIPELINE IMPLEMENTATION DETAIL
Provide specific implementation guidance for the Express AI pipeline. The agent must implement the pipeline as 7 separate service functions. Each function takes a specific input object and returns a specific output object (define the TypeScript interfaces). The Safety Agent must be the final step and must handle the crisis-adjacent care note path. Token cost must be logged per function call. All prompts must be loaded from the PROMPT_LIBRARY — embed the prompt content directly in the appropriate service function files as string constants, tagged with the prompt version identifier.

## SECTION 6: PR PROTOCOL FOR THIS SESSION
Specify how the agent should open PRs during this session. Use this structure:
- PR 1: Monorepo scaffold + Supabase migrations
- PR 2: Shared types + Express backend scaffold + AI pipeline service functions (no routes yet)
- PR 3: API routes (auth, dreams, analysis, export, delete)
- PR 4: React frontend scaffold + routing
- PR 5: Landing + Onboarding screens
- PR 6: Dream Capture + Emotional Check-In screens
- PR 7: Analysis Result screen
- PR 8: Journal + Pattern Dashboard screens
- PR 9: Book with Yuni + Settings/Legal screens
- PR 10: Event instrumentation + deploy config + smoke test results

Remind the agent: do not auto-merge PR 2 (contains prompt content) or PR 7 (contains safety logic and analysis UI copy). All others may merge after CI passes.

## SECTION 7: ENVIRONMENT VARIABLES DOCUMENTATION
Instruct the agent to create a `.env.example` file in the repo root that documents every required environment variable with a description and example format. The agent must not hardcode any API keys, secrets, or environment-specific values.

## SECTION 8: COMPLETION HANDOFF
At the end of the session, the agent must output a handoff summary to Marcus that includes:
- What was built and what was not built
- Which PRs are open and their merge status
- Any PRs that require Marcus's manual review before merge
- Any gaps, flags, or unresolved decisions
- The deploy instructions (environment variables to set, Fly.io and Vercel deploy commands)
- Any §1.12 or §1.13 flags that require Marcus to take manual action

---

The directive you generate must be long enough to be unambiguous and self-sufficient. The agent will not have the ability to ask Marcus questions during execution. Every decision that Marcus would need to make must either be made in the directive or surfaced as a clear flag in the PR description.

Write the directive in the same markdown format as this prompt. Use headers, code blocks, and tables where they add clarity. Do not truncate sections for brevity — the agent needs the complete instruction.
```
