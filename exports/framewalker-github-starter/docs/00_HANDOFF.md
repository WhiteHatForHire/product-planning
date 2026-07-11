# Framewalker Handoff

## One-Line Thesis

Framewalker is a governed AI adventure-frame engine: cinematic AI-generated frames and narration on top of deterministic mission state.

## Product Shape

The player moves through a linear adventure chapter. Each chapter has a mission, win conditions, failure conditions, HP, Mana, inventory, and a small set of dramatic scenes.

The player is presented with:

- a cinematic scene image
- chapter mission and win conditions
- HP / Mana
- inventory
- narration
- a text box asking what they say or do

The player can type naturally:

```text
I lower my weapon and show the captain the cracked sigil ring.
```

The system parses that input into structured intent, resolves it against deterministic state, updates HP/Mana/trust/flags, narrates the result, and generates a new image prompt when the scene changes or a major event happens.

## What This Is

Framewalker is:

- an AI-native adventure game tech demo
- a proof of governed narrative state
- a visual design system for AI-generated adventure frames
- a natural-language combat/dialogue prototype
- a Directed Emergence proof object

Framewalker is not:

- a generic fantasy chatbot
- an infinite story toy
- a full RPG
- a procedural open world
- a normal combat menu game
- a SaaS product

## The Design System Proof

The demo should prove these surfaces:

- mission card
- cinematic frame
- visible win conditions
- HP/Mana bars
- natural-language input
- state-governed outcomes
- constrained AI narration
- AI image prompt generation
- special frame states: reveal, battle, death, victory
- debug panel showing the governed engine underneath

## The Engine Claim

The AI may:

- parse intent
- narrate allowed outcomes
- generate image prompts
- style the world

The AI may not:

- decide mission truth
- invent new win conditions
- ignore HP/Mana
- create unauthorized exits or items
- override deterministic failure conditions
- secretly change state

## MVP Strategy

Build one beautiful chapter, not an infinite system.

The MVP succeeds if a viewer can understand, within 60 seconds, that this is not a chatbot. It is a governed adventure engine that uses AI for expression.

The first chapter should have enough drama to show:

- persuasion
- inspection
- item use
- magic
- nonlethal combat
- failure
- victory
- generated image continuity

## Later Vision

After the MVP works, Framewalker can add:

- chapter generator
- multiple mission templates
- persistent character
- art style presets
- inventory systems
- richer battle mechanics
- generated death/victory frames
- multiple genres
- player-created chapters

The "never-ending story" version should be implemented as an endless chain of bounded chapters, not as unbounded freeform continuation.

