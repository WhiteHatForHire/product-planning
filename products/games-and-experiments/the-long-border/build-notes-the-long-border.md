---
title: "Build notes The long border"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /The Long Border/Build notes  The long border.docx"
status: active
privacy: working
tags:
  - product
---

# Build notes The long border

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Game

https://long-border.vercel.app/

5/10/2026

The Long Border — Build Log, Session 1 Gili Air, cafe block. 1.5 hours.

Opening orientation

The session started as an Anchor day. The plan was to deliver the V4 program-aware prompt system review, get a verdict on paper, and move into some production deployment work. That happened — the review went out, verdict was HOLD, amendment list written and clear. Then the conversation turned to game prototypes, and specifically to whether the Director Model could spec and ship a browser-based auto-battler from nothing in a single session.

The answer, as of ninety minutes later, is yes. There is a live URL.

What actually happened

The game design came first, and it was not a vague sketch. Single-lane auto-battler, late-Bronze-Age frontier siege framing, symmetric economy with gold and food as separate resource channels, ten stages with distinct AI doctrines, a three-unit rock-paper-scissors combat system built around a reach mechanic rather than a stat hierarchy. That last part was the first discipline call of the session: the initial instinct was "bigger unit is stronger" and that got pushed back immediately because it produces bad game feel. The design conversation did real work.

From spec to agentic build prompt took about twenty minutes. The prompt was phase-gated: smoke-first within each phase, commit on green, revert-and-branch on repeated failure, halt-and-surface if three consecutive attempts fail. Five numbered phases plus a seeded RNG sub-step that emerged during Phase 3 preflight. The agent executed cleanly through Phases 0 and 1 and into Phase 2, where it stopped.

The Phase 2 halt was correct. Wall at 1 DMG per 1.0-second attack interval loses to Levy at 3 DMG per 0.7-second interval in every possible scenario under the original stats. The intended rock-paper-scissors relationship — Wall beats Levy — was not achievable without a new mechanic. The directive said halt, do not invent around the conflict. The agent halted. The amendment introduced an armor stat: damage_dealt = max(1, attacker.dmg - target.armor). Wall got armor 2 and DMG bumped to 3. The math was recomputed across all matchups, validated on paper before touching the smoke files, and Phase 2 committed clean.

Phase 3 was the doctrine AI: a reactive state machine with ten distinct stage behaviors, special deploy scheduling for the Champion unit at timed windows in Stages 7 and 9, and a reactive overlay that samples the player's unit composition every three to six seconds and biases the AI's next deploys toward the appropriate counter. Twenty-four smoke tests green by Phase 3 close.

Phase 4 was the vertical slice. Canvas rendering, HTML build panel, game loop with a 0.1-second dt cap and visibility pause on tab switch, win and lose state overlays, restart with clean state reset. Farmhands producing food, Levies marching, AI deploying on its Stage 1 doctrine, units meeting in the road zone and fighting. Then deployment.

The deployment friction came in sequence: wrong working directory (the project was nested inside a directory named "The Long Border" with spaces), wrong shell syntax (the directive assumed PowerShell and the environment was bash), missing scope flag for Vercel, and then a deployment protection wall on the preview URL. Each failure mode got resolved with one corrective command. No spiral. The production URL went live at long-border.vercel.app.

The session ended with a UX audit on the live build: a screenshot review against a structured diagnostic, synthesized with a second model's parallel audit into a single prioritized upgrade directive. Thirteen implementation steps, a 35-item QA checklist. The directive is written. It has not been executed.

Specific named moments worth banking

The Phase 2 halt worked because the protocol made it automatic. There was no decision moment of "should I push through or stop?" The directive had already answered that question. Halt on repeated smoke failure, do not invent around the conflict. The agent halted. That is the practical argument for embedding discipline rules into the build framework before the situation arrives. Phronesis is the right word here: practical wisdom exercised at authorship time, not at decision time. The decision was already made.

The armor mechanic is worth noting not as a patch but as a design improvement. The naive fix would have been to bump Wall's DMG and adjust the smoke assertion. Instead, adding an armor field gave the game something it was missing: a genuine mechanical identity for the Wall unit. Low-damage attacks chip at armored targets for 1 per hit. High-damage units punch through. Champion cleaves hit armored targets for reduced cleave damage. One spec amendment created texture that was not in the original design. When a fix improves the thing it fixes, that is worth banking.

The Vercel chain of failures is worth naming not because it was dramatic but because it was not. Four distinct failure modes in sequence, each resolved with a single corrective command, no anxiety, no catastrophizing, no "the whole deployment is broken." What could have been twenty minutes of spiral took twelve minutes of sequential problem-solving. That is a regulation pattern worth recognizing: the failure mode changes, the response stays the same. Identify the specific problem. Apply the specific fix. Move.

