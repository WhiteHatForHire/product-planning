# [Project] [Wave Name] — Build Directive v[N]

```
Surfaces:          [files and areas]
Production impact: none | schema-only | API change | UI change | prompt change
Council of Models: yes | no
Auto-merge:        yes | no
Credentials:       [list — or none]
Agent:             CC Local | CC Cloud | split
```

## Role

[One paragraph: what the agent is doing, on which surface, with what constraints.]

## Protocol

Apply `.symposium/AUTONOMY_LAYER.md` before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see `.symposium/AUTONOMY_LAYER.md` section 0.1.

## Deployment Posture

[PR-only stop, auto-merge yes/no with rationale, migration application instructions for Marcus if applicable.]

## Design Data

### Schema deltas
[verbatim]

### File structure
[new files, modified files, deleted files — full paths]

### Code patterns
[snippets for non-obvious patterns]

### Prompt fragments
[verbatim]

### Default values
[verbatim]

## Working Files Protocol

Per `.symposium/AUTONOMY_LAYER.md` section 0.4:
- `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md`
- `AUTONOMOUS_RUN_LOG.md` at repo root
- `BLOCKERS_FOR_MARCUS.md` at repo root
- `docs/deferred-issues.md`

## Phase Plan

### Phase A: [name]
- **Pre-flight**: [per AUTONOMY_LAYER section 3]
- **Smoke assertions (write first)**: [list]
- **Implementation**: [steps]
- **AUTOMATED criteria**: [list]
- **HUMAN_REVIEW items**: [list]
- **Commit**: `[type](scope): [what changed]`

### Phase B: [name]
[same structure]

[...repeat per phase]

## Directive-Specific Repair Entries

[Only if introducing failure modes not in `AUTONOMY_LAYER.md` section 2 playbook.]

## Deferred-Issues Format

See `.symposium/AUTONOMY_LAYER.md` section 4.

## BUILD_REPORT Format

See `.symposium/AUTONOMY_LAYER.md` section 5.

## Hard Stops

See `.symposium/AUTONOMY_LAYER.md` section 6.

## GO

Begin Phase A pre-flight per `.symposium/AUTONOMY_LAYER.md` section 3. Credentials preflight scope: [list]. Cut branch from main: `feat/[directive-slug]`. Create `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md` and `AUTONOMOUS_RUN_LOG.md` at repo root.
