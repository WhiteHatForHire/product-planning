---
title: "The Long Border Spec + Prompts MVP"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /The Long Border/The Long Border Spec + Prompts MVP.docx"
status: active
privacy: working
tags:
  - product
---

# The Long Border Spec + Prompts MVP

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Spec

Design thesis

A single-lane economy auto-battler where every stage is a siege with a distinct AI doctrine, a randomized field modifier, and a real rock-paper-scissors unit triangle. Both sides run the same economy. The AI's "intelligence" lives in its doctrine variety and reactive build, not in stat inflation. The player wins by reading what the AI is doing and adapting build order under real-time resource pressure.

Why this isn't derivative

The standard auto-battler trap is "bigger unit = better unit." That's the slop you flagged. Three originality hooks fix it:

Reach-based RPS, not tier-based. Three combat units, hard counters between them via a melee/reach distinction. No unit dominates.

Doctrine AI, not stat-scaling AI. Each stage has a named behavior (rush, wall, raid, starve), not just bigger numbers. Stage 5 "The Hunger Roads" plays fundamentally differently from stage 3 "The Storm."

Symmetric economy, asymmetric doctrine. The AI is bound by the same resource rules you are. It's not a stat block. It's running its own farms and feeling its own resource pressure. The constraint creates real tactical decisions on both sides.

Plus a rogue-like modifier roll per stage so memorization breaks down and replay value emerges.

Closest reference: Stick War meets Slay the Spire stage variety. Distant cousin to PvZ.

Core loop

A stage takes maybe 90-180 seconds. The flow inside a stage:

Pre-stage banner (3 seconds): stage name, AI doctrine hint ("They favor speed"), today's modifier ("Drought: food rate -25%").

Combat phase begins immediately. No build phase. Resources tick. AI starts deploying. You start deploying.

You buy units from a build menu (left panel). Each unit has a cost, a deploy delay, and a march speed. Once deployed, it walks right toward the enemy base.

AI does the same, governed by its doctrine.

Units meet in the middle and fight. Reach mechanics matter (see below).

Whichever side breaches the opposing base first wins the stage.

No pause. No micro. Just deploy decisions under economic pressure.

Units and combat math

Five unit types. Two deploy from gold, three from food, one hybrid. Initial stats:

Unit

Cost

HP

DMG

Speed

Reach

Role

Farmhand

25 gold

5

0

static

0

+1 food/sec

Levy

8 food

6

3

fast

melee

cheap brawler

Wall

14 food

18

1

slow

melee

tank

Spear

12 food

10

4

medium

1-rank reach

reach attacker

Champion

60 gold + 30 food

40

8

medium

melee + cleave

elite

Combat resolution (the math you described, formalized):

When two opposing units meet (their hitboxes touch), they enter combat.

Each unit attacks on its own cooldown (default 0.8s). On attack, target HP -= attacker DMG.

A unit with HP > 0 keeps marching as soon as its target dies. Your "2HP keeps going after killing 1HP" rule is exactly this.

The line is strict: units in the same lane never overlap. They queue. Front-rank fights, ranks behind wait their turn.

The reach mechanic is the RPS pivot:

Spear has 1-rank reach: it can attack the unit in front of its own front-rank ally. So if you put a Wall in front and a Spear behind, the Spear hits the enemy through the Wall while the Wall soaks. This is the formation that beats a wall of Walls.

Levy is fast and cheap: it gets to the front faster than the enemy can stack defense. Levy spam beats Spear because Spears are slow and expensive.

Wall is the soak: it eats Levy attacks all day because Levy DMG is too low to chew through 18 HP fast. Wall beats Levy.

So: Levy beats Spear, Spear beats Wall, Wall beats Levy. Real RPS. No unit is ever "just better."

Champion breaks RPS deliberately as a strategic commitment: it beats anything 1v1 but costs so much of both resources that committing to it leaves you exposed to a swarm response. The decision to deploy a Champion is a real one.

Economy

Two resources, separate sources, separate sinks.

Gold:

Sources: kill enemy units (Levy = 4g, Wall = 8g, Spear = 7g, Champion = 30g), stage clear bonus.

Sinks: Farmhands (25g), upgrades (later stages), Champion partial cost.

