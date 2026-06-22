---
title: "OpenAI Guide to Codex for Marcus"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/#Studio OS/Guides and references /OpenAI_Guide_to_Codex_for_Marcus.docx"
status: active
privacy: working
tags:
  - studio-os
---

# OpenAI Guide to Codex for Marcus

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
OPENAI GUIDE TO CODEX

Marcus Edition: Official Mechanics, Agent-Harness Architecture, Operating Rules, and Quick Reference

Version 1.0 - Source-backed working guide

Purpose

This guide converts the OpenAI Codex material into a practical operating manual for Marcus: what Codex is, how the Codex CLI and Responses API mechanics work, how AGENTS.md changes the game, how to design tool harnesses, and how to apply this inside an AI-native multi-agent build workflow.

Source note: This document uses Marcus's supplied excerpts plus current OpenAI developer documentation checked on May 12, 2026. OpenAI product names, model names, CLI flags, and API details may change; check the official docs before implementing production integrations.

Manual Table of Contents

1. Executive Summary

2. Codex Mental Model

3. OpenAI Mechanics You Need to Understand

4. AGENTS.md: Repo-Local Constitution

5. Tooling Architecture: How to Make Codex Perform Well

6. Operating Rules for Coding Agents

7. Preambles, Phase Metadata, and Long-Running Work

8. Marcus Guide: How You Should Use Codex

9. Anchor-Specific Codex Setup

10. Multi-Agent Coordination Protocol

11. Quick Reference

12. Copy/Paste Templates

13. Source Links and Version Notes

1. Executive Summary

Codex is not merely a chat model that writes code. In the CLI and API patterns described by OpenAI, Codex is a coding agent operating inside a harness: it receives instructions, reads repository state, calls tools, edits files, runs commands, keeps plans, and reports outcomes. The quality of the agent depends on the model and on the harness around it.

The core shift

From prompts to operating systems: Your leverage comes from stable, reusable instructions plus repo-local conventions, not one-off giant prompts for every session.

From chat to execution loop: A good Codex run gathers context, forms a bounded plan, edits, verifies, repairs failures, and summarizes what changed.

From one agent to a team: Your workflow can treat Codex, Claude, ChatGPT, and other tools as specialized agents, with Marcus acting as director/fCTO.

From memory overload to context architecture: Use AGENTS.md for standing rules, task specs for current intent, compaction for long sessions, and handoff notes for continuity.

The biggest practical win

AGENTS.md is the immediate unlock. It lets you place durable instructions at global, repo, and directory levels so Codex starts with the correct operating agreements before every task. This reduces repeated prompt boilerplate and makes the repo itself carry its own agent instructions.

Marcus translation

AGENTS.md is not just documentation. It is an agent constitution. It tells every coding session how to behave before the feature prompt even arrives. The move is not to stuff every philosophical, product, and historical detail into it. The move is to keep it short, practical, and safety-critical, while putting task-specific detail in issue specs and build directives.

2. Codex Mental Model

Codex CLI

OpenAI describes the Codex CLI as a local terminal coding agent that can read, change, and run code in the selected directory. That means the CLI should be treated as a real actor in your repository, not as a passive suggestion engine.

Layer

What It Does

Marcus Interpretation

Model

Reasoning, planning, coding, debugging, natural language

The brain of the session

CLI / harness

File access, terminal execution, patching, plans, tool calls

The body and hands

AGENTS.md

Persistent instruction chain

The constitution

Tools

apply_patch, shell, update_plan, image view, custom functions

The instruments

Repo

Code, tests, conventions, history

The field of action

Marcus

Goal, product taste, risk boundaries, executive approval

The director / fCTO

Agent loop

Receive the task and standing instructions.

Discover repo instructions and relevant files.

Plan only as much as necessary for the task's complexity.

Edit using the least risky mechanism, preferably patch-based edits.

Run verification: tests, typecheck, lint, build, or targeted smoke.

Repair failures if feasible inside the same turn.

Close with a concise, truthful summary of changes, verification, and residual risk.

Important distinction

