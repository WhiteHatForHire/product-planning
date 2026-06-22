---
title: "jamie stern work status checklist"
source_archive: "Software Projects"
source_path: "####Software Projects/# Eagle Rocket/Jamie Stern/jamie-stern-work-status-checklist.docx"
status: active
privacy: private/internal
tags:
  - case-study
---

# jamie stern work status checklist

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Jamie Stern — Work Status Checklist

Every task from the audits, triage, and ClickUp — by status

May 5, 2026  •  3pm Bali time

Use this as: a tracking list. Each section has a clear status. Strikethrough or check off as you ship them. Items in 'Shippable' need no Sam input. Items in 'Blocked' need an answer first. Items in 'Parked' need architectural work or a future window.

✓ Shipped to main (9 PRs merged)

All work on the local copy and private GitHub repo. Zero production deploys.

PR

What shipped

Result

Maps to audit/triage

#1

Custom-search.js dead enqueue removed

Eliminated sitewide 404

Audit High #5

#2

rand() → filemtime() asset versions

Browser caching restored

Audit High #6

#6

Single-product CSS/JS scoped into shortcode callbacks

Page weight reduced on non-product pages

Audit High #7 (partial — Swiper deferred)

#5

Frontend nonces sent from JS for three endpoints

JS counterpart for security batch

Audit High #8

#4

Server-side nonces + input validation on Quick View, custom search, qv-gallery REST

Public endpoint hardening + SVG admin-only + phpMyAdmin folder rename

Audit High #8, #9; Critical #3

#7

'full' image rendering replaced with responsive sizes in 4 templates

srcset/lazy/alt gained automatically

Audit Medium #12, Performance #1

#8

Gallery/search performance: transient cache w/ versioning, dead admin-ajax handler removed, search response cache

21% REST speedup, 37% search speedup, removed unauth surface

Audit Medium #14, Performance #4

#9

Media cleanup analysis script + report (read-only)

Data for cleanup decisions, no media touched

Audit Critical #11, Performance #5

Local environment hardening (no PR needed)

✓ wp-config.php hardened: WP_DEBUG_DISPLAY off, duplicate WP_CACHE removed

✓ advanced-cache.php renamed to .bak

✓ Git initialized on wp-content with code-only tracking

✓ uploads/ excluded from version control

✓ Comprehensive .gitignore for cache, logs, migration artifacts

→ Shippable now (no Sam input needed)

Order matters. Top 3 are highest leverage, smallest risk.

Currently in flight

PR Batch (Local CC): Footer sitemap link + Roboto weight trim + duplicate Swiper removal. Three independent items, one PR.

Next up

#

Task

Why it matters

Source

S-1

Self-host Google Fonts (after weight trim lands)

Remove fonts.googleapis.com dependency, real LCP/FCP win

Performance Audit Section 6, Fonts secondary

S-2

functions.php AJAX extraction (start monolith refactor)

Pull AJAX handlers (quick view, custom search) into includes/ajax-handlers.php. Test coverage already in place from PRs #4/#5/#8.

Audit Low #23

S-3

Static asset cache headers in Local Nginx config

Long-lived immutable cache for fingerprinted assets. Doc reference for Sam's team.

Performance Audit Section 7

S-4

Remove inactive Salient theme + bundled plugin zips

Reduces backup size, removes legacy code surface

Audit Medium #15, Low #22

S-5

Cron / Action Scheduler reschedule errors investigation

Flush schedules, document stale ones for Sam's staging team

Audit Medium #13, Performance Section 18

S-6

Encoding fixes for child theme PHP comments

Replace mojibake (categorÃ­a, â”€, âœ…) with proper UTF-8

Audit Low #24

S-7

Robots.txt + sitemap verification

Confirm Yoast sitemap output works, document for Sam

Audit Low #25

Notes on shippable items

S-1 (self-host fonts) depends on the in-flight weight trim landing first. Then it's a clean follow-up.

S-2 (functions.php split) is the start of the 60-day monolith refactor. Worth doing now while test coverage from PRs #4/#5/#8 is fresh.

S-3 cache headers only affects Local environment, not WP Engine. Marginal value but easy. Document and move on.

S-4 inactive theme cleanup is mostly cosmetic — reduces repo size, no runtime impact. Low priority but easy to ship.

S-5 cron errors may be misleading on Local (different scheduler than production). Investigate carefully.

✗ Blocked on Sam (8 questions)

These are the 8 questions in tonight's email. Until Sam answers, don't act on them.

Q#

Item

Sam's answer needed

Source

B-1

Portfolio body-copy padding to match new blog body copy

Which page/template is the canonical reference?

ClickUp Client Feedback

B-2

Hero block height 788 → 745, padding 75px top/bottom

Global, home only, or specific templates?

ClickUp Client Feedback

B-3

Custom Leather page mockup not findable in Figma

Where is it?

ClickUp Client Feedback

B-4

360 furniture videos: where displayed

Product gallery, separate tab, custom viewer?

ClickUp Client Feedback

B-5

Furniture Landing + Hand-tufted page builds

Approved to build, or queued for estimate?

ClickUp Client Feedback

B-6

Global Bugs (plugin/theme issues, mobile nav, page duplication)

Subtask descriptions didn't export. What are the actual issues?

ClickUp Global Bugs

B-7

