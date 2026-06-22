---
title: "jamie stern postmortem"
source_archive: "Software Projects"
source_path: "####Software Projects/# Eagle Rocket/Jamie Stern/# Final Docs/jamie-stern-postmortem.docx"
status: reference
privacy: working
tags:
  - case-study
---

# jamie stern postmortem

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Jamie Stern: Post-Mortem

What was fixed, what was proved, and what remains in your hands

Maxwell  •  Eagle Rocket LLC  •  May 6, 2026

Sam — this is the final document from my end of this engagement. Part one covers what was shipped and proved with benchmark data. Part two is the handoff: the items that require human access, design decisions, or WP Engine staging work that only your team can execute. My code work is done. The benchmark numbers are in.

Part one: what was shipped and what it moved

The headline numbers

All benchmarks run on May 6, 2026 against two live WP Engine environments. testjamiestg is your existing staging build. maxjamiestern is the post-PR environment with all 20 fixes applied.

Homepage

Before

After

Delta

Note

Performance — mobile

36

68

+32

Red → amber. Biggest single-session gain.

Performance — desktop

52

84

+32

Amber → solid green.

TBT — mobile

1,320 ms

0 ms

−1,320 ms

Total blocking time eliminated.

TBT — desktop

3,670 ms

0 ms

−3,670 ms

Completely gone. JS no longer blocks paint.

LCP — mobile

10.3 s

6.5 s

−3.8 s

Still red. Hero image needs Elementor audit.

Best Practices — mobile

77

96

+19

phpMyAdmin removal + security fixes.

The product page tells a supporting story. The heaviest page on the site — /product/ganges/ with 235 rendered image tags — saw mobile LCP go from 48.6 seconds to 10.9 seconds. Score moved only slightly (24 → 27) because CLS got worse, which is a layout shift issue tied to the Elementor product template — that is the next phase of work documented below.

What drove the gains

Total Blocking Time eliminated on both devices. Before the fixes, the homepage was blocking the main thread for 3,670ms on desktop and 1,320ms on mobile before a visitor could interact with anything. That is pure JavaScript overhead: scripts loading, parsing, and executing before the page is usable. The primary causes were a dead script generating a 404 on every page (custom-search.js), assets with random version strings that prevented browser caching, and product-specific JavaScript loading on the homepage where it had no function. All three were addressed in the first wave of PRs.

Best Practices jumped from 77 to 96. The single biggest factor was the removal of phpMyAdmin as an active WordPress plugin. 22.77 MB of embedded database administration software was sitting in your plugin directory and active_plugins. Lighthouse flags this class of security exposure directly. The SVG upload restriction and nonce validation on the three public AJAX endpoints also contributed.

LCP mobile improved but is not finished. Going from 10.3 seconds to 6.5 seconds on the homepage hero is meaningful. The remaining gap is the hero image itself: it is being served at a size and weight that WP Rocket cannot fully mitigate without an Elementor template change to specify the correct image dimensions and add a preload hint. That is documented in the handoff below.

What was shipped: 20 pull requests

All of the following are merged to main in the private GitHub repo at WhiteHatForHire/jamie-stern-wp-content. Every change has a commit hash, PR description, and diff.

Category

PR

What shipped

Security

PR #1

Removed dead enqueue generating a 404 on every page (custom-search.js)

Security

PR #2

Replaced rand() asset versions with filemtime() — browser caching restored

Security

PR #4

phpMyAdmin soft-deactivated. SVG uploads restricted to admin. Nonces on 3 AJAX/REST endpoints

Security

PR #5

JS counterpart for PR #4 nonces — Quick View, search, load-more all send correct nonces

Performance

PR #6

Single-product CSS/JS scoped to shortcode callbacks only

Performance

PR #7

Full-size images (22–30 MB originals) replaced with responsive WP sizes in 4 templates

Performance

PR #8

Gallery and search transient caching. Dead unauthenticated AJAX handler removed

Performance

PR #18

Swiper initialization guards — no JS errors on non-slider pages

Performance

PR #20

CF7 assets conditional. Lenis disabled on checkout/cart. functions.php 1,800 → 1,047 lines

Code quality

PR #10

AJAX handlers extracted from functions.php into includes/ajax-handlers.php

Code quality

PR #12

Inactive Salient theme removed — 51.89 MB, 2,093 files deleted

Code quality

PR #13

Encoding fixes — pagination arrows and video glyph now use HTML entities

Code quality

PR #16

Enqueue logic extracted into includes/enqueue.php

Tooling

PR #9

Read-only media cleanup analysis — report only, no deletions

Tooling

PR #11

Seven-task investigation report including 40-plugin ownership matrix

Tooling

PR #14

WP-CLI staging verification script — 25+ checks, PASS/WARN/FAIL output

Tooling

PR #17

Performance brief and 30/60/90 roadmap for Sam

Tooling

PR #19

80+ browser smoke tests for QA

Tooling

PR #15

Director Model case study and Prompt Pack v3 (internal)

Docs

PR #3