Autonomy is not permission to be reckless. The target pattern is high autonomy inside bounded lanes, with stop gates around production, credentials, billing, migrations, destructive commands, user data, and live communications.

3. OpenAI Mechanics You Need to Understand

3.1 Codex can operate locally

The CLI is designed to inspect repositories, edit files, and run commands. This is why prompt rules about dirty worktrees, no destructive commands, verification, and clear final summaries matter. Bad instructions can produce bad repository actions.

3.2 AGENTS.md discovery

OpenAI's Codex documentation describes an instruction chain built from global and project-level AGENTS.md files. The chain starts in the Codex home directory and then walks from the project root down to the current working directory. More specific files closer to the current directory can override broader guidance.

Scope

Typical File

What Belongs There

Global

~/.codex/AGENTS.md

Personal defaults, safety gates, reporting preferences, general tool discipline

Repo root

./AGENTS.md

Project overview, test commands, design system, architecture, PR expectations, done definition

Subdirectory

./src/AGENTS.md, ./migrations/AGENTS.md

Local rules that override broad repo rules, such as migration restrictions or frontend conventions

Override

AGENTS.override.md

Higher-priority local instruction when you intentionally need replacement behavior

Do not overstuff it

OpenAI's best-practices guidance favors short, accurate, practical AGENTS.md files over huge vague instruction blocks. If the file grows too large, split stable rules from task-specific playbooks and reference separate docs.

3.3 Compaction

Compaction is OpenAI's mechanism for preserving important state from long-running conversations while reducing context size. In the API, the /responses/compact endpoint returns a compacted response object. In the CLI, /compact replaces earlier turns with a concise summary so the session can continue with less context pressure.

Marcus use case: compaction is the technical version of your continuity briefs. It is not a replacement for final handoffs, build ledgers, or product decision records, but it can keep long Codex sessions moving without drowning the model in raw transcript.

3.4 apply_patch

OpenAI recommends its apply_patch implementation because Codex has been trained to perform well with this diff format. Patch-based editing is easier to audit than freeform file rewrites and is less likely to destroy unrelated changes.

*** Begin Patch
*** Update File: /app/page.tsx
@@
      <div>
        <p>Page component not implemented</p>
        <button onClick={() => console.log("clicked")}>Click me</button>
+       <button onClick={() => console.log("cancel clicked")}>Cancel</button>
      </div>
    );
  }
*** End Patch

3.5 Shell command

OpenAI's default shell tool pattern uses a command string, workdir, timeout, optional escalation flag, and a justification when escalation is requested. The practical rule is: always set workdir, avoid cd when possible, and avoid shell use when a safer dedicated tool exists.

{
  "name": "shell_command",
  "description": "Runs a shell command and returns its output. Always set workdir.",
  "parameters": {
    "command": "string",
    "workdir": "string",
    "timeout_ms": "number",
    "with_escalated_permissions": "boolean",
    "justification": "string"
  }
}

3.6 update_plan

The update_plan tool is the default TODO/planning tool. It should be used for non-trivial tasks, not for the easiest 25% of requests. A plan should not end with pending or in-progress items. Every stated step should be completed, blocked, or cancelled by final response time.

Use Plan When

Skip Plan When

Multi-file feature work

Single obvious edit

Risky refactor

Simple command or answer

Unclear verification path

Tiny typo or copy change

Long-running agent task

One-off read-only inspection

3.7 view_image

view_image attaches a local image by filesystem path to the conversation. This matters for UI review, screenshot boards, design audits, generated assets, visual regression checks, and Playwright screenshot loops.

3.8 Custom tools

OpenAI notes that custom tools can work, but they need careful names, arguments, and examples. Ambiguous tool names like search can confuse the model. More specific names like semantic_search, git, read_file, list_dir, and apply_patch are easier for the model to use correctly.

Bad / Ambiguous

Better

Why

search

semantic_search

Names the retrieval mode

run

shell_command

Clarifies it executes in a shell

files

list_dir / read_file

Separates listing from reading

patch

apply_patch

Matches trained diff behavior

repo

git

Directly maps to git command behavior

4. AGENTS.md: Repo-Local Constitution

