---
title: "NYC SUBLET META PROMPT"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /NYC Sublet Radar/Active/NYC SUBLET META PROMPT.docx"
status: active
privacy: working
tags:
  - product
---

# NYC SUBLET META PROMPT

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
META_PROMPT.md — Sublet Radar Edition v1.0

Send this to Charlie/Claude after generating any Sublet Radar spec. Pairs with AUTONOMY_LAYER.md (Sublet Radar Edition) v1.0.

The Prompt

Paste verbatim after your spec, with AUTONOMY_LAYER.md content appended at the bottom where indicated.

Take the spec above and turn it into a fully autonomous Sublet Radar build directive using AUTONOMY_LAYER.md (Sublet Radar Edition v1.0, repo root).

Apply these rules:

Run scope review first (AUTONOMY_LAYER.md section 0). If the spec exceeds reasonable autonomous executability for one session against the v0 hard build boundary, trim and document trims at the top of the directive. Common Sublet Radar trims: defer Telegram inline approval buttons to v0.5, defer reverse image search, split Ingest and Drafter into separate agent prompts, move "while I'm here" polish to deferred-issues.md upfront.

The stack is fixed. See AUTONOMY_LAYER.md section 0.1. Hermes Agent on a single VPS, SQLite, Python (or Node where forced), Anthropic API, IMAP, RSS, Telegram. Do not propose alternatives. Do not introduce Vercel, Fly, Neon, Supabase, Resend, or Postgres unless the directive's spec explicitly requests a v1 multi-tenant migration.

Open the directive with the header block from AUTONOMY_LAYER.md section 0.2. No line-count estimates, no phase-count estimates, no time estimates. The seven fields are:

Surfaces

Session number (N of 5 for v0, or v0.5+)

Production impact

Council of Models

Auto-merge

Credentials

Agent

For v0 directives: confirm the doctrine boundary status in the directive body. Sessions remaining must be > 0. If the spec would push the build past 5 sessions, halt and flag in the trim block. v0.5+ directives skip this check but still respect the doctrine kill criteria.

Auto-merge eligibility — declare yes/no per AUTONOMY_LAYER.md section 0.2 eligibility rules. Yes only when: all acceptance criteria are AUTOMATED, zero HUMAN_REVIEW items block merge, no scoring-prompt or scam-pattern changes, no Telegram user-facing copy changes, and CI status checks pass.

Specify all fallback content inline (section 1.6). No "agent invents the copy" patterns. Spec verbatim:

Scoring prompt text

Scam pattern lists

Drafter prompt voice and signing convention

Telegram message templates

Default values for new listing fields

Neighborhood canonicalization mappings

Split acceptance criteria into AUTOMATED and HUMAN_REVIEW (section 1.5).

AUTOMATED: typecheck, unit tests, integration tests against mock IMAP and mock LLM responses, build success, programmatic assertion. Block phase gates.

HUMAN_REVIEW: scoring quality on real listings, draft voice, Telegram rendering, behavioral judgment. Do not block phase gates. Log as MANUAL_REVIEW_REQUIRED.

State deployment posture per section 1.8:

The agent does NOT merge manually. Auto-merge eligible: uses gh pr merge --auto. Not eligible: opens PR and stops.

The agent does NOT deploy to the VPS manually. VPS pulls via scripts/deploy.sh on its own cycle or webhook.

Schema migrations (SQLite): code lands in PR with IF NOT EXISTS guards. Deploy script runs them.

Secrets: live in /opt/sublet-radar/.env on the VPS. Adding a new secret requires Marcus to SSH and edit .env, then restart the service. State exact secret name and example value in PR body.

Mark "feel" and visual criteria as HUMAN_REVIEW. The agent cannot verify draft voice, whether a scoring threshold matches Marcus's actual housing taste, whether Telegram messages render well on his phone, or whether scam patterns are correctly tuned. Use AUTOMATED for counts, presence, structure, byte-equality, typecheck, and integration test pass.

Make optional integrations fully deferrable (section 1.11). The system must run without them:

Anthropic API: extraction and scoring paths have a deterministic fallback to a rule-based extractor for known sources. Log on fallback. Do not crash.

