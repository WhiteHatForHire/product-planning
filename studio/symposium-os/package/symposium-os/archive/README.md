# archive/

**Internal historical material.** Files in this directory are preserved verbatim from prior canonical versions. They contain operator-specific names, project-specific references, and unredacted history from the period before v2.1 canonical generalization. Do not publish or share externally without redaction; this material is for internal reference only.

Historical canonical versions of `AUTONOMY_LAYER.md` (and `META_PROMPT.md` if archived separately). Preserved verbatim for reference.

## Why archive

- **Projects on older canonical** need access to their original version when diffing for an upgrade.
- **The CHANGELOG.md** references prior versions; the archive is where those references resolve.
- **Audit trail**: future operators evaluating Symposium OS can read how the protocol evolved over time.

## Convention

- One file per minor version: `AUTONOMY_LAYER-v[X.Y].md`.
- Files are immutable. Do not edit. If a typo is found in a historical version, add a footnote in the current canonical's `CHANGELOG.md` entry rather than rewriting history.

## Currently archived

- `AUTONOMY_LAYER-v1.3.md` — first reusable canonical edition stripped of project-specific stack assumptions. **Predates v2.1 generalization; contains operator-specific names and references.**
- `AUTONOMY_LAYER-v2.1.md` — last version before the docs-only smoke clarification and explicit no-halt-between-phases language landed in v2.2.

## Pending archives

When the canonical bumps from v2.2 to a future version, copy the current `template/AUTONOMY_LAYER.md` into `archive/AUTONOMY_LAYER-v2.2.md` before updating the template.

Earlier versions (v1.4, v2.0) that existed in operator-side history but were never published as standalone canonical artifacts may be added here retroactively if the operator preserves them; otherwise the `CHANGELOG.md` is the only record of those intermediate versions.
