# AUTONOMY_LAYER.md — Symposium OS Canonical Edition v2.3

Reusable autonomous execution protocol for directed AI agent work on any codebase, in any language, against any platform.

Reference with: "Apply AUTONOMY_LAYER.md before executing this directive."

This is the canonical version that lives at `.symposium/AUTONOMY_LAYER.md` in the Symposium OS skills marketplace. Projects copy this file into their own `.symposium/` directory and fill in section 0.1 (project stack) and append to section 2.3 (project-specific repair entries). Strip nothing from the doctrine; the doctrine is the contract.

Changes from v1.4: Stripped all stack assumptions from 0.1 (now a true template). Removed personal and project-specific references throughout. Generalized command examples to operator-agnostic placeholders. Added 0.6 (Operator-Agent contract) clarifying who decides what. Doctrine sections, tier system, MCP write safety, spec-reality reconciliation, and stacked PR protocol all retained verbatim.

Changes from v2.0: Added §1.15 sequential merge maintenance sub-section. Formalizes the pattern of keeping a stacked chain clean across a sequential merge sequence without requiring a re-fired directive per merge.

Changes from v2.1: Clarified §3 EXECUTION to define docs-only smoke assertions (link/path/placeholder validation) so agents do not invent test code for documentation-only phases. Clarified §1.15 to make explicit that the agent does not halt between phases of a stacked chain; the operator merges all PRs in order after the full run completes.

---

## 0. SCOPE REVIEW

### 0.1 Stack reality (fill in per project — do not deviate once set)

Each project copying this file MUST fill in this block before firing any directive. The agent reads this section first and treats it as ground truth for the project.

```
Language(s):       [primary language(s) — e.g. TypeScript, Python, Go]
Frontend:          [framework + UI layer — or "none"]
Backend:           [framework + runtime — or "none"]
Database:          [system — or "none in V1"]
Auth:              [provider — or "none in V1"]
AI:                [SDK(s) used — or "none"]
Email / Comms:     [provider — or "none in V1"]
Repo layout:       [monorepo / single repo / submodules]
Package manager:   [npm / pnpm / yarn / pip / poetry / cargo / go mod / etc.]
Test runner:       [name + how it's invoked]
Build command:     [exact command]
Typecheck command: [exact command, or "n/a"]
Test command:      [exact command]
CI/CD:             [platform + deploy trigger]
Hosting:           [platform — production target]
Cron / schedulers: [if any]
```

### 0.2 Directive header format

Every directive opens with this block. No time estimates, no line estimates, no phase-count estimates.

```
Surfaces:          [files and areas this directive touches]
Production impact: none | data-only | schema-only | API change | UI change | prompt change | safety-adjacent
Council of Models: yes | no
Auto-merge:        yes | no
Credentials:       [list — or none]
Agent:             [agent identifier — e.g. local terminal agent, cloud agent, split]
```

**Auto-merge: yes** — agent registers automatic merge after opening PR. CI completes, merge fires, deploy fires. No operator touch required for the merge itself.

**Auto-merge: no** — agent opens PR and stops. Operator reviews and merges.

Auto-merge eligibility (all must be true):
- All acceptance criteria are AUTOMATED
- Zero HUMAN_REVIEW items gate the merge (post-merge validation is fine)
- No prompt fragment changes
- No safety-adjacent or copy changes
- CI status checks exist on the repo

### 0.3 Markdown formatting conventions

- Code blocks: file paths, commands, code, data structures, agent prompts
- Lists: sequential steps, enumerables, file structures
- Prose: explanations, decisions, rationale
- Tables: comparisons, schemas, phase outcomes
- Agent prompts inside any document: fenced triple-backtick blocks only. Never blockquotes.

### 0.4 Working files

Every autonomous run produces this audit trail. Paths are conventions; if the project has a different docs location, mirror the convention there.

- `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md` — phases and goals (session-scoped path eliminates merge conflicts at repo root)
- `AUTONOMOUS_RUN_LOG.md` — append-only log: commit SHAs, phase outcomes, decisions, SPEC_REALITY_DELTA entries. Prefer appending to existing file. If conflict risk is high across parallel agents, create `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-run-log.md` instead.
- `BLOCKERS_FOR_OPERATOR.md` — items requiring human approval the agent cannot resolve. Keep at root. On merge conflict, accept incoming.
- `docs/deferred-issues.md` — section 4 format.

