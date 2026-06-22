# META_PROMPT.md — Symposium OS Canonical Edition v2.3

Spec-to-directive converter. Send to the directing AI after generating any project spec. Pairs with `AUTONOMY_LAYER.md` (Symposium OS Canonical Edition v2.3).

This file is project- and platform-agnostic. The directing AI uses this prompt to compile a spec into a runnable directive that any agent can execute end-to-end. Stack reality comes from `AUTONOMY_LAYER.md` section 0.1 of the calling project. Operator preferences (parallel-agent concurrency, auto-merge defaults, agent assignments) are passed in alongside the spec.

---

## The Prompt (paste verbatim after your spec, with `AUTONOMY_LAYER.md` contents appended at the bottom)

Take the spec above and turn it into a fully autonomous build directive using `AUTONOMY_LAYER.md` (Symposium OS Canonical Edition v2.1, at `.symposium/AUTONOMY_LAYER.md`).

Apply these rules:

1. Run scope review first (`AUTONOMY_LAYER.md` section 0). If the spec exceeds reasonable autonomous executability, trim and document trims at the top of the directive.

2. The stack is fixed. See `AUTONOMY_LAYER.md` section 0.1 (filled in for this project). Do not propose alternatives.

3. Open the directive with the header block from `AUTONOMY_LAYER.md` section 0.2. No line-count estimates, no phase-count estimates, no time estimates.

4. Auto-merge eligibility — declare yes/no per `AUTONOMY_LAYER.md` section 0.2 eligibility rules.

5. Specify all fallback content inline (`AUTONOMY_LAYER.md` section 1.6). No "agent invents the copy" patterns. Spec verbatim:
   - Prompt fragment text
   - Approved-copy banks and forbidden-copy lists
   - User-facing error messages
   - Default values for new schema fields
   - Migration backfill mappings

6. Split acceptance criteria into AUTOMATED and HUMAN_REVIEW (`AUTONOMY_LAYER.md` section 1.5).

7. State deployment posture per `AUTONOMY_LAYER.md` section 1.8.

8. Mark "feel" and visual criteria as HUMAN_REVIEW. The agent cannot verify voice, visual correctness, or behavioral appropriateness.

9. Make optional integrations fully deferrable (`AUTONOMY_LAYER.md` section 2.1 GENERIC-11). The system must run without them.

10. Use the self-repair playbook in `AUTONOMY_LAYER.md` section 2. Add project-specific entries only when the directive introduces a new failure mode.

11. Atomic commits per concern (`AUTONOMY_LAYER.md` section 1.9). One concern per commit.

12. No silent failures (`AUTONOMY_LAYER.md` section 1.10).

13. Production safety boundaries hold always (`AUTONOMY_LAYER.md` section 1.11).

14. Parallel-agent split is first-class. If multiple independent surfaces exist, propose the split explicitly:
    - Which surfaces can run on code-only cloud agents (no credentials, no production access).
    - Which surfaces require a credentialed local agent (database writes, external API calls with secrets, deploy ops).
    - Which surfaces require Council of Models review before merge.
    - How the branches reconcile (which merges first, what depends on what).
    - Shared coordination layer: `AUTONOMOUS_RUN_LOG.md` at repo root and per-session run notes per `AUTONOMY_LAYER.md` section 0.4.

    Default to the operator's stated concurrency cap. If not stated, assume up to 4 concurrent agents.

15. Every phase MUST include all five of these in order (per `AUTONOMY_LAYER.md` section 3):
    - PRE-FLIGHT
    - SMOKE ASSERTIONS WRITTEN FIRST
    - IMPLEMENTATION
    - HEALTH CHECK
    - COMMIT

    Phases without smoke assertions are not phases. They are unverified changes.

    For docs-only or template-only phases (no executable code), smoke assertions are validation checks: paths resolve, cross-references resolve, no unfilled placeholders, markdown parses. Per `AUTONOMY_LAYER.md` section 3 EXECUTION. Do NOT instruct the agent to write unit tests for docs-only phases.