Food:

Sources: Farmhands (1/sec each).

Sinks: combat units.

Starting state: 60 gold, 0 food, 1 Farmhand pre-deployed. AI mirrors. Stage scaling raises AI starting gold faster than player's, simulating siege pressure.

Strategic tension: Gold spent on Farmhands means more food later, but no immediate combat unit. Skipping eco means you can field units now but starve later. The doctrine you're facing tells you whether to eco-up (slow AI) or rush (fast AI).

The 10 stages

Each stage = name + doctrine + modifier roll + unit roster.

#

Name

Doctrine

What it teaches

1

The First Probe

Light Levy waves, slow tempo

Basic combat, basic eco

2

The Storm

Levy rush, fast tempo

You need Walls

3

The Iron Line

Heavy Walls advancing slowly

You need Spears (unlocks Spear)

4

Mixed Front

First true RPS test, all three units

Read composition, react

5

The Hunger Roads

"Raiders" — fast units that ignore your line and target Farmhands

Eco protection, lane positioning

6

The Long Wall

Wall-heavy attrition, slow grind

Resource stamina

7

The Champion's Arrival

AI deploys a Champion mid-stage (unlocks player Champion)

Tactical pressure, big-unit decision

8

The Tide

Endless small waves, no breathing room

Tempo war

9

The Black Harvest

Famine + Champion combo

Two-axis pressure

10

The Captain's Stand

Reactive AI: it sees your roster and counter-builds

Real RPS test under final pressure

Each stage's doctrine drives AI build weights and deploy timing. Stage 10's "reactive" AI checks player composition every 3 seconds and biases its next deploys toward the counter. That's the closest you get to "real" AI without an LLM.

Stage modifiers (the rogue-like layer)

One modifier rolled at the start of each stage from a pool. Examples:

Drought: food rate -25%

Bountiful Harvest: food rate +25%

Steel Shortage: Wall cost +30%

Quick March: all units +20% speed

Plague: all units max HP -15%

Conscription: Levy cost halved, Levy max HP -2

Pike Festival: Spear reach +1

Champion's Field: Champion cost halved

Fog of Banners: enemy roster hidden until each unit deploys

Shieldwall Tradition: Wall HP +20%

Modifiers apply to both sides symmetrically. Drought hurts the AI too. This keeps it fair and emergent.

AI design (rule-based, no LLM)

Each stage's AI is a state machine with three layers:

Doctrine weights — bias for unit type selection (e.g., "Storm" = 70% Levy, 20% Wall, 10% Spear).

Tempo rule — how often it deploys, with randomization (e.g., "Storm" deploys every 2-4s, "Long Wall" every 5-8s).

Reactive overlay — light counter-logic. Most stages have one reactive rule (e.g., "if player has 3+ Walls, bias toward Spear"). Stage 10's reactive overlay is full (re-evaluates every 3s).

Resource budgeting: AI runs the same economy. It buys Farmhands when its gold/food ratio drops below a doctrine-specific threshold. It saves for Champion when its doctrine includes Champion deploys.

To make it feel intelligent: AI delays its deploy by 1-2s when it has resources but the player just committed a big unit (creates the impression of "they were waiting"). Cheap trick, real feel.

Architecture leaves a clean seam to swap a doctrine for an LLM call later if you want.

Win, lose, progression

Win stage: breach enemy base (300 HP, takes hits from any unit reaching it).

Lose stage: your base breached.

Progression: win advances to next stage. Lose retries with same starting resources. 50% of unspent gold carries to the next stage on a win. Stage 10 win → campaign complete screen.

No persistent meta-progression for the prototype. Each campaign is a fresh run. If the prototype proves out, meta-progression (unlocked starting bonuses, harder difficulty tiers) is a clean post-prototype add.

Visual approach (no art, vector only)

Canvas 2D. Each unit is a distinct silhouette:

Farmhand: small green square, brown line for sickle

Levy: red triangle, point forward

Wall: wide blue rectangle, narrower than tall

Spear: gray rectangle with a thin line extending forward (the spear), making it visually longer than it is wide

Champion: gold pentagon, ~1.5x size of others

