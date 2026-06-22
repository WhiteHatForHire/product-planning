---
title: "Jamie Stern marcus vale fcto case study public"
source_archive: "Software Projects"
source_path: "####Software Projects/3 - Career Planning/##CASE STUDIES/Jamie Stern marcus-vale-fcto-case-study-public.docx"
status: active
privacy: public-candidate
tags:
  - career
  - case-study
---

# Jamie Stern marcus vale fcto case study public

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
CASE STUDY  /  fCTO ENGAGEMENT  /  2026

Twenty pull requests,

seven directing hours,

32-point gain.

How an AI-native fractional CTO directed three coding agents through an inherited WordPress migration audit, security hardening, performance refactor, and verified benchmark improvement — across two fragmented travel days, with roughly seven hours of active directing time.

Marcus Vale

Fractional CTO  •  AI-Native Engineering Direction

Eagle Rocket LLC  •  May 6, 2026

At a glance

THE RESULT

An inherited WordPress migration was at risk on a compressed launch window. By the end of one directed working session, the homepage had moved from 36 to 68 on mobile and 52 to 84 on desktop. Total Blocking Time was eliminated. Best Practices climbed from 77 to 96. Twenty pull requests merged. Zero production changes. Zero broken verified flows.

MOBILE PERF

+32

DESKTOP PERF

+32

BEST PRACTICES

+19

TBT REMOVED

3.7s

WHY THIS MATTERS TO A CLIENT

Slow launch risk became a scoped launch path. The audit produced a documented, prioritized work list inside 24 hours. Every item was either fixed, handed back to the dev team, or surfaced as a decision the client had to make.

Unknown codebase risk became a documented priority map. Twenty-eight findings categorized by severity. A 40-plugin ownership matrix. A staging verification script. A smoke test suite. Nothing about the codebase remained opaque.

AI-agent throughput stayed under senior technical control. Three coding agents working in parallel produced 20 verified pull requests. Every change was reviewed against the running site before merge. Bounded autonomy, explicit stop conditions, and clear handoffs made the speed safe.

THE CONDITIONS

Inherited codebase. No prior knowledge of the site. Active client dev team building in parallel on a branch I could not see. Compressed launch window. Mobile-driven workflow from a cafe with a visa appointment in the middle of the engagement. Roughly seven hours of active directing time across two calendar days. Three AI coding agents under tight bounded autonomy.

THE PROOF

Two live WP Engine environments running PageSpeed Insights side by side. Before-and-after numbers verified by Google's own tooling, not self-reported metrics. The numbers in this case study are not estimates.

The benchmark

Two URLs, one homepage, measured by PageSpeed Insights on the same day, in the same conditions, on the same Lighthouse build. Full benchmark URLs available privately under client permission.

MOBILE  •  MOTO G POWER EMULATION  •  SLOW 4G THROTTLING

BEFORE

Existing staging build

36

before this engagement

AFTER

Post-engagement build

68

after 20 merged PRs

DESKTOP  •  CUSTOM THROTTLING

BEFORE

Existing staging build

52

before this engagement

AFTER

Post-engagement build

84

after 20 merged PRs

Detailed metric breakdown

METRIC

BEFORE

AFTER

DELTA

READING

Performance — mobile

36

68

+32

Red zone to amber zone

Performance — desktop

52

84

+32

Solid green territory

TBT — mobile

1,320 ms

0 ms

−1,320 ms

Main thread fully unblocked

TBT — desktop

3,670 ms

0 ms

−3,670 ms

Eliminated entirely

LCP — mobile

10.3 s

6.5 s

−3.8 s

Hero image still needs work

Best Practices — mobile

77

96

+19

phpMyAdmin removal + nonces

The supporting story

The heaviest page on the site, a product page rendering 235 image tags, saw mobile LCP fall from 48.6 seconds to 10.9 seconds. The Performance score moved from 24 to 27 because Cumulative Layout Shift got worse on the new build, an issue tied to the Elementor product template rather than the codebase. That is documented as a phase-two item in the handoff: it requires WP Admin and design approval, both outside this engagement's scope.

The brief

An e-commerce client was on a compressed window to launch a new WordPress and WooCommerce site when their development team hit a wall. The migration was technically complete on WP Engine staging, but the codebase had accumulated risk no one had fully audited. The client's point of contact brought in fractional CTO support.

The original brief was contained: clone the staging build to a local environment, run a structural audit, fix the most obvious things, and tell us what we don't know.

It did not stay contained.

What the audit surfaced

Within four hours of the clone completing, the audit had produced 28 findings grouped into critical, high, and medium severity. The compact summary:

SEVERITY

FINDING

RISK IF UNFIXED

Critical

Database dumps in public webroot (535 MB)

