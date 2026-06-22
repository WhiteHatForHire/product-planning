---
title: "# Symposium OS Leveling Up Note Skills Marketplace, Shared Language, and Agent Handoffs"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Leveling up /# Symposium OS Leveling Up Note_ Skills Marketplace, Shared Language, and Agent Handoffs.docx"
status: archive
privacy: working
tags:
  - studio-os
---

# # Symposium OS Leveling Up Note Skills Marketplace, Shared Language, and Agent Handoffs

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# Symposium OS Leveling Up Note: Skills Marketplace, Shared Language, and Agent Handoffs

Status: Parked for later

Suggested path: `/levelingup/symposium-os-skills-marketplace.md`

Priority: High signal, not a today task

Owner: Marcus Vale / Symposium Studios

Source material: Matt Pocock skills repo, Brad execution-layer video transcript, Marcus/Charlie notes from May 2026

## Executive read

This is high signal for Symposium Studios because it points at the next layer of the Director Model.

The first layer is the archive: build logs, specs, directives, journal entries, docs, operating principles, product history, and pattern memory.

The second layer is execution: reusable skills that turn the archive and project context into finished work.

The missing layer between them is shared language: a durable glossary and decision history that lets agents understand the actual domain instead of re-learning Marcus’s intent every session.

For Symposium OS, the target is not to copy Matt Pocock’s skills directly. The target is to extract the pattern and adapt it:

> The archive holds memory. The skills execute judgment. The language layer keeps the machine aligned.

This should become a post-Anchor-Mobile / post-Tech-Week infrastructure project.

Do not open this while Anchor Mobile, business cards, public sites, travel, and Tech Week prep are still active. Seed it, park it, and return when the current launch cycle is stable.

## Why this matters for Symposium

Symposium Studios is already developing a distinctive agentic build method:

- AUTONOMY_LAYER directives

- META_PROMPT scope conversion

- API Surface Diagnostic before frontend/mobile waves

- Deployment Preflight

- MCP Write Safety / Section 1.12 preflight

- Council of Models review

- Build Report / Compression Ledger

- Public Surface QA

- Agent Directive Generator

- EOD work inventory and compression estimates

Right now these are scattered across conversations, docs, build logs, and memory. They work, but they are not yet cleanly packaged as executable law.

The Brad execution-layer frame says: a company brain is not enough unless there is a layer that turns context into action.

The Matt Pocock skills frame adds: the execution layer needs shared language, ADRs, handoffs, and prototypes so agents do not drift from the operator’s mental model.

For Marcus, this is not generic AI productivity. This is the operating system for a solo or small-team AI-native studio.

## Core concept

### Context layer

The context layer is the brain.

Examples:

- `CONTEXT.md`

- `docs/adr/`

- product specs

- build logs

- PR history

- issue history

- journal continuity briefs

- launch docs

- client discovery docs

- public positioning docs

- screenshots and artifacts

This layer answers: what do we know?

### Execution layer

The execution layer is the skill system.

Examples:

- `/api-surface-diagnostic`

- `/deployment-preflight`

- `/mcp-write-safety`

- `/generate-directive`

- `/council-review`

- `/build-report-ledger`

- `/public-surface-qa`

- `/handoff`

- `/prototype`

- `/grill-with-docs`

This layer answers: what do we do with what we know?

### Language layer

The language layer is the alignment layer between the archive and execution.

Examples:

- shared glossary

- domain terms

- product-specific meanings

- forbidden ambiguity

- decision records

- canonical names for recurring patterns

- “this word means this in this repo”

This layer answers: what do these words mean here?

The language layer is what prevents an agent from treating “slip,” “check-in,” “commitment,” “crisis,” “red space,” “public surface,” “Director Model,” or “proof artifact” like generic terms.

## What to adopt from Matt Pocock’s repo

### 1. `grill-with-docs`

High signal.

The skill combines an interview/planning session with repository-aware documentation. It challenges the user’s plan against existing domain language, sharpens terminology, cross-checks against code, updates `CONTEXT.md`, and creates ADRs when decisions are meaningful enough to preserve.

Symposium adaptation:

Create `/grill-with-docs-symposium`.

Use when:

- starting a new feature

- writing a client build directive

- introducing a new domain term

- changing app behavior that depends on product language

- clarifying ambiguous concepts before an agent builds

Output should include:

- resolved glossary terms

- open terminology questions

- relevant code paths checked

- any contradictions between plan and current implementation

- recommended ADRs, only when justified