Player units have a blue side-stripe outline; enemy units have a red one. HP bar above each unit. Static base structure at each end (your fort: blue trapezoid; their fort: red trapezoid). Ground line. No background art.

Build menu is a left-side panel: button per unit, cost displayed, disabled when unaffordable, locked icon when not yet unlocked. Stage banner top-center. Resource counters top-left (gold, food). Modifier badge top-right.

File structure

Modular so the agent can build, smoke, commit per module. Vite + vanilla JS. No framework — adds config the agent will fumble.

/long-border

├── index.html

├── package.json

├── vite.config.js

├── /src

│   ├── main.js                 # entry, game loop

│   ├── /game

│   │   ├── state.js            # global game state, current stage, resources

│   │   ├── units.js            # unit definitions, stat tables, factory

│   │   ├── combat.js           # lane resolution, hit detection, reach

│   │   ├── economy.js          # tick, costs, can-afford, buy

│   │   ├── ai.js               # doctrine state machine, deploy logic

│   │   ├── stages.js           # 10 stage definitions, doctrine wiring

│   │   └── modifiers.js        # modifier pool, roll, apply

│   ├── /render

│   │   ├── canvas.js           # canvas setup, frame render orchestration

│   │   ├── units.js            # unit silhouettes, HP bars

│   │   ├── ui.js               # build menu, banners, counters, overlays

│   │   └── effects.js          # death poofs, hit flashes

│   └── /input

│       └── controls.js         # button click handlers

├── /tests

│   └── smoke.js                # asserts: unit factory, combat tick, economy tick, AI deploy, modifier apply

└── README.md

Smoke tests are not unit tests in the rigorous sense. They're a single file that boots the game in headless mode (or with a mock canvas), runs a few scripted scenarios, and asserts core invariants: a Levy vs Levy kills both, a Wall vs Levy kills the Levy and leaves the Wall at HP > 0, the AI deploys at expected tempo for a doctrine, a modifier applies to both sides. Cheap, fast, agent-runnable as a smoke step.

What this gets you that a simpler version doesn't

A simpler version (single unit type, stat-scaled enemy) would be a 200-line prototype that proves the engine but not the design. The Long Border as specced proves the design: it has a real RPS to discover, real economic decisions, real per-stage variety, and real AI feel. After 10 stages a player will have learned a vocabulary, not just memorized a stat curve.

The whole spec is intentionally scoped to be agentically buildable in one prompt with checkpoints. No persistent storage, no metaprogression, no save system, no audio, no art pipeline, no networking. Pure single-file-feeling browser prototype with enough modular architecture that the agent can build → smoke → commit per module.

When you want, the next move is the agentic build prompt: preflight, scaffold, implement-by-module, smoke after each module, commit per green checkpoint, revert on failure, retry. I'd structure that as a directive prompt with explicit phase gates so CC or Codex doesn't try to one-shot the whole thing and stall mid-build. Say go and I'll write it.

Prompt

The prompt below is a single directive, designed to be pasted into CC or Codex with autonomous execution permissions. The structural innovations: smoke-first per module, a vertical-slice gate at Phase 4 that forces an end-to-end playable build before depth, and an explicit revert-and-branch protocol so the agent doesn't pile fixes on broken state.

# THE LONG BORDER — AGENTIC BUILD DIRECTIVE

# Single-lane economy auto-battler. Browser. Vector primitives only. No external assets.

## 1. ROLE

You are a senior game-engine contributor implementing The Long Border. You build phased, smoke-gated, commit-disciplined. You do not improvise architecture, you do not add dependencies, you do not skip smoke tests, you do not advance phases until the previous one is green and committed. You write production-grade vanilla JavaScript with intent. No filler, no decorative comments, no defensive try/catch around code that cannot throw.

## 2. OPERATING DOCTRINE (apply to every phase)

1. Smoke-first. Before implementing a module, write the smoke assertions for that module. The assertions describe the contract. The implementation makes the contract pass. Write the assertion file, watch it fail, then write the code that makes it pass. This is non-negotiable.

2. Vertical slice early. By the end of Phase 4 the game must be playable end-to-end: one stage, basic units, working combat, working win/lose. Everything after Phase 4 deepens what already plays. Do not build breadth before depth.

