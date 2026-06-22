---
title: "Title Marcus s AI Native Builder Workflow & Standards (v1)"
source_archive: "Software Projects"
source_path: "####Software Projects/Title_ Marcus_s AI-Native Builder Workflow & Standards (v1).docx"
status: active
privacy: working
tags:
  - planning
---

# Title Marcus s AI Native Builder Workflow & Standards (v1)

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Title: Marcus's AI-Native Builder Workflow & Standards (v1)

Goal: A living document that captures my current working patterns when directing AI tools as fractional CTO. Not a tutorial on the tools. A codification of MY workflow — the rules I follow, the gates I enforce, the patterns I reach for, and the standards I hold work to.

Audience: Primarily me. Secondarily a senior engineer or VC who wants to understand how I actually work. The document should survive that scrutiny — it should look like the operating manual of someone who has shipped real production software directing AI agents, not a vibe-coder's notes.

Structure I want:

1. Operating principles. The high-level rules that govern everything else. Examples from my actual practice:

- One source of truth (GitHub main branch).

- One implementer per task, one reviewer separately.

- Show me the diff before push on safety-surface and infrastructure PRs.

- "Working" / "feature-complete" / "production-ready" are different and named distinctly.

- Director Model = experienced product/architectural judgment + AI direction, not "AI replaced engineering."

2. The agent roster. Which agent does what, and why I chose them for that role.

- Claude Code: primary implementer in active repos. Strong at reading codebase context, executing multi-file changes, catching spec drift in prompts.

- Codex: reviewer and isolated-environment work. Stubborn implementer in sandboxes, respects constraints, slow but thorough. Used as second-eyes review pass on safety-surface PRs.

- Cursor: evaluated, available, currently not primary.

- Replit Agent: graduated off as primary; remains for runtime/deploy during transition.

- Lovable / v0: aesthetic prototyping layer for utility apps, not production work.

3. PR categorization and gates. The three categories I treat differently:

- Safety-surface: requires Codex review before merge, non-negotiable show-me-the-diff gate, full test coverage including contract assertions, runnable-tonight test command in PR description.

- Infrastructure: show-me-the-diff gate, sanity tests, no required second review.

- Cosmetic: standard Claude Code workflow, merge when green.

4. Spec writing standards. How I write a prompt for an agent engineer.

- Describe behavior and invariants, NOT file:line locations (line numbers go stale, behavior doesn't).

- Name what's in scope AND what's explicitly out of scope.

- Include verification requirements (tests must cover every branch, must assert contracts, must be runnable in my shell).

- End with "Show me the diff before pushing."

- Single-PR shape unless explicitly multi-stage.

5. Review pass standards. How I evaluate an implementer's output.

- Read the diff in GitHub, not in the agent's chat output (different surface, different attention).

- Run tests in my shell, not theirs. Verify independently.

- Check architectural decisions: was the right thing extracted? Was scope held? Was the contract self-enforced by tests?

- Optional Codex re-review on safety-surface PRs.

6. Environmental quirks I've banked. The "I learned this the hard way once" file.

- pnpm commands run from inside repo, not home dir.

- Old Vite holds port 5173 between sessions; netstat + taskkill pattern.

- DATABASE_URL must be set even with dummy value for some test runs.

- Claude Code worktree pattern (.claude/worktrees/) — branch lives in parallel directory, not main working tree.

- Windows git bash: glob expansion on esbuild fails; list files explicitly.

- Never echo env vars even for verification — caused a real key leak yesterday.

7. Recurring prompt templates. Pointers to a prompts/ directory with reusable templates:

- safety-surface-fix.md

- infrastructure-pr.md

- third-party-integration.md

- case-study-update.md

8. What "done" means. The standard for shipping.

- Tests pass in my shell, not just the implementer's.

- Test coverage exercises every branch, asserts every contract.

- PR description includes problem, fix, runnable test command, deviation notes.

- Squash merge with clean commit message.

- Builder's Log entry written before session ends.

9. Workflow patterns by mode. Adapted from my Four Modes framework:

- Build mode: long focused sessions, single PR shape, full review gates.

- Arena mode: faster cycles, more parallel work, tighter prompts.

- Integration mode: writing case studies, refining prompts, banking quirks.

- Exploration mode: trying new tools in isolated sandboxes, no production work.

10. Anti-patterns I avoid. The things that look like progress but aren't.

- Going wide across tools instead of deep in a small stack.

- Skipping the diff-review gate to ship faster.

- Estimating time durations (I'm consistently wrong).

- Letting a small issue become "the new bat" — a side quest that consumes the main work.

- Trusting an implementer's "tests pass on my end" without running them in my own shell.

- Merging safety-surface PRs without a second review pass.

Voice and constraints:

- Written in MY voice. Direct, precise, structured, no AI hype.

- No em dashes. They read as AI tells in writing meant to represent me.

- No "just vibes" or Gen Z "vibes."

- No horizontal divider lines.

- Preserve heading hierarchy. Use prose where prose is right, lists where lists are right.

- Length: approximately 2,500 to 4,000 words. Tight enough to actually re-read, deep enough to be useful.

Source material to draw from when writing:

- My existing operating notes (the userMemories, particularly the AI tooling workflow section).

- Tonight's H3 PR session: spec drift catch, the Codex review pattern, the implementer/reviewer split working in real time, the environmental friction (worktree, Windows glob, DATABASE_URL).

- The Anchor V3 Production Deployment Plan structure.

- The Director Model framing.

Out of scope:

- Generic AI-tool tutorials. This document assumes the reader knows what Claude Code, Codex, Cursor, etc. are. It's about MY workflow with them, not what they are.

- Speculative future workflows (multi-agent orchestration, LangGraph, etc.). This is current practice only. v2 can include the next layer when I'm actually working at that layer.

- Anchor-specific details. Use Anchor as example, but the document is about the workflow, not the project.

Deliverable:

A complete document, structured as above, ready to save as a .docx. Include a brief opening that names what the document is, who it's for, and what it doesn't try to be. Date it. Mark it as v1.
