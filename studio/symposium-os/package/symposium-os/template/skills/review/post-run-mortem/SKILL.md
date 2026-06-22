---
name: post-run-mortem
category: review
trigger: After a multi-phase autonomous directive completes (successfully or with halts), before the operator moves to the next work block.
---

# Post-Run Mortem

## Purpose
Capture the operational lessons from a completed multi-phase directive while context is hot. Different from `build-report-ledger` (which is the receipt of what shipped). The mortem is the learning: what worked, what surprised, what should change in the protocol, the skills, or future directives.

Without this skill, operational improvements live in chat history and dissipate. The mortem turns lived experience into protocol updates and project repair entries.

## When to invoke
- Immediately after a multi-phase directive opens its final PR (regardless of success or halt)
- After any directive that hit unexpected halts, repair-playbook gaps, or scope drift
- After a session that introduced a new skill, a new section 2.3 entry, or a new repair pattern
- Before context unloads at end-of-day, end-of-session, or context-limit handoff
- Before sharing learnings with a collaborator or QA tester

## Inputs
- The completed directive
- `BUILD_REPORT.md` from the run
- `AUTONOMOUS_RUN_LOG.md` entries from the run
- `BLOCKERS_FOR_OPERATOR.md` entries if any halts occurred
- `docs/deferred-issues.md` entries from the run
- Operator's subjective notes on the run

## Process
1. Read the build report and run log. Identify each phase's outcome: clean / hit self-heal / hit defer / hit hard stop.
2. For each non-clean outcome, ask:
   - Was the failure mode in the repair playbook?
   - If yes, was the playbook entry sufficient? If no, what would have been?
   - If no, is this a new pattern worth adding to section 2.3?
3. For each `SPEC_REALITY_DELTA` logged during the run, ask:
   - Was this a one-off mismatch or a pattern likely to recur?
   - If pattern: does the project's `AUTONOMY_LAYER.md` section 0.1 need updating?
4. For each scope decision made mid-run (any time the agent deferred a phase or split scope), ask:
   - Was the directive missing a non-goal that would have prevented the ambiguity?
   - Was the directive missing context that the operator could have provided up front?
5. For each manual halt or operator intervention, ask:
   - Was the halt warranted, or did the agent over-halt on something it should have self-healed?
   - Was the halt necessary because of missing protocol coverage?
6. Identify candidates for promotion (per `docs/PROMOTING_PROJECT_LEARNINGS.md`):
   - Project-specific repair entries that have now fired twice (one application away from the rule of three)
   - Patterns observed in this run that match patterns from earlier projects
7. Identify revisions needed to the directive template, the META_PROMPT, or any existing skill, based on what was observed.
8. Produce the mortem.

## Output
A mortem appended to `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-mortem.md`:

```markdown
# Post-Run Mortem — [directive slug]

**Date**: YYYY-MM-DD
**Directive**: [path]
**Outcome**: [clean | partial | halted]

## What worked
- [Pattern that performed as expected]
- [Pattern that performed better than expected]

## What surprised
- [Behavior the operator did not anticipate]
- [Failure mode not covered by the repair playbook]

## What should change

### Section 2.3 candidates
- [New repair entry: name, symptom, attempt 1, attempt 2, defer]

### Skill revisions
- [Existing skill: what to update]
- [New skill candidate: name, scope, evidence]

### Template revisions
- [Directive template: what to update]
- [META_PROMPT: rule to add or change]

### Section 0.1 corrections
- [Stack reality that didn't match what the directive assumed]

## Promotion watch
- [Pattern observed: count of projects this has applied to so far, target third project]

## Operator observations (subjective)
- [What was tiring, frustrating, or surprising for the operator]
- [What felt smooth that didn't feel smooth before]

## Action items
1. [Specific change, with target file path]
2. [Specific change, with target file path]
```

## Stop conditions
- Halt the mortem if the directive run is still in flight. Wait until final PR opens.
- Halt if the operator does not have time to do this thoughtfully. A rushed mortem produces shallow findings. Defer to next session and note that context will dilute.
- Halt if findings cluster around a single architectural decision rather than operational patterns. That's not a mortem — that's a meta-ADR. Escalate to the meta-ADR process instead.

## Cadence and discipline
The mortem is short. Aim for 15 to 30 minutes after a multi-phase directive completes. Longer than that suggests either over-engineering the document or finding too many issues to address in one mortem (split into multiple action items, tackle one at a time).

Mortems compound. Three mortems showing the same finding is grounds for promotion to canonical per `docs/PROMOTING_PROJECT_LEARNINGS.md`.

## Anti-patterns
- **Mortem theater**: filing the mortem without acting on the action items. The whole point is the changes downstream.
- **Blame framing**: a mortem is about the protocol and the directives, not about the agent or the operator. If the language drifts toward "the agent did X wrong," reframe to "the directive did not specify Y."
- **Mortem as build report**: the receipt belongs in `BUILD_REPORT.md`. The mortem is exclusively about lessons.

## Related
- `skills/review/build-report-ledger` — the receipt that accompanies every run; this skill is the lessons that accompany select runs
- `skills/handoff/session-handoff` — often follows a mortem at end of session
- `docs/PROMOTING_PROJECT_LEARNINGS.md` — where rule-of-three patterns from mortems eventually land
- `AUTONOMY_LAYER.md` section 2.3 (project-specific repair entries)
