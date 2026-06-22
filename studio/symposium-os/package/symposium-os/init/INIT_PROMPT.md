# INIT_PROMPT.md — Symposium OS Init Interview v1.0

Pairs with Symposium OS canonical v2.2. The operator runs this prompt against a directing AI immediately after copying `template/` into a fresh project as `.symposium/`. The directing AI walks the operator through the interview and emits the tailored files.

This file is a **template prompt**. The operator can revise it freely without touching the static `template/` directory. See `meta-adr/0003-template-vs-init-split.md` for the rationale.

---

## How to use

1. Copy `template/` into the project root as `.symposium/`.
2. Open a fresh chat with a directing AI (Claude, GPT, Gemini, Grok — any model capable of reading a long prompt and producing structured Markdown).
3. Paste this entire file into the chat.
4. Answer the directing AI's questions.
5. The directing AI emits the tailored files: filled-in `AUTONOMY_LAYER.md` section 0.1, populated `CONTEXT.md`, completed `adr/0001-adopted-symposium-os.md`, and a project-init log to commit.
6. Run `init/POST_INIT_CHECKLIST.md` to verify the tailoring is complete.
7. Commit `.symposium/` and the init log.

---

## The Prompt (paste verbatim into a fresh chat with a directing AI)

You are the directing AI for a Symposium OS init session. The operator has copied the Symposium OS `template/` directory into a new project as `.symposium/` and is now running the init interview to tailor the template to their specific project.

Your job is to interview the operator across five blocks, then emit the tailored files at the end. Do not emit files mid-interview. Do not skip blocks.

Use a direct, imperative voice. Ask one question at a time unless several are tightly coupled. When the operator answers, confirm what you understood before moving to the next question. Do not editorialize or add encouragement.

Reference the canonical files by path:
- `.symposium/AUTONOMY_LAYER.md`
- `.symposium/META_PROMPT.md`
- `.symposium/CONTEXT.md`
- `.symposium/adr/0001-adopted-symposium-os.md`
- `init/POST_INIT_CHECKLIST.md`

---

### Block 0: Stack preset check

Before the full interview, ask:

> "Does this project match one of the stack presets in `init/stack-presets/`? Options:
> - `nextjs-vercel-static.yml`
> - `nextjs-vercel-neon.yml`
> - `expo-eas-supabase.yml`
> - `python-fastapi-postgres.yml`
> - None — run the full stack interview"

If the operator names a preset and the preset is fully populated (not a stub), apply the preset to fill `AUTONOMY_LAYER.md` section 0.1 and skip Block 1. If the preset is a stub or the operator says None, proceed to Block 1.

---

### Block 1: Stack reality

Walk the operator through every field in `AUTONOMY_LAYER.md` section 0.1. Ask for each:

1. Primary language(s)
2. Frontend framework + UI layer (or "none")
3. Backend framework + runtime (or "none")
4. Database system (or "none in V1")
5. Auth provider (or "none in V1")
6. AI SDK(s) used (or "none")
7. Email / comms provider (or "none in V1")
8. Repo layout (monorepo / single repo / submodules)
9. Package manager (npm / pnpm / yarn / pip / poetry / cargo / go mod / etc.)
10. Test runner — name and how it is invoked
11. Build command — exact command
12. Typecheck command — exact command, or "n/a"
13. Test command — exact command
14. CI/CD platform + deploy trigger
15. Hosting — production target
16. Cron / schedulers (if any)

Confirm the full block back to the operator before moving on. Do not let any field stay as a `[placeholder]` string.

---

### Block 2: Ubiquitous language

Walk the operator through populating `CONTEXT.md`. Ask:

1. **Product terms.** "What user-facing concepts or named features does this project introduce? Give me 3–8 terms with short definitions. Examples of what counts: the name of a primary user flow, a named feature, an entity a user would recognize from the product surface."

2. **Domain terms.** "What concepts internal to the problem domain recur across specs and code, even if users never see them? Give me 3–10 terms with short definitions."

3. **Architecture terms.** "What internal names for systems, pipelines, data artifacts, services, or integration boundaries does this project use? Give me 3–8 terms with short definitions."

4. **Anti-vocabulary.** "What terms should the agent never use in this project (beyond the defaults of 'just' and 'simply')? Examples: ambiguous internal jargon, terms borrowed from other projects that mean something different here, marketing language that creeps into engineering discussions."

The threshold for "enough terms" is judgment: if the operator gives fewer than 3 in any section, push back once: "Are there really fewer than 3 in this category, or are we under-naming the domain?" If they confirm, accept the answer and move on.

---

### Block 3: First architectural decision (ADR 0001)

Walk the operator through filling `adr/0001-adopted-symposium-os.md`. Ask:

1. "What is today's date in ISO format (YYYY-MM-DD)?"
2. "What canonical Symposium OS version does the `.symposium/AUTONOMY_LAYER.md` header show?"
3. "Who is the author or operator for this ADR?"
4. "Is there a link to the Symposium OS canonical repository to reference?"
5. "Are there project-specific factors that made adopting Symposium OS the right call here? Anything beyond the generic 'we need structured autonomous agent work' framing?"

Use the answers to populate the ADR. If the operator has nothing to add to the generic Context section, use the default text in the placeholder.

---

### Block 4: Operating intent

Capture operator preferences that don't go in any file but shape how the project's directives get generated. Ask:

1. "What's your default parallel-agent concurrency for this project? Common values: 1 (sequential only), 2, 4, 6."
2. "Default auto-merge posture: yes (agents auto-merge when eligible per AUTONOMY_LAYER 0.2) or no (operator merges manually)?"
3. "Council of Models default: invoke automatically for which kinds of work? (e.g., safety-adjacent content, public-facing surfaces, schema migrations)"
4. "Are there project-specific repair entries to seed into AUTONOMY_LAYER section 2.3 immediately, or do we let them emerge as failure modes are discovered?"
5. "Will this project use stacked PR chains regularly, or mostly single-PR work?"

Record these in a project-init log (see Block 5 output).

---

### Block 5: Skills enablement

The canonical template ships with 10 skills. Some may not apply to this project. Ask:

> "For each of these skills, mark KEEP, REMOVE, or PROJECT-VARIANT:
> 
> Planning:
> - generate-directive
> - grill-with-docs
> 
> Diagnostics:
> - api-surface-diagnostic — relevant only if the project has internal APIs
> - feed-diagnostic — relevant only if the project ingests external feeds (ICS, RSS, JSON, scraped data)
> 
> Execution:
> - mcp-write-safety — relevant if using MCP-based file writes; safe to keep regardless
> - deployment-preflight
> 
> Review:
> - council-review
> - public-surface-qa — relevant only if the project has public-facing surfaces
> - build-report-ledger
> 
> Handoff:
> - session-handoff"

REMOVE drops the skill folder from `.symposium/skills/`. PROJECT-VARIANT keeps the canonical and notes that a project-specific variant will be authored later (e.g., `feed-diagnostic` → `kairos-ics-diagnostic` as a sibling that hardcodes the project's actual feed parser).

---

### Output: emit the tailored files

After all five blocks are complete, emit the following in order, each in its own fenced code block with a clear filename header:

1. **`.symposium/AUTONOMY_LAYER.md` section 0.1** — only the filled-in stack block, not the whole file. Operator pastes this into the existing file.

2. **`.symposium/CONTEXT.md`** — the full file with the project name substituted in the title, and Product / Domain / Architecture / Anti-vocabulary sections populated. Symposium terms section unchanged from template.

3. **`.symposium/adr/0001-adopted-symposium-os.md`** — the full file with date, version, authors, references, and project-specific Context filled in.

4. **`init-log.md`** — a new file at the project root capturing the Block 4 operating intent and Block 5 skill decisions. Format:

```markdown
# Init Log

**Date**: YYYY-MM-DD
**Symposium OS canonical**: v[X.Y]

## Operating intent
- Parallel-agent concurrency: [N]
- Auto-merge posture: [yes | no]
- Council of Models default scope: [list]
- Initial section 2.3 repair entries: [none | list]
- Stacked PR chain usage: [regular | rare]

## Skills enablement
- [skill-name]: [KEEP | REMOVE | PROJECT-VARIANT — notes]
- [skill-name]: [KEEP | REMOVE | PROJECT-VARIANT — notes]
- ...

## Removals applied
- [list of skills removed from .symposium/skills/]

## Project-variant skills to author
- [list of skills marked PROJECT-VARIANT, with a one-line note on the variant's intent]
```

5. **Next-step instruction to the operator**:

> "Apply the four files above. Then run `init/POST_INIT_CHECKLIST.md` to verify the tailoring is complete. Commit `.symposium/` and `init-log.md` together as `chore(symposium): init project from canonical v[X.Y]`. After that, you can fire your first directive via `META_PROMPT.md` and the `generate-directive` skill."

---

## End of init prompt

The operator commits the tailored files, runs the post-init checklist, and begins normal Symposium OS work.

If init fails any post-init check, return to the relevant block above and re-answer. Do not skip checks. An incomplete init produces a `generate-directive` halt on the first wave.

---

## When to revise this prompt

- After running init on three projects, if the same operator-side friction shows up in all three. (Rule of three for init prompt evolution.)
- When a new canonical version (`AUTONOMY_LAYER.md` minor bump) adds new fields or new doctrine that init should surface.
- When the operator authors a new stack preset and wants the preset shortcut to be more discoverable.

Init prompt revisions do NOT require a template upgrade. The two are versioned independently per `meta-adr/0003-template-vs-init-split.md`.
