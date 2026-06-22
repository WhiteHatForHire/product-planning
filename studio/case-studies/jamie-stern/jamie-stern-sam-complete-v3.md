---
title: "jamie stern sam complete v3"
source_archive: "Software Projects"
source_path: "####Software Projects/# Eagle Rocket/Jamie Stern/# Final Docs/jamie-stern-sam-complete-v3.docx"
status: reference
privacy: private/internal
tags:
  - case-study
---

# jamie stern sam complete v3

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Jamie Stern: What Was Found, What Was Fixed,

and How It Was All Done in One Day

A site audit, 20 pull requests, and a practical look at AI-native fractional CTO work

Maxwell  •  Eagle Rocket LLC  •  May 5, 2026

Sam — two things in this document. The first is a complete status report on your site: what the audit found, what has been fixed, what still needs action from your team, and what needs a decision from you. The second is an honest account of how all of this was done — the tooling, the workflow, and what it means for how engineering work gets done at this scale. You've mentioned you're watching the agentic AI space. I thought it was worth showing you what it looks like in practice, on your own codebase.

Part One: Your site

Everything in Part One is about the Jamie Stern codebase specifically. The audit findings, the fixes that shipped, what your team needs to do on WP Engine, and what needs your decision before anything else moves. Nothing in this section touched your WP Engine build. All work ran on a local clone. Your team can back-port any fix as a reference diff whenever it makes sense.

Status at a glance

Category

Detail

Fixed (20 PRs merged)

Security hardening, performance fixes, encoding cleanup, dead code removed, monolith refactored

Your team's action on WP Engine

4 items requiring staging access — none are code changes

Needs your decision

3 items blocked until you answer — analytics stack, Google Fonts, Elementor templates

Already handled by CK's team

8 ClickUp items resolved in parallel while this work ran

Open

Portfolio padding (B-1) — you said you'd get back to me

What was fixed

All 20 pull requests are logged in the private GitHub repo at WhiteHatForHire/jamie-stern-wp-content. Every change has a commit hash, a PR description, and a diff. Your team can inspect, back-port, or reference any of them.

Security

