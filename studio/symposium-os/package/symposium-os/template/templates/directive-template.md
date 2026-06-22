# [Project] [Wave Name] — Build Directive v[N]

```
Surfaces:          [files and areas this directive touches]
Production impact: none | data-only | schema-only | API change | UI change | prompt change | safety-adjacent
Council of Models: yes | no
Auto-merge:        yes | no
Credentials:       [list — or none]
Agent:             [agent identifier — e.g. local terminal agent, cloud agent, split]
```

## Role

[One paragraph: what the agent is doing, on which surface, with what constraints.]

## Non-Goals

[Explicit list of work this directive does NOT cover, even if related. Prevents scope drift mid-run. Example: "Do not rework scoring logic." "Do not touch backend handlers." "Do not refactor the test runner." Omit this section only if the directive's scope is genuinely small enough that drift is not a risk.]

## Protocol

Apply `.symposium/AUTONOMY_LAYER.md` before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Stack: see `.symposium/AUTONOMY_LAYER.md` section 0.1.

## Deployment Posture

[PR-only stop, auto-merge yes/no with rationale, migration application instructions for the operator if applicable, production secret application instructions if applicable.]

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

### Migration backfill mappings
[verbatim, if applicable]

## Working Files Protocol

Per `.symposium/AUTONOMY_LAYER.md` section 0.4:
- `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md`
- `AUTONOMOUS_RUN_LOG.md` at repo root
- `BLOCKERS_FOR_OPERATOR.md` at repo root
- `docs/deferred-issues.md`

## Phase Plan

**No halt between phases.** The agent runs phases continuously. After opening a PR at the end of a phase, the agent immediately cuts the next branch and begins the next phase. The operator merges all PRs in order after the full run completes. See `.symposium/AUTONOMY_LAYER.md` section 1.15.

### Phase A: [name]
- **Pre-flight**: per `.symposium/AUTONOMY_LAYER.md` section 3
- **Smoke assertions (write first)**: [list] — for docs-only phases, use validation checks per `.symposium/AUTONOMY_LAYER.md` section 3 EXECUTION
- **Implementation**: [steps]
- **AUTOMATED criteria**: [list]
- **HUMAN_REVIEW items**: [list]
- **Commit**: `[type](scope): [what changed]`
- **End-of-phase**: open PR, log URL, immediately cut next branch and begin Phase B. Do NOT wait for operator merge.

### Phase B: [name]
[same structure]

[...repeat per phase]

## Parallel-Agent Split (if applicable)

[Which surfaces run on credentialed local agents, which run on code-only cloud agents, dependency order between branches, shared coordination via `AUTONOMOUS_RUN_LOG.md`.]

## Stacked PR Chain (if applicable)

[Chain order, base SHA expectations, sequential merge maintenance per `.symposium/AUTONOMY_LAYER.md` section 1.15.]

## Directive-Specific Repair Entries

[Only if introducing failure modes not in `.symposium/AUTONOMY_LAYER.md` section 2 playbook.]

## Deferred-Issues Format

See `.symposium/AUTONOMY_LAYER.md` section 4.

## BUILD_REPORT Format

See `.symposium/AUTONOMY_LAYER.md` section 5.

## Hard Stops

See `.symposium/AUTONOMY_LAYER.md` section 6.

## GO

Begin Phase A pre-flight per `.symposium/AUTONOMY_LAYER.md` section 3. Credentials preflight scope: [list]. Cut branch from main: `feat/[directive-slug]`. Create `docs/run-notes/session-YYYY-MM-DD-[directive-slug]-plan.md` and ensure `AUTONOMOUS_RUN_LOG.md` exists at repo root.
