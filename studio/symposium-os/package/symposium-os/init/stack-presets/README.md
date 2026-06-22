# stack-presets/

> **ROADMAP — NONFUNCTIONAL IN v1.0 INIT.** The preset files in this directory are stubs. The v1.0 init prompt (`init/INIT_PROMPT.md`) checks for preset selection in Block 0 but falls through to the full stack interview when the named preset is a stub. Presets become functional once an operator authors their full content. See "Authoring a new preset" below.

Short-circuit configurations for common stack combinations. Skip the stack-discovery questions in `INIT_PROMPT.md` when one of these matches the project being initialized.

## Format

Each preset is a YAML file containing the values that would populate `AUTONOMY_LAYER.md` section 0.1. The init step reads the matching preset, fills the section, and proceeds to the next interview step.

```yaml
# Example preset shape
name: [preset-name]
description: [one line]

stack:
  languages: [...]
  frontend: [...]
  backend: [...]
  database: [...]
  auth: [...]
  ai: [...]
  email: [...]
  repo_layout: [...]
  package_manager: [...]
  test_runner: [...]
  build_command: [...]
  typecheck_command: [...]
  test_command: [...]
  cicd: [...]
  hosting: [...]
  cron: [...]
```

## Existing presets

The presets directory ships with stubs for common combinations the operator has used or expects to use. Each is a placeholder until the operator authors the full preset content during init prompt development.

- `nextjs-vercel-static.yml` — Next.js on Vercel, static data (no DB)
- `nextjs-vercel-neon.yml` — Next.js on Vercel with Neon Postgres
- `expo-eas-supabase.yml` — Expo + EAS with Supabase backend
- `python-fastapi-postgres.yml` — FastAPI on Python with Postgres

## Authoring a new preset

1. Identify the recurring stack combination (rule of three: when you've initialized the same stack three times manually).
2. Copy an existing preset as a starting point.
3. Fill in every field — do not leave blanks; the preset is only useful if it's fully complete.
4. Test by running init against a fresh template with this preset selected.
5. Commit with `chore(presets): add [stack-name] preset`.

## When NOT to use a preset

- The project's stack differs from any preset in any meaningful way.
- The project mixes stacks (e.g., a Python backend with a Next.js frontend that doesn't match `nextjs-vercel-*`).
- The operator wants to walk through the stack-discovery interview deliberately for a new pattern.

When in doubt, skip the preset and run the full interview. Presets save time; they do not save thought.