Do NOT create `ISSUE_EXECUTION_PLAN.md` or any other singleton plan file at repo root. Use the session-scoped path above. Singleton plan files at root produce merge conflicts in any parallel-agent workflow.

### 0.5 Credentials preflight

Run before any implementation. If anything is missing, log to `BLOCKERS_FOR_OPERATOR.md` immediately and stop the relevant phase.

```
[version control auth check]      # always — e.g. gh auth status, glab auth status
git status                         # always — must be clean
[install command from 0.1]         # always — frozen lockfile preferred
```

Plus any project-specific credential checks declared in the directive header.

Cloud agents without filesystem access to operator secrets: declare no credentials in run log. Restrict to code-only work. Escalate anything needing credentials to `BLOCKERS_FOR_OPERATOR.md`.

### 0.6 Operator-Agent contract

The operator owns: scope, architectural decisions outside the directive's stated bounds, safety-adjacent content, production credentials, production deploys requiring human authorization, and final review.

The agent owns: execution within the directive, self-repair within the playbook (section 2), spec-reality reconciliation, deferral decisions, atomic commits, working files, and the build report.

The directive is the contract between them. When the directive is ambiguous, the agent defers per section 1.7 rather than expanding scope.

---

## 1. AUTONOMY DOCTRINE

### TIER 1 — SELF-HEAL
Apply the relevant playbook entry. Two attempts maximum. If self-heal succeeds, continue.

### TIER 2 — DEFER AND CONTINUE
After two failed attempts:
- Log to `docs/deferred-issues.md` with the format in section 4
- Stub or skip so the rest of the system works (e.g. `it.skip("DEFERRED: [reason]")`, equivalent skip in other test runners, feature flag off)
- Commit current state with deferred note
- Continue to the next sub-step

### TIER 3 — HARD STOP
Only for the conditions in section 6. Before stopping:

```
git add -A
git commit -m "halt([phase]): [reason with diagnosis]"
git checkout -b halt-$(date +%Y-%m-%d-%H%M)
git push origin halt-$(date +%Y-%m-%d-%H%M)
```

Generate `BUILD_REPORT.md` with HALTED status. Stop.

### NEVER

- Ask for human input mid-build outside `BLOCKERS_FOR_OPERATOR.md`
- Wait between phases
- Stop for "I'm not sure" — defer per Tier 2 and continue
- Commit broken code without marking it deferred
- Skip `deferred-issues.md` or `BUILD_REPORT.md`
- Expand a phase's scope mid-build
- Merge PRs manually when auto-merge is registered
- Apply production migrations without explicit directive authorization
- Touch production data outside the directive's authorized scope
- Modify safety-adjacent prompts or copy without Council authorization in the directive
- Force-push or rewrite branches outside the rebase rules in section 1.15

### 1.5 Acceptance criteria split

Every directive must declare its acceptance criteria as one of two types:

- **AUTOMATED**: typecheck, unit tests, e2e tests, build success, programmatic assertions. These block phase gates.
- **HUMAN_REVIEW**: prompt voice, visual review, production smoke, behavioral judgment, accessibility tone. These do NOT block phase gates. Log as `MANUAL_PLAYTEST_REQUIRED` in deferred-issues.md.

A directive with HUMAN_REVIEW gates blocking the build is malformed.

### 1.6 Fallback content must be specified

The agent does not invent:
- Prompt fragment text
- Approved-copy banks or forbidden-copy lists
- Crisis routing language or safety-adjacent strings
- User-facing error messages
- Default values for new schema fields
- Migration backfill mappings
- Brand voice, tone, or persona language

Spec this content verbatim in the directive. If the directive does not specify it, halt the relevant sub-step and log to `BLOCKERS_FOR_OPERATOR.md`.

### 1.7 Scope discipline

If implementation grows beyond a phase's stated goal: halt the expansion, defer the additional work to a future phase or `deferred-issues.md`, continue with the current phase as scoped. Scope creep is a deferrable issue, not a license to expand.

### 1.8 Deployment

- Frontend changes auto-deploy to production hosting on merge when the hosting platform is wired for it.
- Backend changes auto-deploy on merge when relevant files are touched.
- Migrations: code lands in PR. Production application is operator-only. State the exact command in the PR body.
- Production secrets: operator-only. State exact command and location in PR body.
- Production environment variable changes: operator-only. State exact variable, value (or location to fetch it), and target environment in PR body.

