---
title: "AUTONOMY LAYER.md Game MVP"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/#Studio OS/Game MVP Prompts/AUTONOMY_LAYER.md  Game MVP.docx"
status: reference
privacy: working
tags:
  - studio-os
---

# AUTONOMY LAYER.md Game MVP

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
AUTONOMY_LAYER

Reusable autonomous execution protocol. Embed in any build directive or reference with: "Apply AUTONOMY_LAYER.md to this directive." Version: 1.1

Changes in 1.1:

Added scope review step (section 0)

Added stack recommendation (section 0.1)

Acceptance criteria split into AUTOMATED vs HUMAN_REVIEW (section 1.5)

Fallback content specification rule (section 1.6)

Added GENERIC-11 (external service) and GENERIC-12 (DOM/canvas testing scope)

Strengthened scope discipline (section 1.7)

Complexity budget declaration required (section 0.2)

Markdown formatting standards (section 0.3)

Explicit deployment requirement (section 1.8)

Meta-prompt updated (section 7)

0. SCOPE REVIEW (apply BEFORE generating directive)

When using this layer to generate a new build directive, first evaluate the spec for autonomous executability.

0.1 Stack recommendation

Default to vanilla JavaScript + Vite + Canvas/DOM unless the project specifically requires:

Server-side state (use Node + serverless functions)

Type safety for a public API surface (then TypeScript is justified)

Component reuse across many views (then a UI framework is justified)

Avoid for autonomous builds unless required:

TypeScript (adds type-error failure category that hurts agent execution)

React/Vue/Svelte (adds rendering complexity unnecessarily)

Heavy game engines (Phaser, Pixi) for projects under ~5000 lines

Asset pipelines (image, font, sprite)

The agent's mental model stays flatter with simpler substrates. Smart substrates eat your debugging time.

0.2 Complexity budget declaration

Every directive must declare at the top:

Complexity budget: ~N lines, ~M phases, target X-Y hours agent time

If the spec exceeds the budget, trim scope before generating the directive. Common trims:

Defer optional integrations to post-v0 phase

Reduce phase count by combining related work

Cut polish phases if core loop is at risk

Move "nice to have" features to deferred-issues.md upfront

0.3 Markdown formatting standards

Code blocks for: file paths, command examples, code snippets, inline data structures

Lists for: enumerable items, sequential steps, file structures

Prose for: explanations, decisions, rationale

Tables for: structured comparisons (stats, phases, criteria)

Do not mix block types in one section without reason

1. AUTONOMY DOCTRINE

Three response tiers, applied in order.

TIER 1 — SELF-HEAL Apply the relevant entry from the Self-Repair Playbook. Two attempts maximum. If self-heal succeeds, continue.

TIER 2 — DEFER AND CONTINUE If self-heal fails after two attempts:

Log to docs/deferred-issues.md per the format in this file

Stub or skip the failing element so the rest of the system works

Mark related tests with it.skip("DEFERRED: [reason]")

Commit current state with deferred summary in the commit message

Continue with the next item

TIER 3 — HARD STOP Only halt for the conditions in HARD STOP CONDITIONS. Before halting:

Commit all in-progress work to a halt-[timestamp] branch

Generate BUILD_REPORT.md with current state and diagnosis

Stop and surface

NEVER:

Ask for human input mid-build

Wait between phases

Stop for "I'm not sure" — defer it and move on

Commit broken code without marking it deferred

Skip generating deferred-issues.md or BUILD_REPORT.md

Expand a phase's scope mid-build (defer expansion to a future phase)

1.5 ACCEPTANCE CRITERIA SPLIT (required in every directive)

Every directive must split acceptance criteria into two categories:

AUTOMATED: can be verified by smoke tests, build success, or programmatic assertion. These block phase gates.

HUMAN_REVIEW: require browser playtest, visual inspection, or "feel" judgment. These do NOT block phase gates. Agent logs them in deferred-issues.md as MANUAL_PLAYTEST_REQUIRED.

