# How to Write an ADR

Architecture Decision Records are immutable artifacts of non-obvious decisions. They exist so future operators and collaborators can understand why the current state of a project exists.

---

## When to write an ADR

Write an ADR when **all four** of the following are true:

1. **The decision is hard to reverse.** Changing it later requires migration work, vendor switches, code rewrites, or data restructuring.
2. **The decision is non-obvious.** A reasonable engineer reading the code six months from now would wonder why this choice was made.
3. **There is a real trade-off.** Multiple defensible alternatives existed. Picking one closed off the others.
4. **The decision has consequences beyond a single file or function.** It shapes how subsequent work will be done.

If any of these fails, the decision belongs in a code comment, a spec, a run note, or the commit message — not an ADR.

The bar is intentionally high. Too many ADRs are worse than too few: they dilute the archive and make it hard to find the decisions that actually matter.

---

## When NOT to write an ADR

- **Style and formatting decisions.** Use a style guide or a linter config.
- **Library and version choices.** Use a `package.json` / `Cargo.toml` / `requirements.txt`. ADR only when there was a real alternatives debate.
- **Single-file refactors.** Commit message is sufficient.
- **Decisions you can change tomorrow with no migration cost.** Reversible decisions don't need ADRs.
- **Decisions imposed by external constraints.** If the stack mandates the choice, document the constraint in `AUTONOMY_LAYER.md` section 0.1 instead.

---

## ADR vs other artifacts

| Artifact | What it captures |
|---|---|
| ADR | A specific, hard-to-reverse decision with a clear before/after state. |
| CONTEXT.md entry | A term in the ubiquitous language. |
| Spec | The desired behavior of a system. |
| Run note | Working notes from a session. |
| Build report | The outcome of a build session. |
| Commit message | A code-level change with its rationale. |

ADRs are not specs. ADRs are not status updates. ADRs are not commit logs. ADRs are pinned moments where a fork in the road was chosen and the other paths were closed off.

---

## ADR anatomy

Use `templates/adr-template.md`. The structure is:

- **Title**: `ADR NNNN: [Decision in Title Case]`
- **Date** and **Status** (`Proposed`, `Accepted`, `Superseded by ADR NNNN`)
- **Authors**
- **Context** — what's the situation, what forces are at play, why now
- **Decision** — what was decided, in one or two sentences
- **Consequences** — Positive, Negative, Neutral
- **Alternatives Considered** — and why each was rejected
- **References** — links to specs, PRs, related ADRs, external docs

---

## Authoring guidelines

**Title**: write the decision, not the topic. "ADR 0003: Adopted External Feed as Source of Truth" is good. "ADR 0003: Event Data Strategy" is bad.

**Context**: describe the situation *as it existed before the decision*. Not the decision itself. Not the consequences. Just the state of affairs that forced the choice.

**Decision**: one or two sentences. If it takes a paragraph, you're explaining the consequences, not stating the decision.

**Consequences**: be honest about negative consequences. ADRs that list only positive consequences read like sales pitches and are useless. The negatives are the most valuable part of the record — they tell future readers what was knowingly traded away.

**Alternatives**: include the alternatives that were seriously considered. Not every alternative ever. Show the reasoning that closed them out.

**References**: link to the spec, the PR, the related ADR. Future readers need a path to the surrounding context.

---

## Immutability

Once an ADR is accepted, it is immutable. Do not edit the body to reflect a later change in circumstances.

If the decision changes later:
1. Write a new ADR explaining the new decision.
2. Set the old ADR's status to `Superseded by ADR NNNN`.
3. Leave the body of the old ADR alone.

The history is the record. Editing the record destroys what made it valuable.

---

## Numbering

ADRs are numbered sequentially from `0001`. Per-project ADRs live in the project's `.symposium/adr/`. Meta-ADRs about Symposium OS itself live in `meta-adr/` at the OS repo root.

`0001-adopted-symposium-os.md` is reserved in every project as the initial ADR. Project-specific ADRs start at `0002`.

---

## Checklist before merging an ADR

- [ ] Decision is hard to reverse, non-obvious, has a real trade-off, has cross-cutting consequences.
- [ ] Title is the decision, not the topic.
- [ ] Context describes the pre-decision state of affairs.
- [ ] Decision is stated in one or two sentences.
- [ ] Consequences include negatives, honestly.
- [ ] Alternatives considered are real alternatives, not strawmen.
- [ ] References link to relevant artifacts.
- [ ] Number is the next sequential integer in the project's `adr/`.