**Auto-merge: yes — END OF DIRECTIVE steps:**
```
[version control PR open command] --title "[type]: [title]" --body "$(cat BUILD_REPORT.md)"
[version control PR merge command] --auto --squash --delete-branch
```
Log: AUTO-MERGE REGISTERED. Stop.

**Auto-merge: no — END OF DIRECTIVE steps:**
```
[version control PR open command] --title "[type]: [title]" --body "$(cat BUILD_REPORT.md)"
```
Log PR URL. Stop. Operator reviews and merges.

### 1.9 Atomic commits

One concern per commit. No "while I'm here" bundling.

```
type(scope): [what changed]

[body — optional, for non-trivial commits]

Phase: [name]
Deferrals: N
Tests: P passing, S skipped, F failing
```

### 1.10 No silent failures

- Every fallback path logs its trigger at the layer where it fires
- Every try/catch logs before returning a fallback value
- No function returns `""`, `null`, `None`, or equivalent as a non-trivial fallback without logging why
- Every external service call that can fail has an observable failure mode in logs

### 1.11 Production safety boundaries

- Production database: read-only unless the directive explicitly authorizes writes
- Real user data: never log, exfiltrate, or include in test fixtures
- Safety-adjacent prompts and forbidden-copy lists: Council of Models review required before merge
- Production feature flags: operator-only

### 1.12 MCP write safety

The destructive failure mode of MCP (Model Context Protocol) writes: passing a literal placeholder string instead of full file content silently overwrites the remote file. This has happened. Preferred path order:

1. **Direct git push** — best. Full history, atomic, normal review.
2. **MCP commit of code files** — when direct push is blocked.
3. **MCP commit of large append-only logs** — last resort. Prefer creating small per-session run notes at `docs/run-notes/session-YYYY-MM-DD-[context].md` and referencing them later.

Before any MCP write, the agent must verify and log:
- Target path
- Current remote SHA (retrieved fresh, not cached)
- Byte length of outgoing content
- First 200 characters of outgoing content
- Last 200 characters of outgoing content
- Explicit assertion: outgoing content is the full file body, not a placeholder, not a diff

Hard stop the MCP write if any of:
- Outgoing byte length is under 25% of remote size for files over 5KB
- Outgoing content matches placeholder patterns (`[paste content here]`, `<file body>`, `// TODO`, single-line content for a known multi-section file)
- Remote SHA cannot be verified

### 1.13 Spec-reality reconciliation

Before implementing the design data in any directive, verify it against actual repo state. Do this once at the start of the first phase where the directive's data is consumed.

Check at minimum:
- Test runner — read package manifest scripts and an existing peer test file
- Test directory — confirm where the runner scans
- Interface fields — read the actual type definitions or schemas being consumed
- File paths — confirm proposed file locations match repo conventions
- Import patterns — match the pattern used by existing peer files

When directive data conflicts with repo reality, log a `SPEC_REALITY_DELTA` entry in `AUTONOMOUS_RUN_LOG.md`:

```
SPEC_REALITY_DELTA — [phase name]
Directive said: [exact text or assumption]
Repo reality:   [what the code/config actually has]
Adopted:        [what the agent used — always repo reality]
Reason:         [one-line justification]
```

The directive is a plan. The repo is the source of truth.

### 1.14 Open PR check before any rebase or merge operation

Before executing any rebase, merge, or branch-cutting operation in a project with active PRs, run:

```
[version control PR list command, state=open]
git log --oneline origin/main..HEAD
```

Verify the actual state of the remote. Do not assume branch names from the directive still exist or that the main branch hasn't moved. Log findings before proceeding.

### 1.15 Stacked PR conflict resolution protocol

Applies whenever the agent is resolving merge or rebase conflicts across a stacked PR chain.

**Pre-rebase: detect squash-merge SHA drift**

When earlier branches in a stacked chain have been squash-merged into the base, plain rebase will attempt to replay already-landed commits (new SHA, same content) and produce false conflicts on every line. Detect this before rebasing:

```
git log --oneline <branch> ^origin/main
```

If commits from prior stack phases appear in this output, the base has shifted via squash-merge. Use `--onto` instead:

```
git rebase --onto <new-base> <last-squashed-commit-sha> <branch>
```

This surgically replays only the branch's unique commits onto the new base. Log as `SPEC_REALITY_DELTA` with the substitution noted.

