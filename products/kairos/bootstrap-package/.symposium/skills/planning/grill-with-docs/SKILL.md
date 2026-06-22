---
name: grill-with-docs
category: planning
trigger: Before introducing new domain terminology, building a new feature with uncertain language, or clarifying ambiguous concepts.
---

# Grill With Docs

## Purpose
Stress-test a plan or concept against existing repo language and conventions. Update `CONTEXT.md` and recommend ADRs when meaningful decisions surface.

## When to invoke
- Starting a new feature with vocabulary that may overlap with existing terms
- Writing a client build directive
- Clarifying ambiguous concepts before implementation
- A new contributor or agent is asking questions that suggest language drift

## Inputs
- The plan, feature description, or concept under discussion
- Current `CONTEXT.md`
- Current `adr/` directory
- Relevant code paths (the skill will read these)

## Process
1. Read the plan. Extract all proper nouns, technical terms, and product-specific vocabulary.
2. Cross-reference each term against `CONTEXT.md`. Flag conflicts, overlaps, undefined terms.
3. Read any code paths the plan touches. Confirm terminology matches usage.
4. Surface ambiguities as explicit questions.
5. Propose `CONTEXT.md` additions or revisions.
6. Identify decisions that should become ADRs: hard to reverse, future readers would wonder why, real trade-off.
7. Produce a grill report.

## Output
A markdown report with:
- Resolved glossary terms (with proposed `CONTEXT.md` updates inline)
- Open terminology questions for the operator to resolve
- Code paths checked
- Contradictions between plan and current implementation
- Recommended ADRs (only when justified)
- Next-step directive or PRD path

## Stop conditions
- Halt if the plan introduces terms that conflict with the safety-relevant vocabulary in `CONTEXT.md`. Escalate.
- Halt if more than 5 critical ambiguities surface. Plan needs more design work before directive generation.

## Important rule
`CONTEXT.md` is a glossary, not a spec or scratchpad. Implementation choices go to specs, issues, or ADRs. Keep it lean.

## Related
- `CONTEXT.md`
- `adr/`
- `skills/planning/generate-directive`
