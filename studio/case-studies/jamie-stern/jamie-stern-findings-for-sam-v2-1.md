---
title: "jamie stern findings for sam v2 (1)"
source_archive: "Software Projects"
source_path: "####Software Projects/# Eagle Rocket/Jamie Stern/Audits/jamie-stern-findings-for-sam-v2 (1).docx"
status: active
privacy: private/internal
tags:
  - case-study
---

# jamie stern findings for sam v2 (1)

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Jamie Stern: Updated Findings and Status

What was found, what has been fixed, and what remains for your team

Maxwell, fractional CTO  •  Eagle Rocket LLC  •  May 5, 2026

Context

Sam — this is an updated version of the original findings document I sent at the start of the day. The original had 15 findings from the structural audit. Since then, 20 pull requests have been merged to the private GitHub repo covering security, performance, and code quality improvements.

This document reflects current status: what has been fixed, what is your team's responsibility on WP Engine, and what still needs a decision from you before further action. The original flag list is reproduced here with updated status against each item.

Nothing in this document touched your WP Engine build. All work was done on my local copy. Your team can back-port any of these as reference patches whenever it makes sense.

Summary at a glance

Category

Detail

Fixed by Maxwell today (20 PRs)

10 of the original 15 findings addressed in full or in part

Your team's responsibility on WP Engine

4 items that need action on staging before launch

Needs your decision before action

3 items that are blocked on a call from you

Already handled by your team (per CK)

8 ClickUp items your team already resolved in parallel

Out of scope for this engagement

5 items that are design/content/architecture decisions

Fixed — merged to private GitHub repo

All of these were shipped as pull requests on my local copy. Each is verifiable in the commit history at WhiteHatForHire/jamie-stern-wp-content. Your team can back-port any of them as a reference diff.

Critical findings (from original audit)

Finding 3 — phpMyAdmin embedded as active plugin

Original finding: wp-phpmyadmin-extension was in active_plugins, adding database attack surface.

Status: Plugin folder renamed in PR #4, making it inactive. Full deletion from WP Engine is your team's action (see below).

Finding 4 — WP_CACHE disabled in wp-config

Original finding: WP_CACHE was commented out, meaning every page was a full PHP render.

Status: Fixed. WP_CACHE re-enabled, advanced-cache.php confirmed active.

High findings (from original audit)

Finding 5 — custom-search.js missing, generating sitewide 404

Original finding: Every page enqueued a script that didn't exist, generating a 404 on every page load.

Status: Fixed in PR #1. Dead enqueue removed. Zero 404s for this file.

Finding 6 — rand() asset versions breaking browser caching

Original finding: CSS/JS version parameters used rand(), so every page load got a unique URL. Browsers and CDNs couldn't cache anything.

Status: Fixed in PR #2. Replaced with filemtime() — stable, file-based version strings.

Finding 7 — Swiper and product assets enqueued globally

Original finding: Swiper CSS/JS, single-product CSS, and custom.js loaded on every page, including pages that didn't need them.

Status: Partially fixed. PR #6 scoped single-product CSS/JS to shortcode callbacks. PR #18 added Swiper initialization guards so pages without slider elements don't initialize Swiper. Full Swiper enqueue scoping is pending — Elementor's Swiper doesn't load on all page types, so the jsDelivr copy stays for now.

Finding 8 — Public AJAX/REST endpoints without nonces

Original finding: Three endpoints (Quick View, custom search, gallery load-more) were publicly accessible with no nonce validation, no rate limiting, and a dead handler with a signature mismatch.

Status: Fixed in PRs #4 and #5. Server-side nonce validation added to all three endpoints. JS counterpart sends matching nonces. Dead admin-ajax handler removed in PR #8.

Finding 9 — SVG uploads without sanitization

Original finding: SVG uploads were allowed with no sanitization. Any user with upload capability could store XSS in media.

Status: Fixed in PR #4. SVG uploads now restricted to admin role only.

Medium findings (from original audit)

Finding 12 — Full-size images in templates

Original finding: Five locations in functions.php called full-size images (22-30 MB originals) in grids, sliders, and search results.

Status: Fixed in PR #7. All four active locations replaced with layout-appropriate responsive sizes. Two were inside commented-out code blocks — left alone per protocol. All affected templates now emit srcset, lazy loading, and proper alt attributes automatically.

Finding 14 — Gallery counter doing full catalog scans

Original finding: gallery-load-more.php queried all products with posts_per_page = -1 on every cache miss (every 300 seconds).

Status: Fixed in PR #8. Replaced with versioned transient caching (30-minute TTL) with automatic invalidation on product save, gallery update, or color attribute change.

Finding 15 — Legacy plugin zips in public paths

Original finding: Salient theme, js_composer, Essential Grid, and Ultimate VC Addons zips were in public upload trash, disclosing old versions.

Status: Partially addressed. Salient theme directories removed from the repo in PR #12 (51.89 MB, 2,093 files). Upload trash zips are gitignored (not in the repo) — your team should empty uploads/wpmc-trash after a backup.

Additional improvements shipped beyond the original audit

PR

Area

What shipped

PR #8

Gallery/search performance

Dead admin-ajax handler removed (was also unauthenticated). Custom search responses cached for 5 minutes.

PR #9

Media cleanup analysis

Read-only analysis script produced. 8.5 GB uploads tree documented, backup/trash directories sized, cleanup candidates identified with commented-out commands.

PR #10