After any pull that includes a squash-merge, run the install command from section 0.1 with frozen lockfile flags before typecheck or build. Dependencies added in squashed PRs will not be in local `node_modules` (or equivalent) until reinstalled.

**Conflict resolution tiers**

Tier 1 — Accept incoming without reading (these files are safe by convention):
- `AUTONOMOUS_RUN_LOG.md`
- `docs/run-notes/*`
- `FINAL_REPORT.md`
- `BLOCKERS_FOR_OPERATOR.md`
- Any file modified only by the branch being rebased, with no overlapping changes on the base

Tier 2 — Read both sides before resolving:
- Any router or page entry file
- Any shared component or shared module touched by multiple phases
- Global styling files (CSS, theme, design tokens)
- Configuration files (build config, framework config, language config)
- Any test file
- Dependency manifests and lockfiles (keep all dependencies from both sides)

Resolution rule for Tier 2: the correct version preserves ALL integrations from earlier phases AND adds the current phase's changes. Neither side is categorically correct. Read both, produce a merged result, confirm it compiles and tests pass.

Tier 3 — Halt and surface:
- Any conflict where accepting either side would silently drop a feature, integration, or import from a prior phase
- Write to `BLOCKERS_FOR_OPERATOR.md` showing both versions and the specific semantic risk
- Do not guess

**"Accept incoming" is NOT a blanket rule.** It applies only to Tier 1 files. For all other files it means: start from the incoming version and verify it does not silently drop prior work. These are different operations.

**Post-rebase verification (mandatory before push)**

After every rebase, before pushing:

```
[typecheck command]  # must pass
[build command]      # must pass
[test command]       # must pass at the same rate as before rebase
```

If any check fails after conflict resolution, the resolution was wrong. Do not push. Fix or escalate to Tier 3.

**Log format for rebase operations**

In `AUTONOMOUS_RUN_LOG.md`:

```
REBASE — [branch name]
Technique:         --onto | plain rebase
Old HEAD:          [SHA]
New HEAD:          [SHA]
Conflicts:         [file list or "none"]
Resolution:        [Tier 1 / Tier 2 / Tier 3 per file]
Typecheck:         clean | [error]
Build:             clean | [error]
Tests:             [N passing, N skipped, N failing]
```

**Sequential merge maintenance**

After any PR in a stacked chain merges to main, every remaining branch in the chain has stale base SHA drift. The agent does not need to be re-fired with a new directive each time. When the agent is operating on a stacked chain and a PR merges mid-run, the agent automatically:

1. Refetches origin and re-detects open PRs in the chain
2. For each remaining open branch, runs the squash-merge SHA drift check above
3. Applies `--onto` rebase against the new main HEAD
4. Resolves conflicts per the Tier 1/2/3 rules above
5. Pushes with `--force-with-lease`
6. Logs each rebase per the rebase log format above

The agent treats this as a single continuous operation, not as multiple separate directives. The operator authorizes merges; the agent maintains the chain.

**No halt between phases of a stacked chain.** The agent opens each PR in the chain and immediately continues to the next phase. It does not wait for the operator to merge between phases. The operator merges all PRs in order after the full run completes. This applies whether `Auto-merge: yes` or `Auto-merge: no`:

- `Auto-merge: yes` — agent opens each PR with auto-merge registered, proceeds to the next phase without waiting for CI to clear.
- `Auto-merge: no` — agent opens each PR, logs the URL, and proceeds to the next phase without waiting for operator review. The operator reviews and merges all PRs in chain order after the full run completes.

Directives that include "operator merges each phase before the next begins" language are malformed. The `generate-directive` skill will not produce such directives. If an older directive contains this language, the agent ignores it in favor of the §1.15 canonical pattern.

If the operator explicitly needs per-phase review gating (e.g., the work is high-risk and each phase must be human-validated before the next), this is not a stacked chain — it is a sequence of separate directives, one per phase, each fired after the prior PR merges.

---

## 2. SELF-REPAIR PLAYBOOK

Apply in order: symptom → attempt 1 → attempt 2 → defer.

### 2.1 Generic entries

These apply across any project and any stack.

- **GENERIC-1 — Specific test fails**
  - A1: Re-read implementation and assertion. Fix obvious bug.
  - A2: Check if assertion is wrong. Update if implementation matches intent.
  - DEFER: Skip the test with a "DEFERRED:" prefix. Log. Continue.

