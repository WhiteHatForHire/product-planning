---
name: api-surface-diagnostic
category: diagnostics
trigger: Before any frontend, mobile, or integration wave that touches backend APIs.
---

# API Surface Diagnostic

## Purpose
Prevent spec-reality drift between frontend and backend before any wave touches API shapes.

## When to invoke
- Starting a frontend or mobile feature that calls existing APIs
- Suspect the spec is ahead of or behind the actual route handlers
- Before generating a frontend directive that depends on backend behavior

## Inputs
- Repo path
- List of suspected route paths
- Frontend scope (which screens or flows are affected)

## Process
1. Read actual route handlers in the repo. Do not guess from the spec.
2. List endpoints with HTTP method, path, auth requirement, runtime (edge vs node).
3. Document request body shape (Zod schema if present; otherwise extract from runtime validation or destructuring).
4. Document response body shape (success and error variants).
5. Document error response codes and their conditions.
6. Identify any deltas from the spec.
7. Produce truth table.

## Output
A markdown truth table:

```
| Endpoint | Method | Auth | Runtime | Request | Response | Error | Spec delta |
```

Plus a "Spec deltas" section listing each mismatch.

## Stop conditions
- No frontend or mobile wave may begin until the truth table exists for backend-dependent work.
- Halt if route handlers reference modules or types that do not exist. Backend is in an inconsistent state and needs a backend wave first.

## Related
- `AUTONOMY_LAYER.md` section 1.13 (spec-reality reconciliation)
- `skills/diagnostics/ics-feed-diagnostic` (analogous skill for upstream feed sources)
