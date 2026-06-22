---
title: "2026 05 05 WordPress Diagnostic Audit"
source_archive: "Software Projects"
source_path: "####Software Projects/# Eagle Rocket/Jamie Stern/Audits/2026-05-05 WordPress Diagnostic Audit.docx"
status: archive
privacy: working
tags:
  - case-study
---

# 2026 05 05 WordPress Diagnostic Audit

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
2026-05-05 WordPress Diagnostic Audit

Audit date: 2026-05-05

Site root inspected: C:\Users\Maxwel\Local Sites\jamie-stern

Mode: report-only. No site behavior was changed.

Executive Summary

This is a Local WordPress site export with an active Hello Elementor child theme, WooCommerce, Elementor/Elementor Pro, WP Rocket, Wordfence, Yoast SEO, Gravity Forms, ACF Pro, media/offload tooling, migration tooling, and several utility plugins. The most important risks are not subtle: database dumps, logs, and plugin archives are present inside public web paths; WP_DEBUG is enabled and has produced a 9.4 MB public debug.log; WP Rocket page caching is disabled in wp-config.php; the active child theme globally enqueues assets and uses random version strings that defeat browser caching; and the media library has grown to roughly 157,059 files and 9.1 GB, with 3.7 GB in uploads/backup and uploads/wpmc-trash alone.

The highest-value remediation is a short, careful stabilization pass: remove public SQL/log/archive artifacts from webroot, turn off debug mode in production, fix the missing custom-search.js enqueue, replace rand() cache busting with file modification versions, scope Swiper/product assets to pages that use them, and clean uploads/backup plus uploads/wpmc-trash only after a verified backup. The longer refactor target is to shrink and simplify the custom child theme gallery/search/quick-view code and reduce the active plugin surface.

Site Inventory

Root is not a Git repository: git status --short from the site root returned fatal: not a git repository.

app/public/wp-content/.git exists, so version control appears nested under wp-content, not at the site root.

Active theme from app/sql/local.sql: template is hello-elementor, stylesheet is hello-elementor-child, current_theme is Hello Elementor Child.

Installed themes: hello-elementor, hello-elementor-child, salient, salient-child, twentytwentyfive, twentytwentyfour, twentytwentythree.

Theme sizes: salient is 51.82 MB across 2,081 files; active hello-elementor-child is 0.30 MB across 15 files.

Active plugins from wp_options.active_plugins: 40.

Plugin directories present: 46.

Notable active versions found in plugin headers:

WordPress core cache HTML references ver=6.9.4.

WooCommerce 10.7.0.

Elementor 3.34.0.

Elementor Pro 3.34.0.

Yoast SEO 27.5 and Yoast SEO Premium 27.5.

WP Rocket 3.14.2.1.

Wordfence 8.2.0.

WP phpMyAdmin 5.2.2.01.

All-in-One WP Migration 7.105.

All-in-One WP Migration Unlimited Extension 2.84.

Media/offload evidence: wp_as3cf_items has 7,517 insert rows in the local SQL dump, pointing at a DigitalOcean Spaces-style bucket (nyc3, jamiesternmedia).

Critical Findings

1. Public webroot contains database dumps

Affected path: app/public/wp-content/__mysql.sql, app/public/wp-content/___1mysql.sql, app/sql/local.sql

Evidence:

app/public/wp-content/__mysql.sql is 267.44 MB.

app/public/wp-content/___1mysql.sql is 267.77 MB.

app/sql/local.sql is 321.64 MB.

wp-content/.htaccess only contains All 404 marker comments; it does not deny SQL, log, backup, or archive files.

Local nginx restrictions deny hidden files and PHP in uploads, but do not deny .sql, .log, .zip, or .gz.

Impact: If production serves similar files from wp-content, an unauthenticated visitor could download the database dump. That may expose user accounts, emails, order/customer data, plugin secrets, salts, sessions, option values, and internal URLs.

Recommended fix: Move SQL dumps outside webroot immediately. Add server-level deny rules for *.sql, *.log, *.bak, *.zip, *.gz, *.tar, *.7z, and backup directories. Rotate secrets after confirming any dump was ever deployed publicly.

Estimated effort: Small for removal/rules; Medium if secrets must be rotated.

2. Public logs disclose filesystem paths and runtime failures

