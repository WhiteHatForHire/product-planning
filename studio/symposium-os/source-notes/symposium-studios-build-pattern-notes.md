---
title: "Symposium Studios Build Pattern Notes"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/#Studio OS/Guides and references /Symposium_Studios_Build_Pattern_Notes.docx"
status: active
privacy: working
tags:
  - studio-os
---

# Symposium Studios Build Pattern Notes

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Symposium Studios

Build Pattern Notes

A platform-agnostic field-note system for AI-native software production

Doctrine seed / internal playbook draft
Compiled from current build observations, prompt patterns, and Symposium Studios direction.

Purpose

Build Pattern Notes is a Symposium Studios documentation artifact for capturing repeatable patterns in AI-native software production. It is not a prompt list, not a platform-specific tutorial, and not a hype document. It is an operating doctrine seed: a way to name, reuse, and refine the methods that turn AI agents, image generation, coding tools, testing tools, and human product judgment into shippable software.

The central thesis is simple: the valuable skill is not merely prompting. The valuable skill is directed production. The human director defines the target experience, constraints, rules, state model, review gates, and acceptance criteria; the toolchain assists with assets, implementation, testing, and iteration.

CORE LINE: Do not just ask AI to code. Give it a directed production pipeline.

WORKING DISTINCTION: Vague prompting asks for output. Directed build systems specify target, assets, rules, state, telemetry, QA, and delivery.

SYMPOSIUM STUDIOS FRAME: Human as product director / showrunner; AI agents as implementation machinery; the artifact as inspectable, runnable, and shareable proof.

Why this exists

AI-assisted builds often fail because the process is under-directed, not because the models are incapable.

Most prompts start too abstractly: "build me an app," "make a game," or "create a dashboard." These phrases leave too much product judgment to the agent.

Strong builds use scaffolds: visual targets, genre constraints, state models, acceptance criteria, debug visibility, and human review gates.

The same patterns apply across games, mobile apps, PWAs, recovery tools, dashboards, simulations, internal tools, and AI-native worlds.

Captured doctrine becomes studio IP: a pattern language that can train agents, onboard collaborators, guide client projects, and eventually become public thought leadership.

Observed prompt signals

Recent build prompts point toward a shared grammar. The examples below are not included as platform commitments; they are field signals that reveal useful production patterns.

Observed prompt

Pattern signal

Native roguelike / dungeon crawler prompt

Use image generation to create the ideal app interface, generate tilesets and textures, then build a turn-by-turn dungeon crawler with telemetry and an end-to-end playable deliverable.

2D platformer prompt

Build a full-screen 2D platformer with generated sprites and assets, then use visual browser testing to verify the result.

Voxel FPS prompt

Generate a voxel-based FPS game with a cyberpunk mood, using genre and mood as immediate constraints.

ASCII roguelike wrapped in a modern interface

Start with mood and UI direction, then build a complete small prototype with procedural dungeon, combat, loot, leveling, inventory, and shareable GitHub output.

What the prompt grammar teaches

Define the target experience before implementation.

Generate or collect assets before the engine is asked to make the product feel alive.

Use genre/product scaffolds as constraints, not just labels.

Treat mood as product architecture; it shapes mechanics, layout, feedback, and perceived quality.

Include visual QA and automated interaction checks, not just compile/build checks.

Demand a small complete loop rather than a broad fake demo.

Make the deliverable runnable, screenshottable, reviewable, and shareable.

The core build grammar

A Symposium Studios build should generally move through this sequence unless there is a deliberate reason to do otherwise:

1. Target: define the target interface, target session, or target emotional experience.

2. Assets: generate or gather the visual, written, data, or content materials needed to make the prototype feel real.

3. Rules: define state, boundaries, transitions, permissions, failure states, and win/completion states.

4. Interface: build the user-facing shell and primary interaction loop.

5. Telemetry: expose enough debug information to understand state, actions, failures, and agent decisions.

6. Playable proof: ship one complete end-to-end loop.

7. Visual QA: interact with and screenshot the system; verify it looks and behaves like the target.

8. Shareable artifact: package the result so it can be reviewed, presented, archived, or handed off.

OPERATING PRINCIPLE: Target -> Assets -> Rules -> State -> Interface -> Telemetry -> Playable proof -> Visual QA -> Shareable artifact.

Pattern index

No.

Pattern

One-line description

001

Visual-Target-First Build

Start from a target experience or target interface before implementation.

002

Asset-Then-Engine

Gather surface materials and content before implementation so the prototype has product feel.

003

Telemetry-First Prototypes

Add debug visibility from the start: state, events, transitions, errors, logs.

004

State-Governed AI Worlds

