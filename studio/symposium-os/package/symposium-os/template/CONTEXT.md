# CONTEXT.md — [Project Name]

Ubiquitous language for [project name]. Read first when joining a session. Update via PR when introducing or clarifying domain terms.

This file is project-specific. It prevents agents from treating domain-specific terms generically. Keep it lean — implementation details go in specs, ADRs, or code; only terminology belongs here.

---

## How to use this file

- **Read** this file at the start of any planning, design, or implementation session for the project.
- **Update** this file via PR when a new term is introduced, an existing term is clarified, or a term is deprecated.
- **Reference** by term name in directives, ADRs, and specs rather than redefining inline.
- **Promote** terms from one-off spec definitions into this file once they appear in three or more documents.

The `grill-with-docs` skill (`.symposium/skills/planning/grill-with-docs/SKILL.md`) audits new vocabulary against this file before generating directives.

---

## Product terms

User-facing concepts, named features, the things a user would recognize from the product surface.

- **[Term]** — [definition]
- **[Term]** — [definition]

## Domain terms (project-specific concepts)

Concepts internal to the problem domain that aren't user-visible but recur across specs, code, and discussions.

- **[Term]** — [definition]
- **[Term]** — [definition]

## Architecture terms

Internal names for systems, pipelines, data artifacts, services, integration boundaries.

- **[Term]** — [definition]
- **[Term]** — [definition]

## Symposium terms (carry over from OS)

These are constant across all projects using the Symposium OS scaffold. Do not redefine; reference here.

- **AUTONOMY_LAYER** — execution protocol. See `.symposium/AUTONOMY_LAYER.md`.
- **META_PROMPT** — spec-to-directive converter. See `.symposium/META_PROMPT.md`.
- **Skill** — an invocable named pattern with a `SKILL.md`. See `.symposium/skills/`.
- **Directive** — a single Markdown file describing one autonomous build wave. Generated via `META_PROMPT.md`. Executed by an agent.
- **Council of Models** — multi-model review (typically Claude, GPT, Gemini, Grok) for safety-adjacent or high-stakes content. Invoked via `.symposium/skills/review/council-review/SKILL.md`.
- **Director Model** — operator pattern of directing agents over coding directly.
- **Spec-reality reconciliation** — `AUTONOMY_LAYER.md` section 1.13. Always run before implementing against directive design data.
- **Operator** — the person directing the work. Owns scope, safety, production credentials, and final review per `AUTONOMY_LAYER.md` section 0.6.
- **Agent** — the AI executing the work. Owns playbook execution, atomic commits, working files, and the build report per `AUTONOMY_LAYER.md` section 0.6.

## Anti-vocabulary (do not use unless quoting)

Terms that produce drift or imprecision. List here so the agent avoids them.

- "Just" / "simply" — implies effort the agent should never imply.
- "[Add project-specific banned terms during init]" — [why not, what to use instead]
