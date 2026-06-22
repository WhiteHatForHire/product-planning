---
title: "# V5.2 — Memory Search Lite"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/# V5.2 — Memory Search Lite.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# # V5.2 — Memory Search Lite

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# V5.2 — Memory Search Lite

## Build Directive — PR 2 of 2

Do not start until PR 1 (feat/v52-data-export) is merged and deployed.

Apply AUTONOMY_LAYER.md before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1.

---

Surfaces:          artifacts/api-server/src/memory/searchEvents.ts (new),

artifacts/api-server/src/memory/intentDetect.ts (new),

artifacts/api-server/src/memory/index.ts (new),

artifacts/api-server/src/chat/ (buildChatSystemPrompt or equivalent — verify path in Phase A)

Production impact: API change | prompt change

Council of Models: yes — required before merge

Auto-merge:        no

Credentials:       gh

Agent:             CC Cloud

## Role

You are implementing V5.2 Memory Search Lite for Anchor. When a user message in chat matches explicit memory-intent signals, the backend queries event_log by keyword, applies redaction rules, and appends a labeled history block to the chat context. No vector RAG. No AI scoring. No new tables. No Memory screen UI. Chat-triggered only. You open a PR and stop; Council review and Marcus approval are required before this merges.

---

## Deployment Posture

PR-only stop. Auto-merge: no — prompt change; Council of Models review required before merge.

No migrations. Memory Search Lite is computed on demand from existing event_log data.

No Fly secrets, no Vercel env changes.

---

## Design Data

### Intent detection — trigger logic

Fire when message matches Group A AND Group B, OR matches an exact trigger phrase.

Group A (time/pattern words):

before, last time, happened before, pattern, history, previous, past, again, usually, always

Group B (subject words):

felt, helped, did, happened, check-in, relapse, urge, mood, pattern, situation

Exact trigger phrases (match any, case-insensitive):

"has this happened before"

"when did this happen last"

"what did I do last time"

"what worked before"

"what helped before"

"what usually happens when"

"is this a pattern"

"do I always do this"

"have I said this before"

"have I been here before"

"remind me what helped"

"look back"

"from my history"

"based on my past"

"in previous check-ins"

"last time I felt this"

"last time I was like this"

"what changed since last time"

Conservative threshold: if uncertain, do not trigger. False positives feel creepy and can distort the current chat. Miss is better than irrelevant injection.

### Backend helper signature (verbatim)

function getRelevantPastEvents(

query: string,

filters: { kind?: string; dateRange?: [Date, Date] },

limit: number

): Promise<EventLogEntry[]>

Scoring: keyword match in event_log summary string (primary), event kind match boost, recency boost. No AI used in scoring.

Result count: default 3. Hard cap: 5.

Date range parsing: minimal. Parse only: "in March", "last week", "last month", "this month", "since [month]". If uncertain, ignore date filter and search normally. Relevance wins over recency.

Search scope: event_log only. Do not directly search check_ins, commitments, or practice tables in V5.2.

### Redaction rules

Excluded from results — never injected into chat:

- Full free-text check-in notes

- Phone numbers

- Contact details

- Email addresses

- Addresses

- Raw journal-like entries

- Crisis-contact numbers

- Private saved messages intended for SOS/contact

- Full AI syntheses unless specifically saved and flagged as relevant by user

Allowed in results:

- event_log summary string

- event type

- timestamp/date

- non-sensitive check-in metrics

- high-level tags/fields

- saved synthesis title or short summary if user saved it

### Presentation in chat (verbatim)

The AI incorporates the pattern naturally in its response. A labeled block appends after the AI response. Do not put the history block before the AI response.

History block format:

A few possibly relevant moments from your history:

- Mar 12: [event summary]

- Apr 03: [event summary]

- May 09: [event summary]

Full framing line (verbatim):

"A few moments from your history came up as possibly relevant. They may or may not match what is happening today."

Short UI label (verbatim):