Let AI narrate or assist, but keep state, progression, and safety deterministic and inspectable.

005

Playable Proof Over Demo

Prefer one complete end-to-end loop over a broad but fake prototype.

006

Multi-Tool Build Chains

Split vision, assets, implementation, QA, and packaging across specialized tools.

007

Genre-as-Constraint

Use familiar product or game forms to reduce ambiguity and control scope.

008

Mood-to-Mechanics

Define tone and emotional language before mechanics so the experience feels coherent.

009

Visual QA Loop

Use automation and screenshots to validate visible usability, not only code execution.

010

Shareable Build Artifacts

Design prototypes so they can be run, screenshotted, reviewed, and shown immediately.

011

Platform-Agnostic Runtime Selection

Choose the runtime after the product loop is clear, not from tool novelty.

012

Mobile Shipping Pipeline

Treat Expo/TestFlight/App Store as a repeatable capability milestone, not a one-off port.

013

Human Feel Review Gates

Separate automated checks from human judgment about feel, tone, pacing, and trust.

014

Autonomous Build Directive

Convert ideas into bounded, acceptance-gated directives that agents can execute without guesswork.

015

Doctrine Capture Loop

Turn noticed build patterns into durable studio IP before they evaporate into chat history.

Standard note template

# [Pattern Name]

## One-line summary

## Problem it solves

## Core sequence

## Where it applies

## Where it fails

## Minimum viable version

## Agent prompt skeleton

## Acceptance criteria

## Human review notes

## Related patterns

001 — Visual-Target-First Build

ONE-LINE SUMMARY: Generate or define the target interface, target session, or target experience before implementation begins.

Problem it solves

Vague build prompts leave the agent guessing what good looks like. A target-first approach gives the agent a visible or experiential contract before code is written.

Core sequence

1. Create a target screenshot, target wireframe, target session transcript, or target output example.

2. Translate the target into layout, interaction, state, and acceptance criteria.

3. Build toward the target in bounded phases.

4. Review the delivered artifact against the original target, then revise the target or implementation deliberately.

Where it applies

Games, mobile apps, dashboards, landing pages, onboarding flows, AI chat products, recovery tools, simulations.

Any product where “feel” and interface hierarchy matter.

Any agentic build where the first failure mode is ambiguity.

Where it fails

When the target artifact is decorative but not functional.

When the visual target ignores data, state, permissions, or failure modes.

When the agent treats the mockup as exact pixel law instead of product direction.

Minimum viable version

One mock screenshot or target transcript plus a short list of must-match behaviors.

Agent prompt skeleton

Create the target experience first. Produce a concise visual/UI direction or target session before coding.

Then implement a small working version that matches the target's layout, interaction model, and tone.

Do not invent a different product direction during implementation. If the target is impossible, document the adjustment.

Acceptance criteria

Target artifact exists before implementation.

Implementation references the target in the build plan.

Primary layout and interaction loop match the target.

Known deviations are documented instead of hidden.

Human review notes

Human review should judge whether the delivered artifact feels like the intended product, not just whether it compiles.

Related patterns

002 Asset-Then-Engine, 008 Mood-to-Mechanics, 009 Visual QA Loop

002 — Asset-Then-Engine

ONE-LINE SUMMARY: Gather or generate surface assets before building so the prototype has product feel, not just mechanics.

Problem it solves

Agent-built prototypes often function but feel empty because assets, copy, sample data, and visual surfaces are treated as afterthoughts.

Core sequence

1. Define the product mood and surface requirements.

2. Generate or collect sprites, icons, textures, copy, sample data, or seed content.

3. Use the assets to inform interface and engine decisions.

4. Build the smallest loop that makes those assets meaningful.

Where it applies

Games, AI-native worlds, educational apps, recovery apps, onboarding, demos, pitch prototypes.

Any experience where the surface layer carries user trust or emotional charge.

Where it fails

When asset work becomes procrastination before a working loop exists.

When assets are too polished for a fragile engine.

When generated assets introduce licensing or brand problems.

Minimum viable version

A small asset pack: one visual theme, three to five UI elements, sample copy, sample data, and one complete user path.

Agent prompt skeleton

Before building the engine, create the minimum asset/content set required for the experience to feel real.

Use these assets during implementation.

Do not leave the app filled with placeholder copy, generic boxes, or unstyled test content unless explicitly marked as debug.

Acceptance criteria

Minimum asset set exists.

Prototype uses real-ish surface material.

No generic placeholder dominates the main path.

Assets support, not obscure, the core loop.

Human review notes

Human review should ask: does this feel like an early version of the real product, or a skeleton with decorations?

Related patterns

