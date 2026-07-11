# Agent Start Here

You are building Framewalker, a governed AI adventure-frame tech demo.

Before implementation, read:

1. `README.md`
2. `docs/00_HANDOFF.md`
3. `docs/01_MVP_SPEC.md`
4. `docs/02_ARCHITECTURE.md`
5. `docs/03_CHAPTER_ONE.md`
6. `docs/04_DESIGN_SYSTEM.md`
7. `prompts/INTENT_PARSER.md`
8. `prompts/NARRATOR.md`
9. `prompts/IMAGE_PROMPT_GENERATOR.md`

## Prime Directive

Do not build a generic chatbot game.

Build a governed adventure system where:

- mission objectives are visible
- state changes are deterministic
- player input is natural language
- AI is constrained by state
- image prompts are generated from state
- debug output proves what rule fired

## MVP Boundary

Build one chapter only:

**The Gate Beneath the Rain**

Do not build:

- infinite chapter generation
- accounts
- saves
- multiplayer
- maps
- animated video
- mobile app
- open-world exploration
- procedural story engine
- multiple chapters

## First Build Target

Create a playable browser MVP with:

- large frame image area using placeholder image first
- mission card
- HP and Mana bars
- inventory row
- visible win/failure conditions
- narration panel
- text input
- submit action
- deterministic state reducer
- intent parser stub, then LLM parser
- narrator stub, then LLM narrator
- image prompt display
- debug panel showing parsed intent, rule fired, and state delta