- next-step directive or PRD path

Important rule:

`CONTEXT.md` should stay a glossary, not a spec or scratchpad. Implementation choices go into specs, issues, or ADRs.

### 2. `CONTEXT.md` / ubiquitous language

Very high signal.

Each repo should carry its own shared language document.

For Anchor, terms could include:

- check-in

- tracker

- commitment

- sober reset

- slip

- relapse

- crisis

- SOS

- program-aware prompt

- sponsor tone

- red/yellow/green state

- memory layer

- safety hard-stop

For Symposium Studios:

- public surface

- proof artifact

- fit call

- build sprint

- technical direction

- client rescue

- LLM-integrated product

- Director Model

- senior-led development

- judgment layer

For Marcus Vale:

- field note

- thesis piece

- build log

- Pattern Intimacy

- AI-native studio

- human judgment

- model council

- archive

- execution layer

This is not literary branding. It is operational compression.

A good shared language layer means agents spend fewer tokens rediscovering what Marcus already means.

### 3. ADRs

High signal.

ADRs preserve non-obvious decisions.

Use an ADR only when all three are true:

1. The decision is hard to reverse.

2. A future reader would wonder why it was done this way.

3. The decision involved a real trade-off.

Possible Symposium/Anchor ADRs:

- Why Anchor crisis responses remove the input bar instead of merely warning the user.

- Why SOS is quiet and text-based rather than red/floating by default.

- Why API Surface Diagnostic is mandatory before any wave touching backend/API shapes.

- Why MCP Write Safety preflight is mandatory before large remote writes.

- Why Marcus Vale hides music pre-Tech-Week.

- Why Symposium Studios avoids overusing “AI-native” in client-facing copy.

- Why business card QR routes to `/marcus` rather than directly to a homepage.

Do not ADR everything. Too many ADRs become noise.

### 4. `handoff`

Very high signal.

Marcus already uses continuity briefs and build handoffs. This skill formalizes that pattern for agent-to-agent work.

Symposium adaptation:

Create `/handoff-symposium`.

Use when:

- switching from planning to implementation

- splitting a long Claude thread into Codex execution

- moving from local agent to cloud agent

- closing a build session

- handing one PR to another agent for review/fix

- preserving context before compaction

Required sections:

- objective

- current state

- what is already done

- exact files/PRs/issues/artifacts to read

- do not duplicate these artifacts

- next agent’s job

- suggested skills/directives to use

- stop gates

- known risks

- acceptance criteria

Key rule:

Do not repeat everything. Reference durable artifacts by path, PR, issue, or URL.

### 5. `prototype`

High signal, especially for taste and product design.

A prototype is throwaway code that answers a question.

Two branches:

- Logic prototype: small interactive terminal/state-machine prototype for business logic, state transitions, or data model uncertainty.

- UI prototype: several radically different UI variations switchable from one route or parameter.

Symposium adaptation:

Create `/prototype-symposium`.

Use before implementation when:

- UI taste is unresolved

- information architecture is fuzzy

- state-machine behavior is hard to reason about

- “feel” matters and human review is necessary

- the agent might build too much too soon

Rules:

- Clearly mark prototype code as throwaway.

- One command to run.

- No persistence unless persistence is the thing being tested.

- Surface state after every action or variant switch.

- Capture the answer somewhere durable when done.

- Delete or absorb the prototype. Do not leave it rotting.

Applications:

- Anchor mobile check-in UX variants

- SOS screen tone variants

- Marcus Vale homepage variations

- Symposium QR page routing

- Dream Mirror interaction loops

- AI-native game state prototypes

- Phronetics assessment flows

### 6. `diagnose`

High signal for avoiding panic debugging.

Symposium already has this pattern informally. Formalize it.

Use when something breaks and the agent is tempted to thrash.

Loop:

1. Reproduce.

2. Minimize.

3. Hypothesize.

4. Instrument.

5. Fix.

6. Regression-test.

Symposium adaptation:

Create `/diagnose-symposium` with extra rules:

- No speculative multi-file edits before reproduction.

- No “maybe this fixes it” commits.

- Save logs and exact failing command.

- If CI runtime suddenly drops, suspect early crash, not faster success.

- If a file was recently edited through MCP or remote tooling, inspect for truncation.

Anchor example:

The `seedUsers.mts` truncation was diagnosable because CI dropped from ~75 minutes to ~85 seconds. That was a signal. The recovery worked because the second agent verified byte length, first/last chars, and named exports before writing.

### 7. `tdd`

