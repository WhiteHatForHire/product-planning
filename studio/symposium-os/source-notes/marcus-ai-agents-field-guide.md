---
title: "marcus ai agents field guide"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/#Studio OS/Guides and references /marcus_ai_agents_field_guide.docx"
status: active
privacy: working
tags:
  - studio-os
---

# marcus ai agents field guide

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Marcus AI Agents Field Guide

Memory, compaction, traces, evals, Codex handoffs, and the Director Model

Version 1.0 - May 2026

Core thesis

An agent is not just a smart model. It is a model embedded in a harness: instructions, tools, state, sandbox, memory, validation, observability, and reviewable artifacts. Your job is not to worship the agent. Your job is to direct the harness.

Source note

This guide is based on the Agents SDK, Codex, memory/compaction, tracing, eval, and local-control-plane material you pasted into ChatGPT, plus your current agentic build workflow. Verify exact API names and package behavior against current official docs before implementation.

How to use this guide

During active builds: use the quick-reference checklists, AGENTS.md rules, and handoff templates.

During architecture reviews: use the memory/compaction/artifact distinctions and the trace-feedback-eval loop.

When tempted by infrastructure: check the control-plane and "park vs build" sections before spending a day wiring tooling.

For product strategy: map agent reliability primitives to Anchor, Pattern Intimacy, The Cave, and AI ops audits.

Static table of contents

1. The useful definition of an AI agent

2. The four things you must never confuse

3. Memory vs. compaction

4. The Marcus agentic build loop

5. AGENTS.md as repo constitution

6. Traces, feedback, evals, and Codex handoffs

7. Sandboxes, manifests, and file-based workspaces

8. The local control-plane app: relevant but parked

9. Project-specific applications

10. Agent OS documents

11. Quick-reference checklists

12. Traps, ethics, and 30/60/90-day priorities

1. The useful definition of an AI agent

For your purposes, an AI agent is not merely a chatbot, not merely an API call, and not merely a model with tools. An agent is a repeatable work loop built around a model.

Working definition

Agent = model + instructions + tools + state + environment + validation + observability + artifacts + feedback loop.

This matters because most agent failures are not model failures. They are harness failures: unclear instructions, missing source-of-truth rules, bad tool contracts, no validation, no artifact schema, weak evals, or unreviewed memory.

The term "harness" is useful. The harness is the full operating contract around the model: instructions, tools, routing, output requirements, validation checks, observability, and review gates. When the harness improves, the agent becomes more reliable even if the model stays the same.

When an agent is worth building

Use an agent when...

Do not use an agent when...

The workflow repeats and has recognizable phases.

You only need a one-off answer or draft.

The agent must inspect files, call tools, write artifacts, or preserve state.

The model can answer from a single prompt with no tools.

There are clear validation checks or human review gates.

You cannot tell what good output means.

The workflow benefits from traces, feedback, and evals over time.

You are mainly chasing novelty or tool hype.

There is a source-of-truth artifact at the end.

The output is ephemeral chat with no downstream consequence.

The director stance

Your strongest stance is not "I am the coder doing every step." It is also not "the agent will figure it out." The correct stance is director/fCTO: define the contract, delegate execution, inspect receipts, approve merges, and preserve judgment.

You direct Telos: what the work is for.

You enforce Phronesis: which tradeoffs matter in context.

You protect Sophrosyne: right measure, no infrastructure binge.

You require Aletheia: evidence, traces, artifacts, and honest uncertainty.

You convert Techne into Praxis: tools become shipped work, not just impressive machinery.

2. The four things you must never confuse

The material you pasted is valuable because it separates four layers that people often blur together. Keep these clean and many agent-design mistakes disappear.

Layer

Purpose

What belongs there

What does not belong there

Context

What the current run can see right now.

Current prompt, files, tool results, active conversation state.

Long-term truth, legal record, medical conclusions, final decisions.

Compaction

Let one long run continue despite finite context.

Working state, current batch, open questions, artifact paths, unresolved concerns.

Permanent memory, case facts as final truth, private conclusions no human reviewed.

Memory

