# .symposium/

The Symposium OS skills marketplace. Lives at the root of every Symposium Studios project.

The archive holds memory. The skills execute judgment. The language layer keeps the machine aligned.

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

`skills/` are libraries. Each one is invocable at a specific decision point by a human or an agent. Like function calls: "run API Surface Diagnostic on this feature scope."

`META_PROMPT.md` is the compiler. It takes a spec and produces a directive using AUTONOMY_LAYER as the runtime.

`CONTEXT.md` is the language layer. It prevents the agent from treating project-specific terms generically.

`adr/` is the decision archive. Captures non-obvious choices for future-Marcus or future-collaborator.

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

## How to add a new skill

1. Decide which category it belongs to (planning, diagnostics, execution, review, handoff).
2. Create `skills/[category]/[skill-name]/SKILL.md` using the structure above.
3. If the skill produces a structured artifact, add a template to `templates/`.
4. If the skill represents a meaningful architectural decision, write an ADR.
5. Update CONTEXT.md if it introduces new vocabulary.

## Versioning

`AUTONOMY_LAYER.md` and `META_PROMPT.md` are versioned. Skills are not; they evolve in place. ADRs are immutable once written; supersede with a new ADR rather than editing.

## Provenance

This folder is the canonical Symposium OS scaffold. Copy it into any new Symposium project as `.symposium/`. Fill in `AUTONOMY_LAYER.md` section 0.1 (stack), append project-specific repair entries to section 2, populate `CONTEXT.md`, and seed ADRs as decisions accumulate.
