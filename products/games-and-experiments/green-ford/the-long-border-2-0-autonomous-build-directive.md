---
title: "THE LONG BORDER 2.0 — AUTONOMOUS BUILD DIRECTIVE"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Green Ford/THE LONG BORDER 2.0 — AUTONOMOUS BUILD DIRECTIVE.docx"
status: reference
privacy: working
tags:
  - product
---

# THE LONG BORDER 2.0 — AUTONOMOUS BUILD DIRECTIVE

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
═════════════════════════════════════════════════════════════════

THE LONG BORDER 2.0 — AUTONOMOUS BUILD DIRECTIVE

Single-pass build. Self-healing. Defer-and-continue.

═════════════════════════════════════════════════════════════════

Branch: rebuild/v2 (created from preview/phase-4)

Mode: autonomous. No human input expected mid-build.

Output: working game + docs/deferred-issues.md + BUILD_REPORT.md

═════════════════════════════════════════════════════════════════

1. ROLE

═════════════════════════════════════════════════════════════════

You are a senior contributor implementing a complete rebuild of

The Long Border in a single autonomous pass. You self-heal failures

when possible, defer them to a tracking document when not, and

continue. You commit liberally and never lose work. You stop only

for the explicit hard-stop conditions in section 13.

═════════════════════════════════════════════════════════════════

2. AUTONOMY DOCTRINE

═════════════════════════════════════════════════════════════════

Three response tiers, in order:

TIER 1 — SELF-HEAL

Try the explicit fix in section 8 (Self-Repair Playbook).

Two attempts maximum per issue. If self-heal succeeds, continue.

TIER 2 — DEFER AND CONTINUE

If self-heal fails after two attempts:

- Log issue to docs/deferred-issues.md per section 11 format

- Stub or skip the failing element so the rest of the system works

- Mark related smoke tests with it.skip() + DEFERRED comment

- Commit current state with deferred summary in commit message

- Continue with the next item in the phase

TIER 3 — HARD STOP

Only halt for the conditions in section 13. Before halting:

- Commit all in-progress work to a halt-N branch

- Generate BUILD_REPORT.md with current status

- Surface the halt reason

NEVER:

- Ask for human input mid-build

- Wait for review between phases

- Skip generating deferred-issues.md or BUILD_REPORT.md

- Stop for "I'm not sure if this is right" — defer it and move on

- Commit partial broken code without marking it deferred

═════════════════════════════════════════════════════════════════

3. STACK

═════════════════════════════════════════════════════════════════

- Vite, vanilla JS, ES modules, Node 20+

- Canvas 2D, DOM/CSS

- Vitest for smoke tests

- Howler.js (cdnjs) for music; Web Audio API for SFX

- Git, conventional commits

═════════════════════════════════════════════════════════════════

4. DO NOT ADD

═════════════════════════════════════════════════════════════════

- React, Vue, Svelte, Solid, Phaser, any framework

- Tailwind, styled-components, CSS-in-JS

- TypeScript or .d.ts files

- Lodash, Ramda, immer, zustand, redux

- Image/font/audio asset files (SFX synthesized; music streamed)

- Any npm package outside: vite, vitest

═════════════════════════════════════════════════════════════════

5. CURRENT STATE

═════════════════════════════════════════════════════════════════

On preview/phase-4 (branch from here):

- Phases 0-4 committed; 24 smoke tests green

- Single-lane combat, Stage 1 only, Levy + Farmhand

- Live: long-border.vercel.app

What's reusable (refactor, do not rewrite):

state.js, economy.js, combat.js, ai.js, rng.js, units.js,

stages.js (Stage 1 config)

What's a placeholder: modifiers.js (empty)

What's missing: campaign system, all visual polish, audio,

remaining stages, all new units, lane architecture

═════════════════════════════════════════════════════════════════

6. GAME DESIGN — V2 SPEC

═════════════════════════════════════════════════════════════════

6.1 THREE-LANE ARCHITECTURE

═══════════════════════════

CANVAS: 1100 × 620

LAYOUT (top to bottom):

y=0..80:    Farm zone (split at x=550, player left, enemy right)

y=80..170:  TOP lane     (combat line y=125)

