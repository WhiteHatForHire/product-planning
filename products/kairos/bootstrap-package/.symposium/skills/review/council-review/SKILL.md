---
name: council-review
category: review
trigger: Before merging safety-adjacent PRs, publishing public surfaces, or shipping high-stakes content.
---

# Council Review

## Purpose
Run a PR, spec, or content artifact through multiple lenses before merge or publication. Catch issues a single reviewer would miss.

## When to invoke
- PR touches safety-relevant prompts or copy
- PR changes user-facing crisis or sober-relevant content (in Anchor) or attendee-facing content (in Kairos)
- Public-facing artifact (landing page, social post, business card) is about to ship
- Spec involves material commercial or reputational risk

## Inputs
- The artifact (PR diff, spec, content draft, page URL)
- Stated scope of concern (what specifically needs scrutiny)

## Process
1. Send the artifact through each lens with a specific prompt for that lens. Lenses:
   - **Product**: Does this serve the user need? Is the user benefit clear?
   - **UX**: Is the interaction intuitive? Are edge cases handled? Mobile and desktop?
   - **Architecture**: Is this maintainable? Does it introduce coupling? Is the abstraction at the right altitude?
   - **Safety / risk**: Could this harm a user? Is there a worst-case interpretation? Are safety rails in place?
   - **Business / commercial**: Does this advance or harm Symposium's positioning? Is it credible?
   - **Brand / public credibility**: Does this read as the kind of thing Symposium ships? Any overclaim?
   - **Operations / maintainability**: Will this be a pain in 6 months? Are observability hooks in place?
2. Use multiple models for safety-relevant content: Claude, GPT, Gemini, Grok. Compare findings.
3. Consolidate findings. Surface conflicts between lenses.
4. Produce a council report.

## Output
A markdown report with:
- Per-lens findings (concise)
- Cross-lens conflicts surfaced
- Severity (block | warn | nit) per finding
- Recommended actions

## Stop conditions
- Council can hold a PR or publication. It does not create scope creep unless risk is material.
- Halt the merge or publication if any "block" severity finding surfaces. Resolve before proceeding.

## Related
- `AUTONOMY_LAYER.md` section 1.11 (production safety boundaries)
- `skills/review/public-surface-qa` (lighter-weight skill for public-facing artifacts)
