# Philosophy

The operating philosophy behind Symposium OS. Not a spec, not a tutorial. Read this when wondering why the system is shaped this way.

---

## The three layers

Symposium OS is structured around three layers, each with a single job:

**Memory layer** — the archive. `adr/`, `CHANGELOG.md`, build reports, run logs. Holds what was decided and why. Immutable once written. Future operators read it to understand why the current state exists.

**Judgment layer** — the skills. Invocable named patterns at decision points. Each skill encodes a hard-won lesson about when to halt, what to verify, what to defer. Skills are libraries; the operator and the agent call them by name.

**Language layer** — `CONTEXT.md`. Project-specific ubiquitous language. Prevents the agent from treating domain terms generically. The smallest layer, the highest leverage.

The protocol (`AUTONOMY_LAYER.md`) sits underneath all three as the kernel that the agent unconditionally obeys.

---

## The Director Model

The operator directs. The agent executes. The split is real and deliberate.

The operator owns:
- Scope and strategic direction
- Architectural decisions outside the directive's stated bounds
- Safety-adjacent content
- Production credentials
- Final review and merge authorization

The agent owns:
- Execution within the directive
- Self-repair within the playbook
- Spec-reality reconciliation
- Deferral decisions inside the directive's bounds
- Atomic commits, working files, build report

The directive is the contract between them. When the directive is ambiguous, the agent defers rather than expanding scope. Scope creep is a deferrable issue, not a license to expand.

This split exists because the failure modes of AI agents are predictable and correctable when the operator stays in the loop on scope, safety, and merge — and intolerable when the operator delegates those.

---

## The contract is the doctrine

`AUTONOMY_LAYER.md` is not advisory. It is the contract. Agents do not negotiate it. The operator does not edit it casually. It carries a version number and a change log because changes to the contract are events that downstream projects need to know about.

Strip nothing from the doctrine when copying it into a new project. The doctrine is what makes autonomous execution reliable. Filling in section 0.1 (stack) and appending project-specific repair entries to section 2.3 is the entire authorized customization surface.

---

## Skills are libraries, not rules

Skills get invoked. The operator runs them; the agent runs them. They are reusable named patterns, not always-on policies. The protocol is what's always on.

A skill is worth writing when the same pattern recurs across sessions and the cost of re-deriving it each time exceeds the cost of formalizing it. Most one-off patterns should not become skills. Skill bloat is real and erodes discoverability.

The five categories — planning, diagnostics, execution, review, handoff — correspond to action modes in a build session. A new skill that doesn't fit cleanly into one of them is probably not the right shape.

---

## Promotion, not synchronization

Projects diverge from canonical. That's expected. Each project appends its own repair entries to `AUTONOMY_LAYER.md` section 2.3, its own skills under `skills/`, its own ADRs. None of this flows back to canonical automatically.

A pattern promotes from project-specific to canonical when it recurs across three or more projects. The bar is intentionally high. A pattern that worked once is an experiment. A pattern that works three times is a method.

---

## What this system is NOT

- **Not a code generation tool.** Symposium OS generates directives. Code comes from the agent acting on the directive.
- **Not a workflow engine.** No daemon, no orchestrator, no agent runtime. Just files agents read and operators reference.
- **Not opinionated about your stack.** The protocol works equally well over TypeScript or Python or Go or Rust. Section 0.1 declares the stack; the rest of the doctrine is stack-agnostic.
- **Not opinionated about your agent.** Skills work in Claude, GPT, Gemini, Grok, or any future agent runtime that can read Markdown and execute shell.
- **Not a substitute for judgment.** The Council of Models exists because no single model's judgment is sufficient for safety-adjacent or high-stakes content. The operator's judgment is the final authority.

---

## What this system IS

Memory the operator does not have to carry in their head. Judgment the operator can hand to an agent without losing the thread. Language the agent and the operator share so the same words mean the same things across sessions.

A way to build that scales beyond what one operator can hold in working memory, without losing the things that matter when an operator goes from typing every line to directing agents.
