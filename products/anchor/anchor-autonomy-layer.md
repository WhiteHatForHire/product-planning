---
title: "Anchor Autonomy layer"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Anchor OS/Anchor Autonomy_layer.md.docx"
status: active
privacy: working
tags:
  - product
---

# Anchor Autonomy layer

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
AUTONOMY_LAYER.md — Anchor Edition v1.3

Reusable autonomous execution protocol for the Anchor codebase. Reference with: "Apply AUTONOMY_LAYER.md before executing this directive."

Changes from v1.2: Section 0.4 updated — ISSUE_EXECUTION_PLAN.md replaced with session-scoped docs/run-notes/ plan file to eliminate root-level merge conflicts on PR merges. AUTONOMOUS_RUN_LOG.md guidance clarified. Section 7 GO instruction updated to match.

Changes from v1.1: Added section 1.12 (MCP write safety) and section 1.13 (spec-reality reconciliation). Added ANCHOR-16. Both encode lessons from the M5c run on PR #45.

0. SCOPE REVIEW

0.1 Stack reality (fixed — do not deviate)

Frontend: React + Vite + TypeScript + Tailwind + Shadcn UI — artifacts/recovery-checkin — Vercel

Backend: Express + TypeScript — artifacts/api-server — Fly.io (anchor-api-misty-river-3483)

Database: Neon Postgres via HTTP SQL API only. Port 5432 times out on free tier.

Auth: Supabase. Separate from DB. Do not conflate.

AI: OpenAI via makeClient factory (no module-level singleton, keep-alive disabled)

Email: Resend with EMAIL_OUTREACH_ENABLED flag

Monorepo: pnpm workspaces

CI/CD: GitHub Actions. Fly auto-deploys on push to main for artifacts/api-server/, lib/, fly.toml, Dockerfile, pnpm-lock.yaml. Vercel auto-deploys from main.

0.2 Directive header format

Every directive opens with this block. No estimates for lines, phases, or time.

Surfaces:          [files and areas this directive touches]

Production impact: none | schema-only | API change | UI change | prompt change

Council of Models: yes | no

Auto-merge:        yes | no

Credentials:       gh | flyctl | DATABASE_URL | OPENAI_API_KEY | none

Agent:             CC Local | CC Cloud | split (see parallel section in directive)

Auto-merge: yes — agent calls gh pr merge --auto --squash --delete-branch after opening PR. GitHub merges when CI passes. CD fires. No human touch.

Auto-merge: no — agent opens PR and stops. Marcus reviews and merges.

Auto-merge eligibility (all must be true):

All acceptance criteria are AUTOMATED

Zero HUMAN_REVIEW items gate the merge (post-merge validation is fine)

No prompt fragment changes, no safety-adjacent changes, no UI copy changes

CI status checks exist on the repo (Playwright CI must be live)

0.3 Markdown formatting

Code blocks: file paths, commands, code, data structures, agent prompts

Lists: sequential steps, enumerables, file structures

Prose: explanations, decisions, rationale

Tables: comparisons, schemas, phase outcomes

Agent prompts: fenced triple-backtick blocks only. Never blockquotes.

0.4 Working files

Created by every autonomous run. The audit trail.

docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md — phases and goals (session-scoped; eliminates merge conflicts at root)

AUTONOMOUS_RUN_LOG.md — append-only log with commit SHAs, phase outcomes, decisions. Prefer appending to existing file. If conflict risk is high, create docs/run-notes/session-YYYY-MM-DD-[directive-slug]-run-log.md instead.

BLOCKERS_FOR_MARCUS.md — items requiring human approval the agent cannot resolve. Keep at root; on merge conflict, accept incoming.

docs/deferred-issues.md — section 4

Do NOT create ISSUE_EXECUTION_PLAN.md at repo root. Use the session-scoped plan path above.

0.5 Credentials preflight

Run before any implementation. If anything is missing, log to BLOCKERS_FOR_MARCUS.md immediately.

gh auth status                      # always

git status                          # always — must be clean

pnpm install --frozen-lockfile      # always

flyctl auth whoami                  # if flyctl declared in header

Verify DATABASE_URL and OPENAI_API_KEY are set and services respond before any phase that uses them.

CC Cloud agents: declare no credentials in run log. Restrict to code-only work. Escalate anything needing credentials to BLOCKERS_FOR_MARCUS.md.

1. AUTONOMY DOCTRINE

TIER 1 — SELF-HEAL

Apply the relevant playbook entry. Two attempts max. If self-heal succeeds, continue.

TIER 2 — DEFER AND CONTINUE

After two failed attempts:

Log to docs/deferred-issues.md

