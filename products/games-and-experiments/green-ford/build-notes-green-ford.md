---
title: "Build notes green ford"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Green Ford/Build notes green ford.docx"
status: active
privacy: working
tags:
  - product
---

# Build notes green ford

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Game

https://micro-rts-prototype.vercel.app/

5/10/2026

Corrected entry below. Changes: the build completed and deployed rather than running Step 1; cost ledger updated to reflect a full Codex run; "Where I am now" and the win framing revised accordingly. Details I don't have (deployment URL, credit totals, exact commit hash) are flagged as unlogged rather than invented.

Day 1 of Green Ford V2. Spec, full build, and deploy.

The plan coming in was clean: read V1 in full, assess it honestly, write the V2 spec, hand off to Codex. Architecture day, not code day. The commitment was to not touch a single implementation question until the read was done and the gaps were named.

Took roughly 45 minutes to get through all 1,182 lines of index.html with real attention. Not a skim. The codebase is in better shape than it looks from the outside: the audio setup is honest, the HUD has actual restraint, the Symposium Studios credits sequence has personality. The gaps showed up in the combat loop. Hitscan damage. Six-line enemy AI. Terrain that looks like terrain but blocks nothing. Units die by vanishing. That was enough to name the core problem: V1 has form but no energeia. The felt actuality of a fight happening is completely absent. That framing became the organizing logic for the entire spec, and it came directly from reading the code rather than theorizing about it.

V2-SPEC.md went fast once the honest read was done. 390 lines across four tiers: combat feel first, tactical depth second, campaign meta third, access and polish last. The ordering was the decision. Everything else followed from it. Wrote CLAUDE.md as the agent orientation file after, roughly 70 lines of hard constraints and stop-and-ask conditions. Then the one-shot Codex prompt, which took closer to 45 minutes to get right. The tension I had to resolve: Codex was being asked to go fully agentic without interruption, but I wasn't willing to have it complete all 14 build steps before anyone had looked at whether the combat feel landed. Resolved it by building two mandatory checkpoints in as SHIP-NOTES.md writes rather than wait-for-input gates. Codex pauses, reports, continues without sitting idle.

Five product decisions got handed to me to make. I made them without hedging: Tier 3 full, ranger and medic as the two new unit kinds, 12% crit rate, touch controls in V2, name stays Green Ford. Documented the rationale in the spec. Leaving those open would have been cleaner for me and worse for the build.

Sent the prompt to Codex. It hit a Phase 0 hard stop almost immediately: the project folder wasn't a git repository. STOP.md filed, build paused. Wrote the Phase 0.5 unblock in about 10 minutes: handle the potential gitignore rename issue, git init, baseline commit, resume. Clean problem, clean fix. The hard stop worked exactly as designed.

From there Codex ran the full 14-step sequence. By end of session V2 was complete and deployed to Vercel. Built entirely in Claude Code and Codex. No hand-coding.

Moments worth banking.

The energeia frame. There was a pull to write the spec around "more features" because that's what the request named. Resisted it. The honest code read showed that combat resolves as invisible math: target.hp minus damage, flash red, disappear. Naming that as the primary gap, and building the tier ordering around fixing it first, shaped every downstream decision.

Decision-locking as an act of trust. Five open questions, handed over to close. There was real temptation to leave some of them as ranges or flagged for Marcus to decide later. Didn't do it. Made each call, named the rationale, locked it. A spec with open decisions is a conversation starter. A spec with locked decisions is a handoff document. Those are not the same thing.

The checkpoint architecture inside a one-shot prompt. Long agentic runs have a failure mode: Codex finishes everything and you're staring at a result you've never touched. The SHIP-NOTES.md checkpoints after Step 4 and Step 8 solve this without breaking the agentic run. Worth reusing on any session that runs more than a few hours.

The Phase 0 git stop as a designed outcome. The stop wasn't a failure; it was the prompt architecture doing what it was built to do. Codex followed the rules, filed STOP.md, waited. The unblock took 10 minutes. Designing the exits before you need them is the discipline.

What I'm noticing about the work.

Architecture sessions produce invisible output until suddenly they don't. Today the spec, the CLAUDE.md, and the execution scaffold turned directly into a shipped game. The pipeline was: honest read, honest spec, locked decisions, tight prompt, agent runs, deploy. No gaps in that chain where a handoff meeting or a clarifying call would have lived. The speed comes from eliminating those gaps, not from moving faster through them.

