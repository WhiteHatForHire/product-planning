# META_PROMPT.md — Symposium Generic Edition v1.3

Send to Charlie/Claude after generating any project spec. Pairs with `AUTONOMY_LAYER.md` (Symposium Generic Edition v1.3).

Changes from Anchor edition: project-specific examples removed; references to Anchor-specific patterns generalized; the prompt below works for any Symposium project once `AUTONOMY_LAYER.md` section 0.1 is filled in.

## The Prompt (paste verbatim after your spec, with AUTONOMY_LAYER.md content appended at the bottom)

Take the spec above and turn it into a fully autonomous build directive using `AUTONOMY_LAYER.md` (Symposium Generic Edition v1.3, at `.symposium/AUTONOMY_LAYER.md`).

Apply these rules:

1. Run scope review first (AUTONOMY_LAYER.md section 0). If the spec exceeds reasonable autonomous executability, trim and document trims at the top of the directive.

2. The stack is fixed. See `AUTONOMY_LAYER.md` section 0.1 (filled in for this project). Do not propose alternatives.

3. Open the directive with the header block from `AUTONOMY_LAYER.md` section 0.2. No line-count estimates, no phase-count estimates, no time estimates.

4. Auto-merge eligibility — declare yes/no per `AUTONOMY_LAYER.md` section 0.2 eligibility rules.

5. Specify all fallback content inline (section 1.6). No "agent invents the copy" patterns. Spec verbatim:
   - Prompt fragment text
   - Approved-copy banks and forbidden-copy lists
   - User-facing error messages
   - Default values for new schema fields
   - Migration backfill mappings

6. Split acceptance criteria into AUTOMATED and HUMAN_REVIEW (section 1.5).

7. State deployment posture per section 1.8.

8. Mark "feel" and visual criteria as HUMAN_REVIEW. The agent cannot verify voice, visual correctness, or behavioral appropriateness.

9. Make optional integrations fully deferrable (section 1.11). The system must run without them.

10. Use the self-repair playbook in `AUTONOMY_LAYER.md` section 2. Add project-specific entries only when the directive introduces a new failure mode.

11. Atomic commits per concern (section 1.9). One concern per commit.

12. No silent failures (section 1.10).

13. Production safety boundaries hold always (section 1.11).

14. Parallel-agent split is first-class. If multiple independent surfaces exist, propose the split explicitly:
    - Which surfaces can be parallel CC Cloud branches (code-only, no credentials).
    - Which surfaces require CC Local (DB writes, external API calls, deploy ops).
    - Which surfaces require Council of Models review before merge.
    - How the branches reconcile (which merges first, what depends on what).
    - Shared coordination layer: `AUTONOMOUS_RUN_LOG.md` at repo root.

    Marcus runs up to 6 agents concurrently. Use that when work allows.

15. Every phase MUST include all five of these in order (per `AUTONOMY_LAYER.md` section 3):
    - PRE-FLIGHT
    - SMOKE ASSERTIONS WRITTEN FIRST
    - IMPLEMENTATION
    - HEALTH CHECK
    - COMMIT

    Phases without smoke assertions are not phases. They are unverified changes.

16. The first phase that consumes the directive's design data must call out spec-reality reconciliation explicitly per `AUTONOMY_LAYER.md` section 1.13.

17. MCP write safety per `AUTONOMY_LAYER.md` section 1.12. Direct git push is preferred.

Generate the directive including:

- Header block (`AUTONOMY_LAYER.md` section 0.2 format)
- Role statement (one paragraph)
- "Apply `AUTONOMY_LAYER.md` before executing."
- "Stack: see `AUTONOMY_LAYER.md` section 0.1."
- Deployment posture (PR-only stop, auto-merge yes/no with rationale, migration application instructions for Marcus if applicable)
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

## How to use

1. Generate the spec in chat. Design conversation: schema, prompts, copy, acceptance criteria.
2. Paste this META_PROMPT verbatim, then paste `AUTONOMY_LAYER.md` contents at the bottom where indicated.
3. Charlie generates the directive — one Markdown file.
4. Review the directive. Verify header block, fallback content inline, parallel-agent split, every phase has the five elements, first data-consuming phase calls out spec-reality reconciliation, auto-merge eligibility correct.
5. Fire at CC Local, CC Cloud, or both.

## The three files together

- `META_PROMPT.md` — what you send to Charlie when generating a directive (this file)
- `AUTONOMY_LAYER.md` — protocol Charlie applies and the agent obeys
- The generated directive — what you fire at CC Local / CC Cloud / Codex

End of META_PROMPT.md (Symposium Generic Edition) v1.3
