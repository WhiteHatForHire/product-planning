---
title: "Autonomous Build Meta Prompt Game MVP"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/#Studio OS/Game MVP Prompts/Autonomous Build Meta Prompt Game MVP.docx"
status: active
privacy: working
tags:
  - studio-os
---

# Autonomous Build Meta Prompt Game MVP

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
META_PROMPT v1.1

Send this to Charlie/Claude after generating any spec. Pairs with AUTONOMY_LAYER.md v1.1.

Take the spec or directive above and turn it into a fully autonomous build directive using AUTONOMY_LAYER.md v1.1.

Apply these rules:

1. Run scope review first. If scope exceeds reasonable autonomous execution, trim and document trims at top of directive.

2. Default to vanilla JavaScript unless type safety or framework features are specifically required.

3. Declare estimated complexity budget at top of directive (~N lines, ~M phases).

4. Split acceptance criteria into AUTOMATED (block phase gates) and HUMAN_REVIEW (logged as MANUAL_PLAYTEST_REQUIRED).

5. Specify all fallback content inline. Do not ask the agent to invent dialogue trees, error messages, default behaviors, or fallback flows. Spec the actual content.

6. Include explicit deployment step in final phase, or state "no deploy in scope, agent commits and stops."

7. Mark "feel" and visual criteria as HUMAN_REVIEW, not AUTOMATED. The agent cannot verify "feels coherent" or "feels alive."

8. Make optional integrations (LLMs, third-party APIs, payment) fully deferrable. The system must work without them.

9. Customize self-repair playbook for the project's stack with at least 10 failure modes.

Generate the full directive including:

1. Role statement

2. Autonomy doctrine (self-heal → defer → halt hierarchy)

3. Stack and dependency rules

4. Full project design data from spec

5. File structure

6. Phase plan with per-phase smoke-first assertions, implementation steps, health checks, commit format

7. Self-repair playbook (stack-specific, 10+ entries with explicit fix steps)

8. Phase execution protocol (preflight, execute, health check, commit, deferred update)

9. deferred-issues.md format

10. BUILD_REPORT.md format

11. Hard stop conditions (only: broken build, broken test runner, broken git, filesystem failure)

12. GO instruction

Hard stops require: commit everything to halt-[timestamp] branch, generate BUILD_REPORT.md, then stop. All other failures use self-heal → defer.

Every deferral must include severity, what was attempted, reproduction steps, recommended fix.

Checkpoint commits after each completed sub-step so reverts are surgical.

Voice: direct, imperative, addressed to the executing agent. No preamble. No pleasantries. Every instruction actionable.

Apply the AUTONOMY_LAYER below to structure sections 2, 7, 8, 9, 10, and 11:

[PASTE AUTONOMY_LAYER.md CONTENTS HERE]

How to use

Generate spec with Charlie (design conversation, requirements, constraints)

Paste this META_PROMPT after the spec

Paste AUTONOMY_LAYER.md contents at the bottom (where indicated)

Charlie generates the autonomous directive

Fire the directive at CC/Codex with Opus

The three files work together:

META_PROMPT.md — what you send to Charlie (this file)

AUTONOMY_LAYER.md — the protocol Charlie applies (paste at bottom of meta-prompt)

The generated directive — what you fire at CC/Codex
