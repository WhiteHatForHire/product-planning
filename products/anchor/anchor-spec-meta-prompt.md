---
title: "Anchor Spec Meta Prompt"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Anchor OS/Anchor Spec Meta Prompt_.docx"
status: active
privacy: working
tags:
  - product
---

# Anchor Spec Meta Prompt

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
META_PROMPT.md — Anchor Edition v1.3

Send this to Charlie/Claude after generating any Anchor spec. Pairs with AUTONOMY_LAYER.md (Anchor edition) v1.3.

Changes from v1.2: GO instruction updated to reference session-scoped execution plan path (docs/run-notes/) per AUTONOMY_LAYER v1.3. AUTONOMY_LAYER version reference updated throughout.

The Prompt (paste verbatim after your spec, with AUTONOMY_LAYER.md content appended at the bottom)

Take the spec above and turn it into a fully autonomous Anchor build directive using AUTONOMY_LAYER.md (Anchor edition v1.3, repo root).

Apply these rules:

1. Run scope review first (AUTONOMY_LAYER.md section 0). If the spec exceeds reasonable autonomous executability, trim and document trims at the top of the directive. Common Anchor trims: defer Settings UI when schema is the load-bearing piece, split parallel surfaces into separate agent prompts, move "while I'm here" polish to deferred-issues.md upfront.

2. The stack is fixed. See AUTONOMY_LAYER.md section 0.1. Do not propose alternatives.

3. Open the directive with the header block from AUTONOMY_LAYER.md section 0.2. No line-count estimates, no phase-count estimates, no time estimates. The six fields are:

- Surfaces

- Production impact

- Council of Models

- Auto-merge

- Credentials

- Agent

4. Auto-merge eligibility — declare yes/no per AUTONOMY_LAYER.md section 0.2 eligibility rules. Yes only when: all acceptance criteria are AUTOMATED, zero HUMAN_REVIEW items block merge (post-merge validation is fine), no prompt fragment changes, no safety-adjacent changes, no UI copy changes, and CI status checks exist on the repo.

5. Specify all fallback content inline (section 1.6). No "agent invents the copy" patterns. Spec verbatim:

- Prompt fragment text (new program slugs, experience-level fragments, etc.)

- Approved-copy banks and forbidden-copy lists

- Crisis routing language

- User-facing error messages

- Default values for new stable_profile fields

- Migration backfill mappings (e.g., recovery_program → recovery_method enum mapping)

6. Split acceptance criteria into AUTOMATED and HUMAN_REVIEW (section 1.5).

- AUTOMATED: typecheck, unit tests, Playwright e2e, build success, programmatic assertion. Block phase gates.

- HUMAN_REVIEW: prompt voice review, visual review, production smoke against sobrietyanchor.com, behavioral judgment. Do not block phase gates. Log as MANUAL_PLAYTEST_REQUIRED.

7. State deployment posture per section 1.8:

- The agent does NOT merge manually. Auto-merge eligible: uses `gh pr merge --auto`. Not eligible: opens PR and stops.

- The agent does NOT deploy manually. CD handles main pushes.

- Migrations: code lands in PR. Production application is Marcus-only. State exact Neon HTTP SQL command in PR body.

- Fly secret changes: Marcus-only. State exact `flyctl secrets set` command in PR body.

- Vercel env changes: Marcus-only. State exact variable and location in PR body.

8. Mark "feel" and visual criteria as HUMAN_REVIEW. The agent cannot verify voice tone, visual correctness, behavioral appropriateness, or whether the experience-level differentiation is meaningful. Use AUTOMATED for counts, presence, structure, byte-equality, typecheck, e2e pass.

9. Make optional integrations fully deferrable (section 1.11). The system must run without them:

- OpenAI: AI generation paths have deterministic fallback (static base prompt, default fragment). Log on fallback. Do not crash.

- Resend: gate on EMAIL_OUTREACH_ENABLED. Test mode skips Resend entirely.

- Fly logs / Fly CLI: required only for CC Local diagnostic phases. CC Cloud directives must not depend on Fly CLI.

- GitHub MCP: required only for PR management. Direct git push is the fallback.

10. Use the Anchor self-repair playbook in AUTONOMY_LAYER.md section 2. Do not duplicate the 16 ANCHOR-N entries. Add directive-specific entries only when the directive introduces a new failure mode (new external API, new test infrastructure).

11. Atomic commits per concern (section 1.9). One concern per commit. Schema change + UI tweak + prompt edit is three commits, not one. No "while I'm here" cleanup bundled with feature work.

12. No silent failures (section 1.10). Any fallback path logs its trigger. Any try/catch that swallows an error logs the error before returning the fallback. Any function that can legitimately return empty must log when it does so for a non-trivial reason.

13. Production safety boundaries hold always (section 1.11):

- No autonomous production schema changes. Code lands; Marcus applies.

- No production data writes outside explicit migration scope.

- Safety prompts (crisis classifier, crisis response, safety override) and forbidden-copy lists require Council of Models review before merge.

- EMAIL_OUTREACH_ENABLED is not toggled without Marcus approval.

14. Parallel-agent split is first-class. If multiple independent surfaces exist (frontend + backend + migration, or multiple feature areas), propose the split explicitly:

- Which surfaces can be parallel CC Cloud branches (code-only, no credentials).

- Which surfaces require CC Local (Neon writes, OpenAI calls, Fly logs, email sends).