001 Visual-Target-First Build, 008 Mood-to-Mechanics, 010 Shareable Build Artifacts

003 — Telemetry-First Prototypes

ONE-LINE SUMMARY: Build debug visibility from the start so the human director can inspect state, events, transitions, errors, and agent decisions.

Problem it solves

AI-generated systems can become mystical black boxes. Without telemetry, the human cannot tell whether the problem is UI, state, model output, validation, or persistence.

Core sequence

1. Identify the state that matters.

2. Expose current state and recent events in a debug surface.

3. Log transitions, errors, and fallback paths.

4. Make reset/export/replay possible where useful.

5. Use telemetry during human review before adding scope.

Where it applies

Games, AI apps, workflow tools, onboarding flows, recovery systems, dashboards, payments, integrations.

Any prototype with hidden state or generated output.

Where it fails

When telemetry leaks sensitive data.

When debug UI ships publicly without role gating.

When logs are noisy but not decision-useful.

Minimum viable version

A debug panel showing current state, last 20 events, errors, and reset/export controls.

Agent prompt skeleton

Implement debug visibility as part of the MVP.

Expose current state, recent events, errors, and important transitions.

If AI is used, show prompt version, model name, validation result, fallback path, and memory/context status.

Do not hide state problems behind polished UI.

Acceptance criteria

Current state is inspectable.

Event log exists.

Errors are visible enough for debugging.

Reset path exists.

Sensitive data is not exposed in unsafe contexts.

Human review notes

Human review should use telemetry actively: click through the product while watching state changes and logs.

Related patterns

004 State-Governed AI Worlds, 009 Visual QA Loop, 014 Autonomous Build Directive

004 — State-Governed AI Worlds

ONE-LINE SUMMARY: AI may narrate or assist, but the system must own state, rules, progression, and safety boundaries.

Problem it solves

Unconstrained AI worlds hallucinate progress, inventory, rules, relationships, and safety behavior. A state-governed system allows creativity inside deterministic boundaries.

Core sequence

1. Define world or product state.

2. Define allowed actions and transitions.

3. Let AI generate narration, coaching, description, or interpretation inside those constraints.

4. Validate AI output before applying state changes.

5. Keep progression server-authoritative or system-authoritative.

Where it applies

Interactive fiction, AI games, recovery companions, coaching systems, simulations, learning environments.

Any experience where the AI is expressive but should not own truth.

Where it fails

When deterministic rules are so rigid that the experience feels dead.

When AI output can mutate state without validation.

When safety boundaries are left to tone instead of system rules.

Minimum viable version

One constrained world or workflow with explicit state, allowed transitions, AI narration, validation, and debug proof panel.

Agent prompt skeleton

Build a state-governed AI experience.

The system owns state, allowed transitions, progression, and safety boundaries.

The AI may narrate, explain, suggest, or dramatize within those constraints.

Every state change must be validated by deterministic code before it is committed.

Acceptance criteria

State schema is explicit.

Allowed transitions are explicit.

AI output cannot directly override state.

Invalid actions are handled gracefully.

Debug panel proves state changes.

Human review notes

Human review should test adversarial and edge-case inputs, not just the happy path.

Related patterns

003 Telemetry-First Prototypes, 005 Playable Proof Over Demo, 014 Autonomous Build Directive

005 — Playable Proof Over Demo

ONE-LINE SUMMARY: Prefer one complete end-to-end loop over a broad but fake prototype.

Problem it solves

Broad demos impress briefly but collapse under interaction. A playable proof demonstrates that the system can actually complete a loop.

Core sequence

1. Choose one core loop.

2. Implement the loop from start to finish.

3. Include success, failure, and reset states.

4. Add just enough surface to make the loop legible.

5. Do not expand scope until the loop survives review.

Where it applies

Games, MVPs, AI tools, client prototypes, internal workflows, onboarding, checkout/payment flows.

Any project where proof matters more than breadth.

Where it fails

When the chosen loop is not actually the product’s core loop.

When polish is mistaken for completion.

When “one loop” excludes necessary failure or recovery paths.

Minimum viable version

One complete path: entry -> action -> state change -> feedback -> completion -> reset or next step.

Agent prompt skeleton

Build one complete end-to-end loop.

Keep scope small, but make it real.

Include input, state change, feedback, success, failure handling, and reset or next-step behavior.

Do not build broad fake screens that are not connected to the loop.

Acceptance criteria

Core loop works end to end.

Failure path exists.

Reset or next-step behavior exists.

No fake main-path buttons.

Demo can be played or used without explanation.

Human review notes

Human review should ask: can someone use this without being told which parts are fake?

Related patterns