The agent cannot verify "feels like a real game" or "the village reads as coherent." These are human checks. Be honest about which is which.

1.6 FALLBACK CONTENT MUST BE SPECIFIED

If a directive specifies a "fallback path" (deterministic fallback dialogue if AI fails, default error messages, offline mode behavior), the actual fallback content or behavior must be specified inline in the directive. The agent should not be asked to invent fallback content.

If the fallback is non-trivial (dialogue trees, error messages, default behaviors), spec the actual content as data the agent can copy.

1.7 SCOPE DISCIPLINE (strict)

If implementation grows beyond a phase's stated goal:

Halt the expansion

Defer the additional work to a future phase or deferred-issues.md

Continue with the current phase as originally scoped

Scope creep is a deferrable issue, not a license to expand mid-build. Most failed autonomous builds fail because the agent kept "improving" things mid-phase and accumulated bugs.

If you find yourself adding features not in the phase plan, you are out of scope. Stop, defer, continue.

1.8 DEPLOYMENT REQUIREMENT

Every directive must explicitly handle deployment:

If deployment is in scope: include the deploy command and verification step in the final phase

If deployment is not in scope: state explicitly "no deployment in scope, agent commits and stops"

Ambiguity here means the agent will either skip deployment or invent a deployment process. Both are wrong.

2. SELF-REPAIR PLAYBOOK

Generic entries apply to all projects. Add stack-specific entries in each directive.

GENERIC-1 — A specific test fails ATTEMPT 1: Re-read implementation and assertion. Identify obvious bug. Fix. ATTEMPT 2: Check if assertion is wrong vs implementation. If implementation matches design intent, update assertion. DEFER: it.skip("DEFERRED: [reason]"). Log to deferred-issues.md. Continue.

GENERIC-2 — A feature's behavior is wrong but system runs ATTEMPT 1: Re-read spec for that feature. Trace implementation. Fix. ATTEMPT 2: Simplify to a known-working baseline behavior. DEFER: Mark as "stub behavior, advanced features deferred". Log. Continue.

GENERIC-3 — Module not found / import error ATTEMPT 1: Verify file path matches import exactly (case-sensitive). Check export name. ATTEMPT 2: Check if file exists. Create stub if missing. DEFER: Stub the import with a dummy export that returns safe defaults. Log. Continue.

GENERIC-4 — DOM element missing or query returns null ATTEMPT 1: Check HTML for expected element ID. Add if missing. ATTEMPT 2: Wrap in optional chaining and skip wiring for that element. DEFER: Log feature as "wiring incomplete". Continue.

GENERIC-5 — Render layer broken (blank canvas or screen) ATTEMPT 1: Check render order. Verify ctx/state saves and restores. Verify state shape matches render expectations. ATTEMPT 2: Add temporary console.log to identify failing function. Fix or stub. DEFER: Render the most basic untextured version. Log all polish features as deferred.

GENERIC-6 — External resource (CDN, URL, asset) fails ATTEMPT 1: Try alternative URL or mirror. ATTEMPT 2: Skip this resource, try next alternative in candidate list. DEFER: Disable the feature that depends on this resource. Log.

GENERIC-7 — File cannot be created ATTEMPT 1: Verify working directory. Check path correctness. ATTEMPT 2: Use absolute path or alternative location. DEFER: HARD STOP if file is critical. Otherwise log and continue.

GENERIC-8 — Test setup throws (not assertion failure) ATTEMPT 1: Check imports in test file. Verify modules exist. ATTEMPT 2: Rewrite test setup with simpler initialization. DEFER: it.skip() with DEFERRED comment. Log root cause.

GENERIC-9 — Build command fails ATTEMPT 1: Identify offending file from error output. Check most recent changes for syntax errors. ATTEMPT 2: Git diff the most recent commit. Revert suspicious chunks one at a time. DEFER: HARD STOP. Build must work.

GENERIC-10 — Dependency install fails ATTEMPT 1: Remove node_modules and lockfile, reinstall clean. ATTEMPT 2: Install with --legacy-peer-deps flag or equivalent. DEFER: HARD STOP. Cannot run anything.

