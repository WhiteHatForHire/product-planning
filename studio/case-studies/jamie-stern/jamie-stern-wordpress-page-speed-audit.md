---
title: "# Jamie Stern WordPress Page Speed Audit"
source_archive: "Software Projects"
source_path: "####Software Projects/# Eagle Rocket/Jamie Stern/Audits/# Jamie Stern WordPress Page Speed Audit.docx"
status: active
privacy: working
tags:
  - case-study
---

# # Jamie Stern WordPress Page Speed Audit

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Audit

# WordPress Page Speed Audit

Audit date: 2026-05-05

Site root inspected: `C:\Users\Maxwel\Local Sites\jamie-stern`

Mode: report-only. No site behavior was changed.

## Executive Summary

The site has significant speed upside. The biggest issues are oversized HTML pages, too many render-blocking CSS and JS assets, very heavy image usage on product/category pages, full-size image rendering in the active child theme, public dynamic AJAX/REST gallery paths, and a huge media library that encourages accidental heavyweight delivery. Local page requests took 12.9-29.2 seconds for representative pages even with WP Rocket cache files present. Local timings are not a production Lighthouse substitute, but the payload and asset counts are concrete and directionally strong.

Good news: the latest merge already fixed two earlier problems. `WP_CACHE` is now enabled in `wp-config.php`, and `rand()` asset versions in the child theme have been replaced with stable `filemtime()` versions. Those changes should help cacheability. The next major wins are to reduce page weight and request count, especially on product pages.

## Measured Local Pages

Measured with `Invoke-WebRequest -UseBasicParsing` against `jamie-stern.local`.

| URL | Status | Time | HTML KB | CSS links | Script tags | Image tags | JPG refs |

|---|---:|---:|---:|---:|---:|---:|---:|

| `/` | 200 | 12.9s | 543.0 | 35 | 70 | 59 | 441 |

| `/product/ganges/` | 200 | 23.4s | 742.9 | 37 | 78 | 235 | 1,640 |

| `/contemporary/3/` | 200 | 20.3s | 567.8 | 31 | 69 | 81 | 684 |

| `/product/dune-sofa/` | 200 | 29.2s | 527.3 | 37 | 77 | 54 | 369 |

WP Rocket cache files exist for these pages. Cached HTML sizes are still large:

| Cached page | HTML KB | CSS | Scripts | Images |

|---|---:|---:|---:|---:|

| `product/ganges/index.html` | 742.9 | 37 | 78 | 235 |

| `contemporary/3/index.html` | 567.8 | 31 | 69 | 81 |

| `index.html` | 543.0 | 35 | 70 | 59 |

| `product/dune-sofa/index.html` | 527.3 | 37 | 77 | 54 |

## Highest-Impact Recommendations

### 1. Reduce product page image payload

- Affected files/paths:

- `app/public/wp-content/themes/hello-elementor-child/functions.php`

- `app/public/wp-content/uploads`

- Product pages such as cached `product/ganges/index.html`

- Evidence:

- `/product/ganges/` renders 235 `<img>` tags and 1,640 JPG references in the HTML.

- Cached `product/ganges/index.html` is 742.9 KB before assets are downloaded.

- The upload library has 157,108 files / 8.5 GB.

- Largest local originals include 30.59 MB, 24.43 MB, 23.87 MB, and 22.18 MB JPEGs.

- `functions.php` renders full-size images at lines 345, 683, 736, 1447, and 1762.

- Impact:

- Large product pages can delay HTML parse, LCP image download, image decode, browser memory use, and mobile performance.

- Recommended fix:

- Replace `full` image usage with explicit layout-appropriate sizes.

- Use `wp_get_attachment_image()` instead of raw `the_post_thumbnail_url()` so WordPress emits `srcset`, `sizes`, width, height, and lazy loading.

- For product galleries, initially render only the first visible slide plus nearby thumbnails; lazy-load the rest after interaction.

- Add max upload dimensions and compress existing originals.

