---
title: "Prompts sent"
source_archive: "Software Projects"
source_path: "####Software Projects/# Eagle Rocket/Jamie Stern/Prompts/Prompts sent.docx"
status: reference
privacy: working
tags:
  - case-study
---

# Prompts sent

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
May 5

1a

TASK: Fix the missing custom-search.js enqueue.

CONTEXT

- Repo: jamie-stern-wp-content (you are at the repo root, which IS wp-content)

- File: themes/hello-elementor-child/functions.php

- Issue: around line 1757, the theme enqueues

get_stylesheet_directory_uri() . '/custom-search.js'

but the file does not exist. Every page generates a 404.

DO

1. Read themes/hello-elementor-child/functions.php and find the exact

enqueue block for custom-search.js. Report the line number and the

surrounding 10 lines.

2. Check if the script's logic is actually used elsewhere:

- Search for "customSearch" or "custom_search" in the theme

- Search for any AJAX handlers the script would call

(custom_search_posts is one we know about)

- Search for shortcodes or templates that depend on it

3. Based on what you find, choose ONE of these fixes and explain why:

a) Create a stub custom-search.js with the minimum logic needed

to call the existing custom_search_posts AJAX handler

b) Remove the enqueue if no dependent code exists

c) Move the enqueue to only fire on pages that need it

4. Implement the chosen fix on a new branch:

git checkout -b bugfix/custom-search-js-404

5. Commit with a clear message describing the fix.

6. Open a PR from the cloud interface when done.

DO NOT

- Refactor adjacent code in functions.php

- Touch other enqueues (rand() versioning is a separate fix)

- Push to main directly

- Rewrite history

REPORT

- Which fix you chose and why

- The diff

- Any AJAX/shortcode dependencies you found

- PR link when opened

DO NOT FABRICATE TOOL OUTPUT. Use real git commands and report

their actual output.

1a output

First proof-strike landed clean. This is exactly the right kind of work and the agent did it well.

What’s good about this:

The reasoning is solid. It didn’t just delete the enqueue — it verified that blog.js already implements the same behavior with the same selectors and same AJAX action. That’s the difference between “remove the broken thing” and “understand why it was broken and confirm nothing else relies on it.” It also correctly identified that creating a stub (option a) would have doubled the AJAX handler firing on blog pages, which would have been a worse outcome than the 404.

The dependency check covered all three places it could matter: the AJAX handler, the shortcode, the actual consumer. Confirming my_ajax_object is already localized onto jQuery globally means removing the redundant wp_localize_script is genuinely safe.

PHP lint clean, branched off main, PR opened. Textbook execution.

A few things to do now:

1.	Review the PR on GitHub. Even with the agent’s reasoning sounding right, a quick eyeball on the diff is worth doing. You’re checking: did it remove only the four-line enqueue + four-line localize block, or did it touch anything else? Should be a 16-line removal, no other changes.

2.	Test on local before merging. Spin up Local, load the site, open browser dev tools network tab, navigate to a few pages including the blog. Confirm:

•	No 404 for /custom-search.js

•	Blog search still works (type in search, results load)

•	Console is clean

3.	Then merge. Squash or merge as a single commit — this is one logical change. Either is fine; squash gives you a cleaner history.

The proof to send Sam:

You now have your first concrete artifact. Something like:

Hey Sam,

Quick first one from the audit list — the custom-search.js 404

that was firing on every page. Diff is small but it was a real

404 on every page request because the script file never shipped.

PR with reasoning: [link]

Branch: bugfix/custom-search-js-404

Lines changed: -16

Verified blog.js already implements the same search behavior, so

removing the dead enqueue was safe (a stub would have double-fired

the AJAX call on blog pages).

Easy one to port to your staging build if it has the same theme.

More coming.

— Marcus

That’s outcome, not philosophy. Diff link, what you did, why it was safe, signal that more is coming. Sam can verify in a minute and either say “already fixed in our rebuild” or “yes, please port.”

Next move:

