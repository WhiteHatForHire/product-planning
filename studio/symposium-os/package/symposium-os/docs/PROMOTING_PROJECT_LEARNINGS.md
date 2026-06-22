# Promoting Project Learnings

Each project using Symposium OS appends its own repair entries, its own skills, and its own conventions. None of this flows back to canonical automatically. This document covers when and how a project-specific learning earns canonical promotion.

---

## The rule of three

A pattern promotes from project-specific to canonical when it has been applied successfully across three or more projects.

- **Once** is an experiment.
- **Twice** is a coincidence.
- **Three times** is a method.

The threshold is intentional. It prevents canonical bloat from patterns that worked once and stopped working when the context changed. It also forces the operator to apply the pattern across distinct domains before treating it as universal.

---

## What can be promoted

### Self-repair entries (section 2.3)
A project-specific repair entry that has fired and resolved a failure mode across three projects → promote to a `GENERIC-N` entry in section 2.1.

### Skills
A project-specific skill that has been invoked successfully across three projects → promote to `template/skills/[category]/[name]/`.

### Doctrine sections
A pattern that's appeared as inline directive instruction across three projects, with no skill capturing it → consider whether it belongs as a new section in `AUTONOMY_LAYER.md` (minor version bump) or as a new skill.

### Templates
A project-specific template variant used in three projects → promote to `template/templates/`.

### Stack presets
The rule of three applies here too. After three projects with the same stack and the same init answers, codify as a `stack-presets/*.yml`.

---

## What cannot be promoted

- **ADRs**: every ADR is project-specific by definition. ADRs about Symposium OS itself live in `meta-adr/`. Project ADRs never promote.
- **CONTEXT.md entries**: ubiquitous language is per-project. The shared Symposium terms in `CONTEXT.md` are already canonical; project-specific terms stay project-specific.
- **Project-specific patterns that depend on a particular stack**: a pattern that only works in Next.js does not promote even if used across three Next.js projects. It belongs in a stack preset's documentation or a stack-specific addendum.

---

## Promotion procedure

When a project-specific pattern meets the rule of three:

1. **Identify the three projects**. Write down which projects applied the pattern, when, and what the outcome was. This is the evidence.

2. **Generalize the pattern**. Strip project-specific names, paths, stack assumptions. The promoted version must work in projects beyond the three that demonstrated it.

3. **Cross-check against existing canonical**. Does an existing skill or section already cover this? If so, the pattern is a refinement to an existing artifact, not a new one. Update the existing artifact instead.

4. **Open a PR against the Symposium OS repo**. Include:
   - The new or updated canonical artifact (skill, section, template, preset)
   - A reference to the three project applications as evidence
   - A note in `CHANGELOG.md` for the next minor version
   - A meta-ADR if the promotion reflects a meaningful architectural decision about the OS itself

5. **Bump the canonical version** per `VERSIONING.md`.

6. **Tag and publish** the new canonical.

7. **Notify** the projects that applied the original pattern. They can choose to upgrade and replace their project-specific version with the canonical reference.

---

## Demoting from canonical

Occasionally a canonical pattern proves wrong, brittle, or superseded by a better pattern.

To demote:

1. **Write a meta-ADR** explaining what went wrong, what's replacing it, and what existing projects should do.
2. **Mark the canonical artifact as deprecated** in its file (header note).
3. **Ship the replacement** (if any) in the next canonical release.
4. **Remove the deprecated artifact** in a subsequent release (one minor cycle later, to give projects time to migrate).

Demotion is rare. Most patterns don't fail; they just stop being relevant. Demote only when the pattern is actively harmful or misleading.

---

## Anti-patterns in promotion

- **Promoting from one project's experience**. Even if the pattern is brilliant, it hasn't proven generality. Wait for the second and third application.

- **Promoting under deadline pressure**. "I need this skill in the canonical so my next project gets it for free." The next project will be the second application, not the third. Wait.

- **Promoting a project's specific implementation**. The canonical version must be generalized. A skill that hardcodes a Next.js path is project-specific, not canonical.

- **Promoting because it would be elegant**. Elegance is not evidence. Three working applications across distinct projects is evidence.

- **Skipping the meta-ADR for architectural promotions**. If the promotion shapes how the OS works, document the decision. Future operators need to understand why the canonical is shaped this way.

---

## What happens to the project-specific version after promotion

After a pattern promotes to canonical:

- **In future projects**: copy from the new canonical. The project-specific version no longer exists; it's been absorbed.
- **In the three originating projects**: the operator can choose to keep the project-specific version (for stability) or replace it with the canonical reference (for simpler maintenance).

The project-specific version does not auto-update when canonical updates. Each project remains in control of its own copy.

---

## Tracking promotion-eligible patterns

A pattern is promotion-eligible when:
1. It has appeared in two or more projects.
2. The operator suspects it would help a third.

Track these patterns in `docs/PROMOTING_PROJECT_LEARNINGS.md` (this file) under a "Watching" section, or in a private operator note. When the third project hits the pattern naturally, promote.

Do not actively force a pattern into a third project just to clear the rule of three. Forced application masks whether the pattern is genuinely general or whether it only seemed general after seeing it twice.
