---
title: "!!Anchor Mobile V1 — Runtime Execution Plan"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Pre-Flight/!!Anchor Mobile V1 — Runtime Execution Plan.docx"
status: active
privacy: working
tags:
  - product
---

# !!Anchor Mobile V1 — Runtime Execution Plan

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Mobile V1 — Runtime Execution Plan

Goal: minimize human intervention, maximize parallelism, stack tightly coupled phases into combined directives, surface self-checks so failures catch themselves before Marcus has to.

Combined directives (stacking)

Three combine opportunities. These are not "run in same session" — they are single directives that ship a single PR covering two phases of work. Less context-switch for the agent, one Marcus review per pairing instead of two.

COMBINED-1: D + H (Home + Settings)

Why combine:

Both pure UI surfaces

Neither touches crisis routing or AI surface

Both Sonnet-suitable

Same agent profile (CC Cloud, gh only)

Marcus reviews home and settings together as a coherent app shell

Single directive: [Mobile] Home + Settings Single PR. Tests for both. One visual playtest pass.

COMBINED-2: H+I → drop H+I as separate, fold I into D+H

Wait — re-read. If we already combined D + H, then I (notifications) stays separate but follows immediately after D+H merges. Tight coupling between Settings toggle and notification scheduler stays inside I.

Revised: keep D+H combined, I as its own follow-up directive.

COMBINED-3: B remains separate

B (component kit) does not combine well with anything. It is the foundation every screen depends on. Keeping it pure means C, D, E, F, G, H all build on a known-stable component layer.

Auto-merge upgrades

Original directives all default auto-merge: no. Several phases can safely upgrade to auto-merge per AUTONOMY_LAYER section 0.2 eligibility rules:

Phase

Original

Upgrade

Reason

A

no

no (keep)

First mobile commit — Marcus eyes-on

B

no

yes

Pure components, no copy, no safety, showcase catches visuals

C

no

no

Auth is load-bearing — Marcus reviews deep-link wiring

D+H

no

no

Touches sign-out flow (Settings half) — keep manual

E

no

no

Crisis routing render — safety surface

F

no

no

Crisis routing + chat — safety surface

G

no

no

SOS — safety surface

I

no

yes

Local-only notifications, no copy change post-spec

J

no

no

External distribution

K

no

no

Marcus voice review

Two upgrades (B and I) save two manual gates. Both have AUTOMATED-only acceptance criteria. Update those directives to:

Add auto-merge: yes to header block

Add gh pr merge --auto --squash --delete-branch to end-of-directive

Confirm CI status check exists (Playwright workflow already lives)

Wave-by-wave execution

Wave 0 — Now (in flight)

Phase A — Opus, CC Local

Status: PR #73 open, awaiting CI + Vercel re-run after lockfile fix

Marcus action: confirm CI green, review, merge

Wave 1 — After A merges (parallel)

Two agents fire simultaneously:

Phase B — Sonnet, CC Cloud, auto-merge upgrade

No credentials needed

PR auto-merges when CI passes

Showcase visual review can happen post-merge (low risk — components)

Phase C — Opus, CC Local

Needs EXPO_PUBLIC_SUPABASE_URL and EXPO_PUBLIC_SUPABASE_ANON_KEY

Marcus reviews deep-link wiring before merge

Marcus side-quest during Wave 1 (no agent needed):

Create App Store Connect app record for com.sobrietyanchor.app

Confirm Apple Team ID

Set EAS secrets: EXPO_PUBLIC_SUPABASE_URL, EXPO_PUBLIC_SUPABASE_ANON_KEY

Verify sobrietyanchor.com/privacy and /terms exist

Verify support@sobrietyanchor.com email forwards

Wave 2 — After B AND C merge (single combined directive)

D+H combined — Sonnet, CC Cloud

Home + Settings in one directive, one PR

Marcus reviews shell coherence

Manual merge

Wave 3 — After D+H merges (parallel safety surfaces)

Three Opus agents fire simultaneously on CC Local. All three are safety- adjacent (crisis routing) and need real API + device testing.

Phase E — Opus, CC Local — Check-in + crisis branch

Phase F — Opus, CC Local — Chat + crisis branch

Phase G — Opus, CC Local — SOS + offline cache

Each opens its own PR. Marcus reviews each independently. No auto-merge.

These three are independent in their files but all share the crisis-routing render pattern. Suggest a one-line shared snippet in each directive's SPEC_REALITY section: "Read sibling Phase E/F/G PRs if they have merged for crisis card render consistency."

Wave 4 — After E, F, G merge

Phase I — Sonnet, CC Local, auto-merge upgrade

Needs device for permission test (deferred to playtest)

Wires into Settings toggle from H (already merged)

Wave 5 — After I merges

Phase J — Opus, CC Local

Marcus pre-requisites must be complete (see Wave 1 side-quest)

PR-level work, then Marcus runs eas build + eas submit

Manual merge

Wave 6 — After TestFlight validated on device

Phase K — Sonnet, CC Cloud

Build report + Director Model case study draft

Marcus voice review on case study

Manual merge

Self-check architecture

Each phase already has AUTOMATED acceptance criteria. Layer these checks so failures catch themselves before they reach Marcus:

Per-phase self-checks (in directive)

Pre-flight: clean git, prior phase merged, credentials present

Smoke-first: tests written before implementation, expected red

Health check: AUTOMATED criteria run before commit

Build verification: expo export --platform ios per phase

Typecheck: tsc --noEmit per phase

Cross-phase self-checks (orchestration layer)

Add these to AUTONOMOUS_RUN_LOG.md as enforced gates:

Phase-N start gate: previous phase PR must be merged AND CI green on main

CI gate: Playwright suite must pass before any phase opens a PR