y=170..255: Grass divider

y=255..345: CENTER lane  (combat line y=300)

y=345..430: Grass divider

y=430..520: BOTTOM lane  (combat line y=475)

y=520..620: Decorative ground

BASES: x=0..60 (player), x=1040..1100 (enemy). Three visible

gates aligned with lanes. SHARED base HP (300 per side).

LANES MODULE (src/game/lanes.js):

export const LANES = ['top', 'center', 'bottom'];

export const LANE_Y = { top: 125, center: 300, bottom: 475 };

export const ADJACENT = {

top: ['center'],

center: ['top', 'bottom'],

bottom: ['center']

};

DEPLOY: Build menu has lane selector (▲ ● ▼). Selected lane

applies to next deploy. Default: center.

6.2 UNIT ROSTER

═══════════════

PLAYER UNITS

| Unit | Cost | HP | DMG | Speed | Range | AtkInt | Armor | Special | Unlock |

|---|---|---|---|---|---|---|---|---|---|

| Farmhand | 25g | 5 | 0 | 0 | - | - | 0 | +1 food/sec, farm zone | S1 |

| Levy | 8f | 6 | 3 | 90 | melee | 0.7s | 0 | - | S1 |

| Wall | 14f | 18 | 3 | 50 | melee | 1.0s | 2 | - | S2 |

| Spear | 12f | 10 | 4 | 70 | reach 1 | 0.9s | 0 | hits past front rank | S3 |

| Archer | 10f | 5 | 3 | 60 | 200px | 1.1s | 0 | rear-rank fire, in-lane | S4 |

| Mage | 30g+10f | 7 | 5 | 60 | 150px | 1.4s | 0 | CROSS-LANE adjacent | S6 |

| Ballista | 30g+15f | 8 | 8 | 30 | 400px | 2.5s | 0 | AOE primary+1 behind | S7 |

| Champion | 60g+30f | 40 | 8 | 70 | melee+30 cleave | 0.8s | 1 | elite | S8 |

ENEMY UNITS

| Unit | HP | DMG | Speed | Range | AtkInt | Armor | Special | First |

|---|---|---|---|---|---|---|---|---|

| Levy | 6 | 3 | 90 | melee | 0.7s | 0 | - | 1 |

| Wall | 18 | 3 | 50 | melee | 1.0s | 2 | - | 2 |

| Spear | 10 | 4 | 70 | reach 1 | 0.9s | 0 | - | 3 |

| Hunter | 5 | 3 | 60 | 200px | 1.1s | 0 | rear-rank archer | 4 |

| Wolf Rider | 8 | 4 | 130 | melee | 0.8s | 0 | hunts farmhands past front | 5 |

| Berserker | 12 | 6 | 100 | melee | 0.7s | 0 | +50% DMG when ally dies w/in 50px | 6 |

| Champion | 40 | 8 | 70 | melee+cleave | 0.8s | 1 | elite | 7 |

| Siege Tower | 60 | 6 | 35 | melee | 1.4s | 1 | DMG×2 vs base | 8 |

| Warlord | 80 | 10 | 60 | melee+cleave | 0.9s | 2 | aura: +1 DMG to allies w/in 100px | 10 |

KILL BOUNTIES: Levy 4g, Wall 8g, Spear 7g, Archer/Hunter 5g,

Wolf Rider 6g, Berserker 8g, Mage 10g, Ballista 12g,

Champion 30g, Siege Tower 25g, Warlord 50g, Farmhand 0g.

6.3 COMBAT MATH

═══════════════

DAMAGE FORMULA: damage = max(1, attacker.dmg - target.armor)

Apply to: melee, reach, ranged, cleave, base damage.

Cleave: floor(attacker.dmg / 2), then armor formula.

Per-unit-type targeting rules detailed in section 9 phase B

implementation. Same-lane only except Mage (cross-lane adjacent).

6.4 ECONOMY

═══════════

Starting: 60g, 0f, 1 Farmhand. AI starting gold scales by stage.

50% gold carry-over on win + 50g stage clear bonus. Food does

not carry.

6.5 STAGES

══════════