3. Phase gate. Each phase ends only when: (a) smoke for that phase is green, (b) the change is committed with the prescribed message format, (c) the working tree is clean. No advancing on yellow.

4. Revert on red. If smoke fails twice after fix attempts within a phase, revert hard to the last green commit and open a new branch named `attempt/phase-N-try-M`. Do not pile fixes on broken state. Reverts are a tool, not a panic.

5. Halt and surface. If three consecutive phase attempts fail, stop. Output a diagnosis: what was attempted, what failed, what the next move would be. Do not silently degrade scope or skip features.

6. No invention. If something is not specified here, choose the simplest option that satisfies the contract and document the choice in the commit message under a "Decisions:" footer line.

7. Commits are checkpoints, not narration. One commit per phase minimum, more if a phase has natural sub-checkpoints. Never commit broken code. Never amend a green commit.

## 3. STACK (fixed)

- Vite, vanilla JS template. Node 20 or higher.

- ES modules. No TypeScript. No JSX. No build steps beyond Vite's default.

- Canvas 2D for all rendering. No WebGL, no PixiJS, no Phaser, no Three.

- Vitest for smoke tests. No Jest. No Playwright. No Cypress.

- Plain CSS in a single file. No preprocessors.

- Git via local repo, conventional commits.

## 4. DO NOT ADD (common agent inventions, all forbidden)

- React, Vue, Svelte, Solid, or any UI framework

- Tailwind, styled-components, CSS-in-JS

- TypeScript or .d.ts files

- Lodash, Ramda, immer, zustand, redux, mobx

- Icon packs, font CDNs, image assets, audio assets

- ESLint or Prettier configs beyond Vite defaults

- Service workers, PWA manifests

- Any npm package outside the explicit dependency list: vite, vitest

If you find yourself reaching for a dependency, stop and reconsider. The answer is plain JS.

## 5. GAME DESIGN DATA

### 5.1 Unit roster

| Unit | Cost | HP | DMG | Speed (px/s) | Reach | Atk Interval | Notes |

|---|---|---|---|---|---|---|---|

| Farmhand | 25 gold | 5 | 0 | 0 | 0 | n/a | static, +1 food/sec |

| Levy | 8 food | 6 | 3 | 90 | melee | 0.7 s | cheap fast brawler |

| Wall | 14 food | 18 | 1 | 50 | melee | 1.0 s | tank |

| Spear | 12 food | 10 | 4 | 70 | 1-rank | 0.9 s | reach attacker |

| Champion | 60 gold + 30 food | 40 | 8 | 70 | melee + 30px cleave | 0.8 s | elite |

Bounty (gold awarded for kill): Levy 4, Wall 8, Spear 7, Champion 30, Farmhand 0.

### 5.2 Combat math

- Each unit has its own attack cooldown timer. When in range and cooldown ≤ 0, deal DMG to target, reset cooldown to attack interval.

- A unit with HP > 0 keeps marching after its target dies. The "two-HP marches on after killing one-HP" rule is exactly this.

- Single lane, strict line. Units of the same side queue behind their front rank, never overlap.

- Reach mechanic: a Spear in rank 2 can attack the enemy front-rank unit through its own front-rank ally. Implement reach as: a unit with reach > 0 can target an enemy whose distance is within (its own attack range + reach × rank-spacing). Rank-spacing = 28 px.

- Champion cleave: on each Champion attack, all enemy units within 30 px of the primary target also take half damage (rounded down).

- Bases: each side has a base at the edge with 300 HP. When a unit reaches the enemy edge with no enemy in melee range, it deals its DMG to the base on its attack cooldown.

### 5.3 Economy

- Player and AI start each stage with: 60 gold, 0 food, 1 Farmhand pre-deployed at their side. AI gets a stage-scaled starting gold bonus per the table in 5.4.

- Gold sources: kill bounties, stage clear bonus (50 gold).

- Gold sinks: Farmhands, Champions (gold portion), upgrades (later, if scoped).

- Food sources: Farmhands generate 1 food/sec each. Tick globally every 1 second.

- Food sinks: Levy, Wall, Spear, Champion (food portion).

- Carry-over: 50% of unspent gold carries between stages on a win. Food does not carry.