- Estimated effort: Medium to Large.

- Expected gain: High. This is likely the largest frontend win.

### 2. Scope CSS/JS assets to the pages that need them

- Affected file: `app/public/wp-content/themes/hello-elementor-child/functions.php`

- Evidence:

- Lines 35-52 enqueue jQuery, Swiper CSS/JS, and `custom.js` globally.

- Product cached pages load 37 CSS links and 77-78 script tags.

- Home cached page loads 35 CSS links and 70 script tags.

- Product pages include WooCommerce, Elementor, Elementor Pro, PixelYourSite, Pinterest, Contact Form 7, Swiper, Lenis, Burst, CookieYes, and custom child-theme assets.

- Impact:

- Global scripts/CSS increase render-blocking work, JS parse/execute time, and third-party connections on pages that do not need them.

- Recommended fix:

- Only enqueue Swiper on templates/shortcodes that render sliders.

- Only enqueue WooCommerce single-product custom code on product pages.

- Only enqueue blog assets on blog/search pages.

- Audit Contact Form 7, Pinterest hover, PixelYourSite, Burst, Leaflet, and CookieYes for page-level necessity.

- Estimated effort: Medium.

- Expected gain: High.

### 3. Consolidate and prune Elementor/WooCommerce CSS

- Affected paths:

- `app/public/wp-content/cache/min`

- `app/public/wp-content/uploads/elementor/css`

- Elementor/WooCommerce generated frontend output

- Evidence:

- Largest minified CSS files include WooCommerce CSS at 86.1 KB, Gravity Forms basic CSS at 48.3 KB, child `custom.css` at 31.1 KB, WooCommerce layout CSS at 19.3 KB, Swiper at 17.8-18 KB, Elementor Swiper at 15.8 KB, Leaflet at 14.5 KB, Select2 at 14.3 KB, and WooCommerce blocks CSS at 13.7 KB.

- Product pages load many Elementor widget-specific styles and multiple post CSS files.

- Impact:

- Many CSS files block rendering. Even if minified, the browser still processes many stylesheet requests and selectors.

- Recommended fix:

- Enable/test WP Rocket Remove Unused CSS or Optimize CSS Delivery on staging.

- Disable WooCommerce blocks CSS on non-block pages if not needed.

- Disable Gravity Forms CSS except on forms pages.

- Remove duplicate Swiper copies: the child theme loads Swiper 10, while Elementor also ships Swiper.

- Review Elementor page/template structure for unused widgets that enqueue CSS.

- Estimated effort: Medium.

- Expected gain: High for First Contentful Paint and LCP.

### 4. Fix gallery/search dynamic endpoints so they do less work

- Affected files:

- `app/public/wp-content/themes/hello-elementor-child/gallery-load-more.php`

- `app/public/wp-content/themes/hello-elementor-child/functions.php`

- Evidence:

- `gallery-load-more.php` lines 118-132 query all matching products with `posts_per_page => -1`.

- Lines 136-158 iterate every product and each gallery attachment.

- The full result set is cached for only 300 seconds.

- Lines 429-434 expose a public REST endpoint with `permission_callback => '__return_true'`.

- Lines 520-521 also register the same required-argument REST callback as an admin-ajax handler.

- Search AJAX in `functions.php` lines 1712-1753 runs public `WP_Query` and outputs full-size image URLs.

- Impact:

- Uncached gallery/search requests bypass page cache and can become very expensive during browsing, filtering, or scraping.

- Recommended fix:

- Precompute gallery lookup data in transients or a custom table and invalidate on product/gallery update.

- Use paginated SQL or `WP_Query` with strict limits rather than building full arrays repeatedly.

- Remove unused duplicate admin-ajax hooks or split the callback signatures.

- Add nonces, rate limiting, max offsets, and page ID validation.

- Return medium/thumbnail images in AJAX search.

- Estimated effort: Medium to Large.

- Expected gain: High for interaction speed and server load.

### 5. Clean media backups/trash and enforce media policy

