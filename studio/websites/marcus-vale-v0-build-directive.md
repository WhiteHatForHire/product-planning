---
title: "MARCUS VALE V0 BUILD DIRECTIVE"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/Websites/marcus-vale.com/MARCUS_VALE_V0_BUILD_DIRECTIVE.md"
status: active
privacy: private/internal
tags:
  - website
---

# MARCUS VALE V0 BUILD DIRECTIVE

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# MARCUS_VALE_V0_BUILD_DIRECTIVE.md

Autonomous build directive for marcus-vale.com V0.

Fire at Claude Code (Opus recommended) with this file and
MARCUS_VALE_V0_COPY_LOCKED.md in the working directory.

---

```
ROLE
You are building the V0 of marcus-vale.com as an autonomous engineer
working under the AUTONOMY_LAYER protocol (v1.2). Marcus Vale is the
director. You will open a PR for review when the build is complete.
Do not configure production domain, DNS, or SSL. Do not merge.

REPOSITORY
Use the existing blank GitHub repo:
https://github.com/WhiteHatForHire/marcus-vale-site

Clone this repo. Create the Astro project inside it. Commit to a feature
branch. Push to origin. Open a PR. Do not create a new repository.

SOURCE OF TRUTH
MARCUS_VALE_V0_COPY_LOCKED.md is the canonical source of all public copy
strings. Do not invent or rewrite any public copy. Do not invent URLs,
pull quotes, or dates. See PENDING ITEMS below for scaffold instructions.

CONTEXT
marcus-vale.com is the public thesis site for Marcus Vale, a writer and
systems thinker on AI-native systems and human judgment. It is not an
agency site. It is not a SaaS landing page. It should feel like a private
library with the door open: restrained, literary, editorial.

This site is allowed to use the explicit theory vocabulary:
AI-native systems, Director Model, Council of Models, Pattern Intimacy,
AI Self-Governance, Minimum Viable Organization, Aristotle and phronesis,
the changing unit of work. The locked copy doc places these terms.

STACK
- Astro with Tailwind CSS (preferred)
- Deploy target: Vercel (connected post-merge, not in this directive)
- Domain: marcus-vale.com (wired post-merge, not in this directive)
- No CMS, no analytics, no third-party scripts in V0

PAGE STRUCTURE (single page, top to bottom, exactly these six sections)
1. Hero
2. Featured essay
3. Songs, Books, Systems (three labeled domain cards)
4. Concepts (named concept index)
5. About
6. Footer

NAVIGATION
V0: no top navigation. Page reads top to bottom.

DESIGN TOKENS
- Background: warm ivory (#F7F3EC or close)
- Text: near-black (#171513)
- Accent: muted gold (#A8884B) or stone (#7A7164), used sparingly
- Heading font: Cormorant Garamond or EB Garamond (literary serif)
- Body font: Inter or IBM Plex Sans
- Max content width: ~720px (narrower than Symposium for a literary feel)
- Generous vertical rhythm (1.7+ line height)
- Optional single classical motif (meander, fragment, or small ornament),
  used once

DOMAIN CARD WEIGHTING
SYSTEMS card: largest, active, with four linked concept labels beneath it
(Director Model, Council of Models, Pattern Intimacy, AI Self-Governance).
BOOKS card: smaller, quieter.
SONGS card: smallest, quietest.
For Tech Week, SYSTEMS should clearly lead visually.

ASSETS
The following asset files will be present in the working directory before
the build is fired. Do not download, generate, or substitute these files.

1. marcus-vale-favicon.svg
   Copy verbatim to: /public/favicon.svg
   This is the final SVG favicon. Do not modify it.

2. og-image.png
   Copy verbatim to: /public/og-image.png
   This is the final 1200x630 OG image. Do not generate or substitute it.
   If og-image.png is not present in the working directory, block and
   report before proceeding.

META TAGS (add to <head> in the base layout, verbatim)

Title:
<title>Marcus Vale</title>

Favicon:
<link rel="icon" type="image/svg+xml" href="/favicon.svg">

Open Graph:
<meta property="og:type" content="website">
<meta property="og:url" content="https://marcus-vale.com">
<meta property="og:title" content="Marcus Vale">
<meta property="og:description" content="Essays and field notes on how AI changes work, judgment, software, and the size of the team required to build serious things.">
<meta property="og:image" content="https://marcus-vale.com/og-image.png">

Twitter / X:
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Marcus Vale">
<meta name="twitter:description" content="Essays and field notes on how AI changes work, judgment, software, and the size of the team required to build serious things.">
<meta name="twitter:image" content="https://marcus-vale.com/og-image.png">

STRICT RULES
- Pull every public copy string verbatim from the locked copy doc
- No em dashes anywhere in copy
- No "we" pronoun (single-author voice; use "his work" or "Marcus")
- No buzzwords: leverage, unlock, transform, 10x, AI-powered
- No gradient hero, no SaaS-style feature icons
- No hero photograph
- No newsletter pop-ups (Substack handles subscription externally)
- All external links open in new tabs
- mailto: links for the contact email if present in footer

AUTONOMY_LAYER
- Before implementation, confirm AUTONOMY_LAYER.md is present in the repo root.
- If it is not present, create it from the provided site-build autonomy
  protocol before proceeding. Do not proceed without it.
- Standard branch protocol: feature branch, PR, no direct main commits.
- Standard review gate: PR review by Marcus before merge to main.
- If you encounter ambiguity in copy or structure, default to the locked
  copy doc. If the locked copy doc does not resolve it, block and report.
  Do not invent.

DEPLOYMENT POSTURE
- Build and verify locally.
- Push feature branch to origin.
- Open a PR summarizing the build and verifier results.
- If Vercel is already connected to the repo, include the preview URL in the PR.
- Do not configure the production domain, DNS, or SSL inside this directive.
- Production domain wiring is a separate post-merge step authorized by Marcus.

PENDING ITEMS AND SCAFFOLD PERMISSION
The locked copy doc has four unresolved items in the Featured Essay section:
1. Essay post URL for "Solo, But Not Alone"
2. Pull quote from the essay
3. Publication date
4. Songs card project-name decision

Build may proceed with the layout and all non-pending copy.

For PENDING items, insert clearly visible placeholder text in the component
so Marcus can see exactly what needs filling. Use this format:
- [ESSAY URL PENDING]
- [PULL QUOTE PENDING]
- [DATE PENDING]
- [SONGS PROJECT NAME PENDING, OR LEAVE GENERIC]

Do not invent any of these strings. Do not deploy to production until all
four pending items are confirmed by Marcus and filled in the locked copy doc.

PRE-FLIGHT (before writing any code)
1. Clone https://github.com/WhiteHatForHire/marcus-vale-site
2. Create a feature branch (e.g. feature/v0-build)
3. Confirm AUTONOMY_LAYER.md is present or create it
4. Read MARCUS_VALE_V0_COPY_LOCKED.md fully
5. Note the four PENDING items; confirm all other copy is present
6. If any non-pending copy is missing, block and report before writing code

BUILD STEPS
1. Initialize Astro project in the repo root (not in a subfolder)
2. Configure Tailwind with the design tokens above
3. Build the six sections in order, pulling copy verbatim from the locked file
4. Insert PENDING placeholders for the four unresolved essay items
5. Verify SYSTEMS card is visually dominant; BOOKS and SONGS are quieter
6. Verify mobile reflow at 375px width
7. Run Lighthouse and confirm accessibility score above 95
8. Run the full verifier checklist below
9. Commit all changes to the feature branch
10. Push to origin
11. Open a PR with: build summary, verifier checklist results, list of
    PENDING placeholders still active, and preview URL if Vercel preview
    is available

VERIFIER CHECKLIST (all must pass before opening PR)
1. No em dashes anywhere in rendered output
2. No buzzwords: leverage, unlock, transform, 10x, AI-powered
3. No "we" pronoun anywhere
4. No exclamation points
5. No hero photograph
6. No newsletter pop-up
7. No stock imagery, no AI-generated art
8. Substack link in footer resolves to https://marcusvalewrites.substack.com
9. Footer cross-link to https://symposiumstudios.ai opens in a new tab
10. Contact email marcus@symposiumstudios.ai resolves correctly in mailto
11. Mobile reflow clean at 375px
12. Lighthouse accessibility score above 95
13. No console errors
14. All PENDING placeholders are visually distinct and clearly labeled

OUT OF SCOPE FOR V0
- Multi-page architecture
- Concept detail pages
- Essay archive or native blog
- Books or Songs dedicated pages
- Contact form
- Newsletter signup form (Substack handles this externally)
- Analytics or CMS
- Hero photograph
- Any Vercel production domain configuration
- Any feature not in the locked copy doc

SUCCESS CRITERIA
A reviewer landing on the preview URL should, within 60 seconds, understand:
1. Marcus Vale writes about AI-native systems, human judgment, and the craft
   of directing intelligent machines.
2. There is a flagship essay worth reading (Solo, But Not Alone).
3. There is a coherent named vocabulary behind the work.
4. There is a sister property called Symposium Studios.
5. This is a serious, restrained voice. Not a guru. Not a hype merchant.

END OF DIRECTIVE
```