- Cannot deploy a unit you cannot afford. Deploy is instant on click; no queue, no build time. The cost is paid at click.

### 5.4 Stages 1-10

Each stage = name + AI doctrine + AI starting gold + reactive overlay flag + roster.

| # | Name | Doctrine | AI Start Gold | Reactive | Roster |

|---|---|---|---|---|---|

| 1 | The First Probe | Slow Levy waves, deploy every 5-7s | 60 | no | Levy, Farmhand |

| 2 | The Storm | Levy rush, deploy every 2-4s, 90% Levy 10% Wall | 80 | no | Levy, Wall, Farmhand |

| 3 | The Iron Line | Wall-heavy, 60% Wall 30% Levy 10% Spear, deploy every 4-6s | 100 | no | Levy, Wall, Spear, Farmhand |

| 4 | Mixed Front | Balanced 33/33/33, deploy every 3-5s | 120 | light (counter biggest stack) | Levy, Wall, Spear, Farmhand |

| 5 | The Hunger Roads | Standard mix + 20% chance Raider deploys (Raider = Levy variant that ignores enemy line and targets Farmhands) | 140 | no | Levy, Wall, Spear, Raider, Farmhand |

| 6 | The Long Wall | 70% Wall 20% Spear 10% Levy, deploy every 5-8s, attrition focus | 160 | no | Levy, Wall, Spear, Farmhand |

| 7 | The Champion's Arrival | Standard mix + AI saves for and deploys 1 Champion at 60s mark | 180 | light | Levy, Wall, Spear, Champion, Farmhand |

| 8 | The Tide | Levy + Spear spam, deploy every 1.5-3s, lots of small units | 200 | no | Levy, Wall, Spear, Farmhand |

| 9 | The Black Harvest | Hunger Roads doctrine + Champion deploy at 45s | 220 | light | Levy, Wall, Spear, Raider, Champion, Farmhand |

| 10 | The Captain's Stand | Reactive AI re-evaluates every 3s, builds counters to player's largest unit class | 260 | full (every 3s) | full roster |

Reactive overlay logic: every N seconds (3s for full, 6s for light), AI samples the player's currently-deployed units. It identifies the player's most-numerous unit class and biases its next 3 deploys toward that class's counter (Levy counter = Wall, Wall counter = Spear, Spear counter = Levy, Champion counter = mass Spear).

Raider unit (stage 5+): Levy variant. Cost: AI-only, free deploy. HP 5, DMG 2, speed 110, no melee priority. Behavior: passes through enemy line if a Farmhand is reachable, attacks Farmhand directly. If no Farmhand reachable, falls back to standard Levy behavior.

### 5.5 Stage modifiers (rolled once per stage, applied symmetrically)

Pool of 10. Roll one randomly at stage start. Display in top-right banner.

1. Drought — food rate ×0.75

2. Bountiful Harvest — food rate ×1.25

3. Steel Shortage — Wall cost ×1.30 (round up)

4. Quick March — all units speed ×1.20

5. Plague — all units max HP ×0.85 (round down, min 1)

6. Conscription — Levy cost halved (round up), Levy max HP -2

7. Pike Festival — Spear reach +1

8. Champion's Field — Champion total cost halved

9. Fog of Banners — enemy roster hidden in pre-stage banner; units render with neutral silhouettes for first 0.5s after deploy

10. Shieldwall Tradition — Wall HP ×1.20

Stage 1 always has no modifier (clean tutorial). Stages 2-10 always roll one.

### 5.6 Player unit unlocks

- Stage 1: Farmhand, Levy

- Stage 2: + Wall

- Stage 4: + Spear

- Stage 7: + Champion

Locked units render in build menu with a lock icon and the stage they unlock at.

### 5.7 Win/lose & progression

- Win stage: enemy base HP reaches 0.

- Lose stage: player base HP reaches 0.

- Win → next stage. Lose → retry current stage with starting resources.

- Stage 10 win → "Campaign Complete" screen with run stats (time elapsed, units lost, gold remaining).

## 6. FILE STRUCTURE

