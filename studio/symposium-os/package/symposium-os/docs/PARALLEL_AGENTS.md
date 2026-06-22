# Parallel Agents

The Director Model — directing AI agents rather than coding directly — is most powerful when multiple agents run concurrently against different surfaces of the same project. This document covers how Symposium OS supports parallel agent operation and what patterns work.

---

## What "parallel" means

Multiple distinct agent instances (Claude, Codex, Gemini, or different sessions of the same model) running concurrently against the same repo, each on its own branch, each executing its own directive.

Not multiple turns in one conversation. Not multiple windows of the same agent on the same branch. Distinct, isolated agents on isolated branches.

---

## What it enables

- **Faster shipping** when surfaces are independent. Frontend, backend, and infra waves often have no dependency between them and can run simultaneously.
- **Specialization by capability.** A credentialed local agent runs database migrations and deploys; a code-only cloud agent runs frontend feature work; a Council of Models agent runs safety reviews. Each operates within its scope.
- **Failure isolation.** When one agent halts on a hard stop, the others continue.

---

## Coordination via working files

All parallel agents share coordination state through `AUTONOMY_LAYER.md` section 0.4 working files:

- `AUTONOMOUS_RUN_LOG.md` at repo root — append-only log. Each agent appends its own phase outcomes, SHAs, and `SPEC_REALITY_DELTA` entries. Conflicts at append are rare (last write wins for a few seconds of overlap) and recoverable.
- `BLOCKERS_FOR_OPERATOR.md` at repo root — any agent can append. On merge conflict, accept incoming.
- `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md` — session-scoped. Each agent has its own. No conflicts possible.
- `docs/deferred-issues.md` — append-only by phase.

This is why singleton plan files at repo root are forbidden (per `AUTONOMY_LAYER.md` section 0.4). Singletons produce merge conflicts in parallel work; session-scoped paths do not.

---

## The credentialed/code-only split

Not all agents need credentials. The directive's `Agent:` field declares which agent runs which work.

**Credentialed agents** require operator secrets. Use for:
- Database writes (migrations, data backfills)
- Deploy operations (`vercel --prod`, `fly deploy`, equivalents)
- External API calls that consume operator-owned API keys
- Anything that touches production state

These run on the operator's local machine or in an environment with managed secrets. The operator authorizes credential access per session.

**Code-only agents** never see credentials. Use for:
- Frontend feature work
- Documentation
- Test authoring
- Refactoring
- Schema design (proposing, not applying)
- Code review

These can run on any agent runtime, including cloud agents with no filesystem access to operator secrets.

The directive's parallel-agent split declares the boundary explicitly. Mixing credentialed and code-only work in the same phase is a `generate-directive` halt condition.

---

## Patterns that work

### Surface-parallel
Three agents on three independent surfaces of one feature: backend API agent, frontend UI agent, infra/migration agent. They land in any order. The first to merge triggers the others to rebase per `AUTONOMY_LAYER.md` section 1.15.

### Wave-stacked
Sequential phases of one wave split across agents by capability. Phase A (schema) on credentialed local. Phase B (API handlers) on code-only cloud. Phase C (frontend consumption) on a third code-only cloud. Each phase blocks the next.

### Review-fanout
One implementation agent produces a PR. Four review agents (Claude, GPT, Gemini, Grok) run Council Review against the same diff in parallel. Operator consolidates findings before merge.

### Spec-and-execute split
A planning agent runs the directive interview and produces the directive. An execution agent reads the directive and runs it. The planning agent's session ends before the execution agent starts.

---

## Patterns that don't work

### Shared-file collisions
Two agents editing the same file on overlapping lines. The protocol does not magically resolve this. Surface the conflict, rebase one branch on the other, or split the work along clean file boundaries.

### Speculative parallel
"Let's run three agents on slight variations and pick the best." This wastes context and creates merge ambiguity. If you need to compare approaches, do it on one agent with explicit alternative-comparison framing.

### Cross-credential leakage
Code-only cloud agents asking the operator for credentials mid-run. The protocol forbids this. The directive must declare credential needs upfront.

### Drift across agents
Two agents disagreeing on what `CONTEXT.md` term means. Run `grill-with-docs` before any wave that introduces new vocabulary, and update `CONTEXT.md` first.

---

## Concurrency limits

There is no hard cap in the protocol. The practical cap is the operator's working memory for tracking what each agent is doing and when each will halt.

Most operators max out at 4–6 concurrent agents. Beyond that, the cost of context-switching exceeds the time saved by parallelism. Some operators run more by automating the consolidation step (e.g., a meta-agent that watches all run logs and surfaces only halt events).

The directive's `Agent:` field and the parallel-agent split section should declare the operator's intended concurrency for each wave.

---

## Stacked PR chains across parallel agents

When parallel agents produce PRs that depend on each other in sequence (PR A → PR B → PR C, where each branches off the previous), apply `AUTONOMY_LAYER.md` section 1.15 (Stacked PR conflict resolution protocol).

Key points:
- After any PR in the chain merges, all remaining branches need rebase against the new main HEAD.
- Detect squash-merge SHA drift before plain rebase. Use `--onto` when drift is present.
- The agent maintains the chain automatically once started; the operator does not need to re-fire a directive per merge.
- If the operator's workflow requires per-PR review (auto-merge: no), the agent prepares all remaining branches against current main and stops. The operator reviews and merges. The agent resumes from state detection on the next invocation.

---

## What the operator owns in parallel work

- **Scope split**: which surfaces are parallel vs sequential, declared in the directive.
- **Agent assignments**: which agent runs which work, declared in the directive.
- **Credential boundaries**: which agents have which credentials, declared in the directive.
- **Final merge order**: even with auto-merge enabled, the operator can override merge sequencing if dependencies emerge.
- **Conflict adjudication**: when two agents produce conflicting changes the protocol can't resolve mechanically, the operator decides.

The agents own everything else within their assigned scope.