Help future runs start smarter.

Reusable workflow lessons, stable preferences, process rules, style and review habits.

Investigation conclusions, crisis facts, medical facts, unreviewed claims.

Artifact

Reviewed source of truth.

Memo, spec, PR, eval file, build ledger, safety decision, user-facing output.

Uninspected model recollection or hidden trace-only facts.

Doctrine

Memory helps the next run work better. It is not the record. The artifact is the record.

3. Memory vs. compaction

Compaction

Compaction is for one long-running run. It compresses the active working state so the agent can continue without carrying every prior token. It is a continuity device, not a truth database.

Use it at meaningful phase boundaries: after Batch 1, before Batch 2; after issue triage, before implementation; after design review, before merge prep.

Tell the compactor what must survive: current goal, files touched, decisions made, unresolved questions, failed attempts, artifact paths, and safety concerns.

Do not compact after every turn. That adds cost and can turn state into mush.

Memory

Memory is for future runs. It should capture reusable lessons and preferences, not case-specific facts that belong in a reviewed artifact.

Good memory candidate

Bad memory candidate

"Use the manifest first before reading files."

"Northwind Logistics violated policy."

"Preserve uncertainty instead of guessing."

"User relapsed on X date."

"Anchor copy should avoid default 12-step assumptions."

"This client has legal exposure of $3.2M" unless in a reviewed file.

"Marcus prefers atomic commits and production smoke before done."

"The app is safe" if no test gate proved it.

"For recovery apps, crisis copy must be direct but non-alarming."

"This medical conclusion is true."

Memory policy for Marcus products

Anchor: memory may store recovery orientation, support style, preferences, and repeated patterns, but crisis or medical facts need careful consent, visibility, and user control.

Pattern Intimacy: memory can index themes and workflow preferences, but journal entries and dated documents remain the source of truth.

AI ops audits: memory can store process lessons about how audits are conducted, but client-specific conclusions belong in audit artifacts.

The Cave / games: memory can store player preferences or design lessons, but game state should live in deterministic state files or database records.

4. The Marcus agentic build loop

The most valuable part of the pasted material is not a particular API. It is the loop. You have been building toward this already. The formal version is below.

Define the product goal. What is the Telos? What human problem does this solve?

Write the behavior contract. What should the agent do, refuse, preserve, cite, write, or escalate?

Write or update AGENTS.md. Repo constitution: commands, conventions, done criteria, safety gates.

Create a scoped build directive. One concern, clear acceptance criteria, automated vs human review split.

Run the agentic implementation. Codex, Claude Code, or another coding agent executes within the contract.

Collect receipts. Diffs, logs, tests, screenshots, smoke results, errors, traces.

Human/product review. You inspect for taste, safety, product fit, and actual user experience.

Turn feedback into evals. Do not leave hard-won lessons as vibes. Preserve them as tests or rules.

Create a handoff. Specific fixes, evidence, validation steps, and stop gates.

Merge and deploy only after gates pass. Done means production-confirmed where relevant, not merely code-written.

Your current edge

You are not merely "vibe coding." You are building a director-led, evidence-preserving, multi-agent delivery system. The value is in the operating loop, not just the prompts.

5. AGENTS.md as repo constitution

AGENTS.md should be treated as a constitution, not a scratchpad. It tells coding agents how to behave before they touch the repo. It should be durable, specific, and enforceable.

What belongs in AGENTS.md

Project purpose and current phase.

Build, test, lint, typecheck, smoke, and deploy commands.

Repo conventions and architecture boundaries.

Branching and commit rules: one concern per commit, no bundled changes.

Definition of done: tests, smoke, production check, screenshots, or manual review as applicable.

Security and privacy rules: no secrets in prompts, no leaking user data, no unsafe autonomy.

Escalation gates: when to stop and ask, when to continue autonomously, when to log uncertainty.

Known pitfalls and parked items.

What does not belong in AGENTS.md

Long one-off tasks that belong in a build directive.

Secrets, API keys, database passwords, or client-sensitive data.

Vague preferences like "make it better" without acceptance criteria.