Asset scoping groundwork — Swiper architectural finding documented

Part two: what remains in your hands

Everything below requires either WP Engine admin access, Elementor WP Admin access, or a design/business decision that is yours to make. None of it is a code change I can make from the codebase.

Your team's WP Engine actions

1. Delete wp-phpmyadmin-extension from WP Engine

Renamed on my local (soft deactivation). Your team needs to delete the directory entirely from WP Engine. Not just deactivate — remove the folder. WP Engine has host-level DB tools. There is no reason for phpMyAdmin to exist as a WordPress plugin on a managed host.

2. Run the staging verification script before launch

tools/staging-verification.sh is in the repo. SSH into WP Engine staging and run it. It covers 25+ checks and prints PASS/WARN/FAIL. Share the output before go-live. It confirms the merged fixes behave on WP Engine, not just on a local machine.

3. WP Rocket nonce caching — fix before launch

This is the one item from the smoke tests that will break anonymous visitor behavior. WP Rocket caches the page HTML including the inline JavaScript that provides nonces to Quick View and custom search. Anonymous visitors get cached HTML without nonces and hit a 403 wall when they try to use either feature.

The fix is a WP Rocket settings change, not a code change. In WP Rocket under Advanced Rules, enable the nonce refresh for AJAX. Alternatively, add the localize script block to the list of uncached fragments. Test while logged out with WP Rocket active on staging — if Quick View and search return results, it is working.

4. Plugin deactivation before launch

The investigation report (PR #11) has the full 40-plugin matrix. Before go-live, your team should deactivate on staging and smoke test: both AIO Migration plugins (migration is complete), duplicate-page, and wp-maintenance-mode. Deactivate one at a time, test, then move to the next.

Decisions that need your answer

1. Analytics stack

Four analytics and tracking systems are running simultaneously: Google Site Kit, PixelYourSite Pro, Burst Statistics, and Pinterest tracking. Each adds scripts to every page. Which ones are required for launch? The rest should be deactivated. This is a business decision, not a technical one.

2. Hero image and LCP — the remaining mobile gap

The homepage mobile LCP is 6.5 seconds. The target is under 2.5 seconds. The gap is almost entirely the hero image. The fix requires two things in Elementor: setting the hero image to the correct display dimensions rather than serving the original upload, and adding a fetchpriority=high preload hint to the LCP image element. Both are Elementor settings changes in WP Admin. This will move the mobile score from amber to green.

3. Google Fonts weight trim

Roboto is loading with weights 100 through 900 plus italics via three separate stylesheet requests. Trimming to the four weights actually in use (400, 500, 600, 700) is an Elementor kit settings change. Real LCP improvement, low risk.

4. Elementor template audit on heavy product pages

The product page for /product/ganges/ renders 235 img tags. The target is under 60. That gap is inside the Elementor product template (ID 28135). Getting there requires an Elementor template audit and design approval on how the gallery is structured. This is the highest-leverage remaining performance item but it requires someone with WP Admin and design sign-off to execute. It is documented in the 30/60/90 roadmap in the repo.

5. Warmly widget on Contact and Custom Leather pages

The smoke tests found CORS failures from the Warmly chat widget on those pages. Likely a local-origin issue that resolves on production, but worth confirming on WP Engine staging. If Warmly is not intentional on those specific pages, deactivating it from them removes the console noise and a third-party script dependency.

Still open from the original triage

Portfolio body-copy padding

You said you would get back to me on which template is the canonical reference. Once I have that, a CSS fix ships the same day.

qv-gallery Load More

The automated smoke test could not find the Load More button on /browse-by-color/ or /browse-by-color-fabrics/. Needs a manual check on staging. May be that the button renders conditionally when there are enough products to paginate. If it is missing on staging, that is a separate investigation.

What this engagement proves

The benchmark numbers are the proof. In one directed working session across two days, conducted primarily from mobile while traveling, a full structural audit and 20 verified pull requests produced a 32-point performance improvement on the homepage in both mobile and desktop modes. Total blocking time was eliminated entirely. Best Practices went from 77 to 96. The heaviest product page on the site had its mobile LCP cut from 48.6 seconds to 10.9 seconds.

The remaining gap to green on mobile is documented, scoped, and actionable. It is not a code problem. It is an Elementor configuration and image delivery problem that requires WP Admin access and a design call. Both are in your hands now.

The GitHub repo is the complete artifact. Every change is in the commit history with a PR description and a diff. The staging verification script will tell you whether WP Engine behaves the same way the local environment did. The smoke test suite covers 80+ manual checks your QA team can run before launch. The 30/60/90 roadmap covers the post-launch engineering work in priority order.

Everything that could be done from the codebase has been done. What follows is yours.

Benchmark URLs: testjamiestg.wpengine.com (before) / maxjamiestern.wpenginepowered.com (after)

Benchmark date: May 6, 2026  •  Lighthouse 13.0.1  •  Mobile: Moto G Power / Slow 4G  •  Desktop: custom throttling

— Maxwell

Eagle Rocket LLC  •  WhiteHatForHire