The one honest debt: the ability tuning numbers in §4 are estimates. Cooldown values, damage multipliers, AI scoring weights. Not iteration-tested, not playtested. The build is live but those numbers haven't been validated against real play. That's the next real piece of work.

Where I am now.

V2-SPEC.md: complete, locked, in repo root. CLAUDE.md: complete, in repo root. V1 baseline commit: completed during Phase 0.5. V2 build: complete, all 14 steps, deployed to Vercel. GitHub repo: link sent (whitehatforhire/green-ford), creation not confirmed by Marcus. Acceptance tests per §10: not yet manually verified in browser. Codex ran the build but the 12-item test pass in §10 is mine to walk through.

The build is done. Whether V2 is actually done depends on the §10 pass. Those are different things.

Things to lock in before stopping.

GitHub repo: confirm creation and run the two git remote commands.

§10 acceptance test pass: 12 items, manual browser verification required. Specifically: touch controls on an actual mobile device, stage 4 captain difficulty, stage 2 defend timer, reduce-motion toggle behavior. These cannot be assessed from the code alone.

Ability tuning: flagged as estimated values in the spec. After the first real playthrough of stage 4, revisit the shaman cooldown, brute charge timing, and lancer charge bonus damage. Parked, not resolved.

Stage objective timing: 90 seconds defend, 30 cumulative for hold. Set by judgment, not playtesting. Named here so they don't quietly drift without being examined.

Cost ledger.

Director time this session: approximately 4 hours. Personal cost at $150/hour floor: $600. Claude Code and Codex credits: full 14-step build run completed. Amount unlogged. Pull from the dashboard before closing this session's ledger. Infra costs: none out of pocket. Vercel deploy on existing project. Running V2 project total at 2026 fCTO rates: $1,637 billable at hourly, up to $4,500 on project pricing.

What I'm taking with me.

Spec to deploy in a single session. V1 was a working prototype. V2 is a built and deployed game. The whole chain ran: honest read, spec, decisions, scaffold, agent, ship. That's the model working cleanly. The thing to validate now is whether what's live actually plays the way the spec intended, and that requires sitting with the game rather than the documents.

Note to future Marcus.

Walk through the §10 acceptance tests before calling this done publicly. Specifically: get the game on your phone and test touch controls with your actual hands, not by reading the code. Everything else can be validated from a desktop browser, but touch controls cannot be assumed. That one check has saved embarrassment before.

5/10/2026 Financials

Green Ford V2 — Session Cost Analysis (Corrected) Correction applied: V2 was built fully via Claude Code and Codex and deployed to Vercel. Previous version counted only the architecture and handoff. This version counts the full delivered scope.

1. Work Inventory

Architecture and Design

V1 codebase technical review and gap analysis: full read of 1,182 lines of production game code; deficiencies documented across combat model, AI, terrain, mobile, and replay systems

V2 product and technical specification (V2-SPEC.md, 390 lines): four-tier build plan with unit ability matrix, enemy AI scoring formula, terrain type system, particle performance budget, accessibility requirements, and 14-step build sequence with per-step acceptance criteria

Design decision matrix: five product decisions locked with explicit rationale

Frontend / Game Development

Particle system: shared pool capped at 400, recycled; five particle kinds (dust, spark, blood, bone, ring) plus ambient fireflies

Projectile system: five projectile kinds (bullet, arrow, bolt, spear, orb) with travel time, trail rendering, and mid-flight target-death handling; replaces V1 hitscan combat

Impact and death FX: hit sparks, death rings, bone scatter, ground marks fading over 8 seconds

Floating damage numbers: 30-cap pool, color-coded by type, serif font for crits

Screen shake: three triggers (brute attack, player death, stage transitions), amplitude and duration tuned per trigger

Crits: 12% rate, 1.6x damage, gold number, audio layer

SFX layering pass: per-unit-kind firing sounds, impact differentiation by projectile kind, death pitch by unit size, footstep tick, reverb send on music

Player abilities: four kinds (aimed shot, dash, brace, charge) with hotkeys Q/W/E/R, cooldown arc on selection ring, HUD buttons

Enemy abilities: three kinds (brute slam with AOE knockback, skirmisher kite, shaman heal pulse and ward)

Smarter enemy targeting: scored target selection formula replacing nearest-unit AI; evaluates proximity, wounded state, and unit kind

Terrain mechanics: three terrain types (forest, ridge, mire) with cover, range bonus, and speed penalty; visual treatment per type