Tear sheets/renderings bulk update for furniture and carpet

Final file-to-product mapping + verified backup?

ClickUp Tear Sheets

B-8

CDN/DigitalOcean account decision

Who owns it, and confirmed for large 3D/360 media?

ClickUp Storage Options + Launch Prep

Ship-ready when answered

If Sam answers Q1, Q2, Q6: we have 3 small visible wins ready to ship: portfolio padding (B-1), hero height (B-2), and the Global Bugs subtasks (B-6) once described.

If Sam answers Q3, Q4, Q5, Q7, Q8: these are larger scope items that need design/content/architecture decisions. They become future work, not next-session work.

⏸ Parked (architectural blockers or future windows)

These are real findings that the audit identified but aren't shippable in current form. Each has a specific reason it's parked.

#

Item

Why parked

When unparked

P-1

Swiper scoping (move out of global enqueue)

custom.js calls new Swiper() unconditionally at document.ready on lines 40, 60, 85, 97. Moving Swiper out of global enqueue would throw ReferenceError site-wide.

Refactor custom.js with Swiper guards first, then scope. Substantial work.

P-2

functions.php full monolith refactor (84KB → multi-file)

Just starting (S-2 is the first split). Real work spans weeks.

Sequential extractions: AJAX → search → sliders → product accordions → upload MIME

P-3

Plugin footprint reduction

40 active plugins. Some clearly removable, others need Sam's input on what's required for business operations.

Build plugin ownership matrix with Sam after launch readiness work

P-4

Media library cleanup execution (8.5 GB → 30-50% smaller)

PR #9 produced the analysis. Actual deletion needs human approval and verified backup.

Execute after Sam approves cleanup candidates and confirms backup

P-5

Product gallery refactor (reduce HTML weight 743KB → <350KB)

Requires changing how product templates render galleries. Not a code-only fix; affects layout and UX.

Bigger scope; needs design/UX decisions and Sam alignment

P-6

WP Rocket aggressive settings (Remove Unused CSS, Delay JS)

These work better when tested on staging-like infrastructure. Local Flywheel is too different.

Test on Sam's WP Engine staging in coordination with his team

P-7

Production Lighthouse / PageSpeed Insights baseline

Need to run from the internet, not local. Requires staging URL accessible externally.

Coordinate with Sam to get staging accessible or run via WP Engine's tools

P-8

Reduce third-party connections (PixelYourSite, Pinterest, Burst, GA, Site Kit)

These are tracking/analytics decisions, not code decisions. Needs Sam's call on what's required.

Audit with Sam after launch

P-9

Database/admin tools warning (audit Critical #4)

wp-phpmyadmin-extension flagged. Folder renamed in PR #4 but full plugin removal needs admin UI access on staging.

Sam's team to remove from active_plugins on WP Engine

P-10

Live fatals from WC logs (Elementor + Wordfence)

These were on production, not local. Verify resolved on Sam's WP Engine staging build.

Sam's team verifies, can support if logs are accessible

✓ Already shipped by Indian team (per CK comments)

From Codex triage of ClickUp comments. These are off your plate.

Product image width / gallery width: CK said 'set the image to cover'

Tramezzo random gallery images: CK said random images were for testing, asked if deleted now

Image sliders looping continuously: CK said slider set to loop back to first image

Footer Contact Us under Who We Are: CK added

Header Contact left of Log In/Search: CK set

Color sample names left-aligned, Roboto Light 14pt: CK confirmed

Moving Blog to WordPress: CK said search optimized for title-based results, footer blog link updated

Tear Sheets/Renderings partial cleanup: CK said old replaced files removed

◇ Scope extensions (separate engagements)

These are tagged 'scope extension' in ClickUp or are clearly outside the cutover support scope. Don't act unless explicitly added to scope.

#

Item

Notes

X-1

AI Search Optimization

ClickUp scope-extension tag. Needs content/schema strategy.

X-2

FAQ page build

ClickUp scope-extension tag. Design/content/page-build task.

X-3

Furniture Landing + Hand-tufted page builds

Page build work, not bug fix.

X-4

Custom Leather page rebuild from new mockup

Design/template work.

X-5

Launch Preparation full punch list

CDN, Yoast live switch, backup/revert, launch window — coordination work, not code.

Tonight's runway (5 hours, until Sam wakes)

In flight right now

Local CC: Footer sitemap + Roboto trim + duplicate Swiper removal (one PR, three commits)

Next queue

S-1: Self-host Google Fonts (after weight trim PR lands)

S-2: functions.php AJAX extraction (cloud CC, parallel-safe)

If still energized

S-3: Static asset cache headers (small, easy)

S-4: Salient theme cleanup (small, mechanical)

S-5: Cron/Action Scheduler investigation (research-heavy)

End-of-runway tasks

Send Sam email/Slack with 8 questions when he's online

Update archive doc with whatever PRs landed

Generate updated Field Log entry if anything noteworthy happened

Engagement stats at archive time

9 PRs merged to main

28 audit findings categorized

16 ClickUp items triaged

8 of those resolved by Indian team in parallel

Of remaining 8 ClickUp items, 3 ship-ready when Sam answers, 5 are scope/decision items

3 agent surfaces in active rotation: Cloud CC, Local CC, Codex

0 production deployments

Status as of May 5, 2026, 3pm Bali. Update as work lands.