001 Visual-Target-First Build, 003 Telemetry-First Prototypes, 010 Shareable Build Artifacts

006 — Multi-Tool Build Chains

ONE-LINE SUMMARY: Use specialized tools for vision, assets, implementation, QA, and packaging instead of forcing one model to do everything.

Problem it solves

Single-agent builds overload one tool with too many roles. A chain lets each tool do the job it is strongest at.

Core sequence

1. Use image generation or design tools for visual direction.

2. Use coding agents for implementation.

3. Use test tools for interaction and screenshots.

4. Use review agents or human review for critique.

5. Use packaging/deployment tools for shareable output.

Where it applies

Game prototypes, mobile apps, landing pages, design-heavy tools, AI workflows, client MVPs.

Any build where assets, code, and QA are all meaningful.

Where it fails

When handoffs are vague.

When tools conflict over source of truth.

When the chain becomes more complex than the product.

Minimum viable version

A two- or three-tool chain: target artifact, implementation agent, visual/functional test pass.

Agent prompt skeleton

Split the build into specialized stages.

Use one tool for target direction/assets, one for implementation, and one for testing or review.

Each stage must produce an artifact the next stage can use.

Do not let later tools silently overwrite the original product direction.

Acceptance criteria

Each tool/stage has a clear role.

Artifacts pass cleanly between stages.

Source of truth remains clear.

QA is separate from implementation.

Human review notes

Human review should look for handoff drift: did the final product still follow the original target and constraints?

Related patterns

001 Visual-Target-First Build, 009 Visual QA Loop, 010 Shareable Build Artifacts

007 — Genre-as-Constraint

ONE-LINE SUMMARY: Use a familiar product or game form to reduce ambiguity and bound scope.

Problem it solves

Blank-slate invention makes agents guess interaction patterns. Genre provides defaults: controls, progression, feedback, layout, and success/failure expectations.

Core sequence

1. Choose a known genre or product scaffold.

2. Name what conventions should be kept.

3. Name what conventions should be ignored.

4. Build a small complete slice inside that scaffold.

5. Use the scaffold to judge completeness.

Where it applies

Platformers, roguelikes, dashboards, intake forms, check-in apps, CRMs, quiz tools, journals, calendars.

Any product where a recognizable pattern can speed implementation.

Where it fails

When genre becomes cliché instead of constraint.

When the agent copies irrelevant conventions.

When novelty requires breaking the scaffold but the prompt forbids it.

Minimum viable version

A named scaffold plus three kept conventions, three excluded conventions, and one complete loop.

Agent prompt skeleton

Use [genre/product scaffold] as the constraint.

Keep these conventions: [list].

Exclude these conventions: [list].

Build one complete slice that proves the scaffold without expanding into a full product.

Acceptance criteria

Scaffold is named.

Kept/excluded conventions are explicit.

Core loop uses the scaffold.

Scope stays small.

Human review notes

Human review should test whether the genre helped the build become clearer or merely made it derivative.

Related patterns

005 Playable Proof Over Demo, 008 Mood-to-Mechanics, 014 Autonomous Build Directive

008 — Mood-to-Mechanics

ONE-LINE SUMMARY: Define the emotional and visual language first so mechanics serve a coherent experience.

Problem it solves

Many prototypes work mechanically but feel dead, generic, or emotionally wrong. Mood is not decoration; it guides pacing, feedback, copy, hierarchy, and interaction style.

Core sequence

1. Define the mood in plain language.

2. Translate mood into visual system, copy tone, interaction pacing, and feedback.

3. Build mechanics that reinforce the mood.

4. Review the product for emotional coherence, not just features.

Where it applies

Games, recovery apps, coaching systems, journaling tools, creative tools, onboarding, high-trust software.

Any product where user state and trust matter.

Where it fails

When mood becomes vague aesthetic language.

When mood overwhelms clarity.

When the product needs boring reliability more than atmosphere.

Minimum viable version

A mood brief with five adjectives, five concrete UI/copy implications, and three anti-patterns.

Agent prompt skeleton

Before implementation, define the product mood.

Translate the mood into concrete UI, copy, pacing, and feedback rules.

Build the mechanics so they reinforce that mood.

Do not use mood words without implementation consequences.

Acceptance criteria

Mood is defined concretely.

Visual/copy rules derive from mood.

Mechanics support mood.

Anti-patterns are listed.

Human review notes

Human review should judge whether the user would feel the intended emotional signal without reading the brief.

Related patterns

001 Visual-Target-First Build, 002 Asset-Then-Engine, 007 Genre-as-Constraint

009 — Visual QA Loop

ONE-LINE SUMMARY: Use automation and screenshots to validate visible usability, not only code execution.

