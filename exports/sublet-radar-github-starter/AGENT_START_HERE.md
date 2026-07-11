# Agent Start Here

You are working on NYC Sublet Radar.

Read these files before making changes:

1. `README.md`
2. `docs/00_BIG_PICTURE.md`
3. `docs/01_BUILD_DOCTRINE.md`
4. `docs/02_V0_SPEC.md`
5. `docs/03_PRE_V0_VALIDATION.md`
6. `AUTONOMY_LAYER.md`

Do not implement V0 infrastructure until `docs/PRE_V0_VALIDATION.md` exists and contains an explicit PASS note from Marcus.

## First Implementation Target

If validation has passed, the first build target is:

- scaffold Python project
- define SQLite schema
- create local sample-ingest path from `data/manual/raw-listings.md`
- normalize sample listings into JSON
- write results into SQLite
- produce `data/digests/digest-YYYY-MM-DD.md`

Do not start with Telegram, VPS deployment, or background services.