AGENTS.md is the cleanest way to make Codex reliably inherit your standing instructions. It should answer the things a senior engineer would need to know before touching the repo.

What belongs in AGENTS.md

Repo layout and important directories.

How to run, build, test, lint, typecheck, and smoke test the project.

Engineering conventions: naming, patterns, state management, database access, API style, error handling.

Product constraints and do-not rules.

Definition of done and verification expectations.

Deployment, migration, secrets, and production stop gates.

What does not belong in AGENTS.md

Entire product history when a short architecture note will do.

Vague motivational language that does not change implementation behavior.

Long philosophical context unless it directly governs product safety or language.

Task-specific requirements that belong in an issue, spec, or build directive.

Large code examples that should live in reference docs or skills.

Layering strategy

Layer

Purpose

Rule of Thumb

Global

Your personal operating style

Stable across all repos

Repo root

Project-level truth

All agents on this repo need it

Feature area

Local conventions

Only applies when working there

Task spec

Current mission

Temporary and specific

Handoff

What happened

Post-run receipt

Recommended AGENTS.md file map for Marcus

~/.codex/AGENTS.md
  Global Marcus coding-agent OS: safety gates, verification rules, multi-agent etiquette.

repo/AGENTS.md
  Project overview, how to run/test/build, design system, product safety, done definition.

repo/src/AGENTS.md
  Frontend conventions, component patterns, styling rules, accessibility expectations.

repo/server/AGENTS.md or repo/api/AGENTS.md
  Backend conventions, logging, validation, error handling, data access rules.

repo/migrations/AGENTS.md
  Strict database safety rules. No production migration without explicit approval.

