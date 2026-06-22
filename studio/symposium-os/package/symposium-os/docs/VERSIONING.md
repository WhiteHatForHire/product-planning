# Versioning Policy

Symposium OS uses semantic-ish versioning for `AUTONOMY_LAYER.md` and `META_PROMPT.md`. Skills, templates, and documentation are not individually versioned; they track the canonical release.

---

## Version format

`MAJOR.MINOR`

- **Major** bumps for incompatible protocol changes. Projects must do a deliberate migration.
- **Minor** bumps for additive doctrine, new sections, new skills, new self-repair entries.

Patch numbers are not used. Typo fixes and clarifications ship as part of the next minor release.

---

## When to bump major

- A `NEVER` rule changes meaning.
- The tier system (Tier 1 / 2 / 3) changes.
- An existing protocol section's contract changes (not additions — actual semantic changes).
- A file convention changes that requires every project to rename or restructure.

Major bumps are rare and disruptive. Avoid unless the existing protocol is genuinely broken.

---

## When to bump minor

- A new doctrine section is added (e.g., section 1.15 was added in v2.0).
- A new sub-section is added to an existing section (e.g., sequential merge maintenance was added in v2.1).
- A new generic self-repair entry is added (e.g., `GENERIC-12`).
- A new canonical skill is added.
- A new template scaffold is added.

Minor bumps should always be additive. Projects on an older minor should be able to upgrade without breaking changes.

---

## Versioning the template

The `template/` directory carries the canonical version in two places:
- `template/AUTONOMY_LAYER.md` header line
- `template/META_PROMPT.md` header line

Both must match. The version is the same number; they ship together.

Skills, templates, and the in-template README do not carry version numbers. They reflect the canonical version of `AUTONOMY_LAYER.md` at the time of their commit.

---

## Versioning projects

Each project's copy of `.symposium/AUTONOMY_LAYER.md` carries the version it was last upgraded from. To check a project's current version, read the header of `.symposium/AUTONOMY_LAYER.md`.

Projects do NOT need to upgrade on every canonical release. Upgrade when:
- A new skill solves a problem the project is hitting.
- A new self-repair entry addresses a failure mode the project has seen.
- The operator wants the new doctrine sections (e.g., adopting v1.15 sequential merge maintenance after starting to stack PRs).

There is no penalty for staying on an older minor as long as the protocol is working for the project.

---

## Upgrade procedure

To upgrade a project from canonical version `vX.Y` to `vX.Z`:

1. **Read the changelog.** Note new sections, new self-repair entries, new skills.
2. **Diff the protocol.** Compare `.symposium/AUTONOMY_LAYER.md` against `template/AUTONOMY_LAYER.md` at the new canonical. Apply all additions. Preserve section 0.1 (stack) and section 2.3 (project-specific repair entries) verbatim.
3. **Diff `META_PROMPT.md`.** Apply changes if any.
4. **Diff skills.** Apply additions and improvements. Preserve any project-specific skill variants under `skills/[category]/[project-specific-name]/`.
5. **Diff templates.** Apply additions. Preserve project-specific template variants if any.
6. **Update the header version line** in both `AUTONOMY_LAYER.md` and `META_PROMPT.md` to the new canonical.
7. **Commit**: `chore(symposium): upgrade to canonical v[X.Z] — [one-line summary of what changed]`.

For major version upgrades, the operator may also need to:
- Rewrite project-specific repair entries that referenced superseded protocol sections.
- Re-read every project ADR to confirm none was invalidated by the protocol change.
- Re-run `POST_INIT_CHECKLIST.md` to confirm the upgraded project still passes.

---

## How the canonical itself versions

When canonical changes:

1. **Author** the changes on a branch in the Symposium OS repo.
2. **Update** `template/AUTONOMY_LAYER.md` and `template/META_PROMPT.md` header version lines.
3. **Archive** the previous canonical: copy the old `AUTONOMY_LAYER.md` to `archive/AUTONOMY_LAYER-v[X.Y].md`.
4. **Changelog**: append a section to `CHANGELOG.md` describing what changed, what migration is required (if any), and which existing projects are affected.
5. **Meta-ADR (optional)**: if the change reflects a meaningful architectural decision about Symposium OS itself, write a meta-ADR in `meta-adr/`.
6. **Commit**: `chore(canonical): v[X.Y] — [one-line summary]`.
7. **Tag** the commit with `v[X.Y]`.
8. **Notify** all projects that an upgrade is available. (The operator handles this manually; there is no automatic notification.)

---

## What is NOT versioned

- Individual skills (they evolve in place; the canonical version they ship with is the reference)
- The in-template `README.md`
- The `CONTEXT.md` template
- The scaffold templates in `template/templates/`
- ADRs (each ADR is its own immutable record)
- Documentation in `docs/`
- Case studies in `case-studies/`

These all track the canonical release. They are at "current canonical" by definition.
