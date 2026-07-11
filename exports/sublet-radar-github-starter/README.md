# NYC Sublet Radar

NYC Sublet Radar is a white-hat housing-search assistant for short-term NYC sublets.

It does not scrape hostile platforms, does not automate outbound messages, and does not try to replace the human trust signal that gets someone to hand over keys. It collects legal/opt-in listing signals, normalizes them, scores them against Marcus's actual preferences, and produces a daily shortlist with reply drafts. Marcus reviews and sends from the original platform.

The product thesis is simple:

> The durable consumer-agent pattern is filter plus human closer.

## What V0 Does

- Ingests listings from a dedicated Gmail inbox, RSS feeds, and manual paste files.
- Normalizes raw listing text into structured JSON.
- Scores listings for fit, trust, speed, and scam risk.
- Deduplicates seen listings.
- Produces a daily digest with top listings, reasons, red flags, and reply drafts.
- Keeps outbound human-only.

## What V0 Does Not Do

- No Facebook scraping.
- No Craigslist page scraping.
- No anti-detect browsers, proxy fleets, captcha solving, or account automation.
- No automated messaging.
- No marketplace, payments, multi-user accounts, or SaaS productization.

## Start Here

1. Read [docs/00_BIG_PICTURE.md](docs/00_BIG_PICTURE.md).
2. Run the manual validation in [docs/03_PRE_V0_VALIDATION.md](docs/03_PRE_V0_VALIDATION.md).
3. If validation passes, build from [docs/02_V0_SPEC.md](docs/02_V0_SPEC.md).
4. Any autonomous agent must follow [AUTONOMY_LAYER.md](AUTONOMY_LAYER.md).

## Recommended Stack

- Python 3.11+
- SQLite
- Gmail IMAP or Gmail API
- RSS via `feedparser`
- Anthropic API or compatible LLM provider
- Markdown digest first; Telegram bot optional after the core loop works