Outdated instructions from previous architectures.

Conflicting commands from old stack decisions.

Marcus AGENTS.md skeleton

# Project operating rules

Purpose: <one paragraph>

Current phase: <MVP / redesign / safety hardening / production maintenance>

## Commands

- Install: <command>

- Dev: <command>

- Test: <command>

- Typecheck/lint: <command>

- Smoke: <command>

## Work rules

- One concern per commit.

- Do not bundle unrelated fixes.

- Preserve existing behavior unless the directive explicitly changes it.

- Do not claim done without running the listed gates.

## Review gates

- Automated gates: <tests/smoke/typecheck>.

- Human review gates: <visual/taste/safety/product judgment>.

## Safety and data

- No secrets in committed files.

- No sensitive user data in prompts or logs unless explicitly required and approved.

- Crisis/safety flows must remain conservative and testable.

6. Traces, feedback, evals, and Codex handoffs

This is the agent improvement flywheel. It converts experience into system improvement. Without it, every fix stays trapped in chat history.

Signal

What it captures

What to do with it

Trace

What actually happened: model calls, tool calls, errors, spans, timings, outputs.

Use it for diagnosis and evidence. Do not rely on memory of the run.

Human feedback

What mattered to the reviewer or user.

Convert recurring feedback into evals or repo rules.

LLM/model critique

Second-pass observations, contradiction spotting, coverage gaps.

Useful, but subordinate to human judgment and source evidence.

Eval

Reusable expectation that can be rerun.

Promote hard-won lessons into gates.

Handoff

Implementation-ready summary for Codex/Claude.

Include evidence, ranked fixes, acceptance criteria, and validation steps.

How to turn feedback into evals

A good eval is not "be better." It is a durable expectation that would catch a real regression.

Weak feedback

Better eval-shaped rule

"The answer was too confident."

When evidence is incomplete, output must include an explicit open-question section and must not state unsupported conclusions.

"The flow felt too 12-step-heavy."

If user recovery orientation is non-12-step, crisis/help copy must not default to sponsor/meeting-only language.

"The UI looked cramped."

Mobile viewport smoke must verify no bottom-nav label clipping at 390px width.

"The agent ignored the source file."

Every material claim must cite one of the files in the manifest or be marked unsupported.

"The fix broke another page."

Smoke test must cover all eight primary routes before merge.

Codex handoff structure

Executive summary: what changed, what failed, what needs to happen next.

Top 3 fixes: ranked by impact and confidence.

Evidence: trace IDs, screenshots, test logs, user feedback, failing files.

Implementation instructions: exact files or areas to inspect when known.

Automated acceptance criteria: tests, typecheck, smoke, validators.

Human review criteria: UX feel, safety copy, product judgment, visual review.

Stop gates: when the agent must stop instead of improvising.

7. Sandboxes, manifests, and file-based workspaces

The sandbox material is important because it moves the agent away from giant prompts and toward controlled workspaces. This is how agentic work becomes auditable.

The workspace pattern

Manifest first: the agent reads a compact index of available files before diving into content.

Source files stay as files: large documents, logs, specs, and datasets should be mounted or staged, not pasted into prompts.

Outputs go in outputs/: memos, reports, JSON, screenshots, and validation files should be written to a known place.

Validation tools live nearby: scripts that check output contract, citations, schema, screenshots, or safety rules.

The final artifact is human-reviewable: the agent should leave behind something you can inspect, commit, archive, or hand off.

Manifest best practices

Practice

Why it matters

Use stable document IDs.

Makes citations and audit trails durable.

Avoid absolute paths and parent-directory escapes.

Improves portability and sandbox safety.

Keep secrets out of manifests.

Runtime config should inject secrets, not prompt text.

Group evidence by batch or domain.

Helps agents process evolving records without flattening time.

Put task instructions in README.md, task.md, or AGENTS.md.

Keeps prompts smaller and workspace behavior clearer.

Keep outputs under a known directory.

Makes downstream validation and artifact collection simple.

8. The local control-plane app: relevant but parked

