---
title: "angel at the dock master spec"
source_archive: "Software Projects"
source_path: "####Software Projects/Games /Angel at the dock/angel-at-the-dock-master-spec.docx"
status: active
privacy: working
tags:
  - product
---

# angel at the dock master spec

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
The Angel at the Dock

Master Spec — Parked Build

An AI-dialogue RPG where growing up is the leveling system, conversation is combat, intuition is the guide, and death teaches you what your ego missed.

Status: Spec only. Parked until Anchor V4 ships.

Author: Marcus, with Charlie

Eagle Rocket LLC

0. Purpose of This Document

This is a parking artifact. It captures the full concept, mechanics, technical architecture, and phased build plan for The Angel at the Dock so the idea does not have to live in working memory while Anchor V4 is being shipped to production.

Doctrine: production not more features. Anchor ships first. This doc is lifted, not coded, when Anchor V4 is live and stable.

This is not a game design document for a publisher. It is a director's spec — written so that future Marcus, with CC and Codex, can pick up exactly where the thinking stopped.

1. Concept in One Breath

You are born as a baby boy on an island in Indonesia. Each year of your life is one level. Every encounter is a real, spoken conversation with an AI character — your father, a fisherman, a teacher, a stranger, a god in disguise. You are guided, sometimes, by an angel that only speaks when you are spiritually fit. You can die. You will die. When you do, you wake again as a child, and the angel remembers.

The game is a meditation on growing up, paying attention, and becoming someone who listens.

2. Why This Game, Why Now

2.1 The unfair advantages

Indonesian island setting. Marcus is living it. The texture, the water, the sounds, the rhythms of the village — that authenticity is impossible to fake and almost no Western indie has used it.

AI-native development. Marcus is operating with agentic workflows. Asset generation, dialogue authoring, evaluator design, and code production are all radically faster than traditional indie pipelines.

Voice-first dialogue as combat. Whisper makes spoken input cheap and reliable. Almost no one is shipping spoken-LLM combat in a 2D RPG. This is the differentiator.

Director Model fit. This project is exactly the kind of work that proves the fCTO thesis: one operator, multiple agents, shipping a non-trivial product.

2.2 The honest risks

Scope creep is the existential threat. The concept naturally wants to expand — multiple lives, randomization, branching, every island. Discipline to stay linear and small for V1 is the whole game.

Evaluator quality is the technical risk. The judge layer that scores player dialogue is the hard part, not the rendering or the API call.

Voice-only could exclude players. Mitigated by offering text fallback, but voice should be primary for the intended experience.

Latency. LLM round-trip plus TTS must feel responsive enough not to break dramatic tension. Target sub-3-second perceived response.

3. Design Pillars

Every feature decision is tested against these four pillars. If a feature does not serve at least one, it does not ship.

Pillar 1 — Age is the leveling system

The protagonist ages one year per scene resolved. Each age has its own sprite, its own moves, its own vulnerabilities. There is no XP bar. There is only time.

Pillar 2 — Conversation is combat

Combat is not turn-based menus. It is real spoken dialogue with a character whose internal state, goals, and persuasion vectors are hidden. You win by being heard, not by hitting harder.

Pillar 3 — Intuition is the guide

The angel mechanic represents the inner witness — what some traditions call the daimon, what others call conscience or intuition. When the player is spiritually aligned, hints are given. When they are not, they walk blind.

Pillar 4 — Death is a teacher

Death is not failure. It is mythic. When you die, you wake again, and the angel remembers what you forgot. This is Groundhog Day with grace.

4. The Opening — Vertical Slice (V1 MVP)

4.1 Working title

The Angel at the Dock

4.2 Setting

A small fishing village on a quiet Indonesian island. Wooden houses on stilts. Roosters. The smell of salt and frangipani. Mid-morning. The sea is uncharacteristically calm, and that is wrong.

4.3 Protagonist

A seven-year-old boy. Quiet. Curious. Already prone to listening to things adults cannot hear.

4.4 The opening montage (non-playable)