| # | Name | Doctrine | AI Gold | Reactive | Lane Strategy | Special Deploys |

|---|---|---|---|---|---|---|

| 1 | The First Probe | 100% Levy, 5-7s | 60 | none | single:center | - |

| 2 | The Storm | 90L 10W, 2-4s | 80 | none | alternate | - |

| 3 | The Iron Line | 60W 30L 10S, 4-6s | 100 | none | primary:center | - |

| 4 | Mixed Front | 30L 25W 25S 20H, 3-5s | 120 | light | spread | - |

| 5 | The Hunger Roads | 30L 20W 20S 30WR, 2.5-4s | 140 | none | focus_weakest | - |

| 6 | The Long Wall | 35W 25S 15B 25L, 4-6s | 160 | light | primary:center | - |

| 7 | The Champion's Arrival | 25L 20W 20S 15B 20H, 3-5s | 180 | light | spread | Champion @60s±5 weakest |

| 8 | The Tide | 35L 25S 20WR 15H 5ST, 1.5-3s | 200 | light | alternate | 2 Siege @45/80s alternating |

| 9 | The Black Harvest | 25L 20W 15S 20WR 10B 10H, 2.5-4s | 220 | light | focus_weakest | Champion @45s±5 |

| 10 | The Captain's Stand | 20L 15W 15S 10WR 10B 10H 10C 5ST, 2-3.5s | 280 | full | focus_weakest | Warlord @70s weakest |

LANE STRATEGIES:

- single:N — always lane N

- primary:N — 70% N, 15% each other

- spread — 33/33/33 random

- alternate — round-robin

- focus_weakest — sample player units per lane, pick weakest

REACTIVE OVERLAY:

- light: every 6s, bias next 3 deploys toward counter of player's

largest unit class

- full: every 3s, both unit counter AND lane focus_weakest

Stage flavor strings:

S1: "Hold the border. Test the enemy line."

S2: "The storm is coming. Build your shields."

S3: "They march in walls. Find the gaps."

S4: "A real test. They have hunters too."

S5: "Their riders hunt your farmhands. Defend the rear."

S6: "The long grind. Their berserkers rage."

S7: "Their champion walks. Hold every gate."

S8: "The tide does not pause. Their towers march."

S9: "Starve and crush. They play both hands."

S10: "The warlord comes. Make this the last stand."

6.6 MODIFIERS

═════════════

Pool of 10. Stage 1 has none. Stages 2-10 roll one. Symmetric.

1. Drought — food rate × 0.75

2. Bountiful Harvest — food rate × 1.25

3. Steel Shortage — Wall cost × 1.30

4. Quick March — all unit speed × 1.20

5. Plague — all units max HP × 0.85 (min 1)

6. Conscription — Levy cost halved, Levy max HP -2

7. Pike Festival — Spear reach +1

8. Champion's Field — Champion total cost halved

9. Fog of Banners — enemy unit hidden until first attack

10. Shieldwall Tradition — Wall HP × 1.20

Roll seed: stage * 1000 + run number.

6.7 CAMPAIGN MAP

════════════════

Linear path, 10 nodes on parchment background.

Node positions:

S1:(140,520) S2:(240,460) S3:(360,480) S4:(470,410)

S5:(580,360) S6:(690,380) S7:(790,310) S8:(870,250)

S9:(950,180) S10:(1010,100)

States: locked / available / completed.

Banner advances on win. Click available node to begin stage.

Stage 10 win → Campaign Complete screen with run stats.

6.8 WIN/LOSE

════════════

Win stage: enemy base shared HP ≤ 0

Lose stage: player base shared HP ≤ 0

Lose: retry overlay, retry same stage (no map view)

Win: map view, banner advance, click next node

═════════════════════════════════════════════════════════════════

7. FILE STRUCTURE

═════════════════════════════════════════════════════════════════

/long-border

├── index.html

├── package.json

├── vite.config.js

├── vitest.config.js

├── README.md

├── BUILD_REPORT.md           # generated at end

├── /docs

│   └── deferred-issues.md    # living document, updated per phase

├── /src

│   ├── main.js

│   ├── style.css

│   ├── /game

│   │   ├── state.js