GENERIC-11 — External service / API fails (NEW in v1.1) Symptoms: API returns error, key missing, JSON malformed, timeout, rate limit. ATTEMPT 1: Verify credentials, request format, response parsing. Add JSON validation. ATTEMPT 2: Implement deterministic local fallback. Make external service optional. DEFER: Disable external service entirely. Game/app must work without it. Log as MEDIUM.

This entry is critical for any directive that integrates with external services (LLMs, payment APIs, third-party data sources). The pattern: external service is augmentation, not foundation. The system must work without it.

GENERIC-12 — Tests fail because DOM/Canvas environment unavailable (NEW in v1.1) Symptoms: Vitest can't handle document, window, canvas, or browser APIs. ATTEMPT 1: Scope the test to pure logic only. Move DOM-dependent assertions to manual smoke. ATTEMPT 2: Configure jsdom or happy-dom test environment if simple, otherwise skip. DEFER: Pure logic tests stay automated. UI/render tests become MANUAL_PLAYTEST_REQUIRED. Log.

This entry exists because Vitest does not handle DOM/canvas natively. Trying to test rendering in unit tests almost always fails. Scope unit tests to pure logic from the start.

[STACK-SPECIFIC entries go here in the full directive]

3. PHASE EXECUTION PROTOCOL

Apply this structure to every phase.

PRE-FLIGHT (5 minute budget)

Run git status. Working tree must be clean. If dirty: stash with message phase-X-preflight-stash and investigate.

Verify previous phase commit exists in git log.

Run full test suite. Record baseline: passing / skipped / failing counts.

Verify required files from previous phase exist.

Verify build command succeeds.

If pre-flight finds gaps: apply Self-Repair Playbook. Log unrepaired gaps. Proceed with what does exist.

EXECUTION

Write smoke assertions first. Run them and expect red.

Implement until smoke is green.

For each failing test: apply GENERIC-1 (max 2 attempts), then defer.

For each failing feature: apply GENERIC-2 (max 2 attempts), then stub and defer.

Checkpoint commits: commit after every successful sub-step that leaves the system in a working state:

chore(phase-X-checkpoint): [what just completed]

HEALTH CHECK

After all implementation steps:

Run full test suite. Count passing / skipped (deferred) / failing.

Verify all expected files from this phase exist.

Run build command. Verify success.

Log any "manual verification required" items to deferred-issues.md as MANUAL_PLAYTEST_REQUIRED.

COMMIT

Always commit at phase end, even with deferrals:

feat(phase-X): [phase name]

[body describing what shipped]

Deferrals: N items (see docs/deferred-issues.md)

Tests: P passing, S skipped (deferred), F failing

Decisions:

- [unspecified choice and why]

REPORT UPDATE

Append a phase section to docs/deferred-issues.md listing all deferrals.

TRANSITION

After commit and report update, immediately begin the next phase. No pause.

4. DEFERRED-ISSUES.MD FORMAT

Create on first deferral. Update throughout build. Never delete entries; use RESOLVED tag if fixed later.

# Deferred Issues — [Project Name] Build

Generated during autonomous build. Human review required.

## Severity Legend

- BLOCKER: cannot ship without this

- HIGH: major feature broken or missing

- MEDIUM: minor feature degraded

- LOW: cosmetic or polish issue

- MANUAL_PLAYTEST_REQUIRED: needs human verification

---

## Phase X: [Phase Name]

### [SEVERITY] [Short title]

**What failed:** [description]

**Attempts:**

1. [what was tried and what happened]

2. [what was tried and what happened]

**Current state:** [how it was stubbed, skipped, or partially shipped]

**Reproduction:** [how to reproduce]

**Recommended fix:** [what a human should do]

**Continued with:** [what shipped instead]

5. BUILD_REPORT.MD FORMAT

Generate at project root at end of final phase, or before any hard stop.

# [Project Name] — Build Report