- Affected path: `app/public/wp-content/uploads`

- Evidence:

- `uploads/backup`: 6,798 files / 2,034.9 MB.

- `uploads/wpmc-trash`: 14,729 files / 1,675.7 MB.

- Generated image derivative pattern `-\d+x\d+.`: 142,074 files / 4.59 GB.

- Extension totals: 127,927 WebP files / 4,339.5 MB and 27,017 JPG files / 3,743.8 MB.

- Impact:

- Storage bloat slows backups, migrations, sync/offload operations, media scans, and increases the chance templates accidentally reference oversized originals.

- Recommended fix:

- Back up first, then empty Media Cleaner trash and remove upload backups that are not referenced.

- Define allowed image sizes and regenerate thumbnails.

- Remove unused intermediate sizes after confirming theme/WooCommerce needs.

- Set max upload dimensions/file size and compress on upload.

- Estimated effort: Medium.

- Expected gain: Medium directly, High operationally.

### 6. Reduce third-party connection count

- Affected output: cached HTML pages

- Evidence:

- Home page references external hosts including DigitalOcean Spaces, Google Fonts, Facebook, Pinterest, jsDelivr, unpkg, Google Tag Manager, Google Analytics, ExactDN, and Google Fonts static.

- `product/ganges` references `jamiesternmedia.nyc3.digitaloceanspaces.com` 232 times, plus local assets and several third-party scripts.

- Impact:

- Each third-party origin adds DNS/TLS/connect cost and runtime variability. Analytics/pixel scripts can delay interaction and main-thread idle time.

- Recommended fix:

- Host Swiper/Lenis locally or use one bundled source.

- Self-host fonts and trim Roboto weights. Current Google Fonts request includes 100-900 plus italics.

- Audit PixelYourSite/Pinterest/Facebook/Burst firing rules and load only where needed.

- Add preconnect only for truly critical external origins, likely media CDN and fonts if fonts remain external.

- Estimated effort: Small to Medium.

- Expected gain: Medium to High.

### 7. Improve cache headers for static assets

- Affected file: `conf/nginx/site.conf.hbs`

- Evidence:

- CSS/JS location uses `Cache-Control "no-cache, public, must-revalidate, proxy-revalidate"`.

- Image/font locations use only `expires 5m`.

- WebP is not included in the image cache regex.

- Impact:

- If this config influences staging/production, browser caching is far weaker than it should be.

- Recommended fix:

- Use long-lived immutable cache headers for versioned CSS/JS, fonts, WebP, AVIF, JPG, PNG, SVG, and GIF.

- Keep HTML/cacheable page rules separate from static asset rules.

- Estimated effort: Small.

- Expected gain: Medium for repeat visits.

## Secondary Recommendations

### Plugin footprint review

The active stack is heavy: WooCommerce, Elementor, Elementor Pro, ACF, Gravity Forms, Contact Form 7, PixelYourSite, Pinterest integrations, Burst, Google Site Kit, CookieYes, Wordfence, WP Rocket, Yoast, media cleaners, migration tools, and admin utilities. Some are necessary, but page speed improves when fewer plugins hook into frontend requests.

Recommended production review:

- Remove/deactivate migration-only tools when not actively migrating.

- Remove `wp-phpmyadmin-extension` from production.

- Pick one form strategy where possible: Contact Form 7 and Gravity Forms both appear active.

- Confirm whether Burst plus Google Analytics/Site Kit plus PixelYourSite all need to run.

- Disable plugin assets page-by-page using Asset CleanUp, Perfmatters, custom dequeue logic, or WP Rocket exclusions after staging tests.

### WP Rocket tuning

WP Rocket is active and cache files exist. Confirm these settings on staging/production:

- Page cache enabled and serving cached pages anonymously.

- Separate mobile cache only if mobile markup differs.

- Remove Unused CSS enabled after checking Elementor/WooCommerce layouts.

- Delay JavaScript enabled with tested exclusions for menu, product gallery, checkout, search, and quick-view.