- **GENERIC-2 — Feature behavior wrong but system runs**
  - A1: Re-read spec. Trace. Fix.
  - A2: Simplify to known-working baseline.
  - DEFER: Stub the behavior. Log. Continue.

- **GENERIC-3 — Module not found / import error**
  - A1: Verify path (case-sensitive). Check export name. Check language-specific module resolution config.
  - A2: Create stub file if missing.
  - DEFER: Stub with typed dummy returning safe defaults. Log.

- **GENERIC-9 — Build fails**
  - A1: Identify offending file. Check syntax.
  - A2: Run a diff against the last working commit. Revert suspicious chunks.
  - DEFER: HARD STOP.

- **GENERIC-10 — Dependency install fails**
  - A1: Run install with frozen lockfile flag. Check lockfile drift if frozen fails.
  - A2: Remove local dependency directory, reinstall clean. Commit any updated lockfile separately.
  - DEFER: HARD STOP.

- **GENERIC-11 — External service fails**
  - A1: Verify credentials, request format, response parsing. Retry once with backoff.
  - A2: Deterministic local fallback. Make the service optional.
  - DEFER: Disable dependent feature. Log MEDIUM or HIGH. System must work without it.

- **GENERIC-12 — Stale dependencies after squash-merge pull**
  - Symptom: build or typecheck fails with "Cannot find module X" (or language equivalent) after pulling main, where X was added in a recently squashed PR.
  - A1: Run install with frozen lockfile. The lockfile is correct; local dependency directory is stale.
  - A2: Delete the local dependency directory, reinstall clean.
  - DEFER: HARD STOP if install itself fails (escalates to GENERIC-10).

### 2.2 Working tree repair

- **WORKTREE-1 — Dirty working tree at preflight**
  - A1: Check what is uncommitted. If it's a known scratch file (e.g. `.env.local`, log files, build artifacts), confirm it's gitignored or stash it.
  - A2: If unexpected, stash with a clear message. Surface in run log.
  - DEFER: HARD STOP if there is uncommitted work that could be lost.

### 2.3 Project-specific entries

Each project copying this file appends its own repair entries here as failure modes are discovered. Use the convention `PROJECT-1`, `PROJECT-2`, etc., or a clearer namespace like `WEB-1`, `API-1`. Do not modify the generic entries.

Append below this line per project.

---

## 3. PHASE EXECUTION PROTOCOL

### PRE-FLIGHT
```
git status                          # must be clean
git log --oneline -1                # previous phase commit exists (if not the first phase)
[install command]                   # with frozen lockfile flag
```

Build affected workspaces. Record baseline test counts.

First phase that consumes directive design data: run spec-reality reconciliation per section 1.13.

If the project has active stacked PRs: run section 1.14 open PR check.

### EXECUTION
Write smoke assertions first. Run them. Expect red. Implement until green.

**Smoke assertions for docs-only or template-only phases**: when a phase touches only documentation, templates, scaffold files, or markdown content — not executable code — invented test code is not appropriate. The smoke check for these phases is validation, not assertion:

- All referenced internal file paths exist
- All cross-references and section anchors resolve
- No `[placeholder]` or `[TBD]` markers remain unfilled (unless the directive explicitly authorizes them)
- Markdown parses without syntax errors
- Code-fenced blocks declare their language
- Front-matter (if present) parses

Run these checks before treating the docs-only phase as green. Do not invent unit tests for files that have no runtime.

Failing test: GENERIC-1, 2 attempts, then defer.
Failing feature: GENERIC-2, 2 attempts, stub, defer.

Checkpoint commits after every sub-step leaving the system in a working state:
```
chore([phase]-checkpoint): [what completed]
```

### HEALTH CHECK
Full test suite for affected workspaces. Count passing / skipped / failing.

Verify expected files exist.

Build passes.

Prompt or AI changes → `MANUAL_PLAYTEST_REQUIRED`.
UI changes → `MANUAL_PLAYTEST_REQUIRED`.
Log all to `deferred-issues.md`.

### COMMIT
Per section 1.9 format.

### REPORT UPDATE
Append to `docs/deferred-issues.md`. Append to `AUTONOMOUS_RUN_LOG.md` with timestamp, phase name, SHA, counts. If any `SPEC_REALITY_DELTA` entries surfaced this phase, log them here. If any rebase happened this phase, log per section 1.15 format.

### TRANSITION
Immediately begin next phase. No pause. No human prompt.

