# AUTONOMY_LAYER.md — Symposium Generic Edition v1.3

Reusable autonomous execution protocol for any Symposium Studios project.
Reference with: "Apply AUTONOMY_LAYER.md before executing this directive."

This is the generic baseline. Project-specific entries live in section 0.1 (stack) and section 2 (repair playbook). Strip nothing from this file when copying into a new project; instead fill in 0.1 and append project-specific repair entries to 2.

Changes from Anchor edition v1.3: Anchor-specific stack and playbook entries removed; section 0.1 is now a fill-in template; section 2 retains generic GENERIC-N entries only; project-specific repair entries are appended per project.

## 0. SCOPE REVIEW

### 0.1 Stack reality (fill in per project — do not deviate once set)

```
Frontend:   [framework + language + UI library + hosting]
Backend:    [framework + language + hosting]
Database:   [provider + access pattern + constraints]
Auth:       [provider + scope]
AI:         [provider + client pattern]
Email:      [provider + feature flag if any]
Monorepo:   [pnpm workspaces | single repo | other]
CI/CD:      [auto-deploy rules per target]
```

### 0.2 Directive header format

Every directive opens with this block. No estimates for lines, phases, or time.

```
Surfaces:          [files and areas this directive touches]
Production impact: none | schema-only | API change | UI change | prompt change
Council of Models: yes | no
Auto-merge:        yes | no
Credentials:       [list — or none]
Agent:             CC Local | CC Cloud | split
```

Auto-merge: yes — agent calls `gh pr merge --auto --squash --delete-branch` after opening PR. GitHub merges when CI passes. CD fires. No human touch.

Auto-merge: no — agent opens PR and stops. Marcus reviews and merges.

Auto-merge eligibility (all must be true):
- All acceptance criteria are AUTOMATED
- Zero HUMAN_REVIEW items gate the merge (post-merge validation is fine)
- No prompt fragment changes, no safety-adjacent changes, no UI copy changes
- CI status checks exist on the repo

### 0.3 Markdown formatting

- Code blocks: file paths, commands, code, data structures, agent prompts
- Lists: sequential steps, enumerables, file structures
- Prose: explanations, decisions, rationale
- Tables: comparisons, schemas, phase outcomes
- Agent prompts: fenced triple-backtick blocks only. Never blockquotes.

### 0.4 Working files

Created by every autonomous run. The audit trail.

- `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md` — phases and goals (session-scoped; eliminates merge conflicts at root)
- `AUTONOMOUS_RUN_LOG.md` — append-only log with commit SHAs, phase outcomes, decisions. Prefer appending to existing file. If conflict risk is high, create `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-run-log.md` instead.
- `BLOCKERS_FOR_MARCUS.md` — items requiring human approval the agent cannot resolve. Keep at root; on merge conflict, accept incoming.
- `docs/deferred-issues.md` — section 4 format

Do NOT create `ISSUE_EXECUTION_PLAN.md` at repo root. Use the session-scoped plan path above.

### 0.5 Credentials preflight

Run before any implementation. If anything is missing, log to `BLOCKERS_FOR_MARCUS.md` immediately.

```
gh auth status                      # always
git status                          # always — must be clean
pnpm install --frozen-lockfile      # always (or npm ci / yarn install --frozen-lockfile)
```

Plus any project-specific credential checks declared in the directive header.

CC Cloud agents: declare no credentials in run log. Restrict to code-only work. Escalate anything needing credentials to `BLOCKERS_FOR_MARCUS.md`.

## 1. AUTONOMY DOCTRINE

### TIER 1 — SELF-HEAL
Apply the relevant playbook entry. Two attempts max. If self-heal succeeds, continue.

### TIER 2 — DEFER AND CONTINUE
After two failed attempts:
- Log to `docs/deferred-issues.md`
- Stub or skip so the rest of the system works (`it.skip("DEFERRED: [reason]")` or Playwright `test.skip()`)
- Commit current state with deferred note
- Continue

### TIER 3 — HARD STOP
Only for conditions in Section 6. Before stopping:

```
git add -A
git commit -m "halt([phase]): [reason with diagnosis]"
git checkout -b halt-$(date +%Y-%m-%d-%H%M)
git push origin halt-$(date +%Y-%m-%d-%H%M)
```

Generate `BUILD_REPORT.md` with HALTED status. Stop.

### NEVER

- Ask for human input mid-build outside `BLOCKERS_FOR_MARCUS.md`
- Wait between phases
- Stop for "I'm not sure" — defer and continue
- Commit broken code without marking deferred
- Skip `deferred-issues.md` or `BUILD_REPORT.md`
- Expand a phase's scope mid-build
- Merge PRs manually (use `--auto` for eligible directives)
- Apply migrations to production without directive authorization
- Touch production data outside explicit migration scope
- Modify safety-relevant prompts without Council authorization in the directive

