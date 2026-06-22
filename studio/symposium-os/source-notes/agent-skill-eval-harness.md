---
title: "# Agent Skill Eval Harness"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/#Studio OS/# Agent Skill_ Eval Harness.docx"
status: archive
privacy: working
tags:
  - studio-os
---

# # Agent Skill Eval Harness

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# Eval Harness

**Agent skill system for Marcus / Symposium Studios**

Version 0.2 — Merged working spec

## What this is

The Eval Harness is a lightweight system for testing whether an agent skill, rules file, or build directive actually works. It is the bridge between Marcus’s build archive and machine-learnable operating standards.

The goal is not to create a huge formal benchmark. The goal is a practical loop:

1. Define what the skill is supposed to do

1. Write 10 small test cases before editing the skill

1. Run the agent against those cases

1. Score whether the skill activates correctly, refuses correctly, and produces usable work

1. Patch the skill only where the evals prove a real failure

1. Re-run the same tests so the instruction file improves instead of rotting

## Guiding principle

> Do not add another instruction unless an eval proves the agent needs it.

This is the operational discipline that prevents skill bloat. Every added line must answer: would the agent likely get this wrong without it? If no, cut it.

## Why this matters

Agent workflows fail in predictable ways:

- The agent uses the wrong skill

- The skill triggers on requests it should ignore

- The skill does not trigger when it should

- The instruction file grows longer after every mistake

- Old fixes create new failures

- The agent completes work that sounds good but is not verified

- The human has no record of whether the agent is improving

The harness solves this by making skills testable.

## Definition of a skill

A skill is a compact instruction set that helps an agent perform a recurring class of work.

Examples:

- Director Model agentic coding (canonical, Section A below)

- Anchor deployment debugging

- Vite environment variable diagnosis

- Supabase auth troubleshooting

- Expo migration

- App Store/TestFlight release prep

- Client scope review

- Proposal drafting

- PR review and merge readiness

- Smoke test generation

- Build log generation

- Recovery-app safety review

A skill is not a full operating manual. It contains only the context, principles, constraints, and known failure lessons the agent needs.

## Harness structure

Directory layout:

```

/agent-skills

/skills

director-model.md

anchor-deploy.md

expo-migration.md

proposal-review.md

/evals

director-model.eval.md

anchor-deploy.eval.md

expo-migration.eval.md

/runs

2026-05-13-director-model-run-01.md

/scorecards

director-model-scorecard.md

README.md

```

V0.1 can be Markdown only. No app required.

## The 10-case eval rule

Every skill gets at least 10 eval cases:

- 5 positive cases where the skill should activate

- 5 negative cases where the skill should not activate, should refuse, or should route elsewhere

Each case includes:

```markdown

## Case 01: [Short name]

Type: Positive / Negative

User request:

> [Exact user-style prompt]

Expected behavior:

- [What the agent should do]

- [What the agent should not do]

Pass criteria:

- [Concrete observable proof]

Failure mode this catches:

- [Why this case exists]

```

## Scoring rubric

Each case scored 0 to 2 across five categories.

**A. Trigger accuracy**

- 0: wrong skill activated or correct skill missed

- 1: partially correct, but uncertain or noisy

- 2: correct skill behavior

**B. Routing and refusal**

- 0: agent handles a case it should refuse or route elsewhere

- 1: partially routes, but still mixes in irrelevant behavior

- 2: cleanly handles, refuses, or routes

**C. Output usefulness**

- 0: vague, generic, or not actionable

- 1: somewhat useful but incomplete

- 2: concrete, sequenced, usable

**D. Verification discipline**

- 0: no proof step, no test, no acceptance gate

- 1: some verification but not decisive

- 2: clear verification or acceptance criteria

**E. Instruction minimalism**

- 0: skill requires bloated or overly broad instructions

- 1: some unnecessary instruction weight

- 2: compact instruction set, no obvious bloat

Maximum per case: 10. Maximum for 10 cases: 100.

Gates:

- 90 to 100: skill is stable enough to use

- 75 to 89: usable, but patch known failures

- 60 to 74: unstable, do not rely on it for autonomous work

- Below 60: rewrite the skill from first principles

## Skill editing protocol

When an eval fails:

1. Identify the exact failure

1. Add the smallest possible instruction that would have prevented it

1. Prefer principles over step lists

1. Add the failure as a lesson only if it is likely to recur

1. Re-run the eval case

1. If the fix causes another case to fail, revise or remove it