phpMyAdmin embedded as a plugin (PR #4). The plugin folder was renamed (soft deactivation). 22.77 MB, 3,201 files, direct database access through a WordPress plugin. Your team still needs to delete it from WP Engine entirely — see the next section.

Three public AJAX/REST endpoints with no authentication (PRs #4 and #5). Quick View, custom blog search, and the qv-gallery Load More button were all accessible to anonymous users with no rate limiting and no nonce validation. A bot could hammer these endpoints and force expensive WooCommerce database queries on every hit, bypassing page cache entirely. Server-side nonce validation was added to all three. The JavaScript counterpart was shipped in PR #5, which fetched the exact action strings from PR #4's diff via the GitHub API before writing a single line — no guessing, no mismatch. Both verified with valid and invalid nonces on the running local site before merge.

SVG uploads without sanitization (PR #4). SVGs can contain script tags. WordPress doesn't sanitize them by default. Any user with upload capability could store cross-site scripting payloads in the media library. Restricted to admin role only.

Performance

Sitewide 404 on every page (PR #1). functions.php was enqueuing a script called custom-search.js that didn't exist anywhere in the theme. Every single page load generated a 404 for this file. Console noise, wasted request, and the blog search behavior it was supposed to power was broken. Dead enqueue removed. Single line change, immediately verifiable.

Browser caching completely broken (PR #2). Four CSS and JavaScript files were enqueued with rand() as their version parameter. This means every page request generated a unique URL for each asset. Browsers see a unique URL, don't cache it, request it fresh every time. Browsers and CDNs can never reuse anything. Replaced with filemtime() — stable, file-based version strings that only change when the file actually changes.

Full-size images in templates (PR #7). Four active locations in the theme were calling full-size images directly. Original uploads on this site reach 22 to 30 MB per file. Pulling those into grids, sliders, and search result thumbnails is a serious page weight problem — especially given that 142,074 derivative image files (4.7 GB) had already been generated specifically to serve smaller sizes. Replaced with layout-appropriate responsive sizes. All affected templates now emit srcset, lazy loading, and alt attributes automatically.

Gallery and search performance (PR #8). The gallery load counter was querying all products with posts_per_page = -1 on every cache miss, which happened every 300 seconds. On a WooCommerce catalog this creates a full product rebuild from scratch every five minutes regardless of traffic. Replaced with versioned transients (30-minute TTL) with automatic invalidation hooks on product save, gallery update, and color attribute change. A dead admin-ajax handler was also removed — it was not just unused but unauthenticated, a secondary security item. Custom search responses now cache for five minutes.

Asset scoping (PRs #3, #6, #18, #20). Single-product CSS and JavaScript moved into shortcode callbacks (only loads when those shortcodes render). Swiper initialization guards added to custom.js so pages without slider elements don't attempt Swiper initialization and throw JavaScript errors. Contact Form 7 assets now only load on pages with actual CF7 forms. Lenis smooth scroll disabled on cart, checkout, and my-account pages where it interferes with form interactions.

Code quality

functions.php refactored from monolith to modules (PRs #10, #16, #20). The child theme's functions.php started at roughly 1,800 lines. AJAX handlers, enqueue logic, and shortcode callbacks have been extracted into three include files: includes/ajax-handlers.php, includes/enqueue.php, and includes/shortcodes.php. functions.php is now 1,047 lines. The monolith is meaningfully smaller and each include file has a single responsibility.

Salient theme removed (PR #12). The inactive Salient theme was still in the theme directory: 51.89 MB, 2,093 files. Removed entirely after confirming hello-elementor-child was active and zero Salient shortcodes existed in active theme PHP. That's 51 MB out of the repo.

Encoding fixes (PR #13). Pagination arrows and the video play glyph in rendered HTML were using literal byte sequences that could appear as garbled characters depending on the environment. Replaced with encoding-agnostic HTML entities.

Documentation and tooling shipped alongside the code

WP-CLI staging verification script (PR #14). tools/staging-verification.sh is a bash script your team can run on WP Engine staging via SSH. It covers 25+ checks with color-coded PASS/WARN/FAIL output: debug mode, WP_CACHE, plugin health, cron, media, nonce-protected endpoints, encoding. Run it before launch.

Browser smoke test suite (PR #19). SMOKE_TEST_SUITE.md is 80+ browser-based test cases covering every feature area: homepage slider, product gallery, Quick View, custom search, gallery load-more, contact form, footer, mobile, console errors, network tab. Written for a non-developer QA tester. Check to do, check what you should see, pass/fail column.

Performance brief and 30/60/90 roadmap (PR #17). SAM_PERFORMANCE_BRIEF.md is a plain-English summary of the performance state with no jargon. PERFORMANCE_ROADMAP_30_60_90.md lays out what to do in each window before and after launch with specific targets.

Media cleanup analysis (PR #9). Read-only analysis of the 8.5 GB uploads tree. Backup and trash directories sized, cleanup candidates identified, commands documented but not executed. Needs your explicit approval and a verified backup before any deletion runs.

Investigation report (PR #11). Seven-task deep-dive: Salient database cleanup, cron errors, encoding, sitemap and robots.txt, product gallery HTML weight across 55 pages, Elementor and Wordfence fatal stack traces, and a full plugin ownership matrix for all 40 active plugins categorized by risk, necessity, and deactivation priority.

What your team needs to do on WP Engine

These four items need staging access. None of them are code changes. None of them are in the GitHub repo.

1. Delete wp-phpmyadmin-extension entirely

The folder was renamed on the local copy (which deactivates it in WordPress). Your team needs to delete it from the WP Engine plugin directory completely. Not just deactivated — gone. WP Engine has its own database tools at the host level. There is no reason to have phpMyAdmin embedded as a WordPress plugin on a managed host.

2. Run the staging verification script

SSH into WP Engine staging and run:

bash wp-content/tools/staging-verification.sh https://your-staging-url.wpengine.com

It prints color-coded PASS/WARN/FAIL for each check. Share the output before launch. It confirms the merged fixes behave on WP Engine, not just on my local.

3. Test WP Rocket aggressive settings on staging

Two settings that could move the Lighthouse numbers significantly need a controlled staging test before production: Remove Unused CSS and Delay JavaScript. Both can break Elementor and WooCommerce if misconfigured. Enable one at a time, test thoroughly on product pages, checkout, and Quick View before enabling on production.

4. Review plugin deactivation candidates

The investigation report (PR #11) documents the full 40-plugin inventory with deactivation recommendations. Top five for your team to review before launch: wp-phpmyadmin-extension (remove entirely), both AIO Migration plugins (migration is done, remove), duplicate-page (admin convenience only), wp-maintenance-mode (disable before go-live).

What needs your decision

1. Analytics stack

Your site is running four separate analytics and tracking systems simultaneously: Google Site Kit, PixelYourSite Pro, Burst Statistics, and Pinterest tracking. Each injects scripts on every page load. Which ones do you actually need for launch? The rest can be deactivated, and the page weight reduction is real.

2. Google Fonts weight

Cached pages show Roboto loading with weights 100 through 900 plus italics, via three separate stylesheet requests. Most brands use four or five weights at most. Trimming to 400/500/600/700 requires a change in the Elementor kit settings — I can't do that from the codebase. Worth a conversation about which weights are actually in use.

3. Elementor template audit on heavy product pages

The investigation found that two Elementor template IDs (28135 and 28084) appear on the heaviest cached pages. The product page for /product/ganges/ currently renders 235 img tags in the HTML source. The target is under 60. Getting there requires auditing and simplifying those Elementor templates, which means WP Admin access and design approval. This is probably the highest-leverage remaining performance item.

Where the performance numbers stand

These measurements are from the local WP Rocket cache. The benchmark environment on a fresh WP Engine instance is being set up now — the AIO Migration export is in progress and needs to import and stabilize before PageSpeed Insights can run against both URLs. This document is a work in progress in that sense: the code is shipped and verified, but the business proof (before/after PageSpeed numbers) is not yet in hand. That section will be updated once the benchmark completes.

Metric

Current (cached)

Target before launch

Homepage HTML weight

543 KB

Under 250 KB

Product page HTML (/product/ganges/)

742.9 KB

Under 350 KB

Product page script tags

78

Under 35

Product page stylesheet links

37

Under 20

Initially rendered product images

235 (ganges)

Under 60

The remaining gap between current and target is primarily the Elementor template audit, the analytics stack decision, and the WP Rocket aggressive settings test. Those are all on your side of the table now.

Part Two: How this was done

Sam, you mentioned you’re watching the agentic AI space and trying to figure out what’s real versus hype. What follows is an honest account of how this work actually happened. The engagement window spanned two days, but the active directing time was probably 3 to 4 hours of real decision-making work. The rest was agents running, exports moving, and a visa appointment in the middle. Most of the mobile-driven sessions ran while traveling or from a café. That context matters, because the stronger story here is not “I coded for 14 hours.” It’s that a multi-agent technical engagement ran through fragmented, travel-day conditions and still produced a real, verified, client artifact. No pitch. Just the record.

The setup: starting from zero on an inherited codebase

The engagement started at 11pm on May 4 with a download of your WP Engine staging build via All-in-One WP Migration. By 1:30am the site was running in Local by Flywheel on a Windows laptop in Bali. By morning it had a clean private GitHub repo with the entire wp-content directory under version control, uploads excluded.

Everything that followed was driven from mobile during the day: reviewing pull requests in the GitHub app, sending prompts to agents from a phone, checking back when work was complete. The desktop came into play for verification: confirming that fixes actually worked against the running local site before merge.

No production access was touched at any point. The GitHub repo is the artifact. Your team applies changes to WP Engine on their own schedule.

Three agents, one repo, clear routing

The work ran across three distinct AI tools, each used for a specific job:

Cloud Claude Code (claude.ai/code). Connected to the GitHub repo. Ran in Anthropic's cloud infrastructure, accessible from a phone. Used for code generation: reading the codebase, writing the fix, committing it, opening the PR. Zero local access — it can't reach a site running on your laptop.

Local Claude Code (Windows desktop). Running on the same machine as Local by Flywheel. Could make HTTP requests to the running local site and inspect the filesystem in real time. Used for verification: confirming fixes worked against the actual site before merging.

Codex (OpenAI's coding agent). Used for triage, analysis, and documentation: the ClickUp triage, the investigation report, the smoke test suite, the 30/60/90 roadmap. When the deliverable was a report rather than code, Codex was the right tool.

The routing rule was simple and held throughout: Cloud CC for code, local CC for verification, Codex for synthesis. When a task crossed surfaces, it was split into two agent jobs with a clear handoff.

The full PR timeline

Every PR that merged to main, in order, with what it did and which tool shipped it.

PR

Title

Agent

What it did

#1

Fix: remove enqueue for non-existent custom-search.js (sitewide 404)

Cloud CC

Removed dead enqueue in functions.php. Eliminated 404 on every page load.

#2

Fix: use filemtime() instead of rand() for asset versions

Cloud CC

4 lines. Restored browser caching for custom.css, blog.css, blog.js, single-product.css.

#3

Scope single-product assets to shortcode callbacks (Swiper deferred)

Cloud CC

Agent hit Swiper architectural blocker. Shipped safe subset only.

#4

Audit batch: security + config fixes (5 shipped, 1 report-only)

Cloud CC

phpMyAdmin soft-deactivated. SVG restricted. Nonces on 3 endpoints. AI1WM version check.

#5

Frontend nonces for PR #4 (Quick View, custom search, qv/v1/load-more)

Cloud CC

JS counterpart. Agent verified exact action strings via GitHub API before writing.

#6

Bugfix/scope frontend assets shortcode callbacks

Cloud CC

Recovery of PR #3 work. Single-product assets properly scoped.

#7

Replace 'full' image size with responsive WP sizes (4 sites)

Cloud CC

4 active template locations fixed. srcset, lazy load, alt attributes added.

#8

qv-gallery + custom-search perf: real transient cache, invalidation, dead handler

Cloud CC

Strategy-first. 5 commits. Dead unauthenticated handler removed as bonus.

#9

Add read-only media cleanup analysis script and report

Local CC

Report only. No deletions. Needs Sam approval before any cleanup runs.

#10

Refactor: extract AJAX handlers from functions.php into includes/ajax-handlers.php

Cloud CC

First monolith slice. -200 lines from functions.php.

#11

Docs: add seven-task investigation report

Codex

INVESTIGATION_REPORT.md. 7 deep-dive tasks including 40-plugin audit.

#12

Chore: remove inactive Salient theme and bundled plugin zips

Local CC

51.89 MB, 2,093 files deleted after safety checks.

#13

Fix(encoding): mojibake to HTML entities in rendered output, ASCII in comments

Cloud CC

Pagination arrows, video glyph, 18 comment normalizations.

#14

Docs: add WP-CLI staging verification script and checklist

Local CC

25+ checks, PASS/WARN/FAIL output. Run on WP Engine staging before launch.

#15

Docs: add Director Model case study and Prompt Pack v3 additions

Codex

Internal workflow documentation. Not client-facing.

#16

Refactor: extract enqueue logic from functions.php into includes/enqueue.php

Cloud CC

Second monolith slice.

#17

Docs: add Sam performance brief and 30/60/90 roadmap

Codex

SAM_PERFORMANCE_BRIEF.md and PERFORMANCE_ROADMAP_30_60_90.md.

#18

Fix(swiper): add existence guards to custom.js Swiper initializations

Local CC

5 Swiper inits guarded. Prerequisite for future full Swiper scoping.

#19

Docs: add browser smoke test suite

Codex

SMOKE_TEST_SUITE.md. 80+ test cases, structured for non-developer QA.

#20

Perf + refactor batch: CF7 scope, Lenis scope, shortcodes extract

Cloud CC

Third monolith slice. functions.php from ~1800 to 1047 lines.

What the agents actually did well — and where they didn't

The honest version, because the hype around AI coding tools obscures what they're actually useful for.

The Swiper stop — the single most important moment

PR #3 was supposed to scope all globally loaded assets including Swiper to the pages that actually need them. The agent opened the relevant files and discovered that custom.js calls new Swiper() unconditionally at page load on four separate lines. Moving Swiper out of global loading without guards would throw a JavaScript error on every page without a slider — and that error would stop all other JavaScript on the page from running.

The agent stopped. It documented the exact line numbers, explained why the change was unsafe, proposed three alternative paths, and shipped only the safe subset. It did not guess. It did not plow through.

A Replit-style agent — the kind that prioritizes momentum over precision — would have shipped the broken change with a clean commit message. That would have been a JavaScript failure on every non-slider page of your site. Catching it before it happened is worth more than any throughput number.

PR #5: verifying action strings from source before writing

PR #5 was the JavaScript counterpart to PR #4's server-side nonce validation. The agent needed the exact action strings from the server-side code in order to write matching strings in the JavaScript. Rather than trusting its own reading of the conversation, it fetched PR #4's diff directly from the GitHub API and extracted the strings from the source. The nonce coupling held perfectly through verification on the running site.

PR #8: strategy table before touching any code

The gallery performance prompt required the agent to produce a strategy table before implementing anything. It found five things worth knowing before editing: the cache layer being used (wp_cache_*) was request-scoped and a no-op without a persistent object cache; the dead admin-ajax handler was not just unused but also unauthenticated; and search response caching wasn't in the original spec but was a natural addition. The strategy was reviewed before the first file was modified.

Where things went wrong

Unsanctioned git history rewrite. During the initial baseline setup, the agent squashed three prior commits into one root commit without being asked. The code was intact. The history was not. A permanent rule was added to every subsequent prompt: do not rewrite git history under any circumstances.

Fabricated completion notifications. During a size measurement step, the agent produced lines that looked like real timestamped completion messages for a command that was still running. It admitted the notifications had been speculative when pressed for actual output. Rule added: real command output or 'I cannot verify.' Nothing in between.

Stacked-PR base branch confusion. PR #3 was created with PR #2's branch as its base. When merged in the wrong order, the changes went into the wrong branch. Recovery was clean but required careful investigation. Rule added: verify the intended base branch before creating each PR, merge bottom-up.

What this means for your engineering workflow

Sam, I'm not going to tell you to fire your dev team and replace them with AI agents. That's not what happened here and it's not what this work shows.

What it does show is that a single person with the right workflow can audit, fix, document, and ship at a speed that doesn’t make sense by traditional development economics. Twenty pull requests on a codebase I’d never seen, verified before every merge, directed from a phone in Bali across a fragmented travel day. The active decision-making time was somewhere around 3 to 4 hours. The rest was agents running. That math only works because the agents are doing the mechanical execution while the human does the judgment work: what to fix, in what order, with what constraints, and when to stop.

For your team specifically, I'd point to three things:

The verification pattern is something your dev team should adopt regardless of whether they use AI agents. Every change verified with valid and invalid inputs, both the happy path and the rejection path, before merge. That discipline caught the Elementor template ID issue (a product page URL doesn't always give you a product ID) and the REST route method confusion (POST only, not GET). That's just good practice.

The staging verification script is immediately useful for your team. tools/staging-verification.sh runs 25+ checks on WP Engine via WP-CLI in about 90 seconds. It would have caught the WP_DEBUG issue, the WP_CACHE issue, and the phpMyAdmin plugin if it had existed before this build started. Worth running on every future deployment.

The investigation report gives your team a prioritized plugin list they didn't have. 40 active plugins, categorized by risk, necessity, and deactivation priority. Most WordPress sites carry plugins they stopped needing years ago. Knowing which ones are safe to remove and in what order is usually weeks of careful detective work. It's in INVESTIGATION_REPORT.md in the repo.

What the prompts actually looked like

Since you're evaluating this workflow, here are two real prompts from the engagement. These aren't polished for presentation — they're exactly what was sent.

Prompt sent for PR #1 (custom-search.js fix)

TASK: Fix the missing custom-search.js enqueue.

CONTEXT

- Repo: jamie-stern-wp-content (you are at the repo root, which IS wp-content)

- File: themes/hello-elementor-child/functions.php

- Issue: around line 1757, the theme enqueues

get_stylesheet_directory_uri() . '/custom-search.js'

but the file does not exist. Every page generates a 404.

DO

1. Read functions.php and find the exact enqueue block.

Report the line number and surrounding 10 lines.

2. Check if the script's logic is actually used elsewhere

3. Choose ONE fix and explain why:

a) Create a stub custom-search.js

b) Remove the enqueue if no dependent code exists

c) Move the enqueue to only fire on pages that need it

4. Implement on branch: bugfix/custom-search-js-404

5. Commit with a clear message

6. Open a PR

DO NOT

- Refactor adjacent code

- Touch other enqueues

- Push to main directly

- Rewrite history

DO NOT FABRICATE TOOL OUTPUT.

Prompt sent for PR #8 (gallery performance — strategy first)

TASK: Optimize qv-gallery and custom search AJAX/REST performance

without changing frontend behavior.

CONTEXT

- Recent merged work to NOT undo: PR #4 nonces, PR #5 JS, PR #7 images

- This PR is about query/cache efficiency, not security or UX

DO

1. Identify -1 queries, full iterations, short cache TTLs

2. Propose ONE strategy BEFORE implementing:

a) Replace -1 query with paginated SQL via $wpdb

b) Move data into transients with invalidation hooks

c) Increase cache TTL with explicit invalidation

d) Remove duplicated handlers if REST is the actual path

3. After reporting strategy, implement on bugfix/qv-gallery-performance

4. For search AJAX: add transient cache for common search strings

STOP CONDITIONS

- If -1 with bounded result set: leave it, document why

- If transient invalidation requires plugin code: STOP and document

DO NOT FABRICATE TOOL OUTPUT.

The pattern is consistent across all 20 PRs: a specific task, a narrow scope, explicit stop conditions, and a hard prohibition on fabricating output. The agents work well when the instructions are tight. When instructions are vague, agents drift — just like people.

What comes next

In order of priority:

1. Benchmark results. Once the AIO Migration export imports cleanly to the WP Engine benchmark environment, run PageSpeed Insights against both URLs — your existing staging and the new environment with all 20 PRs applied. That before/after number is what completes this case study. Right now the proof is operational and architectural. Once the benchmark runs, it becomes business proof.

2. Your team's four WP Engine items. Delete phpMyAdmin, run the staging verification script, test WP Rocket aggressive settings, review the plugin deactivation list. These are blocking launch quality, not blocking launch date — but they should happen before go-live.

3. Your three decisions. Analytics stack, Google Fonts weights, Elementor template audit authorization. Once I have answers on those, the remaining performance work has a clear path.

4. Portfolio padding (B-1). You said you'd get back to me on which template is the canonical reference. Once I have that, CSS fix ships the same day.

5. The 30/60/90 roadmap. PERFORMANCE_ROADMAP_30_60_90.md in the repo covers the larger items that are right-sized for post-launch work: media library cleanup, plugin footprint reduction, deeper Elementor template optimization. Worth a call once the launch pressure is off.

Everything in this document is verifiable. The GitHub repo has the commit history, the PR descriptions, the diffs. The staging verification script will tell you whether the changes behave the same way on WP Engine that they did on my local. And I'm here for questions on any of it.

— Maxwell

Eagle Rocket LLC  •  WhiteHatForHire
