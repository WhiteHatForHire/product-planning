# Symposium OS

A reusable operating system for directed AI agent work. Templates, skills, and protocols for autonomous build sessions across any project, any stack, any agent runtime.

The archive holds memory. The skills execute judgment. The language layer keeps the machine aligned.

## What this is

Symposium OS is a versioned, portable scaffold that drops into any project to make autonomous agent work reliable:

- **A protocol** (`AUTONOMY_LAYER.md`) that agents unconditionally obey. Covers tiered self-repair, atomic commits, MCP write safety, spec-reality reconciliation, stacked PR handling, and hard-stop conditions.
- **A compiler** (`META_PROMPT.md`) that converts a project spec into a runnable directive.
- **A skills marketplace** organized by action mode: planning, diagnostics, execution, review, handoff.
- **A language layer** (`CONTEXT.md`) that prevents agents from treating domain-specific terms generically.
- **An immutable decision log** (`adr/`) for non-obvious architectural choices.

## Who this is for

- Operators running the Director Model: directing AI agents rather than writing code directly.
- Operators running multiple concurrent agents and needing shared coordination.
- Operators building safety-adjacent products where multi-model review is non-negotiable.
- Operators who want their build method to be a portable, version-controlled artifact rather than tribal knowledge in chat history.

## Repository layout

```
symposium-os/
├── README.md              this file
├── OVERVIEW.md            complete file-by-file map of the repo
├── CHANGELOG.md           canonical version changes
├── PHILOSOPHY.md          operating philosophy and mental model
│
├── template/              the canonical .symposium/ to copy into projects
│   ├── README.md          in-template readme
│   ├── AUTONOMY_LAYER.md  protocol (versioned)
│   ├── META_PROMPT.md     spec-to-directive converter (versioned)
│   ├── CONTEXT.md         project ubiquitous language (blank template)
│   ├── skills/            invocable named patterns
│   ├── templates/         scaffolds (directive, handoff, build report, ADR)
│   └── adr/               per-project architecture decisions
│
├── init/                  init system that tailors template → project
│   ├── INIT_PROMPT.md     interview prompt the operator runs
│   ├── stack-presets/     short-circuit common stack combos
│   └── POST_INIT_CHECKLIST.md
│
├── docs/                  documentation about the OS itself
│   ├── HOW_TO_AUTHOR_A_SKILL.md
│   ├── HOW_TO_WRITE_AN_ADR.md
│   ├── VERSIONING.md
│   ├── PARALLEL_AGENTS.md
│   └── PROMOTING_PROJECT_LEARNINGS.md
│
├── case-studies/          real worked examples from production projects
├── meta-adr/              ADRs about the OS itself (not per-project)
└── archive/               historical canonical versions
```

## How to adopt Symposium OS in a project

1. Copy `template/` into the project root as `.symposium/`.
2. Run the init interview (`init/INIT_PROMPT.md`) to fill in:
   - `AUTONOMY_LAYER.md` section 0.1 (stack)
   - `CONTEXT.md` Product / Domain / Architecture terms
   - `adr/0001-adopted-symposium-os.md`
3. Run `init/POST_INIT_CHECKLIST.md` to verify init completed.
4. Generate the first directive via `template/skills/planning/generate-directive` and `META_PROMPT.md`.

## How to use a skill

Each skill folder contains a `SKILL.md`. To invoke in agent context: "Run skill `[name]` with inputs [...]"

## How to upgrade a project to a new canonical version

See `docs/VERSIONING.md` for the diff-and-merge procedure.

## How to contribute back

A project-specific learning recurs across three or more projects → it's a candidate for promotion to canonical. See `docs/PROMOTING_PROJECT_LEARNINGS.md`.

## Status

Current canonical: **v2.3** (see `CHANGELOG.md`).

For a complete file-by-file overview of the entire repo, see `OVERVIEW.md`.

## License

[TBD]