Problem it solves

Agent-built apps often pass builds while the interface is clipped, unreadable, off-screen, awkward, or visually broken.

Core sequence

1. Build the feature.

2. Run automated interaction through the main path.

3. Capture screenshots at key states.

4. Review screenshots for visual defects and UX friction.

5. File fixes and repeat until acceptable.

Where it applies

Browser apps, PWAs, dashboards, games, mobile web, admin tools, onboarding flows.

Any UI with layout risk.

Where it fails

When screenshot review is skipped.

When visual review is treated as subjective and not linked to acceptance criteria.

When automation only tests happy paths.

Minimum viable version

One Playwright-style test that loads the app, performs the core path, captures screenshots, and verifies no obvious errors.

Agent prompt skeleton

After implementation, run interactive visual QA.

Exercise the main user path.

Capture screenshots for the start, middle, completion, and error/empty states.

Fix visible layout, contrast, clipping, overflow, or broken interaction before marking complete.

Acceptance criteria

Main path is exercised.

Screenshots exist for key states.

No obvious clipping/overflow.

Visual defects are logged or fixed.

Functional checks and visual checks are separated.

Human review notes

Human review remains required for feel, tone, density, and trust. Automation can catch defects; it cannot fully judge product quality.

Related patterns

003 Telemetry-First Prototypes, 006 Multi-Tool Build Chains, 013 Human Feel Review Gates

010 — Shareable Build Artifacts

ONE-LINE SUMMARY: Design prototypes so they can be run, screenshotted, reviewed, and shown immediately.

Problem it solves

A build that only works on the builder’s machine is not yet a studio artifact. The output should be portable enough to review, archive, sell, or hand off.

Core sequence

1. Define the share format: URL, repo, build, video, screenshot set, or package.

2. Include setup/run instructions.

3. Include screenshots or a review path.

4. Include known limitations.

5. Keep the artifact small enough to understand.

Where it applies

Client demos, portfolio pieces, internal prototypes, AI-native games, mobile builds, public field notes.

Any project intended to create proof or trust.

Where it fails

When packaging consumes more time than the MVP.

When shareability causes premature polish.

When sensitive internal material is made public by accident.

Minimum viable version

A README, one-command run instruction, screenshots, and a concise limitations section.

Agent prompt skeleton

Package the prototype as a shareable artifact.

Include run instructions, screenshots, known limitations, and the intended review path.

The artifact should be easy to open, understand, and evaluate without the original builder present.

Acceptance criteria

Run instructions exist.

Screenshots or demo path exists.

Known limitations are documented.

Artifact can be reviewed by another person.

Sensitive information is not exposed.

Human review notes

Human review should ask whether the artifact creates confidence in the method, not just the feature.

Related patterns

005 Playable Proof Over Demo, 009 Visual QA Loop, 015 Doctrine Capture Loop

011 — Platform-Agnostic Runtime Selection

ONE-LINE SUMMARY: Choose the runtime after the product loop is clear, not from tool novelty or platform glamour.

Problem it solves

Teams often lock into SwiftUI, Phaser, Unity, Expo, or web before clarifying the product loop. That can make the prototype more expensive than the question it is trying to answer.

Core sequence

1. Define the core loop and audience.

2. List platform requirements: input, distribution, performance, offline use, camera/audio, payments, notifications.

3. Choose the simplest runtime that proves the loop.

4. Defer native complexity unless it directly improves the proof.

Where it applies

Any prototype with multiple possible runtimes: web, mobile, desktop, game engine, local app, hosted service.

Studio planning and client scoping.

Where it fails

When platform itself is the milestone, such as TestFlight/App Store capability.

When hardware APIs require native implementation.

When the runtime decision is part of the commercial proof.

Minimum viable version

A one-page runtime decision memo: loop, audience, constraints, chosen platform, rejected platforms, migration path.

Agent prompt skeleton

Select the runtime based on the product loop, not novelty.

Compare web/PWA, Expo, native mobile, desktop, and game-engine options.

Choose the smallest runtime that proves the core loop, and document what would trigger a later port.

Acceptance criteria

Runtime choice is justified.

Rejected options are documented.

Migration path is noted.

No unnecessary platform lock-in.

Human review notes

Human review should challenge whether the chosen runtime serves the product or the builder’s excitement.

Related patterns

005 Playable Proof Over Demo, 012 Mobile Shipping Pipeline, 014 Autonomous Build Directive

012 — Mobile Shipping Pipeline

ONE-LINE SUMMARY: Treat Expo, TestFlight, and App Store submission as a repeatable capability milestone, not a one-off port.

Problem it solves