- Lazy-load images and iframes enabled, but exclude only the true LCP image.

- Preload critical product/category/home URLs after purge.

- Database cleanup scheduled, but keep revisions/order data policies conservative.

### Fonts

The cached product page shows three repeated Google Fonts stylesheet links for Roboto with weights 100-900 and italics. Most brands do not need that many weights.

Recommended fix:

- Self-host only used weights, likely 400/500/600/700.

- Remove duplicate font declarations from Elementor/theme/plugin settings.

- Preload the primary font file only if it is actually used above the fold.

### HTML size

HTML documents between 527 KB and 743 KB are large. This usually means too much above-the-fold markup, too many inline configs/scripts, too many rendered gallery items, or excessive Elementor wrapper output.

Recommended fix:

- Reduce initial gallery item count.

- Move non-critical product sections behind interaction or lazy-rendered tabs.

- Avoid duplicating desktop/mobile markup when CSS can adapt one markup tree.

- Simplify Elementor templates where repeated widgets generate heavy markup.

## Prioritized 30-Day Speed Plan

1. Replace all remaining `full` image rendering in custom theme code with appropriate responsive sizes.

2. Scope Swiper, single-product assets, Pinterest hover script, Contact Form 7 assets, and blog/search assets to only pages that use them.

3. Test WP Rocket Remove Unused CSS and Delay JS on staging.

4. Remove duplicate Swiper source: use Elementor's or the child theme's, not both.

5. Reduce Google Fonts to required weights or self-host them.

6. Reduce product gallery initial render count, especially on image-heavy products like `ganges`.

7. Fix gallery/search endpoints to avoid full catalog scans after cache expiry.

8. Clean `uploads/backup` and `uploads/wpmc-trash` after backup.

9. Add long-lived static asset cache headers, including WebP/AVIF.

10. Re-run local and production tests after each batch.

## 60-90 Day Speed Plan

- Rebuild product gallery data access around precomputed lookup data or indexed queries.

- Audit all top templates with Chrome Lighthouse/PageSpeed Insights in production-like conditions.

- Remove or replace redundant plugins and analytics/pixel tags.

- Regenerate media sizes against a new image-size policy.

- Introduce a deployment check that fails if key pages exceed asset/HTML budgets.

- Add performance budgets:

- Home HTML under 250 KB.

- Product HTML under 350 KB for typical products.

- Fewer than 20 CSS files before WP Rocket optimization.

- Fewer than 35 script tags on product pages before interaction.

- No full-size images in grids/search/category cards.

## Suggested Performance Budgets

| Metric | Current observed | Target |

|---|---:|---:|

| Home HTML | 543 KB | < 250 KB |

| Product HTML | 527-743 KB | < 350 KB |

| Product script tags | 77-78 | < 35 |

| Product CSS links | 37 | < 20 |

| Home image tags | 59 | < 30 initially rendered |

| `ganges` image tags | 235 | < 60 initially rendered |

| Uploads footprint | 8.5 GB | reduce by 30-50% after review |

| Generated image derivatives | 4.59 GB | reduce after size policy |

## Verification Commands Used