AJAX handler extraction

Quick View and custom search handlers extracted from functions.php into includes/ajax-handlers.php.

PR #13

Encoding fixes

Pagination arrows and video play glyph in rendered HTML replaced with safe HTML entities. 18 comment-only mojibake occurrences normalized to ASCII.

PR #16

Enqueue extraction

Asset enqueue logic extracted into includes/enqueue.php.

PR #18

Swiper guards

All 5 Swiper initializations in custom.js wrapped with element existence checks. No more ReferenceError on pages without sliders.

PR #20

CF7 + Lenis + shortcode extraction

CF7 assets now conditional. Lenis smooth scroll disabled on cart/checkout/my-account. 8 shortcode callbacks extracted into includes/shortcodes.php. functions.php reduced from ~1,800 to ~1,047 lines.

PR #14

Staging verification script

WP-CLI bash script covering 25+ checks across security, performance, plugin health, cron, media, and content. Run on WP Engine staging before launch.

Your team's responsibility on WP Engine

These items cannot be done from my local copy. They require WP Engine admin access or staging credentials.

1. Fully delete wp-phpmyadmin-extension from WP Engine

The plugin folder was renamed on my local copy (which deactivates it in WordPress), but your team needs to delete the directory entirely from WP Engine. Not just deactivate — full removal from the filesystem. This is a security item and should be done before launch.

2. Run the staging verification script

tools/staging-verification.sh is in the repo. SSH into WP Engine staging and run:

bash wp-content/tools/staging-verification.sh https://your-staging-url.wpengine.com

It prints color-coded PASS/WARN/FAIL for each check. Share the output before launch — it confirms the merged PRs behave on WP Engine, not just Local.

3. Test WP Rocket aggressive settings on staging

Two WP Rocket settings should be tested but are too risky to enable without staging verification: Remove Unused CSS and Delay JavaScript. Both can break Elementor and WooCommerce behavior if misconfigured. Enable one at a time, test thoroughly on product pages, checkout, and Quick View before enabling on production.

4. Review plugin deactivation candidates

The plugin audit identified five clear candidates for deactivation before launch: wp-phpmyadmin-extension (high risk, remove entirely), all-in-one-wp-migration and unlimited extension (migration complete, remove), duplicate-page (admin convenience only), wp-maintenance-mode (disable before go-live), media-cleaner and media-cleaner-pro (cleanup tool, risky to leave active). Your team should deactivate on staging first, smoke test, then production.

Needs your decision before action

1. Analytics stack consolidation

Your site is currently running four separate analytics/tracking systems simultaneously: Google Site Kit, PixelYourSite Pro, Burst Statistics, and Pinterest tracking. Each injects frontend scripts on every page load. This is likely more than you need and adds real page weight. Once you confirm which tools are actually required for launch, the others can be deactivated.

2. Google Fonts weight trim

Cached pages show Roboto loading with weights 100 through 900 plus italics, repeated three times via separate stylesheet requests. Most brands use 4-5 weights at most. Trimming to 400/500/600/700 is a real LCP improvement but requires changing Elementor kit settings in WP Admin — not something I can do from the codebase.

3. Elementor template audit for heavy product pages

The investigation found that data-elementor-id 28135 and 28084 appear repeatedly on the heaviest cached pages. These are likely the global templates responsible for the product and archive page weight. Auditing and simplifying them would be the biggest remaining page speed win, but it requires WP Admin access and design approval.

Still open

Portfolio body-copy padding (B-1)

You mentioned you'd get back to me on this. Once you confirm which portfolio page or template is the canonical reference, I can have a CSS fix in PR-ready shape within one session.

Already handled by your team

From the ClickUp triage, your team (CK/Shahid) already resolved these in parallel with today's work. No action needed from me.

Product image width and gallery width: CK set the image to cover

Tramezzo random gallery images: CK confirmed they were for testing

Image sliders looping continuously: CK set slider to loop back to first image

Footer Contact Us under Who We Are: CK added

Header Contact left of Log In/Search: CK set

Color sample names left-aligned, Roboto Light 14pt: CK confirmed

Blog search optimization: CK optimized for title-based results, updated footer link

Tear sheets/renderings partial cleanup: CK confirmed old replaced files removed

Performance context

The local WP Rocket cache shows the site is still heavier than the targets before launch, especially on product and gallery pages. The current measured state and targets are:

Metric

Current

Target

Homepage HTML

543 KB

Under 250 KB

Product HTML (/product/ganges/)

742.9 KB

Under 350 KB

Product script tags

78

Under 35

Product stylesheet links

37

Under 20

Initially rendered product images

235 (ganges)

Under 60

The biggest remaining gains are staging-tested WP Rocket settings, analytics consolidation, plugin reduction, and a deeper Elementor template audit on the heaviest product pages. A benchmark environment is being set up on a fresh WP Engine instance to measure the impact of today's PRs with real PageSpeed Insights numbers.

Smoke test suite: SMOKE_TEST_SUITE.md in the repo covers 80+ browser-based tests across every feature area. Your QA team can run it on WP Engine staging before launch.

Staging verification script: tools/staging-verification.sh in the repo covers 25+ automated checks via WP-CLI. Run it on WP Engine staging and share the output.

30/60/90 day roadmap: PERFORMANCE_ROADMAP_30_60_90.md in the repo covers what to do in each window leading up to and after launch.

— Maxwell

Eagle Rocket LLC  •  WhiteHatForHire