│   │   ├── lanes.js          # NEW

│   │   ├── units.js

│   │   ├── combat.js

│   │   ├── economy.js

│   │   ├── ai.js

│   │   ├── stages.js

│   │   ├── modifiers.js

│   │   ├── rng.js

│   │   └── campaign.js       # NEW

│   ├── /render

│   │   ├── canvas.js

│   │   ├── battlefield.js    # NEW

│   │   ├── units.js

│   │   ├── effects.js        # NEW

│   │   ├── ui.js

│   │   ├── map.js            # NEW

│   │   └── overlays.js       # NEW

│   ├── /input

│   │   └── controls.js

│   └── /audio

│       ├── music.js          # NEW

│       ├── sfx.js            # NEW

│       ├── settings.js       # NEW

│       └── settingsModal.js  # NEW

└── /tests (smoke tests)

═════════════════════════════════════════════════════════════════

8. SELF-REPAIR PLAYBOOK

═════════════════════════════════════════════════════════════════

Common failure modes with explicit auto-repair sequences.

8.1 — npm install fails

ATTEMPT 1: rm -rf node_modules package-lock.json && npm install

ATTEMPT 2: npm install --legacy-peer-deps --no-audit

DEFER: this is HARD STOP (section 13). Cannot continue without

deps.

8.2 — A specific test fails

ATTEMPT 1: Re-read implementation and assertion. Identify obvious

bug (typo, wrong variable, off-by-one). Fix.

ATTEMPT 2: Check if assertion is wrong vs implementation. If

implementation matches design intent and assertion is incorrect,

update assertion.

DEFER: Mark with it.skip("DEFERRED: [reason]"). Log to

deferred-issues.md with reproduction steps. Continue.

8.3 — vite build fails

ATTEMPT 1: Identify offending file from error output. Check for

syntax errors in most recent changes.

ATTEMPT 2: If unclear, git diff the most recent commit and revert

suspicious chunks one at a time.

DEFER: HARD STOP (section 13). Build must work.

8.4 — npm test crashes (vitest itself fails)

ATTEMPT 1: Check vitest.config.js for syntax. Reinstall vitest.

ATTEMPT 2: Try running a single test file in isolation.

DEFER: HARD STOP. Test runner must work.

8.5 — Music track URL returns non-200

ATTEMPT 1: Replace

"incompetech.com/music/royalty-free/mp3-royaltyfree/" with

"incompetech.filmmusic.io/mp3/" and retry

ATTEMPT 2: Skip this track, try next in candidate list

DEFER: Continue with remaining live tracks. If <6 live, log

warning, disable music feature, show in-game toast at start:

"Music unavailable — see settings"

8.6 — Howler.js CDN fails

ATTEMPT 1: Try jsdelivr:

https://cdn.jsdelivr.net/npm/howler@2.2.4/dist/howler.min.js

ATTEMPT 2: Try unpkg:

https://unpkg.com/howler@2.2.4/dist/howler.min.js

DEFER: Skip music entirely. SFX still work via Web Audio API.

Settings modal hides music section. Log to deferred.

8.7 — Vercel deploy fails

ATTEMPT 1: Verify VERCEL_TOKEN, --scope marcusvale, --name

long-border flags

ATTEMPT 2: Try deploy with --debug flag, capture error

DEFER: HARD STOP only after all code committed. BUILD_REPORT.md

notes deploy didn't complete. User runs deploy manually after

review.

8.8 — A unit's combat behavior is wrong but game still runs

ATTEMPT 1: Re-read 6.2 spec for that unit. Trace combat.js for

that unit's targeting. Fix.

ATTEMPT 2: Simplify unit's behavior to known-working baseline

(e.g., make Mage in-lane only if cross-lane is buggy).

DEFER: Mark unit as "stub behavior, advanced features deferred".

Smoke test with it.skip(). Continue.

8.9 — Render layer broken (canvas blank, units not visible)

ATTEMPT 1: Check render order in canvas.js. Verify ctx state

saves/restores. Verify state shape matches what render expects.

ATTEMPT 2: Add console.log temporarily to identify which render

function fails. Fix or stub.