The rand() → filemtime() fix (audit finding #6) is the natural follow-up. Same pattern: small, contained, easy to demo, real impact. Want the prompt for it?

This is a good moment, Marcus. You wanted GitHub-as-source-of-truth + cloud agent execution + Director Model directing rather than coding. That’s exactly what just happened. From your phone, against a real client codebase, with a clean PR at the end. The Nusa Lembongan workflow finally has the right tooling under it.​​​​​​​​​​​​​​​​

1b

TASK: Replace rand() asset versions with filemtime() in the

hello-elementor-child theme.

CONTEXT

- Repo: jamie-stern-wp-content (you are at the repo root)

- File: themes/hello-elementor-child/functions.php

- Issue: lines 26, 30, 31, 35 pass rand() as the asset version

parameter for custom.css, blog.css, blog.js, single-product.css.

This defeats browser caching site-wide.

DO

1. Read functions.php and locate the four enqueue lines.

2. For each, replace rand() with filemtime() pointed at the

actual asset file in the theme directory. Use:

filemtime( get_stylesheet_directory() . '/path/to/asset.ext' )

3. Verify each asset path actually exists in the theme before

referencing it in filemtime(). If an asset doesn't exist,

leave that enqueue untouched and flag it.

4. Create branch bugfix/asset-versioning-filemtime

5. Commit with a clear message.

6. Open a PR.

DO NOT

- Touch any other enqueue (custom-search.js is a separate fix

already in PR)

- Refactor the surrounding function

- Change asset paths or filenames

- Rewrite history

REPORT

- The diff

- Any assets that didn't exist (if any)

- PR link

DO NOT FABRICATE TOOL OUTPUT or invent async notifications.

DO NOT REWRITE GIT HISTORY.

1b output

wp_enqueue_style('custom-css', trailingslashit(get_stylesheet_directory_uri()) . 'assets/custom.css', array('hello-elementor', 'hello-elementor-theme-style', 'hello-elementor-header-footer'), rand());

•

wp_enqueue_style('custom-css', trailingslashit(get_stylesheet_directory_uri()) . 'assets/custom.css', array('hello-elementor', 'hello-elementor-theme-style', 'hello-elementor-header-footer'), filemtime( get_stylesheet_directory() . '/assets/custom.css' ));

if(is_page( 28934 ) || is_singular('post')) {

•

wp_enqueue_style('blog-css', trailingslashit(get_stylesheet_directory_uri()) . 'assets/blog.css', array('hello-elementor', 'hello-elementor-theme-style', 'hello-elementor-header-footer'), rand());

•

wp_enqueue_script('blog-js', trailingslashit(get_stylesheet_directory_uri()) . 'assets/blog.js', '', rand());

•

wp_enqueue_style('blog-css', trailingslashit(get_stylesheet_directory_uri()) . 'assets/blog.css', array('hello-elementor', 'hello-elementor-theme-style', 'hello-elementor-header-footer'), filemtime( get_stylesheet_directory() . '/assets/blog.css' ));

•

wp_enqueue_script('blog-js', trailingslashit(get_stylesheet_directory_uri()) . 'assets/blog.js', '', filemtime( get_stylesheet_directory() . '/assets/blog.js' ));

}

•

wp_enqueue_style('single-product-css', trailingslashit(get_stylesheet_directory_uri()) . 'assets/single-product.css', array('hello-elementor', 'hello-elementor-theme-style', 'hello-elementor-header-footer'), rand());

•

wp_enqueue_style('single-product-css', trailingslashit(get_stylesheet_directory_uri()) . 'assets/single-product.css', array('hello-elementor', 'hello-elementor-theme-style', 'hello-elementor-header-footer'), filemtime( get_stylesheet_directory() . '/assets/single-product.css' ));

Missing assets: none. All four target files (assets/custom.css, assets/blog.css, assets/blog.js, assets/single-product.css) verified present via ls before being referenced.

PHP lint: clean. Commit e5e2367a on bugfix/asset-versioning-filemtime, branched from main.

PR: https://github.com/WhiteHatForHire/jamie-stern-wp-content/pull/2

1c

TASK: Scope Swiper and product asset enqueues to pages that use them.

CONTEXT

- Repo: jamie-stern-wp-content (you are at the repo root)

- File: themes/hello-elementor-child/functions.php

- Issue: lines around 35-55 enqueue Swiper CSS/JS (from jsDelivr),

single-product CSS, custom.js, and single-product.js on ALL frontend

pages. Portfolio and content pages pay the cost without using them.

GOAL

Scope each asset to the pages that actually need it. Do not break

any page that currently uses these assets.

DO

1. Read functions.php and locate the global enqueue block (around

lines 35-55, may be wider).

2. For each asset, determine where it's actually used:

- Single-product CSS/JS: WooCommerce single product pages

(is_product())

- Swiper CSS/JS: search the theme for actual Swiper usage

(grep for "swiper", "Swiper", "new Swiper", swiper class names

in templates and shortcodes). Report what you find.

- custom.js: search for what it does. If it's truly site-wide

behavior, leave it global. If it's scoped, scope it.

3. Based on findings, propose a scoping plan BEFORE editing. Report:

- Which assets stay global and why

- Which assets get scoped and to what conditional

- Which assets you're uncertain about (flag for human review)

4. After reporting the plan, if no uncertainties, implement on

branch bugfix/scope-frontend-assets

5. Commit and open PR.

STOP CONDITIONS

- If Swiper usage is unclear or spread across many templates,

STOP after the report in step 3. Do not edit. Wait for human

decision on scoping strategy.

- If custom.js does anything that touches every page (analytics,

global UI behavior, header/footer scripts), leave it global and

note why.

DO NOT

- Touch the rand() enqueues (separate fix already in PR #2)

- Touch the custom-search.js enqueue (already merged)

- Refactor the surrounding function structure

- Add new abstractions or helper functions unless the existing

code already uses them

- Rewrite history

REPORT

- The scoping plan (what stays global, what gets scoped, what's

uncertain)

- The diff (if implemented)

- Any pages you're worried might break

- PR link

DO NOT FABRICATE TOOL OUTPUT or invent async notifications.

DO NOT REWRITE GIT HISTORY.

1c.1

TASK: Implement Option 1 — move asset enqueues into shortcode

callbacks for proper scoping.

CONTEXT

- You previously analyzed the asset/shortcode relationships and

stopped on uncertainty. We're now authorizing Option 1: enqueue

each asset inside its shortcode callback so it only loads when

the shortcode is rendered on the page.

- This is a real refactor of 8 shortcode callbacks. The "no refactor

adjacent code" rule is relaxed for this specific transformation.

ASSETS TO RESCOPE

- swiper-css and swiper-js: enqueue inside shortcodes that render

Swiper markup (luminous_slider, portfolio_slider, product_acf_slider,

qv_gallery, acf_product_gallery)

- single-product-css: enqueue inside shortcodes that render product-

specific markup, OR scope to is_product() if cleaner

- single-product-js: same logic — enqueue where its accordion/lightbox

markup is rendered, including inside shortcode callbacks where

applicable

ASSETS TO LEAVE GLOBAL (per your earlier analysis)

- custom.js: contains global browseByColor() and delegated handlers,

leave global

- custom.css: not analyzed as scoped, leave global

EXECUTION RULES

- Branch: bugfix/scope-frontend-assets-shortcode-callbacks

- One commit per shortcode callback modified, with clear messages

describing what was moved

- Inside each shortcode callback, use wp_enqueue_style/wp_enqueue_script

with the same handles, paths, dependencies, and filemtime() versions

as the global enqueues

- Remove the corresponding global enqueues from wp_enqueue_scripts

ONLY after all shortcode callbacks are updated

- Preserve the existing filemtime() versioning we just landed in PR #2

STOP CONDITIONS — apply the same "stop on uncertainty" rule

1. AJAX response rendering: if load_product_quick_view AJAX returns

HTML that needs Swiper, flag it. Do not assume the assets will

be available; either keep Swiper global on product pages or print

inline in the AJAX response. Report which approach you chose.

2. Elementor integration: if any Elementor widget calls these

shortcodes via do_shortcode() in a way you can detect, flag it.

Late enqueues from inside shortcodes called after wp_enqueue_scripts

may not load reliably. If unclear, flag and proceed with the

global wp_enqueue_scripts approach for that asset.

3. Shortcode nesting: if a shortcode renders content that contains

another shortcode, the inner one will handle its own enqueue.

Note any nesting you find, do not duplicate enqueues.

4. Any shortcode where the markup-to-asset mapping is unclear from

the code: skip it, leave the asset global, document in PR.

DELIVERABLE

PR description must include:

- Per-shortcode summary: what was moved, what stayed, why

- AJAX/Elementor/nesting decisions and reasoning

- Anything left global with explanation

- Risk assessment per change (low/medium/high)

- "Things to test on Local before merging" checklist for the human

reviewer (specific page types: product page, portfolio with slider,

quick-view AJAX, browse-by-color page, etc.)

DO NOT

- Touch custom.js or custom.css enqueues

- Touch the rand() fixes (already shipped)

- Touch the custom-search.js enqueue (already shipped)

- Rewrite history

- Squash commits

REPORT

- PR link

- List of shortcodes modified with brief description

- Anything skipped and why

- The testing checklist

DO NOT FABRICATE TOOL OUTPUT.

1c output

I'm going to stop and report rather than edit. Here's why.

## Findings

custom.js (137 lines) actually does:

1. Delegated click handler on .quick-view-btn (anywhere a quick-view button exists) — opens an Elementor popup, AJAXes in product gallery markup, then calls initQuickViewSlider() which initializes Swiper on the loaded markup.

2. On document.ready, initializes Swiper for .luminous-slider, .mySwiper/.mySwiper2, .main-gallery if present.

3. Defines a global function browseByColor() that is called from inline onclick="browseByColor(...)" in browse_by_color_shortcode.

single-product.js (168 lines) actually does:

1. Generic accordion behavior on .accordion-title / .accordion-content / .accordion-item (document-ready).

2. Initializes Swiper for .acf-swiper-gallery (.main-swiper + .thumb-swiper).

3. Lightbox click handler for .acf-swiper-gallery .main-swiper .swiper-slide — builds a Swiper-driven lightbox.

Where Swiper-using markup is rendered (all in functions.php):

| Selector | Rendered by | Hooked as |

|---|---|---|

| .luminous-slider | luminous_slider_shortcode | shortcode [luminous_slider] (line 638) |

| .mySwiper/.mySwiper2 | portfolio_slider_shortcode | shortcode [portfolio_slider] (line 714) |

| .main-gallery | product_acf_slider_shortcode | shortcode [product_acf_slider] (line 773) |

| .qv-main-slider/.qv-thumb-slider | load_product_quick_view AJAX response (line 109-151) and qv_gallery_shortcode (line 1359) | AJAX action + shortcode [qv_gallery] |

| .acf-swiper-gallery | acf_product_gallery_shortcode (line 1051, also dup-registered at 1165) | shortcode [acf_product_gallery] |

| .accordion-* (theme's) | product_acf_category_accordion | shortcode [product_acf_accordion] (line 969) |

| .quick-view-btn markup | inside loop/template renderers in functions.php (lines 355, 1442) and gallery-load-more.php:311 | rendered when product loops are output |

| browseByColor() callsite | browse_by_color_shortcode (lines 1318, 1330) | shortcode [browse_by_color] |

The problem with page-conditional scoping: Every consumer is a shortcode (or AJAX-loaded markup). Shortcodes are placed by editors into arbitrary pages via Elementor — their location is data in the WP database, not in the code. We can guess based on intent (luminous_slider -> home, product_acf_* -> product singles), but we cannot prove from code that an editor hasn't dropped [product_acf_accordion] onto a content page or [browse_by_color] onto a marketing landing page.

Real risks if I scoped by page conditional:

- Scoping single-product.js to is_product() breaks any non-product page that embeds [product_acf_accordion] (accordion stops working) or [acf_product_gallery] (gallery + lightbox stop working).

- Scoping custom.js to product/portfolio/home conditionals breaks [browse_by_color] (ReferenceError on the inline onclick) and breaks Quick View buttons on any custom page that lists products.

- Scoping Swiper to "Woo + home" pages breaks every shortcode-embedded slider on a non-Woo page.

Plugin namespace check: The grep across plugins shows accordion classes from cookie-law-info (.cky-app-accordion-title) and Elementor (.elementor-accordion-title, .n-accordion-title). None collide with the bare .accordion-title the theme uses, so the theme's accordion handler is unique to [product_acf_accordion].

## Scoping plan

| Asset | Recommendation | Why |

|---|---|---|

| single-product-css (already global at line 35) | Uncertain — flag | Selectors include both .acf-swiper-gallery (shortcode-driven, could be embedded anywhere) and product-only selectors. Page-scoping risks breaking shortcode-embedded galleries on non-product pages. |

| swiper-css / swiper-js (jsDelivr) | Uncertain — flag | Needed wherever any of the eight shortcodes above is embedded, plus AJAX quick-view modal. Cannot determine page set from code. |

| custom.js | Leave global | Defines browseByColor() consumed by inline onclick from [browse_by_color], and the delegated .quick-view-btn click handler is global UI behavior. Removing it from any page that embeds either shortcode silently breaks them. Matches the STOP rule "global UI behavior". |

| single-product-js | Uncertain — flag | Accordion behavior is generic enough that [product_acf_accordion] could be on any page. The lightbox handler is also a $(document).on(...) delegated handler. |

Nothing is clearly safe to scope by is_product() / is_singular('post') / etc. without risking shortcode-embedded breakage on pages we can't enumerate from code.

## Stopping per the task's STOP condition

> If Swiper usage is unclear or spread across many templates, STOP after the report in step 3. Do not edit.

Swiper usage is spread across eight different shortcodes plus an AJAX-loaded modal. I'm not editing.

Recommended path forward (needs human decision):

1. Best fix (requires the "no new abstractions" rule to be relaxed): Move each wp_enqueue_* for Swiper / custom.js / single-product.js / single-product.css into the corresponding shortcode callback (and the load_product_quick_view AJAX handler can localize a flag, or the click handler can lazy-load Swiper). Then assets only load on pages that actually render the shortcode. This is the WordPress-idiomatic answer and is what scoping really requires here, but it touches eight functions and is a refactor — outside the current task's "do not refactor" guardrail.

2. Second-best fix (page-conditional, with editor's confirmation): If the editor can confirm a fixed mapping (e.g. "[luminous_slider] is only on the front page; [product_acf_*] is only on is_product() and the page IDs X, Y, Z"), I can scope to is_front_page() || is_product() || is_page([X,Y,Z]) || is_singular('post-type-portfolio'). But that requires the editor to enumerate the embedding pages — code can't tell us.

3. Compromise (low-risk subset): Scope only single-product-css to is_product() || is_singular('product') — it's enqueued at line 35 and its name strongly implies product-only intent. But even here the file styles .acf-swiper-gallery which could be on non-product pages, so this still has a real risk.

No PR opened. Branch bugfix/scope-frontend-assets not created. No commits, no diff, repo unchanged from current main + the two open PRs.

---

Stopped per STOP condition. No edits made.

Findings:

- custom.js: Quick View click handler (delegated, $(document).on), Swiper init for .luminous-slider/.mySwiper/.mySwiper2/.main-gallery, and global function browseByColor() consumed by inline onclick= in [browse_by_color] shortcode. Touches global UI behavior.

- single-product.js: generic accordion handler on .accordion-title/.accordion-content, Swiper init for .acf-swiper-gallery, and lightbox click handler.

- All Swiper-using markup is rendered via SHORTCODES: [luminous_slider], [portfolio_slider], [product_acf_slider], [qv_gallery], [acf_product_gallery], [product_acf_accordion], [browse_by_color], plus the load_product_quick_view AJAX response.

Why I stopped:

- Shortcode placement lives in the WP database (page/post content), not in code. Page-conditional scoping (is_product, is_page, etc.) cannot prove an editor hasn't embedded these shortcodes onto arbitrary pages.

- custom.js qualifies as global UI behavior (browseByColor global, delegated quick-view handler) per the STOP rule -> leave global.

- single-product.js, single-product-css, swiper-css, swiper-js cannot be scoped safely from code alone -> flagged.

Recommendations needing human decision:

1. Idiomatic fix: enqueue each asset INSIDE its shortcode callback. Requires relaxing "no refactor" rule (touches 8 functions).

2. Page-conditional fix: requires editor to enumerate which pages embed which shortcodes.

3. Low-risk partial: scope single-product-css to is_product() || is_singular('product'). Still some risk because .acf-swiper-gallery is shortcode-driven.

PR: none opened.

1c.1 output

I'll start by mapping each shortcode callback's full body so I know exactly what markup it renders and can place enqueues correctly.

Before I execute, I need to share what changed in my understanding once I read the actual file contents. Two important findings:

1. browse_by_color_shortcode and the qv_gallery in functions.php are inside /* */ blocks (1297-1351 and 1353 onwards). The active qv_gallery is in gallery-load-more.php. So browseByColor() (defined in custom.js) has no active call sites in the current code.

2. portfolio_slider_shortcode, product_acf_slider_shortcode, and product_acf_category_accordion already self-gate with is_singular(...) / is_product() early-returns. So enqueues placed inside them are auto-scoped.

3. Critical Swiper blocker — custom.js (which the task instructs us to leave global) calls new Swiper(...) unconditionally at document.ready in four places (lines 40, 60, 85, 97). If I move swiper-js out of global enqueue, every page without a Swiper-using shortcode will throw ReferenceError: Swiper is not defined from custom.js, killing the rest of the ready handler. Same for initQuickViewSlider() when .quick-view-btn is clicked on a page without Swiper.

Per STOP condition 4, I'm skipping Swiper. Moving it requires either (a) editing custom.js to add typeof Swiper !== 'undefined' guards, or (b) moving custom.js itself to be conditional — both outside this task's scope per the DO NOT list.

Revised plan I'll execute:

| Asset | Action | Why |

|---|---|---|

| swiper-css | Skip — leave global | custom.js depends on Swiper at unconditional document.ready |

| swiper-js | Skip — leave global | same |

| single-product-css | Move into 2 shortcodes | clean shortcode-driven mapping |

| single-product-js | Move into 2 shortcodes | clean shortcode-driven mapping; safe on Swiper-missing pages because its new Swiper(...) is inside .each(...) over shortcode-rendered markup that's gated by Swiper-staying-global |

Target shortcodes for single-product-* enqueues:

- acf_product_gallery_shortcode (line 1054) — renders .acf-swiper-gallery markup

- product_acf_category_accordion (line 840) — renders .product-accordion markup, already gated is_product()

Now executing.

Wait — I need to reconsider the branch base. PR #2 changes line 35 (rand() → filemtime()); I'm about to remove that line. If I branch from main (which has neither PR merged), my removal of line 35 will conflict with PR #2's edit at the same line. The task says "Preserve the existing filemtime() versioning we just landed in PR #2" — so I should branch off PR #2's tip.

Now commit 1 — add single-product-css and single-product-js enqueues inside acf_product_gallery_shortcode. I'll insert right after if (!empty($images)): so they only enqueue when markup is actually produced.

Commit 2 — same enqueues inside product_acf_category_accordion. The function already gates with is_product() early-return (line 842), so I'll insert right after that gate so non-product pages don't enqueue.

Commit 3 — remove the global enqueues for single-product-css (line 35) and single-product-js (line 55).

Three clean commits on top of PR #2's tip. Pushing and opening PR.

## Done

PR: <https://github.com/WhiteHatForHire/jamie-stern-wp-content/pull/3>

Stacked on PR #2 (base = bugfix/asset-versioning-filemtime) so the diff stays focused. Once #2 merges, GitHub will auto-retarget to main.

### Shortcodes modified

- acf_product_gallery_shortcode — added enqueues for single-product-css + single-product-js inside the if (!empty($images)) block (so they only fire when output is actually produced)

- product_acf_category_accordion — added the same enqueues right after the existing if ( ! is_product() ) return; early-return

Then removed both global wp_enqueue_* calls for single-product-css (line 35) and single-product-js (line 55) from child_theme_configurator_css().

Three commits, one per task step:

- 20f485ed — enqueue inside acf_product_gallery_shortcode

- 7f3bdf55 — enqueue inside product_acf_category_accordion

- b6a655f1 — remove global enqueues

### Skipped (with reasons in PR body)

- Swiper (swiper-css/swiper-js) — custom.js (kept global per task) calls new Swiper(...) unconditionally at document.ready on lines 40/60/85/97. Moving Swiper would throw ReferenceError site-wide and break the Quick-View AJAX flow. Stop condition 4 applies. Documented as a follow-up requiring either guards inside custom.js or making custom.js itself conditional.

- luminous_slider, portfolio_slider, product_acf_slider, qv_gallery — only carry Swiper markup, no single-product-* dependency, so nothing to move while Swiper stays global.

- Two /* */-blocked shortcodes (browse_by_color, qv_gallery in functions.php) — not actively registered; no edits needed.

### What the human reviewer needs to test on Local

Full per-page checklist is in the PR body. Headlines:

- Should still work: single product (accordion + ACF gallery + lightbox), Quick View modal anywhere .quick-view-btn renders.

- Should now load less: homepage, portfolio singles, blog/archive, My Account, Cart, Checkout, plain content pages — verify in network tab that single-product.css / single-product.js no longer appear.

- Edge cases: any page using .grid-products .elementor-grid (styled in single-product.css), any page using bare .accordion-title/.accordion-content outside the shortcode, and Elementor cached-output behavior with shortcode-based late enqueues.

1d

TASK: Ship a batch of six audit fixes as a single PR.

CONTEXT

- Repo: jamie-stern-wp-content (you are at the repo root)

- This is a deliberate test of multi-finding batched work.

- All fixes target the same theme/plugin codebase. None depend

on each other. None require Local site testing for code-correctness

(security and config changes).

- Sandbox environment. Worst case is git revert.

FIXES TO SHIP (each is independent — if one is uncertain, skip it

and continue with the others, do not block the batch)

1. Remove wp-phpmyadmin-extension from active plugins

- Read wp_options is not accessible from filesystem; instead,

look in plugins/ directory and rename plugins/wp-phpmyadmin-extension

to plugins/wp-phpmyadmin-extension.disabled OR document in PR

that the active_plugins option needs to be updated in DB by

human after merge.

2. Add SVG sanitization

- functions.php lines 1568-1573 add svg to allowed MIME types.

- Either: restrict the cu_mime_types filter to admin role only,

OR add a comment recommending Safe SVG plugin installation.

- Pick the smaller change. If unsure, write the role restriction.

3. Add nonce + rate guard to load_product_quick_view AJAX

- functions.php ~line 64 registers wp_ajax + wp_ajax_nopriv

- Add nonce verification using check_ajax_referer

- Add a basic minimum-input validation (product_id must be a

valid published product)

- Note in PR: nonce must be passed from the calling JS;

update site templates that render quick-view buttons.

4. Add nonce + minimum length to custom_search_posts AJAX

- functions.php ~line 1709 registers wp_ajax + wp_ajax_nopriv

- Add check_ajax_referer

- Reject queries shorter than 2 characters

- Note in PR: same nonce-passing requirement on calling JS

5. Add nonce + input validation to qv/v1/load-more REST route

- gallery-load-more.php ~line 429

- Replace permission_callback => '__return_true' with nonce

verification using wp_verify_nonce on X-WP-Nonce header

- Validate offset is a non-negative integer with reasonable max

- Validate page_id is a published page

- Note in PR: REST nonces are different from AJAX nonces;

calling JS must send X-WP-Nonce header with rest nonce.

6. Investigate AI1WM Unlimited Extension version mismatch

- Read plugin headers for all-in-one-wp-migration and

all-in-one-wp-migration-unlimited-extension

- Report the versions in PR description

- If versions are clearly mismatched per public compatibility

info you can determine from the plugin files alone, recommend

the fix (do not implement). If unclear, just report findings.

EXECUTION RULES

- Branch off latest main: bugfix/audit-batch-security-config

- Commit per fix with clear messages (NOT one giant commit). Six

commits expected unless a fix is skipped.

- If any fix has uncertainty about scope or risk, SKIP IT and

document in PR description. Do not guess past uncertainty on

security code.

- Do not refactor adjacent code.

- Do not touch the rand() enqueues, custom-search.js enqueue,

or Swiper enqueues (separate fixes already merged).

- Do not rewrite history.

- Do not invent async notifications.

DELIVERABLE

PR description must include, for each fix:

- What was changed

- What was skipped (if any) and why

- Frontend follow-up required (e.g., "calling JS must pass nonce")

- Risk level (low/medium/high)

REPORT

- PR link

- Per-fix status: shipped, skipped (with reason), or partial

- Any ASSUMPTION comments left in code

DO NOT FABRICATE TOOL OUTPUT.

DO NOT REWRITE GIT HISTORY.
