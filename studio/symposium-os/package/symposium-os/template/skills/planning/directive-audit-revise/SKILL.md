---
name: directive-audit-revise
category: planning
trigger: Before firing a high-stakes or long-running directive, especially when scope spans multiple phases or surfaces.
---

# Directive Audit & Revise

## Purpose
Catch directive defects before they consume an autonomous run. A directive that ships with brittle instructions wastes the entire run on false halts, scope drift, or hardcoded assumptions that don't match repo reality. This skill applies external lenses to a draft directive and produces revisions before GO.

## When to invoke
- Directive covers more than 3 phases or expects to run more than 90 minutes of agent time
- Directive will run on credit-limited or capacity-limited capability (Opus runs, expensive API tiers)
- Directive touches multiple distinct surfaces (frontend + backend + infra)
- Directive depends on assumptions about repo state that haven't been verified
- Previous directive of this scope hit avoidable halts or scope drift
- Stakes are high enough that a wasted run sets the project back by a day or more

## Inputs
- Draft directive (from `skills/planning/generate-directive`)
- Current canonical `AUTONOMY_LAYER.md` for the project
- Auditor lens set (operator-chosen — see Process step 2)
- Optionally: a second model run for cross-model audit

## Process
1. Read the draft directive end to end. Note any instruction that depends on a specific number (route counts, file counts, test counts) — these are common false-halt sources.
2. Select auditor lenses. The default set:
   - **Brittle-assertion auditor**: hardcoded numbers, exact-string matches, "should pass with N routes" claims that will false-halt if the number changes for unrelated reasons
   - **Phase-dependency auditor**: instructions in one phase that implicitly require something a future phase builds (e.g., Phase A requires a bottom-sheet pattern that Phase B owns)
   - **Scope-drift auditor**: phases that quietly expand into adjacent work, non-goals not stated, scope creep risks
   - **Repo-reality auditor**: paths, commands, file references, test runners that may not match `AUTONOMY_LAYER.md` section 0.1
   - **Operator-decision auditor**: places where the directive defers to the operator without saying so, or implicitly bakes in an operator decision that should be explicit
   - **Stop-condition auditor**: hard stops that should be self-heals; self-heals that should be hard stops; missing stop conditions on phases that need them
3. Run the directive through each lens. Either by directing a second AI instance to apply the lens explicitly, or by walking through the lens questions manually as the operator.
4. For multi-model audit on high-stakes directives: send the directive to two or three distinct models (e.g., Claude, GPT, Gemini) with the same lens prompt. Compare findings.
5. Consolidate findings. Group by severity:
   - **Must-fix**: directive will halt incorrectly or produce wrong output without this change
   - **Should-fix**: directive will work but is brittle or wasteful
   - **Nit**: minor clarity or convention issues
6. Apply must-fix and should-fix revisions. Defer nits to next revision cycle if any.
7. If the directive substantially changes (more than 20% of content), run one more audit pass before GO. Otherwise fire after applying revisions.

## Output
A revision diff or revised directive, plus a short audit log:

```markdown
# Directive Audit — [directive slug]

## Auditors
- Lens A: [name] — [findings count]
- Lens B: [name] — [findings count]
- Multi-model: [models used]

## Findings

### Must-fix
1. [Finding]: [exact directive line] → [revised line]
2. ...

### Should-fix
1. [Finding]: [exact directive line] → [revised line]
2. ...

### Nits (deferred)
1. [Finding]

## Revision summary
- N must-fix applied
- N should-fix applied
- N nits deferred to next revision
- Directive cleared for GO
```

## Stop conditions
- Halt if must-fix findings cannot be applied without changing scope. The directive needs more design work; do not fire.
- Halt if auditor lenses disagree on whether a finding is must-fix vs nit. Escalate to operator.
- Halt if a multi-model audit produces sharply divergent findings — that signals the directive itself is ambiguous, not that one model is wrong.

## Anti-patterns
- **Audit theater**: running the lenses without acting on the findings. The point is revisions, not a checklist.
- **Endless revision**: more than 3 audit cycles signals the directive is the wrong shape, not that one more pass will fix it. Stop and reconsider scope.
- **Single-lens audit on high-stakes work**: one auditor catches one class of error. Use the full lens set for any multi-phase run.

## Related
- `skills/planning/generate-directive` — produces the input to this skill
- `skills/review/council-review` — analogous skill at the artifact level rather than the directive level
- `AUTONOMY_LAYER.md` section 1.7 (scope discipline)
- `AUTONOMY_LAYER.md` section 1.13 (spec-reality reconciliation)