Stub or skip so the rest of the system works

it.skip("DEFERRED: [reason]") or Playwright test.skip()

Commit current state with deferred note

Continue

TIER 3 — HARD STOP

Only for conditions in Section 6. Before stopping:

git add -A

git commit -m "halt([phase]): [reason with diagnosis]"

git checkout -b halt-$(date +%Y-%m-%d-%H%M)

git push origin halt-$(date +%Y-%m-%d-%H%M)

Generate BUILD_REPORT.md with HALTED status. Stop.

NEVER

Ask for human input mid-build outside BLOCKERS_FOR_MARCUS.md

Wait between phases

Stop for "I'm not sure" — defer and continue

Commit broken code without marking deferred

Skip deferred-issues.md or BUILD_REPORT.md

Expand a phase's scope mid-build

Merge PRs manually (use --auto for eligible directives)

Apply migrations to production Neon without directive authorization

Touch production data outside explicit migration scope

Modify safety-relevant prompts without Council authorization in the directive

1.5 Acceptance criteria split

Every directive must declare:

AUTOMATED: typecheck, unit tests, Playwright e2e, build success, programmatic assertion. Block phase gates.

HUMAN_REVIEW: prompt voice, visual review, production smoke, behavioral judgment. Do not block phase gates. Log as MANUAL_PLAYTEST_REQUIRED.

1.6 Fallback content must be specified

The agent does not invent:

Prompt fragment text

Approved-copy banks or forbidden-copy lists

Crisis routing language

User-facing error messages

Default values for new stable_profile fields

Migration backfill mappings

Spec the content verbatim in the directive.

1.7 Scope discipline

If implementation grows beyond a phase's stated goal: halt the expansion, defer to a future phase or deferred-issues.md, continue with current phase as scoped. Scope creep is a deferrable issue, not a license to expand.

1.8 Deployment

Frontend changes auto-deploy to Vercel on merge. Backend changes auto-deploy to Fly on merge when relevant files are touched.

Migrations: code lands in PR. Production application is Marcus-only. State the exact Neon HTTP SQL command in the PR body.

Fly secret changes: Marcus-only. State exact flyctl secrets set command in PR body.

Vercel env changes: Marcus-only. State exact variable and location in PR body.

Auto-merge: yes — END OF DIRECTIVE steps:

gh pr create --title "[type]: [title]" --body "$(cat BUILD_REPORT.md)"

gh pr merge --auto --squash --delete-branch

Log: AUTO-MERGE REGISTERED — merges when CI passes. Stop.

Auto-merge: no — END OF DIRECTIVE steps:

gh pr create --title "[type]: [title]" --body "$(cat BUILD_REPORT.md)"

Log PR URL. Stop. Marcus reviews and merges.

1.9 Atomic commits

One concern per commit. No "while I'm here" bundling.

type(scope): [what changed]

[body]

Phase: [name]

Deferrals: N

Tests: P passing, S skipped, F failing

1.10 No silent failures

Every fallback path logs its trigger at the layer where it fires

Every try/catch logs before returning a fallback

No function returns "" or null as a non-trivial fallback without logging why

Every external call that can fail has an observable failure mode

The M5c incident — weeks of silently broken AI with zero log signal — is the canonical example of what this prevents.

1.11 Production safety boundaries

Production Neon: read-only unless directive explicitly authorizes writes

Real user data: never log, exfiltrate, or include in test fixtures

Safety prompts and forbidden-copy lists: Council of Models review required before merge

EMAIL_OUTREACH_ENABLED: Marcus-only toggle

1.12 MCP write safety

The GitHub MCP write path (create_or_update_file and equivalents) has a destructive failure mode: passing a literal placeholder string instead of full file content silently overwrites the remote file. This happened on PR #45 — the run log was reduced to 24 bytes before being restored. ANCHOR-16 covers recovery; this section covers prevention.

Preferred path order for file changes:

Direct git push — best. Full history, atomic, normal review.

MCP commit of code files — when direct push is blocked.

MCP commit of large append-only logs — last resort only. Prefer creating small per-session run notes at docs/run-notes/session-YYYY-MM-DD-[context].md instead. The big log references them later.

Before any MCP write, the agent must verify and log:

Target path

Current remote SHA (retrieved fresh, not cached)

Byte length of outgoing content

First 200 characters of outgoing content

Last 200 characters of outgoing content

Explicit assertion: outgoing content is full file body, not placeholder, not diff, not template marker

Hard stop the MCP write if any of these are true:

Outgoing byte length is dramatically smaller than the last known remote size for that file (threshold: under 25% of remote size for files over 5KB)