Ages 0 to 6 play as a brief, beautiful montage. Stylized vignettes:

Age 0 — A first cry. A mother's face. Light through palm leaves.

Age 1 — A first word. The player chooses from three options. This choice silently weights a virtue stat.

Age 3 — A first fear. A dog barks too close. A wave too big. A shadow under the house.

Age 5 — A first attachment. A sibling, a grandparent, a stray cat. This NPC will appear later.

Age 6 — A first small skill choice. Fishing, climbing, drawing, singing. This becomes a minor mechanic later.

Total montage length: short. The point is to establish tone, not to gate the game.

4.5 The playable scene begins at age 7

The player wakes in a small room. A rooster crows. Father is downstairs preparing the boat. He has invited his son to come fishing for the first time.

Something is wrong with this morning. The sea is too calm. A frigatebird circles the wrong way. The angel is present, if the player has been spiritually aligned in the montage.

4.6 The dramatic question

Can you, at age 7, convince your father not to take you on this boat — without lying, without tantrum, without disrespect?

4.7 The encounters (in order)

Mother — washing rice in the kitchen. She knows something. She will not say it directly. Win condition: get her to bless your reluctance.

Old fisherman by the dock — has seen weather like this before. Will speak if approached with respect. Win condition: extract the warning he is holding back.

The strange woman by the temple — possibly an angel in human form, possibly senile, possibly both. Speaks in riddles. Win condition: receive the right line to use with father.

Father — at the boat. The final encounter. The one that matters. Win condition: father agrees to delay the trip OR inspects the boat OR leaves you behind without shame.

4.8 The two endings of V1

Ending A — You convinced him.

The boat goes out without you. A storm comes. Father returns three days later, alive, changed. He does not speak of it. The angel says: "You listened." You age to eight. The screen fades. End of V1.

Ending B — You went on the boat.

The storm comes. The boat sinks. Black screen. Then: "You wake again at age seven. The angel remembers." The game restarts at the beginning of the playable scene. The angel is now slightly more present. End of V1.

5. Systems

5.1 The Dialogue Engine — the heart of the game

This is the system that makes the game novel. Everything else is solved problems. This is the part that has to be right.

5.1.1 Architecture

Each NPC encounter has three layers:

Layer 1 — The Character. A system prompt that defines personality, hidden goals, fears, what persuades them, what offends them, what they will never say, what they want the player to see. The character does not know it is in a game.

Layer 2 — The Scene. A scene state object that tracks turn count, established facts, emotional temperature, and any state changes from prior turns.

Layer 3 — The Evaluator. A separate model call that runs after the player speaks and the character responds. The evaluator does not roleplay. Its only job is to score the turn against the hidden win condition and update virtue stats.

5.1.2 Why three layers, not one

A single prompt that tries to roleplay AND judge will collapse. The character must be free to refuse, redirect, or be persuaded organically. The judge must be cold, structured, and consistent. Separating them is the whole trick.

5.1.3 Evaluator output schema

{

"win_condition_progress": 0.0 to 1.0,

"virtues": {

"truthfulness": -1 to +1,

"courage": -1 to +1,

"compassion": -1 to +1,

"manipulation": -1 to +1,

"avoidance": -1 to +1

},

"scene_should_end": boolean,

"outcome": "win" | "loss" | "neutral" | "continuing",

"angel_hint_eligible": boolean,

"private_reasoning": "..."

}

5.1.4 Voice loop

Player taps a microphone button. Holds to talk.

Audio captured locally. Sent to Whisper API for transcription.

Transcript shown on screen so the player sees their own line.

Transcript sent to Character model. Character responds in text.

Character response sent to TTS (ElevenLabs or OpenAI TTS) with a stable voice ID per character.

Audio plays while text appears in dialogue box.

In parallel: transcript and character response sent to Evaluator.

Evaluator returns JSON. Scene state updates. Virtue stats adjust.

5.1.5 Anti-exploit guardrails

The evaluator has access to the hidden win condition. The character does not.