"Possibly relevant from your history:"

### Forbidden phrases — never appear in any chat response or framing

"Your history shows..."

"This matches a pattern..."

"You always do this when..."

"Based on your history, you are likely to..."

And any other definitive pattern claim or predictive statement about user behavior.

### Chat integration

Locate buildChatSystemPrompt or the equivalent function that assembles the chat system prompt (verify path in Phase A).

When memory intent is detected:

1. Call getRelevantPastEvents(userMessage, {}, 3)

2. If results are returned, append to the context passed to the AI — not to the system prompt — as a clearly labeled block using the verbatim framing above

3. If results are empty, do not append anything and do not mention the search to the user

4. Log the trigger (intent detected, query used, result count) — no user content in log

### New files

artifacts/api-server/src/memory/searchEvents.ts    — getRelevantPastEvents implementation

artifacts/api-server/src/memory/intentDetect.ts    — trigger detection module

artifacts/api-server/src/memory/index.ts           — barrel

### Modified files

artifacts/api-server/src/chat/[prompt builder file — verify in Phase A]  — integrate memory search on intent detection

---

## Acceptance Criteria

### AUTOMATED

- getRelevantPastEvents returns max 3 results by default

- getRelevantPastEvents is hard-capped at 5 results regardless of matches

- getRelevantPastEvents returns no results containing phone numbers, email addresses, addresses, raw check-in notes, or crisis-contact numbers

- Intent detection returns true for all 18 exact trigger phrases

- Intent detection returns true for representative Group A + Group B combinations

- Intent detection returns false for normal check-in messages with no memory-intent language (5+ sample messages asserted)

- When intent is detected and results exist, constructed context contains verbatim framing: "A few moments from your history came up as possibly relevant. They may or may not match what is happening today."

- When intent is detected and results exist, context contains label: "Possibly relevant from your history:"

- When intent is detected but no results exist, nothing is appended to chat context

- When intent is not detected, getRelevantPastEvents is not called

- Forbidden phrase assertion: none of the following appear in any framing string constructed by the integration: "Your history shows", "This matches a pattern", "You always do this when", "Based on your history, you are likely to"

- History block appears after AI response in constructed context, not before

- Typecheck clean. Build passes.

### HUMAN_REVIEW (MANUAL_PLAYTEST_REQUIRED — do not block phase gates)

- Memory results feel naturally integrated in a real chat session — not jarring

- Production smoke: send a memory-intent message on sobrietyanchor.com, verify history block appears

### COUNCIL_REVIEW_REQUIRED — do not merge without

See Council prompt in BUILD_REPORT. Marcus runs this across Claude, GPT, Gemini, and Grok before merging.

---

## Phase Plan

### Phase A — Spec-reality reconciliation + event_log shape verification

PRE-FLIGHT: git status clean (confirm PR 1 is merged). `pnpm install --frozen-lockfile`. Cut branch: `feat/v52-memory-search`. Create `docs/run-notes/session-YYYY-MM-DD-v52-memory-search-plan.md` and `AUTONOMOUS_RUN_LOG.md`. Create `BLOCKERS_FOR_MARCUS.md`.

SPEC-REALITY RECONCILIATION (required, section 1.13):

Read actual repo state before implementing. Verify and log:

- event_log table: actual column names and types for summary string, event type/kind, timestamp

- Whether event_log rows contain a saved/flagged field for saved syntheses

- File path and function signature of the chat prompt builder (buildChatSystemPrompt or equivalent)

- How the chat context is passed to the OpenAI call — where to inject the memory block

- Test runner and test directory for api-server (Vitest vs node:test), import/mock patterns from a peer test file

- Whether a memory/ directory already exists or is being created fresh

Log all SPEC_REALITY_DELTA entries to AUTONOMOUS_RUN_LOG.md. Adopt repo reality.

SMOKE ASSERTIONS WRITTEN FIRST: Write a field-presence assertion on event_log row shape using TypeScript interface inspection. Run.