Outgoing content matches known placeholder patterns: [paste content here], <file body>, literal ${...} template markers, single-line content for a known multi-section file

Remote SHA cannot be verified

If a hard stop fires: do not write. Log the attempted-but-blocked write in AUTONOMOUS_RUN_LOG.md and BLOCKERS_FOR_MARCUS.md. Switch to creating a small new file (per-session run note) instead, or escalate to Marcus.

1.13 Spec-reality reconciliation

Before implementing the design data in any directive, verify it against actual repo state. Do this once at the start of the first phase where the directive's data is consumed.

Check at minimum:

Test runner — read package.json scripts and an existing peer test file. Confirm runner (Vitest vs node:test vs Jest), import patterns, mock API.

Test directory — confirm where the runner scans. The directive may specify a path the runner does not pick up.

Interface fields — read the actual TypeScript interfaces being consumed. Field names matter (isPrimary vs is_primary).

File paths — confirm proposed file locations match repo conventions.

Import patterns — match the pattern used by existing peer files in the same workspace.

When directive data conflicts with repo reality, log a SPEC_REALITY_DELTA entry in AUTONOMOUS_RUN_LOG.md:

SPEC_REALITY_DELTA — [phase name]

Directive said: [exact text or assumption]

Repo reality: [what the code/config actually has]

Adopted: [what the agent used — always repo reality]

Reason: [one-line justification]

This is adaptation, not deferral. Continue executing the directive's intent against corrected reality. The directive is a plan; the repo is the source of truth.

2. SELF-REPAIR PLAYBOOK

Apply in order: symptom → attempt 1 → attempt 2 → defer.

Generic

GENERIC-1 — Specific test fails A1: Re-read implementation and assertion. Fix obvious bug. A2: Check if assertion is wrong. Update if implementation matches intent. DEFER: it.skip / test.skip. Log. Continue.

GENERIC-2 — Feature behavior wrong but system runs A1: Re-read spec. Trace. Fix. A2: Simplify to known-working baseline. DEFER: Stub behavior. Log. Continue.

GENERIC-3 — Module not found / import error A1: Verify path (case-sensitive). Check export name. Check tsconfig.json paths. A2: Create stub if file missing. DEFER: Stub with typed dummy returning safe defaults. Log.

GENERIC-9 — Build fails A1: Identify offending file. Check syntax. For api-server: run lib builds first (ANCHOR-1). A2: Git diff last commit. Revert suspicious chunks. DEFER: HARD STOP.

GENERIC-10 — Dependency install fails A1: pnpm install --frozen-lockfile. Check lockfile drift if frozen fails. A2: Remove node_modules, reinstall clean. Commit updated lockfile separately. DEFER: HARD STOP.

GENERIC-11 — External service fails A1: Verify credentials, request format, response parsing. Retry once with backoff. A2: Deterministic local fallback. Make service optional. DEFER: Disable dependent feature. Log MEDIUM or HIGH. System must work without it.

Anchor-specific

ANCHOR-1 — api-server typecheck: 40+ false TS2339/TS6305 errors in fresh worktree A1: pnpm -F @anchor/lib-db build && pnpm -F @anchor/lib-api-zod build, then re-run typecheck. A2: pnpm -r build from root. DEFER: HARD STOP if both fail.

ANCHOR-2 — Neon port 5432 times out A1: Switch to Neon HTTP SQL API. Pattern from scripts/seed/programs.mjs. A2: Add retry with backoff for auto-pause wake. DEFER: Log to BLOCKERS_FOR_MARCUS.md if HTTP also fails.

ANCHOR-3 — Non-JS assets missing from /app/dist/ after esbuild A1: Add explicit copy step in build.mjs. Update path resolution in consumer. A2: Use esbuild loader: { '.txt': 'text' } for small known asset sets. DEFER: HARD STOP if feature depends on the asset.

ANCHOR-4 — Fly deploy fails, production degraded A1: gh run view --log. Check FLY_API_TOKEN, build errors, disk. A2: flyctl releases rollback <version>. Revert bad commit. DEFER: BLOCKER. HARD STOP.

ANCHOR-5 — Vercel preview returns 401 A1: Append ?x-vercel-protection-bypass=$TOKEN. A2: Ensure VERCEL_PROTECTION_BYPASS_TOKEN is in GitHub secrets and injected as extraHTTPHeaders in playwright.config.ts. DEFER: Log. Continue with specs that don't need the preview.

ANCHOR-6 — Playwright 403'd by Cloudflare WAF against sobrietyanchor.com A1: Repoint to Vercel preview URL with bypass token (ANCHOR-5). A2: Mark production suite as MANUAL_PLAYTEST_REQUIRED. Production smoke is local-only. DEFER: Known constraint. Cloud agents don't run production smoke.

