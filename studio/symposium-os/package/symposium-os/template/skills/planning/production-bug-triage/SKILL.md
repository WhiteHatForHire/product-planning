---
name: production-bug-triage
category: planning
trigger: When real-user testing or production usage surfaces multiple bugs that need scoped, sequenced fixes.
---

# Production Bug Triage

## Purpose
Convert a batch of user-reported production bugs into one or more scoped fix directives that the agent can execute end-to-end. Prevents the failure mode of "fix one bug, ship a PR, find the next one, repeat" — which doesn't compound and rarely closes the issue list.

## When to invoke
- Real-user testing returns multiple bug reports against a deployed product
- A QA tester (junior or senior) submits a structured bug list
- A post-launch retrospective surfaces a backlog of small product gaps
- Multiple operator-internal observations accumulate without a clear path to ship

## Inputs
- The bug list (informal text is fine; the skill structures it)
- Current production URL or build SHA where the bugs were observed
- Operator's launch deadline or sequencing constraint
- Awareness of any in-flight directives that should not be disturbed

## Process
1. Read every bug report. Do not assume the operator's framing is correct — re-read the raw observation if a screenshot or paste is attached.
2. For each bug, identify the layer where it lives:
   - **Data layer**: source data wrong, missing, malformed, duplicated
   - **State layer**: localStorage, server state, or in-memory state inconsistent across surfaces
   - **UI layer**: visible component bug, layout, copy, density
   - **Logic layer**: scoring, search, filtering, sorting producing wrong results
   - **Integration layer**: external service call, deep link, calendar provider, API contract
   - **Performance / network layer**: slow load, broken asset, 4xx/5xx response
3. For each bug, diagnose root cause from observable symptoms. If the cause is unclear, note it as "needs diagnosis" rather than guessing.
4. Group bugs by:
   - Same layer + same files → bundle into one PR
   - Different layers but same surface → still bundle if scope stays small
   - Risk-mismatched (one safety-adjacent, others cosmetic) → separate PRs
5. For each group, determine sequencing dependencies. Example: a state-layer fix that other bugs depend on goes first. A cosmetic fix that downstream bugs touch the same file can go second.
6. Produce a fix plan: which PRs, what each one fixes, what order they ship in, which can be auto-merged.
7. Write a fix directive per group using `skills/planning/generate-directive`. Each directive references the specific bugs it closes and the user reports it answers.
8. Identify any bugs that need operator decisions before they can be fixed (scope decisions, design changes, intent ambiguity). Surface those to the operator separately — do not bundle into a fix directive.

## Output
A structured bug triage report:

```markdown
# Bug Triage — [date]

## Source
- Reporter: [QA tester / operator / external user / etc.]
- Observed against: [production URL or build SHA]
- Raw report: [path or quoted block]

## Triage table

| # | Bug | Layer | Root cause hypothesis | Group |
|---|---|---|---|---|
| 1 | [short description] | [data / state / UI / logic / integration / perf] | [hypothesis or "needs diagnosis"] | [Group A / B / C / standalone / operator-decides] |

## Fix plan

### Group A — [name]
- Bugs: [#1, #3, #5]
- Surfaces: [file paths]
- Directive: `docs/directives/fix-[slug]-vN.md`
- Sequencing: ship before Group B because Group B depends on the state-layer fix here

### Group B — [name]
- ...

## Operator decisions required
- [Bug #N]: needs decision on [specific question] before the fix can be scoped
```

## Stop conditions
- Halt if any bug is safety-adjacent (per `AUTONOMY_LAYER.md` section 1.11) — route to `skills/review/council-review` before scoping a fix.
- Halt if a bug requires reopening a locked architectural decision documented in `adr/`. The fix is not in scope; the architecture change is. Escalate.
- Halt if the bug count is high enough that the triage becomes its own multi-hour effort. Surface to operator with a recommendation to split the triage itself across sessions.
- Halt if the bug report is vague enough that triage requires guessing. Ask the operator to clarify before triaging.

## Anti-pattern
Do not silently expand fix scope to address bugs not in the original list. If you find additional bugs during diagnosis, surface them to the operator as a separate triage entry. Each fix directive must close a stated bug, not drift into adjacent territory.

## Related
- `skills/planning/generate-directive` — the skill that writes each fix directive
- `skills/review/council-review` — for safety-adjacent bugs before fixing
- `skills/review/post-run-mortem` — for bug patterns that recur across sessions
- `AUTONOMY_LAYER.md` section 1.7 (scope discipline)
- `AUTONOMY_LAYER.md` section 1.11 (production safety boundaries)