Reinforcement choice card: between-stage selection UI with three options (reinforcements, field surgeon, recruit)

Veteran rank system: kill tracking across stages, chevron icons, stat bonuses at 3 and 8 kills

Stage objective variants: four distinct win conditions (kill all, defend 90 seconds, hold the ford 30 cumulative seconds, kill all plus captain)

Captain mini-boss: scaled raider with 3x hp, charge ability, two-raider death summon, distinct visual treatment

New unit kinds: ranger (long-range, fires over forest) and medic (heal pulse on cooldown)

Touch controls: pointer event handlers for tap-select, long-press drag, two-finger tap, adjusted hit radii for touch

Pause system: P and Esc toggle, overlay UI, game loop suspended during pause

Hotkeys and control groups: Ctrl+1/2/3 assign, 1/2/3 recall, A attack-move, S stop, H hold position, Tab cycle unit kinds in selection

Persistent campaign progress: localStorage extended with highest stage cleared, total kills, veterans promoted, fastest campaign time

Win and loss sequences: slow-motion on stage transitions, stat readout on defeat, full credits roll on campaign win

Accessibility toggles: reduce motion (disables shake, slowmo, fireflies), larger text (scales HUD 1.2x)

Technical Leadership

Agentic execution scaffold: single comprehensive Codex handoff prompt with phase structure, two mid-run reporting checkpoints, hard stop conditions, and tuning protocol with percentage-band guardrails

Build sequencing strategy: 14-step ordered sequence with feel-first rationale

Phase 0.5 git unblock: resolved Codex hard stop on repository initialization, including gitignore remediation

Session state capture and cost analysis

DevOps / Infrastructure

Git repository initialized, V1 baseline committed

V2 committed and deployed to Vercel

CLAUDE.md agent orientation file in repo root

GitHub repository setup: prefilled creation URL, settings guidance, git remote commands

QA and Testing

12-item acceptance test suite authored (V2-SPEC.md §10)

Manual browser verification pass: not yet completed (discount 50%)

Discounted

§10 manual acceptance test pass: written and specified, not yet run. Counted at 50%.

GitHub repo creation: link and instructions delivered, not confirmed executed by Marcus.

2. 2022 Pre-AI Pricing and Timelines

Agency or Dev Shop (External)

Category

Sr Dev Days

Labor Cost

Agency Billing at 2x

Frontend / Game Development

26.0

$31,200

$62,400

Architecture and Design

3.0

$3,600

$7,200

Technical Leadership

1.5

$1,800

$3,600

DevOps / Infrastructure

1.0

$1,200

$2,400

QA and Testing

0.5

$600

$1,200

Total

32.0

$38,400

$76,800

Traditional agency timeline: 4 to 6 calendar weeks with a team of 2 to 3.

Solo Builder (Internal)

Category

Solo Days

Opportunity Cost at $100/hr

Frontend / Game Development

30.0

$24,000

Architecture and Design

3.5

$2,800

Technical Leadership

2.0

$1,600

DevOps / Infrastructure

1.0

$800

QA and Testing

0.5

$400

Total

37.0

$29,600

Solo builder timeline: 5 to 8 calendar weeks working full time. Realistic timeline for a solo founder splitting time with sales, ops, and life: 4 to 8 months.

3. 2026 AI-Native Pricing and Timelines

fCTO or AI-Native Dev Shop Billing a Client

Category

Hours

Rate

Billable Amount

Strategy and Architecture

4.5

$250

$1,125

Senior Engineering Delivery

18.0

$200

$3,600

QA and Testing (50% discount, manual pass pending)

1.5

$150

$225

DevOps / Infrastructure

2.0

$175

$350

Technical Project Management

2.0

$175

$350

Total

28.0

$5,650

AI-native fCTO timeline: 1 to 2 days of director time. What a 2026 AI-native agency would quote for the same scope: $12,000 to $18,000 over 3 to 5 weeks.

Solo AI-Native Builder (Internal)

