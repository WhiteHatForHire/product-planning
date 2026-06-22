---
name: deployment-preflight
category: execution
trigger: Before any deploy to production, staging, or a new environment.
---

# Deployment Preflight

## Purpose
Catch environment, secret, and target mistakes before they cause a broken or wrong-environment deploy.

## When to invoke
- Before merging a PR that auto-triggers a production deploy
- Before manually running the deploy command for production
- After adding any new environment variable or secret
- After changing the hosting target (subdomain, new project ID, new environment)
- Before the first deploy to any new environment

## Inputs
- Target environment (production, staging, preview, or named environment)
- Deploy command (per `AUTONOMY_LAYER.md` section 0.1)
- Expected env vars
- Expected secrets and their location
- Expected health endpoint
- Expected post-deploy smoke check

## Process
1. Verify correct working directory (`pwd` matches expected repo root).
2. Verify correct project / app ID for the hosting platform.
3. Verify hosting target (production vs staging vs preview).
4. Verify all required env vars are present in the target environment.
5. Verify all required secrets are present (and not expired or rotated).
6. Verify API health endpoint is live in the current target environment if applicable (a request returns the expected response).
7. Verify frontend API base URL is baked into the build pointing at the correct environment (not localhost, not the wrong environment).
8. Verify auth provider and callback URLs are configured for the target environment.
9. Verify CORS origin list includes the deploying domain.
10. Verify build command matches `AUTONOMY_LAYER.md` section 0.1.
11. Define post-deploy smoke command. Confirm it can be run from the operator's environment.
12. Produce preflight checklist with pass/fail per item.

## Output
A markdown checklist showing pass/fail for each item, with the deploy command staged at the bottom (commented out if any check failed).

## Stop conditions
- Halt the deploy if any check fails. Investigate. Fix. Rerun preflight.
- Halt if production is currently degraded and the deploy is not an explicit rollback.
- Halt if the deploy would change a production environment variable as part of the deploy. Environment variable changes are operator-only per `AUTONOMY_LAYER.md` section 1.8 and must land before the code that depends on them.

## Related
- `AUTONOMY_LAYER.md` section 0.5 (credentials preflight)
- `AUTONOMY_LAYER.md` section 1.8 (deployment posture)
- `AUTONOMY_LAYER.md` section 1.11 (production safety boundaries)
- `skills/review/build-report-ledger` (often run right after preflight on successful deploy)