DEFER: Render the most basic version (untextured shapes, no

effects). Log polish features as deferred.

8.10 — DOM element missing or query returns null

ATTEMPT 1: Check index.html for the expected element ID. Add

if missing.

ATTEMPT 2: Wrap in optional chaining and skip the wiring for

that element.

DEFER: Log feature as "wiring incomplete" and continue.

8.11 — File can't be created (permission, path)

ATTEMPT 1: Verify cwd. Check path correctness.

ATTEMPT 2: Use absolute path or alternative location.

DEFER: HARD STOP if file is critical. Otherwise log and continue

without that file.

8.12 — Smoke test setup throws (not assertion failure, setup

failure)

ATTEMPT 1: Check imports in test file. Verify modules exist.

ATTEMPT 2: Rewrite test setup with simpler initialization.

DEFER: it.skip() with DEFERRED comment. Log root cause.

8.13 — Cannot find module / import error at runtime

ATTEMPT 1: Verify file path matches import path exactly

(case-sensitive on Linux/Mac).

ATTEMPT 2: Check if file exists, check if export name matches.

DEFER: Log missing module as deferred. Stub the import with a

dummy export. Continue.

═════════════════════════════════════════════════════════════════

9. PHASE PROTOCOL

═════════════════════════════════════════════════════════════════

Each phase follows this structure. Apply to all phases A-G.

9.1 — PHASE PRE-FLIGHT (5 minutes max)

Before phase work:

- git status: working tree must be clean. If dirty: stash with

message "phase-X-preflight-stash", check log

- Verify previous phase's commit exists in git log

- Run npm test. Note baseline (passing + skipped + failing)

- Verify required files from previous phase exist (file list per

phase below)

- Verify dev server starts: npm run dev for 3s background, then kill

If pre-flight finds missing prereqs:

- Apply self-repair from section 8 if applicable

- Log any unrepaired issues to deferred-issues.md

- Proceed with phase using whatever DOES exist

9.2 — PHASE EXECUTION

Smoke-first per existing pattern. For each implementation step:

- Write smoke assertion

- Implement

- Run npm test

- If test fails: apply 8.2 self-repair (max 2 attempts)

- If still failing: defer per 8.2, continue with next step

CHECKPOINT COMMITS:

Within a phase, commit after every successful sub-step that

leaves the system in a working state. Branch is rebuild/v2;

checkpoint commits use:

chore(phase-X-checkpoint): [what just got done]

9.3 — PHASE HEALTH CHECK

After phase implementation:

- Run npm test, count passing/skipped/failing

- Verify all expected files exist (from file structure section 7)

- Run npm run build, verify success

- Manual playtest is OPTIONAL — log a "manual playtest required"

note to deferred-issues.md if any feature can only be verified

by human play

9.4 — PHASE COMMIT

Always commit at phase end, even with deferrals:

feat(phase-X): [phase name]

[body]

Deferrals: N items (see docs/deferred-issues.md)

Tests: P passing, S skipped (deferred), F failing

Decisions:

- [any unspecified choices]

9.5 — PHASE REPORT UPDATE

Append to docs/deferred-issues.md a section for this phase listing

all deferrals. Format per section 11.

9.6 — PHASE TRANSITION

After commit, immediately begin next phase. No pause. No

confirmation request.

═════════════════════════════════════════════════════════════════

10. PHASES A-G

═════════════════════════════════════════════════════════════════

PHASE A — Lane refactor + damage feedback

==========================================

Pre-flight files needed: state.js, combat.js, ai.js, units.js,

stages.js, render/canvas.js, render/units.js (all from

preview/phase-4)

Build:

1. git checkout preview/phase-4 && git checkout -b rebuild/v2

2. Create src/game/lanes.js with constants from 6.1

3. Refactor state.js: units carry .lane, baseHP shared

4. Refactor combat.js: per-lane resolution, no cross-lane melee

5. Refactor ai.js: createAiController accepts laneStrategy,

implements single/primary/spread/alternate/focus_weakest

6. Update stages.js Stage 1 with laneStrategy: 'single:center'

7. Update economy.js buyUnit signature with lane parameter

8. Create render/battlefield.js: terrain, lane bands, fort bases