Mobile distribution is a credibility and capability layer. A team that can repeatedly ship to TestFlight/App Store has a different commercial offering than a team that only deploys web prototypes.

Core sequence

1. Stabilize the web/PWA or product loop first.

2. Port to Expo or native stack only after the loop is worth carrying.

3. Set up app identity, signing, build profiles, environment handling, and update pipeline.

4. Ship to TestFlight.

5. Complete App Store review once the product is ready.

Where it applies

Daily-use apps, recovery tools, check-in systems, AI companions, field tools, consumer MVPs, client products.

Products where notifications, home-screen presence, offline use, or mobile trust matter.

Where it fails

When the product loop is still unstable.

When App Store work becomes avoidance from product clarity.

When native scope balloons before the web/PWA proof is reviewed.

Minimum viable version

One existing stable product loop ported to Expo, running in TestFlight with documented build/release steps.

Agent prompt skeleton

Port the stable product loop to Expo with a repeatable mobile release pipeline.

Do not redesign the product during the port unless required.

Set up build profiles, environment variables, app identity, TestFlight release notes, and a documented update process.

Acceptance criteria

Core loop works on device.

Build pipeline is documented.

TestFlight build is available.

Environment handling is safe.

Known native gaps are logged.

Human review notes

Human review should validate mobile feel: thumb reach, speed, notifications, trust, and daily-use practicality.

Related patterns

011 Platform-Agnostic Runtime Selection, 009 Visual QA Loop, 010 Shareable Build Artifacts

013 — Human Feel Review Gates

ONE-LINE SUMMARY: Separate automated checks from human judgment about feel, tone, pacing, density, trust, and product meaning.

Problem it solves

Agents can pass tests while producing products that feel wrong. The human director must protect qualitative judgment instead of outsourcing it to automation.

Core sequence

1. List automated acceptance criteria.

2. List human review criteria separately.

3. Block merge/deploy on automated criteria.

4. Log human review as required where feel matters.

5. Do not let agents claim subjective polish as complete without review.

Where it applies

Design-heavy apps, recovery systems, games, writing tools, coaching products, AI companions, brand surfaces.

Any product where user trust or emotional tone matters.

Where it fails

When human review becomes vague taste without criteria.

When every minor aesthetic choice blocks progress.

When human review is used to avoid shipping.

Minimum viable version

Two acceptance lists: automated checks and human review checks, with feel criteria stated concretely.

Agent prompt skeleton

Split acceptance criteria into AUTOMATED and HUMAN_REVIEW.

Automated checks must pass before completion.

Human review must evaluate tone, density, pacing, trust, and product feel.

Agents may log MANUAL_REVIEW_REQUIRED but must not self-certify subjective quality.

Acceptance criteria

Automated and human criteria are separated.

Subjective criteria are concrete.

Agent does not claim feel completion alone.

Review gate is documented.

Human review notes

Human review should be decisive, not endless. The point is judgment, not perfectionism.

Related patterns

009 Visual QA Loop, 014 Autonomous Build Directive, 015 Doctrine Capture Loop

014 — Autonomous Build Directive

ONE-LINE SUMMARY: Convert ideas into bounded, acceptance-gated directives that agents can execute without asking avoidable questions.

Problem it solves

A good idea is not automatically buildable. Agents need scope, defaults, phases, constraints, fallback content, tests, and stop gates.

Core sequence

1. Run scope review.

2. Declare complexity budget.

3. Define architecture and runtime defaults.

4. Inline fallback content.

5. Split phases with acceptance gates.

6. Separate automated and human review.

7. Specify deploy or stop behavior.

Where it applies

Agentic coding, Codex, Claude Code, Cursor/Windsurf, multi-agent builds, client prototypes, internal tools.

Any build that should proceed autonomously.

Where it fails

When the directive is larger than the available context/time.

When it leaves core content for the agent to invent.

When it lacks stop gates and lets scope sprawl.

Minimum viable version

A one- to three-page directive with phases, constraints, fallback content, automated tests, human review gates, and final output rules.

Agent prompt skeleton

Turn the concept into an autonomous build directive.

Run scope review first.

Declare complexity budget.

Inline fallback copy/data.

Split the work into phases.

Define automated acceptance criteria and human review criteria separately.

State whether deployment is in scope or the agent should commit and stop.

Acceptance criteria

Scope is bounded.

Defaults are explicit.

Fallback content is inline.

Acceptance gates exist.

Deploy/stop behavior is clear.

No avoidable clarifying questions remain.

Human review notes

Human review should check whether the directive removes ambiguity without crushing agent initiative.

Related patterns

003 Telemetry-First Prototypes, 013 Human Feel Review Gates, 015 Doctrine Capture Loop

