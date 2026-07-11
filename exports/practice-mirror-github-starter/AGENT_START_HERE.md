# Agent Start Here - Practice Mirror

## Mission

Build the first working MVP of Practice Mirror: an AI rehearsal room for hard conversations.

## Source docs

Use these docs as the product contract:

- `docs/START_HERE.md`
- `docs/MVP_SPEC.md`
- `docs/ARCHITECTURE.md`
- `docs/DESIGN_SYSTEM.md`
- `docs/PROMPTS.md`
- `docs/BUILD_PLAN.md`

## Recommended first implementation

1. Scaffold a Next.js or Vite React app.
2. Build a static prototype with seed scenarios.
3. Add Scenario Designer route.
4. Add Counterpart Actor route.
5. Add pause coach route.
6. Add after-action review route.
7. Add local save/delete/export for sessions.

## Hard constraints

- Do not make the live counterpart coach the user.
- Do not support coercion, harassment, stalking, or consent evasion.
- Do not claim certainty about a real person's thoughts.
- Do not present legal, medical, employment, or crisis advice as authoritative.
- Keep user stop/reset/delete controls visible.

## Definition of done

The MVP is done when a user can run a 5-10 turn rehearsal from a custom scenario, pause for one concise hint, end the session, and receive a specific review plus a final script.