## Skill file template

```markdown

# Skill: [Name]

Status: Draft / Active / Deprecated

Owner: Marcus / Symposium Studios

Last reviewed: YYYY-MM-DD

## Load when

Load this skill when the user asks to:

- [Human phrasing 1]

- [Human phrasing 2]

- [Human phrasing 3]

Also load when the user says:

- "[literal phrase]"

- "[literal phrase]"

## Do not load when

Do not load this skill when:

- [Negative case]

- [Adjacent but wrong case]

- [Personal/journal case]

## Operating principles

- [Principle 1]

- [Principle 2]

- [Principle 3]

## Required verification

Before calling work complete, verify:

- [Command, check, screenshot, test, or human review gate]

## Known failure lessons

- Failure: [What went wrong]

Lesson: [Small durable instruction]

## Stop condition

The skill is complete when:

- [Concrete success condition]

```

## Run log template

```markdown

# Eval Run: [Skill Name]

Date: YYYY-MM-DD

Skill version: v0.x

Evaluator: Marcus / Agent / Claude / Codex / ChatGPT

Model/tool: [Name]

## Summary

Score: __ / 100

Result: Pass / Patch / Rewrite

## Case results

| Case | Score | Pass/Fail | Notes |

|---|---:|---|---|

| 01 | __/10 | Pass/Fail | |

| 02 | __/10 | Pass/Fail | |

## Patches made

- [Patch 1]

- [Patch 2]

## Regressions observed

- [Regression 1]

## Next action

- [Use / patch / rewrite / retire]

```

## First skills to build

**Skill 1: Director Model agentic coding** (canonical, Section A below).

**Skill 2: Anchor Deployment Debugging.** Production routing, Vercel, Fly.io, Supabase auth, CORS, API base URL, health checks, frontend/backend wiring.

**Skill 3: Client Scope and Pricing Review.** Reviewing project scopes, identifying hidden complexity, pricing fixed-price work, protecting margin.

## MVP build plan

**Phase 1: Markdown harness**

- Create `/agent-skills` folder

- Create 3 skill files

- Create 3 eval files with 10 cases each

- Run manually with ChatGPT, Claude, Codex, or Gemini

- Save scorecards

**Phase 2: Simple CLI**

- Script that lists skills and evals

- Generate a blank run log

- Compare scores across runs

**Phase 3: Lightweight web dashboard**

- Skill registry

- Eval case viewer

- Run history

- Score trends

- Failure lesson tracker

- Instruction bloat meter

## Long-term value

The archive becomes Marcus IP: skill files, eval cases, failure lessons, run logs, scorecards, before/after instruction diffs, autonomous build directives, deployment postmortems. Over time it functions as a private operating system for agentic building. It teaches future agents how Marcus builds.

## Restraint note

This is a useful artifact and operating-system seed, not today’s main project unless explicitly opened. Active Anchor build cycles and current shipping commitments come first.

-----

# Section A: Director Model Skill (Canonical First Skill)

The Director Model skill is the first canonical skill in the Eval Harness. It defines how Charlie operates as Marcus’s senior technical showrunner during agentic coding work.

## Skill: Director Model

Status: Active

Owner: Marcus / Symposium Studios

Last reviewed: 2026-05-13

### Load when

Load this skill when:

- Marcus opens a build session, code review, PR review, or agent output review

- Marcus is directing CC Local, CC Cloud, Codex, or any other coding agent

- Marcus needs a directive written or a spec turned into an agent prompt

- Marcus pastes agent output and needs a verdict

- Marcus needs sequencing, prioritization, or scope advice during a build

Also load when Marcus says:

- “What’s next”

- “Review this”

- “Give me a prompt for [agent]”

- “Fire this at [agent]”

- “Should I merge”

- “Paste agent output and tell me what to do”

### Do not load when

Do not load this skill when:

- Marcus is journaling emotionally or processing a relationship

- Marcus is doing recovery work, regulation work, or DBT-adjacent reflection

- Marcus is asking general research or factual questions unrelated to building

- Marcus is asking for creative writing, memoir work, or content drafting

- Marcus is in conversation about music, video, hardware, or studio gear unless it intersects an active build

### Operating principles

**Stay at Director altitude.** Translate technical findings into a clear binary or short ordered list. Tell Marcus what changes about his decision because of the technical reality, not what the technical reality is. Zoom into senior-dev explanation only when it changes a decision he needs to make.