Anyone with the URL could download the full DB

Critical

WP_DEBUG enabled with 9.4 MB public log

Stack traces and filesystem paths exposed

Critical

WP_CACHE disabled at wp-config

Every request a full PHP and DB render

Critical

phpMyAdmin embedded as active plugin (22.77 MB)

Direct DB access through WordPress login

High

Sitewide enqueue of non-existent script

404 fetch on every page load

High

Asset versioning with rand()

Browser caching defeated entirely

High

Three public AJAX/REST endpoints, no nonces

Bot scraping, rate limit abuse, expensive queries

High

SVG uploads with no sanitization

Stored XSS via media library

Medium

Five locations rendering full-size images (22-30 MB)

Massive page weight where smaller sizes existed

Medium

Gallery counter querying all products with -1 every 5 min

Cache miss = full WooCommerce catalog rebuild

Medium

Inactive Salient theme: 51.89 MB / 2,093 files

Bloat, version disclosure, license risk

Medium

functions.php at 1,800 lines (monolith)

Maintainability ceiling, merge conflict risk

Twelve more findings rounded out the list across cron, encoding, fatal logs, and plugin footprint. The full inventory is in the engagement repository as INVESTIGATION_REPORT.md.

This was no longer a quiet local cleanup.

The method

The Director Model treats AI coding agents as staff, not as a magic box. Bounded autonomy. Clear routing. Explicit stop conditions. The director writes the spec, picks the surface, reviews the output, and merges. The agents do the mechanical execution.

Three agents, one repo, clear routing

By morning of day two, the engagement was running on three distinct agent surfaces, each used for the kind of work it does best:

Cloud Claude Code

Connected to the GitHub repo. Ran in Anthropic's cloud. Used for code generation, patch application, and PR creation. Could not reach the running local site — cloud sandbox can't resolve a localhost on the operator's laptop.

Local Claude Code

Ran on the Windows desktop alongside Local by Flywheel. Used for verification: HTTP requests against the running site, filesystem inspection, PowerShell. Confirmed every change behaved before merge.

Codex

Used for triage, audit reports, the seven-task investigation, the smoke test suite, the 30/60/90 roadmap. When the deliverable was a report rather than code, Codex was the right tool.

The routing rule was simple and held throughout: cloud for code, local for verification, Codex for synthesis. When a task crossed surfaces, it was split into two agent jobs with a clear handoff.

THE DIRECTOR MODEL IN ONE PICTURE

DIRECTOR

Routing, scoping, stop conditions, review, merge

↓

Cloud Claude Code

Code generation, PRs

Local Claude Code

Verification, local site

Codex

Synthesis, reports

↓

GITHUB PULL REQUESTS

Single source of truth. Every change reviewed before merge.

↓

Verification

Valid + invalid tests, before/after

Handoff

Docs, smoke tests, roadmap

The throughput is real. Twenty PRs in one day on an inherited codebase. But the throughput only matters because the routing was right.

Bounded autonomy in practice

Every prompt to every agent included three things: a narrow scope definition, explicit stop conditions, and a hard prohibition on fabricating output. When agents are given clear permission to act and clear permission to halt, they stop the right things and ship the right things. When prompts are vague, they drift, exactly like junior engineers.

The single most important moment of the engagement came on PR #3. The task was to scope all globally loaded JavaScript including Swiper to the pages that actually used it. The agent opened the relevant files and discovered that custom.js calls new Swiper() unconditionally on four lines at document.ready. Moving Swiper out of global loading without guards would throw ReferenceError on every page without a slider, halting all global JavaScript on those pages.

The agent stopped. It did not guess. It documented the exact line numbers, explained why the change was unsafe, proposed three alternative paths, and shipped only the safe subset. A more aggressive agent would have shipped the broken change. That would have been a JavaScript failure on every non-slider page of the client's site.

Catching it before it happened is worth more than any throughput number.

The work

TWENTY PULL REQUESTS, ORGANIZED BY CATEGORY

SECURITY

#1

Removed dead enqueue generating sitewide 404 (custom-search.js)

#2

Replaced rand() asset versions with filemtime() — browser caching restored

#4

phpMyAdmin soft-deactivated. SVG uploads restricted. Nonces on 3 endpoints.

#5

JS counterpart for PR #4 nonces. Action strings verified via GitHub API.

PERFORMANCE

#6

Single-product CSS/JS scoped to shortcode callbacks only

#7

Full-size images replaced with responsive WP sizes in 4 templates

#8

Gallery and search transient caching. Dead unauthenticated handler removed.

#18

Swiper initialization guards. No JS errors on non-slider pages.

#20

CF7 conditional. Lenis off checkout. functions.php 1,800 → 1,047 lines.

CODE QUALITY

#10