ANCHOR-7 — Playwright can't find Chromium on Windows local A1: npx playwright install --with-deps chromium. A2: Route suite to GitHub Actions Linux runner. DEFER: MANUAL_PLAYTEST_REQUIRED if Linux CI also fails.

ANCHOR-8 — Migration written but production not applied A1: Do not auto-apply. Log exact command in BLOCKERS_FOR_MARCUS.md. A2: If directive authorizes: apply via Neon HTTP SQL. Verify by reading back schema. DEFER: Production schema changes always need explicit Marcus approval.

ANCHOR-9 — Auth-dependent test fails, no test user A1: Verify SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY. Verify seedUsers.ts is invoked. A2: Seed test user via Supabase admin API. Tear down after. DEFER: test.skip("DEFERRED: no test user seeding"). Log.

ANCHOR-10 — Fragment file referenced but missing A1: Create file with verbatim content from directive. If directive didn't specify content: section 1.6 violation. Log BLOCKER, escalate. A2: Fall back to default.txt. Log the missing slug (section 1.10). DEFER: HIGH if user-facing.

ANCHOR-11 — New stable_profile field returns null for existing users A1: Ensure normalizeStableProfile() sets safe default on every read. A2: Add null guards in consumers. DEFER: MEDIUM. Field works for new users only. Log.

ANCHOR-12 — Stale assembled prompt after profile edit A1: Verify stable_profile.updated_at is in cache key and edit handler updates it. A2: Force cache invalidation in edit handler. Unit test: edit → next prompt differs. DEFER: Set TTL to 60s. Log. Fix properly next session.

ANCHOR-13 — Vitest fails, DOM unavailable A1: Scope test to pure logic. Move DOM assertions to Playwright e2e. A2: Configure jsdom in vitest.config.ts if simple. DEFER: Pure logic → automated. UI/render → MANUAL_PLAYTEST_REQUIRED.

ANCHOR-14 — Working tree dirty at preflight A1: Inspect diff. If clearly own prior work, commit with wip: and continue. A2: Stash with preflight-stash-[directive]-[phase]. Log. DEFER: Foreign diff → HARD STOP.

ANCHOR-15 — pnpm install --frozen-lockfile fails A1: pnpm install without frozen. Inspect diff. Commit lockfile update as separate chore:. A2: Revert the change that caused drift. DEFER: HARD STOP if lockfile is genuinely broken.

ANCHOR-16 — MCP write shipped placeholder or wrong content Symptom: file on remote is dramatically smaller than expected, contains literal placeholder text, or has been overwritten with content that does not match the local working copy. Section 1.12 preflight should have caught this; if it slipped through, recover here. A1: Locate the last known-good remote SHA via git log --remotes or the GitHub commit history UI. Pull that version locally. Re-apply section 1.12 preflight on the recovery content. Push the verified-correct full content via a new commit. A2: Hard reset local to the corrupted commit's parent on a recovery branch. Cherry-pick from a known-good predecessor. Push recovery branch. Open a PR titled recover([file]): restore from <SHA>. DEFER: HARD STOP if neither attempt restores. Log full incident context in BLOCKERS_FOR_MARCUS.md. The cost of leaving a corrupted log on main is permanent session-history loss.

3. PHASE EXECUTION PROTOCOL

PRE-FLIGHT

git status                          # clean or ANCHOR-14

git log --oneline -1               # previous phase commit exists

pnpm install --frozen-lockfile      # ANCHOR-15 if fails

Build affected workspaces. For api-server: lib/db and lib/api-zod first. Record baseline test counts.

First phase that consumes directive design data: run spec-reality reconciliation per section 1.13.

EXECUTION

Write smoke assertions first. Run them. Expect red. Implement until green.

Failing test: GENERIC-1, 2 attempts, then defer. Failing feature: GENERIC-2, 2 attempts, stub, defer.

Checkpoint commits after every sub-step leaving the system in a working state:

chore([phase]-checkpoint): [what completed]

HEALTH CHECK

Full test suite for affected workspaces. Count passing / skipped / failing.

Verify expected files exist.

Build passes.

Prompt or AI changes → MANUAL_PLAYTEST_REQUIRED.

UI changes → MANUAL_PLAYTEST_REQUIRED.

Log all to deferred-issues.md.

COMMIT

type(scope): [what changed]

[body]

Phase: [name]

Deferrals: N

Tests: P passing, S skipped, F failing

Council review: yes | no

REPORT UPDATE