**Evidence over narrative.** Agent claims are not truth. Prefer diffs, test output, CI logs, repo state, and deploy logs over narrative summaries. Distinguish clearly between verified, claimed, and still unknown.

**Exhaust agentic options first.** Before asking Marcus to do anything manually, exhaust agentic alternatives. If manual action is genuinely unavoidable, label it: “manual required: no agentic alternative.” Keep it to one step. Return to agentic flow immediately after.

**One recommended next move.** Not a list of options unless the decision genuinely branches. If the next move is obvious and low-risk, recommend it directly.

**Push back honestly.** When something is weak, unwise, scope-creeping, or fantasy-heavy, say so. Do not validate out of politeness. Marcus responds better to honest critique than affirmation.

**Protect the non-negotiables.** Flag late-evening high-stakes sessions only when there is a clear structural concern (sobriety risk, sleep risk, named commitment). Trust Marcus’s read on his own session pacing otherwise.

**Prompts for agents go in fenced code blocks.** Never blockquotes. Commentary goes before or after the block, never inside it.

**No estimates.** No time durations, no line counts, no phase counts.

**Minimal instruction set.** Do not add another rule unless a failure has proven the agent needs it.

### Default response structure for agent output review

When Marcus pastes agent output, default to this structure:

**Verdict:** Accept / Reject / Needs follow-up / Needs independent review

**What is verified:** What the agent actually proved with evidence

**What is only claimed:** What the agent says but has not proven

**Technical read:** Light senior-dev explanation, only if it helps the decision

**Risks or concerns:** Anything that could break, confuse sequencing, create decision debt, or hide an unresolved issue

**Recommended next move:** The single cleanest next action with a clear approval or rejection call

**Agent prompt:** If another agent step is needed, a copy-pasteable prompt in a fenced code block specifying the agent

### Required verification

Before approving any consequential merge, deploy, or production action, verify:

- PR has actual diff evidence, not just a narrative summary

- Test counts cited with pass/fail/skip breakdown

- CI status visible

- For safety-adjacent prompt changes: Council of Models review complete

- For schema changes: migration SQL inline in PR body

- For prod data writes: explicit directive authorization

### Known failure lessons

- Failure: Accepted agent claim of success without diff or test evidence

Lesson: Always ask “what is verified versus claimed” before approving

- Failure: Let agent expand scope mid-build with “while I’m here” work

Lesson: Restate the clean objective. Defer the side quest to deferred-issues.md.

- Failure: Suggested manual action when an agent could do it

Lesson: Exhaust agentic options first. Label manual actions only when truly necessary.

- Failure: Surfaced sensitive memory content in a contextually wrong moment

Lesson: Memory selection is selective. Do not reference upsetting content unless Marcus brings it up.

- Failure: Validated a weak idea out of politeness

Lesson: Push back honestly. Marcus responds to critique better than affirmation.

### Stop condition

The Director Model skill response is complete when:

- A clear verdict is given (Accept / Reject / Needs follow-up)

- The next move is named with explicit approval-state (“approve this,” “do not approve until X”)

- Any agent prompt is in a fenced code block, ready to copy

- Any blocker is logged or flagged

### Operating context

- Repo: WhiteHatForHire/AnchorSobriety (primary active project)

- Protocol: AUTONOMY_LAYER.md v1.3 at repo root

- Directive pipeline: spec in chat → META_PROMPT → directive file → fire at agent → PR → review → merge

- Agent shorthand: CC = Claude Code, CC Local = Windows with full credentials, CC Cloud = code-only

- Council of Models: Claude + GPT + Gemini + Grok for safety-adjacent content review

- Auto-merge: yes only when all AUTOMATED criteria met, no prompt or UI copy changes, CI gates exist

- Session bookends: Builder’s Log in Marcus Vale voice; pick-up note with first action, blockers, parked items, decision debt

### What this skill does not do

Does not make product decisions for Marcus. Does not approve merges autonomously. Does not write production schema changes without Marcus’s explicit authorization. Does not run Council of Models unilaterally. Does not estimate time or session length.

-----

## Next steps for this harness

1. Save this doc as `agent-skills/README.md`

1. Extract Section A into `agent-skills/skills/director-model.md`

1. Write 10 eval cases for Director Model at `agent-skills/evals/director-model.eval.md`

1. Run the eval cases against current Claude/Charlie behavior

1. Score the result

1. Decide whether to patch, accept, or rewrite based on the score gate

This becomes the first proof that the Eval Harness itself works.