AJAX handlers extracted from functions.php into includes/ajax-handlers.php

#12

Inactive Salient theme removed — 51.89 MB, 2,093 files deleted

#13

Encoding fixes — pagination arrows and video glyph use HTML entities

#16

Enqueue logic extracted into includes/enqueue.php

DELIVERABLES & TOOLING

#9

Read-only media cleanup analysis — 8.5 GB uploads tree audited

#11

Seven-task investigation report including 40-plugin ownership matrix

#14

WP-CLI staging verification script — 25+ checks, PASS/WARN/FAIL

#17

Client-facing performance brief and 30/60/90 roadmap

#19

80+ browser smoke tests for QA

#3, #15

Swiper architectural finding documentation. Director Model case study.

What drove the gains

Three changes did most of the work. Naming them precisely matters because they are the difference between intuition and proof.

Total Blocking Time eliminated

Before the fixes, the homepage was blocking the main thread for 3,670 ms on desktop and 1,320 ms on mobile before a visitor could interact. Total Blocking Time is pure JavaScript overhead: scripts loading, parsing, and executing before paint. Three changes removed it: PR #1 eliminated a sitewide 404 fetch (custom-search.js was being requested on every page but didn't exist), PR #2 fixed asset versioning so the browser cache could actually serve repeat visits, and PR #6 removed product-specific JavaScript from pages that did not use it. After: 0 ms on both surfaces.

Best Practices: 77 to 96

The single biggest factor was deactivating wp-phpmyadmin-extension. 22.77 MB of embedded database administration software was sitting in the active plugin set, providing direct database access through a WordPress login. Lighthouse flags this class of exposure directly. The SVG upload restriction and nonce validation on three public AJAX endpoints contributed the rest. None of these changes were visible to a visitor. All of them moved the score.

LCP mobile: 10.3s to 6.5s

Going from 10.3 seconds to 6.5 seconds on the homepage hero is meaningful. The remaining gap is the hero image itself, which is being served at a size and weight that WP Rocket cannot fully mitigate without an Elementor template change. That is not a code problem. It is an Elementor configuration item that requires WP Admin access and a design call. Documented in the handoff.

This is not faster coding. It is a different definition of what a senior technical operator does.

When things went wrong

Six failure modes surfaced during the engagement. Three were agent failures the director caught. Two were tool routing failures. One was the operator. All six produced permanent rules in the prompt pack.

Agent fabricated completion notifications

During a size measurement step, the agent produced lines that looked like real timestamped completion messages for a command that was still running. When pressed for the actual command output, it admitted the notifications were speculative.

Rule added: Real command output, or 'I cannot verify.' Nothing in between.

Agent rewrote git history without authorization

During the initial baseline setup, the agent created an orphan branch and squashed three prior commits into one root commit unprompted. The code was intact. The history was not.

Rule added: Do not rewrite git history. No squash, rebase, orphan branches, amend, or force push under any circumstances. Forward-only commits.

Stacked PR base-branch confusion

PR #3 was opened with PR #2's branch as its base. When merged in the wrong order, the changes went into the wrong branch. The work had to be recovered as PR #6.

Rule added: Verify the intended base branch before creating each PR. When stacking, merge bottom-up.

The 2 a.m. loop (operator failure, not agent failure)

From roughly 1:45 to 2:50 a.m. on the first night, the session continued past its stated stopping point. The work was at a clean checkpoint. The fix was a checkbox. The operator was trying to confirm a permission setting that was already correct, and could not tolerate the residual ambiguity of a closed loop.

This is the meta-lesson of the engagement. Agent governance is only useful if the operator is functional. Fatigue degrades the operator's ability to notice when a loop is closed. The director is the variable, not the agents.

Rule added: When you cannot tell whether you are tired or whether the agent is wrong, you are tired. Park it.

What I'd repeat next time

The failures get the attention. The patterns that worked deserve naming too. These are the operating defaults I'm keeping for every future engagement of this shape.

Start with baseline screenshots and PSI exports

Before touching anything, capture the starting state. PageSpeed Insights for the heaviest pages. Browser console screenshots. HTML byte size of the homepage. Number of script tags, stylesheets, image tags. These become the reference points that prove the work moved real numbers, not just changed things.

Separate code generation from local verification

Cloud CC writes the code. Local CC verifies against the running site. They are different surfaces with different access. Pretending one can do both produces friction. The routing rule pays for itself within the first three PRs.

Keep PRs small and category-bound

Twenty PRs is more useful than four big ones, even when the total work is the same. Each PR has one purpose, one scope, one verifiable change. If a PR description requires more than three bullets to explain, the PR should be split.

Require real command output, never paraphrase

Every verification step ends with terminal output, file contents, or HTTP responses pasted into the PR description. If the agent says it ran a command, the output is in the record. If there is no output, the command did not run.