015 — Doctrine Capture Loop

ONE-LINE SUMMARY: Turn noticed build patterns into durable studio IP before they disappear into chat history.

Problem it solves

Important agentic methods often emerge during live work and are lost because they are not named, indexed, or reusable.

Core sequence

1. Notice a repeated build move.

2. Name the pattern.

3. Write the problem, sequence, use cases, failure modes, prompt skeleton, and acceptance criteria.

4. Test the pattern in a real build.

5. Revise the note based on field evidence.

Where it applies

Studio operations, product methodology, AI-native build workflows, internal playbooks, consulting material, public field notes.

Any repeated practice that could become leverage.

Where it fails

When the note is written before the pattern is tested.

When everything becomes doctrine and nothing gets built.

When IP capture turns into performative publishing too early.

Minimum viable version

One markdown note written after a real observation, linked into the index, with at least one example use case.

Agent prompt skeleton

Capture this build pattern as a reusable note.

Name the pattern.

Describe the problem, sequence, applications, failure modes, minimum viable version, agent prompt skeleton, and acceptance criteria.

Keep it practical and field-tested, not theoretical.

Acceptance criteria

Pattern is named.

Note follows template.

At least one real use case is included.

Failure modes are honest.

The pattern can be reused by another agent or collaborator.

Human review notes

Human review should guard against premature public performance. Capture first; publish later if it becomes durable.

Related patterns

010 Shareable Build Artifacts, 014 Autonomous Build Directive, 006 Multi-Tool Build Chains

Codex-ready directive: create the markdown repository

Use the following directive to create the Build Pattern Notes artifact as a markdown-first repository or folder inside an existing Symposium Studios repo.

Build a small documentation repository for Symposium Studios called Build Pattern Notes.

This is not a game project and not a native macOS app. It is a platform-agnostic documentation/playbook artifact.

Goal:

Create a clean markdown-first internal doctrine repo that captures repeatable AI-native software production patterns. This repo should feel like serious internal field notes from an AI-native product studio: practical, founder/operator-grade, and distinct from vibe coding or generic prompt lists.

Positioning:

Build Pattern Notes is a Symposium Studios artifact for capturing build patterns, agentic production methods, orchestration patterns, QA patterns, product-direction patterns, and reusable structures for AI-assisted software creation.

Required structure:

- README.md

- build-pattern-notes/001-visual-target-first-build.md

- build-pattern-notes/002-asset-then-engine.md

- build-pattern-notes/003-telemetry-first-prototypes.md

- build-pattern-notes/004-state-governed-ai-worlds.md

- build-pattern-notes/005-playable-proof-over-demo.md

- build-pattern-notes/006-multi-tool-build-chains.md

- build-pattern-notes/007-genre-as-constraint.md

- build-pattern-notes/008-mood-to-mechanics.md

- build-pattern-notes/009-visual-qa-loop.md

- build-pattern-notes/010-shareable-build-artifacts.md

- build-pattern-notes/011-platform-agnostic-runtime-selection.md

- build-pattern-notes/012-mobile-shipping-pipeline.md

- build-pattern-notes/013-human-feel-review-gates.md

- build-pattern-notes/014-autonomous-build-directive.md

- build-pattern-notes/015-doctrine-capture-loop.md

README requirements:

1. What this is: an internal Symposium Studios field-note system for documenting repeatable AI-native build patterns.

2. Why it exists: most AI-assisted software work fails because the build process is under-directed, under-specified, and not broken into reusable patterns.

3. What this is not: random prompt collections, one-shot vibe coding, platform-specific docs, or shallow AI hype.

4. How to use the notes: each note is a reusable pattern adaptable across games, tools, apps, PWAs, mobile apps, and interactive AI systems.

5. Pattern index: link every note with a one-line description.

6. Contribution format: future notes should be practical operating doctrine, not theory essays.

7. Status: early field notes / doctrine seed.

Each note must use this template:

# [Pattern Name]

## One-line summary

## Problem it solves

## Core sequence

## Where it applies

## Where it fails

## Minimum viable version

## Agent prompt skeleton

## Acceptance criteria

## Human review notes

## Related patterns

Tone:

- serious

- precise

- practical

- founder/operator-grade

- compact but not shallow

- no hype language

- no juvenile gamer tone even when using game examples

Constraints:

- Keep everything platform-agnostic.

- Do not center SwiftUI, macOS, native-only assumptions, Phaser, or any single runtime.

- Use game examples and software/app examples.

- Make the notes reusable for apps, tools, AI-native products, simulations, and interactive systems.

- Explicitly distinguish the doctrine from vague prompting or vibe coding.

