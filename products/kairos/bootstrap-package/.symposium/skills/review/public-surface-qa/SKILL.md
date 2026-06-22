---
name: public-surface-qa
category: review
trigger: Before publishing Marcus Vale, Symposium Studios, or product landing pages and public-facing artifacts.
---

# Public Surface QA

## Purpose
Audit any externally-visible Symposium surface for clipping, readability, CTA clarity, credibility, and overclaim before it ships.

## When to invoke
- Before publishing a new landing page
- Before printing business cards (especially QR-destination pages)
- Before publishing a public artifact like Kairos `/tech-week/marcus`
- After any redesign of an existing public surface

## Inputs
- URL or rendered artifact
- Target audience and stated purpose
- Acceptable risk level (e.g., "this is a public proof artifact, not a brochure")

## Process
1. Mobile readability check: load on iOS Safari and Chrome Android. Check font sizes, tap targets, scroll behavior, clipping.
2. Desktop and tablet layout check: 1280px, 1024px, 768px breakpoints.
3. Clipping, overflow, and weird-artifact scan.
4. CTA clarity: is the next action obvious within 3 seconds?
5. Proof and credibility audit: every metric, claim, and badge is real and substantiated?
6. No fake metrics scan: no "100,000 users" if untrue; no "$10M ARR" placeholders.
7. Empty-link audit: every build-log link, every "case study" link, every external destination works.
8. Navigation audit: every nav link goes somewhere valid.
9. QR destination audit if applicable: scan the printed or rendered QR, confirm it lands on the intended page.
10. Copy audit: no overclaim, no "AI-native" overuse, no Marcus-Vale vs Symposium identity blur.
11. Contact path audit: clear way for the audience to reach Marcus or take next step.
12. Produce QA report.

## Output
A markdown report with pass/fail per check, screenshots or notes for any fail, and recommended fixes ordered by severity.

## Stop conditions
- Halt publication if any "credibility" check fails (fake metric, broken proof link, empty case study).
- Halt if mobile readability fails on iOS Safari (your primary mobile audience).
- Halt if the QR destination is wrong or broken when applicable.

## Related
- `skills/review/council-review` (heavier-weight, for safety-adjacent content)