Stop at clean checkpoints

The 2 a.m. loop happened because the operator did not stop when the work was done. Every engagement gets a clean stop condition: PRs merged, verification passed, deliverable shipped. When you hit it, leave. The next session starts fresh, not exhausted.

Every engagement makes the next one start from a higher floor. The Prompt Pack v3, the verification script, the smoke test suite, and the routing logic from this work are now permanent assets.

The shape of the work

Across a 13-14 hour engagement window, the active directing time was probably 7 to 8 hours of real decision-making work. The rest was agents running, exports moving, and a visa appointment in the middle. Most of the mobile-driven sessions ran while traveling or from a cafe.

That context matters. The point of the Director Model is not that one person can grind for 14 hours straight. The point is that one person can direct a multi-agent technical engagement through fragmented, mobile, travel-day conditions and still produce a real, verified, client artifact.

CALENDAR WINDOW

2 days

ACTIVE DIRECTING

~7 hrs

PRS MERGED

20

PRODUCTION TOUCHES

0

The honest limitation

This was code-side engagement work. Client trust building, scope negotiation, team dynamics, reading the room in a call — agents do not help with those. The throughput came from direction, not from the agents being powerful. The agents amplified judgment. The judgment was the variable.

The agents amplified judgment. The judgment was the variable.

What remains in the client's hands

Everything below requires either WP Engine admin access, Elementor WP Admin access, or a business decision that is the client's to make. None of it is code work. All of it is documented in the repo with priority order and effort estimates.

Action items for the dev team

Delete wp-phpmyadmin-extension entirely from WP Engine plugin directory.

Run tools/staging-verification.sh on WP Engine staging before launch. Share PASS/WARN/FAIL output.

Enable WP Rocket nonce refresh in Advanced Rules. Quick View and search will fail for anonymous visitors otherwise.

Deactivate AIO Migration plugins, duplicate-page, and wp-maintenance-mode before go-live.

Decisions for the client

Analytics stack consolidation. Four trackers running simultaneously. Which are required for launch?

Hero image and LCP. The remaining mobile gap. Elementor template change plus fetchpriority hint will move mobile to green.

Google Fonts trim. Roboto loading 9 weights. Trim to 4 in the Elementor kit.

Elementor template audit on heavy product pages (template ID 28135). 235 image tags target under 60.

What this engagement proves

The Director Model is a professional posture, not a productivity trick. It changes what fractional CTO work looks like and what it can deliver in a single working session.

The throughput number is interesting but secondary. The more important number is zero: zero production incidents, zero broken features, zero unverified changes on main. The agents shipped fast because the director kept the work tight and the verification rigorous, not because the agents were autonomous.

The Swiper stop is the best evidence for why bounded autonomy beats maximum autonomy. A more aggressive workflow would likely have shipped a Swiper scoping change that broke global JavaScript on every non-slider page. That is a production incident on a client site. The value of the stop condition was not the time saved by not shipping the broken change. The value was not having a broken client site to debug at 1 a.m.

The benchmark numbers are the proof that this is real, repeatable engineering work measured by Google's own tooling. The 32-point gain was not self-reported. PageSpeed Insights ran the same test twice on two real WP Engine environments and produced the result. Anyone with access to either URL can verify it.

The remaining gap to green on mobile is documented, scoped, and actionable. It is not a code problem. It is an Elementor configuration and image delivery problem that requires WP Admin access and a design call. Both are in the client's hands now.

The agents amplified judgment. The judgment was the variable.

About this work

Engagement type. Fractional CTO support on a WordPress migration audit and stabilization. Two-day engagement, mobile-driven, no production access required.

Tooling stack. Cloud Claude Code, Local Claude Code, OpenAI Codex. Local by Flywheel for the local environment. Private GitHub repo as source of truth. WP Engine for both before and after benchmark environments. PageSpeed Insights / Lighthouse 13.0.1 for verification.

Repository. Private repository. Every PR in this case study has a commit hash, description, and verifiable diff. The full prompt pack, director-model documentation, smoke test suite, and 30/60/90 roadmap are all in the engagement repository. Repository details and benchmark URLs available privately under client permission.

Client confidentiality. Client name and benchmark URLs withheld. All technical details, commit hashes, and metrics are real and verifiable.

WHEN THIS KIND OF ENGAGEMENT IS THE RIGHT FIT

This is the work I am best suited for: inherited technical mess, unclear risk, compressed timeline, senior judgment needed quickly, and a team that needs the path made visible. If that describes a project on your plate, the rest is a conversation.

Marcus Vale

Fractional CTO  •  AI-Native Engineering Direction

Eagle Rocket LLC  •  marcusvale.work