Generated: [timestamp]

Branch: [branch name]

Final commit: [SHA]

Production URL: [URL or "DEPLOY FAILED — see deferred-issues.md" or "NO DEPLOY IN SCOPE"]

---

## Summary

[One paragraph: what shipped, what deferred, overall health]

## Phase Outcomes

| Phase | Status | Tests Passing | Deferrals | Commit SHA |

|---|---|---|---|---|

| A — [name] | COMPLETE / PARTIAL / FAILED / DEFERRED | N | N | [SHA] |

## Deferred Issues by Severity

- BLOCKER: count — titles

- HIGH: count — titles

- MEDIUM: count — titles

- LOW: count — titles

- MANUAL_PLAYTEST_REQUIRED: count — titles

Full details in `docs/deferred-issues.md`.

## Test Status

| Metric | Count |

|---|---|

| Total tests | N |

| Passing | N |

| Skipped / Deferred | N |

| Failing | N |

## Manual Verification Required

[List items flagged as MANUAL_PLAYTEST_REQUIRED in deferred-issues.md]

## Recommended Next Actions

1. [highest priority deferred item]

2. [next]

3. [next]

## Notes for Human Review

[Edge cases, judgment calls, design questions worth flagging]

6. HARD STOP CONDITIONS

Halt ONLY for these. All other failures use Tier 1-2.

Dependency install fails after GENERIC-10 attempts

Build fails after GENERIC-9 attempts

Test runner crashes (runner itself fails to start)

Git operations fail after credential verification

Filesystem errors (disk full, permission denied)

Elapsed time exceeds N hours (specified per directive, default 8)

Before any hard stop:

git add -A

git commit -m "halt(phase-X): [reason with full diagnosis]"

git checkout -b halt-[YYYY-MM-DD-HHMM]

git push origin halt-[branch-name]

Then generate BUILD_REPORT.md with HALTED status. Stop.

7. META-PROMPT (use this when asking Charlie to generate a directive)

Send this prompt to Charlie/Claude after generating any spec:

Take the spec or directive above and turn it into a fully autonomous build directive using AUTONOMY_LAYER.md v1.1.

Apply these rules:

1. Run scope review first (section 0). If scope exceeds reasonable autonomous execution, trim and document trims at top of directive.

2. Default to vanilla JavaScript unless type safety or framework features are required.

3. Declare complexity budget at top.

4. Split acceptance criteria into AUTOMATED and HUMAN_REVIEW.

5. Specify all fallback content inline (do not delegate to agent invention).

6. Include explicit deployment step (or state "no deploy in scope").

7. Customize self-repair playbook for the project's stack (10+ entries).

8. Make optional integrations fully deferrable (game/app must work without them).

9. Mark "feel" and visual criteria as HUMAN_REVIEW, not AUTOMATED.

Generate the full directive including:

- Role statement

- Autonomy doctrine (self-heal → defer → halt)

- Stack and dependency rules

- Game/project design data from spec

- File structure

- Phase plan with smoke-first per phase

- Self-repair playbook (stack-specific)

- Phase execution protocol

- deferred-issues.md format

- BUILD_REPORT.md format

- Hard stop conditions

- GO instruction

Voice: direct, imperative, addressed to executing agent. No preamble. Every instruction actionable.

Apply the AUTONOMY_LAYER below to structure execution layer:

[PASTE AUTONOMY_LAYER.md CONTENTS]

8. HOW TO USE THIS FILE

Generating a new directive (with Charlie): send the meta-prompt from section 7 with the spec.

Embedding in CC/Codex: place this file in project root. Add to top of directive: "Apply AUTONOMY_LAYER.md before executing this directive."

Self-contained directive: paste contents of sections 1-6 directly into the directive where execution layer is defined.

Per-project customization: add stack-specific self-repair entries after GENERIC-12. Each new project type benefits from 5-10 stack-specific entries (e.g., Python migrations, Docker builds, database connection failures).

End of AUTONOMY_LAYER.md v1.1