Medium-high signal.

Useful, but should not become dogma.

Symposium should use TDD when:

- safety behavior must not regress

- parsing/normalization logic is subtle

- backend API behavior is contract-dependent

- state transitions are important

- production bug needs a regression test

Do not use TDD for:

- pure visual polish

- exploratory UI taste

- copy-only edits

- throwaway prototypes

- urgent deployment routing fixes where smoke tests are more appropriate

### 8. `to-issues` and `to-prd`

Medium-high signal.

Useful for turning plans into vertical slices.

Symposium adaptation:

- `/to-prd-symposium`: turn current context into a builder-ready PRD with scope review, defaults, constraints, acceptance criteria, and stop gates.

- `/to-issues-symposium`: break PRD into independently grabbable GitHub issues with one concern per issue.

Must include Marcus-specific rules:

- one concern per commit

- no bundled unrelated changes

- automated acceptance vs human review separated

- do not invent fallback content

- declare manual playtest requirements

- include deployment or explicitly state no deploy

### 9. `zoom-out`

Medium signal, potentially very useful when agents tunnel.

Use when:

- agent is stuck in a file-level fix

- architecture is unclear

- PR is accumulating patches without a clear model

- Marcus needs a high-altitude read before directing next step

Symposium adaptation:

Create `/zoom-out-symposium`.

Output:

- what system this code belongs to

- adjacent modules

- hidden coupling

- likely failure modes

- simpler architecture option

- what not to touch

### 10. `improve-codebase-architecture`

High signal, but use carefully.

Good as a periodic architecture review, not a constant refactor permission slip.

Use when:

- codebase is getting muddy after agent waves

- repeated patches suggest deeper design issue

- test pain is rising

- naming/language drift is increasing

- onboarding a new agent feels hard because structure is unclear

Rules:

- Must read `CONTEXT.md` and ADRs first.

- Must identify deepening opportunities, not just aesthetic refactors.

- Must propose small, reversible improvements first.

- Must not launch a large refactor without explicit directive and acceptance criteria.

## Proposed Symposium OS repo structure

Future private repo idea:

```text

symposium-os/

README.md

CONTEXT.md

docs/

adr/

0001-symposium-os-purpose.md

0002-skills-marketplace-over-custom-agent-platform.md

levelingup/

symposium-os-skills-marketplace.md

brad-execution-layer-notes.md

matt-pocock-skills-notes.md

skills/

planning/

grill-with-docs-symposium/

SKILL.md

agent-directive-generator/

SKILL.md

to-prd-symposium/

SKILL.md

to-issues-symposium/

SKILL.md

engineering/

api-surface-diagnostic/

SKILL.md

deployment-preflight/

SKILL.md

mcp-write-safety/

SKILL.md

diagnose-symposium/

SKILL.md

tdd-symposium/

SKILL.md

prototype-symposium/

SKILL.md

zoom-out-symposium/

SKILL.md

architecture-review/

SKILL.md

review/

council-review/

SKILL.md

public-surface-qa/

SKILL.md

build-report-ledger/

SKILL.md

productivity/

handoff-symposium/

SKILL.md

session-closeout/

SKILL.md

context-transfer/

SKILL.md

templates/

adr-template.md

context-template.md

build-report-template.md

directive-template.md

handoff-template.md

```

## First Symposium-native skills to build

Do not start with everything. Start with the skills that already proved value in Anchor.

### Wave 1: proven urgent value

1. API Surface Diagnostic

2. Deployment Preflight

3. MCP Write Safety

4. Handoff Symposium

5. Build Report / Compression Ledger

### Wave 2: planning and language

6. Grill With Docs Symposium

7. Context.md / Ubiquitous Language Template

8. ADR Template and ADR Writer

9. Agent Directive Generator

### Wave 3: quality and product taste

10. Public Surface QA

11. Council Review

12. Prototype Symposium

13. Diagnose Symposium

14. Architecture Review

## Draft skill briefs

### API Surface Diagnostic

Purpose: prevent spec-reality drift before any frontend, mobile, or integration wave touches the API.

Inputs:

- repo path

- feature scope

- relevant frontend/mobile screens

- suspected backend routes

Agent actions:

- read actual route handlers

- list endpoints

- list request methods

- list required auth/session behavior

- list request body shapes

- list response shapes

- list error shapes

- identify deltas from existing spec/directive

- produce a table

Stop gate:

No build wave may begin until this table exists for backend-dependent work.

### Deployment Preflight