```powershell

git status --short

Get-ChildItem app\public\wp-content\cache\wp-rocket\jamie-stern.local -Recurse -File -Filter index.html -ErrorAction SilentlyContinue | Measure-Object Length -Sum

Get-ChildItem app\public\wp-content\cache\wp-rocket\jamie-stern.local -Recurse -File -Filter index.html -ErrorAction SilentlyContinue | Sort-Object Length -Descending | Select-Object -First 20

rg -n "rand\(|wp_enqueue_style\(|wp_enqueue_script\(|the_post_thumbnail\('full'|the_post_thumbnail_url\('full'|wp_get_attachment_image\([^,]+, 'full'|cdn.jsdelivr.net|custom-search\.js|WP_CACHE|WP_DEBUG|lazy|preload|remove_unused_css|delay_js" app\public\wp-config.php app\public\wp-content\themes\hello-elementor-child app\public\wp-content\wp-rocket-config

Get-ChildItem app\public\wp-content\uploads -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum

Invoke-WebRequest -Uri http://jamie-stern.local/ -UseBasicParsing -TimeoutSec 20

Invoke-WebRequest -Uri http://jamie-stern.local/product/ganges/ -UseBasicParsing -TimeoutSec 45

Invoke-WebRequest -Uri http://jamie-stern.local/contemporary/3/ -UseBasicParsing -TimeoutSec 45

Invoke-WebRequest -Uri http://jamie-stern.local/product/dune-sofa/ -UseBasicParsing -TimeoutSec 45

Get-ChildItem app\public\wp-content\cache\min -Recurse -File -ErrorAction SilentlyContinue

Get-ChildItem app\public\wp-content\themes\hello-elementor-child\assets -File

Get-ChildItem app\public\wp-content\plugins -Directory

Select-String -Path app\public\wp-content\debug.log -Pattern 'Cron reschedule|PHP Warning|PHP Fatal|_load_textdomain_just_in_time|mysqli_real_connect'

Get-Content app\public\wp-content\themes\hello-elementor-child\functions.php

Get-Content app\public\wp-content\themes\hello-elementor-child\gallery-load-more.php

Get-Content conf\nginx\site.conf.hbs

```

## Checks Not Run

- Production Lighthouse/PageSpeed Insights was not run from the internet.

- Browser waterfall and Core Web Vitals were not captured.

- PHP profiling and database query profiling were not run.

- PHP lint was not run because PHP is not available in PATH in this shell.

Prompts

Here's the revised set, sequenced for what's actually still net-new value given everything you've shipped today.

Prompt 1: Image sizes (run first, highest mechanical value)

TASK: Replace 'full' image rendering with responsive WordPress

image sizes in the hello-elementor-child theme.

CONTEXT

- Repo: jamie-stern-wp-content (you are at the repo root, which IS

wp-content)

- Active theme: themes/hello-elementor-child/

- Recent merged work to coordinate with:

- PR #1: removed dead custom-search.js enqueue

- PR #2: rand() -> filemtime() asset versions

- PR #6: scoped single-product-css/js into shortcode callbacks

- PR #4 + #5: nonce/validation guards on AJAX/REST endpoints

- This PR should NOT touch enqueue logic, asset versioning, or

AJAX/REST handlers. Stay in image rendering only.

- Branch off latest main.

DO

1. Find all 'full' image usages in child-theme PHP files:

grep -rn "the_post_thumbnail('full')" themes/hello-elementor-child/

grep -rn "the_post_thumbnail_url('full')" themes/hello-elementor-child/

grep -rn "wp_get_attachment_image.*'full'" themes/hello-elementor-child/

Per the audit, expect findings in functions.php around lines

345, 683, 736, 1447, 1762. Verify by reading actual file before

editing.

2. For each occurrence, classify the context:

- Product/category cards: replace with 'woocommerce_thumbnail'

or 'medium_large'

- Product gallery main image: 'woocommerce_single' or 'large'

- Blog cards/search results: 'medium_large'

- Portfolio sliders: 'large' unless full resolution is required

- Quick View / shortcode galleries: 'large' as default, document

reasoning per case

3. Where you find raw <img src> markup using full-size URLs,

prefer wp_get_attachment_image() to emit srcset, sizes, width,

height, loading, decoding attributes. Preserve existing CSS

classes via the $attr parameter.

4. Where raw <img> markup remains, ensure alt handling is