Players who try to break character ("ignore previous instructions") receive a fixed in-fiction response: the character looks confused, says something like "I do not understand what you mean," and the turn counts as wasted.

Manipulation virtue increases when the player wins through false promises, threats, or guilt. This affects later angel hint frequency.

5.2 The Angel System

The angel is not a character. It is a UX layer. It manifests as:

A faint chime. The player hears it. No words yet.

A whisper. A short hint, delivered as overlay text and optional audio. Example: "Not this boat. Not today."

A presence. In rare moments, a visible halo or shimmer near an object or NPC.

5.2.1 Spiritual fitness

A hidden stat. Goes up with: truthfulness, compassion, courage, listening, going to the temple, sitting still. Goes down with: manipulation, avoidance, lying to mother, mocking the strange woman, rushing.

The angel speaks more clearly when this stat is high. This is the entire reward loop. Not gold. Not XP. Attention.

5.3 Movement and Exploration

Top-down 2D, Zelda-style. Tile-based map.

V1 map is one small village: house, kitchen, dock, temple, beach. Maybe ten screens, generously.

Walking is unhurried. There is no run button in V1. The pace is part of the meaning.

Interactions are radius-based. Walk near an NPC, press a button, dialogue begins.

5.4 Aging and Death

V1 only spans a single scene at age 7. But the architecture should support aging from V1, even if only one age is implemented. This means:

A central PlayerState object includes: age, sprite_set, virtue_stats, spiritual_fitness, lives_lived, memories_carried.

On scene resolution, age increments. Sprite swaps. Stats persist.

On death, age resets to scene start. lives_lived increments. memories_carried captures specific learned facts (e.g., "the storm comes from the south").

6. Technical Architecture

6.1 Stack

Game engine: Phaser 3 (TypeScript). Web-native, runs in browser, no install friction.

Hosting: Vercel for the web build.

Backend: Lightweight Node API (Vercel functions or Fly) for LLM calls. Never call models directly from the client — keys must stay server-side.

Models: Claude Sonnet for character roleplay, Claude Haiku or GPT-4o-mini for evaluator (cheap and fast). Whisper for STT. ElevenLabs or OpenAI TTS.

State: Local storage for V1. No server DB needed yet. Save the PlayerState as JSON.

Asset generation: agentic pipeline. Sprites via image gen + post-processing. Tile sets sourced from open-licensed packs initially, replaced over time.

6.2 Critical separations

Character prompts and evaluator prompts live in separate files. They are versioned. They are tested independently.

Win conditions are data, not code. A scene config file defines NPCs, win conditions, and angel hints. The engine reads config, does not hardcode.

Voice is feature-flagged. Text input is always available. Voice is the primary mode but cannot be the only mode.

6.3 Latency budget

Whisper transcription: ~1s for short utterances.

Character response (streaming): first token ~500ms, full short response ~1.5s.

TTS: ~1s for short lines (streaming TTS preferred).

Evaluator: runs in parallel with TTS, ~1s. Does not block player.

Total perceived latency target: under 3 seconds from end of player speech to start of character speech. Achievable but not trivial.

6.4 Cost model (rough V1)

A single playthrough of V1 (one scene, ~15 dialogue turns across 4 NPCs): roughly $0.20–$0.50 in API costs.

This is fine for a free demo. Becomes a real consideration if the game scales.

V1 should include a per-session token cap as a safety rail.

7. Phased Build Plan

No time estimates per Marcus's directive. Phases are sequential. Each phase has a clear ship gate.

Phase 0 — Prerequisite

Anchor V4 is live in production and stable for at least one full week.

If this is not true, no work begins on this project.

Phase 1 — The Dialogue Engine, headless

Goal: prove the dialogue + evaluator architecture works in a terminal. No game. No graphics.

Build a CLI that loads one character config, accepts text input, returns character response, runs evaluator, prints virtue scores.

Test with the father-on-the-boat scene as the first character.

Iterate until the evaluator scores feel honest. This is the riskiest part of the whole project.

Ship gate: a non-Marcus playtester can have a real conversation with the father and feel the win condition is fair.

