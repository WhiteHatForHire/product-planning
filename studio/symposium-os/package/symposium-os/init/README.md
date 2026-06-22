# init/

The init system that tailors a fresh `template/` copy into a project's working `.symposium/`.

## Files

- **`INIT_PROMPT.md`** — the interview the operator runs against a directing AI to populate the blank fields in the copied template. **v1.0 shipped with canonical v2.2.**
- **`stack-presets/`** — short-circuit configurations for common stack combinations. Skip the stack-discovery questions in `INIT_PROMPT.md` when one of these matches.
- **`POST_INIT_CHECKLIST.md`** — verification steps the operator runs after init completes. Confirms the template is fully tailored before the project starts firing directives.

## The init flow

1. **Copy.** Copy `template/` into the project root, renaming to `.symposium/`.
2. **Preset check.** If the project's stack matches a `stack-presets/*.yml` file, apply that preset to skip the discovery interview for stack details.
3. **Interview.** Run `INIT_PROMPT.md` against a directing AI. The operator answers questions about the project's stack, vocabulary, first architectural decisions, parallel-agent intent, and credentials.
4. **Generation.** The directing AI emits:
   - Filled-in `AUTONOMY_LAYER.md` section 0.1 (stack)
   - Filled-in `CONTEXT.md` (product, domain, architecture terms; anti-vocabulary)
   - Filled-in `adr/0001-adopted-symposium-os.md` (date, OS version, references)
5. **Verify.** Run `POST_INIT_CHECKLIST.md`. Every item must pass before the project is considered initialized.
6. **Smoke.** Generate a tiny first directive via `template/skills/planning/generate-directive` to confirm the scaffold is wired up correctly end-to-end.

## What init does NOT do

- Init does not write project ADRs beyond 0001. Subsequent ADRs are written as architectural decisions arise.
- Init does not author project-specific skills. Those emerge from project work and append to `skills/` over time.
- Init does not configure CI/CD. That's project setup, separate from Symposium OS scaffolding.

## Why init is separate from template

The template is static. It changes only when canonical Symposium OS releases a new version. The init step is dynamic — it adapts the static template to a specific project. Keeping them separate means:

- Template upgrades don't break init.
- Init upgrades don't require template changes.
- Operators can author multiple init variants (different interview styles, different presets) without touching the canonical template.

See `meta-adr/0003-template-vs-init-split.md` for the full reasoning.