The Council of Models pattern showed up in the UX audit. My audit went first, prioritized by severity. A second model's audit came in separately. The synthesis produced a document cleaner than either source, with a priority ordering that neither audit had on its own. The P0/P1/P2 structure from mine and the unit card design language and DOM/Canvas split from the second model. That is the pattern working correctly. Neither output alone was the answer.

What I'm noticing about the work

The Director Model compresses most sharply at architecture and backend: the doctrine AI system, the game design spec, the combat math. These took minutes where they would have taken days without AI tooling. What does not compress at the same rate is tooling friction in DevOps: environment assumptions, auth flows, CLI flag requirements, deployment protection settings. The tools have their own pace and it is not the director's pace.

There is also a domain knowledge variable that showed up today. The armor mechanic spec error shipped in the original game design document and was not caught until Phase 2 smoke. A designer with real playtesting experience would have validated the combat math before writing the spec. The Director Model is as good as the director's domain knowledge at the spec layer. When that knowledge is shallow, the smoke catches it. When it is deep, it gets caught at the design table. Today it got caught in the smoke. That is acceptable. Earlier would have been better.

Where I am now

The Long Border as a fCTO proof-of-concept is roughly 45 percent complete.

Done and committed to preview/phase-4:

Phases 0 through 4, six commits, all smoke green

24 tests passing

Production deployment live at long-border.vercel.app

UX audit delivered

UX upgrade directive written

Not done:

UX implementation (directive written, not executed)

Phase 4 formal playtest against the a-i checklist (written, not formally logged)

preview/phase-4 not merged to main

Phases 5 through 8 (full unit roster, modifiers, all 10 stages, polish)

The URL works. The game is playable. Stage 1 only, basic visuals, no modifiers, no stage progression beyond the first stage. That is what Phase 4 promised. Not more.

A few things to lock in before stopping

The UX upgrade directive is written and ready to fire. Do not open it and start editing before the next session. Fire it as written or park it. Those are the two options.

The Phase 4 formal playtest against the a-i checklist is a five-minute task on the live URL. Do not skip it to start Phase 5. The gate exists and it exists for a reason.

The OpenAI integration idea — hooking an LLM into the AI doctrine system so the opponent genuinely reasons about deploy decisions — was raised in the session and deliberately deferred. It is not Phase 5 scope. It is not in any current directive. It stays parked until Phase 8 is green and the prototype is otherwise complete. This is the most tempting side quest in the project and it needs to stay named and parked, not reopened.

Phases 5 through 8 have defined scope. Do not pre-write their directives. Write each one at gate-pass time, with current context, after the prior phase has cleared its playtest.

Cost ledger

Session duration: 1.5 hours director time. Director time cost at $150/hour floor: $225. Billable at 2026 fCTO rates: $7,488. No Vercel costs. No API costs. Cumulative session total: $7,488 billable on $225 in director time. 97 percent gross margin.

What I'm taking with me on the break

A live game at a live URL, built in ninety minutes, with a doctrine-based AI that has ten distinct stage behaviors, a three-unit RPS combat system grounded in a reach mechanic, an armor formula that actually balances the matchups, and 24 passing smoke tests. The case study numbers are what they are: 139x compression against a 2022 solo build, $4,992 per director hour effective yield. Those are real numbers on a real deliverable. The proof-of-concept exists. It runs. A client could look at it today.

Note to future Marcus

The discipline that mattered most in this session was not the speed. It was the halt at Phase 2. The protocol said stop, and the system stopped. No heroics, no invention around the problem, no rationalizing through it. The spec had a defect. The defect got surfaced. The fix came back clean. That sequence only works if you trust the protocol over the instinct to push through. Remember that the next time the smoke fails and the temptation arrives to make it pass by adjusting the assertion rather than fixing the problem. The protocol is the discipline. Follow it.

5/10/2026 Financials

The Long Border — Build Session Cost Analysis (Corrected: 1.5 Director Hours)

1. Work Inventory

Architecture and Design

Full game design specification: 10-stage campaign, 5-unit roster with reach-based RPS mechanic, symmetric two-resource economy, doctrine-based AI system, rogue-like modifier pool, file structure, and visual approach

Armor mechanic redesign: diagnosed Wall vs Levy spec conflict, rebuilt unit stat table with armor formula max(1, atk - armor), validated math across all matchups

Agentic build framework: phase-gate doctrine, smoke-first discipline, revert protocol, halt conditions, and commit protocol for full campaign build

UX audit: priority-ordered findings from live screenshot review, synthesized with second model audit into ranked remediation list

