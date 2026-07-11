# V0 Spec

## Objective

Build a local-first or small-VPS Sublet Radar that processes legal/opt-in listing sources and produces a daily digest with ranked listings and reply drafts.

## Stack

Default:

- Python 3.11+
- SQLite
- Markdown files for manual input/output
- Gmail IMAP for inbox ingestion
- RSS via `feedparser`
- Anthropic API for normalization/scoring/drafting
- Telegram optional after Markdown digest works

Avoid:

- web app
- frontend
- SaaS auth
- Postgres
- background task framework unless needed
- containerization before a working local loop

## Directory Structure

```text
sublet-radar/
  README.md
  AUTONOMY_LAYER.md
  AGENT_START_HERE.md
  requirements.txt
  .env.example
  data/
    manual/
      raw-listings.md
    digests/
    listings.db
  docs/
    00_BIG_PICTURE.md
    01_BUILD_DOCTRINE.md
    02_V0_SPEC.md
    03_PRE_V0_VALIDATION.md
    04_PROMPTS.md
    PRE_V0_VALIDATION.md
    deferred-issues.md
  src/
    sublet_radar/
      __init__.py
      db.py
      schema.sql
      ingest_manual.py
      ingest_imap.py
      ingest_rss.py
      normalize.py
      score.py
      draft.py
      digest.py
      models.py
      config.py
  tests/
    fixtures/
      sample_listings.md
      normalized_listing.json
    test_normalize.py
    test_score.py
    test_digest.py
```

## Data Model

Single table is enough for V0.

```sql
CREATE TABLE IF NOT EXISTS listings (
  id TEXT PRIMARY KEY,
  source TEXT NOT NULL,
  source_id TEXT,
  url TEXT,
  title TEXT,
  raw_text TEXT NOT NULL,
  neighborhood TEXT,
  borough TEXT,
  price_total INTEGER,
  price_per_night INTEGER,
  dates_start TEXT,
  dates_end TEXT,
  furnished TEXT,
  room_type TEXT,
  contact_method TEXT,
  trust_score INTEGER,
  fit_score INTEGER,
  urgency_score INTEGER,
  scam_risk_score INTEGER,
  overall_score INTEGER,
  status TEXT DEFAULT 'new',
  reasons_json TEXT,
  red_flags_json TEXT,
  reply_draft TEXT,
  first_seen_at TEXT NOT NULL,
  last_seen_at TEXT NOT NULL,
  raw_hash TEXT NOT NULL
);
```

## Module 1: Ingest + Normalize

Inputs:

- `data/manual/raw-listings.md`
- Gmail inbox
- RSS feeds

Output:

- rows in SQLite
- normalized fields
- logged fallback if LLM unavailable

V0 order:

1. manual paste
2. RSS
3. Gmail IMAP

## Module 2: Score + Flag

Score dimensions:

- date fit
- price fit
- neighborhood fit
- commute/usefulness
- trust signal
- scam risk
- reply urgency
- overall fit

Use 0-100 integer scores. Store reasons and red flags as JSON.

## Module 3: Digest + Draft

Output Markdown first:

```text
data/digests/digest-YYYY-MM-DD.md
```

Each shortlist item includes:

- title
- source
- link
- price
- dates
- neighborhood
- overall score
- why it fits
- red flags
- recommended action
- reply draft

Telegram comes after Markdown digest works.

## V0 Acceptance Criteria

Automated:

- tests pass
- SQLite schema initializes idempotently
- sample raw listing normalizes into expected fields
- scoring returns bounded integer scores
- digest file is generated from fixture listings
- forbidden platform adapters/imports are absent

Human:

- scoring feels directionally right
- digest is useful on phone
- reply drafts sound like Marcus
- scam flags catch obvious bad listings

