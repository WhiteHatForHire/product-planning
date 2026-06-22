# POST_INIT_CHECKLIST.md

Run this after the init interview completes. Every item must pass before the project is considered initialized and `generate-directive` can be invoked without halting.

---

## `AUTONOMY_LAYER.md`

- [ ] Section 0.1 (Stack reality) — every field has a concrete value. No `[placeholder]` strings. No "TBD".
- [ ] Section 0.1 — `Build command`, `Typecheck command`, and `Test command` are the exact commands the operator would run from the repo root.
- [ ] Section 2.3 — header is present, ready to append project-specific repair entries. (Empty at init time is expected.)

## `CONTEXT.md`

- [ ] Top heading replaced from `[Project Name]` to the actual project name.
- [ ] **Product terms** section has at least one term defined (or explicitly notes that the project has no product-level vocabulary distinct from its domain).
- [ ] **Domain terms** section has at least one term defined.
- [ ] **Architecture terms** section has at least one term defined.
- [ ] **Anti-vocabulary** section either has project-specific banned terms or is explicitly noted as carrying only the default entries.

## `adr/0001-adopted-symposium-os.md`

- [ ] Date filled in.
- [ ] Canonical Symposium OS version filled in (matches the version in the copied `AUTONOMY_LAYER.md`).
- [ ] Reference link to the Symposium OS repo present.

## Working files convention

- [ ] `docs/run-notes/` directory exists at repo root (create if absent — a session run note will be created in it).
- [ ] Repo root has no pre-existing `BLOCKERS_FOR_OPERATOR.md` left over from another project copy.
- [ ] Repo root has no pre-existing `AUTONOMOUS_RUN_LOG.md` left over.

## Smoke test

- [ ] Generate a minimal directive (one trivial phase) via `.symposium/skills/planning/generate-directive` and `META_PROMPT.md`. The directing AI should produce a runnable directive without halting on any init-related stop condition.
- [ ] If the smoke directive halts on "CONTEXT.md is the blank template", "AUTONOMY_LAYER.md section 0.1 is unfilled", or "adr/0001-adopted-symposium-os.md is unfilled" — init is incomplete. Return to the relevant section above.

## Repo hygiene

- [ ] `.symposium/` is added to version control and committed.
- [ ] `.symposium/AUTONOMY_LAYER.md` carries the canonical version number in its header.
- [ ] Any operator-specific or stack-specific edits to `AUTONOMY_LAYER.md` are confined to section 0.1 and section 2.3. No edits to other sections.

---

## When this checklist passes

The project is initialized. Subsequent work:
- Generate directives via `META_PROMPT.md` + `generate-directive` skill.
- Append project-specific repair entries to `AUTONOMY_LAYER.md` section 2.3 as failure modes are discovered.
- Write project ADRs `0002+` as architectural decisions arise.
- Run `grill-with-docs` before any feature that introduces new vocabulary.

## When this checklist fails

Init is incomplete. Do not fire any directive. Return to `INIT_PROMPT.md` or re-run the relevant init step.