IMPLEMENTATION: Reconciliation only. No code changes.

HEALTH CHECK: Shape map complete. Deltas logged.

COMMIT:

chore(v52-memory): Phase A spec-reality reconciliation

Phase: A

Deferrals: 0

Tests: N passing, 0 skipped, 0 failing

---

### Phase B — getRelevantPastEvents helper

PRE-FLIGHT: Phase A commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

Write unit tests:

- Returns empty array when no event_log rows match query

- Returns max 3 results by default

- Returns max 5 results when limit is 5

- Never returns more than 5 regardless of matches

- Strips phone numbers from all returned entries

- Strips free-text check-in note fields from all returned entries

- Strips email/address fields from all returned entries

- Applies date range filter when "last month" is detected in query

- Ignores malformed date phrase and searches normally

- Keyword match in summary string scores higher than no match

- Results with matching kind receive a boost

Run all. Expect red. Implement.

IMPLEMENTATION:

Create artifacts/api-server/src/memory/searchEvents.ts. Implement getRelevantPastEvents per function signature in design data. Create artifacts/api-server/src/memory/index.ts barrel. Redaction is applied to every row before returning — no consumer can bypass it.

No silent failures: log when query returns empty for a non-trivial reason (e.g., table read succeeded but zero matching rows vs DB error). Log trigger context — not user content.

HEALTH CHECK: All unit tests pass. Typecheck clean. Build passes.

COMMIT:

feat(v52-memory): getRelevantPastEvents helper with redaction

Phase: B

Deferrals: N

Tests: P passing, S skipped, F failing

---

### Phase C — Intent detection module

PRE-FLIGHT: Phase B commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

Write unit tests:

- All 18 exact trigger phrases return true

- "how are you doing" returns false

- "I feel anxious today" returns false (Group B only, no Group A)

- "last time I felt this way" returns true

- "based on my past check-ins" returns true

- "remind me what helped before" returns true

- At least 5 representative normal check-in messages return false

Run all. Expect red. Implement.

IMPLEMENTATION:

Create artifacts/api-server/src/memory/intentDetect.ts. Implement Group A / Group B intersection logic and exact phrase matching. Case-insensitive. Export a single function: detectMemoryIntent(message: string): boolean.

Conservative threshold: when match is ambiguous at edge of Group A/B intersection, return false.

HEALTH CHECK: All unit tests pass. Typecheck clean. Build passes.

COMMIT:

feat(v52-memory): intent detection module

Phase: C

Deferrals: N

Tests: P passing, S skipped, F failing

---

### Phase D — Chat integration

PRE-FLIGHT: Phase C commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

Write unit tests:

- When intent is detected and events are returned, constructed context contains verbatim framing: "A few moments from your history came up as possibly relevant. They may or may not match what is happening today."

- When intent is detected and events are returned, context contains label: "Possibly relevant from your history:"

- When intent is detected but no events are returned, nothing is appended

- When intent is not detected, getRelevantPastEvents is not called

- Forbidden phrase check: none of "Your history shows", "This matches a pattern", "You always do this when", "Based on your history, you are likely to" appear in any constructed framing string

- History block appears after AI response in constructed context, not before

Run all. Expect red. Implement.

IMPLEMENTATION:

Modify the chat prompt builder (path confirmed in Phase A). At the point where the user message is received, call detectMemoryIntent(userMessage). If true, call getRelevantPastEvents(userMessage, {}, 3). If results are non-empty, append the formatted history block to the user-facing context per design data format. If results are empty, do not append, do not mention. Log trigger + result count (no user content).

History block is appended to context, not injected into system prompt.

MANUAL_PLAYTEST_REQUIRED (log, do not block):

- Memory results feel naturally integrated in a real chat session

- Production smoke: send a memory-intent message on sobrietyanchor.com, verify history block appears