16. The first phase that consumes the directive's design data must call out spec-reality reconciliation explicitly per `AUTONOMY_LAYER.md` section 1.13.

17. MCP write safety per `AUTONOMY_LAYER.md` section 1.12. Direct git push is preferred.

18. If the spec depends on a stacked PR chain or an in-flight merge sequence, apply `AUTONOMY_LAYER.md` section 1.15 (stacked PR conflict resolution protocol). State the chain order in the directive header.

19. **No halt between phases of a stacked chain.** The directive must NOT include language like "operator merges each PR before the next phase begins" or "agent waits for operator merge between phases." Per `AUTONOMY_LAYER.md` section 1.15, the agent opens each PR and immediately continues to the next phase. The operator merges all PRs in order after the full run completes. This applies regardless of `Auto-merge: yes` or `Auto-merge: no` settings. If the operator's spec genuinely requires per-phase review gating (high-risk work), that is not a stacked chain — split it into separate directives, one per phase.

Generate the directive including:

- Header block (`AUTONOMY_LAYER.md` section 0.2 format)
- Role statement (one paragraph)
- "Apply `AUTONOMY_LAYER.md` before executing."
- "Stack: see `AUTONOMY_LAYER.md` section 0.1."
- Deployment posture (PR-only stop, auto-merge yes/no with rationale, migration application instructions for the operator if applicable)
- Full design data from the spec (schema deltas, file structure, code snippets for non-obvious patterns, prompt fragments verbatim, test fixture data verbatim, default values verbatim)
- Working files protocol (`AUTONOMY_LAYER.md` section 0.4)
- Phase plan: ordered phases, each with the five elements from rule 15. The first data-consuming phase explicitly includes spec-reality reconciliation as the first implementation step.
- Directive-specific self-repair entries (only if introducing failure modes not in the playbook)
- "Deferred-issues format: `AUTONOMY_LAYER.md` section 4"
- "BUILD_REPORT format: `AUTONOMY_LAYER.md` section 5"
- "Hard stops: `AUTONOMY_LAYER.md` section 6"
- GO instruction: first concrete action with branch name.

Voice:
- Direct, imperative, addressed to executing agent.
- No preamble. No pleasantries.
- Every instruction actionable.
- Reference `AUTONOMY_LAYER.md` by section number. Do not duplicate long passages.
- All agent-facing prompts and commands in fenced triple-backtick blocks. Never blockquotes.

[PASTE `AUTONOMY_LAYER.md` CONTENTS HERE]

---

## How to use

1. Generate the spec in chat. Design conversation: schema, prompts, copy, acceptance criteria, parallel-agent intent, auto-merge intent.
2. Paste this META_PROMPT verbatim, then paste `AUTONOMY_LAYER.md` contents at the bottom where indicated.
3. The directing AI generates the directive as a single Markdown file.
4. Review the directive. Verify:
   - Header block present and complete
   - Fallback content inlined (no "agent invents the copy" patterns)
   - Parallel-agent split declared if applicable
   - Every phase has the five elements
   - First data-consuming phase calls out spec-reality reconciliation
   - Auto-merge eligibility declared correctly
5. Fire at the chosen agent(s) per the directive's `Agent:` field.

## The three files together

- `META_PROMPT.md` — what you send to the directing AI when generating a directive (this file)
- `AUTONOMY_LAYER.md` — protocol the directing AI applies and the executing agent obeys
- The generated directive — what you fire at the executing agent(s)

## Versioning alignment

This META_PROMPT version tracks `AUTONOMY_LAYER.md` version. If `AUTONOMY_LAYER.md` ticks to v2.4 or v3.0, regenerate this file referencing the new section numbers and any new doctrine sections.

End of META_PROMPT.md (Symposium OS Canonical Edition) v2.3