The local control-plane app is a mini command center for running and observing Agents SDK demo projects. It can import projects, inspect entrypoints and environment variables, create local deployment records, start/stop Docker containers, collect logs, and store traces locally.

Why it is relevant

It points toward the future AI-native studio stack: local observability, deployment records, run logs, app events, and trace inspection.

It could help when you run multiple agent demos or sandboxed local apps and need a control tower.

It reinforces the principle that agents need observability, not just prompts.

Why not now

It requires uv, npm, Docker, Flask/Vite, local ports, Docker socket access, and app contracts. That is real infrastructure surface area.

Docker socket mounting is powerful but not casual. It lets the manager create containers through Docker and should be treated as a security boundary.

For Anchor, this is probably not the next bottleneck. Your next bottleneck is product/safety/UX plus deploy reliability, not a generalized Agents SDK control plane.

This could easily become a Techne trap: a beautiful command center before the city needs it.

Decision rule

Build or install a control plane only when you have at least two or three agent apps whose runs, traces, deployments, and logs you actually need to compare. Until then, use simpler logs, smoke reports, and handoff artifacts.

9. Project-specific applications

Anchor

Anchor is the highest-stakes application because recovery, crisis support, memory, and personalization can help people but also create risk.

Use memory for recovery orientation, preferred support style, stable preferences, and repeated patterns the user can inspect or edit.

Do not let memory become a hidden crisis or medical record. Sensitive facts need transparency, user control, and careful retention choices.

Use evals for crisis idioms, non-12-step paths, safety copy, meeting-link gating, and high-risk support flows.

Artifacts matter: check-ins, safety decisions, SOS copy, and reflection summaries should be reviewable rather than lost inside chat memory.

Trace safety-critical flows during testing, but avoid storing unnecessary sensitive payloads.

Pattern Intimacy

The corpus is the source material. The AI is a librarian and synthesizer, not the source of truth.

Memory can store your writing preferences, recurring themes, and workflow rules, but dated entries remain the record.

Compaction is useful inside long live-journal days so the thread keeps continuity without flattening the day.

Future products could use queryable life-corpus architecture, but privacy and consent must be first-class design principles.

The Cave / AI-native worlds

Use deterministic state machines for progression. The model narrates; the rules govern.

Game state should live in explicit state files or a database, not hidden memory.

Traces can help debug why the narrator ignored constraints or why a transition fired incorrectly.

Evals can test that required world-state conditions block or allow progression.

Eagle Rocket / AI ops audits

The compliance and diligence examples map well to client audits: inspect files, preserve uncertainty, cite evidence, write memos, generate open questions.

Client-specific conclusions belong in audit artifacts, not generalized memory.

A manifest-first workflow could become part of a paid AI Operations Audit deliverable.

Evals can preserve client promises: no unsupported claims, no autonomous outbound communication, no sensitive-data leakage.

Symposium Studios / AI-native build studio

The studio IP is the operating method: specs, agents, traces, evals, handoffs, design taste, and final judgment.

The first tactical hire may eventually be a deployment closer, but the operating system should make that handoff easy.

Build receipts are assets: logs, case studies, production smoke results, before/after diffs, and build ledgers.

10. Agent OS documents

A serious agentic workflow should have a small set of recurring documents. These are not bureaucracy. They are how you keep agent work from becoming amnesia.

Document

Purpose

When to update

AGENTS.md

Durable repo constitution and agent rules.

When commands, architecture, or done criteria change.

BUILD_DIRECTIVE.md

Scoped autonomous task instructions.

Every meaningful build block.

ACCEPTANCE_CRITERIA.md

Automated and human review gates.

Before implementation starts.

EVALS.md or tests/

Durable expectations from feedback.

After user tests, failures, or model critiques.

HANDOFF.md

Next-agent or next-session continuity.

At migration points or after partial completion.

LEARNINGS.md

Human-reviewed process lessons.

After postmortems, not every small issue.

BUILD_LEDGER.md

What shipped, what failed, time/cost, receipts.

End of major build sessions.

11. Quick-reference checklists

Agent design checklist

What repeated workflow is this agent responsible for?