Telegram: gate on TELEGRAM_BOT_TOKEN. Fallback: write the digest to data/digest-YYYY-MM-DD.md for SSH viewing.

Firecrawl: required only for the small set of web-fetch sources beyond IMAP and RSS. If absent, those sources are silently skipped with a log entry.

Hermes: required for orchestration. If Hermes is down, the radar is down. SUBLET-3 covers self-heal.

GitHub MCP: required only for PR management. Direct git push is the fallback (and is preferred — section 1.12).

Use the Sublet Radar self-repair playbook in AUTONOMY_LAYER.md section 2. Do not duplicate the SUBLET-N entries. Add directive-specific entries only when the directive introduces a new failure mode (new external API, new ingestion adapter, new persistence layer).

Atomic commits per concern (section 1.9). One concern per commit. Schema change + scoring tweak + Telegram template edit is three commits, not one. No "while I'm here" cleanup bundled with feature work.

No silent failures (section 1.10). Any fallback path logs its trigger. Any try/except that swallows an error logs the error before returning the fallback. Normalizer returning null fields without logging is a silent failure; spec the logging requirement explicitly.

Platform compliance and no-auto-send hold structurally (sections 1.14 and 1.15):

Every ingestion adapter declares SOURCE, METHOD, COMPLIANCE, TOS_NOTES in the file header. Only white_hat is allowed in v0.

No code path opens a session to a listing platform with the intent to post or message. No Selenium / Playwright / Puppeteer in any reply path. The Drafter writes text. Marcus presses send.

Section 0.7 forbidden imports (anti-detect browsers, residential-proxy clients, captcha solvers, account-warming utilities) are non-negotiable refusals; if the spec includes them, halt the directive generation and flag to Marcus.

Single-agent default. Parallel-agent split is allowed when the directive touches two genuinely independent surfaces (Ingest module and Drafter module, for example). Two agents is the practical max for this project. If proposing parallel:

Which surfaces can be CC Cloud branches (code-only, no credentials)

Which surfaces require CC Local (IMAP creds, Anthropic key, Telegram token, VPS SSH)

How branches reconcile (which merges first, what depends on what)

Shared coordination layer: ISSUE_EXECUTION_PLAN.md + AUTONOMOUS_RUN_LOG.md at repo root

Every phase MUST include all five of these in order (per AUTONOMY_LAYER.md section 3):

PRE-FLIGHT: git status clean, prior phase commit exists, credentials preflight per section 0.5, build boundary check per section 0.6 (v0 only), baseline test counts recorded, dependencies install cleanly.

SMOKE ASSERTIONS WRITTEN FIRST: pytest / vitest / node:test. Run them. Expect red. Then implement.

IMPLEMENTATION: until smoke is green. Self-heal per playbook. Defer after two attempts.

HEALTH CHECK: full test suite for affected modules, build passes, MANUAL_REVIEW_REQUIRED and COUNCIL_REVIEW_REQUIRED items logged.

COMMIT: per section 1.9 format.

Phases without smoke assertions are not phases. They are unverified changes.

The first phase that consumes the directive's design data must call out spec-reality reconciliation explicitly per AUTONOMY_LAYER.md section 1.13. Read actual repo state — test runner, test directory, schema or dataclass fields, file paths, import patterns from peer files — before implementing against directive data. Log any SPEC_REALITY_DELTA findings to AUTONOMOUS_RUN_LOG.md. Adopt repo reality; the directive is a plan, the repo is source of truth.

MCP write safety per AUTONOMY_LAYER.md section 1.12. Direct git push is preferred for all file changes. MCP writes are last resort and must run the preflight checklist (target path, remote SHA, byte length, first/last 200 chars, explicit assertion of full-body content). Large append-only logs should never be rewritten via MCP — create a small per-session run note at docs/run-notes/session-YYYY-MM-DD-[context].md instead.

If this is a Session 1 v0 directive: include the pre-v0 manual validation check explicitly. The directive must verify that docs/PRE_V0_VALIDATION.md exists and contains an explicit pass note from Marcus. If absent, the directive halts and directs Marcus to the doctrine doc Section 19. No VPS or Hermes work proceeds before manual validation passes (SUBLET-16).