### 1.5 Acceptance criteria split

Every directive must declare:
- **AUTOMATED**: typecheck, unit tests, e2e tests, build success, programmatic assertion. Block phase gates.
- **HUMAN_REVIEW**: prompt voice, visual review, production smoke, behavioral judgment. Do not block phase gates. Log as `MANUAL_PLAYTEST_REQUIRED`.

### 1.6 Fallback content must be specified

The agent does not invent:
- Prompt fragment text
- Approved-copy banks or forbidden-copy lists
- Crisis routing language (when applicable)
- User-facing error messages
- Default values for new schema fields
- Migration backfill mappings

Spec the content verbatim in the directive.

### 1.7 Scope discipline

If implementation grows beyond a phase's stated goal: halt the expansion, defer to a future phase or `deferred-issues.md`, continue with current phase as scoped. Scope creep is a deferrable issue, not a license to expand.

### 1.8 Deployment

- Frontend changes auto-deploy to production hosting on merge.
- Backend changes auto-deploy to production hosting on merge when relevant files are touched.
- Migrations: code lands in PR. Production application is Marcus-only. State the exact command in the PR body.
- Production secrets: Marcus-only. State exact command in PR body.
- Production env changes: Marcus-only. State exact variable and location in PR body.

Auto-merge: yes — END OF DIRECTIVE steps:
```
gh pr create --title "[type]: [title]" --body "$(cat BUILD_REPORT.md)"
gh pr merge --auto --squash --delete-branch
```
Log: AUTO-MERGE REGISTERED. Stop.

Auto-merge: no — END OF DIRECTIVE steps:
```
gh pr create --title "[type]: [title]" --body "$(cat BUILD_REPORT.md)"
```
Log PR URL. Stop. Marcus reviews and merges.

### 1.9 Atomic commits

One concern per commit. No "while I'm here" bundling.

```
type(scope): [what changed]

[body]

Phase: [name]
Deferrals: N
Tests: P passing, S skipped, F failing
```

### 1.10 No silent failures

- Every fallback path logs its trigger at the layer where it fires
- Every try/catch logs before returning a fallback
- No function returns `""` or `null` as a non-trivial fallback without logging why
- Every external call that can fail has an observable failure mode

### 1.11 Production safety boundaries

- Production database: read-only unless directive explicitly authorizes writes
- Real user data: never log, exfiltrate, or include in test fixtures
- Safety prompts and forbidden-copy lists: Council of Models review required before merge
- Production feature flags: Marcus-only

### 1.12 MCP write safety

Destructive MCP write failure mode: passing a literal placeholder instead of full file content silently overwrites the remote file. Preferred path order:

1. **Direct git push** — best. Full history, atomic, normal review.
2. **MCP commit of code files** — when direct push is blocked.
3. **MCP commit of large append-only logs** — last resort. Prefer creating small per-session run notes at `docs/run-notes/session-YYYY-MM-DD-[context].md` and referencing them later.

Before any MCP write, the agent must verify and log:
- Target path
- Current remote SHA (retrieved fresh, not cached)
- Byte length of outgoing content
- First 200 characters of outgoing content
- Last 200 characters of outgoing content
- Explicit assertion: outgoing content is full file body, not placeholder, not diff

Hard stop the MCP write if any of:
- Outgoing byte length is under 25% of remote size for files over 5KB
- Outgoing content matches placeholder patterns (`[paste content here]`, `<file body>`, single-line content for known multi-section file)
- Remote SHA cannot be verified

### 1.13 Spec-reality reconciliation

Before implementing the design data in any directive, verify it against actual repo state. Do this once at the start of the first phase where the directive's data is consumed.

Check at minimum:
- Test runner — read `package.json` scripts and an existing peer test file
- Test directory — confirm where the runner scans
- Interface fields — read the actual TypeScript interfaces being consumed
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

The directive is a plan; the repo is the source of truth.

## 2. SELF-REPAIR PLAYBOOK

Apply in order: symptom → attempt 1 → attempt 2 → defer.

### Generic

- **GENERIC-1 — Specific test fails**
  - A1: Re-read implementation and assertion. Fix obvious bug.
  - A2: Check if assertion is wrong. Update if implementation matches intent.
  - DEFER: `it.skip` / `test.skip`. Log. Continue.

- **GENERIC-2 — Feature behavior wrong but system runs**
  - A1: Re-read spec. Trace. Fix.
  - A2: Simplify to known-working baseline.
  - DEFER: Stub behavior. Log. Continue.

