---
title: "NYC SUBLET AUTONOMY LAYER"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /NYC Sublet Radar/Active/NYC SUBLET AUTONOMY_LAYER.docx"
status: active
privacy: working
tags:
  - product
---

# NYC SUBLET AUTONOMY LAYER

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
AUTONOMY_LAYER.md — Sublet Radar Edition v1.0

Reusable autonomous execution protocol for the NYC Sublet Radar codebase. Reference with: "Apply AUTONOMY_LAYER.md before executing this directive."

This file is the execution protocol. The strategic constraints (build boundary, kill criteria, scope discipline) live in the build doctrine doc at docs/nyc-sublet-radar-doctrine-v0.2.docx. This file enforces them at execution time.

0. SCOPE REVIEW

0.1 Stack reality (fixed — do not deviate)

Orchestrator: Hermes Agent (Nous Research). MEMORY.md and USER.md for persistent preferences. Listing-level state lives in SQLite, not in Hermes memory.

Runtime: Python 3.11+ or Node 20+. One language per module, not mixed. Default: Python for ingestion and DB, Node only if a library forces it.

Database: SQLite at /opt/sublet-radar/data/listings.db. WAL mode enabled. Single-writer assumption.

LLM: Anthropic API via the official SDK. Cheaper model (Haiku or Sonnet) for Normalizer, stronger model for Evaluator and Drafter. No module-level singletons; create clients per call.

Ingestion: IMAP fetch from a dedicated Gmail inbox. RSS via feedparser (Python) or equivalent. User-pasted URL queue via Telegram bot updates.

Output: Telegram bot for daily digest. Email fallback only if Telegram is unreachable.

Optional reads: Firecrawl for the small set of white-hat web fetches that aren't email or RSS.

Host: Single VPS (Hetzner, Vultr, or DigitalOcean). Ubuntu 22.04 or 24.04 LTS. systemd for services.

CI/CD: GitHub Actions runs tests on push. VPS pulls via deploy script (scripts/deploy.sh) on push to main. No auto-deploy from CI to VPS; VPS pulls on its own pull schedule or via webhook.

Source of truth: GitHub repo eagle-rocket/sublet-radar. Direct git push preferred. MCP writes are last resort and require Section 1.12 preflight.

What this project does NOT have: Vercel, Fly.io, Neon, Supabase, Resend, real users, production schema, multi-tenant concerns, safety-critical user-facing prompts, EMAIL_OUTREACH_ENABLED. If a directive references any of those, it is from the wrong repo.

0.2 Directive header format

Every directive opens with this block. No estimates for lines, phases, or time.

Surfaces:          [modules / files / areas this directive touches]

Session number:    [N of 5 in the v0 build boundary, or "v0.5+" if past boundary]

Production impact: none | schema-only | output behavior | LLM prompt | infra

Council of Models: yes | no

Auto-merge:        yes | no

Credentials:       gh | ssh-to-vps | IMAP | ANTHROPIC_API_KEY | TELEGRAM_BOT_TOKEN | none

Agent:             CC Local | CC Cloud | Codex | split (see parallel section)

Session number rule: Every v0 directive must declare which session it is against the 5-session hard boundary in the doctrine. If "Session 6 of 5" appears, the directive is rejected by preflight (Section 0.6).

Auto-merge: yes — agent calls gh pr merge --auto --squash --delete-branch after opening PR. CI runs, merge fires, VPS pulls on next cycle. No human touch.

Auto-merge: no — agent opens PR and stops. Marcus reviews and merges.

Auto-merge eligibility (all must be true):

All acceptance criteria are AUTOMATED

Zero HUMAN_REVIEW items gate the merge