Affected path: app/public/wp-content/debug.log, app/public/wp-content/debug_.log, app/public/wp-content/debug.log.*.gz, app/public/wp-content/uploads/wc-logs/*.log

Evidence:

app/public/wp-content/debug.log is 9.42 MB.

Additional compressed debug logs exist: debug.log.1.gz through debug.log.5.gz.

debug_.log is 213 KB.

WooCommerce fatal logs are under uploads/wc-logs.

debug.log contains 13,360 repeated early textdomain load notices and references production-like paths such as /nas/content/live/testjamiestg/....

Impact: Logs can leak filesystem paths, plugin names/versions, stack traces, request behavior, and operational details useful for targeted attacks. Large logs also add disk and backup weight.

Recommended fix: Remove public logs from webroot after preserving any needed diagnostics. Configure production logging outside the document root. Keep WP_DEBUG_LOG off in production unless routing logs to a non-public path.

Estimated effort: Small.

3. Debug mode is enabled in wp-config.php

Affected file: app/public/wp-config.php

Evidence:

Lines 90-94 define WP_DEBUG as true, WP_DEBUG_LOG as true, and WP_DEBUG_DISPLAY as false.

Comment at lines 86-88 says debug mode was enabled for local diagnosis and should be turned back.

Impact: Production debug logging can leak sensitive paths and runtime details, grow without bound, and mask performance problems by writing on busy requests.

Recommended fix: For staging/production, set WP_DEBUG to false and WP_DEBUG_LOG to false or to a non-public custom log path. Confirm deployment-specific config is not copied from this local debug file.

Estimated effort: Small.

4. Database/admin tooling plugin is active in the WordPress plugin tree

Affected path: app/public/wp-content/plugins/wp-phpmyadmin-extension

Evidence:

Plugin directory is present and is 22.77 MB across 3,201 files.

Plugin header reports WP phpMyAdmin version 5.2.2.01.

wp_options.active_plugins includes wp-phpmyadmin-extension/index.php.

Impact: phpMyAdmin embedded in WordPress materially increases attack surface. Even if it is permission-gated, any plugin vulnerability, admin compromise, or nonce/capability bug can become direct database access.

Recommended fix: Remove from production entirely. Use host-level database tools over authenticated admin/VPN paths instead.

Estimated effort: Small.

High Findings

5. WP Rocket page caching appears disabled at the config entry point

Affected file: app/public/wp-config.php

Evidence:

Line 2 is // define( 'WP_CACHE', true ); // Added by WP Rocket - disabled during local debug.

WP Rocket cache files exist under app/public/wp-content/cache/wp-rocket, so the site has used page caching.

app/public/wp-content/wp-rocket-config/jamie-stern.local.php has mobile cache enabled, but WP_CACHE is commented out.

Impact: If this state is deployed, WordPress will bypass advanced-cache page caching and every uncached page becomes a full PHP/database render. This is a major TTFB and scalability hit.

Recommended fix: Re-enable WP_CACHE in production/staging configs after resolving the local debug issue. Verify advanced-cache.php is active and matches WP Rocket's expected drop-in.

Estimated effort: Small.

6. Active child theme defeats browser caching with rand()

Affected file: app/public/wp-content/themes/hello-elementor-child/functions.php

Evidence:

Lines 26, 30, 31, and 35 pass rand() as asset versions for custom.css, blog.css, blog.js, and single-product.css.

Impact: Every request gets a new asset URL. Browsers and CDNs cannot reuse cached CSS/JS reliably, which increases repeat-view bandwidth and delays render. It can also fragment WP Rocket/minify cache.

Recommended fix: Replace rand() with stable file modification versions, for example filemtime(get_stylesheet_directory() . '/assets/custom.css'), or a theme version constant.

Estimated effort: Small.

7. Active child theme globally enqueues assets that are not globally needed

Affected file: app/public/wp-content/themes/hello-elementor-child/functions.php

Evidence:

Lines 35, 37, 40-52, 54, and 55 enqueue single-product CSS, jQuery, Swiper CSS/JS from jsDelivr, custom.js, and single-product.js on all frontend pages.

Cached portfolio pages show Swiper CSS near the head and Swiper JS plus child-theme scripts on pages such as portfolio/1600-market-street.

Cached largest page sample (portfolio/moxy-hotel/index.html) is 507.52 KB HTML, with 39 stylesheet links, 74 script tags, and 61 images.

Impact: Portfolio/category/content pages pay product-gallery and Swiper costs even when they do not need them. This adds render-blocking CSS, more JavaScript parse/evaluate work, and another third-party dependency.

Recommended fix: Scope product CSS/JS to product templates and quick-view/gallery pages. Enqueue Swiper only on shortcodes/templates that render Swiper. Where possible, bundle/localize the Swiper asset or use Elementor/WooCommerce's existing copy if available.

Estimated effort: Medium.

8. Enqueued custom-search.js does not exist

Affected file: app/public/wp-content/themes/hello-elementor-child/functions.php

Evidence:

Lines 1757-1763 enqueue get_stylesheet_directory_uri() . '/custom-search.js'.

Test-Path app/public/wp-content/themes/hello-elementor-child/custom-search.js returned False.

Test-Path app/public/wp-content/themes/hello-elementor-child/assets/custom-search.js returned False.

Cached pages include requests for /wp-content/themes/hello-elementor-child/custom-search.js.

Impact: Every page that enqueues this file generates a 404. That wastes a request, adds frontend noise, and likely breaks custom blog search/load-more behavior.

Recommended fix: Either move the intended script into that path, correct the enqueue to an existing asset, or enqueue the script only where the shortcode is rendered.

Estimated effort: Small.

9. Gallery REST/AJAX handler is public and has mismatched callback signatures

Affected file: app/public/wp-content/themes/hello-elementor-child/gallery-load-more.php

Evidence:

Lines 429-434 register REST route qv/v1/load-more with permission_callback => '__return_true'.

Lines 520-521 also register qv_load_more_ajax for wp_ajax_qv_load_more and wp_ajax_nopriv_qv_load_more.

Function signature at line 436 is function qv_load_more_ajax($request), which works for REST but not for an admin-ajax action that passes no required parameter.

Lines 477-479 trust public offset, color, and page_id request values after basic casting/sanitization.

Impact: The REST route is intentionally public, but it can be scraped or hammered to force expensive product/gallery work. The admin-ajax action can fatal because the callback requires an argument. This is both reliability and abuse risk.

Recommended fix: Split REST and admin-ajax callbacks or remove the unused admin-ajax hooks. Add nonce/rate checks where feasible, cap offsets, validate page IDs against the expected pages, and return WP_REST_Response.

Estimated effort: Medium.

10. Quick-view AJAX endpoint is public and lacks nonce/rate controls

Affected file: app/public/wp-content/themes/hello-elementor-child/functions.php

Evidence:

Lines 64-65 register load_product_quick_view for both logged-in and non-logged-in users.

Line 70 reads $_POST['product_id'] directly with intval().

The function loads ACF product gallery images, featured images, WooCommerce product data, and rendered HTML.

Impact: This can be scraped for product data and repeatedly hit to force server-side WooCommerce/ACF lookups. It is not a privilege escalation by itself, but it is a public dynamic endpoint on an otherwise cacheable storefront.

Recommended fix: Add a nonce tied to rendered quick-view buttons, validate the product is published/visible, cap response work, and consider caching rendered quick-view fragments by product ID.

Estimated effort: Medium.

11. Media library contains large backup/trash directories inside uploads

Affected paths: app/public/wp-content/uploads/backup, app/public/wp-content/uploads/wpmc-trash

Evidence:

Entire uploads tree: 157,059 files, 9,120,986,653 bytes, about 8.70 GiB by PowerShell sum.

uploads/backup: 6,798 files, 2,034.89 MB.

uploads/wpmc-trash: 14,729 files, 1,675.70 MB.

Largest files include duplicate pairs such as Caldera-rcd1325g-Sample.jpg at 30.59 MB in both root uploads and uploads/backup.

Impact: Backups and trash inside uploads slow backups/migrations, increase disk use, increase CDN/storage sync costs, and may keep deleted or private material publicly reachable.

Recommended fix: After a full offsite backup and media reference check, archive/delete uploads/backup and empty uploads/wpmc-trash through Media Cleaner or a controlled script. Add deny rules for trash/backup directories if they must temporarily remain.

Estimated effort: Medium.

12. Uploads contain many generated image derivatives and oversized originals

Affected path: app/public/wp-content/uploads

Evidence:

Image derivative pattern -\d+x\d+. matched 142,074 files totaling 4,700.83 MB.

By extension: .webp has 127,927 files / 4,339.52 MB; .jpg has 27,017 files / 3,743.79 MB; .png has 546 files / 191.42 MB.

Largest image originals include 30.59 MB, 24.43 MB, 23.87 MB, and 22 MB JPEGs.

Impact: Large originals and many derivative sizes increase storage, backup time, image lookup complexity, and can hurt page speed if templates request full images.

Recommended fix: Define a strict image size policy, remove unused intermediate sizes, regenerate only needed sizes, compress originals, and audit templates using full image size.

Estimated effort: Medium to Large.

13. SVG uploads are enabled without visible sanitization

Affected file: app/public/wp-content/themes/hello-elementor-child/functions.php

Evidence:

Lines 1568-1573 add svg to allowed upload MIME types.

Uploads include SVG files, including uploads/smile_fonts/Defaults/Defaults.svg at 456.87 KB.

Impact: SVG can contain scripts or external references if not sanitized. WordPress does not safely sanitize SVG by default.

Recommended fix: Use a maintained SVG sanitization plugin/library or restrict SVG upload capability to a tiny trusted admin group. Existing SVGs should be scanned/sanitized.

Estimated effort: Small to Medium.

Medium Findings

14. Product/search templates request full-size images in multiple places

Affected file: app/public/wp-content/themes/hello-elementor-child/functions.php

Evidence:

Line 348 calls the_post_thumbnail('full').

Lines 686, 739, and 1421 call wp_get_attachment_image(..., 'full').

Line 1736 emits <img src="<?php the_post_thumbnail_url('full'); ?>" />.

Impact: Full-size image URLs can pull multi-megabyte originals into grids, sliders, and search results. This is especially costly with the observed 10-30 MB originals.

Recommended fix: Use named sizes appropriate to layout (medium_large, WooCommerce catalog/single, or custom sizes) and ensure srcset/sizes are emitted by wp_get_attachment_image.

Estimated effort: Medium.

15. Custom gallery count function re-fetches full result sets

Affected file: app/public/wp-content/themes/hello-elementor-child/gallery-load-more.php

Evidence:

Lines 118-132 query all product IDs with posts_per_page => -1.

Lines 136-158 iterate every product and every gallery attachment.

Lines 168 onward count by calling qv_get_products($cat_ids, $color, 999999, 0).

Cache TTL is only 300 seconds at line 161.

Impact: The first request after cache expiry rebuilds the entire product/gallery map. With a large WooCommerce catalog and media library, this can create slow uncached requests and memory pressure.

Recommended fix: Store an indexed product-gallery lookup in transients/object cache with invalidation on product/gallery updates, or implement direct paginated SQL with indexed meta/taxonomy joins and a separate COUNT(DISTINCT ...).

Estimated effort: Medium to Large.

16. Static asset cache headers are too short and incomplete in local nginx config

Affected file: conf/nginx/site.conf.hbs

Evidence:

CSS/JS location sets Cache-Control "no-cache, public, must-revalidate, proxy-revalidate".

JPG/JPEG/GIF/PNG/ICO/XML expires in only 5m.

Fonts/SVG/OTF expire in only 5m.

WebP is not included in the image static file regex.

Impact: Even if production differs, this config is poor for page speed if reused. It forces frequent revalidation, misses WebP, and undercuts long-lived browser caching.

Recommended fix: For fingerprinted/minified assets, use Cache-Control: public, max-age=31536000, immutable. Include webp, avif, css, js, fonts, and common document assets where appropriate. Keep HTML/no-cache separate.

Estimated effort: Small.

17. Local PHP/MySQL config is tuned for debugging/imports, not performance parity

Affected files: conf/php/php.ini.hbs, conf/mysql/my.cnf.hbs

Evidence:

PHP display_errors = On, max_execution_time = 1200, upload_max_filesize = 300M, post_max_size = 1000M.

MySQL innodb_buffer_pool_size = 32M, performance_schema = off, max_allowed_packet = 1G.

Impact: The local environment can hide slow queries/import stress and differs sharply from production behavior. A 32 MB InnoDB buffer pool is too low for diagnostic performance testing against a 321 MB SQL dump.

Recommended fix: Keep import-friendly settings in local only, but document production parity values. For local performance tests, raise InnoDB buffer pool and use production-like PHP memory/opcache settings.

Estimated effort: Small.

18. Action Scheduler and cron schedules show recurring schedule errors

Affected paths: logs/php/error.log, app/public/wp-content/debug.log, app/sql/local.sql

Evidence:

logs/php/error.log contains 9 cron reschedule errors for missing schedules such as every_minute, rocket_preload_process_pending, pys_queue_interval, rsssl_five_minutes, and Burst/WP Rocket intervals.

debug.log contains 3 rocket_preload_process_pending cron reschedule errors.

wp_actionscheduler_actions has 2,565 insert rows in the local SQL dump.

Impact: Missing schedules can stop preload, remove-unused-CSS, PixelYourSite queues, SSL checks, and analytics jobs from running predictably. Cron churn can also add DB writes and admin noise.

Recommended fix: Flush cron schedules after plugin activation/update, confirm active plugins that register schedules are loaded, clear stale cron options, and verify Action Scheduler queues in WooCommerce status.

Estimated effort: Small to Medium.

19. All-in-One WP Migration Unlimited Extension fatal in local logs

Affected path: logs/php/error.log

Evidence:

Fatal: Undefined constant "AI1WM_MAX_FILE_SIZE" in all-in-one-wp-migration-unlimited-extension/lib/controller/class-ai1wmue-main-controller.php:266.

Active plugins include both All-in-One WP Migration and its Unlimited Extension.

Impact: Import/export admin screens can fatal. This can interrupt maintenance and may indicate plugin version mismatch or load-order problems.

Recommended fix: Confirm compatible versions of base plugin and extension, update both together, or deactivate/remove the extension when not actively migrating.

Estimated effort: Small.

20. Elementor and Wordfence fatal errors exist in WooCommerce logs

Affected path: app/public/wp-content/uploads/wc-logs/fatal-errors-2026-04-13-b62f8663797dbfd57a3495d6cd4b2b5e.log

Evidence:

Elementor Cloud Library fatal: WpOrg\Requests\Exception\Http\Status403: 403 Forbidden in elementor/modules/cloud-library/module.php:207.

Wordfence fatal: ValueError: inet_pton(): Argument #1 ($ip) must not contain any null bytes in wordfence/lib/wfUtils.php:927.

Impact: These were production/staging fatal errors that can white-screen requests. Elementor cloud calls and Wordfence crawler verification should be checked after updates.

Recommended fix: Update Elementor/Wordfence in a staging copy, confirm outbound requests are permitted, and review Wordfence IP/crawler settings.

Estimated effort: Medium.

21. Search and gallery AJAX endpoints are publicly accessible and uncached

Affected file: app/public/wp-content/themes/hello-elementor-child/functions.php

Evidence:

Lines 1709-1710 register custom_search_posts for logged-in and non-logged-in users.

Lines 1714-1725 run a WP_Query from public POST values.

Line 1736 uses full-size featured image URL in returned HTML.

Impact: Public search can be repeatedly called and bypasses page cache. Returning full-size images can make each response heavy.

Recommended fix: Add nonce/rate controls, minimum search length, response caching for common queries, and thumbnail-sized images.

Estimated effort: Medium.

Low Findings

22. Inactive themes and legacy plugin zips add attack/maintenance surface

Affected paths: app/public/wp-content/themes/salient, app/public/wp-content/themes/salient-child, app/public/wp-content/uploads/wpmc-trash/*.zip, app/public/wp-content/themes/salient/plugins/*.zip

Evidence:

Active theme is Hello Elementor Child, but salient is still 51.82 MB.

Upload trash contains old plugin/theme zips including Salient 8.5.3, Salient 8.0.2, js_composer 5.5.2, Essential Grid 2.2.x, and Ultimate VC Addons 3.16.x/3.17.x.

Salient theme plugins folder contains bundled plugin zips.

Impact: Inactive code and archives increase backup size and can confuse future audits. Public zips disclose legacy versions and may expose proprietary plugin packages.

Recommended fix: Keep only active theme plus one current default fallback theme. Move commercial plugin zips outside webroot or delete after backup.

Estimated effort: Small.

23. Child theme has large monolithic functions.php

Affected file: app/public/wp-content/themes/hello-elementor-child/functions.php

Evidence:

File is roughly 84 KB and contains enqueue logic, quick-view HTML, search, sliders, product accordions, redirects, upload MIME changes, and large commented migration snippets.

require_once('gallery-load-more.php') appears at line 1295.

Impact: Changes are risky because unrelated frontend, WooCommerce, and AJAX behavior are coupled in one file. It also makes code review and targeted testing harder.

Recommended fix: Split by responsibility into included files such as assets.php, ajax-quick-view.php, shortcodes/search.php, shortcodes/gallery.php, and woocommerce/product.php.

Estimated effort: Medium.

24. Some code comments/text show encoding damage

Affected files: app/public/wp-content/themes/hello-elementor-child/functions.php, app/public/wp-content/themes/hello-elementor-child/gallery-load-more.php

Evidence:

Comments include mojibake such as categorÃ­a, â”€, âœ…, ðŸŽ¨, and pagination text Â«/Â».

Impact: Mostly maintainability, but it indicates mixed encodings and can leak into UI if similar strings are rendered.

Recommended fix: Normalize edited child-theme PHP files to UTF-8 and replace corrupted comments/rendered labels during refactor.

Estimated effort: Small.

25. No root-level robots.txt was present in the inspected export

Affected path: app/public/robots.txt

Evidence:

Get-Content app/public/robots.txt returned no content because the file was absent.

Impact: WordPress/Yoast can generate virtual robots.txt and sitemap routes, so this is not necessarily broken. It does mean file-based robots rules are not visible in the export.

Recommended fix: Verify live /robots.txt, /sitemap_index.xml, and Yoast sitemap output on staging/production.

Estimated effort: Small.

Opportunities

26. Reduce active plugin footprint

Affected paths: app/public/wp-content/plugins, wp_options.active_plugins

Evidence:

40 active plugins and 46 plugin directories are present.

Active plugin list includes multiple overlapping tool families: migration/backup, image optimization/cleaning, analytics/pixels, SEO free+premium, security, maintenance mode, admin utilities, media categories/library, and phpMyAdmin.

Impact: Every active plugin adds update risk, possible hooks, admin load, DB options, and conflict surface.

Recommended fix: Create a plugin ownership matrix: required for frontend, admin-only, migration-only, redundant, unknown. Remove or deactivate migration/admin-only tools from production.

Estimated effort: Medium.

27. Use media cleanup as a page-speed project, not only a storage project

Affected path: app/public/wp-content/uploads

Evidence:

4.34 GB of WebP files and 3.74 GB of JPG files coexist.

142,074 derivative image files total 4.70 GB.

Several pages render dozens of images and some theme functions request full image sizes.

Impact: Smaller media means faster backup/deploy, faster image lookup, lower CDN storage/egress, and fewer accidental full-size downloads.

Recommended fix: Identify top traffic templates, map the image sizes they need, remove obsolete image sizes, regenerate, and enforce maximum original dimensions/file sizes at upload.

Estimated effort: Large.

28. Add a repeatable performance test harness

Affected area: whole site

Evidence:

Local Invoke-WebRequest http://jamie-stern.local/ timed out during audit.

PHP CLI is not available in PATH, so php -l could not run.

Impact: It is hard to safely refactor theme/plugin behavior without baseline TTFB, HTML weight, asset count, and error budgets.

Recommended fix: Add a local/staging checklist using Lighthouse or WebPageTest plus WP-CLI checks, Query Monitor snapshots, and a crawl of key templates.

Estimated effort: Medium.

Quick Wins Under 1 Hour

Move app/public/wp-content/__mysql.sql and app/public/wp-content/___1mysql.sql out of webroot or delete them after backup.

Remove or archive public debug.log, debug_.log, and debug.log.*.gz outside webroot.

Turn off production debug logging in wp-config.php.

Fix or remove the missing custom-search.js enqueue.

Replace rand() asset versions with filemtime() versions.

Remove/deactivate wp-phpmyadmin-extension from production.

Add nginx/Apache deny rules for public backup/log/archive extensions.

Re-enable WP_CACHE in production config after confirming WP Rocket drop-in health.

Empty uploads/wpmc-trash only after verified backup and media reference review.

Delete old commercial plugin zips from public upload trash after backup.

30/60/90 Day Roadmap

First 30 Days: Stabilize and remove exposure

Remove public SQL dumps, logs, and plugin/theme zip archives from webroot.

Confirm WP_DEBUG and WP_DEBUG_LOG are off in production.

Re-enable WP Rocket WP_CACHE in the correct environment.

Fix the missing custom-search.js enqueue.

Replace rand() cache busting with stable versions.

Scope Swiper and product assets to pages that actually use them.

Remove production-only risk plugins that are only needed for migration/admin access.

Verify /robots.txt, Yoast sitemaps, checkout/account cache exclusions, and no-index settings on live/staging.

Days 31-60: Performance and reliability refactor

Refactor hello-elementor-child/functions.php into responsibility-based includes.

Split REST and admin-ajax gallery handlers and add nonce/rate controls.

Rework quick-view and search to cache fragments and use thumbnail/medium image sizes.

Audit top 20 cached pages for HTML size, CSS/JS count, image count, and unused scripts.

Regenerate image sizes after deciding which WooCommerce/portfolio sizes are truly needed.

Flush and validate WP-Cron/Action Scheduler schedules.

Update/test Elementor, Wordfence, WP Rocket, WooCommerce, and migration plugins in staging.

Days 61-90: Media and architecture cleanup

Complete media cleanup for uploads/backup, uploads/wpmc-trash, unused derivatives, and oversized originals.

Build a media upload policy: max dimensions, max file size, allowed file types, SVG sanitization.

Add repeatable performance monitoring for home, product category, product detail, portfolio, search, cart/checkout, and blog pages.

Reduce plugin footprint based on measured need and business owner signoff.

Document production config expectations for cache headers, PHP settings, MySQL sizing, WP Rocket, object cache, and CDN/offload.

Do Not Touch Without Backup

app/public/wp-content/uploads: Media cleanup can break product galleries, ACF fields, WooCommerce downloads, and offloaded-object references.

app/public/wp-content/uploads/backup and app/public/wp-content/uploads/wpmc-trash: likely removable, but only after a verified backup and media reference check.

app/sql/local.sql and public SQL dumps: contain the authoritative local data snapshot.

wp_as3cf_items / media offload data: changing paths can break cloud-hosted media.

app/public/wp-content/themes/hello-elementor-child/functions.php: many unrelated frontend behaviors are coupled here.

app/public/wp-content/wp-rocket-config and app/public/wp-content/cache: safe to clear through WP Rocket, but do not hand-edit production cache config without a rollback.

WooCommerce checkout/account/cache exclusions.

User roles/options in wp_options.

Checks That Could Not Be Run

php -v failed because php is not available in PATH.

php -l app/public/wp-content/themes/hello-elementor-child/functions.php failed for the same reason.

php -l app/public/wp-content/themes/hello-elementor-child/gallery-load-more.php failed for the same reason.

Invoke-WebRequest http://jamie-stern.local/ timed out, so live local runtime page timing could not be measured.

No network-based vulnerability/version lookup was performed. Plugin versions are local header observations only.

Verification Commands Used

git status --short

Get-ChildItem -Force

if (Get-Command rg -ErrorAction SilentlyContinue) { rg --files } else { Get-ChildItem -Recurse -File | ForEach-Object { $_.FullName } }

Get-ChildItem -Force app\public\wp-content | Select-Object Mode,LastWriteTime,Length,Name

Get-ChildItem -Directory app\public\wp-content\themes | Select-Object Name,LastWriteTime

Get-ChildItem -Directory app\public\wp-content\plugins | Select-Object Name,LastWriteTime

if (Test-Path app\public\wp-content\mu-plugins) { Get-ChildItem -Force app\public\wp-content\mu-plugins } else { 'NO_MU_PLUGINS_DIR' }

Get-ChildItem logs -Recurse -File | Select-Object FullName,Length,LastWriteTime

rg "\$table_prefix|WP_DEBUG|WP_CACHE|DISALLOW_FILE_EDIT|FORCE_SSL|AUTOMATIC_UPDATER|DB_NAME|DB_HOST" app\public\wp-config.php

rg -m 5 -n "'template'|'stylesheet'|'active_plugins'|'current_theme'|'siteurl'|'home'|'wp_rocket_settings'|'woocommerce_version'|'blog_public'" app\sql\local.sql

Get-Content logs\php\error.log -Tail 80

Get-Content logs\nginx\error.log -Tail 80

Get-Content app\public\wp-content\debug.log -Tail 120

Get-ChildItem app\public\wp-content -Force -File | Sort-Object Length -Descending | Select-Object -First 20 Name,Length,LastWriteTime

rg -n "Theme Name|Template|Version" app\public\wp-content\themes\salient-child\style.css app\public\wp-content\themes\salient\style.css app\public\wp-content\themes\hello-elementor-child\style.css app\public\wp-content\themes\hello-elementor\style.css

Get-ChildItem app\public\wp-content\themes\salient-child -Recurse -File | Select-Object FullName,Length,LastWriteTime | Sort-Object Length -Descending | Select-Object -First 50

Get-ChildItem app\public\wp-content\themes\hello-elementor-child -Recurse -File | Select-Object FullName,Length,LastWriteTime | Sort-Object Length -Descending | Select-Object -First 50

Get-ChildItem app\public\wp-content\cache -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum | Select-Object Count,Sum

Get-ChildItem app\public\wp-content\uploads -Recurse -File -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum | Select-Object Count,Sum

rg -n "'template'|'stylesheet'|'current_theme'|'blog_public'|'permalink_structure'" app\sql\local.sql

Get-ChildItem app\public\wp-content\uploads -Recurse -File | Group-Object Extension | Sort-Object Count -Descending | Select-Object -First 20 @{n='Extension';e={$_.Name}},Count,@{n='MB';e={[math]::Round(($_.Group|Measure-Object Length -Sum).Sum/1MB,2)}}

Get-ChildItem app\public\wp-content\uploads -Recurse -File | Sort-Object Length -Descending | Select-Object -First 40 FullName,@{n='MB';e={[math]::Round($_.Length/1MB,2)}},LastWriteTime

Get-ChildItem app\public\wp-content -Directory | ForEach-Object { $m=Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum; [pscustomobject]@{Dir=$_.Name;Files=$m.Count;MB=[math]::Round($m.Sum/1MB,2)} } | Sort-Object MB -Descending

Get-ChildItem app\public\wp-content\uploads -Recurse -File | Where-Object { $_.Name -match '-\d+x\d+\.' } | Measure-Object Length -Sum | Select-Object Count,@{n='MB';e={[math]::Round($_.Sum/1MB,2)}}

Get-ChildItem app\public\wp-content\uploads -Directory | ForEach-Object { $m=Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum; [pscustomobject]@{Dir=$_.Name;Files=$m.Count;MB=[math]::Round($m.Sum/1MB,2)} } | Sort-Object MB -Descending | Select-Object -First 30 | Format-Table -AutoSize

Get-ChildItem app\public\wp-content\uploads\backup -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum | Select-Object Count,@{n='MB';e={[math]::Round($_.Sum/1MB,2)}}

Get-ChildItem app\public\wp-content\uploads\wpmc-trash -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum | Select-Object Count,@{n='MB';e={[math]::Round($_.Sum/1MB,2)}}

Get-ChildItem app\public\wp-content\uploads -Recurse -File -Include *.psd,*.ai,*.tif,*.tiff,*.zip,*.pdf | Group-Object Extension | Sort-Object Count -Descending | Select-Object @{n='Extension';e={$_.Name}},Count,@{n='MB';e={[math]::Round(($_.Group|Measure-Object Length -Sum).Sum/1MB,2)}} | Format-Table -AutoSize

Get-Content app\public\wp-content\.htaccess

Get-Content app\public\.htaccess -ErrorAction SilentlyContinue

Get-Content conf\nginx\includes\restrictions.conf.hbs

Get-Content conf\nginx\site.conf.hbs

Get-Content app\public\wp-content\themes\hello-elementor-child\functions.php

Get-Content app\public\wp-content\themes\hello-elementor-child\gallery-load-more.php

rg -n "rand\(|wp_enqueue_style\(|wp_enqueue_script\(|wp_ajax_nopriv|intval\(\$_POST|\$_GET|posts_per_page'\s*=>\s*-1|upload_mimes|custom-search\.js|__return_true|wp_redirect|the_post_thumbnail\('full'|the_post_thumbnail_url\('full'|wp_get_attachment_image\([^,]+, 'full'|get_field\('hover_image'" app\public\wp-content\themes\hello-elementor-child

Test-Path app\public\wp-content\themes\hello-elementor-child\custom-search.js

Test-Path app\public\wp-content\themes\hello-elementor-child\assets\custom-search.js

Get-ChildItem app\public\wp-content\themes\hello-elementor-child\assets -File | Select-Object Name,Length

Get-ChildItem app\public\wp-content\plugins -Directory | ForEach-Object { $m=Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum; [pscustomobject]@{Plugin=$_.Name;Files=$m.Count;MB=[math]::Round($m.Sum/1MB,2)} } | Sort-Object MB -Descending | Select-Object -First 25 | Format-Table -AutoSize

Get-ChildItem app\public\wp-content\themes -Directory | ForEach-Object { $m=Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum; [pscustomobject]@{Theme=$_.Name;Files=$m.Count;MB=[math]::Round($m.Sum/1MB,2)} } | Sort-Object MB -Descending | Format-Table -AutoSize

rg -n "WP_DEBUG|WP_DEBUG_LOG|WP_DEBUG_DISPLAY|SCRIPT_DEBUG|SAVEQUERIES|WP_CACHE" app\public\wp-config.php

Select-String -Path app\sql\local.sql -Pattern "'active_plugins'|'template'|'stylesheet'|'current_theme'|'wp_rocket_settings'|'woocommerce_db_version'|'woocommerce_version'|'elementor_version'|'cron'" | Select-Object -First 30 LineNumber,Line

Get-ChildItem -Path app\sql,app\public\wp-content -File -Filter *.sql | Select-Object @{n='Path';e={$_.FullName.Replace((Get-Location).Path + '\','')}},@{n='MB';e={[math]::Round($_.Length/1MB,2)}},LastWriteTime | Format-Table -AutoSize

Select-String -Path app\public\wp-content\debug.log -Pattern 'PHP Fatal error|PHP Warning|PHP Notice|Cron reschedule event error|_load_textdomain_just_in_time|Undefined constant|Allowed memory size|Maximum execution time' | Group-Object { if ($_.Line -match 'PHP Fatal error') {'Fatal'} elseif ($_.Line -match 'PHP Warning') {'Warning'} elseif ($_.Line -match 'Cron reschedule') {'Cron reschedule'} elseif ($_.Line -match '_load_textdomain_just_in_time') {'Textdomain early load'} elseif ($_.Line -match 'PHP Notice') {'Notice'} else {'Other'} } | Sort-Object Count -Descending | Select-Object Name,Count | Format-Table -AutoSize

Get-ChildItem app\public\wp-content\uploads\wc-logs -File -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 20 Name,@{n='KB';e={[math]::Round($_.Length/1KB,2)}},LastWriteTime | Format-Table -AutoSize

Get-Content app\public\wp-content\uploads\wc-logs\fatal-errors-2026-04-13-b62f8663797dbfd57a3495d6cd4b2b5e.log -Tail 60 -ErrorAction SilentlyContinue

php -v

php -l app\public\wp-content\themes\hello-elementor-child\functions.php

php -l app\public\wp-content\themes\hello-elementor-child\gallery-load-more.php

try { $r=Invoke-WebRequest -Uri http://jamie-stern.local/ -UseBasicParsing -TimeoutSec 10; [pscustomobject]@{Status=$r.StatusCode;Length=$r.RawContentLength;Title=($r.Content -replace '(?s).*<title>(.*?)</title>.*','$1')} } catch { $_.Exception.Message }

Get-Content conf\nginx\includes\gzip.conf.hbs

Get-Content conf\php\php.ini.hbs | Select-String -Pattern 'memory_limit|max_execution_time|upload_max_filesize|post_max_size|display_errors|error_reporting|opcache|realpath_cache' -Context 0,0

Get-Content conf\mysql\my.cnf.hbs

Get-Content app\public\wp-content\wp-rocket-config\jamie-stern.local.php

Get-ChildItem app\public\wp-content\cache\wp-rocket\jamie-stern.local -Recurse -File -Filter index.html | Select-Object -First 20 @{n='Path';e={$_.FullName.Replace((Get-Location).Path + '\','')}},@{n='KB';e={[math]::Round($_.Length/1KB,2)}} | Format-Table -AutoSize

Open Assumptions

None. This was an evidence-driven audit and no // ASSUMPTION: code comments were added.
