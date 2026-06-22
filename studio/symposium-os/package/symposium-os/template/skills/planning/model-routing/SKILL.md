---
name: model-routing
category: planning
trigger: Before firing any directive, when choosing which agent capability tier to assign.
---

# Model Routing

## Purpose
Match agent capability to directive complexity. Spending high-tier capability on mechanical work wastes credits; spending low-tier capability on architectural work wastes the run. This skill formalizes the routing decision so it doesn't get re-derived each time.

The skill is platform-agnostic. Capability tiers map differently across runtimes (Claude Opus / Sonnet / Haiku, GPT-5 / 4o / mini, etc.), but the routing principles are the same.

## When to invoke
- About to fire a new directive and the agent assignment is not obvious
- Operator credit budget is tight and tier selection matters
- Multi-phase directive could be split across capability tiers per phase
- Past directive of similar shape hit unexpected halts or scope drift that suggest wrong tier was used

## Inputs
- The directive (or directive draft) being routed
- Available capability tiers in the operator's current agent runtime
- Operator's credit / budget posture
- Concurrency constraints (parallel agents, runtime caps)

## Process
1. Read the directive header and phase plan. Identify the dominant work type.
2. Classify the directive against the routing matrix below.
3. If the directive spans multiple work types, consider splitting it across capability tiers. Example: Phase A is architectural (high tier), Phases B–E are mechanical execution (mid tier), Phase F is batch enrichment (low tier).
4. Apply the routing decision:
   - High tier for architectural judgment, ambiguous requirements, complex multi-file refactors, council adjudication
   - Mid tier for well-bounded execution, single-file changes, mechanical verification, build/test loops
   - Low tier for batch processing of structured data, high-volume simple tasks, deterministic transformations
5. Record the routing decision in the directive header (`Agent:` field) and in `AUTONOMOUS_RUN_LOG.md` with one-sentence rationale.

## Routing matrix

| Work type | Tier | Why |
|---|---|---|
| Spec → directive conversion | High | Requires judgment about scope, sequencing, fallback content |
| Architectural decision under uncertainty | High | Multiple defensible answers; needs reasoning across constraints |
| Complex script authorship that imports project code | High | Type matching, import resolution, runtime correctness |
| Multi-file refactor crossing system boundaries | High | Cross-cutting reasoning; mid-tier produces "looks right but fails at runtime" |
| Council adjudication on conflicting findings | High | Synthesis across model disagreements |
| Single-file UI changes with clear acceptance criteria | Mid | Bounded; spec is the spec |
| Build / typecheck / test verification loops | Mid | Mechanical; failure modes are well-defined |
| Conflict resolution on known-tier files (per AUTONOMY_LAYER §1.15) | Mid | Tier 1 is mechanical; Tier 2 needs judgment; Tier 3 escalates |
| Sequential merge maintenance across stacked PRs | Mid | Mechanical once protocol is followed |
| QA pass against a live deployment | Mid | Reading output, applying rubric, generating report |
| Batch enrichment of structured data (LLM-tagging large corpora) | Low | High-volume, deterministic transformations, idempotent retries |
| Format conversions, data extractions, regex over corpora | Low | Throughput-bound, not judgment-bound |
| Generating per-record summaries from templates | Low | Template-driven, parallelizable |

## Output
A routing note appended to the directive header and to `AUTONOMOUS_RUN_LOG.md`:

```
Agent assignment: [tier]
Rationale: [one sentence]
Multi-tier split: [yes/no — if yes, which phases at which tier]
```

## Stop conditions
- Halt if a directive's work type doesn't fit any row in the matrix cleanly. The directive may need decomposition before routing.
- Halt if the operator's budget cannot support the recommended tier for the dominant work type. Surface the tradeoff: cheaper tier likely produces lower-quality output and may require re-runs.
- Halt if a single phase would need to bounce between tiers mid-execution. Either split the phase or accept the higher tier for the whole phase.

## Common mistakes to avoid
- **Using high tier for everything**: burns credits without proportional quality gain. Most build work is mid-tier territory.
- **Using mid tier for spec-to-directive conversion**: the directive is the contract; defects propagate through the entire run. Always high-tier for directive generation.
- **Using low tier on tasks that need reasoning about edge cases**: batch tools fail silently on edge cases. Use mid tier when correctness matters even at high volume.
- **Switching tiers mid-run to save credits**: usually produces worse output than completing on the original tier. Commit to a tier per phase.

## Related
- `skills/planning/generate-directive` — the directive whose agent assignment this skill informs
- `skills/planning/directive-audit-revise` — audits often surface tier mismatches as findings
- `AUTONOMY_LAYER.md` section 0.2 (directive header format includes Agent field)
- `docs/PARALLEL_AGENTS.md` — capability tiers also inform parallel-agent split decisions
