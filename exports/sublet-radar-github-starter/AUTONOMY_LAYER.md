# AUTONOMY_LAYER.md

Reusable execution protocol for agents working on NYC Sublet Radar.

## 0. Prime Directive

This project is a bounded field tool, not a platform.

Build the smallest white-hat system that helps Marcus find a real NYC sublet. Preserve the portfolio value, but do not let architecture cosplay displace the actual search.

## 1. Hard Build Boundary

V0 has a strict boundary:

- Maximum build budget: 5 focused sessions.
- Maximum spend before review: $100 infra + LLM.
- No v0.5 work until V0 has helped produce at least one real reply.
- No work after 9pm local time.
- No automated outbound messaging.
- No adversarial scraping.

If a task violates the boundary, stop and write the reason to `BLOCKERS_FOR_MARCUS.md`.

## 2. White-Hat Enforcement

Never implement:

- HTTP requests to Facebook Marketplace, Facebook Groups, or any Facebook surface.
- Automated reads of Craigslist listing pages. Craigslist email alerts are allowed.
- Anti-detect browser tooling.
- Residential proxy clients.
- Captcha-solving services.
- Account-warming or fingerprint spoofing.
- Automated outbound messages to listing hosts.

Allowed:

- Dedicated Gmail inbox.
- User-forwarded listing emails.
- Craigslist saved-search email alerts.
- Listings Project email.
- Leasebreak/Roomi/SpareRoom email alerts.
- Reddit RSS or official API at low volume.
- User-pasted links and text.
- Manual Facebook link/text paste processed locally.

## 3. Required Working Files

Every substantial autonomous run creates or updates:

- `ISSUE_EXECUTION_PLAN.md`
- `AUTONOMOUS_RUN_LOG.md`
- `BLOCKERS_FOR_MARCUS.md`
- `docs/deferred-issues.md`
- `BUILD_REPORT.md`

These files are part of the audit trail.

## 4. Preflight

Before implementation:

```bash
git status --short
git log --oneline -1
python --version
```

If dependencies exist:

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```

If credentials are needed, check only for presence. Do not print secret values.

Required secret names, if used:

- `ANTHROPIC_API_KEY`
- `SUBLET_GMAIL_USER`
- `SUBLET_GMAIL_APP_PASSWORD`
- `TELEGRAM_BOT_TOKEN` optional
- `TELEGRAM_CHAT_ID` optional

## 5. Manual Validation Gate

Do not build ingestion infrastructure until `docs/PRE_V0_VALIDATION.md` exists and says `PASS`.

If absent, halt and tell Marcus to complete `docs/03_PRE_V0_VALIDATION.md`.

## 6. Acceptance Criteria Split

Automated acceptance criteria may block merge:

- unit tests pass
- integration tests with fixture listings pass
- schema migrations run idempotently
- sample digest is generated
- no forbidden imports or forbidden platform adapters exist

Human review criteria do not block automated tests, but must be logged:

- listing scoring quality
- draft reply voice
- scam-risk judgment
- whether digest is useful on phone
- whether preferences match Marcus's actual housing taste

## 7. Fallbacks

The system must run without optional services:

- No Telegram token: write Markdown digest to `data/digests/`.
- No LLM key: run deterministic rule-based extraction and log fallback.
- No RSS configured: process manual paste and inbox only.

No silent failures. Any fallback logs why it triggered.

## 8. Commit Discipline

One concern per commit:

- schema
- ingest
- normalization prompt
- scoring
- digest rendering
- tests
- docs

No "while I'm here" cleanup in feature commits.

## 9. Stop Conditions

Hard stop if:

- manual validation has not passed
- forbidden scraping/outbound path appears
- session budget is exhausted
- costs exceed the review budget
- no real listings flow after inbox/RSS setup
- implementation starts drifting into SaaS/productization