/long-border ├── index.html ├── package.json ├── vite.config.js ├── vitest.config.js ├── /src │ ├── main.js │ ├── style.css │ ├── /game │ │ ├── state.js │ │ ├── units.js │ │ ├── combat.js │ │ ├── economy.js │ │ ├── ai.js │ │ ├── stages.js │ │ └── modifiers.js │ ├── /render │ │ ├── canvas.js │ │ ├── units.js │ │ ├── ui.js │ │ └── effects.js │ └── /input │ └── controls.js ├── /tests │ ├── economy.smoke.js │ ├── combat.smoke.js │ ├── ai.smoke.js │ ├── modifiers.smoke.js │ └── stages.smoke.js └── README.md

## 7. PHASE PLAN

### Phase 0 — Preflight

Goal: clean repo, working dev server, working test runner, file scaffolds (empty exports).

1. Verify `node --version` >= 20. If not, halt and surface.

2. `npm create vite@latest long-border -- --template vanilla`. cd in.

3. `git init`. `.gitignore` with node_modules, dist, .DS_Store.

4. `npm install`. `npm install --save-dev vitest`.

5. Create the full file structure from section 6 with empty placeholder exports for every module (e.g., `export const init = () => {}`).

6. Add `"test": "vitest run"` and `"test:watch": "vitest"` to package.json scripts.

7. Write a single trivial smoke test that asserts `1 === 1` to verify vitest runs.

8. Run `npm run dev` and verify it serves at localhost. Run `npm test` and verify the trivial smoke passes.

9. Commit: `chore(phase-0): preflight scaffold`.

Gate: dev server starts, vitest runs, all files exist as empty modules, trivial smoke passes.

### Phase 1 — State + Economy

Goal: state model and economy tick implemented, smoke-tested.

1. Write `tests/economy.smoke.js` first. Assertions:

- Initial state: 60 gold, 0 food, 1 Farmhand on player side, expected AI starting gold per stage.

- Tick at +1s: each Farmhand contributes 1 food. 1 Farmhand → 1 food.

- Buy Farmhand at 25 gold: gold -= 25, Farmhand count += 1.

- Cannot buy when broke: state unchanged, returns false.

- Kill bounty: applying a kill of Levy adds 4 gold to opponent.

2. Implement `src/game/state.js`: factory for initial state given a stage number. Single source of truth. No globals.

3. Implement `src/game/economy.js`: `tickEconomy(state, dt)`, `canAfford(state, side, cost)`, `applyCost(state, side, cost)`, `applyBounty(state, side, unitType)`.

4. Run smoke. Green → commit `feat(phase-1): state and economy core`.

Gate: economy.smoke.js fully green.

### Phase 2 — Units + Combat

Goal: unit factory, lane resolution, reach mechanic, base damage. No rendering.

1. Write `tests/combat.smoke.js` first. Assertions:

- Levy vs Levy: after combat resolves, both dead.

- Wall (HP 18) vs Levy (HP 6, DMG 3): Wall lives, ends with HP > 12 (Wall took ≤ 6 damage before Levy died). Levy dead.

- Spear vs Wall with Levy in front of Wall: Spear can damage Wall through reach. Run a tick where Spear's rank-2 enemy is the Wall behind a Levy front rank. Spear deals damage to Wall, not to fronting Levy.

- Champion cleave: a Champion attacks a Levy with two other Levies within 30px. Primary takes 8, others take 4.

- Base damage: a Levy reaches the enemy edge with no defenders. Base HP decreases by 3 per attack interval.

2. Implement `src/game/units.js`: unit factory, stat table from section 5.1, unit type constants.

3. Implement `src/game/combat.js`: `tickCombat(state, dt)` that handles movement, line queueing, range checks, attack cooldowns, damage application, death cleanup, base damage. Pure function over state.

4. Run smoke. Green → commit `feat(phase-2): unit roster and combat resolution`.

Gate: combat.smoke.js fully green. Reach mechanic provably working.

### Phase 3 — AI doctrines + stage definitions

Goal: AI deploys per doctrine, stage definitions wired, reactive overlay working.

1. Write `tests/ai.smoke.js` and `tests/stages.smoke.js` first.

- ai.smoke: a Storm-doctrine AI given 100 gold over 30s deploys roughly 90% Levy. Assert ratio within ±15%.

- ai.smoke: a reactive AI sampling a player roster of 4 Walls + 1 Levy biases next 3 deploys toward Spear.