- Emphasize human direction, agent orchestration, inspectable systems, and shareable artifacts.

Acceptance criteria:

- All files are created.

- README links to every pattern note.

- Every note uses the same structure.

- The notes include concrete agent prompt skeletons.

- The notes include honest failure modes.

- The repo reads as the beginning of a serious internal doctrine library for Symposium Studios.

Reusable prompt skeletons

These are not final product specs. They are reusable skeletons for turning the pattern language into build directives.

Visual-target-first interactive prototype

Build a small platform-agnostic interactive prototype using a visual-target-first process.

Phase 1: Create the target experience.

- Describe or generate the ideal screen/session.

- Define layout, controls, information hierarchy, empty/error states, and mood.

Phase 2: Define rules and state.

- Specify state objects, allowed actions, transitions, success/failure states, and reset behavior.

Phase 3: Build one complete loop.

- Implement the smallest working version that proves the core interaction.

Phase 4: Add telemetry.

- Show current state, event log, errors, and reset/export controls.

Phase 5: Visual QA.

- Run through the main path, capture screenshots, and fix obvious layout or usability defects.

Deliverable: runnable, inspectable, screenshottable prototype with README and known limitations.

2D platformer / browser game skeleton

Build a simple 2D platformer prototype in a browser-friendly runtime.

Use generated or placeholder assets only after defining the target visual direction.

The player should move, jump, land on platforms, and progress upward through a constrained level.

Keep scope small: one level, one player, a few platform types, one failure/reset condition, one completion condition.

Add visual QA screenshots for start, mid-level, failure/reset, and completion states.

Add debug telemetry for player position, velocity, collision state, and current level progress.

Deliver a playable proof, not a broad fake demo.

Voxel FPS / mood-constrained game skeleton

Build a small voxel-style first-person prototype with a defined mood and one complete play loop.

Start with mood direction: visual palette, environment feel, UI density, weapon/tool feel, enemy or obstacle tone, and sound/feedback assumptions.

Then define the minimum loop: spawn, move, encounter, act, receive feedback, complete or reset.

Keep it small enough to understand. Prioritize responsive movement, readable environment, telemetry, and screenshots over feature breadth.

State-governed AI world skeleton

Build a state-governed AI world.

The AI may narrate scenes and respond to user actions, but deterministic code owns world state, inventory, location, progression, locked/unlocked paths, and failure/win conditions.

Implement:

- explicit state schema

- allowed action parser

- validated state transitions

- AI narration constrained by current state

- debug proof panel

- event log

- reset and export controls

Deliver one complete world slice with a beginning, progression gate, and completion state.

Expo mobile pipeline skeleton

Port an existing stable product loop to Expo as a mobile capability milestone.

Do not redesign the product during the port unless required.

Implement the core loop on device, safe environment handling, app identity, build profiles, TestFlight-ready configuration, and release notes.

Acceptance criteria:

- core loop works on device

- build command documented

- environment variables are handled safely

- TestFlight build path documented

- known native gaps logged

- screenshots captured for main mobile states

Operating principles for Symposium Studios

DIRECTION BEFORE DELEGATION: Agents can produce quickly, but the human director owns target, constraints, priorities, and acceptance.

SMALL COMPLETE LOOPS BEAT BROAD FAKE WORLDS: One real path creates more proof than ten disconnected screens.

STATE IS SACRED: If the product has progression, memory, safety, inventory, decisions, or payments, state must be explicit and inspectable.

FEEL IS A REVIEW GATE: A product can pass tests and still feel wrong. Human judgment remains part of the build system.

RUNTIME IS A SERVANT, NOT A RELIGION: Choose web, Expo, native, desktop, or game engine based on the loop and the proof required.

TELEMETRY MAKES AGENTS MANAGEABLE: Debug visibility lets the director inspect what the system is doing instead of guessing.

BUILD ARTIFACTS SHOULD TRAVEL: A good prototype can be run, reviewed, screenshotted, archived, and shared without the builder narrating every missing piece.

CAPTURE DOCTRINE WHILE THE PATTERN IS HOT: When a strong build pattern appears, name it and file it before it disappears into chat history.

Suggested next steps

1. Create the markdown repo or folder using the Codex-ready directive above.

2. Keep the first pass simple: README plus 15 notes, no website yet.

3. After three real builds, revise the notes based on field evidence rather than theory.

4. Add a lightweight examples folder later with one applied example per pattern.

5. Eventually turn selected notes into public Symposium Studios Field Notes only after the method has receipts.

CURRENT STATUS: Early doctrine seed. Useful internally now; public positioning later.

CORE TAKEAWAY: You are not just prompting. You are directing build systems.
