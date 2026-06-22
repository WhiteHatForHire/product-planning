---
name: council-review
category: review
trigger: Before merging safety-adjacent PRs, publishing public surfaces, or shipping high-stakes content.
---

# Council Review

## Purpose
Run a PR, spec, or content artifact through multiple lenses before merge or publication. Catch issues a single reviewer would miss. Required for safety-adjacent content per `AUTONOMY_LAYER.md` section 1.11.

## When to invoke
- PR touches safety-relevant prompts, forbidden-copy lists, or crisis routing
- PR changes user-facing content where misalignment could harm a user
- Public-facing artifact (landing page, social post, printed material) is about to ship
- Spec involves material commercial or reputational risk
- Architecture decision that is hard to reverse and affects multiple surfaces

## Inputs
- The artifact (PR diff, spec, content draft, page URL)
- Stated scope of concern (what specifically needs scrutiny)
- Lens set (default to the seven below; project may declare additional lenses)

## Process
1. Send the artifact through each lens with a specific prompt for that lens. Default lenses:
   - **Product**: Does this serve the stated user need? Is the user benefit clear?
   - **UX**: Is the interaction intuitive? Are edge cases handled? Mobile and desktop?
   - **Architecture**: Is this maintainable? Does it introduce unwanted coupling? Is the abstraction at the right altitude?
   - **Safety / risk**: Could this harm a user? Is there a worst-case interpretation? Are safety rails in place?
   - **Business / commercial**: Does this advance or harm the project's positioning? Is it credible?
   - **Brand / public credibility**: Does this read as the kind of thing the project ships? Any overclaim?
   - **Operations / maintainability**: Will this be painful to maintain in 6 months? Are observability hooks in place?
2. For safety-relevant content: run the same prompt through multiple models (typically Claude, GPT, Gemini, Grok). Compare findings across models.
3. Consolidate findings. Surface conflicts between lenses or between models.
4. Produce a council report.

## Output
A markdown report with:
- Per-lens findings (concise, with specific quoted-from-artifact references)
- Per-model findings if multi-model review was used
- Cross-lens and cross-model conflicts surfaced
- Severity (block | warn | nit) per finding
- Recommended actions, ordered by severity

## Stop conditions
- Halt the merge or publication if any "block" severity finding surfaces. Resolve before proceeding.
- Halt if the lenses disagree on whether a finding is "block" vs "warn" — escalate to the operator for adjudication.
- Council can hold a PR or publication. It does not create scope creep unless risk is material.

## Related
- `AUTONOMY_LAYER.md` section 1.11 (production safety boundaries)
- `AUTONOMY_LAYER.md` section 1.6 (fallback content must be specified)
- `skills/review/public-surface-qa` (lighter-weight skill for public-facing surfaces that aren't safety-adjacent)