HEALTH CHECK: All unit tests pass. Typecheck clean. Build passes. MANUAL_PLAYTEST_REQUIRED items logged.

COMMIT:

feat(v52-memory): chat integration with memory intent detection

Phase: D

Deferrals: N

Tests: P passing, S skipped, F failing

Council review: required before merge

---

### Phase E — BUILD_REPORT + PR

PRE-FLIGHT: All prior phase commits exist. Full test suite passes. Build passes.

IMPLEMENTATION:

Run full test suite for all affected workspaces. Record counts.

Generate BUILD_REPORT.md per AUTONOMY_LAYER.md section 5. Include:

- SPEC_REALITY_DELTA entries from AUTONOMOUS_RUN_LOG.md

- MANUAL_PLAYTEST_REQUIRED items

- COUNCIL_REVIEW_REQUIRED block with council prompt verbatim (below)

- Note: no migrations, no Fly secrets, no Vercel env changes required

COMMIT:

docs(v52-memory): BUILD_REPORT and working files

Phase: E

Deferrals: N

Tests: P passing, S skipped, F failing

Council review: required before merge

Open PR:

gh pr create --title "feat(v52-memory): V5.2 Memory Search Lite" --body "$(cat BUILD_REPORT.md)"

Log PR URL to AUTONOMOUS_RUN_LOG.md. Stop. Do not merge. Council review and Marcus approval required.

---

## Council Review Prompt

Include verbatim in BUILD_REPORT.md under "Council Review Required." Marcus runs this across Claude, GPT, Gemini, and Grok before merging.

---

You are reviewing the Memory Search Lite feature for Anchor, a sobriety support app.

This feature searches a user's past event log when their chat message contains explicit memory-intent language and injects a small labeled block of results into the AI chat context. Review the following for safety and appropriate framing only — not technical implementation.

--- FRAMING COPY ---

Full framing line:

"A few moments from your history came up as possibly relevant. They may or may not match what is happening today."

Short UI label:

"Possibly relevant from your history:"

--- REDACTION RULES ---

Excluded from results (never injected): full free-text check-in notes, phone numbers, contact details, email addresses, addresses, raw journal-like entries, crisis-contact numbers, private saved messages intended for SOS/contact, full AI syntheses unless specifically saved and flagged by user.

Allowed in results: event_log summary string, event type, timestamp/date, non-sensitive check-in metrics, high-level tags/fields, saved synthesis title or short summary if user saved it.

--- FORBIDDEN PHRASES ---

The following phrases must never appear in any chat response or framing:

"Your history shows..."

"This matches a pattern..."

"You always do this when..."

"Based on your history, you are likely to..."

And any other definitive pattern claim or predictive statement about user behavior.

--- QUESTIONS FOR REVIEW ---

1. Does the framing copy make any definitive pattern claims or predictive statements? If so, what specific language should change?

2. Are the redaction rules sufficient to protect sensitive content for a recovery app user? Is anything missing?

3. Does the framing appropriately hedge the relevance of past events without being dismissive?

4. Is there any language in the framing or labels that could feel clinical, alarming, or inappropriate for someone in active recovery?

5. Is there any way the allowed result content (event_log summaries, event types, timestamps) could surface sensitive information even under the redaction rules?

Respond with: APPROVED (no changes needed), APPROVED WITH NOTES (minor suggested changes), or NEEDS REVISION (specific issues that must be resolved before merge). Include specific suggested copy changes if applicable.

---

## GO

Begin Phase A pre-flight per AUTONOMY_LAYER.md section 3. Confirm feat/v52-data-export is merged and deployed before cutting this branch. Credentials preflight scope: gh only. Cut branch from main: feat/v52-memory-search. Create docs/run-notes/session-YYYY-MM-DD-v52-memory-search-plan.md and AUTONOMOUS_RUN_LOG.md at repo root. Create BLOCKERS_FOR_MARCUS.md at repo root. Begin spec-reality reconciliation.