- ai.smoke: stage 7 Champion deploy fires at the 60s mark ±5s if AI has resources.

- stages.smoke: each of the 10 stage configs is a valid object with required fields.

2. Implement `src/game/stages.js`: array of 10 stage configs as defined in section 5.4.

3. Implement `src/game/ai.js`: doctrine evaluator. Function `tickAI(state, dt)` that maintains internal AI timers, samples doctrine weights, applies reactive overlay if enabled, deploys units when affordable.

4. Run smoke. Green → commit `feat(phase-3): doctrine AI and stage configs`.

Gate: ai.smoke and stages.smoke green. Reactive overlay measurably changes deploy bias.

### Phase 4 — VERTICAL SLICE: playable Stage 1

Goal: end-to-end playable game. Stage 1 only. Levy + Farmhand only. Render + input + game loop wired up. Win/lose works.

1. Implement `src/render/canvas.js`: canvas init, frame loop with `requestAnimationFrame`, dt computation (cap at 0.1s), render orchestration.

2. Implement `src/render/units.js`: Levy and Farmhand silhouettes (red triangle, green square + brown line). HP bar above each. Side-stripe outline (blue for player, red for enemy).

3. Implement `src/render/ui.js`: gold/food counters top-left, build menu left side with Levy and Farmhand buttons (cost, disabled state), base HP bars at each edge.

4. Implement `src/input/controls.js`: button click handlers wired to economy buy actions.

5. Implement `src/main.js`: bootstrap, start Stage 1, run game loop, detect win/lose, show win/lose overlay with Restart button.

6. Manual playtest: deploy Farmhand, deploy Levy, win the stage. Then lose the stage by under-building. Both end states must trigger overlay correctly.

7. Run all prior smoke. Green → commit `feat(phase-4): vertical slice — playable stage 1`.

Gate: human-verifiable playable game. Stage 1 winnable and losable. All prior smoke still green.

This is the most important gate. If you cannot play Stage 1 end-to-end, do not advance. Halt and diagnose.

### Phase 5 — Full unit roster + RPS

Goal: Wall, Spear, Champion deployable and rendering. RPS verified.

1. Add Wall (blue rectangle), Spear (gray rectangle with extending line), Champion (gold pentagon, 1.5x size) to `render/units.js`.

2. Add buttons to `render/ui.js` build menu with lock icons for not-yet-unlocked units.

3. Verify in playtest: deploy Wall, Spear, Champion. Verify Spear reach visually (Spear behind Wall hits enemy through Wall).

4. Add a smoke assertion in combat.smoke for full roster combat (already covered if Phase 2 was thorough; extend if needed).

5. Commit `feat(phase-5): full unit roster, RPS verified`.

Gate: all four combat units deployable, render correctly, combat math proven. RPS observable in play.

### Phase 6 — Modifiers

Goal: modifier system implemented, applied symmetrically, displayed in UI.

1. Write `tests/modifiers.smoke.js` first. Assertions:

- Each modifier in the pool of 10 is a valid object with apply function.

- Drought reduces food tick to 0.75/sec per Farmhand.

- Steel Shortage raises Wall cost to round-up of 14 × 1.30 = 19.

- Pike Festival raises Spear reach from 1 to 2.

- Stage 1 has no modifier; stages 2-10 always have one.

2. Implement `src/game/modifiers.js`: pool, roll function (deterministic given seed for testability), apply function that mutates stage config.

3. Wire modifier roll into stage start in `main.js`. Display modifier name in top-right banner.

4. Run smoke. Green → commit `feat(phase-6): stage modifiers`.

Gate: modifiers.smoke.js green. Modifier visible in banner. At least three modifiers manually verified in play.

### Phase 7 — All 10 stages + progression

Goal: campaign playable from stage 1 to stage 10, with progression, base HP, win/lose carry-over.

1. Wire stage transitions: on win, apply 50 gold bonus + 50% gold carry, advance stage index, reset combat state, roll new modifier, show pre-stage banner. On lose, reset stage with starting resources.

2. Implement Champion deploy timing for stages 7 and 9 in `ai.js` (saved-up gold deploy).