### END OF DIRECTIVE
Generate `BUILD_REPORT.md` (section 5).
Commit working files and report:
```
docs(directive): BUILD_REPORT and working files
```
Push branch. Direct git push preferred. If blocked, MCP write of small files only — apply section 1.12 preflight.
Open PR. If `Auto-merge: yes`, register auto-merge. If no, log URL and stop.

---

## 4. DEFERRED-ISSUES.MD FORMAT

```markdown
# Deferred Issues — [Directive Name]

## Severity
- BLOCKER | HIGH | MEDIUM | LOW | MANUAL_PLAYTEST_REQUIRED | COUNCIL_REVIEW_REQUIRED

---

## Phase [name]

### [SEVERITY] [Title]

**What failed:** [description]
**Attempts:** 1. [result] 2. [result]
**Current state:** [how stubbed or skipped]
**Reproduction:** [steps + commit SHA]
**Recommended fix:** [concrete next move]
**Continued with:** [what shipped instead]
```

---

## 5. BUILD_REPORT.MD FORMAT

```markdown
# [Directive Name] — Build Report

Generated: [ISO timestamp]
Branch: [name]
Base SHA: [SHA on main when cut]
Final commit: [SHA]
Production impact: [level]
Auto-merge: registered | pending operator | HALTED

## Summary
[One paragraph]

## Phase Outcomes
| Phase | Status | Passing | Deferrals | SHA |
|---|---|---|---|---|

## Spec-Reality Deltas
[List SPEC_REALITY_DELTA entries from AUTONOMOUS_RUN_LOG.md, if any]

## Rebase Operations
[List REBASE entries from AUTONOMOUS_RUN_LOG.md, if any]

## Deferred by Severity
- BLOCKER: N — [titles]
- HIGH: N | MEDIUM: N | LOW: N
- MANUAL_PLAYTEST_REQUIRED: N — [titles]
- COUNCIL_REVIEW_REQUIRED: N — [titles]

## Test Status
| Workspace | Total | Passing | Skipped | Failing |
|---|---|---|---|---|

## Manual Verification Required
[List]

## Council Review Required
[List with exact prompt for operator to run across multiple models]

## Production Application Pending
[Migrations, secrets, env vars — exact commands]

## Next Actions
1. [highest priority]
2. [next]
```

---

## 6. HARD STOP CONDITIONS

Halt ONLY for:

- Dependency install fails after GENERIC-10 attempts exhausted
- Build fails after GENERIC-9 attempts exhausted
- Test runner itself crashes (not test failures — runner failure)
- Git operations fail after credential preflight succeeded
- Filesystem errors (permission, disk space, etc.)
- Production deploy fails and production is degraded
- Foreign dirty working tree after WORKTREE-1 attempts exhausted
- Production data accidentally modified
- Safety-adjacent prompt change attempted without Council authorization in directive
- MCP write recovery fails after section 1.12 preflight + recovery attempts
- Tier 3 stacked PR conflict that cannot be safely resolved

---

## 7. META-PROMPT

See `META_PROMPT.md` (sibling file in `.symposium/`). Pairs with this AUTONOMY_LAYER. Send to the directing AI after generating any project spec to convert that spec into a runnable directive.

---

## 8. HOW TO USE

- Initializing a new project: copy `.symposium/AUTONOMY_LAYER.md` from the Symposium OS canonical location into the project. Fill in section 0.1. Do not modify anything else on first copy.
- Generating a directive: spec in chat → paste meta-prompt from `META_PROMPT.md` → directing AI produces directive → operator reviews → fire at the chosen agent.
- Embedding in agent runtime: `AUTONOMY_LAYER.md` at `.symposium/AUTONOMY_LAYER.md`. Directive opens with "Apply AUTONOMY_LAYER.md before executing."
- Parallel agents: same layer file, coordination via working files (section 0.4).
- Updating this file: PR with `chore(autonomy): v[X.Y] — [what changed]`. Tick version.
- Project-specific learnings: append to section 2.3 in the project copy. Promote to canonical only if the pattern recurs across three or more projects.

---

## 9. WHAT THIS FILE EXCLUDES

Personal operating context. Product strategy. Feature acceptance criteria. Prompt content. Safety copy. Project-specific tooling.

This file is execution protocol only. The directive carries the project intent. The stack reality lives in section 0.1. Project-specific repair entries live in section 2.3.

End of AUTONOMY_LAYER.md (Symposium OS Canonical Edition) v2.3
