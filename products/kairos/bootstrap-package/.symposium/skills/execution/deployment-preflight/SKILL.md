---
name: deployment-preflight
category: execution
trigger: Before any deploy to production, staging, or new environment.
---

# Deployment Preflight

## Purpose
Catch environment, secret, and target mistakes before they cause a broken or wrong-environment deploy.

## When to invoke
- Before merging a PR that auto-triggers a production deploy
- Before manually running `vercel --prod`, `fly deploy`, or equivalent
- After adding any new environment variable or secret
- After changing hosting target (e.g., subdomain, new project)

## Inputs
- Target environment (production, staging, preview)
- Deploy command
- Expected env vars
- Expected health endpoint
- Expected post-deploy smoke check

## Process
1. Verify correct working directory (`pwd` matches expected repo root).
2. Verify correct project / app ID (Vercel project, Fly app, Supabase project).
3. Verify hosting target (production vs preview).
4. Verify all required env vars are present in the target environment.
5. Verify all required secrets are present (and not expired).
6. Verify API health endpoint is live in target environment (curl + expected response).
7. Verify frontend API base URL is baked into the build (not pointing at localhost or wrong environment).
8. Verify auth provider and callback URLs are configured for the target environment.
9. Verify CORS origin list includes the deploying domain.
10. Verify build command is correct.
11. Define post-deploy smoke command. Confirm it can be run.
12. Produce preflight checklist with checkmarks or fails.

## Output
A markdown checklist showing pass/fail for each item, with the deploy command staged at the bottom (commented out if any check failed).

## Stop conditions
- Halt the deploy if any check fails. Investigate. Fix. Rerun preflight.
- Halt if production is currently degraded and the deploy is not a rollback.

## Related
- `AUTONOMY_LAYER.md` section 0.5 (credentials preflight)
- `AUTONOMY_LAYER.md` section 1.8 (deployment posture)
- `skills/review/build-report-ledger` (often run right after preflight on successful deploy)