Generate the directive including:

Header block (AUTONOMY_LAYER section 0.2 format)

Role statement (one paragraph: what the agent is doing, on which module, with what constraints)

"Apply AUTONOMY_LAYER.md before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive."

"Stack: see AUTONOMY_LAYER.md section 0.1."

"Build boundary: see doctrine doc Section 2. This directive consumes Session [N] of 5." (v0 only)

Deployment posture (PR-only stop, auto-merge yes/no with rationale, secret/migration instructions for Marcus if applicable)

Full design data from the spec:

Schema deltas for SQLite (table, column, type, default, migration logic with IF NOT EXISTS guards)

File structure (new files, modified files, deleted files — full paths)

Code snippets for non-obvious patterns

Prompt content verbatim (Normalizer, Evaluator, Drafter where applicable)

Test fixture data verbatim

Default values for new fields verbatim

Ingestion adapter compliance headers (SOURCE, METHOD, COMPLIANCE, TOS_NOTES) for any new adapters

Working files protocol (section 0.4): ISSUE_EXECUTION_PLAN.md, AUTONOMOUS_RUN_LOG.md, BLOCKERS_FOR_MARCUS.md created and maintained throughout

Phase plan: ordered phases, each with the five elements from rule 16. The first data-consuming phase explicitly includes spec-reality reconciliation as the first implementation step.

Directive-specific self-repair entries (only if introducing failure modes not in the playbook)

"Deferred-issues format: AUTONOMY_LAYER.md section 4"

"BUILD_REPORT format: AUTONOMY_LAYER.md section 5"

"Hard stops: AUTONOMY_LAYER.md section 6"

GO instruction: first concrete action with branch name. Example: "Begin Phase A pre-flight per AUTONOMY_LAYER.md section 3. Credentials preflight scope: [list]. Cut branch from main: feat/[directive-slug]. Create ISSUE_EXECUTION_PLAN.md and AUTONOMOUS_RUN_LOG.md at repo root."

Voice:

Direct, imperative, addressed to executing agent.

No preamble. No pleasantries.

Every instruction actionable.

Reference AUTONOMY_LAYER.md by section number. Do not duplicate long passages.

All agent-facing prompts and commands in fenced triple-backtick blocks. Never blockquotes.

[PASTE AUTONOMY_LAYER.md CONTENTS HERE]

How to use

Generate the spec in chat. Design conversation: ingestion adapter list, schema deltas, scoring prompt text, scam pattern updates, drafter voice tweaks, Telegram message templates, acceptance criteria. The spec is yours, in your voice, with all content verbatim.

After the spec is complete, paste this META_PROMPT verbatim, then paste the contents of AUTONOMY_LAYER.md at the bottom where indicated.

Charlie generates the directive — one Markdown file ready to fire at CC Local, CC Cloud, or Codex.

Review the directive. Verify:

Header block has all seven fields

Session number is declared (v0) and consistent with build budget

Fallback content is spec'd inline

Single-agent vs parallel split makes sense

Every phase has the five elements

The first data-consuming phase calls out spec-reality reconciliation

Auto-merge eligibility is correct

Ingestion adapters (if any) carry compliance headers

Fire the directive at the appropriate agent(s).

The three files together

META_PROMPT.md — what you send to Charlie when generating a directive (this file, lives in docs/)

AUTONOMY_LAYER.md — protocol Charlie applies and the agent obeys (paste at bottom of meta-prompt + lives in repo root)

The generated directive — what you fire at CC Local / CC Cloud / Codex

AUTONOMY_LAYER.md lives in the repo and every directive references it by section. META_PROMPT.md lives in docs/ and is the tool when starting any new feature.

The doctrine doc (docs/nyc-sublet-radar-doctrine-v0.2.docx) sits above both: strategic constraints, build boundary, kill criteria, source inventory, scoring criteria, architecture. Charlie reads it for context. The agent does not.

What this file excludes

Stack choices. The self-repair playbook. Deferred-issues format. BUILD_REPORT format. Hard stop list. Doctrine constraints. Product strategy. All elsewhere.

This file generates directives. Nothing more.

End of META_PROMPT.md (Sublet Radar Edition) v1.0
