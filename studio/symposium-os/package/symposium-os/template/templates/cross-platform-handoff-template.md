# Cross-Platform Agent Handoff — [run slug]

**Date**: YYYY-MM-DD
**From runtime**: [origin: Claude / Codex / Gemini / etc.]
**To runtime**: [destination: Claude / Codex / Gemini / etc.]
**Reason for handoff**: [credit limit / context limit / capability mismatch / parallel split / runtime outage / operator choice]

Use this template when an in-flight directive must continue on a different agent runtime. Different from `handoff-template.md` (which assumes both ends speak the same runtime). The cross-platform variant carries extra context the destination runtime cannot infer from chat history.

---

## Current state

- **Repo**: [URL]
- **Production URL**: [URL or N/A]
- **Working branch**: [name]
- **Base SHA**: [SHA]
- **Last commit**: [SHA + short message]
- **Local working tree**: [clean / dirty — describe if dirty]

## Directive in flight

- **Directive path**: [path]
- **Phases complete**: [list]
- **Phases pending**: [list]
- **Current phase**: [name]
- **Current phase step**: [where the previous agent stopped within the phase]

## What the previous agent did

Walk the destination runtime through what's already been done. Do not assume it can read prior chat. Reference durable artifacts by path, not by chat reconstruction.

- Files changed: [paths with one-line summary each]
- PRs opened: [#N — [name]]
- Tests added: [list]
- Self-check gate results so far: [paste or reference]

## What the destination agent must do next

State the resumption point in imperative voice. Be specific enough that the destination can begin without rereading the entire directive.

1. [Concrete first action]
2. [Concrete second action]
3. [Continue per phase plan in the directive]

## Runtime-specific notes for the destination

Address differences in how the destination runtime should approach the work, if any:

- **Tool access differences**: [e.g., destination has no shell access, must use MCP file writes per `skills/execution/mcp-write-safety`]
- **Context window differences**: [e.g., destination has a smaller context; aggressive use of session-scoped run notes to avoid context bloat]
- **Capability tier**: [per `skills/planning/model-routing` — note if the tier is different and what to be cautious about]
- **Convention differences**: [e.g., destination defaults to different comment styles, different commit message formats; reinforce the project's conventions]

## Apply protocol unconditionally

The destination runtime must apply `.symposium/AUTONOMY_LAYER.md` before executing. Doctrine does not transfer through chat history; it transfers through the repo.

If the destination cannot read `.symposium/AUTONOMY_LAYER.md`, halt immediately and surface to `BLOCKERS_FOR_OPERATOR.md`. Do not proceed with the directive on assumption.

## Stop gates

- Halt if the destination cannot reach the repo (auth issue, network, tooling difference). Surface to operator.
- Halt if the destination's tool set cannot perform a required action in the next phase (e.g., needs to deploy but has no credentials). Surface.
- Halt if continuing would require re-running phases the previous agent already completed. Surface — re-running risks divergent commits.

## Known risks of the cross-platform handoff

- **Tooling drift**: the destination may use a different test runner, build command, or version control workflow. Reinforce per `AUTONOMY_LAYER.md` section 0.1.
- **Style drift**: the destination may produce code or commits in a style that diverges from the previous agent's. Operator may need a small style-consistency pass after the run.
- **Hidden state**: the previous agent may have built up implicit context (open file references, scratch files, partial diagnoses) that does not transfer through chat or repo. Make implicit context explicit in this handoff.

## Acceptance criteria for the handoff itself

This handoff is successful when:
- The destination agent reads this document and `.symposium/AUTONOMY_LAYER.md`
- Begins from the stated resumption point without re-running prior phases
- Produces output that the operator can merge or evaluate against the original directive

## Original directive

Reference the original directive by path. Do NOT re-paste the directive content into this handoff. The destination reads the directive from the repo or from the operator-pasted directive in the new chat session.

- Path: [path]
- Operator may also paste the directive into the destination chat alongside this handoff.

## Operator action after handoff

After the destination agent acknowledges this handoff and begins:

1. Verify the destination has access to the repo and can read `.symposium/`
2. Verify the destination's first commit matches the intended phase
3. Stand back; let the destination complete the run
4. Mortem the cross-platform handoff itself per `skills/review/post-run-mortem` to capture any tooling or convention gaps for future handoffs