explicit (use the attachment's alt text from postmeta).

5. Branch: bugfix/responsive-image-sizes

6. Commit per logical unit (one commit per function/section

modified, not one giant commit).

STOP CONDITIONS

- If a 'full' usage is in code that's commented out, leave it

alone and report it.

- If you find usages where the size choice isn't obvious from

context (e.g., a function used in many templates), STOP for

that one and document in the PR for human decision.

- If the change would affect visual layout (e.g., a hero image

that genuinely needs full-resolution), leave it and document why.

DO NOT

- Touch enqueue/version logic (PR #1, #2, #6 already shipped this)

- Touch AJAX/REST handlers (PR #4, #5 already shipped this)

- Refactor surrounding code

- Delete media or change image selection logic

- Rewrite history

DELIVERABLE

PR description must include:

- Per-occurrence summary: file:line, old size, new size, reasoning

- Anything left as 'full' with explanation

- QA checklist for human reviewer:

- Pages to load and verify look correct

- Network tab check: srcset present, smaller image variants served

- Mobile/responsive check on at least one product page

REPORT

- PR link

- File-by-file change summary

- Any 'full' usages left alone with reasoning

DO NOT FABRICATE TOOL OUTPUT.

DO NOT REWRITE GIT HISTORY.

Prompt 2: Media cleanup analysis (report-only, no risk)

TASK: Create a media cleanup analysis script and report. REPORT-ONLY.

Do not delete, move, rename, or modify any uploads.

CONTEXT

- This runs against the local Windows machine where Local by Flywheel

hosts the site. Uploads are at:

C:\Users\Maxwel\Local Sites\jamie-stern\app\public\wp-content\uploads

- Output: a script + Markdown report committed to the repo at:

tools/media-cleanup-analysis.ps1

MEDIA_CLEANUP_REPORT.md

- These give Marcus (and Sam) data to make cleanup decisions later.

Nothing in this PR changes media or site behavior.

- Branch off latest main.

SHELL: Windows PowerShell. PowerShell-native commands only.

DO

1. Create tools/media-cleanup-analysis.ps1 that scans the uploads

directory and reports:

- Total file count and total size in GB

- Top 50 largest files (path, size in MB, last modified)

- Total size of uploads/backup/ if it exists

- Total size of uploads/wpmc-trash/ if it exists

- Count of generated image derivatives matching pattern

-<width>x<height>. and their total size

- Count of files by extension with total size per extension

- Files matching risky extensions in uploads:

.zip, .psd, .sql, .log, .php, .bak, .tif, .tiff, .pdf

- Duplicate-candidate originals: files with the same basename

(without -<width>x<height>. suffix) appearing in multiple

directories

2. Output should be Markdown written to MEDIA_CLEANUP_REPORT.md

at the repo root. Include:

- Summary stats at the top

- Each finding as its own section with tables

- A "Candidate cleanup commands" section with EXACT commands

to remove backup/trash dirs, but COMMENTED OUT and prefixed

with "# REQUIRES HUMAN APPROVAL — DO NOT RUN BLINDLY"

- A "Requires human approval" section explaining what each

candidate cleanup would delete and the risks

3. Branch: feature/media-cleanup-analysis

4. Commit the script and the report it generates. Do NOT commit

any actual changes to uploads.

STOP CONDITIONS

- If the uploads directory is unreachable or empty, STOP and

report (means script is being run somewhere other than the

Local install).

- If the script would take more than 10 minutes to run, add

progress output and continue. Do not silent-hang.

DO NOT

- Delete, move, rename, or modify any file under uploads/

- Run any of the candidate cleanup commands

- Touch theme files, plugins, or wp-config

- Rewrite history

DELIVERABLE

- The PowerShell script at tools/media-cleanup-analysis.ps1

- The generated MEDIA_CLEANUP_REPORT.md

- PR description listing what the script reports and how to run it

REPORT

- PR link

- Top-line numbers (total uploads size, backup/trash sizes,

derivative count)

- Script run time

DO NOT FABRICATE TOOL OUTPUT.

DO NOT REWRITE GIT HISTORY.

Prompt 3: Gallery/search performance refactor (bigger surface area, save for after image sizes lands)

TASK: Optimize qv-gallery and custom search AJAX/REST performance

without changing frontend behavior.

CONTEXT

- Repo: jamie-stern-wp-content

- Files in scope:

- themes/hello-elementor-child/gallery-load-more.php

- themes/hello-elementor-child/functions.php (search AJAX section)

- themes/hello-elementor-child/assets/qv-gallery.js (read only,

do not modify — JS already updated by PR #5)

- Recent merged work to NOT undo:

- PR #4: nonce + input validation already added to qv/v1/load-more

REST route, load_product_quick_view AJAX, custom_search_posts AJAX

- PR #5: JS already sends nonces correctly

- This PR is about query/cache efficiency, not security or UX.

- Branch off latest main.

DO

1. Read gallery-load-more.php and identify:

- Functions that query products with posts_per_page = -1

- Functions that iterate every product and gallery attachment

- Cache TTL values (audit found 300s — too short for full

catalog scan)

- Any duplicated admin-ajax + REST handler registrations

2. For each finding, propose ONE of these strategies BEFORE

implementing:

a) Replace -1 query + in-PHP iteration with paginated SQL

using $wpdb with proper indexes

b) Move expensive lookup data into transients with

invalidation hooks on product save / gallery update

c) Increase cache TTL where data doesn't change often,

with explicit invalidation hooks

d) Remove duplicated handlers if REST is the actual path