UX upgrade directive: 13-step agentic implementation plan with 35-item QA checklist — design deliverable complete; implementation not executed, excluded from frontend billing

Backend

state.js: game state model, stage initialization, player and AI state factory

economy.js: resource tick, canAfford, applyCost, applyBounty, buyUnit

units.js: unit factory, stat table with armor field, unit type constants

combat.js: lane resolution, formation queueing, reach mechanic, Champion cleave, base damage, armor formula

ai.js: doctrine state machine, reactive overlay (light and full), special deploy scheduling, farmhand auto-buy threshold

stages.js: 10 stage configurations with doctrine weights, deploy intervals, roster, special deploy lists, reactive overlay level

rng.js: mulberry32 seeded RNG, createRng, rngInt, rngPick helpers

Frontend

render/canvas.js: canvas setup, rAF game loop with 0.1s dt cap, visibility pause and resume

render/units.js: unit silhouettes (Levy, Farmhand — Phase 4 scope), HP bars with dark casing

render/ui.js: HUD resource counters, build menu with disable states, base HP display, end overlays

input/controls.js: event delegation on build panel, restart handler

main.js: game bootstrap, Stage 1 initialization, AI controller wiring, loop start, restart callback

index.html and style.css: game shell layout, dark palette scaffold

UX implementation pass: 0% complete — directive written, not executed; excluded

QA and Testing

economy.smoke.js, combat.smoke.js, ai.smoke.js, stages.smoke.js, rng.smoke.js: full smoke coverage across all Phase 1-3 contracts

loop.smoke.js, input.smoke.js, render.smoke.js: Phase 4 behavioral contracts

Phase 3 and Phase 4 preflight directives: 5-point and 7-point verification protocols

Phase 4 playtest checklist: written and deployed to live URL — formal a-i logged pass not completed; discounted 50%

Total passing: 24 smoke tests green at session close

DevOps

Git repository initialized, conventional commit format established

GitHub remote configured at WhiteHatForHire/long-border, branch preview/phase-4 pushed

Vercel project configured at marcusvale/long-border, production deployment live at https://long-border.vercel.app

Deployment troubleshooting resolved: directory path, bash vs PowerShell syntax, scope flag, deployment protection on preview URLs

Technical Leadership

Phase-gated build framework authored and enforced across all phases

Phase 2 halt-and-surface executed correctly: spec defect caught, diagnosed, amended, re-smoked, committed clean

Thread summary produced covering Long Border scope

2. 2022 Pre-AI Pricing and Timelines

Agency or dev shop (external)

Category

Sr Dev Days

Labor Cost

Agency Billing (2x)

Architecture + Design

5.5

$6,600

$13,200

Backend

8.0

$9,600

$19,200

Frontend

5.0

$6,000

$12,000

QA + Testing

3.0

$3,600

$7,200

DevOps

1.0

$1,200

$2,400

Technical Leadership

1.5

$1,800

$3,600

Total

24.0

$28,800

$57,600

Traditional agency timeline: 5 to 7 calendar weeks with a team of 2 to 3.

Solo builder (internal)

Category

Solo Days

Opportunity Cost ($100/hr)

Architecture + Design

4.0

$3,200

Backend

10.0

$8,000

Frontend

6.0

$4,800

QA + Testing

3.5

$2,800

DevOps

1.5

$1,200

Technical Leadership

1.0

$800

Total

26.0

$20,800

Solo builder timeline: 5 to 6 calendar weeks working full time. Realistic timeline for a solo founder splitting time with sales, ops, and life: 3 to 5 months.

3. 2026 AI-Native Pricing and Timelines

fCTO or AI-native dev shop billing a client

Category

Hours

Rate

Billable Amount

Architecture + Design

12.0

$250

$3,000

Backend

11.0

$200

$2,200

Frontend

5.0

$200

$1,000

QA + Testing

4.5

$150

$675

DevOps

1.5

$175

$263

Technical Leadership

2.0

$175

$350

Total

36.0

—

$7,488

AI-native fCTO timeline: 1 to 2 days of director time. What a 2026 AI-native agency would quote for the same scope: $12,000 to $18,000 over 2 to 3 weeks.

Solo AI-native builder (internal)

Your actual cost: 1.5 director hours at $150/hour floor = $225 in your time. Effective compression ratio versus 2022 solo builder: 139x.

4. Actual Timeline vs 2026 Market Standard

Deliverable

Your Timeline

2026 Market Standard

Your Delta

Game design specification

45 min

2–4 hrs (solo) / 6–10 hrs (agency)

3–13x faster

Agentic build framework + directive

25 min

1–2 hrs (solo) / 3–5 hrs (agency)

2–12x faster

Phase 0 — Project scaffold

20 min

30–45 min

Comparable

