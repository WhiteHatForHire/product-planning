# QA Tester Onboarding — [project name]

**For**: junior QA tester or part-time contractor
**Project**: [name]
**Operator contact**: [name + channel]
**Last updated**: YYYY-MM-DD

This document is the brief a junior QA tester receives when joining a project under Symposium OS. The role is structured, scoped, and async. The deliverable is structured bug reports, not code.

---

## What this project is

[One paragraph: what the product does, who it's for, what stage it's in (pre-launch / live / iterating). Avoid jargon. Avoid the project's internal vocabulary on the first read; if you must use a term, link to `.symposium/CONTEXT.md` glossary.]

## What your role is

You test the product against a feature list and document what doesn't match. You do not write code. You do not propose fixes (though observations are welcome). You produce structured bug reports the operator can hand to an agent for resolution.

Your work compounds: bugs you find now save the operator from finding them later, and the bug patterns you surface inform how the product evolves.

## What you need to get set up

- Access to the production URL: [URL]
- Access to the staging URL (if separate): [URL]
- Device set for testing: [iOS / Android / desktop browsers / specific hardware]
- A way to record screen / take screenshots: [Loom / native screen recording / etc.]
- A way to submit bug reports: [GitHub issues / shared doc / Notion / Linear / etc.]
- (Optional) Read access to `.symposium/CONTEXT.md` for project vocabulary

## What you do on a typical session

1. Read the current `MANUAL_PLAYTEST_REQUIRED.md` at repo root or wherever the operator points you. This file lists what to test.
2. Pick a device and a checklist section.
3. Walk through each item. For each: confirm the expected behavior, or document the deviation.
4. For each deviation, capture:
   - What you did (steps to reproduce)
   - What you expected
   - What actually happened
   - Screenshot or short video
   - Device + browser + viewport size
   - URL or build SHA if available
5. Submit each bug as a separate report (one bug per report, not bundled).

## Bug report format

Use this exact structure. Consistency makes triage faster.

```markdown
**Title**: [Short, specific. "Filter drawer doesn't close on backdrop tap (iOS Safari)"]

**Severity**: blocker / high / medium / low

**Device**: [iPhone 15 Pro / Pixel 7 / MacBook Pro 14" / etc.]
**Browser**: [Safari 17 / Chrome 120 / Firefox 122]
**Viewport**: [375x812 / 1280x800 / etc.]
**URL or build**: [URL or SHA]

**Steps to reproduce**:
1. [Step]
2. [Step]
3. [Step]

**Expected**: [What you expected]

**Actual**: [What actually happened]

**Screenshot / video**: [link]

**Notes** (optional): [anything else worth flagging]
```

## What "good" looks like

- Bugs are reproducible: someone else can follow your steps and see the same thing
- Bugs are scoped: one bug per report, not a list of issues bundled together
- Severity is honest: a typo is not a blocker; a broken core flow is not a low
- Screenshots show the bug clearly: cropped, annotated if helpful, not full-page when only a corner matters
- Edge cases are explored: the obvious paths and the weird ones (back button, offline, slow network, rotation, etc.)

## What's out of scope for QA

- **Writing code** to fix bugs. You report; the agent fixes.
- **Architectural opinions** on how a bug should be fixed. Observations welcome; the operator decides scope.
- **Triaging across reports**. File each bug; the operator's triage skill handles consolidation.
- **Bug discovery in unfinished surfaces**. The playtest checklist defines scope. Bugs found outside scope are welcome but flagged as out-of-scope discoveries.

## How feedback reaches you

- Bugs you file get triaged (per `skills/planning/production-bug-triage`)
- Fixes land in PRs you can follow if you want context
- Re-test asks come back to you with the build SHA where the fix shipped
- Patterns across your reports inform skill and protocol updates

## Cadence

[Specify the working cadence — async with a weekly check-in / synchronous sessions on certain days / etc.]

## Escalation

If you find something that looks like a serious problem (data loss, security issue, payment bug, user-harm risk), escalate immediately to the operator via [channel] instead of filing a routine report. The escalation path is short on purpose.

## Glossary

For project vocabulary, see `.symposium/CONTEXT.md` in the repo. If the operator hasn't shared this file with you yet, the most important terms for testing are:

- [Term]: [definition]
- [Term]: [definition]
- [Term]: [definition]

(The operator fills in 3 to 5 terms here that are required to understand the product at the level of testing it.)

## First-session checklist

Before your first real session:
- [ ] Confirm access to all URLs and tools above
- [ ] Read the current `MANUAL_PLAYTEST_REQUIRED.md`
- [ ] File one practice bug report on any minor issue, to confirm the report flow works end to end
- [ ] Confirm with the operator that the format is right

Then begin real testing.