used by JS (verify against qv-gallery.js)

3. After reporting the strategy, implement on:

Branch: bugfix/qv-gallery-performance

4. For search AJAX in functions.php:

- Require minimum search length of 2 chars (PR #4 already

added this — verify, don't duplicate)

- Use medium-sized images in response, not full

- Add a brief transient cache for common search strings

(cache key includes the search term, TTL ~5 minutes)

5. Commit per logical unit. Each function modified gets its

own commit with clear before/after description.

STOP CONDITIONS

- If a query is doing -1 because the result set is genuinely

small and bounded (e.g., "all categories"), leave it alone

and document why

- If transient invalidation would require hooking into plugin

code outside the theme, STOP and document

- If you can't determine what calls a given function, STOP

and document

- If PR #4's input validation conflicts with proposed paginated

query approach (e.g., offset cap), reconcile by adjusting

the new code to honor existing validation

DO NOT

- Touch nonce/security code (PR #4 owns that)

- Modify qv-gallery.js (PR #5 owns that)

- Change REST route signatures or admin-ajax action names

- Refactor unrelated code

- Rewrite history

DELIVERABLE

PR description must include:

- Strategy chosen per function with reasoning

- Before/after for each function (lines of code, query count,

expected TTL behavior)

- QA checklist for human reviewer:

- qv-gallery Load More on pages 16889 and 16890 still works

- Custom search returns expected results

- No 401/403 errors (proves nonce flow still intact)

- Page rendering on first load (cold cache) is acceptable

REPORT

- PR link

- Per-function change summary

- Anything left alone with reasoning

DO NOT FABRICATE TOOL OUTPUT.

DO NOT REWRITE GIT HISTORY.

Skipped from the original list:

Asset scoping prompt — PR #6 already did the safe scoping (single-product-css/js into shortcode callbacks). The remaining piece is Swiper, which has the architectural blocker in custom.js (calls new Swiper() unconditionally at document.ready). Running a generic asset-scoping prompt now would either re-do work or hit the same blocker. Save Swiper for desktop session work where you can guard custom.js properly.

Static asset cache headers prompt — only affects local Nginx config, not WP Engine production. Marginal value for the engagement. Skip unless Sam confirms WP Engine production cache config is also in scope.

Order I'd run them:

Image sizes (Prompt 1) — kick off now, runs in parallel with PR #4/#5 verification work

Media cleanup analysis (Prompt 2) — kick off after Prompt 1 lands, low-risk, gives you data for Sam

Gallery/search performance (Prompt 3) — last, biggest surface area, save for when main is fully clean

Don't queue all three at once. Run sequentially, verify each lands clean before stacking the next. Today already showed what stacked-PR confusion looks like.

Send Prompt 1 first.