Phase 1 — State + economy engine

20 min

1–1.5 hrs

3–5x faster

Phase 2 — Combat engine + spec fix

35 min

1.5–2.5 hrs

3–4x faster

Phase 3 — Seeded RNG + doctrine AI + stages

55 min

2–3 hrs (solo) / 5–8 hrs (agency)

2–9x faster

Phase 4 — Vertical slice, playable game

30 min

2–4 hrs (solo) / 5–10 hrs (agency)

4–20x faster

GitHub repo + branch setup

20 min

15–30 min

Comparable

Vercel production deployment

30 min

15–25 min (standardized CI)

Slower

UX audit + upgrade directive

45 min

1.5–2 hrs (solo) / 4–6 hrs (agency)

2–8x faster

Where you outpaced the 2026 market: Phase 3 doctrine AI — a reactive state machine with 10 distinct doctrines, timed Champion deploy scheduling, and a reactive overlay required zero team alignment or client review cycles, going from blank file to 24 passing smoke tests in a single directive session.

Where the 2026 market matched or beat you: Vercel deployment — a well-resourced 2026 agency maintains standardized CI/CD pipelines with pre-configured framework detection, eliminating the directory path, shell syntax, scope flag, and deployment protection troubleshooting that added 15 minutes of friction.

5. Value Delivered Today

2022 agency would have billed a client: $50,000 to $60,000

2026 fCTO bills a client today: $7,488

Your personal cost as AI-native solo: $225 in director time

Your timeline versus 2026 market standard: Faster — delivered in 1.5 director hours what a 2026 AI-native solo founder would typically spend 1 to 2 focused days on and an agency 2 to 3 weeks.

The range in 2022 agency billing reflects variability in discovery overhead, project management cost, and whether the spec arrives tight or requires significant iteration before implementation begins.

6. Margin Reality (private)

Billable at 2026 fCTO rates: $7,488 Your personal cost: $225 Gross margin: $7,263 — 97%

At 97% gross margin the Eagle Rocket fCTO model is structurally sound as a solo operation; delivery capacity is not the constraint — client pipeline quality and scope discipline are, because one under-priced or under-scoped engagement erodes what several well-run sessions build.

7. Running Context

Total billed this session at 2026 fCTO rates: $7,488

Total director hours logged: 1.5 hours

Effective hourly yield on your time: $4,992/hour

8. One Honest Caveat (private)

The armor stat error — Wall at 1 DMG cannot win a 1v1 against Levy at 3 DMG over a 1.0s vs 0.7s attack interval — shipped in the original game design document and was not caught until Phase 2 implementation triggered the smoke failure. A 2022 senior game developer with playtesting experience would have validated core combat math on paper before specifying unit stats, knowing intuitively that a slow low-damage unit cannot win a 1v1 against a fast high-damage unit without a separate mechanic. The fix was handled correctly once surfaced, but the cycle reveals that numeric spec validation — running the math before writing the design document — is not yet standard in the director workflow and should be.

9. Conclusion

The Long Border session produced a full game design, seven committed code phases, 24 passing smoke tests, a GitHub repository, and a live production deployment in 1.5 director hours. The 2022 equivalent is $57,600 and 5 to 7 calendar weeks with a team. The 139x compression ratio is not evenly distributed across categories: backend compresses hardest because AI writes deterministic game logic well once the contracts are clearly specified, and DevOps compresses least because tooling friction, authentication flows, and shell environment assumptions are real and do not compress. The meaningful result today is not speed in the abstract — it is that a single director applying the Director Model can specify, verify, and ship a complex multi-system prototype at a quality level that holds up to formal smoke testing and a production deployment, in a single 90-minute session.

The 97% gross margin and $4,992 effective hourly yield are not arguments for charging less. They are arguments for tighter scope discipline and more selective client engagement. At 1.5 director hours per engagement of this scope, the Eagle Rocket fCTO model can run multiple engagements per week if the pipeline is healthy. The real constraint is upstream: each engagement requires a clearly defined scope and a correctly priced outcome contract before work begins. One retainer priced at day-rate instead of outcome-rate, or one scope that expands mid-engagement without a change order, erases the margin that makes the model viable. The model rewards outcome pricing and punishes time pricing.

The Vercel deployment friction — directory path, shell syntax mismatch, scope flag, deployment protection — was the only phase where the 2026 market standard would have matched or beaten the pace. The fix is operational and costs nothing: add a 5-item DevOps preflight sub-step (confirm shell, confirm working directory, confirm token, add scope flag, add project-name flag) to the agentic build template before any first-deploy directive. It adds two minutes at the start and eliminates fifteen minutes of reactive troubleshooting. Build it into the template now so it does not happen again.
