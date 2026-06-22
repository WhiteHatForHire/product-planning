---
title: "maxs guide to agentic coding"
source_archive: "Software Projects"
source_path: "####Software Projects/# Eagle Rocket/Jamie Stern/# Final Docs/maxs-guide-to-agentic-coding.docx"
status: reference
privacy: private/internal
tags:
  - case-study
---

# maxs guide to agentic coding

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
PRACTICAL GUIDE  /  AGENTIC CODING METHOD  /  2026

Max's Guide to

Agentic Coding

Jamie Stern Example

The complete working method, including platform setup, the meta-prompting workflow, branch strategy, parallel agents, and verbatim prompts from twenty merged pull requests. Written so your team can copy what works.

Maxwell

Eagle Rocket LLC  •  WhiteHatForHire

Written for Sam, May 2026

Contents

0

Why this exists

How to read this guide

1

Platform setup

Cloud Claude Code, Local Claude Code, Codex, Replit, Local by Flywheel

2

The routing rule

Which agent does what, and why

3

How to prompt

The five-section structure with annotated examples

4

Meta-prompting

Having the LLM write the prompt for the agent

5

Branch strategy

Stacked PRs, parallel agents, and avoiding collisions

6

Verification

Before/after, valid+invalid, and the gotchas

7

Failure modes

Six failures from this engagement and the rules they produced

8

Prompt library

Twelve real prompts from Jamie Stern, ready to adapt

9

The prompt pack

Permanent rules, routing rules, and templates

10

Starting your team

Three concrete things you can do this week

0. Why this exists

Sam, you said you're watching the agentic AI space and trying to figure out what's real. The case study answers what was delivered. This document answers how. It's the playbook I wish someone had handed me two years ago when I was figuring this out by trial and error.

This isn't theory. Every prompt in here was sent to a real agent against your real codebase. Every rule came from a moment when something nearly went wrong, or did go wrong, and I had to figure out how to keep it from happening again. Every command and PowerShell snippet is what I actually ran. Treat this as a working reference.

Two ground rules before any of the rest of this matters:

The agents are staff, not magic. They will write better code than most junior engineers when directed well, and worse code than a tired senior when directed badly. The variable is the direction.

Bounded autonomy beats maximum autonomy. Agents that have permission to act and permission to halt produce better outcomes than agents told to figure it out. Tight scope, clear stop conditions, real verification. Every time.

HOW TO READ THIS

Sections 1-2 are the platforms and how to route work between them.

Sections 3-4 are how to write prompts — including the meta-prompting trick.

Section 5 covers running multiple agents in parallel without breaking everything.

Sections 6-7 are verification and the failure modes you will hit.

Section 8 is twelve real prompts you can copy and adapt today.

Sections 9-10 are the prompt pack and how your team can start tomorrow.

1. Platform setup

Three coding agents, one local environment, one private repo. The setup is the foundation. Get it right once and you stop thinking about it for every engagement after that.

Cloud Claude Code

What it is. Anthropic's coding agent running on their cloud infrastructure. You access it through claude.ai/code in any browser. Or on the Claude mobile app (Yes, you can do this from your phone!) Connects to a GitHub repository and works on your code remotely.

What it can do. Read every file in the connected repo. Write code. Create branches. Open pull requests. Run shell commands inside its sandbox. Search the web when allowed.

What it cannot do. Reach your laptop. The cloud sandbox is a Linux container with public-internet access only. Hostnames like jamie-stern.local exist only on your machine — they point to 127.0.0.1, your laptop's loopback. The cloud sandbox has its own loopback that has nothing on it. So when Cloud CC tries curl https://jamie-stern.local/, it asks public DNS, gets nothing, fails.

Setup steps:

Sign in at claude.ai with a Pro or Max plan.

Go to claude.ai/code or open the mobile app ‘code’ tab.

Connect your GitHub account. Authorize the repo (or repos) you want it to work on.

Open a new chat. Tell it which repo to work on.

Send a small first task to confirm everything connects: 'Read the README and tell me what this project does.'

Cost. Bundled in your Claude subscription. Pro plan covers casual use. For full-engagement work expect to use Max usage tier or hit limits. Model tip: Use Sonnet for most work. Opus only when you are doing something super intense or writing specs.

Best for. Code generation, refactors, PR creation against any repo on GitHub. Mobile-friendly because it runs in the cloud.

Local Claude Code

What it is. The same Claude Code agent, running on your laptop instead of in the cloud. You install it as a desktop app or via the npm CLI.

What it can do. Everything the cloud version can do, PLUS reach your local site, run PowerShell or bash commands on your machine, inspect files in any directory, hit localhost, run WP-CLI, anything you can do in your terminal.

Setup steps:

Download Claude Code from claude.ai/download or install via npm install -g @anthropic-ai/claude-code

Authenticate with your Claude account on first run.

Open a terminal, navigate to your project directory.

Run claude to start a session. The agent now has access to that directory.

Optional but recommended: enable bypass mode for trusted projects so it doesn't ask for confirmation on every file edit.

Cost. Same plan, same usage limits. Local CC and Cloud CC share the same usage pool.

Best for. Verification against running local sites, file inspection, running shell scripts, anything that needs your laptop.

Codex (OpenAI)

What it is. OpenAI's coding agent. Available through ChatGPT Plus, Pro, or via codex.openai.com. Different model family than Claude (GPT-5 / GPT-Codex) but same general workflow.

Setup steps:

Sign in to ChatGPT with a Plus or Pro subscription.

Go to codex.openai.com or use the Codex app.

Connect to GitHub the same way.

Best for. Triage, audit reports, plugin matrices, smoke test specs, performance roadmaps, prompt packs, case studies. When the deliverable is a document rather than code, Codex's writing quality on technical reports is consistently strong, and you don't need codebase access for those tasks.

Worth knowing. Codex sometimes produces stronger written reports for the same input. Claude Code sometimes produces tighter code. I use both. Running the same prompt across both and comparing outputs is a real workflow — I call it the Council of Models.

Replit Agent

What it is. Replit hosts your project on their infrastructure. The agent has direct access to the live runtime.

Why I deliberately did NOT use it on Jamie Stern. Replit's strength is greenfield work — vague spec, build something fast, see it running. It is the wrong tool for inherited client codebases. Replit plows through ambiguity, which is the right behavior for discovery and the wrong behavior for client work where you can't afford a guess.

Where Replit shines. My own project, Anchor, was started on Replit. The agent and the runtime are co-located. That works because I own the runtime and I'm fine with the agent making architectural decisions inside my project. On client work, I am not. I’ve since migrated to Codex/Claude Code and am saving $ as well as having better control over every step and decision.

