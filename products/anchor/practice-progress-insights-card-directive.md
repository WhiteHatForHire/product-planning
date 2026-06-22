---
title: "# Practice Progress Insights Card directive"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Archive/# Practice Progress Insights Card directive.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# # Practice Progress Insights Card directive

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# Practice Progress Insights Card

## Build Directive

Apply AUTONOMY_LAYER.md before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see AUTONOMY_LAYER.md section 0.1.

---

Surfaces:          artifacts/api-server/src/routes/insights.ts (or existing insights route — verify in Phase A),

artifacts/recovery-checkin/src/pages/Insights.tsx (or equivalent)

Production impact: API change | UI change

Council of Models: no

Auto-merge:        no

Credentials:       gh

Agent:             CC Cloud

## Role

You are adding a Practice Progress card to the Anchor Insights page. Stats are computed from existing `practice_progress` and `practice_choices` tables — no schema changes required. You open a PR and stop; Marcus reviews and merges.

---

## Deployment Posture

PR-only stop. Auto-merge: no — UI copy changes present.

No migrations. No Fly secrets. No Vercel env changes.

---

## Design Data

### What counts as a rep

A session counts as a rep when:

- `status = 'completed'` OR `completion_path IS NOT NULL`

Abandoned sessions (`status = 'abandoned'`) are excluded from all counts and never surfaced.

Saved-without-committing sessions count as reps.

### Stats to compute

**Practice reps**

COUNT of qualifying sessions.

Sub-labels: "X started · Y completed · Z saved without committing"

- Started: total sessions created (including abandoned — for sub-label only)

- Completed: completion_path = 'commitment' OR 'tiny_next_action'

- Saved without committing: completion_path = 'saved_without_committing'

**Modules worked on**

COUNT of unique module_slug values across qualifying reps.

Below count: list module titles using the category mapping below.

**Tiny actions saved**

COUNT of sessions where completion_path = 'tiny_next_action'

**Commitments saved**

COUNT of sessions where completion_path = 'commitment'

**Most practiced skill**

Module category with highest rep count.

Label: "Most practiced: [category label]"

Use category mapping below — do not infer dynamically or via AI.

**Recent practice activity**

Title and relative date of last qualifying rep.

Label: "Recently practiced: [module title] · [relative date]"

For slugs `lapse-vs-relapse` or `what-to-do-after-slip`: show title only, no chosen action.

For all other modules: omit chosen action in MVP.

### Module category mapping (verbatim — use exactly)

| Slug | Category label |

|------|---------------|

| twenty-minute-urge | Creating space before acting |

| holding-a-no | Holding a boundary |

| ask-for-help | Reaching out |

| declining-the-offer | Declining an offer |

| lapse-vs-relapse | Understanding what happened |

| what-to-do-after-slip | Responding after a slip |

### API endpoint

GET /api/insights/practice

Returns:

{

"reps": { "total": N, "started": N, "completed": N, "savedWithoutCommitting": N },

"modulesWorkedOn": { "count": N, "titles": ["..."] },

"tinyActionsSaved": N,

"commitmentsSaved": N,

"mostPracticedSkill": "category label" | null,

"recentActivity": { "title": "...", "relativeDate": "..." } | null

}

Mount at existing insights route group or create /api/insights/practice. Verify path in Phase A.

### Copy (verbatim)

Section header: Practice progress

Subtext: Small reps count. This shows the recovery moves you have practiced over time.

Empty state (0 reps):

"No practice reps yet. When you try a practice, Anchor will show your progress here. You do not have to complete one perfectly for it to count."

Low-volume state (1–3 reps):

"You've started building reps. A few small practices can make the next hard moment easier to recognize."

Active state (4+ reps):

"You're building usable recovery moves. These are the practices you have worked with, saved, or returned to."

CTA primary: Continue Practice

CTA secondary: View all practices

### Copy guardrails — strictly enforced

Never show:

- "Abandoned practices"

- "Failed" or "incomplete" or "missed"

- "Practice streak broken"

- "You haven't practiced in X days"

- "Consistency score"

- Any phrasing implying the user should have done more

Always use:

- "Started" / "Worked on" / "Saved" / "Returned to"

- "Tiny actions chosen" / "Commitments saved"

- "Reps" not "sessions"

### Layout

Compact card on Insights page, consistent with existing card styling.

Four mini stat tiles in 2×2 grid:

- Practice reps (top left)

- Modules worked on (top right)

- Tiny actions saved (bottom left)

- Commitments saved (bottom right)

Below tiles: Most practiced skill (only if more than one module worked on)

Below that: Recently practiced (title + relative date)

Below that: Continue Practice (primary CTA) + View all practices (secondary CTA)

Mobile: tiles stack to single column. Card stays scannable.

Desktop: constrain to same max-width as other Insights cards. Do not stretch full viewport.

### New files

artifacts/api-server/src/routes/insights/practice.ts (or add to existing insights route — verify in Phase A)

### Modified files

artifacts/recovery-checkin/src/pages/Insights.tsx (or equivalent — verify in Phase A)

---

## Acceptance Criteria

### AUTOMATED

- GET /api/insights/practice returns correct shape

- Abandoned sessions excluded from all counts

- Saved-without-committing sessions counted as reps