Phase 2 — Voice in, voice out, headless

Goal: add Whisper and TTS to the CLI. Still no game.

Press-to-talk in a small web UI.

Whisper transcription roundtrip.

Stable TTS voices for father, mother, fisherman, strange woman.

Ship gate: a voice conversation with the father feels emotionally real, not robotic.

Phase 3 — The world

Goal: Phaser overworld with one village, walking character, NPC interaction triggers. No dialogue yet — just walking up to an NPC and triggering a placeholder.

Tile map for the village.

Player sprite, age 7, with walk animations.

Four NPC sprites placed in the world.

Interaction radius and prompt UI.

Ship gate: it looks and feels like a 2D RPG village.

Phase 4 — Integration

Goal: connect the dialogue engine from Phase 1+2 to the world from Phase 3.

Walking up to father triggers the real dialogue scene.

Virtue stats persist between encounters.

Spiritual fitness updates.

Both endings (A and B) are reachable.

Ship gate: V1 vertical slice is complete and playable end-to-end.

Phase 5 — The angel

Goal: implement the angel layer.

Chime, whisper, and presence implementations.

Hint generation tied to spiritual fitness threshold.

Death and rebirth loop with memory carryover.

Ship gate: the player can feel the angel system working.

Phase 6 — Polish and playtest

Audio: ambient sound (waves, roosters, wind), music cues.

UI polish, dialogue box typography.

Three blind playtesters who do not know Marcus.

Rate limit, cost cap, error handling for API failures.

Ship gate: ready to share publicly as a playable demo.

Phase 7 — Public release of the demo

Domain. Landing page. Itch.io listing.

One short video showing a real conversation with the father.

Press post to indie game communities and AI development communities.

8. What V1 Is Not

These are explicit non-goals. Anything in this section that begins to creep in during the build is a scope violation and should be cut on sight.

Not multiple lives or playable ages beyond age 7.

Not multiple islands or maps.

Not character creation. The protagonist is fixed.

Not branching narratives across scenes.

Not procedural generation.

Not multiplayer.

Not mobile-native. Web first, mobile later.

Not monetized. Free demo only.

Not a marketplace, a meta-game, or a roguelike.

If V1 ships well, V2 can earn the right to expand. Not before.

9. Risks and Mitigations

9.1 Evaluator gives bad scores

Mitigation: build evaluator first, iterate longest. Use Council of Models — run identical evaluator prompts across Claude, GPT, Gemini and compare scores on a fixed test set of player responses.

9.2 Players try to break character

Mitigation: in-fiction confusion response. Wasted-turn penalty. Document this behavior in the demo's intro.

9.3 Latency feels broken

Mitigation: aggressive streaming. Show transcript immediately. Begin TTS on first character sentence, not full response.

9.4 API costs spiral

Mitigation: per-session token cap. Cheaper model for evaluator. Cache common opening exchanges.

9.5 Project becomes the new bat

Mitigation: this doc. The phased plan. The Phase 0 gate. Marcus's own track record of parking specs (Sober Garden) successfully.

9.6 Voice introduces accessibility friction

Mitigation: text input is always available alongside voice.

10. What This Proves

If V1 ships, this becomes:

A genuine fCTO portfolio piece. Director Model in action. One operator, multiple agents, novel product.

A press hook. "Marcus Vale shipped the first voice-LLM dialogue RPG" is a real story, not vapor.

A creative integration of Marcus's recovery, philosophy, and craft. Greek ethics encoded in a virtue system. The angel as daimon. Death as metanoia.

Proof that the AI-native development thesis ships finished products, not just demos.

11. Parking Notes

When this doc is lifted, the first three things to do are:

Re-read this entire spec without editing.

Verify Phase 0 prerequisite is met (Anchor V4 in production, stable one full week).

Open Phase 1 only. Do not look at later phases until Phase 1 ships.

Frame to remember: Access the state. Don't be possessed by it.

This game is exciting. Excitement is welcome. But it does not get the keys to the car until Anchor is done.

"This is a probe, not a return."