Purpose: catch environment/deployment mistakes before debugging the client.

Checks:

- correct working directory

- correct project/app ID

- correct deployment target

- env vars present in the right environment

- secrets not missing

- API health endpoint live

- frontend API base URL baked into build

- auth provider and callback URLs configured

- CORS origin list correct

- build command confirmed

- post-deploy smoke command defined

### MCP Write Safety

Purpose: prevent remote write truncation, especially on larger files.

Required before remote/MCP edits on non-trivial files:

- byte length before write

- line count before write

- first 200 chars captured

- last 200 chars captured

- named exports/functions/classes listed when relevant

- write performed

- byte length after write

- line count after write

- first/last chars checked

- exports/functions/classes still present

- no force push unless explicitly authorized

### Build Report / Compression Ledger

Purpose: turn work sessions into receipts.

Sections:

- work inventory

- backend/frontend/infra/QA/devops/design/technical leadership

- shipped vs open PRs

- tests added/passing

- 2022 pre-AI baseline

- 2026 AI-native market baseline

- actual director hours

- compression ratio

- private margin estimate

- caveats

- workflow lessons

- next-session handoff

### Public Surface QA

Purpose: prevent credibility damage before publishing Marcus Vale / Symposium surfaces.

Checks:

- mobile readability

- desktop/tablet layout

- clipping/overflow

- weird artifacts

- CTA clarity

- proof credibility

- no fake metrics

- no empty build-log links

- nav links work

- QR destination works

- contact path works

- copy does not overclaim

- Marcus Vale and Symposium jobs are distinct

### Council Review

Purpose: catch issues from multiple lenses before merge/publish.

Lenses:

- product

- UX

- architecture

- safety/risk

- business/commercial

- brand/public credibility

- operations/maintainability

Rule:

Council can hold a PR or publication. It should not create scope creep unless risk is material.

## Rules for Symposium skill design

1. Skills should be small, composable, and easy to edit.

2. Skills should encode Marcus’s standards, not hide them behind opaque automation.

3. Every skill should have a clear use case and a clear stop point.

4. Skills should produce durable artifacts when a decision matters.

5. Skills should reduce repeated explaining, not create more documentation debt.

6. Skills should work across Claude, Codex, and future tools wherever possible.

7. Skills should prefer paths, PRs, issues, and artifacts over duplicated summaries.

8. Skills should separate automated acceptance from human review.

9. Skills should protect the director’s attention.

10. Skills are executable law, not decorative prompts.

## When to build this

Not today.

Trigger conditions for opening this project:

- Anchor Mobile V1 is shipped or at least through TestFlight gate.

- Tech Week public surfaces are printed/launched/stable.

- Business cards are ordered and QR path works.

- Travel/farm/passport loops are not in acute mode.

- Marcus has a clean Build block with enough quiet to create durable infrastructure.

## First action when reopened

Create a private repo or folder for Symposium OS.

Then add only three files:

1. `README.md`

2. `CONTEXT.md`

3. `docs/levelingup/symposium-os-skills-marketplace.md`

Do not build all skills immediately.

Then create ADR 0001:

`0001-use-a-private-skills-marketplace-for-symposium-os.md`

Decision:

Symposium Studios will encode its agentic build standards as small, portable, version-controlled skills rather than relying only on long chat prompts, memory, or tool-specific configuration.

Rationale:

The archive is not enough. The archive needs executable law.

## Source notes

- Matt Pocock’s skills repo frames the skills as small, adaptable, composable tools for real engineering rather than process-owning frameworks.

- The repo identifies common agent failure modes: misalignment, verbosity/language drift, weak feedback loops, and codebase entropy.

- `grill-with-docs` combines planning interviews with `CONTEXT.md` and ADR updates.

- `prototype` distinguishes logic prototypes from UI prototypes and treats prototypes as throwaway code that answers a question.

- `handoff` compacts the current conversation for another agent and tells it to reference existing artifacts rather than duplicating them.

- The repo also includes `diagnose`, `tdd`, `to-issues`, `to-prd`, `zoom-out`, `improve-codebase-architecture`, `caveman`, `grill-me`, `write-a-skill`, and related setup/guardrail skills.

Primary source: https://github.com/mattpocock/skills

## Parked conclusion

This is not a new side quest. It is future factory machinery.

The Director Model is already working. The next level is turning its repeated judgments into a portable skills layer that can be installed across projects, agents, and eventually team members.

The archive holds memory. The skills execute judgment. The language layer keeps the machine aligned.
