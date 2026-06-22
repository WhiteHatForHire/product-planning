---
title: "SYMPOSIUM STUDIOS V0 BUILD DIRECTIVE"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/Websites/Symposiumstudios.ai/SYMPOSIUM_STUDIOS_V0_BUILD_DIRECTIVE.md"
status: active
privacy: working
tags:
  - website
---

# SYMPOSIUM STUDIOS V0 BUILD DIRECTIVE

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# SYMPOSIUM_STUDIOS_V0_BUILD_DIRECTIVE.md

Autonomous build directive for symposiumstudios.ai V0.

Fire at Claude Code (Opus recommended) with this file and
SYMPOSIUM_STUDIOS_V0_COPY_LOCKED.md in the working directory.

---

```
ROLE
You are building the V0 of symposiumstudios.ai as an autonomous engineer
working under the AUTONOMY_LAYER protocol (v1.2). Marcus Vale is the
director. You will open a PR for review when the build is complete.
Do not configure production domain, DNS, or SSL. Do not merge.

REPOSITORY
Use the existing blank GitHub repo:
https://github.com/WhiteHatForHire/symposium-studios

Clone this repo. Create the Astro project inside it. Commit to a feature
branch. Push to origin. Open a PR. Do not create a new repository.

SOURCE OF TRUTH
SYMPOSIUM_STUDIOS_V0_COPY_LOCKED.md is the canonical source of all public
copy strings. Do not invent or rewrite any public copy. If a required
string is not in that file, block and report.

CONTEXT
Symposium Studios is a senior-led software studio founded by Marcus Vale.
The public lane is LLM-integrated apps, interactive LLM systems, founder
prototypes, internal tools, product MVPs, and serious custom software.
The site should feel like an architecture firm or fashion-house workshop,
not an AI hype agency.

CRITICAL POSITIONING RULES
Banned terms (verifier must fail the build if any appear in rendered output):
- AI-native
- AI-powered
- agentic
- Director Model
- Council of Models
- model councils

Banned protected names (verifier must fail the build if any appear):
- Phronetics
- Arbiter
- Propylaea
- DreamMirror

AI and LLM are allowed where they describe actual product capability or
development method, as they appear in the locked copy doc. They are not
allowed as empty hype or generic automation-agency copy.

STACK
- Astro with Tailwind CSS (preferred)
- Deploy target: Vercel (connected post-merge, not in this directive)
- Domain: symposiumstudios.ai (wired post-merge, not in this directive)
- No CMS, no analytics, no third-party scripts in V0

PAGE STRUCTURE (single page, top to bottom, exactly these eight sections)
1. Hero
2. What we build
3. How we work
4. Proof
5. Engagements
6. How the studio operates
7. Contact
8. Footer

NAVIGATION
Minimal top nav with three anchor links:
- Work (scrolls to #what-we-build)
- Services (scrolls to #engagements)
- Contact (scrolls to #contact)

DESIGN TOKENS
- Background: warm ivory (#F7F3EC or close)
- Text: near-black (#171513)
- Accent: muted gold (#A8884B) or stone (#7A7164), used sparingly
- Heading font: Inter Display or Söhne if licensed
- Body font: Inter or IBM Plex Sans
- Max content width: ~960px
- Generous vertical rhythm (1.6+ line height)
- Optional single classical motif (meander or column fragment), used once

ASSETS
The following asset files will be present in the working directory before
the build is fired. Do not download, generate, or substitute these files.

1. symposiumstudios-favicon.svg
   Copy verbatim to: /public/favicon.svg
   This is the final SVG favicon. Do not modify it.

2. og-image.png
   Copy verbatim to: /public/og-image.png
   This is the final 1200x630 OG image. Do not generate or substitute it.
   If og-image.png is not present in the working directory, block and
   report before proceeding.

META TAGS (add to <head> in the base layout, verbatim)

Title:
<title>Symposium Studios</title>

Favicon:
<link rel="icon" type="image/svg+xml" href="/favicon.svg">

Open Graph:
<meta property="og:type" content="website">
<meta property="og:url" content="https://symposiumstudios.ai">
<meta property="og:title" content="Symposium Studios">
<meta property="og:description" content="Senior-led development for prototypes, product systems, and LLM-integrated applications.">
<meta property="og:image" content="https://symposiumstudios.ai/og-image.png">

Twitter / X:
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Symposium Studios">
<meta name="twitter:description" content="Senior-led development for prototypes, product systems, and LLM-integrated applications.">
<meta name="twitter:image" content="https://symposiumstudios.ai/og-image.png">

STRICT RULES
- Pull every public copy string verbatim from the locked copy doc
- No em dashes anywhere in copy
- "We" only as the studio operating system, not faking headcount
- No gradient hero, no stock imagery, no AI-generated art
- No people photographs, no client logos
- No prices, no newsletter signup, no booking widget
- All external links open in new tabs
- mailto: links for the contact email

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

PRE-FLIGHT (before writing any code)
1. Clone https://github.com/WhiteHatForHire/symposium-studios
2. Create a feature branch (e.g. feature/v0-build)
3. Confirm AUTONOMY_LAYER.md is present or create it
4. Read SYMPOSIUM_STUDIOS_V0_COPY_LOCKED.md fully
5. Confirm every section in PAGE STRUCTURE has corresponding locked copy
6. If any copy is missing, block and report before writing code

BUILD STEPS
1. Initialize Astro project in the repo root (not in a subfolder)
2. Configure Tailwind with the design tokens above
3. Build the eight sections in order, pulling copy verbatim from the locked file
4. Verify mobile reflow at 375px width
5. Run Lighthouse and confirm accessibility score above 95
6. Run the full verifier checklist below
7. Commit all changes to the feature branch
8. Push to origin
9. Open a PR with: build summary, verifier checklist results, and preview URL
   if Vercel preview is available

VERIFIER CHECKLIST (all must pass before opening PR)
1. No banned terms in rendered output:
   AI-native, AI-powered, agentic, Director Model, Council of Models,
   model councils
2. No protected names in rendered output:
   Phronetics, Arbiter, Propylaea, DreamMirror
3. AI and LLM appear only where they describe real product capability
   or development method (as placed in the locked copy doc)
4. No em dashes anywhere
5. No "vibes" anywhere
6. No exclamation points anywhere
7. No people photographs, stock imagery, or AI-generated art
8. Contact email marcus@symposiumstudios.ai resolves correctly in mailto
9. Cross-link to https://marcus-vale.com opens in a new tab
10. Mobile reflow clean at 375px
11. Lighthouse accessibility score above 95
12. No console errors

OUT OF SCOPE FOR V0
- Multi-page architecture
- Case study pages
- Pricing
- Client portal or booking widget
- Analytics or CMS
- About page (operator background is in the Proof section)
- Any Vercel production domain configuration
- Any feature not in the locked copy doc

SUCCESS CRITERIA
A reviewer landing on the preview URL should, within 60 seconds, understand:
1. Symposium Studios builds LLM-integrated apps, interactive systems,
   prototypes, internal tools, and product MVPs.
2. The studio operates with senior technical direction and disciplined delivery.
3. Anchor is live proof of building serious software under review.
4. Marcus Vale leads the studio with eight years of agency experience.
5. There is a clear path to start a conversation.

END OF DIRECTIVE
```
