---
title: "ADR DreamMirror v1"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Dream Mirror /Dream Mirror OS/ADR_DreamMirror_v1.md"
status: active
privacy: working
tags:
  - product
---

# ADR DreamMirror v1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# DreamMirror — Architecture Decision Record v1.0

**Status:** Locked for V0  
**Owner:** Marcus Vale / Eagle Rocket LLC  
**Date:** May 2026

---

## The Decision

**Frontend:** React + Vite + TypeScript + Tailwind CSS + Shadcn UI  
**Backend:** Express + TypeScript  
**Database / Auth:** Supabase Postgres + Supabase Auth + Row-Level Security  
**Frontend deploy:** Vercel  
**Backend deploy:** Fly.io  
**AI abstraction:** Server-side provider layer (model-agnostic at call time)

---

## Context

DreamMirror handles sensitive personal dream content. The AI pipeline requires server-side orchestration to protect API keys, coordinate multi-step prompt chains, and log token cost per stage. V0 target is approximately 50 beta users. The stack must be cheap to run at that scale, fast to iterate on, and familiar enough that agent-directed builds don't require context ramp-up.

---

## Rationale by Layer

| Layer | Choice | Rationale |
|---|---|---|
| Frontend framework | React + Vite + TypeScript | Known. Fast HMR. TypeScript gives agent builds type safety without boilerplate fights. |
| UI system | Tailwind + Shadcn UI | Shadcn gives accessible, unstyled component primitives. Tailwind keeps CSS agent-friendly. No fighting a design system at V0. |
| Backend | Express + TypeScript | Server-side AI provider abstraction is the core reason to have a backend at all. Express is minimal. TypeScript gives shared types with frontend if monorepo is used. |
| Database | Supabase Postgres | Proven on Anchor. Relational schema supports the longitudinal pattern moat. Postgres is not going to surprise you. |
| Auth | Supabase Auth | Reduces auth build surface significantly. JWT + RLS integration is native. |
| RLS | Enabled from day one | Dream content is intimate. Row-level security is not optional. Every table that stores user dream data must have RLS policies before any user touches production. |
| Frontend deploy | Vercel | Zero-config. Preview deploys on every PR. Known CD workflow. |
| Backend deploy | Fly.io | Known workflow from Anchor. Persistent server is appropriate given multi-step AI pipeline coordination and async work. |

---

## Known Trade-offs

**Fly.io vs. Vercel serverless functions:** Fly adds ops overhead. For a simple API, Vercel functions would be cheaper and simpler. The choice of Fly is justified by the multi-step AI pipeline: each dream analysis may fan out to 4–7 sequential or parallel prompt calls with intermediate state. Managing that in serverless cold-start environments adds complexity without benefit. If infra cost exceeds $50/month before 100 users, revisit and consider moving stateless routes to Vercel functions while keeping only the pipeline coordinator on Fly.

**Supabase free tier limits:** Supabase pauses inactive projects after 1 week on free tier. Ensure the project is upgraded before beta invites go out.

---

## What This ADR Locks

- No native iOS/Android app in V0. Mobile-first responsive web app only.
- No GraphQL. REST only between frontend and backend.
- No client-side AI calls. All model calls made server-side, all API keys server-side only.
- RLS enabled before any user data is stored. Not a post-launch task.
- Supabase is the single source of truth for user data. No secondary user store.
- All AI analysis outputs stored to database with `model_version` and `prompt_version` fields. No ephemeral outputs.
- Token cost logged per pipeline stage from the first deploy.

## What This ADR Does Not Lock

- AI model provider. The abstraction layer handles this. Swap Claude for GPT or Gemini without schema changes.
- Specific model per agent step. Cheaper models handle extraction; stronger models handle synthesis.
- Pricing tier of any service.
- Prompt content. Prompts are versioned externally and injected at runtime.

---

## Review Triggers

Revisit this ADR if any of the following occur before V1:

- Fly.io cost exceeds $50/month before 100 active users
- Cold start latency on Fly becomes a visible UX problem (>3s pipeline initiation)
- Supabase free tier pauses the project
- A need emerges for native push notifications (reconsider PWA vs. native)
- The multi-agent pipeline complexity outgrows Express and requires a proper queue/worker architecture