- Module category labels match lookup table exactly

- Recent activity for lapse-vs-relapse and what-to-do-after-slip shows title only

- Empty, low-volume, and active state copy renders correctly based on rep count thresholds

- Typecheck clean. Build passes.

### HUMAN_REVIEW (MANUAL_PLAYTEST_REQUIRED — do not block phase gates)

- Card layout matches Insights page visual language

- Stats feel motivating not clinical

- No guardrail copy violations

- Desktop max-width respected

- Production smoke: verify stats match actual practice history on sobrietyanchor.com

---

## Phase Plan

### Phase A — Spec-reality reconciliation

PRE-FLIGHT: git status clean. `pnpm install --frozen-lockfile`. Cut branch: `feat/practice-insights`. Create `docs/run-notes/session-YYYY-MM-DD-practice-insights-plan.md`, `AUTONOMOUS_RUN_LOG.md`, `BLOCKERS_FOR_MARCUS.md`.

SPEC-REALITY RECONCILIATION (required, section 1.13):

Read and log:

- Insights page file path and existing card structure

- Whether an /api/insights route group exists and how it's mounted

- practice_progress and practice_choices actual column names and types

- Test runner, test directory, import/mock patterns from a peer test file

- How relative dates are currently formatted elsewhere in the app (use same utility)

Log SPEC_REALITY_DELTA entries to AUTONOMOUS_RUN_LOG.md. Adopt repo reality.

SMOKE ASSERTIONS WRITTEN FIRST: Assert practice_progress and practice_choices tables have expected columns. Run.

IMPLEMENTATION: Reconciliation only.

COMMIT:

chore(practice-insights): Phase A spec-reality reconciliation

Phase: A

Deferrals: 0

Tests: N passing, 0 skipped, 0 failing

---

### Phase B — Backend stats endpoint

PRE-FLIGHT: Phase A commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

- GET /api/insights/practice returns correct shape with all fields

- Abandoned sessions excluded from reps count

- saved_without_committing sessions included in reps count

- completion_path = 'commitment' increments commitmentsSaved

- completion_path = 'tiny_next_action' increments tinyActionsSaved

- modulesWorkedOn.count reflects unique slugs across qualifying reps

- mostPracticedSkill returns correct category label from mapping, not a raw slug

- recentActivity returns null when no qualifying reps exist

- Unauthenticated request returns 401

Run all. Expect red. Implement.

IMPLEMENTATION:

Create the endpoint. Mount in insights route group (verify path from Phase A). Category label lookup is a static map — do not compute dynamically. Relative date uses the same utility found in Phase A reconciliation.

HEALTH CHECK: All tests pass. Typecheck clean. Build passes.

COMMIT:

feat(practice-insights): GET /api/insights/practice stats endpoint

Phase: B

Deferrals: N

Tests: P passing, S skipped, F failing

---

### Phase C — Practice Progress card UI

PRE-FLIGHT: Phase B commit exists. Build clean.

SMOKE ASSERTIONS WRITTEN FIRST:

- Practice Progress card renders on Insights page

- Empty state copy renders when reps = 0

- Low-volume state copy renders when reps = 1–3

- Active state copy renders when reps >= 4

- Four stat tiles present: Practice reps, Modules worked on, Tiny actions saved, Commitments saved

- Most practiced skill label hidden when only one module worked on

- None of the forbidden copy strings appear in any rendered state

- Continue Practice and View all practices CTAs present

Run. Expect red. Implement.

IMPLEMENTATION:

Add Practice Progress card to Insights page per layout spec. Fetch from GET /api/insights/practice. Show loading state during fetch. States: empty / low-volume / active per rep count thresholds (0 / 1–3 / 4+). Tiles in 2×2 grid. Mobile: single column stack. Desktop: match existing Insights max-width.

MANUAL_PLAYTEST_REQUIRED (log, do not block):

- Card feels motivating, not clinical

- Layout matches Insights page visual language

- Desktop max-width respected

- Production smoke against sobrietyanchor.com

HEALTH CHECK: All assertions pass. Typecheck clean. Build passes.

COMMIT:

feat(practice-insights): Practice Progress card on Insights page

Phase: C

Deferrals: N

Tests: P passing, S skipped, F failing

---

### Phase D — BUILD_REPORT + PR

PRE-FLIGHT: All prior commits exist. Full test suite passes. Build passes.

Generate BUILD_REPORT.md per AUTONOMY_LAYER.md section 5.

Include: SPEC_REALITY_DELTA entries, MANUAL_PLAYTEST_REQUIRED items, note no migrations or env changes required.

COMMIT:

docs(practice-insights): BUILD_REPORT and working files

Open PR:

gh pr create --title "feat(practice-insights): Practice Progress card on Insights" --body "$(cat BUILD_REPORT.md)"

Log PR URL. Stop.

---

## GO

Begin Phase A pre-flight per AUTONOMY_LAYER.md section 3. Credentials preflight scope: gh only. Cut branch from main: feat/practice-insights. Create docs/run-notes/session-YYYY-MM-DD-practice-insights-plan.md and AUTONOMOUS_RUN_LOG.md at repo root. Create BLOCKERS_FOR_MARCUS.md at repo root. Begin spec-reality reconciliation.
