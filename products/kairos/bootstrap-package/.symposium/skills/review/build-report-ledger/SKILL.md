---
name: build-report-ledger
category: review
trigger: At the end of any meaningful work session, especially autonomous build sessions.
---

# Build Report / Compression Ledger

## Purpose
Convert a finished session into a receipt. Document what shipped, what was deferred, what the agentic compression ratio was relative to a pre-AI baseline. Used for Symposium positioning and Marcus's own pattern memory.

## When to invoke
- End of an autonomous build session
- End of a meaningful work day
- After a client-facing build sprint (for Symposium positioning artifacts)

## Inputs
- Branch name
- PR list (merged and open)
- Test results
- Production deploy outcomes
- A rough 2022 pre-AI baseline estimate for the same scope
- The actual hours Marcus spent directing

## Process
1. Inventory the work: shipped PRs, open PRs, tests added/passing, prompts edited, infra changed, design decisions made, council reviews run.
2. Categorize: backend, frontend, infra, QA, devops, design, technical leadership.
3. Estimate 2022 pre-AI baseline for the same scope (hours, team size, calendar time).
4. Estimate 2026 AI-native market baseline (what a typical AI-native shop would quote).
5. Record actual director hours.
6. Compute compression ratio (2022 baseline / actual director hours).
7. Estimate private margin (rough financial framing for Symposium's positioning).
8. Caveats: what's not done, what's deferred, what's MANUAL_PLAYTEST_REQUIRED.
9. Workflow lessons: what worked, what didn't, what to encode in a new or revised skill.
10. Next-session handoff: what the next agent or next session should pick up.
11. Produce the ledger.

## Output
A `BUILD_REPORT.md` per `AUTONOMY_LAYER.md` section 5 format, plus a "Compression Ledger" appendix with the baseline estimates and director hours.

## Stop conditions
- Skip the compression ratio for sessions under one hour. The signal is too noisy.
- Halt if you cannot honestly cite a 2022 baseline. Fake compression numbers damage Symposium's credibility more than absent ones.

## Related
- `AUTONOMY_LAYER.md` section 5 (BUILD_REPORT format)
- `templates/build-report-template.md`
- `skills/handoff/session-handoff`
