---
name: public-surface-qa
category: review
trigger: Before publishing any externally-visible page or artifact.
---

# Public Surface QA

## Purpose
Audit any externally-visible surface for clipping, readability, CTA clarity, credibility, and overclaim before it ships. Lighter-weight than Council Review; appropriate for public surfaces that aren't safety-adjacent.

## When to invoke
- Before publishing a new landing page or marketing surface
- Before printing physical materials with QR codes or URLs (business cards, flyers, signage)
- Before publishing a public artifact (case study, public dashboard, public profile)
- After any redesign of an existing public surface
- Before announcing a launch externally

## Inputs
- URL or rendered artifact
- Target audience and stated purpose
- Acceptable risk level (e.g., "this is a public proof artifact, not a sales brochure")

## Process
1. Mobile readability check: load on iOS Safari and Chrome Android. Check font sizes, tap targets, scroll behavior, clipping.
2. Desktop and tablet layout check: 1280px, 1024px, 768px breakpoints.
3. Clipping, overflow, and rendering-artifact scan.
4. CTA clarity: is the intended next action obvious within 3 seconds?
5. Proof and credibility audit: every metric, claim, and badge is real and substantiated.
6. No-fake-metrics scan: no aspirational numbers ("100,000 users") if untrue; no placeholder values ("$10M ARR") left in.
7. Empty-link audit: every external link, every "case study" link, every nav destination resolves to real content.
8. Navigation audit: every nav link goes somewhere valid.
9. QR destination audit if applicable: scan the printed or rendered QR, confirm it lands on the intended page.
10. Copy audit: no overclaim, no buzzword overuse, no identity blur between project / product / personal brand.
11. Contact path audit: clear way for the audience to take the next step.
12. Accessibility quick-check: contrast ratios on metadata text, alt text on meaningful images, keyboard navigability of primary CTAs.
13. Produce QA report.

## Output
A markdown report with pass/fail per check, screenshots or notes for any fail, and recommended fixes ordered by severity.

## Stop conditions
- Halt publication if any "credibility" check fails (fake metric, broken proof link, empty case study).
- Halt if mobile readability fails on the project's primary mobile target browser.
- Halt if the QR destination is wrong or broken when applicable.
- Halt if any accessibility check fails on a primary CTA path.

## Related
- `skills/review/council-review` (heavier-weight, for safety-adjacent or high-stakes content)
- `skills/review/build-report-ledger` (often run alongside QA before announcing a launch)
