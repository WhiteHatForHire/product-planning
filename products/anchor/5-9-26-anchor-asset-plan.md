---
title: "5 9 26 Anchor Asset Plan"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Assets/Marketing Assets/5_9_26 Anchor Asset Plan.docx"
status: reference
privacy: public-candidate
tags:
  - product
---

# 5 9 26 Anchor Asset Plan

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Asset Plan

Recovery. Clarity. Momentum.

Last updated: May 9, 2026. No icon system exists yet. Items 3–5 are blocked on the app icon.

Priority order

Do now — agentically

Recovery loop / product flow diagram

Trust and safety model diagram

Next — dedicated design session 3. App icon system 4. OG / social share image 5. Email header

After desktop redesign stabilizes 6. Screenshot board / UI collage 7. Loading / splash screen 8. Empty state illustrations

Later 9. App store screenshot pack 10. Landing page hero illustration / animation

Do now — agentically

1. Recovery loop / product flow diagram

A user-facing systems map explaining how Anchor works end-to-end. Not a technical diagram — a human-readable product story.

Show:

Open app → daily check-in → AI reflection

Risk and support identification

Continue into coach chat

Memory updates over time

Reminders and weekly summaries

Insights and history reveal patterns

User controls: memory edit, export, reset

Purpose: explains product value clearly. Useful for case study, founder content, landing page support, and onboarding explainer.

How to make: agentically via Claude visualizer as SVG. No design dependencies. Dark background, recovery-appropriate color palette, clean flow arrows. No clinical language.

Where it lives: exported as SVG or PNG. Used in case study doc and landing page. Not a repo asset — lives in marketing materials.

2. Trust and safety model diagram

A systems map showing how Anchor handles AI and recovery responsibly. Critical for a recovery AI product.

Show:

User check-in → risk classification → crisis-safe handling

AI reflection boundaries — no clinical claims, no diagnosis

Human support always encouraged

User-owned memory with export and reset controls

No autonomous clinical or medical authority

Purpose: responsible AI positioning, trust and safety communication, fCTO portfolio and case study credibility, future public explanation of design choices.

How to make: agentically via Claude visualizer as SVG. No design dependencies. Diagram style, not marketing style.

Where it lives: case study doc, docs/ folder in repo, future landing page trust section.

Dedicated design session

3. App icon system

Highest-priority branded asset. Do not start items 4 or 5 until the icon exists. Should be done intentionally in a focused creative session, not rushed.

Deliverables:

Primary square app icon (1024x1024 source)

Favicon: 16px, 32px, 48px

Apple touch icon: 180x180

PWA manifest icons: 192x192, 512x512

Simple dark-background wordmark / icon lockup (horizontal)

Purpose: browser tab, PWA install, mobile home screen, email branding, social identity, future app store listing.

How to make: Figma. Start with the anchor mark concept — restrained, not nautical-clipart. Dark background, single accent color. Export all sizes from one source file. Drop favicon into artifacts/recovery-checkin/public/. Update index.html and manifest.json.

Where it lives: artifacts/recovery-checkin/public/ for web assets. Source files archived outside repo.

4. OG / social share image

One polished preview image for when sobrietyanchor.com gets shared anywhere.

Deliverables:

Open Graph image: 1200x630

Social card variant if needed: 1080x1080 for Instagram / LinkedIn

Suggested copy: Anchor — Daily recovery check-ins, AI reflection, and support nudges.

Purpose: iMessage previews, Slack unfurl, X/Twitter card, LinkedIn post, WhatsApp link, case study links.

How to make: Figma. Dark background, wordmark, one-line positioning statement, subtle abstract visual. No UI screenshots at this stage. Export as PNG. Add <meta property="og:image"> to artifacts/recovery-checkin/index.html. Host in /public/.

Where it lives: artifacts/recovery-checkin/public/og-image.png. Meta tag in index.html.

5. Email header

Branded header for all Resend transactional emails. Currently emails are unbranded.

Deliverables:

Daily reminder email header — 600px wide, ~120px tall

Weekly summary email header — same dimensions, slight variation if needed

Minimal Anchor icon + wordmark treatment

Purpose: makes transactional emails feel like a real product, improves trust, creates visual consistency outside the app.

How to make: Figma. Export at 2x (1200px wide source). Host on a stable public URL or embed as base64 in the email template. Wire into email templates in artifacts/api-server/src/. Requires icon from item 3 first.

Where it lives: hosted image URL referenced in email template strings in the api-server.

After desktop redesign stabilizes

6. Screenshot board / UI collage

A polished wide image showing all product surfaces together. Do not make this before the desktop redesign is done — it will need to be redone.

Include: Home, Check-in, Chat, History detail, Insights, Memory/Settings.

Purpose: hero case-study asset, landing page visual, founder/product announcement image, "what is Anchor?" explainer.

How to make: high-resolution browser screenshots at 1440px after desktop redesign is stable. Compose in Figma with subtle depth. Real product screenshots, not mockups.

Where it lives: marketing materials, case study doc, landing page. Not a repo asset.

7. Loading / splash screen

Create once the icon system and core visual direction are set. Requires item 3.

Purpose: app initialization, PWA launch, auth/session loading states.

Feel: calm, minimal, serious. Not gamified. The anchor mark fading in on a dark background is sufficient.

How to make: CSS keyframe animation in artifacts/recovery-checkin/src/. Wire into the app shell before the router mounts.

Where it lives: artifacts/recovery-checkin/src/components/SplashScreen.tsx — rendered conditionally during initial auth check.

8. Empty state illustrations

Only after core UI layouts are stable.

Possible empty states: no check-ins yet, no tracker data yet, no insights yet, no memory patterns yet, no chat history yet.

Keep them subtle. Copy may matter more than illustration at this stage. A single well-written sentence often beats a graphic.

How to make: inline SVG or simple CSS. Minimal, not decorative. Wire into each page's empty branch in the existing conditional render logic.

Where it lives: shared EmptyState component in artifacts/recovery-checkin/src/components/ or inline in each page.

Later

9. App store screenshot pack

Only when preparing native wrapper, PWA listing, or real store distribution. Do not make before the UI is stable.

Deliverables:

iPhone screenshots: 6.7" and 6.1" at minimum

Android screenshot set

Annotated store-ready panels with short benefit captions

App preview video if required by store

How to make: Playwright screenshots at standard device dimensions, composed in Figma with caption overlays. Requires icon system and final stable UI.

Where it lives: app store developer consoles. Source files archived outside repo.

10. Landing page hero illustration / animation

Do only after the icon system exists, desktop UI is improved, and product positioning is tighter.

Do not make: a literal illustration of a person in recovery. Keep it abstract — the daily arc, rhythm, momentum. Motion is optional and not worth the complexity at this stage.

Purpose: marketing polish. Not needed for current product closure.

How to make: Figma illustration exported as SVG, or a CSS/Lottie animation. Wire into the landing page component at sobrietyanchor.com.

Where it lives: artifacts/recovery-checkin/src/pages/ — the landing page component.

Notes

Items 1 and 2 can be generated agentically in the current session with no design dependencies. Both are high value for case study and founder content.

Items 3, 4, and 5 should be done together in one dedicated creative session. Do not rush the icon — it sets the visual identity for everything downstream.

Items 6 and 9 are explicitly gated on the desktop redesign being stable. Do not produce marketing screenshots of a UI that is actively being reworked.