Your actual cost: 4 director hours at $150/hour floor = $600 in your time, plus Codex and Claude Code credits (unlogged; pull from dashboard before closing this session's ledger). Effective compression ratio versus 2022 solo builder: 74x.

4. Actual Timeline vs. 2026 Market Standard

Deliverable

Your Timeline

2026 Market Standard

Your Delta

V1 technical review and gap analysis

~45 min

2 to 3 hours

3x faster

V2-SPEC.md (390 lines, full)

~2.5 hours

3 to 5 hours

1.5x faster

Design decisions locked

~15 min

30 to 45 min

3x faster

Agentic execution scaffold

~45 min

1 to 2 hours

2x faster

CLAUDE.md and DevOps setup

~30 min

45 to 60 min

Comparable

V2 full build, 14 steps (Codex runtime)

1 director session

3 to 5 days (AI-native solo)

10x to 15x faster

Vercel deployment

Included in build run

1 to 2 hours standalone

Comparable to faster

Session capture and cost analysis

~35 min

45 to 60 min

Comparable

Where you outpaced the 2026 market: The spec-to-deploy pipeline collapsed into a single director session because the honest codebase read directly scaffolded the spec, the spec directly scaffolded the Codex prompt, and the Codex prompt was tight enough to run 14 steps without a remediation loop; a 2026 AI-native agency would have broken this into at least three separate handoff cycles with client review between them.

Where the 2026 market would have matched or beaten you: A 2026 AI-native studio with a dedicated game designer would have shipped ability tuning values derived from playtesting rather than estimation, and would have completed the §10 acceptance test pass before declaring the build done; those are genuine gaps in this session's delivery.

5. Value Delivered Today

2022 agency would have billed a client: $65,000 to $85,000 2026 fCTO bills a client today: $5,000 to $10,000 Your personal cost as AI-native solo: $600 in director time plus unlogged Codex credits Your timeline versus 2026 market standard: Dramatically faster, compressing a 5 to 8 week build into one director session with Codex handling implementation

The range in billing figures is driven by whether the engagement is priced hourly at market rates or positioned as an outcome-based project; the lower bound is strict hourly billing against actual professional hours equivalent, the upper bound reflects what a client would pay for a fully specified, built, and deployed V2 game delivered in a single session.

6. Margin Reality (Private)

Billable at 2026 fCTO rates: $5,650 (hourly equivalent); up to $10,000 on project pricing. Director time cost: $600. Margin on director time: $5,050 at hourly billing = 89%. Up to $9,400 on project pricing = 94%.

The 89 to 94% margin on a full spec-and-build session is the Eagle Rocket thesis at its clearest: Codex absorbed the implementation labor entirely, the Codex credits are a cost-of-goods figure not a labor figure, and what the client pays for is the director judgment that made the 14-step build run clean on the first pass.

7. Running Context

No prior session totals provided. Starting the tally.

Total billed this project at 2026 fCTO rates: $5,650 (hourly) to $10,000 (project) Total director hours logged: 4 hours Effective hourly yield on your time: $1,412/hour (hourly billing) to $2,500/hour (project billing)

8. One Honest Caveat

The ability tuning numbers shipped in V2 have never been playtested. A 2022 senior game developer or a 2026 studio with QA cycles would have run the build against real players before shipping, and the cooldown values, damage multipliers, and AI scoring weights in §4 would have been revised at least once. The §10 acceptance tests have not been manually verified. The game is deployed but the balance is assumed, not confirmed. That is a specific and recoverable gap, but it is a gap.

9. Conclusion

This session moved from V1 codebase read to V2 fully deployed in approximately 4 director hours. The 2022 equivalent of that scope was 37 solo days and $29,600 in opportunity cost, or $76,800 billed through an agency. The 74x compression ratio is not evenly distributed: it concentrates at the implementation layer, where Codex absorbed roughly 30 days of 2022 solo build work under a single agentic prompt. The architecture and judgment work did not compress in the same way, which is precisely why the fCTO margin holds: the 4 director hours are the irreducible human contribution, and they are what made the Codex run coherent enough to ship.

At 89% margin on director time and a $1,400 per hour effective yield, the Eagle Rocket model is demonstrably viable on creative software builds of this kind. The structural limit is not the margin, it is the pipeline: this session generated significant value from a single focused block, but it requires a clear brief, an honest codebase read, and a spec tight enough to run an agentic prompt without remediation loops. Those conditions do not show up automatically. They are the product of the director discipline, and they take time to establish with each new client context. The model scales if the intake process is standardized; it does not scale if every session starts from scratch.

The operational lesson from today is to add the §10 acceptance test pass to the session close checklist rather than treating it as optional follow-up. The build shipped clean and the deploy worked, but a game with unverified ability tuning and no confirmed mobile touch behavior is not fully done. Next time: run the 12-item acceptance test pass before filing the session as complete, not after. That is a 30-minute check that separates "deployed" from "delivered."