- **GENERIC-3 — Module not found / import error**
  - A1: Verify path (case-sensitive). Check export name. Check `tsconfig.json` paths.
  - A2: Create stub if file missing.
  - DEFER: Stub with typed dummy returning safe defaults. Log.

- **GENERIC-9 — Build fails**
  - A1: Identify offending file. Check syntax.
  - A2: Git diff last commit. Revert suspicious chunks.
  - DEFER: HARD STOP.

- **GENERIC-10 — Dependency install fails**
  - A1: Run install command with frozen lockfile. Check lockfile drift if frozen fails.
  - A2: Remove `node_modules`, reinstall clean. Commit updated lockfile separately.
  - DEFER: HARD STOP.

- **GENERIC-11 — External service fails**
  - A1: Verify credentials, request format, response parsing. Retry once with backoff.
  - A2: Deterministic local fallback. Make service optional.
  - DEFER: Disable dependent feature. Log MEDIUM or HIGH. System must work without it.

### Project-specific

Append project-specific repair entries here (e.g., `PROJECT-1`, `PROJECT-2`) when a directive introduces a new failure mode. Do not modify the generic entries.

## 3. PHASE EXECUTION PROTOCOL

### PRE-FLIGHT
```
git status                          # clean
git log --oneline -1                # previous phase commit exists
pnpm install --frozen-lockfile      # or equivalent
```

Build affected workspaces. Record baseline test counts.
First phase that consumes directive design data: run spec-reality reconciliation per section 1.13.

### EXECUTION
Write smoke assertions first. Run them. Expect red. Implement until green.
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
Append to `docs/deferred-issues.md`. Append to `AUTONOMOUS_RUN_LOG.md` with timestamp, phase name, SHA, counts. If any `SPEC_REALITY_DELTA` entries surfaced this phase, log them here.

### TRANSITION
Immediately begin next phase. No pause.

### END OF DIRECTIVE
Generate `BUILD_REPORT.md` (section 5).
Commit working files and report:
```
docs(directive): BUILD_REPORT and working files
```
Push branch. Direct git push preferred. If blocked, MCP write of small files only — apply section 1.12 preflight.
Open PR. If `Auto-merge: yes`, register auto-merge. If no, log URL and stop.

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

## 5. BUILD_REPORT.MD FORMAT

```markdown
# [Directive Name] — Build Report

Generated: [ISO timestamp]
Branch: [name]
Base SHA: [SHA on main when cut]
Final commit: [SHA]
Production impact: [level]
Auto-merge: registered | pending Marcus | HALTED

## Summary
[One paragraph]

## Phase Outcomes
| Phase | Status | Passing | Deferrals | SHA |
|---|---|---|---|---|

## Spec-Reality Deltas
[List SPEC_REALITY_DELTA entries from AUTONOMOUS_RUN_LOG.md, if any]

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
[List with exact prompt for Marcus to run across Claude, GPT, Gemini, Grok]

## Production Application Pending
[Migrations, secrets, env vars — exact commands]

## Next Actions
1. [highest priority]
2. [next]
```

## 6. HARD STOP CONDITIONS

Halt ONLY for:
- Dependency install fails after GENERIC-10
- Build fails after GENERIC-9
- Test runner itself crashes
- Git operations fail after credential check
- Filesystem errors
- Production deploy fails and production is degraded
- Foreign dirty working tree after the working-tree repair attempts
- Production data accidentally modified
- Safety-prompt change attempted without Council authorization in directive
- MCP write recovery fails after preflight + recovery attempts

## 7. META-PROMPT

See `META_PROMPT.md` (sibling file). Pairs with this AUTONOMY_LAYER. Send to Charlie/Claude after generating any project spec to convert it into a runnable directive.

## 8. HOW TO USE

- Generating a directive: spec in chat → paste meta-prompt from `META_PROMPT.md` → Charlie produces directive → Marcus reviews → fire at CC Local or CC Cloud (or both, parallel).
- Embedding in CC / Codex: `AUTONOMY_LAYER.md` at `.symposium/AUTONOMY_LAYER.md`. Directive opens with "Apply AUTONOMY_LAYER.md before executing."
- Parallel agents: same layer file, coordination via working files (section 0.4).
- Updating this file: PR with `chore(autonomy): v[X.Y] — [what changed]`. Tick version.

## 9. WHAT THIS FILE EXCLUDES

Personal operating context. Product strategy. Feature acceptance criteria. Prompt content. Safety copy.
This file is execution protocol only.

End of AUTONOMY_LAYER.md (Symposium Generic Edition) v1.3
