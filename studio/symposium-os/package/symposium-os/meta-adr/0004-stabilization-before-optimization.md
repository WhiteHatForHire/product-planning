# Meta-ADR 0004: Stabilization Before Optimization

**Date**: 2026-05-18
**Status**: Accepted
**Authors**: Symposium OS

## Context

Across multiple projects, a recurring failure pattern has emerged: the operator and the agent are deep in algorithm tuning, scoring calibration, or feature optimization when the actual product is broken at the integration level. Profile state doesn't persist. Schedule page reads from the wrong store. Mobile layout duplicates intake cards. Calendar deep links download .ics regardless of provider preference. The data layer is excellent; the visible product is incoherent.

The temptation in this state is to keep optimizing the engine — better scoring, sharper labels, more aliases — because the engine is what the operator has been building and the engine is what the operator knows how to talk about. Meanwhile, what users actually experience is a product that doesn't appear to know what they told it.

This failure mode is operator-side, not agent-side. The agent will optimize whatever the directive says to optimize. The judgment call is at the directive level: when is more cleverness wrong, and when is product coherence the right next move?

## Decision

Adopt **stabilization before optimization** as a Symposium OS-canonical operating principle:

When the visible product is incoherent — when profile state doesn't propagate, when shortlist and schedule disagree, when mobile layout is unusable, when integrations announce one thing and do another — the next move is not more algorithm work. The next move is integration stabilization. Make the visible loop trustworthy end to end before adding more cleverness underneath.

This principle is encoded operationally as follows:

1. **Directive headers may declare `Non-Goals`** explicitly (added to `directive-template.md`). Stabilization directives use this to lock out scoring or optimization drift mid-run.

2. **The `generate-directive` skill checks for a coherent visible loop** before allowing optimization-only directives to proceed. If recent user testing or production observation has surfaced integration bugs, the skill surfaces them as a stop condition to be addressed first.

3. **The `production-bug-triage` skill exists** specifically to convert user-reported coherence bugs into stabilization directives before any further optimization work.

4. **The `post-run-mortem` skill flags** when a session over-invested in optimization while integration bugs remained open, to surface the pattern for future sessions.

## Consequences

### Positive
- Products ship with coherent visible loops, which is what users actually evaluate.
- The operator's directive output is less brittle: stabilization PRs land cleanly because their scope is bounded.
- Algorithm work, when it does happen, lands on a working product surface rather than a broken one.
- The principle gives the operator language for the judgment call: "this is a phronesis moment — stabilization before optimization." Easier to invoke than to re-derive.

### Negative
- Stabilization is less exciting than algorithm work. The operator may resist invoking the principle exactly when it matters most.
- Stabilization directives can feel like "going backwards" to clean up debt that wasn't visible during the optimization arc. The operator may underestimate the time required.
- A pure stabilization session produces fewer dramatic before/after artifacts for case studies. The wins are quieter.

### Neutral
- The principle does not say algorithm work is bad. It says algorithm work after the visible loop is coherent compounds; algorithm work before is wasted.

## Alternatives Considered

- **No formal principle; rely on operator instinct**: rejected because the operator's instinct in this state often drifts toward more algorithm work. The pull is real and bidirectional; the principle exists to counter it.

- **Block optimization directives unless integration tests pass**: rejected as too rigid. Some integration debt is acceptable when the operator has explicit reason to prioritize an algorithm change first (e.g., the algorithm change is what reveals which integration bugs matter). The principle is a heuristic, not a hard gate.

- **Encode this as a section in `AUTONOMY_LAYER.md` rather than a meta-ADR**: rejected because the principle is operator-facing judgment, not agent-facing protocol. Agents executing a stabilization directive don't need the principle; they need the directive. The operator needs the principle when deciding what directive to write next.

## When the principle does NOT apply

- The algorithm change directly fixes a visible coherence bug (e.g., scoring returns no labels because the cap is set wrong). Then the algorithm work IS the stabilization work.
- The integration layer is fine; only the algorithm output is wrong. Optimize freely.
- The operator has explicit user research showing the visible loop is acceptable and the algorithm is the bottleneck.

## How to recognize the moment

The principle applies when at least two of the following are true:

- User testing or production observation surfaces multiple bugs at the integration / state / UI / mobile layer
- Engineering effort has been concentrated on scoring, search, or algorithm work for multiple sessions
- The operator finds themselves explaining why the product "should" work despite users not experiencing it that way
- The next planned directive is about making the algorithm cleverer, not making the existing cleverness visible

When at least two are true, stop. Invoke `production-bug-triage`. Write a stabilization directive. Resume optimization once the visible loop is coherent.

## References

- `template/skills/planning/production-bug-triage/SKILL.md` — converts user-reported coherence bugs into stabilization directives
- `template/skills/review/post-run-mortem/SKILL.md` — flags stabilization-vs-optimization drift across sessions
- `template/templates/directive-template.md` — Non-Goals section, where stabilization directives lock out optimization drift
- `PHILOSOPHY.md` — three-layer architecture (memory / judgment / language); this principle is judgment-layer doctrine
