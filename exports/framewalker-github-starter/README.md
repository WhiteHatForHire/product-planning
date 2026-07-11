# Framewalker

Framewalker is a governed AI adventure-frame engine.

It is a slow, cinematic, linear adventure game where each chapter gives the player a mission, visible win conditions, HP, Mana, inventory, and a scene image. The player types natural-language dialogue or action. The engine parses intent, updates deterministic state, resolves consequences, and uses AI to generate narration and cinematic image prompts for major frames.

The key design rule:

> State owns truth. AI performs the world.

This is not an open-ended chatbot fantasy game. It is a proof of a design system: governed state, mission objectives, natural-language input, HP/Mana, occasional combat, image generation, and inspectable state transitions.

## MVP Demo

Product working title: **Framewalker**

First chapter: **The Gate Beneath the Rain**

Mission:

> Enter the sealed city before dawn.

Win conditions:

- Get past the gate.
- Keep HP above 0.
- Learn why the gate was sealed.
- Do not kill the gate captain.

Failure conditions:

- HP reaches 0.
- The captain raises the alarm.
- The captain dies.
- Mana reaches 0 before the sigil is revealed.

## Start Here

1. Read [AGENT_START_HERE.md](AGENT_START_HERE.md).
2. Read [docs/00_HANDOFF.md](docs/00_HANDOFF.md).
3. Read [docs/01_MVP_SPEC.md](docs/01_MVP_SPEC.md).
4. Read [docs/02_ARCHITECTURE.md](docs/02_ARCHITECTURE.md).
5. Read [docs/03_CHAPTER_ONE.md](docs/03_CHAPTER_ONE.md).

## MVP Stack Recommendation

- Next.js or Vite + React + TypeScript
- Node/Express or Next route handlers for LLM/image calls
- In-memory state for MVP
- Generated/static placeholder frames first
- Image generation integration second
- No accounts, no database, no save system for MVP

