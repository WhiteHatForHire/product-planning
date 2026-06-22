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
- You're ready to fire at CC Local, CC Cloud, or Codex

## Inputs
- The spec document
- The current `AUTONOMY_LAYER.md` for the project
- The `META_PROMPT.md` for the project
- Any known constraints not in the spec (parallel-agent intent, auto-merge intent)

## Process
1. Read the spec end-to-end. Identify scope, phases, design data, fallback content.
2. Run a scope review: is anything outside reasonable autonomous executability? If yes, propose trims and document them.
3. Open the directive with the six-field header block from `AUTONOMY_LAYER.md` section 0.2.
4. Write the role statement. One paragraph. What the agent is doing, on which surface, with what constraints.
5. Reference `AUTONOMY_LAYER.md` for protocol, stack, repair playbook, deferred-issues format, BUILD_REPORT format, hard stops. Do not duplicate.
6. Embed all design data verbatim: schema deltas, file structure (new/modified/deleted with full paths), code patterns, prompt fragments, copy banks, default values, migration mappings.
7. Plan phases. Each phase must have all five elements (pre-flight, smoke-first, implementation, health check, commit). The first data-consuming phase explicitly calls out spec-reality reconciliation.
8. Propose parallel-agent split if applicable. Mark which surfaces are credentialed (CC Local) vs code-only (CC Cloud).
9. Declare auto-merge eligibility per `AUTONOMY_LAYER.md` section 0.2 rules.
10. Write the GO instruction with branch name and first concrete action.

## Output
A single markdown file: `[project]-directive-[wave-name]-v[N].md`

## Stop conditions
- Halt if any fallback content (prompt fragment, copy, default values) is not specified in the spec. Escalate to the spec author.
- Halt if the stack section of `AUTONOMY_LAYER.md` is unfilled.
- Halt if more than 10 phases are needed and no parallel split is possible.

## Related
- `META_PROMPT.md` (the prompt you paste into the chat to invoke this skill)
- `AUTONOMY_LAYER.md` sections 0.2, 1.5, 1.6, 1.8, 3
- `templates/directive-template.md`