3. Implement Raider variant for stages 5 and 9 in `units.js` and `combat.js` (priority-targets Farmhands, free deploy for AI).

4. Implement reactive overlay for stage 10 (every 3s, full counter logic).

5. Implement Campaign Complete screen with run stats.

6. Manual playtest: complete the full campaign. Lose at least one stage to verify retry. Win stage 10 to verify campaign-complete flow.

7. Commit `feat(phase-7): full campaign progression`.

Gate: full 10-stage campaign playable. All doctrines observable. Reactive AI demonstrably countering.

### Phase 8 — Polish

Goal: hit flashes, death effects, banner readability, edge-case fixes.

1. Implement `src/render/effects.js`: brief white flash on hit, small fade-out poof on death.

2. Tune banner timing (3s pre-stage banner with stage name, doctrine hint, modifier).

3. Fix any visual bugs from playtest: HP bar clipping, unit overlap edge cases, UI z-order.

4. Final manual playtest pass.

5. Update README with: how to run, how to test, design summary, controls.

6. Commit `polish(phase-8): effects, banners, readme`.

Gate: clean visual presentation, README accurate, all smoke green, working tree clean.

## 8. SMOKE DISCIPLINE

Smoke tests are not unit tests in the rigorous sense. They are behavioral assertions on the game's contracts. Keep them:

- Fast (whole suite under 1 second).

- Deterministic (use seeded RNG for any random behavior).

- Behavioral (assert observable outcomes, not internal structure).

- Few but pointed. Each assertion proves a contract.

Do not test private functions. Do not mock the canvas. Do not write assertions that pass trivially. Each assertion you write should fail meaningfully if its contract breaks.

## 9. COMMIT PROTOCOL

Format:

type(phase-N): summary

Body if needed.

Decisions:

Any unspecified choices made and why

Types: feat, fix, chore, polish, refactor, docs.

One commit per phase minimum. More within a phase is fine if there's a natural sub-checkpoint.

Never commit broken code.

Never amend a green commit.

Always commit before advancing phases.

## 10. REVERT & HALT

Revert protocol:

- Smoke fails → fix attempt 1.

- Smoke fails again → fix attempt 2.

- Smoke fails third time → `git reset --hard {last-green-commit}`. Branch `attempt/phase-N-try-M`. Restart phase from scratch. Log the abandoned attempt's failure mode in the new branch's first commit message under "Previous attempt failure:".

Halt protocol:

- Three consecutive phase attempts fail → halt.

- Output: phase number, attempt history, root failure analysis, recommended next move.

- Do not silently degrade scope. Do not skip the failing phase. Do not move on without surfacing.

## 11. ANTI-PATTERNS (immediate red flags, do not commit if any are present)

- Decorative comments explaining what the code obviously does

- try/catch wrapping code that cannot throw

- Defensive null checks against state shapes you control

- Magic numbers without named constants for game values

- Mutating state outside designated mutator functions

- Console.log statements in committed code (use only during debugging, remove before commit)

- Adding a dependency to fix a problem solvable in 10 lines of vanilla JS

- "Helper" abstractions used in only one place

- Premature optimization (cache, memoization, object pools) before measured need

- Smoke tests that assert internal structure instead of observable behavior

## 12. GO

Execute Phase 0 immediately. Surface progress per phase with a one-line status. Do not pause for confirmation between phases unless a halt condition triggers. The directive above is your single source of truth.

Begin.

That's the full directive. Three things to know before you fire it:

The vertical-slice gate at Phase 4 is the most important load-bearing rule. If the agent gets to Phase 4 and cannot produce a playable Stage 1, that's where the design or the agent's interpretation has broken down, and the halt-and-surface protocol exists to catch it before Phase 5+ pile complexity on top. Do not let it advance past Phase 4 on a partial slice.

The smoke-first instruction is genuinely costly in agent tokens but pays off because the agent thinks about the contract before the implementation. Without it, agents tend to write implementations that "work" against assertions written to match what they happened to build. With it, the assertion is the spec.

If you want a Council of Models pass on the prompt itself before firing it, run this same text through Codex / Gemini / Grok with the question "what would break if a competent agent executed this exactly as written?" Their answers usually surface the one ambiguity that sinks the build. Cheap insurance.
