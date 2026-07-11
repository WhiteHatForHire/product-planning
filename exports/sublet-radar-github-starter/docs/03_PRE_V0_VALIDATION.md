# Pre-V0 Manual Validation

Do this before building infrastructure.

The goal is to answer:

> Does AI triage materially improve the search?

## Setup

1. Create a dedicated Gmail inbox for sublet search.
2. Subscribe to:
   - Craigslist saved-search email alerts
   - Listings Project
   - Leasebreak alerts if available
   - Roomi / SpareRoom alerts if useful
3. Add Reddit RSS feeds:
   - `r/NYCapartments`
   - `r/sublets`
   - `r/AskNYC` if relevant
4. Manually paste any Facebook/Slack/Discord listings into a local note. Do not automate reads.

## Wait

Let the inbox accumulate for 48 hours.

## Collect

Copy 20 real listings into:

```text
data/manual/raw-listings.md
```

Use this format:

```markdown
## Listing 001

Source:
URL:
Raw text:

---
```

## Manual Prompt Run

Run the Normalizer prompt from `docs/04_PROMPTS.md` on all 20 listings.

Run the Evaluator prompt on the normalized output.

Run the Drafter prompt on the top 5.

## Pass/Fail

Create `docs/PRE_V0_VALIDATION.md` with:

```markdown
# PRE_V0_VALIDATION

Status: PASS | FAIL
Date:
Listings reviewed:
Useful shortlist count:
Usable draft count:
Decision:
Notes:
```

Pass only if:

- at least 5 plausible shortlist items appear
- at least 3 drafts are usable with light editing
- the process feels faster/better than manual search alone

If fail, tune prompts before building anything.