9. Update render/canvas.js to delegate to battlefield.js

10. Update render/units.js: position by LANE_Y[unit.lane]

11. Create render/effects.js: damage numbers, hit flash, screen

shake

12. Wire effects into combat.js applyDamage

13. Add lane selector to build panel in index.html and

style.css

14. Update input/controls.js: track selectedLane, pass to buyUnit

Smoke updates:

- tests/lanes.smoke.js (new): lane constants, lane assignment,

no cross-lane melee

- tests/combat.smoke.js (existing + extensions): all combat math

still works with lane field

- tests/effects.smoke.js (new): damage number spawn, fade,

hit flash duration

Health check:

- 24 prior tests + new lanes/effects tests all green

- Game playable with Stage 1 in 3 lanes, all on center lane

(preserves existing behavior)

- Build passes, dev server runs

PHASE B — Full unit roster

==========================

Pre-flight files needed: lanes.js, refactored combat.js,

effects.js (from Phase A)

Build:

1. units.js: add stat blocks for all 13 units (8 player, 9 enemy

with overlap)

2. combat.js: refactor target search per unit type

- getTargets(unit, state) handles melee/reach/ranged/AOE/cross

- applyDamage handles cleave AOE, projectile spawn

3. Special unit behaviors:

- Wolf Rider farmhand-targeting: when no friendly between

it and enemy farmhands within 200px, pivot

- Berserker rage: track ally deaths within 50px, stack to 2x

- Warlord aura: +1 DMG to friendly enemy units within 100px

- Mage cross-lane: prefer in-lane, fall back to ADJACENT

4. economy.js: enforce unlock per stage, dual-resource costs

5. render/units.js: add silhouettes for all unit types

6. render/effects.js: projectile arcs for ranged + cross-lane

7. input/controls.js: build panel shows all 8 player units

with three states

Smoke updates:

- tests/combat.smoke.js: assertions per new unit

- tests/ranged.smoke.js (new): Archer stops at range, Ballista

AOE

- tests/crosslane.smoke.js (new): Mage targeting rules

- tests/wolfrider.smoke.js (new): farmhand targeting rules

Health check:

- All units render and deploy

- Combat behaviors verified per smoke

- Game playable with full roster on Stage 1 (will be

dev-test only since other stages not enabled yet)

PHASE C — All 10 stages + AI lane targeting + modifiers

========================================================

Pre-flight files needed: full unit roster from Phase B

Build:

1. stages.js: complete all 10 stage configs per 6.5

2. modifiers.js: 10-modifier pool, rollModifier, applyModifier

3. ai.js: implement all laneStrategies, special deploys

scheduling, full reactive overlay

4. state.js: stage init rolls modifier, applies to stage config

copy

5. ui.js: modifier badge in HUD top-right

6. Stage flavor strings on each stage config

Smoke updates:

- tests/stages.smoke.js: all 10 stages valid, roster checks

- tests/ai.smoke.js: lane strategies produce expected ratios,

reactive overlay measurable

- tests/modifiers.smoke.js (new): pool valid, applies correctly,

deterministic

Health check:

- All 10 stages load without error

- Modifier badge displays

- Game playable through stage transitions (manual stage

advance via dev tool until Phase E wires campaign)

PHASE D — UX upgrade

====================

Pre-flight files needed: all game logic complete from Phase C

Build:

1. style.css: CSS variables and palette per 6.x design notes

2. index.html: command-table layout shell

3. ui.js: resource chips with rate, unit cards with 3 states,

stage display, modifier badge

4. battlefield.js: terrain detail, fort silhouettes, base HP

bars on canvas

5. overlays.js: stage intro, end overlay, toast system

6. controls.js: speed control (1x/2x/0.5x via dt multiplier)

7. Wire all toasts: insufficient resources, unit unlock, stage

clear

Health check:

- Visual upgrade complete

- All Phase A-C functionality preserved

- Build passes, dev server runs

PHASE E — Campaign map + progression

=====================================

Pre-flight files needed: UX upgrade from Phase D

Build:

1. campaign.js: state factory, advance, persistence to

localStorage (key: lb_campaign_v2)