Lockfile gate: pnpm-lock.yaml committed, no drift between mobile/web

No node_modules in commits (this already bit you on Phase A — the agent caught it but it's worth enshrining)

Build-time self-checks (CI workflow addition)

Worth adding a mobile-specific GitHub Actions job that runs on PRs touching artifacts/mobile-app/**:

- pnpm install --frozen-lockfile

- cd artifacts/mobile-app && pnpm typecheck

- cd artifacts/mobile-app && pnpm test

- cd artifacts/mobile-app && npx expo export --platform ios

This catches the bulk of Phase B–I failure modes without device testing.

Add this as part of Phase B (since B is the first phase with tests). Make it a separate small PR before firing B's main directive, or fold into B.

Drift self-checks (Hermes territory, deferred)

In a future Hermes phase:

Auto-comment on PRs when a phase's spec-reality deltas exceed N

Auto-flag deferred-issues.md entries above MEDIUM severity

Auto-summarize BUILD_REPORT contents in a Slack/Discord webhook

Not for V1. Note for the corpus.

Marcus intervention points (minimized)

Pre-build (Wave 0–1, parallel to A/B/C):

[ ] App Store Connect app record

[ ] Apple Team ID confirmation

[ ] EAS secrets configured

[ ] sobrietyanchor.com/privacy live

[ ] sobrietyanchor.com/terms live

[ ] support@sobrietyanchor.com working

Per-phase (only where auto-merge: no):

Review PR

Merge

Post-merge playtests (batched, not blocking):

After Wave 3 merges: full simulator playtest of all flows

After Wave 5: TestFlight install + smoke on physical device

Phase J actions (cannot be delegated):

Run eas build --platform ios --profile production

Run eas submit --platform ios --profile production

Confirm TestFlight build appears in App Store Connect

Install on Marcus's iPhone

Phase K action:

Edit Director Model case study draft into Marcus Vale's voice

That's it. Everything else runs.

Failure modes and how the plan handles them

Failure

Self-catches at

Recovery

CI red on Phase A

Vercel/Actions UI

Lockfix push (already done)

Lockfile drift

CI on subsequent phases

pnpm install + commit + push

Auto-merge on B fires but visuals are broken

Showcase playtest post-merge

Open hotfix PR

Crisis card not rendering in E/F/G

Smoke tests (MOBILE-12, MOBILE-15)

HARD STOP, directive-level repair

Deep link doesn't open app in C

Smoke tests + device playtest

MOBILE-8 repair, defer to physical

EAS build fails in J

eas credentials check

MOBILE-20 repair

TestFlight crash on launch

Console.app diagnostics

MOBILE-22 repair, rollback

Concurrency ceiling

Marcus has 4 CC Local + 4 CC Cloud = 8 concurrent agents available.

Peak concurrency in this plan: 3 agents simultaneously (Wave 3 with E, F, G in parallel). Well under ceiling. The ceiling matters more for the Symposium/Hermes parallel work that can happen during mobile waits.

Suggested parallel side-tracks during mobile waits:

During Wave 1 (A→merge wait): draft Symposium OS Level-Up Brief in Drive

During Wave 2 (B+C wait): Marcus side-quest list above

During Wave 3 (E/F/G build): start Hermes MVP spec

During Wave 5 (J external work): write first Marcus Vale essay seed ("The AI-Native Studio Is Not a Software Factory")

Order of operations summary

Wave 0:  A                              [in flight, awaiting CI]

Wave 1:  B ∥ C                          [parallel after A merges]

Wave 2:  D+H combined                   [after B and C merge]

Wave 3:  E ∥ F ∥ G                      [parallel after D+H merges]

Wave 4:  I                              [after E, F, G merge]

Wave 5:  J                              [after I + Marcus pre-reqs]

Wave 6:  K                              [after J + TestFlight validated]

Total Marcus interventions across all waves:

7 PR reviews (A, C, D+H, E, F, G, J)

3 auto-merges (B, I, with safety net of CI + showcase)

1 set of Marcus pre-Phase-J actions (App Store Connect setup)

1 set of eas build + eas submit commands

1 case study voice edit

The rest runs without you.

On CC Cloud vs CC Local — revised honest breakdown:

CC Cloud constraints (what it actually can't do):

Run eas build / eas submit (needs authenticated EAS session)

Run scripts that hit real production APIs with real auth

Write actual .env files with real secrets

Run device or simulator tests

Everything else Cloud can do, including writing code that consumes those things at runtime.

Phase

Originally drafted

Honest can-run

Reason

B Components

Cloud

Cloud ✓

Pure UI + tests

C Auth

Local

Cloud capable

Cloud writes code + mocked tests; real Supabase test is MANUAL_PLAYTEST anyway

D Home

Cloud

Cloud ✓

Hooks + mocked API tests

E Check-in

Local

Cloud capable

Crisis logic is backend; mobile renders. Cloud writes with mocked responses

F Chat

Local

Cloud capable

Same as E

G SOS

Local

Cloud capable

AsyncStorage testable via Jest mocks

H Settings

Cloud

Cloud ✓

Pure UI

I Notifications

Local

Cloud capable

expo-notifications testable via mocks

J TestFlight

Local

Local only

Genuinely needs EAS auth

K Build report

Either

Cloud ✓

Documentation

Only Phase J truly needs Local. The rest are Cloud-capable for the CODE WORK. The Local designation in my original directives was conservative — based on "this surface needs real testing" but that's all MANUAL_PLAYTEST after merge, not part of the agent's directive scope.

Practical implication: you can run more in parallel than the original runtime plan implied. Wave 3 (E + F + G) could be three Cloud agents instead of three Local agents, freeing local capacity for other work.