- Which surfaces require Council of Models review before merge.

- How the branches reconcile (which merges first, what depends on what).

- Shared coordination layer: AUTONOMOUS_RUN_LOG.md at repo root.

Marcus runs up to 6 agents concurrently. Use that when work allows.

15. Every phase MUST include all five of these in order (per AUTONOMY_LAYER.md section 3):

- PRE-FLIGHT: git status clean, prior phase commit exists, credentials preflight per section 0.5, baseline test counts recorded, build for affected workspaces succeeds. For api-server: lib/db and lib/api-zod build first (ANCHOR-1).

- SMOKE ASSERTIONS WRITTEN FIRST: Vitest unit tests or Playwright e2e or node:test. Run them. Expect red. Then implement.

- IMPLEMENTATION: until smoke is green. Self-heal per playbook. Defer after two attempts.

- HEALTH CHECK: full test suite for affected workspaces, build passes, MANUAL_PLAYTEST_REQUIRED items logged.

- COMMIT: per section 1.9 format.

Phases without smoke assertions are not phases. They are unverified changes.

16. The first phase that consumes the directive's design data must call out spec-reality reconciliation explicitly per AUTONOMY_LAYER.md section 1.13. Read actual repo state — test runner, test directory, interface fields, file paths, import patterns from peer files — before implementing against directive data. Log any SPEC_REALITY_DELTA findings to AUTONOMOUS_RUN_LOG.md. Adopt repo reality; the directive is a plan, the repo is source of truth.

17. MCP write safety per AUTONOMY_LAYER.md section 1.12. Direct git push is preferred for all file changes. MCP writes are last resort and must run the preflight checklist (target path, remote SHA, byte length, first/last 200 chars, explicit assertion of full-body content). Large append-only logs should never be rewritten via MCP — create a small per-session run note at docs/run-notes/session-YYYY-MM-DD-[context].md instead.

Generate the directive including:

- Header block (AUTONOMY_LAYER section 0.2 format)

- Role statement (one paragraph: what the agent is doing, on which surface, with what constraints)

- "Apply AUTONOMY_LAYER.md before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive."

- "Stack: see AUTONOMY_LAYER.md section 0.1."

- Deployment posture (PR-only stop, auto-merge yes/no with rationale, migration application instructions for Marcus if applicable)

- Full design data from the spec:

- Schema deltas (table, column, type, default, migration logic)

- File structure (new files, modified files, deleted files — full paths)

- Code snippets for non-obvious patterns

- Prompt fragments verbatim

- Test fixture data verbatim

- Default values for new fields verbatim

- Working files protocol (section 0.4): session-scoped plan file at docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md, AUTONOMOUS_RUN_LOG.md, BLOCKERS_FOR_MARCUS.md created and maintained throughout

- Phase plan: ordered phases, each with the five elements from rule 15. The first data-consuming phase explicitly includes spec-reality reconciliation as the first implementation step.

- Directive-specific self-repair entries (only if introducing failure modes not in the playbook)

- "Deferred-issues format: AUTONOMY_LAYER.md section 4"

- "BUILD_REPORT format: AUTONOMY_LAYER.md section 5"

- "Hard stops: AUTONOMY_LAYER.md section 6"

- GO instruction: first concrete action with branch name. Example: "Begin Phase A pre-flight per AUTONOMY_LAYER.md section 3. Credentials preflight scope: [list]. Cut branch from main: feat/[directive-slug]. Create docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md and AUTONOMOUS_RUN_LOG.md at repo root."

Voice:

- Direct, imperative, addressed to executing agent.

- No preamble. No pleasantries.

- Every instruction actionable.

- Reference AUTONOMY_LAYER.md by section number. Do not duplicate long passages.

- All agent-facing prompts and commands in fenced triple-backtick blocks. Never blockquotes.

[PASTE AUTONOMY_LAYER.md CONTENTS HERE]

How to use

Generate the spec in chat. Design conversation: schema deltas, prompt fragment content, copy banks, migration mappings, onboarding/settings changes, acceptance criteria. The spec is yours, in your voice, with all content verbatim.

After the spec is complete, paste this META_PROMPT verbatim, then paste the contents of AUTONOMY_LAYER.md at the bottom where indicated.

Charlie generates the directive — one Markdown file ready to fire at CC Local, CC Cloud, or both.

Review the directive. Verify: header block is six fields, fallback content is spec'd inline, parallel-agent split makes sense, every phase has the five elements (pre-flight, smoke-first, implementation, health check, commit), the first data-consuming phase calls out spec-reality reconciliation, auto-merge eligibility is correct.

Fire the directive at the appropriate agent(s).

The three files together

META_PROMPT.md — what you send to Charlie when generating a directive (this file)

AUTONOMY_LAYER.md — protocol Charlie applies and the agent obeys (paste at bottom of meta-prompt + lives in repo root)

The generated directive — what you fire at CC Local / CC Cloud / Codex

AUTONOMY_LAYER.md lives in the repo and every directive references it by section. META_PROMPT.md lives in docs/ and is your tool when starting any new feature.

What this file excludes

Stack choices. The self-repair playbook. Deferred-issues format. BUILD_REPORT format. Hard stop list. Personal operating context. Product strategy. All elsewhere.

This file generates directives. Nothing more.

End of META_PROMPT.md (Anchor edition) v1.3