2. render/map.js: parchment background, 10 node positions, path,

banner animation

3. main.js: state machine — intro → stage → win/lose → map → intro

4. overlays.js: stage intro shows on stage start, end overlay,

campaign complete screen

5. Map click handlers: only available node responds

Smoke updates:

- tests/campaign.smoke.js (new): state transitions, persistence

Health check:

- Full campaign playable from Stage 1 to complete

- Lose returns to retry, not map

- Stage 10 win shows Campaign Complete

PHASE F — Audio

===============

Pre-flight files needed: complete game from Phase E

Build:

1. Verify Howler.js CDN loads (8.6 fallback if needed)

2. Verify music track URLs (8.5 with fallback chain)

3. audio/settings.js: state, persistence

4. audio/music.js: playlist, lazy load, crossfade, stage mapping

5. audio/sfx.js: Web Audio synthesized SFX per spec (deploy,

hit, death, base damage, victory, defeat, unlock, click,

insufficient resources)

6. audio/settingsModal.js: settings modal UI wired up

7. Wire SFX into combat.js, economy.js, ui.js, controls.js

8. Wire music into main.js stage transitions

9. Throttle per-unit hit SFX to 80ms

Health check:

- Music plays on user gesture (no autoplay)

- SFX fire on game events

- Settings persist across reload

- If <6 tracks live, music feature gracefully degrades

with toast notification

PHASE G — Final polish + deploy

================================

Pre-flight files needed: complete v2 from Phase F

Build:

1. Run full automated test suite, generate test report

2. Run manual playtest checklist (LOG to deferred-issues.md as

"manual playtest required" — agent cannot perform)

3. Review docs/deferred-issues.md, attempt to resolve any

newly-actionable items

4. Update README.md with overview, run instructions,

credits (Kevin MacLeod CC BY 4.0)

5. Generate BUILD_REPORT.md per section 12 format

6. Run vercel deploy:

npx vercel --token $VERCEL_TOKEN --scope marcusvale --prod \

--yes --name long-border

7. If deploy succeeds, verify URL returns 200

8. Final commit with full deferral summary

9. Push rebuild/v2 to origin

Health check:

- BUILD_REPORT.md exists and is comprehensive

- deferred-issues.md is complete

- All commits pushed to origin/rebuild/v2

- Production URL live (or deploy failure logged as deferred)

═════════════════════════════════════════════════════════════════

11. DEFERRED ISSUES PROTOCOL

═════════════════════════════════════════════════════════════════

11.1 — File: docs/deferred-issues.md

Created on first deferral. Updated throughout build. Never

deleted entries (use "RESOLVED" tag if fixed later).

11.2 — Format

```markdown

# Deferred Issues — The Long Border 2.0 Build

Generated during autonomous build. Human review required.

## Severity Legend

- BLOCKER: Game cannot ship without this

- HIGH: Major feature broken or missing

- MEDIUM: Minor feature degraded

- LOW: Cosmetic or polish issue

## Phase A: Lane Refactor + Damage Feedback

### [HIGH] Hit flash visual delay

**What failed:** Hit flash overlay appears 50ms after damage

applied, not synchronously

**Attempts:**

1. Adjusted render order in canvas.js — no change

2. Moved flashUnit call before applyDamage — broke timing

**Current state:** Damage numbers correct, flash delayed but

visible

**Reproduction:** Open game, deploy unit, observe hit

**Recommended fix:** Render effects layer earlier in frame

**Continued with:** Damage feedback functional, polish deferred

### [LOW] Lane selector keyboard shortcut not implemented

**What failed:** Spec mentions optional 1/2/3 keyboard shortcut

**Attempts:** None — explicitly optional

**Current state:** Click-only

**Recommended fix:** Add keydown listener if desired

**Continued with:** Click works fine

## Phase B: ...

```

11.3 — When to add an entry

- Any test marked it.skip() with DEFERRED comment

- Any feature stubbed below spec

- Any visual element rendering incorrectly but game functional

- Any "manual playtest required" item

- Any decision the agent made that diverges from spec

11.4 — When NOT to add an entry

- Spec was ambiguous and agent made a defensible choice — log

