# case-studies/

Real worked examples of Symposium OS in production. Each case study is a directory with the actual artifacts from a build session: the directive that was fired, the build report that came out, the council review responses (if applicable), and the compression ledger.

These are not tutorials. They are receipts. They exist so operators evaluating Symposium OS can see what an autonomous build session actually produces, and so operators using Symposium OS can compare their own work against worked examples.

---

## Convention

Each case study directory contains:

```
case-studies/[project-slug]/
├── README.md              narrative summary, context, outcome
├── directive.md           the fired directive (verbatim from the session)
├── build-report.md        the resulting BUILD_REPORT.md
├── council-review.md      council responses, if Council of Models was invoked
└── compression-ledger.md  baseline vs actual hours, compression ratio analysis
```

Not every case study has every file. Council review and compression ledger are optional.

---

## What makes a good case study

- **A real session**, not a synthetic example.
- **Non-trivial scope**: enough phases that the autonomous protocol mattered. A single-file change is not a case study.
- **Interesting halts or deferrals**, if any. Clean runs are useful but less instructive than runs that surfaced real edge cases.
- **Honest outcome**: include what didn't work, what was deferred, what failed council.
- **Operator approval to publish**: not every session is public-shareable. Get explicit approval before adding.

---

## What to anonymize

- Production credentials, even revoked ones.
- Real user data of any kind.
- Vendor-specific information the operator's contracts prohibit sharing.
- Internal team member names if the operator chooses to anonymize.

Project names, stacks, and architectural decisions are typically fine to share. Use the operator's judgment.

---

## Case-study slots

- **`kairos-bootstrap/`** — slot for initial Symposium OS adoption case study for the Kairos project. **Artifacts pending.**
- **`kairos-rescue/`** — slot for [project-specific case study]. **Artifacts pending.**

Both case study directories ship with stub READMEs. Replace the stubs with real artifacts when the operator is ready to publish. Do not link to these slots as "published case studies" from the OS-level README or any external surface until the artifacts exist.