What tools can it use, and what tools are forbidden?

What is the source of truth?

What must be written as an artifact?

What should be remembered for future runs?

What must never be remembered without review or consent?

What validation gate catches wrong output?

What does the agent do when evidence is missing?

What logs, traces, or receipts are needed?

Where does human judgment enter the loop?

Memory checklist

Is this a reusable process lesson or a case-specific fact?

Would the user expect this to be remembered later?

Is it sensitive? If yes, is there explicit consent and visibility?

Can the user inspect, edit, or delete it?

Would storing this create a hidden shadow record?

Should this instead be written into a reviewed artifact?

Compaction checkpoint checklist

Current goal and phase.

Files read or modified.

Decisions made.

Assumptions that changed or were superseded.

Open questions.

Known failures and failed attempts.

Artifact paths.

Next action and stop gate.

Eval checklist

Does the eval catch a real failure that matters?

Is it durable beyond one prompt?

Does it distinguish deterministic checks from human-review criteria?

Does it avoid rewarding superficial keyword stuffing?

Does it cite the feedback or trace that motivated it?

Can it run cheaply enough to be part of the build loop?

Codex handoff checklist

State the problem in one paragraph.

List exact files/routes/components if known.

Include evidence: logs, screenshots, traces, failing tests, user feedback.

Separate automated gates from human-review gates.

Specify no-go behavior and stop gates.

Require one concern per commit.

Require final status with commit hash, tests run, failures, and unresolved risks.

12. Traps, ethics, and priorities

Common traps

Trap

Distorted form

Corrective principle

Tool lust

Installing every new agent framework because it is impressive.

Use tools only when they reduce real bottlenecks.

Infrastructure hubris

Building a control plane before having agent apps that need it.

Let need pull infrastructure into existence.

Context addiction

Assuming more context always means better work.

Use manifests, compaction, and artifacts to structure context.

Shadow memory

Letting memory become an unreviewed fact database.

Memory stores workflow lessons; artifacts store facts.

Eval theater

Creating tests that look rigorous but do not catch actual failures.

Base evals on real failures and human feedback.

Automation overreach

Removing human judgment before the loop is trustworthy.

Increase autonomy only after gates prove stable.

Agent yes-man loop

Using model critique as validation without evidence.

Require traces, citations, artifacts, and human review.

Greek ethics lens

Concept

Healthy expression in agent work

Distorted expression

Techne

Skillful use of tools to ship real systems.

Tool worship and endless tinkering.

Phronesis

Choosing the right level of automation for the situation.

Treating all workflows as equally automatable.

Sophrosyne

Right measure: build only the infrastructure the phase needs.

Overbuilding, overfitting, or buying tools as stimulation.

Aletheia

Truth through traces, citations, evals, and artifacts.

Confident summaries without evidence.

Telos

Every agent serves a clear human/product end.

Building agents because agents are fashionable.

Praxis

Learning becomes repeated action and shipped work.

Insight without execution.

Hubris

Believing autonomy removes the need for judgment.

Letting agents self-validate high-stakes work.

30 / 60 / 90-day priorities

Timeframe

Focus

What to do

Now

Use what directly improves the build loop.

Tighten AGENTS.md, build directives, acceptance criteria, handoffs, smoke gates, and artifact discipline.

Next 30 days

Formalize feedback into evals.

For Anchor and The Cave, turn real bugs/user feedback into durable regression checks.

Next 60 days

Build repeatable workspace patterns.

Use manifest-first file workflows for audits, corpus analysis, and product reviews.

Next 90 days

Consider observability/control-plane needs.

Only explore local control-plane or HALO-style automation if multiple active agent apps need shared trace/deployment visibility.

Final operating doctrine

Remember this

The agent is not the sovereign. The model is not the record. Memory is not truth. The artifact is the record, evals preserve lessons, traces preserve behavior, and you remain the director responsible for judgment.

The best version of this work is not a pile of clever demos. It is a disciplined AI-native studio method: define the game, constrain the agent, preserve receipts, learn from traces, ship artifacts, and let each loop make the next loop smarter.
