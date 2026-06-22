---
name: generate-directive
category: planning
trigger: When a spec is ready and needs to be converted into a runnable build directive.
---

# Generate Directive

## Purpose
Convert a finalized spec into a single autonomous build directive that an agent can execute end-to-end.

## When to invoke
- A spec has been reviewed and accepted
- The stack is locked (`AUTONOMY_LAYER.md` section 0.1 populated)
- The operator is ready to fire at one or more executing agents

## Inputs
- The spec document
- The current `AUTONOMY_LAYER.md` for the project
- The current `META_PROMPT.md` for the project
- Known constraints not in the spec: parallel-agent intent, auto-merge intent, agent assignments, stacked PR chain order if applicable

## Process
1. Read the spec end-to-end. Identify scope, phases, design data, fallback content.
2. Run a scope review: is anything outside reasonable autonomous executability? If yes, propose trims and document them.
3. Open the directive with the header block from `AUTONOMY_LAYER.md` section 0.2.
4. Write the role statement. One paragraph. What the agent is doing, on which surface, with what constraints.
5. Reference `AUTONOMY_LAYER.md` for protocol, stack, repair playbook, deferred-issues format, BUILD_REPORT format, hard stops. Do not duplicate.
6. Embed all design data verbatim: schema deltas, file structure (new/modified/deleted with full paths), code patterns, prompt fragments, copy banks, default values, migration mappings.
7. Plan phases. Each phase must have all five elements (pre-flight, smoke-first, implementation, health check, commit). The first data-consuming phase explicitly calls out spec-reality reconciliation per `AUTONOMY_LAYER.md` section 1.13.
8. **No halt between phases.** State explicitly in the Phase Plan that the agent opens each PR and immediately continues to the next phase. The operator merges all PRs in order after the full run completes. Per `AUTONOMY_LAYER.md` section 1.15. Do NOT include language like "operator merges each PR before the next phase begins."
9. For docs-only or template-only phases, specify smoke assertions as validation checks (paths resolve, cross-references resolve, no unfilled placeholders, markdown parses) per `AUTONOMY_LAYER.md` section 3 EXECUTION. Do not instruct the agent to write unit tests for docs.
10. Propose parallel-agent split if applicable. Mark which surfaces require credentialed agents (production writes, deploy ops) vs code-only cloud agents (no credentials).
11. Declare auto-merge eligibility per `AUTONOMY_LAYER.md` section 0.2 rules.
12. If the directive depends on or extends a stacked PR chain, declare chain order and apply `AUTONOMY_LAYER.md` section 1.15.
13. Write the GO instruction with branch name and first concrete action.

## Output
A single markdown file: `[project]-directive-[wave-slug]-v[N].md`, using `.symposium/templates/directive-template.md` as the scaffold.

## Stop conditions
- Halt if `CONTEXT.md` is the blank template (no domain terms filled in across Product, Domain, or Architecture sections). Init has not completed; the agent lacks the language layer required to disambiguate the spec.
- Halt if `AUTONOMY_LAYER.md` section 0.1 is unfilled.
- Halt if `adr/0001-adopted-symposium-os.md` is unfilled or missing. Init has not completed.
- Halt if any fallback content (prompt fragment, copy, default values) is not specified in the spec. Escalate to the spec author.
- Halt if more than 10 phases are needed and no parallel split is possible. The spec needs decomposition.
- Halt if any phase mixes credentialed and code-only work. Split into separate directives or separate phases with clear agent assignments.
- Halt if the draft directive contains "operator merges each phase before the next begins" or equivalent halt-per-merge language. This contradicts `AUTONOMY_LAYER.md` section 1.15. Rewrite to use the no-halt pattern before emitting the directive.

## Related
- `META_PROMPT.md` — the prompt that invokes this skill in a chat-based directing AI
- `AUTONOMY_LAYER.md` sections 0.2, 1.5, 1.6, 1.8, 1.13, 1.15, 3
- `templates/directive-template.md`
- `skills/planning/grill-with-docs` — run this first if the spec introduces new vocabulary
