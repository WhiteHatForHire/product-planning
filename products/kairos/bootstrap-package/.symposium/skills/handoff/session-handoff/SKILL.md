---
name: session-handoff
category: handoff
trigger: When passing context between agents, between sessions, or when compacting before a context limit.
---

# Session Handoff

## Purpose
Transfer context between agents (Claude → Codex, CC Local → CC Cloud) or between sessions (today → tomorrow) without re-explaining everything.

## When to invoke
- Switching from planning to implementation
- Splitting a long Claude thread into Codex execution
- Moving from local agent to cloud agent
- Closing a build session
- Handing one PR to another agent for review or fix
- Preserving context before compaction or a context-limit cliff

## Inputs
- Current session state (what's been decided, what's open)
- Durable artifacts produced (PRs, issues, specs, ADRs, build logs)
- The next agent's task

## Process
1. Identify the objective for the next agent. One sentence.
2. Snapshot current state: what's done, what's in progress, what's pending.
3. List durable artifacts the next agent should read (paths, PR URLs, issue numbers, ADR slugs). Do not duplicate their content.
4. Specify exactly which artifacts not to duplicate (e.g., "the spec lives at `docs/kairos-spec-v1.1.md`; do not re-summarize").
5. State the next agent's job in imperative voice. Concrete actions.
6. Suggest skills or directives the next agent should invoke.
7. Note stop gates (when to halt and escalate back).
8. List known risks.
9. State acceptance criteria.
10. Produce the handoff.

## Output
A markdown handoff doc using `templates/handoff-template.md`. Lives at `docs/handoffs/session-YYYY-MM-DD-[slug].md`.

## Stop conditions
- Halt if the next agent's objective is unclear. Sharpen before handing off.
- Halt if there are more than 5 open decisions. Resolve them or surface them as `BLOCKERS_FOR_MARCUS.md` items.

## Key rule
Do not repeat everything. Reference durable artifacts by path, PR, issue, or URL. The handoff is a pointer document, not a re-summary.

## Related
- `templates/handoff-template.md`
- `skills/review/build-report-ledger` (often run alongside handoff at end of session)