repo/docs/agent-playbooks/*.md
  Longer reference docs linked from AGENTS.md when needed.

5. Tooling Architecture: How to Make Codex Perform Well

5.1 Prefer dedicated tools over raw shell

The supplied prompt says to prefer solver tools such as git, rg, read_file, list_dir, glob_file_search, apply_patch, and update_plan over raw terminal commands. This makes the agent's behavior safer, more structured, and easier to audit.

Need

Preferred Tool

Shell Fallback

Search text

rg or semantic_search

grep only if rg unavailable

Search files

rg --files, glob_file_search

find only if needed

Read file

read_file

sed/cat only if no file tool exists

Patch file

apply_patch

scripted rewrite only for generated/bulk changes

Git status/diff/log

git dedicated tool

terminal git if no dedicated tool

Run tests

shell_command with workdir

same, but avoid cd

5.2 Parallel tool calls

When parallel tool calling is enabled, OpenAI adds instructions that tell the model to think first, identify all files/resources needed, and batch reads through multi_tool_use.parallel. The intent is to reduce slow one-by-one exploration and avoid wasting turns.

Marcus field rule

Parallel reads are good. Parallel edits by multiple agents in the same files are dangerous. Use parallelism for exploration, not uncoordinated modification.

5.3 Tool response truncation

OpenAI recommends truncating tool outputs to a manageable budget. The supplied guidance uses about 10k tokens, approximated by bytes divided by four. When truncating, keep the beginning and end and mark the middle as truncated. This preserves file headers, imports, setup, and tail-end errors.

Truncation pattern:
- Budget: roughly 10k tokens.
- Approximation: num_bytes / 4.
- If over budget: first half + marker + second half.
- Marker: ...N tokens truncated...

Why it works:
- The beginning often contains imports, definitions, config, and context.
- The end often contains errors, exports, stack traces, and recent output.

5.4 Tool naming matters

Tool names should be semantically clear and close to the underlying action. If the model is trained around terminal patterns, dedicated tools that look like familiar command behavior usually perform better than abstract tools with surprising schemas.

Tool Design Principle

Example

Name the action clearly

read_file(path), list_dir(path), semantic_search(query)

Use familiar argument names

command, workdir, timeout_ms

Keep outputs distinguishable

Do not make semantic search output look exactly like ripgrep

Provide explicit use rules

Use git tool for all git commands; shell only if no dedicated tool exists

Add examples

Good and bad examples reduce tool-selection drift

6. Operating Rules for Coding Agents

6.1 Autonomy and persistence

A good Codex agent should not stop at a plan unless blocked. Once given a direction, it should gather context, implement, test, refine, and report. But this autonomy should be bounded by safety gates.

Good Autonomy

Bad Autonomy

Implements a contained UI fix and runs tests

Touches auth, billing, migrations, and UI in one bundled change

Makes reasonable assumptions and states them

Invents requirements that change the product

Repairs test failures caused by its edits

Chases unrelated pre-existing failures endlessly

Stops at a real blocker with a targeted question

Asks avoidable clarification before reading the repo

6.2 Code implementation standards

Optimize for correctness, clarity, and reliability over speed.

Follow existing codebase conventions before introducing new patterns.

Search for prior helpers before creating new helpers.

Avoid broad try/catch blocks and silent success-shaped fallbacks.

Preserve type safety; avoid unnecessary as any and unsafe casts.

Make coherent edit batches instead of repeated micro-edits.

6.3 Dirty worktree rules

Never revert changes you did not make unless explicitly asked.

Never use destructive commands such as git reset --hard or git checkout -- unless specifically requested or approved.

If unrelated files are dirty, ignore them.

If files you need to edit have unexpected changes, inspect carefully before touching them.

In multi-agent workflows, distinguish unrelated concurrent work from true conflicts.

6.4 Review mode

When Marcus asks for a review, Codex should default to a code-review mindset: findings first, ordered by severity, with file/line references where possible. Summaries and praise are secondary. If no findings are found, say that explicitly and mention residual risks or testing gaps.

Review response shape:
1. Findings, ordered by severity.
2. Open questions or assumptions.
3. Testing gaps / residual risk.
4. Optional change-summary only after findings.

Do not start with general praise.
Do not bury a serious bug under a narrative overview.

6.5 Frontend tasks

For greenfield frontend work, the OpenAI-style instruction pushes against generic AI slop: intentional typography, clear visual direction, meaningful motion, non-flat backgrounds, and a finished working state on desktop and mobile. For existing design systems like Anchor, preserve established patterns unless the task is explicitly a redesign.

Greenfield

Existing Product

Use bold, intentional visual language

Preserve the current design system

Avoid default stacks and generic purple/white layouts

Do not introduce visual chaos

Add purposeful motion

Respect accessibility and existing motion patterns

Finish the demo end to end

Avoid adjacent-feature sprawl

7. Preambles, Phase Metadata, and Long-Running Work

7.1 Preambles

Preambles are short user-facing progress notes sent while the model is working. OpenAI's Codex prompting guide says newer Codex models can provide more communicative mid-rollout updates. These are meant to orient the user, not create a noisy tool-call log.

Good Preamble

Bad Preamble

I found the likely source of the auth bug and am checking the callback route before patching.

Running rg. Running cat. Running sed. Now reading file.

The UI fix is in; I am running the smoke path now.

Still working.

The test failure is unrelated to this change; I am verifying the touched path separately.

Aha, good catch, now I will proceed.

7.2 Phase metadata

For newer Codex models, assistant output items may include phase metadata such as commentary or final_answer. OpenAI's deployment checklist says follow-up requests should preserve and resend phase on assistant messages, which helps the model distinguish progress updates from final answers and avoid early stopping.

Implementation risk

If you build your own Codex-like harness, do not flatten all assistant messages into plain text and drop phase metadata. That can make the model treat a progress update as the final answer, or degrade long-running behavior.

7.3 Friendly vs pragmatic personality

The supplied material describes Friendly and Pragmatic personalities as example harness-level prompts. Friendly is warmer, more collaborative, and better for onboarding or ambiguous work. Pragmatic is terse, direct, and better when the operator already knows the workflow and wants throughput.

Mode

Best For

Marcus Use

Friendly

Ambiguous tasks, onboarding, high-stakes explanation

When you want a pair-programmer feel or are emotionally activated

Pragmatic

Known workflows, fast iteration, build execution

Default for Anchor build tasks and CLI throughput

Hybrid

Serious work with concise orientation

Your likely best default: brief warmth, strong action

7.4 Metaprompting

The supplied OpenAI material recommends asking the model to analyze its own slow or poor behavior and propose targeted instruction changes. This is useful when a repeated failure appears: slow start, overly loggy preambles, excessive planning, missing tests, or tool misuse.

Targeted metaprompt:
That response was useful, but it took too long / was too loggy / missed verification.
Review the instructions that shaped your behavior.
Identify which instructions caused the failure mode.
Propose short, generalized instruction edits that would improve future runs without overfitting to this task.

8. Marcus Guide: How You Should Use Codex

8.1 Your role

You should treat yourself as the director/fCTO, not the line-by-line implementer. Codex owns tactical implementation inside the lane you define. You own product judgment, risk boundaries, prioritization, final acceptance, and whether the work matters.

Marcus Owns

Codex Owns

What problem matters

Repo investigation

Product taste and acceptance

Implementation

Safety and deployment approval

Tests, typecheck, smoke

Task boundaries

Repairing failures caused by edits

Final business/product decision

Clear technical summary

8.2 Your context architecture

Context Type

Where It Should Live

Example

Standing agent rules

~/.codex/AGENTS.md

No destructive commands; one concern per commit

Project rules

repo/AGENTS.md

Anchor safety rules, build commands, design system

Feature spec

Issue/build directive

Practice Mode module behavior

Long project memory

Docs/archive/Claude/ChatGPT

Why a decision was made

Current execution state

update_plan and final summary

What is done/blocked

Post-run receipt

handoff note/build ledger

Commit hash, tests, risks

8.3 When to use Codex vs other AI systems

Task

Best Tool Pattern

Repo-local implementation

Codex CLI

Large product specification

ChatGPT/Claude, then Codex for implementation

Architecture review / council

Multiple models, then synthesize

Visual/UI critique

Codex with screenshots plus ChatGPT/Claude for product eye

Long personal strategy/context

ChatGPT with memory/archive

Deployment debugging

Codex if it has shell access; otherwise Claude/ChatGPT for analysis

8.4 Your best default Codex workflow

Start with a narrow task: what to change, what not to change, and the verification expectation.

Let Codex inspect the repo and plan internally or through update_plan.

Make it implement in one concern, not several bundled features.

Require verification before final response.

Use /diff or git diff to inspect the result.

If good, commit with one concern per commit.

If shaky, ask for review or hand to another agent as council review.

8.5 Your stop gates

Production database migrations.

Live deploys unless explicitly requested for that task.

Billing, payment, subscription, or tax behavior.

Credential, secret, API key, OAuth, or SMTP changes.

Email sending or notification systems that contact real users.

Deleting user data or changing privacy/security boundaries.

Crisis/safety behavior in Anchor without explicit review.

Greek lens

Codex gives you energeia: force, motion, execution. Your job is sophrosyne and phronesis: right measure and practical judgment. The agent should move fast only inside the boundaries you actually chose.

9. Anchor-Specific Codex Setup

9.1 Anchor root AGENTS.md priorities

Anchor is a recovery-support app; trust and safety matter more than cleverness.

Do not weaken crisis, SOS, sobriety, relapse-risk, or recovery-profile behavior to satisfy tests.

Do not make 12-step the default assumption; support multiple recovery orientations.

Use non-shaming, non-moralizing, non-infantilizing language.

Preserve locked product copy unless explicitly asked to change it.

Preserve design system unless the task is explicitly a redesign.

9.2 Anchor directory rules

Directory

AGENTS.md Should Emphasize

app / src

Frontend components, routes, design tokens, accessibility, mobile-first behavior

server / api

Validation, logging, explicit errors, no silent fallbacks, auth/user boundaries

prompts / ai

JSON contracts, safety classifiers, no brittle parsing, crisis override rules

migrations

No production migration without explicit approval, local verification first

tests / e2e

Smoke paths, Playwright expectations, known flake notes

docs

Product decisions, locked copy, build handoffs

9.3 Anchor verification hierarchy

Run typecheck/build if available.

Run relevant unit/integration tests if present.

Run targeted route smoke for touched screens.

For UI changes, capture/inspect screenshots when possible.

For safety flows, test adversarial or edge-case input explicitly.

If verification cannot be completed, state exactly what was not verified and why.

9.4 Anchor danger patterns

Safety regression disguised as UX simplification: Example: hiding crisis resources too aggressively.

Schema drift: Frontend expects one shape while backend returns another.

Silent fallback: Agent catches errors and displays success-looking UI.

Program bias: Assuming all users want AA/12-step language or meeting links.

Morning/evening semantic mismatch: Check-in scoring that punishes users for not having completed a full day yet.

Visual redesign creep: A simple fix turns into a new visual system.

10. Multi-Agent Coordination Protocol

Your current workflow can involve multiple Codex, Claude, ChatGPT, and local agents. The single-agent dirty-worktree rule is not enough. You need explicit coordination rules.

10.1 File ownership

One agent should own a file at a time when edits are likely to overlap.

Parallel agents can inspect the same files, but not patch the same files without coordination.

If two agents need the same file, split work by sequence: Agent A patches, commits; Agent B rebases/reviews.

Use branches for major parallel workstreams.

10.2 Commit discipline

One concern per commit.

No bundled drive-by refactors.

No formatting sweeps mixed with behavior changes.

Commit messages should name the product outcome and risk surface.

Leave untracked unrelated files alone unless they belong to the task.

10.3 Handoff receipt

Codex handoff receipt:
- Task:
- Files changed:
- Behavior changed:
- Verification run:
- Verification result:
- Known risks:
- Not touched:
- Commit hash, if committed:
- Recommended next action:

10.4 Council review pattern

Primary agent implements the change.

Review agent receives the diff and task spec, not the full distracting thread.

Review agent reports findings first, ordered by severity.

Primary agent fixes validated findings.

Marcus accepts/rejects based on product judgment and verification.

11. Quick Reference

11.1 Session starter

You are working in this repo as a senior coding agent.
Read the relevant AGENTS.md instructions first.
Task: <specific task>
Scope: <what is in scope>
Out of scope: <what not to touch>
Verification: <tests/build/smoke expected>
Stop gates: do not deploy, run production migrations, send live email, or touch secrets unless explicitly asked.
Deliverable: working code plus concise summary of changes and verification.

11.2 Review prompt

Review the current working tree against this task:
<task/spec>

Use code-review mode:
- Findings first, ordered by severity.
- Include file/line references where possible.
- Focus on bugs, regressions, safety issues, missing tests, and behavior mismatches.
- If no findings, say so and list residual risks/testing gaps.
- Do not provide praise or a general summary before findings.

11.3 Bugfix prompt

Investigate and fix this bug end to end:
<bug description>

Rules:
- Reproduce or identify the failing path first.
- Find the root cause, not just the symptom.
- Make the smallest coherent fix.
- Add or update tests if a suitable test surface exists.
- Run verification.
- Do not touch unrelated files or refactor outside the fix.

11.4 Frontend implementation prompt

Implement this UI change:
<desired behavior and visual outcome>

Design constraints:
- Preserve the existing design system unless explicitly changing it.
- Mobile and desktop must both work.
- Avoid generic AI-slop layout decisions.
- Respect accessibility and reduced-motion preferences.

Verification:
- Run build/typecheck if available.
- Manually inspect or screenshot touched screens if possible.
- Report any visual uncertainty.

11.5 Safe deploy prompt

Prepare for deployment, but do not deploy until explicitly told.

Checklist:
- Confirm git status.
- Confirm build/typecheck/tests/smoke.
- List migrations, env var changes, secrets, or external service changes.
- Identify rollback path.
- Summarize risk.
- Stop and wait for explicit deploy instruction.

11.6 Command memory

Need

Codex CLI Pattern

Scaffold AGENTS.md

/init

Compact long context

/compact

Inspect changes

/diff

Ask for working tree review

/review

Mention a file

/mention path/to/file

Start fresh conversation

/new

Resume previous session

/resume

Fork current approach

/fork

Side analysis

/side <question>

List MCP tools

/mcp

12. Copy/Paste Templates

12.1 Global Marcus AGENTS.md

# AGENTS.md - Global Marcus Coding Agent OS

## Role
You are a senior AI-native coding agent working for Marcus. Marcus is the executive/product director. You own implementation quality, investigation, verification, and concise reporting.

## Operating Mode
Default to action. Gather context, plan when useful, implement, test, and report. Do not end with only a plan unless blocked.

## Safety Gates
Do not run destructive git commands, production migrations, live email sends, billing/payment changes, credential rotations, or data deletion unless Marcus explicitly requested that exact action in this turn.

## Multi-Agent Safety
Assume other agents may be active. Never revert changes you did not make. If unexpected changes overlap files you need to edit, stop and report the conflict. If unrelated, leave them alone.

## Commit Discipline
One concern per commit. Do not bundle unrelated refactors, formatting sweeps, and feature work.

## Verification
Prefer automated tests. If unavailable, run build/typecheck/lint. If unavailable, perform a targeted smoke test and state the limitation.

## Reporting
Be concise. Explain what changed, what was verified, what remains risky, and any next step Marcus should decide.

12.2 Anchor repo AGENTS.md

# AGENTS.md - Anchor

## Product Context
Anchor is a recovery-support app. Trust, safety, clarity, and stability matter more than cleverness.

## Safety Rules
Crisis, relapse-risk, sobriety, program selection, SOS, and recovery-profile flows require extra care. Do not weaken safety behavior to satisfy tests. Do not hardcode crisis content differently from locked product copy unless explicitly instructed.

## UX Rules
Avoid shame, moralizing, infantilizing language, and excessive 12-step assumptions. Support multiple recovery orientations.

## Database Rules
Do not run production migrations without explicit approval. Migrations must be reversible where practical and verified against expected schema.

## Design Rules
Preserve the existing design system unless the task is explicitly a redesign.

## Done Means
Code is implemented, relevant verification has run, known limitations are stated, and the final response names changed files and residual risk.

12.3 Migrations AGENTS.md

# AGENTS.md - Migrations

Do not create, modify, or run production migrations unless Marcus explicitly requested database work in this turn.

Before touching migrations:
1. Inspect existing schema and migration history.
2. Explain intended schema change.
3. Verify app code compatibility.
4. Run local/safe migration checks when available.
5. Stop before production execution unless explicitly authorized.

12.4 Preamble instructions

Preambles:
- Acknowledge then state the immediate plan before tool calls for non-trivial tasks.
- Keep updates to 1-2 sentences.
- Update every 1-3 major execution steps, not every tool call.
- Report outcome/impact, not low-level command logs.
- Avoid repetitive tics like 'Aha', 'Good catch', or 'Still working'.
- Do not treat a preamble as a final answer.

12.5 Metaprompting prompt

That response was useful, but it had this failure mode: <slow start / too loggy / missed tests / overplanned / touched too much>.

Review the instructions that shaped your behavior.
Identify the smallest generalized instruction changes that would prevent this next time.
Do not overfit to this exact task.
Return:
1. Likely instruction conflict or gap.
2. Proposed instruction edit.
3. Why it helps.
4. Any risk it introduces.

13. Source Links and Version Notes

Official sources consulted while creating this guide:

Codex Prompting Guide

Custom instructions with AGENTS.md

Codex CLI

Codex Best Practices

Compact a response - API Reference

Codex Advanced Configuration

Slash commands in Codex CLI

API Deployment Checklist

Agent Skills

Run long horizon tasks with Codex

OpenAI Prompt Guidance

Version note

This guide reflects the source material and official documentation available on May 12, 2026. Model names, API fields, CLI commands, and behavior can change. For production harness work, verify against current OpenAI docs before implementation.

Marcus conclusion

The practical takeaway: build a layered agent environment. Use AGENTS.md for stable rules, issue specs for current tasks, tools for safe execution, compaction for long context, council review for risk, and final handoffs for receipts. That is how the agentic workflow becomes a repeatable engineering system instead of a sequence of heroic prompts.