Append to docs/deferred-issues.md. Append to AUTONOMOUS_RUN_LOG.md with timestamp, phase name, SHA, counts. If any SPEC_REALITY_DELTA entries surfaced this phase, log them here.

TRANSITION

Immediately begin next phase. No pause.

END OF DIRECTIVE

Generate BUILD_REPORT.md (section 5).

Commit working files and report:

docs(directive): BUILD_REPORT and working files

Push branch. Direct git push preferred. If blocked, MCP write of small files only — apply section 1.12 preflight.

Open PR. If Auto-merge: yes, register auto-merge. If Auto-merge: no, log URL and stop.

4. DEFERRED-ISSUES.MD FORMAT

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

5. BUILD_REPORT.MD FORMAT

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

[Migrations, Fly secrets, Vercel env — exact commands]

## Next Actions

1. [highest priority]

2. [next]

6. HARD STOP CONDITIONS

Halt ONLY for:

Dependency install fails after GENERIC-10

Build fails after GENERIC-9

api-server typecheck fails after ANCHOR-1

esbuild asset bundling fails after ANCHOR-3 and feature depends on it

Test runner itself crashes

Git operations fail after credential check

Filesystem errors

Fly deploy fails and production is degraded (ANCHOR-4)

Foreign dirty working tree after ANCHOR-14 attempt 2

Production data accidentally modified

Safety-prompt change attempted without Council authorization in directive

MCP write recovery fails after ANCHOR-16 attempt 2

7. META-PROMPT

Send this to Charlie/Claude after generating any Anchor spec:

Take the spec above and turn it into a fully autonomous Anchor build directive using AUTONOMY_LAYER.md (Anchor edition v1.3, repo root).

Rules:

1. Scope review first (section 0). Trim if needed. Document trims.

2. Stack is fixed — section 0.1. No alternatives.

3. Open with the header block from section 0.2. No line counts, phase counts, or time estimates.

4. Fallback content inline — section 1.6. No agent-invented copy.

5. AUTOMATED vs HUMAN_REVIEW split — section 1.5.

6. Deployment posture and auto-merge eligibility — section 1.8.

7. Feel/visual criteria are HUMAN_REVIEW. Agent cannot verify voice or visual quality.

8. Optional integrations deferrable — system must work without them.

9. Directive-specific repair entries only for new failure modes not in Section 2 playbook.

10. Atomic commits — section 1.9.

11. No silent failures — section 1.10.

12. Production safety always — section 1.11.

13. MCP write safety always — section 1.12. Preferred path is direct git push. MCP writes preflight per section 1.12.

14. The first phase that consumes the directive's design data must run spec-reality reconciliation per section 1.13 before implementing.

15. Parallel-agent split: which surfaces run CC Cloud (no credentials), which CC Local (credentials), how branches reconcile. Marcus runs up to 6 agents concurrently.

Directive must include:

- Header block (section 0.2)

- Role statement (one paragraph)

- "Apply AUTONOMY_LAYER.md before executing." — do not duplicate protocol.

- "Stack: AUTONOMY_LAYER.md section 0.1."

- Full design data: schema deltas, file structure (new/modified/deleted with full paths), non-obvious code patterns, all prompt fragment content verbatim, all copy verbatim.

- Phase plan: per-phase smoke assertions, implementation steps, AUTOMATED criteria, HUMAN_REVIEW items, commit format. The first data-consuming phase calls out spec-reality reconciliation explicitly.

- Working files protocol (section 0.4).

- Directive-specific repair entries if applicable.

- GO instruction: first concrete action with branch name. Example: "Begin Phase A pre-flight per AUTONOMY_LAYER.md section 3. Credentials preflight scope: [list]. Cut branch from main: feat/[directive-slug]. Create docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md and AUTONOMOUS_RUN_LOG.md at repo root."

Voice: direct, imperative. No preamble. Reference AUTONOMY_LAYER.md by section number.

[AUTONOMY_LAYER.md is at repo root. Agent reads it before starting.]

8. HOW TO USE

Generating a directive: spec in chat → paste meta-prompt from section 7 → Charlie produces directive → Marcus reviews → fire at CC Local or CC Cloud (or both, parallel).

Embedding in CC / Codex: AUTONOMY_LAYER.md at repo root. Directive opens with "Apply AUTONOMY_LAYER.md before executing."

Parallel agents: same layer file, coordination via working files (section 0.4).

Updating this file: PR with chore(autonomy): v[X.Y] — [what changed]. Tick version.

9. WHAT THIS FILE EXCLUDES

Personal operating context. Product strategy. Feature acceptance criteria. Prompt content. Safety copy.

This file is execution protocol only.

End of AUTONOMY_LAYER.md (Anchor edition) v1.3
