---
name: build-report-ledger
category: review
trigger: At the end of any meaningful work session, especially autonomous build sessions.
---

# Build Report / Compression Ledger

## Purpose
Convert a finished session into a receipt. Document what shipped, what was deferred, and (optionally) the compression ratio relative to a pre-AI baseline. Used for project positioning, operator pattern memory, and downstream handoff.

## When to invoke
- End of an autonomous build session
- End of a meaningful work day
- After a client-facing build sprint where the compression ratio is positioning evidence
- Before handing the project off to another operator or agent

## Inputs
- Branch name(s)
- PR list (merged and open)
- Test results
- Production deploy outcomes
- A rough pre-AI baseline estimate for the same scope (optional; required only when claiming a compression ratio publicly)
- The actual operator hours spent directing

## Process
1. Inventory the work: shipped PRs, open PRs, tests added/passing, prompts edited, infra changed, design decisions made, council reviews run.
2. Categorize: backend, frontend, infra, QA, devops, design, technical leadership.
3. (Optional) Estimate pre-AI baseline for the same scope (hours, team size, calendar time).
4. (Optional) Estimate the current AI-native market baseline (what a typical AI-native shop would quote).
5. Record actual operator hours directing.
6. (Optional) Compute compression ratio (pre-AI baseline / actual operator hours).
7. (Optional) Estimate private margin if relevant to positioning.
8. Caveats: what's not done, what's deferred, what's `MANUAL_PLAYTEST_REQUIRED`, what's `COUNCIL_REVIEW_REQUIRED`.
9. Workflow lessons: what worked, what didn't, what to encode in a new or revised skill.
10. Next-session handoff pointer: what the next agent or next session should pick up. Reference `skills/handoff/session-handoff` if a full handoff doc is warranted.
11. Produce the ledger.

## Output
A `BUILD_REPORT.md` per `AUTONOMY_LAYER.md` section 5 format, plus an optional "Compression Ledger" appendix with the baseline estimates and operator hours.

## Stop conditions
- Skip the compression ratio for sessions under one hour. The signal is too noisy.
- Halt the public compression claim if you cannot honestly cite the pre-AI baseline. Fake compression numbers damage project credibility more than absent ones.
- Halt if the report would expose production secrets, real user data, or any content covered by `AUTONOMY_LAYER.md` section 1.11.

## Related
- `AUTONOMY_LAYER.md` section 5 (BUILD_REPORT format)
- `templates/build-report-template.md`
- `skills/handoff/session-handoff`