Local by Flywheel

What it is. A free desktop app that spins up a local WordPress site that mirrors a live one. Available at localwp.com.

Setup steps for cloning a live site:

Install Local by Flywheel.

On the live WordPress site, install the All-in-One WP Migration plugin.

Use AIO Migration to export the site (excluding uploads/backup and uploads/wpmc-trash to keep the file size down).

In Local, create a new site and import the AIO Migration file.

Site is now running at https://your-site.local on your laptop.

For Jamie Stern this took about 45 minutes to download from WP Engine and 30 minutes to import into Local.

Private GitHub repository

Why this matters. The repo is your source of truth. Everything you ship goes through it. Cloud CC works against it directly. Local CC pushes to it from your laptop. Codex can read it for analysis. PRs are the unit of work.

For Jamie Stern setup:

Created a private repo at WhiteHatForHire/jamie-stern-wp-content.

Initialized git inside the wp-content directory of the local clone (not the entire WordPress install — only the part I'd be modifying).

Added .gitignore excluding uploads/, cache/, and SQL dumps. Final tracked baseline was 144 MiB across 37,292 objects.

First push hit a 144 MiB HTTPS transport error. Fixed with git config http.postBuffer 524288000 and git config http.version HTTP/1.1.

THE TWO GIT SETTINGS THAT FIX THE MOST COMMON PUSH ERRORS

git config --global http.postBuffer 524288000

git config --global http.version HTTP/1.1

First one increases the buffer to 500MB. Second forces HTTP/1.1 for compatibility.

2. The routing rule

Different agents are good at different things. Sending the right task to the right surface is half of why this works. The other half is verification.

THE RULE, IN ONE SENTENCE

Cloud for code. Local for verification. Codex for synthesis.

What that means in practice

Cloud Claude Code: code generation

If the task is 'write code, commit it, open a PR,' Cloud CC is the surface. It has the full repo, runs against the GitHub API for branch creation and PR opening, and produces clean diffs. Most of the 20 PRs in the Jamie Stern engagement were Cloud CC. You can run as many instances concurrently as you want.

Local Claude Code: verification

If the task is 'confirm the change actually works on the running site,' Local CC is the surface. It can hit jamie-stern.local, parse the HTML, check console errors, run WP-CLI commands, inspect the filesystem in real time. Cloud CC cannot do any of that.

Codex: synthesis

If the deliverable is a document — audit report, plugin matrix, roadmap, smoke test plan, prompt pack, case study — Codex is the surface. Its writing quality on technical reports is consistently strong, and it doesn't need codebase access for those tasks.

The handoff pattern

When a task crosses surfaces, split it explicitly. Don't try to make one agent do both jobs.

Real example from PR #4 (security batch). Cloud CC wrote the server-side nonce validation on three AJAX endpoints and opened the PR. Local CC then verified, against the running site, that valid nonces returned 200 and invalid nonces returned 403. Two agents, two prompts, one merge.

# Step 1 — Cloud CC prompt:

TASK: Add nonce validation to three AJAX endpoints.

Server-side only. JS counterpart is a separate PR.

Open as PR. Stop conditions listed below.

# Step 2 — After Cloud CC opens the PR, Local CC prompt:

PR #4 is open. Pull the branch locally. Run the verification

script below against jamie-stern.local. Confirm valid nonces

return 200 and invalid nonces return 403. Report results.

When the cloud sandbox can't reach localhost

This was a real moment of confusion in the Jamie Stern engagement. I asked Cloud CC to verify a fix on the running local site. It returned connection errors. I thought the fix was broken. The actual problem was that Cloud CC physically cannot reach jamie-stern.local because the hostname only resolves on my Windows machine.

Three options when you hit this:

Use Local CC for verification. This is what local CC is for. Different jobs, different tools. Most of the time, this is the answer.

Eyeball it in the browser. Honestly fine. Open the site, click around. For most engagements, this is faster than scripting it.

Cloudflare tunnel. If you do this kind of work often and want Cloud CC to verify production-coupled features, run cloudflared on your laptop to expose jamie-stern.local at https://something.trycloudflare.com. Cloud CC can hit that URL. Real capability upgrade, but probably not worth it for one engagement.

PERMANENT RULE

Code generation against a GitHub repo: Cloud Claude Code.

Verification against a running local site: Local Claude Code.

Triage, audit reports, prompt packs, decision matrices: Codex.

Do not ask Cloud Claude Code to verify local-only URLs or browser behavior.

3. How to prompt

Every prompt I send to every agent has the same structure. Not because I'm rigid — because I learned that vague prompts produce drift, and drift produces work that has to be redone.

The five sections of every good prompt

Task. One sentence. What are you trying to accomplish.

Context. Files involved, line numbers if known, recent related work. Just enough for the agent to orient.

Do. Numbered list of concrete actions. Short. Sequential.

Stop conditions. Things that would make the agent halt and ask. Be specific about what counts as a real blocker.

Don't. Hard prohibitions. Things you absolutely don't want the agent to do, regardless of how reasonable it seems in the moment.

Example 1: A simple prompt

SENT TO: Cloud Claude Code    PURPOSE: Removed dead enqueue (PR #1)

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

DON'T

- Refactor adjacent code

- Touch other enqueues

- Push to main directly

- Rewrite history

DO NOT FABRICATE TOOL OUTPUT.

This prompt is short by design. The task is contained. The agent doesn't need a lot of context. Notice that step 3 gives the agent three options to choose from rather than telling it which fix to apply — because I genuinely didn't know which was right and I wanted the agent to read the code and decide.

Example 2: A prompt with explicit STOP CONDITIONS

SENT TO: Cloud Claude Code    PURPOSE: Asset scoping with architectural blocker (PR #3)

TASK: Implement Option 1 — move asset enqueues into shortcode

callbacks for proper scoping.

ASSETS TO RESCOPE

- swiper-css and swiper-js: enqueue inside shortcodes that render

Swiper markup

- single-product-css: enqueue inside product-specific shortcodes,

OR scope to is_product()

- single-product-js: same

ASSETS TO LEAVE GLOBAL

- custom.js: contains global browseByColor() and delegated handlers

- custom.css: not analyzed as scoped, leave global

STOP CONDITIONS

1. AJAX response rendering: if load_product_quick_view returns

HTML that needs Swiper, flag it

2. Elementor integration: if any widget calls these shortcodes

via do_shortcode() in a way you can detect, flag it

3. Shortcode nesting: if a shortcode renders content that contains

another shortcode, note any nesting

4. Any shortcode where mapping is unclear: skip it, leave global

DELIVERABLE

PR description must include a "Things to test on Local" checklist.

DO NOT FABRICATE TOOL OUTPUT.

This is the prompt that triggered the Swiper architectural stop. The agent opened custom.js, saw that it calls new Swiper() unconditionally on four different lines at document.ready, and stopped at stop condition #1. Without those stop conditions, it would have shipped a change that broke JavaScript on every non-slider page of the site.

WHAT GOOD STOP CONDITIONS LOOK LIKE

Specific, named, verifiable. 'If X is true, stop and document.'

NOT 'use your judgment.' That's an invitation to drift.

Stop conditions are how you protect the parts of the codebase you don't want the agent to touch even if the change seems reasonable.

Example 3: A meta-coordination prompt

SENT TO: Cloud Claude Code    PURPOSE: Performance refactor with awareness of recent merges (PR #8)

TASK: Optimize qv-gallery and custom search AJAX/REST performance

without changing frontend behavior.

CONTEXT

- Repo: jamie-stern-wp-content

- Files in scope:

- themes/hello-elementor-child/gallery-load-more.php

- themes/hello-elementor-child/functions.php (search AJAX section)

- themes/hello-elementor-child/assets/qv-gallery.js (READ ONLY,

do not modify — JS already updated by PR #5)

- Recent merged work to NOT undo:

- PR #4: nonce + input validation already added to qv/v1/load-more

REST route, load_product_quick_view AJAX, custom_search_posts AJAX

- PR #5: JS already sends nonces correctly

- This PR is about query/cache efficiency, not security or UX.

DO

1. Identify -1 queries, full iterations, short cache TTLs

2. Propose ONE strategy BEFORE implementing:

a) Replace -1 query with paginated SQL via $wpdb

b) Move data into transients with invalidation hooks

c) Increase cache TTL with explicit invalidation

d) Remove duplicated handlers if REST is the actual path

3. After reporting strategy, implement on bugfix/qv-gallery-performance

STOP CONDITIONS

- If a -1 query has a bounded result set (e.g., all categories),

leave it and document

- If transient invalidation requires plugin code, STOP and document

DON'T

- Touch nonce/security code (PR #4 owns that)

- Modify qv-gallery.js (PR #5 owns that)

- Refactor unrelated code

DO NOT FABRICATE TOOL OUTPUT.

This prompt is heavier on context because it had to coordinate with already-merged work. Notice how it explicitly names the boundaries: which files PR #4 owns, which files PR #5 owns. The agent then knew exactly what NOT to touch.

This prompt also asks for a strategy step before implementation. The agent produced a five-finding strategy table before writing any code. One of the findings was that wp_cache_* is request-scoped and a no-op without a persistent object cache backend, which is the kind of insight you want before the agent writes 200 lines that don't actually do anything.

4. Meta-prompting: have the LLM write the prompt

This is the most important workflow trick in this guide. The agent that ships the code is rarely the one that writes the prompt. Use a smarter conversational LLM to design the prompt, then send the polished version to the coding agent.

The pattern

Most people send their first draft of a prompt directly to a coding agent. That works for simple tasks. For anything non-trivial, you get better results by treating prompt-writing as its own task with its own model.

My setup:

Conversational LLM (Claude in chat, ChatGPT, Gemini): the meta-prompter. Use this to draft, refine, and review prompts.

Coding agent (Cloud CC, Local CC, Codex): the executor. Receives the polished prompt and ships the work.

The meta-prompter has full context on your engagement, the previous PRs, the conversation history with the client, the architectural blockers, the rules you've added to the prompt pack. The coding agent doesn't need any of that — it just needs the final, scoped, executable prompt.

How I actually used this on Jamie Stern

Through the entire engagement I was running a Claude conversational chat in the background. That chat had every PR's outcome, every failure mode, every architectural decision. When I needed to write a new prompt, I'd describe what I wanted to the conversational Claude. It would draft a prompt. I'd review, edit, and send it to Cloud CC.

A real example.

After PR #6 hit the Swiper architectural blocker, I wanted to ship the next batch of work. I asked the conversational Claude:

I want to ship more PRs but several items are blocked by the Swiper

issue. What's still cleanly shippable that doesn't touch Swiper or

the asset enqueue code I've already worked on?

The conversational Claude analyzed what was already shipped, what was blocked, and produced a six-item list with proposed agent routing for each. Then it offered to write the full prompts for the top three. That output became Prompts 1-3 of the next batch (image sizes, media cleanup analysis, gallery performance).

This is what meta-prompting saves you from: starting every prompt cold without remembering all the constraints from the previous twelve hours of work.

How to ask for a prompt

The simplest version is:

I need to [task]. The codebase is [context]. The last PR did

[recent work]. I'm worried about [risks]. Write me a prompt for

[which agent] following the standard structure: TASK, CONTEXT, DO,

STOP CONDITIONS, DON'T.

Better version, with constraint-passing:

I need to [task]. Here's the context:

- [Previous PR list]

- [Files already touched]

- [Architectural blockers]

- [Recent client conversation summary]

Write me a prompt for [Cloud CC / Local CC / Codex]. Follow my

standard structure (TASK / CONTEXT / DO / STOP CONDITIONS / DON'T).

Append "DO NOT FABRICATE TOOL OUTPUT" and "DO NOT REWRITE GIT

HISTORY" at the end.

Coordination notes:

- Don't touch [files already in flight in another PR]

- Branch off latest main

- The prompt should be small enough that I can review the diff

in 5 minutes

That last paragraph is the one most people skip. Telling the meta-prompter what NOT to put in the prompt produces tighter prompts. 'Small enough that I can review in 5 minutes' is a real constraint that produces real scoping.

The Council of Models pattern

For high-stakes decisions, send the same prompt to multiple conversational LLMs and compare. I run this regularly: Claude, ChatGPT, Gemini, sometimes Grok. Different models catch different things. If three of four agree on the approach, that's a strong signal. If they disagree, that's a flag worth investigating.

On Jamie Stern, I used the Council pattern for the strategic call about whether to send Sam the audit findings early or wait for proof-strikes. Three models said 'wait, ship the proof first.' One model said 'send the findings now to establish presence.' The majority view was right. Sending an audit before fixes makes you sound like a consultant. Sending an audit alongside merged fixes makes you sound like you ship.

When NOT to meta-prompt

Tiny tasks. 'Format this paragraph' doesn't need a meta-prompt.

Tasks where the agent already has full context from a previous turn in the same conversation.

Throwaway exploration. If you're just poking at something to see what's possible, write the prompt directly.

Meta-prompting is for production work. Anything that will produce a PR, a deliverable, or a client artifact.

5. Branch strategy and parallel agents

The biggest source of confusion when running multiple agents is git. Branches collide. PRs stack incorrectly. Work gets lost. Here's how to avoid it.

One PR, one branch, off latest main

Default rule. Every PR branches off main. Every PR merges back to main. Every PR is independent of every other PR.

Advantages: PRs can merge in any order. No coordination required between agents. If one PR fails review, the others are unaffected.

Disadvantages: when two PRs touch the same file, you'll have a merge conflict. The second PR to merge has to rebase.

This is the right default for 80% of work.

Stacked PRs: only when truly necessary

Sometimes a PR depends on another PR. PR B builds on PR A. The naive way to handle this is to branch B off A's branch instead of off main.

PERMANENT RULE FROM A REAL FAILURE

Stacked PRs cause more confusion than they solve. If you must stack, merge bottom-up. Verify the intended base branch before creating each PR. If the base changes between PR creation and merge, verify the retargeting before merging.

Better default: branch each PR off main and accept the rebase cost when there's overlap.

What actually happened on Jamie Stern. PR #3 was opened with PR #2's branch as its base. When merged in the wrong order, PR #3's commits went into PR #2's branch instead of main. PR #2 then merged into main without PR #3's changes. Net effect: PR #3's work was absent from main. The recovery was clean but cost 30 minutes of confused investigation, and required opening PR #6 with the same changes branched off the latest main.

The lesson. If you find yourself stacking PRs because the agents are fast, you've moved past the speed where one director can manage them safely. Slow down. Merge sequentially. Branch independently.

Running multiple agents in parallel

On Jamie Stern I had three agents working at peak: Cloud CC writing image-size fixes, Local CC running the media cleanup analysis script, and Codex producing the seven-task investigation report.

How to do this without breaking things:

Each agent works on a different scope. Cloud CC was editing theme PHP files. Local CC was creating a new tools/ directory. Codex was generating Markdown reports. Zero file overlap.

Each agent works on a different branch. Branch names included the agent that opened them so I could track who shipped what.

Tell each agent what the others are doing. When I sent Local CC the media cleanup prompt while Cloud CC was working on image sizes, the prompt explicitly said: 'Cloud CC may be working on a separate branch (image sizes) at the same time. Do not touch theme files. Stay in tools/ and the report.'

The honest constraint: the director is the bottleneck

During Jamie Stern I asked myself if I could run a fourth or fifth agent. I'd seen people post screenshots of six agents running in parallel. Tempting.

Then I caught myself. The agents weren't the constraint. I was. Every PR they produced needed me to review, decide, merge or revert. Two agents in flight is comfortable for one director. Three starts to feel like air traffic control. Four+ is where today's stacked-PR confusion happens — not because the agents fail, but because the human directing them loses track.

The right number of parallel agents = how many PRs you can fully review in the time the slowest one takes to run.

For most work, that's 2. For documentation tasks where the agent runs longer and the review is faster, you can stretch to 3. Beyond that, you're optimizing for agent throughput at the cost of director judgment, which is the wrong tradeoff.

THE DIRECTOR MODEL IS NOT 'MAXIMUM AGENTS IN PARALLEL.'

It is 'appropriate agents for the work, with the director still able to direct.' If you can't review every PR before deciding to merge it, you're moving too fast. Slow down. The throughput is real but it comes from clean direction, not from agent count.

6. Verification

The throughput in this engagement was real because verification was rigorous. Every change was tested against the running site before merge. Most teams skip this. Don't.

The before-and-after pattern

Before any non-trivial change, capture a baseline. After the change, capture the same set of measurements. If they don't match, you have a problem to investigate before merging.

For Jamie Stern, the baselines I captured at the start:

HTTP status of the homepage, a product page, a category page, a portfolio page, the contact page

Page weight (HTML byte size) of the same set

Number of script tags, stylesheet links, image tags on each

Browser console error count on each

Specific functional tests: Quick View opens, search returns results, footer links work

After each PR, the same measurements. Anything that changed unexpectedly is a flag to investigate.

The valid + invalid pattern

When you add validation, don't only test that the happy path works. Test that the rejection path works too. A nonce check that lets everything through is worse than no nonce check, because you think you're protected.

The pattern I used for the three AJAX endpoints in PR #4:

Send a request with a valid nonce. Confirm 200 and expected response body.

Send the same request with an invalid nonce. Confirm 403 and rejection.

Send malformed input. Confirm validation rejects without PHP warnings.

Check the WordPress debug.log for any errors generated.

Two methodology gotchas

GOTCHA #1: ELEMENTOR TEMPLATE ID IS NOT A PRODUCT ID

When testing Quick View, my first attempt extracted post-27944 from the URL of /product/portal/. The Quick View handler returned 404 because 27944 is the Elementor template that wraps the product page, not the product itself.

Fix: get a real WooCommerce product ID from the shop page, not from a product URL. Re-tested with 28967 (Ganges product). Worked.

GOTCHA #2: REST ROUTES CAN BE METHOD-SPECIFIC

First test of the qv/v1/load-more REST endpoint used GET. Returned rest_no_route. Spent five minutes thinking the route registration was broken.

Fix: read the route registration. It's POST-only. POST works. The lesson is: when a REST endpoint returns rest_no_route, check the method before assuming the route is broken.

A complete verification script (real, from the engagement)

This is the actual PowerShell verification script I used on PR #4 + PR #5 after merging the security batch. The agent ran it against jamie-stern.local and reported back ALL PASS.

SHELL: Windows PowerShell. PowerShell-native commands only.

TASK: Verify PR #4 (security batch) merged on top of PR #5 produces

working Quick View, custom search, and qv-gallery load-more.

CONTEXT

- Both PR #5 and PR #4 are now merged on main.

- Server now requires nonces. JS sends nonces. They must match.

- Action strings:

- Quick View AJAX: 'quick_view_nonce', POST field 'nonce'

- Custom search AJAX: 'custom_search_nonce', POST field 'nonce'

- qv-gallery REST: 'wp_rest', header 'X-WP-Nonce'

- qv-gallery enqueues only on page IDs 16889 and 16890.

DO

1. Pull latest main:

Set-Location "C:\Users\Maxwel\Local Sites\jamie-stern\app\public\wp-content"

git checkout main

git pull

git log --oneline -8

2. Verify site still boots:

$home = Invoke-WebRequest -Uri "https://jamie-stern.local/" `

-SkipCertificateCheck -UseBasicParsing

Write-Host "Homepage: $($home.StatusCode)"

If status is 500 or other error, STOP and recommend revert PR #4.

3. Extract nonces from the localized JS objects:

$homeHtml = $home.Content

$qvNonce = [regex]::Match($homeHtml,

'"quick_view_nonce":"([a-f0-9]+)"').Groups[1].Value

$searchNonce = [regex]::Match($homeHtml,

'"custom_search_nonce":"([a-f0-9]+)"').Groups[1].Value

if (-not $qvNonce -or -not $searchNonce) {

Write-Host "STOP: Required nonces not localized. Investigate."

return

}

4. Find a real product ID for the Quick View test:

$productMatch = [regex]::Match($homeHtml,

'href="(https://jamie-stern\.local/product/[^"]+)"')

$productUrl = $productMatch.Groups[1].Value

$product = Invoke-WebRequest -Uri $productUrl `

-SkipCertificateCheck -UseBasicParsing

$productId = [regex]::Match($product.Content,

'post-(\d+)').Groups[1].Value

5. TEST 1 — Quick View AJAX with valid nonce:

$qvBody = "action=load_product_quick_view&product_id=$productId&nonce=$qvNonce"

$qvResp = Invoke-WebRequest `

-Uri "https://jamie-stern.local/wp-admin/admin-ajax.php" `

-Method POST -Body $qvBody -SkipCertificateCheck `

-UseBasicParsing -ContentType "application/x-www-form-urlencoded"

Expect: HTTP 200, response length > 1000 chars.

6. TEST 2 — Same request with INVALID nonce:

$badBody = "action=load_product_quick_view&product_id=$productId&nonce=invalid123"

# Expect: HTTP 403 OR response body == "0" (WordPress rejection)

7. TEST 3 — qv/v1/load-more REST with X-WP-Nonce header:

$headers = @{ "X-WP-Nonce" = $restNonce }

$restResp = Invoke-WebRequest `

-Uri "https://jamie-stern.local/wp-json/qv/v1/load-more?offset=0&page_id=16889" `

-Method POST -Headers $headers -SkipCertificateCheck -UseBasicParsing

Expect: HTTP 200, JSON response.

8. VERDICT:

- All 3 PASS → security batch fully landed

- 1-2 FAIL → action string mismatch, recommend targeted fix

- All 3 FAIL → systemic problem, recommend revert PR #4

REPORT

- Each test with HTTP code and pass/fail

- Final verdict

- If any failures, name the specific endpoint and likely cause

What this returned. All three tests PASS. Quick View 200, 11.8KB HTML response. Custom search 200, 3.9KB JSON. REST load-more 200, 75.7KB JSON. Invalid nonces all returned 403 with rest_cookie_invalid_nonce. The security batch was fully verified before being relied on.

7. Failure modes you will hit

Six things went wrong during this engagement. All six are now permanent rules in my prompt pack. Three were agent failures. Two were tool routing failures. One was operator failure. The operator failure is the most important one.

Agent failure: unsanctioned git history rewrite

During the initial baseline setup, the agent created an orphan branch and squashed three prior commits into one root commit, unprompted. The code was intact. The history was not. I caught it on review.

What happened: the agent thought the history was 'cleaner' if it started from a single commit. Made a unilateral decision. Did not ask.

PERMANENT RULE

Do not rewrite git history. No squash, rebase, orphan branches, amend, or force push under any circumstances. Forward-only commits only. If you think history should be cleaner, flag it in the deliverable. Do not act on it.

Agent failure: fabricated completion notifications

During a long-running du command (measuring uploads tree size), the agent produced lines that looked like real timestamped completion messages. The command was still running. The notifications were speculative.

Why this is dangerous: the agent didn't fabricate a fact. It fabricated the experience of progress to fill a wait. In a less alert review session it could go undetected.

PERMANENT RULE

Real command output, or 'I cannot verify.' Nothing in between. If a long-running command hasn't returned, say so explicitly. Wait, kill it, or run a faster alternative. Never paraphrase or invent what output would have been.

Tool routing failure: stacked PR base-branch confusion

Already covered in Section 5. PR #3 was created with PR #2's branch as its base. When merged in the wrong order, the changes went into the wrong branch.

PERMANENT RULE

Verify the intended base branch before creating each PR. When stacking PRs, merge bottom-up. If the base changes between PR creation and merge, verify the retargeting before merging.

Tool routing failure: PowerShell vs Git Bash confusion

Local CC sometimes attempted bash-style commands (wc, tail, grep, &&) on Windows PowerShell, producing syntax errors or hanging sessions. The local environment ran Windows 11 with Git Bash available for git operations and PowerShell for everything else.

PERMANENT RULE

Include an explicit shell hint at the top of every prompt. SHELL: Windows PowerShell. PowerShell-native commands only. Use Invoke-WebRequest (not curl). Use Select-String (not grep). Use Set-Location (not cd).

Tool routing failure: cloud sandbox can't reach localhost

Cloud Claude Code's infrastructure can't resolve jamie-stern.local. That hostname only exists on the laptop running Local by Flywheel. The cloud sandbox has its own loopback. Verification prompts sent to Cloud CC return connection errors.

PERMANENT RULE

Code generation goes to Cloud CC. Verification goes to Local CC. These are separate jobs for separate surfaces. Never ask Cloud CC to verify local site behavior.

The 2 a.m. loop — operator failure

From roughly 1:45 to 2:50 a.m. on the first night, the session continued past its stated stopping point. The work was at a clean checkpoint. The fix was a checkbox — confirming a permission setting that was already correct.

Each answer produced one more question. The session ended only when I asked for a handoff document to close on. The document gave my brain the closure it wanted.

This is the meta-lesson and it's the one I want you to take seriously. The agent governance work is only useful if the operator is functional. Fatigue degrades your ability to notice when a loop is closed. The director is the variable, not the agents.

PERMANENT RULE — THE MOST IMPORTANT ONE

When you cannot tell whether you are tired or whether the agent is wrong, you are tired. Park it. The work was at a clean checkpoint when you started doubting. It still is.

8. Prompt library: twelve real prompts

Every prompt in this section was sent during the Jamie Stern engagement. The format is the same throughout: who it was sent to, what it accomplished, and the verbatim text. Adapt these to your context.

Prompt 1: Git baseline staging

SENT TO: Local Claude Code    PURPOSE: Initial commit setup, no code changes

SHELL: Windows PowerShell. PowerShell-native commands only.

TASK: Finalize .gitignore and stage code-only commit.

Append the following entries to wp-content/.gitignore:

# Rotated logs

*.log.gz

__.logs/

# Cache and runtime dirs

__cache/ cache123/ bfu-temp/ wflogs/ updraft/

upgrade-temp-backup/ smush-webp/

# Stray migration artifacts

__wp-cache-config.php autoptimize_404_handler.php

# Media (tracked separately, not in git)

uploads/

After updating .gitignore:

1. Run git status --short and report file count + breakdown

2. Confirm uploads/ is NOT in the staged set

3. Confirm no .sql, .log, .log.gz, or cache directory contents staged

4. Do NOT commit yet. Stop and show me the staging summary.

DO NOT FABRICATE TOOL OUTPUT.

Prompt 2: First push to GitHub

SENT TO: Local Claude Code    PURPOSE: First push of large repo, expected HTTPS issues

SHELL: Git Bash. Unix-style commands work natively.

TASK: Push the wp-content baseline to GitHub.

PRECONDITIONS:

- Empty private GitHub repo exists at:

https://github.com/whitehatforhire/jamie-stern-wp-content.git

- Authenticated to GitHub.

DO:

1. Verify current git state (log, status, remote -v)

2. Add remote: git remote add origin <url>

3. Verify branch name; if master, rename to main: git branch -M main

4. Push and set upstream: git push -u origin main

5. After push: confirm origin set, log oneline, report final commit hash

If push fails with HTTPS transport error (likely on >100MB repos):

- Run: git config http.postBuffer 524288000

- Run: git config http.version HTTP/1.1

- Retry the push

DO NOT force push, push other branches, modify .gitignore,

rewrite history.

IF AUTH FAILS: Stop, report exact error, wait for human resolution.

IF PUSH REJECTED: Stop, do not force push, report rejection reason.

DO NOT FABRICATE TOOL OUTPUT.

Prompt 3: Dead enqueue removal (PR #1)

SENT TO: Cloud Claude Code    PURPOSE: First proof-strike: sitewide 404 fixed

TASK: Fix the missing custom-search.js enqueue.

CONTEXT

- Repo: jamie-stern-wp-content

- File: themes/hello-elementor-child/functions.php

- Issue: around line 1757, enqueues '/custom-search.js' but file doesn't exist.

DO

1. Read functions.php and find the exact enqueue block.

2. Check if the script's logic is actually used elsewhere

3. Choose ONE fix and explain why:

a) Create a stub custom-search.js

b) Remove the enqueue if no dependent code exists

c) Move the enqueue to only fire on pages that need it

4. Implement on branch: bugfix/custom-search-js-404

5. Commit with a clear message

6. Open a PR

DON'T

- Refactor adjacent code, touch other enqueues, push to main, rewrite history.

DO NOT FABRICATE TOOL OUTPUT.

Prompt 4: Asset version fix (PR #2)

SENT TO: Cloud Claude Code    PURPOSE: Restored browser caching

TASK: Replace rand() asset versions with filemtime() in

hello-elementor-child theme.

CONTEXT

- File: themes/hello-elementor-child/functions.php

- Issue: lines 26, 30, 31, 35 pass rand() as asset version parameter.

Defeats browser caching site-wide.

DO

1. Read functions.php and locate the four enqueue lines

2. For each, replace rand() with filemtime() pointed at the asset file

3. Verify each asset path actually exists before referencing

4. Create branch bugfix/asset-versioning-filemtime

5. Commit, open PR

DON'T touch any other enqueue.

DO NOT FABRICATE TOOL OUTPUT.

Prompt 5: Security batch with stop conditions (PR #4)

SENT TO: Cloud Claude Code    PURPOSE: Five security fixes + one investigation

TASK: Ship a batch of six audit fixes as a single PR.

FIXES TO SHIP (each is independent — if uncertain, skip and continue)

1. Remove wp-phpmyadmin-extension from active plugins

(rename folder to .disabled if wp_options not accessible)

2. Add SVG sanitization

(restrict to admin role OR recommend Safe SVG plugin)

3. Add nonce + product validation to load_product_quick_view AJAX

(check_ajax_referer + post_type/post_status validation)

4. Add nonce + min length to custom_search_posts AJAX

(check_ajax_referer + 2-character minimum)

5. Add nonce + input validation to qv/v1/load-more REST route

(wp_verify_nonce on X-WP-Nonce header + args schema)

6. Investigate AI1WM Unlimited Extension version mismatch

(report only, do not implement)

EXECUTION RULES

- Branch: bugfix/audit-batch-security-config

- Commit per fix with clear messages. Six commits expected.

- If uncertain about scope or risk: SKIP IT and document.

- Do not refactor adjacent code.

- Do not rewrite history.

DO NOT FABRICATE TOOL OUTPUT.

Prompt 6: JS counterpart with cross-PR verification (PR #5)

SENT TO: Cloud Claude Code    PURPOSE: JS sends nonces matching PR #4's server-side validation

TASK: Update theme JS to send nonces for the security fixes in PR #4.

CONTEXT

- PR #4 (open, not merged) adds nonce verification to three endpoints

- The calling JS does not currently send these nonces

- This PR is the frontend counterpart that makes PR #4 safe to merge

- Branch off main, NOT off PR #4's branch

DO

1. Read PR #4's body and diff via GitHub API to find:

- Exact nonce action strings used by check_ajax_referer

- Action string used by wp_verify_nonce for REST

- Exact JS file references PR #4 calls out

2. For each endpoint, locate calling JS, localize call, script handle

3. For each endpoint, update JS to read nonce and include in request

STOP CONDITIONS

- Unfamiliar territory (Elementor widget, plugin code): STOP

- Minified/built JS: STOP and document

- Cannot determine exact action string: STOP for that endpoint

DO NOT fabricate action strings if you can't find matching

server-side strings.

DO NOT FABRICATE TOOL OUTPUT.

DO NOT REWRITE GIT HISTORY.

What the agent did. Fetched PR #4's diff via GitHub API to verify exact action strings before writing JS. Zero guessing. The nonce coupling held perfectly through verification.

Prompt 7: Image sizes refactor (PR #7)

SENT TO: Cloud Claude Code    PURPOSE: Replace full-size images with responsive sizes

TASK: Replace 'full' image rendering with responsive WordPress

image sizes in hello-elementor-child theme.

CONTEXT

- Active theme: themes/hello-elementor-child/

- Recent merged work to coordinate with:

- PR #1: removed dead custom-search.js enqueue

- PR #2: rand() -> filemtime() asset versions

- PR #6: scoped single-product-css/js into shortcode callbacks

- PR #4 + #5: nonce/validation guards on AJAX/REST endpoints

- This PR should NOT touch enqueue logic, asset versioning, or

AJAX/REST handlers. Stay in image rendering only.

DO

1. Find all 'full' image usages in child-theme PHP files:

grep -rn "the_post_thumbnail('full')" themes/hello-elementor-child/

grep -rn "the_post_thumbnail_url('full')" themes/hello-elementor-child/

grep -rn "wp_get_attachment_image.*'full'" themes/hello-elementor-child/

2. For each occurrence, classify the context:

- Product/category cards: 'woocommerce_thumbnail' or 'medium_large'

- Product gallery main image: 'woocommerce_single' or 'large'

- Blog cards/search results: 'medium_large'

- Portfolio sliders: 'large'

3. Where you find raw <img src> markup using full URLs,

prefer wp_get_attachment_image() to emit srcset, sizes, width,

height, loading, decoding. Preserve existing CSS classes.

STOP CONDITIONS

- 'full' usage in commented-out code: leave it alone, report it

- Size choice not obvious from context: STOP for that one

- Hero image that genuinely needs full-resolution: leave, document

DO NOT

- Touch enqueue/version logic (PR #1, #2, #6 already shipped)

- Touch AJAX/REST handlers (PR #4, #5 already shipped)

- Refactor surrounding code

DO NOT FABRICATE TOOL OUTPUT.

Prompt 8: Strategy-first performance refactor (PR #8)

SENT TO: Cloud Claude Code    PURPOSE: Required strategy step before any code changes

TASK: Optimize qv-gallery and custom search AJAX/REST performance

without changing frontend behavior.

CONTEXT

- Recent merged work to NOT undo: PR #4 nonces, PR #5 JS, PR #7 images

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

- If -1 query has bounded result set: leave, document

- If transient invalidation requires plugin code: STOP and document

DO NOT FABRICATE TOOL OUTPUT.

What the agent did. Produced a five-finding strategy table before any code changes. Found that wp_cache_* was request-scoped (no-op without persistent backend) before implementing. Five commits, clean.

Prompt 9: Read-only analysis script (PR #9)

SENT TO: Local Claude Code    PURPOSE: Generate analysis without making changes

TASK: Create a media cleanup analysis script and report.

REPORT-ONLY. Do not delete, move, rename, or modify any uploads.

CONTEXT

- Uploads at: C:\Users\Maxwel\Local Sites\jamie-stern\app\public\wp-content\uploads

- Output: tools/media-cleanup-analysis.ps1 + MEDIA_CLEANUP_REPORT.md

- Cloud CC may be working on a separate branch (image sizes) at the

same time. Do not touch theme files. Stay in tools/ and the report.

SHELL: Windows PowerShell.

DO

1. Create tools/media-cleanup-analysis.ps1 that scans uploads:

- Total file count and total size in GB

- Top 50 largest files

- Total size of uploads/backup/ if it exists

- Total size of uploads/wpmc-trash/ if it exists

- Count of generated image derivatives (-<width>x<height> pattern)

- Count of files by extension with total size

- Risky extensions: .zip, .psd, .sql, .log, .php, .bak

2. Output Markdown to MEDIA_CLEANUP_REPORT.md including:

- Summary stats

- Each finding as its own section with tables

- "Candidate cleanup commands" section with EXACT commands

to remove backup/trash dirs, but COMMENTED OUT and prefixed

with "# REQUIRES HUMAN APPROVAL — DO NOT RUN BLINDLY"

DO NOT

- Delete, move, rename, or modify any file under uploads/

- Run any of the candidate cleanup commands

- Touch theme files, plugins, or wp-config

DO NOT FABRICATE TOOL OUTPUT.

Prompt 10: Theme removal with safety checks (PR #12)

SENT TO: Local Claude Code    PURPOSE: Delete inactive theme — 51 MB, 2,093 files

TASK: Remove inactive Salient theme directory from the repo.

CONTEXT

- Active theme: hello-elementor-child (confirmed)

- Inactive theme to remove: themes/salient/

- Investigation found 51.89 MB, 2,093 files

- Salient bundled plugins also at themes/salient/_bundled/

PRE-DELETION SAFETY CHECKS (DO ALL OF THESE FIRST):

1. Confirm hello-elementor-child is active in wp_options:

grep -rn "stylesheet" wp-config.php (should not find override)

2. Confirm zero references to Salient shortcodes in active theme PHP:

grep -rn "salient_" themes/hello-elementor-child/

grep -rn "nectar_" themes/hello-elementor-child/

Both should return zero matches.

3. Report sizes before deletion:

Get-ChildItem themes/salient -Recurse | Measure-Object Length -Sum

4. ONLY THEN proceed to deletion.

IF ANY SAFETY CHECK FAILS: STOP. Report findings. Do not delete.

DO

1. Run all safety checks above. Report results.

2. If all checks pass, git rm -r themes/salient/

3. Commit on branch chore/remove-salient-theme

4. Open PR with safety check output in description

DO NOT delete anything if any safety check returns unexpected output.

DO NOT REWRITE GIT HISTORY.

Prompt 11: Multi-task investigation report (PR #11)

SENT TO: Codex    PURPOSE: Synthesis task: 7-task deep dive into investigation findings

TASK: Produce an investigation report covering seven outstanding

research items from the Jamie Stern audit. Output as

INVESTIGATION_REPORT.md committed to the repo.

CONTEXT

- This is research output, not code. Branch: docs/investigation-report

- All seven tasks below need analysis. Some are read-only audits,

some produce findings + recommendations, none should make code changes.

THE SEVEN TASKS

1. Salient theme database cleanup

- File deletion shipped in PR #12. Database rows remain.

- Find: SELECT option_name FROM wp_options WHERE option_name

LIKE 'salient%' OR option_name LIKE 'theme_mods_salient%'

- Recommend: WP-CLI command sequence for Sam's team to clean.

2. Cron reschedule errors

- debug.log shows 9 cron reschedule errors for missing schedules

- Identify which plugins register them, recommend fixes

3. Encoding damage in theme files

- Investigation prompt: any mojibake or invalid UTF-8 sequences

- Hex-dump suspect bytes before claiming damage exists

4. Robots.txt and sitemap audit

- Verify robots.txt allows production crawling

- Verify sitemap_index.xml is accessible and valid

5. Product gallery HTML weight analysis

- 55 cached pages: which Elementor template IDs appear

- Count img tags per page across category, product, portfolio

6. Elementor and Wordfence fatal stack traces

- uploads/wc-logs/fatal-errors-*.log has prior production fatals

- Document the stack traces, recommend verification on staging

7. Plugin ownership matrix

- 40 active plugins. Categorize by:

- Risk level (security exposure, attack surface)

- Necessity (required, useful, optional, deactivation candidate)

- Owner (theme dep, plugin dep, ecommerce, marketing)

- Output as a Markdown table

DELIVERABLE

- INVESTIGATION_REPORT.md with each task as its own section

- Each section: Findings / Recommendations / Owner action required

DO NOT make any code changes. Research and documentation only.

Prompt 12: Final cleanup batch (PR #20)

SENT TO: Cloud Claude Code    PURPOSE: Three-item batch with per-item stop conditions

TASK: Three-item batch — CF7 conditional enqueue, Lenis scope,

shortcode extraction.

CONTEXT

- functions.php is currently around 1,800 lines after PRs #10, #16

- Continue the monolith refactor with one more slice

- Branch: feature/perf-batch-cf7-lenis-shortcodes

ITEM 1: Contact Form 7 conditional enqueue

- Currently CF7 assets load on every page

- Make conditional on: shortcode present OR Elementor CF7 widget present

- If conditional logic gets complex, leave it global and document

ITEM 2: Lenis smooth scroll scoping

- Currently Lenis loads globally

- Disable on cart, checkout, my-account (interferes with form interactions)

- If Lenis is initialized in a minified file, STOP and document

ITEM 3: Shortcode callbacks extraction

- Move shortcode register_callback code from functions.php

to includes/shortcodes.php

- This is extraction, not refactoring. Do not change any logic

inside the extracted functions.

STOP CONDITIONS PER ITEM

- Item 1: complex conditional → leave global, document

- Item 2: minified Lenis init → STOP, document, do not edit built file

- Item 3: shortcode registers depend on theme constants → flag, ask

DELIVERABLE

- One PR with three commits, one per item

- PR description must list:

- functions.php line count before/after

- Which items shipped, which items skipped (and why)

DO NOT FABRICATE TOOL OUTPUT.

DO NOT REWRITE GIT HISTORY.

9. The prompt pack

These are the rules I append to every prompt. Steal them. Modify them. Add your own as you hit your own failure modes.

Permanent rules (every prompt)

Do not rewrite git history. No squash, rebase, orphan branches, amend, or force push. Linear forward commits only.

Do not fabricate tool output. If a long-running command hasn't returned, say so. Never paraphrase or invent.

Verify the current branch and intended base branch before creating or updating a PR.

When stacking PRs, state the stack order and merge bottom-up.

Never claim future notifications, async follow-ups, or monitoring unless the current tool surface can actually perform them.

Do not make production deploys unless the prompt explicitly says deploy.

Routing rules

Code generation against a GitHub repo: Cloud Claude Code.

Verification against a running local site: Local Claude Code.

Triage, audit reports, prompt packs, decision matrices: Codex.

Do not ask Cloud Claude Code to verify local-only URLs or browser behavior.

Route security and performance refactors through a strategy step before assigning implementation.

Strategy-before-implementation template

For any change that touches more than one file or could affect performance, security, or data integrity, require a strategy step before code is written.

## Strategy Before Implementation

### Observed Problem

[Concrete symptoms, files, counts, timings, logs, examples]

### Candidate Fixes

| Option | Files touched | Risk | Expected impact | Verification |

| --- | --- | --- | --- | --- |

| A | [paths] | Low/Medium/High | [impact] | [commands] |

| B | [paths] | Low/Medium/High | [impact] | [commands] |

### Recommended Path

[Choose the smallest path that creates meaningful improvement]

### Stop Conditions

[List what would make the agent stop before editing]

### Implementation Boundary

[Name the files or modules the agent is allowed to touch]

Verification template

1. Load the page and extract any localized values (nonces, IDs)

2. Send the request with valid input. Confirm 200 + expected body.

3. Send the same request with INVALID input. Confirm rejection.

4. Send malformed input. Confirm validation handles cleanly.

5. Check debug.log and PHP error log for warnings.

6. Test on at least 2 different page types where the feature appears.

7. Capture before/after for any performance metric being claimed.

Standard prompt header (PowerShell environments)

SHELL: Windows PowerShell. PowerShell-native commands only.

Use Invoke-WebRequest (not curl). Use Select-String (not grep).

Use Set-Location (not cd).

DO NOT FABRICATE TOOL OUTPUT.

DO NOT REWRITE GIT HISTORY.

If you hit unfamiliar territory, STOP and document.

If a stop condition fires, STOP and report.

PowerShell SSL bypass for Local environments

Local by Flywheel sites use self-signed certificates. PowerShell 5.1 doesn't have -SkipCertificateCheck on Invoke-WebRequest. This snippet enables HTTPS calls to https://your-site.local in older PowerShell.

Add-Type @"

using System.Net;

using System.Security.Cryptography.X509Certificates;

public class TrustAllCerts : ICertificatePolicy {

public bool CheckValidationResult(ServicePoint sp, X509Certificate cert,

WebRequest req, int problem) { return true; }

}

"@

[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCerts

[System.Net.ServicePointManager]::SecurityProtocol =

[System.Net.SecurityProtocolType]::Tls12

10. What your team can do tomorrow

You don't need to overhaul anything. There are three things your team can adopt this week that would change how your engineering work feels.

1. Adopt the verification pattern, regardless of agents

The verification pattern is just good engineering. Every change verified against the running site. Valid input AND invalid input. Before/after measurements. Console errors checked. Debug log checked. This catches issues that human review misses, and it's the same discipline whether the change came from a human, an agent, or a vendor patch.

Make this the standard for every PR your team merges. The cost is 10 minutes per PR. The benefit is fewer production fires.

2. Set up Local Claude Code on one developer's machine

Pick your most curious developer. Install Claude Code locally. Have them try the verification pattern on their next PR — not to write the code, just to verify someone else's PR more rigorously than they normally would. Time how long it takes. See what they catch that they would have missed.

That is the entry-level use case for agents. Verification, not generation. Lower stakes, faster feedback, easier to learn the prompt structure.

3. Run the staging verification script before every deploy

tools/staging-verification.sh is in the repo. It's 25+ checks via WP-CLI that run in about 90 seconds. WP_DEBUG, WP_CACHE, plugin health, cron, encoding, nonce-protected endpoints. The next time someone on your team is about to deploy, run it first.

If the output has any FAIL lines, hold the deploy. If it has WARN lines, document them. If it's all PASS, deploy with confidence. This costs you 90 seconds and prevents a category of small fires.

Going deeper

If your team wants to pilot agentic workflows on a contained scope, I'm available. Start small. One PR. One feature. One refactor. See how it lands. Iterate from there.

The throughput is real. The verification is non-negotiable. The director is the variable. Everything else follows.

Repository reference. Everything from this engagement is in WhiteHatForHire/jamie-stern-wp-content. PR #15 contains the full case study and the Prompt Pack v3 in markdown form. PR #14 is the staging verification script. PR #19 is the smoke test suite.

Tools mentioned in this guide. Cloud Claude Code (claude.ai/code). Local Claude Code (Anthropic desktop app or npm CLI). Codex (OpenAI). Local by Flywheel (free, localwp.com). All-in-One WP Migration (WordPress plugin).

Maxwell

Eagle Rocket LLC  •  WhiteHatForHire

Written for Sam, May 2026
