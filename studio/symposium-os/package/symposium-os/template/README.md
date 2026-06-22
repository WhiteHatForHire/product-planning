# .symposium/

The Symposium OS skills marketplace, copied into this project at init time.

The archive holds memory. The skills execute judgment. The language layer keeps the machine aligned.

This folder is NOT authored fresh per project. It is copied from the Symposium OS canonical `template/` directory and tailored by the init prompt to the project's stack, vocabulary, and first architectural decisions. To upgrade, re-copy from the canonical and re-apply project-specific entries.

## What's in here

```
.symposium/
├── README.md                  this file
├── AUTONOMY_LAYER.md          execution doctrine (always applied by agents)
├── META_PROMPT.md             spec-to-directive converter
├── CONTEXT.md                 project-specific glossary and ubiquitous language
│
├── skills/                    invocable, named patterns at decision points
│   ├── planning/              before code (directive generation, planning interviews)
│   ├── diagnostics/           read state (API truth tables, feed validation)
│   ├── execution/             write state (MCP write safety, deployment preflight)
│   ├── review/                gate state (council, public surface QA, build ledger)
│   └── handoff/               transfer state (agent-to-agent context handoff)
│
├── templates/                 reusable scaffolds (directive, handoff, build report, ADR)
└── adr/                       architecture decision records
```

## Mental model

`AUTONOMY_LAYER.md` is the kernel. It's the protocol that always applies to autonomous agents. They obey it unconditionally.

`skills/` are libraries. Each one is invocable at a specific decision point by an operator or an agent. Like function calls: "run API Surface Diagnostic on this feature scope."

`META_PROMPT.md` is the compiler. It takes a spec and produces a directive using AUTONOMY_LAYER as the runtime.

`CONTEXT.md` is the language layer. It prevents the agent from treating project-specific terms generically.

`adr/` is the decision archive. Captures non-obvious choices for future operators and collaborators.

## How to use a skill

Each skill folder contains a `SKILL.md` that specifies:
- **Purpose**: one-sentence outcome
- **When to invoke**: trigger conditions
- **Inputs**: what the skill needs
- **Process**: numbered steps
- **Outputs**: what it produces
- **Stop conditions**: when to halt

To invoke a skill in agent context: "Run skill `[name]` with inputs [...]"

To invoke a skill manually: read the SKILL.md, follow the process, produce the output artifact.

## How to add a project-specific skill

1. Decide which category it belongs to (planning, diagnostics, execution, review, handoff).
2. Create `skills/[category]/[skill-name]/SKILL.md` using the structure above.
3. If the skill produces a structured artifact, add a template to `templates/`.
4. If the skill represents a meaningful architectural decision, write an ADR.
5. Update `CONTEXT.md` if it introduces new vocabulary.

A project-specific skill that recurs across three or more projects is a candidate for promotion to canonical. See the Symposium OS docs for the promotion process.

## Versioning

`AUTONOMY_LAYER.md` and `META_PROMPT.md` carry version numbers and track the canonical Symposium OS release they were copied from. Skills are not individually versioned; they evolve in place. ADRs are immutable once written; supersede with a new ADR rather than editing.

## Upgrading from a newer Symposium OS canonical

1. Diff the project's current `AUTONOMY_LAYER.md` and `META_PROMPT.md` against the new canonical.
2. Apply protocol changes. Preserve section 0.1 (stack) and section 2.3 (project-specific repair entries).
3. Diff skills. Apply any improvements to existing skills. Add new canonical skills if applicable.
4. Note the new canonical version in a chore commit: `chore(symposium): upgrade to canonical v[X.Y]`.

## Init dependency

This folder relies on the init step having filled in:
- `AUTONOMY_LAYER.md` section 0.1 (stack reality)
- `CONTEXT.md` Product / Domain / Architecture terms
- `adr/0001-adopted-symposium-os.md` (date adopted and reference to the OS canonical)

Without these, the `generate-directive` skill will halt at its first stop condition.
