# Kairos

A personalized signal map for NYC Tech Week 2026. Built by Symposium Studios as a live prototype of agentic event intelligence.

## What this is

An intelligence layer on top of the Carly NYC Tech Week 2026 ICS feed. Tell Kairos who you are and what you're looking for; it surfaces the ~1,035 events ranked, filtered, and personalized for you.

## Repo orientation

- `.symposium/` — the Symposium Studios build system: AUTONOMY_LAYER (execution doctrine), META_PROMPT (spec-to-directive converter), CONTEXT.md (project glossary), skills marketplace (invocable named patterns), templates, ADRs.
- `docs/kairos-spec-v1.1.md` — the product specification.
- `KAIROS_DIRECTIVE.md` — the V1 bootstrap build directive. Fire this at CC Local or CC Cloud.
- `data/marcus-route.json` — Marcus's public Tech Week route (populated separately).

## To build

1. Read `.symposium/AUTONOMY_LAYER.md` for execution protocol.
2. Read `docs/kairos-spec-v1.1.md` for the product specification.
3. Fire `KAIROS_DIRECTIVE.md` at CC Local or CC Cloud per the GO instruction at the bottom of the directive.

## Status

Pre-build. V1 directive ready. AUTONOMY_LAYER and META_PROMPT generic editions seeded. Skills marketplace seeded with 10 skills across planning, diagnostics, execution, review, and handoff categories.