in commit message instead

- Feature works as specified — no deferral needed

- Self-repair succeeded on first or second attempt — no log

needed (success is the default)

═════════════════════════════════════════════════════════════════

12. FINAL BUILD REPORT

═════════════════════════════════════════════════════════════════

Generate /BUILD_REPORT.md at end of Phase G with this structure:

```markdown

# The Long Border 2.0 — Build Report

Generated: [timestamp]

Branch: rebuild/v2

Final commit: [SHA]

Production URL: [URL or "DEPLOY FAILED — see deferred-issues"]

## Summary

[One paragraph: what shipped, what didn't, overall health]

## Phase Outcomes

| Phase | Status | Tests Passing | Deferrals | Commit |

|---|---|---|---|---|

| A — Lanes + Effects | COMPLETE | N | N | [SHA] |

| B — Unit Roster | COMPLETE | N | N | [SHA] |

| ... | ... | ... | ... | ... |

## Deferred Issues by Severity

- BLOCKER: count, titles

- HIGH: count, titles

- MEDIUM: count, titles

- LOW: count, titles

## Test Status

Total tests: N

Passing: N

Skipped (deferred): N

Failing: N

## Audio Status

Howler.js: loaded / failed

Music tracks live: N of 10 candidates

Music feature: enabled / disabled (per 8.5)

SFX: working

## Manual Verification Required

Items in deferred-issues.md flagged "manual playtest required":

- [list]

## Recommended Next Actions

1. [highest priority deferral]

2. [next]

3. [next]

## Notes for Human Review

[Any agent observations, design questions, edge cases worth

flagging]

```

═════════════════════════════════════════════════════════════════

13. HARD STOPS

═════════════════════════════════════════════════════════════════

The agent halts ONLY for these conditions. For each: commit all

in-progress work to a halt-N branch, generate BUILD_REPORT.md

with current status, then stop.

13.1 — Cannot install dependencies

After 8.1 attempts exhausted, npm install still fails. Cannot

run anything else.

13.2 — Cannot build

After 8.3 attempts exhausted, vite build still fails. Cannot

deploy or even verify code in browser.

13.3 — Test runner crashes

After 8.4 attempts exhausted, vitest itself won't start. Cannot

verify any work.

13.4 — Git operations fail

Cannot commit or push. Anywhere. After verifying credentials and

remote URL.

13.5 — File system errors

Disk full, permission denied on critical paths, cannot write

files.

13.6 — Total elapsed time exceeds 8 hours

Hard time cap. Stop, commit, report current state.

For ANY hard stop:

1. git add -A

2. git commit -m "halt(phase-X): [reason]"

3. git checkout -b halt-[YYYY-MM-DD-HHMM]

4. git push origin halt-[branch]

5. Generate BUILD_REPORT.md with HALTED status and full diagnosis

6. Stop.

═════════════════════════════════════════════════════════════════

14. ANTI-PATTERNS

═════════════════════════════════════════════════════════════════

- Asking for human input when section 8 has a self-repair path

- Halting for non-hard-stop conditions

- Committing broken code without marking deferred

- Skipping deferred-issues.md updates

- Reverting work without logging why

- Adding undocumented dependencies

- Decorative comments

- try/catch around code that cannot throw

- console.log in committed code

- Magic numbers without named constants

- Mutating state outside designated mutators

- Premature optimization

- Smoke tests that test internal structure not behavior

- Skipping the final BUILD_REPORT.md generation

═════════════════════════════════════════════════════════════════

15. GO

═════════════════════════════════════════════════════════════════

Begin Phase A pre-flight immediately. Branch off preview/phase-4

to rebuild/v2. Work through phases A → G without stopping.

Self-heal where possible, defer where not, halt only for

section 13 conditions.

Output expectations at end of run:

- All committable code on rebuild/v2 branch

- docs/deferred-issues.md present and comprehensive

- BUILD_REPORT.md present at repo root

- README.md updated

- Production URL live (or deploy failure documented)

The directive above is your single source of truth. If a detail

is unspecified and section 8 has no relevant entry, choose the

simplest option that satisfies the contract, document the choice

in the commit footer, and continue.

Begin.