No scoring-prompt or scam-pattern changes (these affect what reaches Marcus's eyes — manual voice check first)

No Telegram-bot user-facing copy changes

CI status checks exist on the repo and pass

0.3 Markdown formatting

Code blocks: file paths, commands, code, data structures, agent prompts

Lists: sequential steps, enumerables, file structures

Prose: explanations, decisions, rationale

Tables: comparisons, schemas, phase outcomes

Agent prompts: fenced triple-backtick blocks only. Never blockquotes.

0.4 Working files

Created at repo root by every autonomous run. The audit trail.

ISSUE_EXECUTION_PLAN.md — phases and goals

AUTONOMOUS_RUN_LOG.md — append-only log with commit SHAs, phase outcomes, decisions, SPEC_REALITY_DELTA entries

BLOCKERS_FOR_MARCUS.md — items requiring human approval the agent cannot resolve

docs/deferred-issues.md — Section 4 format

These files are committed to the branch and survive the session.

0.5 Credentials preflight

Run before any implementation. If anything is missing, log to BLOCKERS_FOR_MARCUS.md immediately.

gh auth status                      # always

git status                          # always — must be clean (or ANCHOR-equivalent SUBLET-13)

git log --oneline -1                # always

# Python: python -m venv && pip install -r requirements.txt  (frozen)

# Node:   pnpm install --frozen-lockfile

If the directive touches IMAP, Anthropic, Telegram, or the VPS: verify the respective env vars are set and the services respond before any phase that uses them.

CC Cloud agents: declare no credentials in run log. Restrict to code-only work. Escalate anything needing credentials to BLOCKERS_FOR_MARCUS.md.

0.6 Hard build boundary check (NEW)

Before any v0 directive runs, the agent verifies the build boundary from the doctrine doc.

Doctrine boundary check (v0 only):

Sessions used:        [N]

Sessions remaining:   [5 - N]

Spend used:           $[X]

Spend remaining:      $[100 - X]

Hour:                 [local time]

Anchor priority done: [yes | no]

Hard stop on any of these:

Sessions remaining is 0 and this is a v0 directive

Spend used exceeds $100 and no review gate has been passed

Local time is after 21:00 and this is a v0 directive

Anchor priority block is not done for the day

If hard stop fires, the agent logs the attempted execution in BLOCKERS_FOR_MARCUS.md and exits without changes.

0.7 White-hat enforcement (NEW)

The agent never implements:

HTTP requests to FB Marketplace, FB Groups, or any Facebook surface for automated reads

HTTP requests to Craigslist listing pages (CL email alerts are fine; scraping CL pages directly is not)

Anti-detect browser tooling, residential proxy clients, captcha-solving service integrations, anti-bot evasion utilities

Automated outbound messaging to listing hosts (drafts-only is structural)

Account-warming scripts, fingerprint spoofing, behavioral-simulation utilities

If a directive includes any of the above, the agent halts and logs to BLOCKERS_FOR_MARCUS.md with the literal directive text. This is non-negotiable and not a Tier 1 self-heal.

1. AUTONOMY DOCTRINE

TIER 1 — SELF-HEAL

Apply the relevant playbook entry. Two attempts max. If self-heal succeeds, continue.

TIER 2 — DEFER AND CONTINUE

After two failed attempts:

Log to docs/deferred-issues.md

Stub or skip so the rest of the system works

it.skip("DEFERRED: [reason]") or pytest.mark.skip(reason="DEFERRED: ...")

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

Modify scoring prompts or scam pattern lists without Council authorization in the directive

Implement any item from Section 0.7

Continue past a Section 0.6 hard boundary check

1.5 Acceptance criteria split

Every directive must declare:

AUTOMATED: typecheck, unit tests, integration tests against mock IMAP/LLM, build success, programmatic assertion. Block phase gates.

HUMAN_REVIEW: scoring quality, draft voice, Telegram message rendering, real-listing behavior. Do not block phase gates. Log as MANUAL_REVIEW_REQUIRED.

1.6 Fallback content must be specified

The agent does not invent:

Scoring prompt text

Scam pattern lists

Drafter prompt voice and signing convention

Telegram message templates

Default values for new listing fields

Neighborhood canonicalization mappings

Spec the content verbatim in the directive.

1.7 Scope discipline

If implementation grows beyond a phase's stated goal: halt the expansion, defer to a future phase or deferred-issues.md, continue with current phase as scoped. Scope creep is a deferrable issue, not a license to expand.

This is doubly enforced for v0: every phase that grows costs a session against the boundary.

1.8 Deployment

Code lands in PR. CI runs tests. On merge to main, VPS pulls via scripts/deploy.sh (cron every 10 minutes, or webhook if configured later).

Hermes config changes: code lands; VPS pulls; systemctl restart hermes-agent.service runs as part of the deploy script.

Schema changes (SQLite): migration script lands; VPS runs it as part of the deploy script with IF NOT EXISTS guards. Migrations are forward-only.

Secrets: live in /opt/sublet-radar/.env on the VPS only. Never committed. Adding a new secret requires Marcus to SSH and edit .env, then restart the service. State exact secret name and example value in PR body.

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

Session: [N of 5] (v0 only)

Deferrals: N

Tests: P passing, S skipped, F failing

1.10 No silent failures

Every fallback path logs its trigger at the layer where it fires

Every try/except logs before returning a fallback

No function returns "" or None as a non-trivial fallback without logging why

Every external call (IMAP, Anthropic, Telegram, Firecrawl) has an observable failure mode

Specifically: LLM extraction returning null fields without logging is a silent failure. The Normalizer must log when it deliberately leaves a field null vs. when extraction failed.

1.11 Operational safety boundaries

VPS production data (SQLite, .env): never log secrets, never include real listing contents in committed test fixtures (sanitize host names and addresses)

Telegram bot: never log or forward chat IDs beyond Marcus's own

The radar is single-user. Multi-user features require a new directive series and are out of scope for v0 and v0.5.

Scoring prompts and scam-pattern lists: Council of Models review required before merge if changed.

1.12 MCP write safety

The GitHub MCP write path has a destructive failure mode: passing a literal placeholder string silently overwrites the remote file. This is a known pattern from the Anchor PR #45 incident.

Preferred path order for file changes:

Direct git push — best. Full history, atomic, normal review.

MCP commit of code files — when direct push is blocked.

MCP commit of large append-only logs — last resort only. Prefer creating small per-session run notes at docs/run-notes/session-YYYY-MM-DD-[context].md instead.

Before any MCP write, the agent must verify and log:

Target path

Current remote SHA (retrieved fresh, not cached)

Byte length of outgoing content

First 200 characters of outgoing content

Last 200 characters of outgoing content

Explicit assertion: outgoing content is full file body, not placeholder, not diff, not template marker

Hard stop the MCP write if:

Outgoing byte length is dramatically smaller than the last known remote size for that file (threshold: under 25% of remote size for files over 5KB)

Outgoing content matches placeholder patterns: [paste content here], <file body>, literal ${...} template markers, single-line content for a known multi-section file

Remote SHA cannot be verified

If hard stop fires: do not write. Log the attempted-but-blocked write in AUTONOMOUS_RUN_LOG.md and BLOCKERS_FOR_MARCUS.md. Switch to creating a small new file (per-session run note) instead, or escalate to Marcus.

1.13 Spec-reality reconciliation

Before implementing the design data in any directive, verify it against actual repo state. Do this once at the start of the first phase where the directive's data is consumed.

Check at minimum:

Test runner — read pyproject.toml / pytest.ini / package.json. Confirm pytest vs unittest, vitest vs node:test, import patterns.

Test directory — confirm where the runner scans.

Data types — read the actual schema or TypedDict / dataclass / Pydantic model being consumed. Field names matter (price_total vs priceTotal).

File paths — confirm proposed file locations match repo conventions.

Import patterns — match peer files in the same module.

When directive data conflicts with repo reality, log a SPEC_REALITY_DELTA entry in AUTONOMOUS_RUN_LOG.md:

SPEC_REALITY_DELTA — [phase name]

Directive said: [exact text or assumption]

Repo reality:   [what the code/config actually has]

Adopted:        [what the agent used — always repo reality]

Reason:         [one-line justification]

This is adaptation, not deferral. Continue executing the directive's intent against corrected reality.

1.14 Platform compliance (NEW)

Every ingestion adapter must declare its source type and compliance posture in the file header:

# SOURCE: Craigslist

# METHOD: email_alert  # only: email_alert | rss | opt_in_newsletter | user_paste | partner_api | public_archive

# COMPLIANCE: white_hat

# TOS_NOTES: Craigslist saved-search alerts are an offered platform feature.

If METHOD is anything other than the listed values, the directive is rejected. If COMPLIANCE is not white_hat, halt. There is no gray_hat ingestion in v0; that is a v0.5+ decision and requires a separate directive series.

1.15 No auto-send (NEW)

The radar produces drafts. Marcus sends.

No code path in the radar may:

Open a session against FB, CL, Listings Project, Leasebreak, Roomi, SpareRoom, Reddit, or any listing platform with the intent to post or message

POST to any platform endpoint with listing-reply or messaging semantics

Use Selenium, Playwright, Puppeteer, or any browser-automation library in a path that could result in a message being sent on Marcus's behalf

The Drafter writes text. The Telegram digest displays it. The original listing URL is one tap away. Marcus presses send manually, on the platform, from his own account.

If a directive includes any auto-send path, halt and log to BLOCKERS_FOR_MARCUS.md. This is structural, not negotiable.

2. SELF-REPAIR PLAYBOOK

Apply in order: symptom → attempt 1 → attempt 2 → defer.

Generic

GENERIC-1 — Specific test fails. A1: Re-read implementation and assertion. Fix obvious bug. A2: Check if assertion is wrong. Update if implementation matches intent. DEFER: skip with DEFERRED: reason. Log. Continue.

GENERIC-2 — Feature behavior wrong but system runs. A1: Re-read spec. Trace. Fix. A2: Simplify to known-working baseline. DEFER: Stub behavior. Log.

GENERIC-3 — Module not found / import error. A1: Verify path (case-sensitive). Check pyproject.toml / package.json. A2: Create stub if file missing. DEFER: Stub with typed dummy returning safe defaults. Log.

GENERIC-9 — Build or install fails. A1: Identify offending file. Check syntax. A2: Git diff last commit. Revert suspicious chunks. DEFER: HARD STOP.

GENERIC-10 — Dependency install fails. A1: Reinstall frozen. A2: Remove venv / node_modules, reinstall clean. Commit updated lockfile separately. DEFER: HARD STOP.

GENERIC-11 — External service fails. A1: Verify credentials, request format, response parsing. Retry once with backoff. A2: Deterministic local fallback. Make service optional. DEFER: Disable dependent feature. Log MEDIUM or HIGH.

Sublet Radar-specific

SUBLET-1 — IMAP fetch fails. A1: Verify IMAP host, port (993 IMAPS), credentials, mailbox name ("INBOX" vs "[Gmail]/All Mail"). Reconnect once. A2: Use Gmail API as backup if app-password auth is the blocker; log the switch. DEFER: Log to BLOCKERS_FOR_MARCUS.md; ingestion stops until Marcus checks credentials. Other modules continue with stored listings.

SUBLET-2 — RSS feed unreachable. A1: Retry with 5s backoff up to 3 times. Verify the feed URL still serves the expected content-type. A2: Mark feed as disabled_until: <timestamp + 24h> in config. Skip it. DEFER: Log LOW; one source down is not a system outage.

SUBLET-3 — Hermes orchestration error. A1: Read Hermes logs. Restart the orchestrator service. A2: Bypass Hermes for this phase: run the affected module as a direct Python/Node script invocation. DEFER: HARD STOP if both fail; the radar relies on Hermes for v0.

SUBLET-4 — LLM extraction returns malformed JSON. A1: Retry with response_format constraint and a shorter input. A2: Strict JSON parser with structured-output mode; if SDK supports tool-calling for schema enforcement, switch to that. DEFER: Mark listing status = needs_manual_review. Do not fabricate fields. Log MEDIUM.

SUBLET-5 — SQLite locked or busy. A1: Verify WAL mode is on (PRAGMA journal_mode = WAL). Retry with 200ms backoff. A2: Check for a runaway transaction; rollback any open one. DEFER: HARD STOP if persistent; investigate for unclosed connections.

SUBLET-6 — Telegram bot send fails. A1: Verify TELEGRAM_BOT_TOKEN and chat_id. Retry once. A2: Fallback to email digest via the configured SMTP path if email fallback is enabled. DEFER: Log HIGH; write digest to data/digest-YYYY-MM-DD.md so it can be viewed via SSH.

SUBLET-7 — Dedup miss / duplicate listing surfaced. A1: Check (source, source_id) index integrity. Recompute hash on raw_text as secondary dedup key. A2: Add fuzzy dedup on (neighborhood, price, dates_start) tuple if exact match fails. DEFER: Surface duplicate with a duplicate_of: <id> annotation. Log MEDIUM.

SUBLET-8 — VPS service crash. A1: systemctl restart [service]. Check logs in /var/log/journal or journalctl -u [service] -n 100. A2: Check disk and memory; the VPS is small and SQLite WAL files can grow. DEFER: HARD STOP; service unavailability is operator-visible.

SUBLET-9 — Cron job missed. A1: Verify systemd timer or cron is enabled. Run manually once to catch up. A2: Check for VPS clock drift; install chrony if absent. DEFER: Log LOW.

SUBLET-10 — Scoring drift / shortlist quality regression. A1: Diff the current scoring prompt against the last known-good version. Revert if a recent change is suspect. A2: Run the scoring prompt against the canonical 50-listing test corpus; surface delta. DEFER: COUNCIL_REVIEW_REQUIRED; do not silently adjust scoring without voice review.

SUBLET-11 — LLM cost ceiling hit. A1: Verify the per-day cost cap is configured and the alert fired correctly. A2: Switch Normalizer to the cheaper model tier; keep Evaluator and Drafter on current tier. DEFER: HARD STOP for the day. Log to BLOCKERS_FOR_MARCUS.md with current spend.

SUBLET-12 — Scam pattern flag bypassed shortlist. A1: Verify the flag list is loaded and the check ran. Add the missing flag if it's new. A2: Lower the shortlist threshold or add the flag as auto-reject. DEFER: COUNCIL_REVIEW_REQUIRED; surface the bypass to Marcus before changing live scoring.

SUBLET-13 — Working tree dirty at preflight. A1: Inspect diff. If clearly own prior work, commit with wip: and continue. A2: Stash with preflight-stash-[directive]-[phase]. Log. DEFER: Foreign diff → HARD STOP.

SUBLET-14 — Lockfile drift. A1: Reinstall without frozen. Inspect diff. Commit lockfile update as separate chore:. A2: Revert the change that caused drift. DEFER: HARD STOP.

SUBLET-15 — MCP write shipped placeholder or wrong content. Section 1.12 preflight should catch this; if it slipped through, recover here. A1: Locate the last known-good remote SHA via git log or GitHub UI. Pull that version locally. Re-apply Section 1.12 preflight on the recovery content. Push the verified-correct full content. A2: Hard reset local to the corrupted commit's parent on a recovery branch. Cherry-pick from a known-good predecessor. Push recovery branch. Open PR recover([file]): restore from <SHA>. DEFER: HARD STOP if neither attempt restores. Log full incident in BLOCKERS_FOR_MARCUS.md.

SUBLET-16 — Pre-v0 manual validation not yet passed. A1: Check docs/PRE_V0_VALIDATION.md for the explicit pass note from Marcus. A2: If missing, halt and direct Marcus to Section 19 of the doctrine doc. DEFER: HARD STOP. No VPS or Hermes setup proceeds before manual validation has been declared passed.

3. PHASE EXECUTION PROTOCOL

PRE-FLIGHT

git status                          # clean or SUBLET-13

git log --oneline -1                # previous phase commit exists

# Python: pip-sync or pip install -r requirements.txt

# Node:   pnpm install --frozen-lockfile

Run Section 0.5 credentials preflight. Run Section 0.6 build boundary check (v0 directives only). Build affected modules. Record baseline test counts.

First phase that consumes directive design data: run spec-reality reconciliation per Section 1.13.

EXECUTION

Write smoke assertions first. Run them. Expect red. Implement until green.

Failing test: GENERIC-1, 2 attempts, then defer.

Failing feature: GENERIC-2, 2 attempts, stub, defer.

Checkpoint commits after every sub-step leaving the system in a working state:

chore([phase]-checkpoint): [what completed]

HEALTH CHECK

Full test suite for affected modules. Count passing / skipped / failing.

Verify expected files exist.

Build passes.

Scoring or scam-pattern changes → COUNCIL_REVIEW_REQUIRED.

Telegram message rendering changes → MANUAL_REVIEW_REQUIRED.

Log all to deferred-issues.md.

COMMIT

type(scope): [what changed]

[body]

Phase: [name]

Session: [N of 5] (v0 only)

Deferrals: N

Tests: P passing, S skipped, F failing

Council review: yes | no

REPORT UPDATE

Append to docs/deferred-issues.md. Append to AUTONOMOUS_RUN_LOG.md with timestamp, phase name, SHA, counts. Log any SPEC_REALITY_DELTA entries.

TRANSITION

Immediately begin next phase. No pause.

END OF DIRECTIVE

Generate BUILD_REPORT.md (Section 5). Commit working files and report:

docs(directive): BUILD_REPORT and working files

Push branch. Direct git push preferred. If blocked, MCP write of small files only — apply Section 1.12 preflight.

Open PR. If Auto-merge: yes, register auto-merge. If Auto-merge: no, log URL and stop.

4. DEFERRED-ISSUES.MD FORMAT

# Deferred Issues — [Directive Name]

## Severity

- BLOCKER | HIGH | MEDIUM | LOW | MANUAL_REVIEW_REQUIRED | COUNCIL_REVIEW_REQUIRED

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

Generated:        [ISO timestamp]

Branch:           [name]

Base SHA:         [SHA on main when cut]

Final commit:     [SHA]

Session number:   [N of 5] (v0 only)

Production impact:[level]

Auto-merge:       registered | pending Marcus | HALTED

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

- MANUAL_REVIEW_REQUIRED: N — [titles]

- COUNCIL_REVIEW_REQUIRED: N — [titles]

## Test Status

| Module | Total | Passing | Skipped | Failing |

|---|---|---|---|---|

## Manual Verification Required

[List]

## Council Review Required

[List with exact prompt for Marcus to run across Claude, GPT, Gemini, Grok]

## Operator Application Pending

[Secrets to add, SQLite migrations to run, systemd restart commands — exact commands]

## Doctrine Boundary Status

Sessions used after this directive:    [N of 5]

Spend after this directive:            $[X of 100]

Kill criteria triggered:               none | [list]

## Next Actions

1. [highest priority]

2. [next]

6. HARD STOP CONDITIONS

Halt ONLY for:

Section 0.6 build boundary check fails (v0 directives only)

Section 0.7 white-hat enforcement fires

Section 1.14 platform-compliance check fails

Section 1.15 auto-send path detected

Dependency install fails after GENERIC-10

Build fails after GENERIC-9

Hermes orchestration unrecoverable after SUBLET-3

SQLite unrecoverable after SUBLET-5

VPS service crash unrecoverable after SUBLET-8

LLM cost ceiling hit (SUBLET-11)

Pre-v0 manual validation not yet passed (SUBLET-16)

MCP write recovery fails after SUBLET-15

Git operations fail after credential check

Filesystem errors

Foreign dirty working tree after SUBLET-13 attempt 2

A doctrine kill criterion is triggered (Section 3 of doctrine doc)

7. META-PROMPT

See docs/META_PROMPT.md for the prompt sent to Charlie/Claude when turning a spec into a directive that obeys this layer.

8. HOW TO USE

Generating a directive: spec in chat → paste meta-prompt from docs/META_PROMPT.md → Charlie produces directive → Marcus reviews → fire at CC Local, CC Cloud, or Codex.

Embedding in CC / Codex: This file lives at repo root. Directive opens with "Apply AUTONOMY_LAYER.md before executing."

Parallel agents: Same layer file. Coordination via working files (Section 0.4). Default is single-agent. Parallel only when two surfaces are genuinely independent (e.g., Ingest module and Drafter module can be split). Two agents is normal max for this project; six is Anchor-scale.

Updating this file: PR with chore(autonomy): v[X.Y] — [what changed]. Tick version.

9. WHAT THIS FILE EXCLUDES

Strategic constraints (build boundary numbers, kill criteria specifics, scope rationale). Those live in the doctrine doc.

Product strategy. Source inventory. Scoring criteria. Prompt content. Telegram message templates.

This file is execution protocol only.

End of AUTONOMY_LAYER.md (Sublet Radar Edition) v1.0
