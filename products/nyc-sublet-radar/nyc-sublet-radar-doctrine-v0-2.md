---
title: "nyc sublet radar doctrine v0.2"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /NYC Sublet Radar/Active/nyc-sublet-radar-doctrine-v0.2.docx"
status: active
privacy: working
tags:
  - product
---

# nyc sublet radar doctrine v0.2

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
NYC SUBLET RADAR

Build Doctrine v0.2

Eagle Rocket LLC

1. Phronesis Check

Before architecture, the practical-wisdom question.

Anchor V4 is mid-pivot from feature work to production. Year one of sobriety has a stated no-new-entrepreneurial-commitments rule. This document exists because the sublet radar can be built in two registers.

Side quest dressed as need. Time pulled from Anchor, agent credit burn, half-finished system. Bad outcome.

Cofounder-grade portfolio piece executed lean. A working consumer-agent prototype on a hostile-information problem. Demonstrates the fCTO thesis. Good if the budget is honest and Anchor stays primary.

The cleanest framing: this is a probe. If it ships at v0 and finds a workable sublet, win. If it stalls, the architecture document survives as a portfolio reference. Treat it like the Momoyo evaluation: study the structure, do not buy the franchise.

The hard constraints that make this safe to build are in Section 2. Read them before the architecture.

2. Hard Build Boundary

This box is a tripwire. It overrides all good intentions.

HARD BUILD BOUNDARY

Maximum build budget:   5 sessions. No exceptions.

Maximum spend:          $100 infra + LLM before a review gate.

Priority lock:          No session starts until the Anchor priority block is done.

Time boundary:          No work after 9pm.

Scope lock:             No v0.5 work until v0 has helped find a real sublet.

Kill authority:         If any kill criterion in Section 3 is hit, the build stops.

Stated in prose, boundaries are good intentions. Stated in a box this size, they are architecture.

3. Success and Kill Criteria

v0 Success Criteria

All five required before v0.5 work is authorized.

At least 30 real listings ingested from live sources.

At least 10 correctly normalized to structured JSON.

At least 5 plausible shortlist items surfaced.

At least 3 usable reply drafts produced.

Operator sends at least 1 real reply from the original platform, from a draft produced by the system.

Kill Criteria

Any single item stops the build.

Setup exceeds 5 focused sessions without a working digest.

More than $100 spent without real listings flowing.

No listings flowing after inbox and RSS are configured.

Anchor production closure is displaced by a build session.

Build sessions are creeping into late-night or consuming morning priority time.

The kill criteria exist to protect against "it is almost working" purgatory. Almost working is not working. If a kill criterion is hit, the doctrine document stays. The build stops.

4. Problem Statement

The operator is in Gili Air and wants a one-week to one-month NYC base for a field-test sprint. The market is fragmented across Craigslist, Facebook housing groups, Listings Project, Leasebreak, Roomi, SpareRoom, Reddit threads, and a long tail of Substack, Slack, and Discord channels.

The friction is not finding listings. The friction is signal-to-noise (scams, ghost listings, mismatched neighborhoods), speed of human response, and being a legible-enough stranger that a leaseholder hands over keys.

The product is not a scraper. The product is a sublet radar that does cognitive triage and hands a curated shortlist plus drafted replies to the operator. The operator presses send.

5. The Three Routes

White Hat

Legal sources only. Email alerts, RSS, opt-in newsletters, partner APIs, user-pasted links. Agent scores, dedupes, drafts, and digests. Human sends every message. Zero ToS exposure, zero ban risk, full trust signal preserved. This is the build.

Gray Hat

Same as above plus light reads of sites whose ToS is ambiguous or whose anti-bot posture is thin: Reddit JSON endpoints, public Substack archives, certain aggregators. Still no automated outbound. Modest risk profile, mostly contractual. Extension of v0 if a specific source justifies it.

Adversarial / Black Hat

Active scraping and automated messaging against FB Marketplace, CL, and similar. Documented separately in Section 8 as a rejected approach. Not a build target.

6. White Hat Stack (full landscape)

Ingestion sources

Craigslist saved-search email alerts (multiple per neighborhood and price band)

Listings Project weekly email

Leasebreak email alerts

Roomi and SpareRoom alerts

Reddit RSS for r/NYCapartments, r/AskNYC, r/sublets

NYC sublet Substacks

User-pasted FB Marketplace and FB group links (manual collection, agent processes the paste)

Curated Slack and Discord channels where invited

Processing layer

IMAP poller or forwarding rules into a dedicated inbox

RSS poller (small Python cron, or Feedly/Inoreader API)

LLM extraction agent turning raw email into structured JSON

Listing CRM (SQLite for v0, Postgres if it ever needs to be multi-user)

LLM scoring and drafting agents

Daily digest to Telegram bot (recommended) or email fallback

Outbound

Drafts only. Human reviews and sends from the original platform, on the original account, in their own voice, lightly edited from the agent draft.

Why this is the real architecture

Zero ToS violations and zero captcha wars

Zero ban risk on the operator's real accounts

Trust signal to leaseholder is preserved (human-sent reply)

Defensible as a portfolio piece

Scales cleanly into a multi-user product if that decision is made later

7. Gray Hat Stack

Where the platform allows or tolerates light reads:

Reddit JSON endpoints via OAuth, low volume

Public Substack archives (typically scraping-tolerant)

Listings Project public archive

Aggregator sites with no aggressive anti-bot

Tools: Firecrawl, ScrapingBee, or BrowserUse for managed reads. Standard Playwright or Puppeteer otherwise. Residential proxies optional, usually not required at this volume. Outbound still human-only.

8. Rejected Approach: Adversarial Scraping and Automated Outbound

The full technical stack for active scraping and automated messaging against FB Marketplace and CL (anti-detect browsers, residential proxies, aged accounts, behavioral simulation, captcha-solving services) has been reviewed and is documented separately in the conversation record for landscape literacy.

The conclusion:

The adversarial counter-detection stack costs $200 to $500 per month in tooling alone, requires 30 to 60+ engineering hours to build, and requires ongoing maintenance against silent detection updates.

Write actions (messaging) trigger spam classifiers stacked on top of bot classifiers. This is where accounts burn.

The trust signal to the leaseholder is eliminated the moment a bot sends the message. In a market where a stranger is deciding who gets their keys, that is not a recoverable loss.

For a single sublet, the white-hat path produces better outcomes per hour by a large margin.

Eagle Rocket LLC is a real entity with real legal exposure. The civil liability from ToS violations on platforms that actively sue scrapers attaches to the LLC, not to an anonymous actor.

The adversarial approach is interesting as a landscape artifact. It is not a build target and it is not a portfolio item. The conclusion it surfaces is the whole point: the filter-plus-human-closer pattern is durable precisely because the adversarial path is not.

9. Detection Mechanisms

Understanding what platforms see explains why the white-hat approach is not a compromise but an architectural advantage.

Network signals

IP reputation, ASN reputation, TLS fingerprint (JA3/JA4), HTTP/2 fingerprint, request rate, geographic consistency with the account's prior login history.

Browser signals

Canvas fingerprint, WebGL fingerprint, audio context fingerprint, font enumeration, screen resolution, timezone, language, plugin list, navigator.webdriver flag, presence or absence of chrome.runtime, WebRTC local IP leak.

Behavioral signals

Mouse-movement entropy, typing cadence, scroll velocity, page dwell time distribution, click target distribution, navigation paths.

Account graph signals

Account age, friend graph density, posting history, login locations, device history, phone number reputation, cross-account fingerprint overlaps. Meta runs ML over the joint distribution of all of the above. A fleet of synthetic profiles looks like a fleet.

A human with a real account using the platform naturally, pasting one URL into a Telegram channel, generates no signals worth detecting.

10. Legal Landscape

Three legal theories matter when scraping platforms at scale:

Computer Fraud and Abuse Act (CFAA). Federal anti-hacking statute. The hiQ Labs v. LinkedIn line established that scraping technically public data probably does not violate CFAA. Case law is still evolving.

Breach of contract. Civil liability for ToS violations. Platforms have sued and won on this theory. Meta has filed and settled multiple suits against scrapers including commercial data brokers.

Tortious interference and unfair competition. State-law claims that often stack on top of contract claims.

Practical exposure for an LLC operator: even a successfully defended suit costs six figures. Discovery is invasive. A federal subpoena to a VPS provider produces server logs. Insurance does not cover intentional ToS violations. The white-hat plan carries effectively zero legal exposure.

11. Source Inventory

White-hat sources ranked by signal-to-noise for NYC short-term sublets:

Listings Project. Curated, low volume, high signal, weekly email. Best single source.

Craigslist email alerts. High volume, medium signal. Requires aggressive scoring.

Leasebreak. Purpose-built for sublets and lease breaks. Medium volume.

Roomi. Roommate and room-share focused.

SpareRoom. Larger, more national, decent NYC coverage.

Reddit r/sublets, r/NYCapartments, r/AskNYC. Variable signal, occasional gems.

NYC sublet Substacks. Hyper-curated, low volume.

Friend-of-friend Slack and Discord channels. Highest trust signal, hardest to find.

FB Marketplace and FB groups, manual save only. High volume, high noise.

Each source gets a dedicated feed adapter in the Scout module. Adapters are thin and isolated.

12. Six-Agent Architecture: Conceptual Model

This is the full architectural vision. It describes the system at maturity. The v0 build uses a simplified three-module version of this (see Section 13), but the six-agent model is the correct mental scaffold and the portfolio artifact.

Agent 1: Scout

Polls each ingestion source. IMAP fetch, RSS pulls, user-pasted URL queue. Outputs raw listing payloads to the Normalizer.

Agent 2: Normalizer

Takes raw payload, outputs structured JSON: source, title, url, neighborhood, borough, price, dates, room type, furnished status, transit notes, contact method, raw text, photos present, posted at.

Agent 3: Evaluator

Scores each normalized listing 0 to 100 against the criteria in Section 15. Outputs score, reasons, and risk_flags. Runs scam-pattern checks from Section 16.

Agent 4: Drafter

For listings above the score threshold, generates a human-sounding reply that references two or three specific details from the listing. Avoids AI tells.

Agent 5: Review Queue

Pushes the daily shortlist to a Telegram channel. Each item carries top-line summary, score, reasons, risk flags, drafted reply, and a one-tap link to the original listing.

Agent 6: Memory / Deduper

Maintains persistent state. Hermes MEMORY.md and USER.md for preferences and patterns. Listing-level history in SQLite, not in agent memory, because volume exceeds the intended memory scope.

13. v0 Build Modules: Three-Module Implementation

For v0, the six-agent model collapses to three modules. Less ceremony, faster to a working digest.

Module 1: Ingest and Normalize

Combines Scout and Normalizer. IMAP fetch plus RSS polling, LLM extraction, writes to SQLite. One cron job per source type.

Module 2: Score and Flag

Combines Evaluator and Memory/Deduper. Scoring prompt, scam pattern detection, dedup check against seen listing IDs. Marks status in the database.

Module 3: Digest and Draft

Combines Drafter and Review Queue. Drafts for shortlisted listings, pushes daily Telegram digest with score, reasons, draft, and link.

When v0 is working and the kill criteria are cleared, the three modules can be refactored into the six-agent model for v0.5. Do not pre-optimize.

14. Data Model

Single listings table is enough for v0.

Field

Type

Notes

id

uuid

primary key

source

text

listings_project, craigslist, leasebreak, reddit, etc.

source_id

text

platform's listing ID, for dedup

url

text

original listing URL

title

text

listing title or summary line

neighborhood

text

parsed, normalized to canonical names

borough

text

parsed

price_total

int

for the full stay

price_per_night

int

normalized

dates_start

date

dates_end

date

room_type

text

private_room / studio / 1br / etc.

furnished

bool

photos_present

bool

raw_text

text

full original listing body

score

int

0-100, from Evaluator

reasons

text

LLM rationale

risk_flags

text[]

scam patterns triggered

status

text

new / shortlist / contacted / viewing / dead

draft_reply

text

contacted_at

timestamp

created_at

timestamp

updated_at

timestamp

Indexes: (source, source_id) for dedup, status for queue queries, score for ranking.

15. Scoring Criteria

Must-have (auto-reject if missing)

NYC or close-in Brooklyn/Queens

Short-term flexibility (1 week to 1 month)

Workable WiFi mentioned or reasonably inferable

Private room minimum

Clear photos of the actual unit

Identifiable host (real name, account history, or platform verification)

Strong positives

Furnished

Within 15 minutes walk of subway

Below price ceiling (set per sprint; $1,500/mo for a private room is a reasonable starting point)

Quiet or work-friendly mentioned explicitly

Host responsive (proxy: posted recently)

Week-to-month flexibility

Weak positives

Near gym or yoga

Near serviceable cafes

Interesting neighborhood

Desk or work surface in room

Auto-reject (any single flag)

Deposit before viewing

Wire transfer, Western Union, or crypto payment request

Name mismatch between listing and payment request

Stock-photo apartment images

"Kindly send payment" phrasing

Unwilling to do video tour

No physical address even at neighborhood granularity

16. Scam Detection Patterns

Classic NYC sublet scam signatures the Score and Flag module checks.

Linguistic

"Kindly", "dear", "my good friend", "blessings"

Grammar inconsistent with claimed nationality

Excessive religious framing ("God bless this transaction")

Urgency without justification ("must rent today")

Logistical

Owner is "out of the country" or "on a missionary trip"

Cannot show in person, only video, and resists requests for a live call

Deposit via Zelle, Venmo, wire, or crypto before key handoff

Price more than 30 percent below comparable units in the neighborhood

Same photos appearing on multiple listings

Listing claims furnished but photos show empty rooms

Identity

New account, no history

Profile photo is a stock image or known celebrity

Name on listing differs from name on payment request

Phone number is VOIP

Single flag: review-with-caution bucket. Two or more flags: score drops below the shortlist threshold.

17. Prompt Library

Normalizer prompt (sketch)

You extract structured data from rental listings. Input is raw email
or listing text. Output is JSON matching the schema below. Be
conservative. If a field is not stated, use null. Do not infer
aggressively.

Schema: { source, title, url, neighborhood, borough, price_total,
price_per_night, dates_start, dates_end, room_type, furnished,
photos_present, raw_text }

Handling:
- Dates: parse to ISO dates. If "ASAP" or "flexible", use null + note.
- Prices: normalize to USD per month. If weekly, multiply by 4.33.- Neighborhoods: canonical names only (Williamsburg, not "Wburg").

Evaluator prompt (sketch)

You score NYC short-term sublet listings for the operator, a
30-something remote worker visiting NYC for a one-week to one-month
sprint. Score 0-100 against the criteria below. Output JSON:
{ score, reasons, risk_flags, recommendation }.

[criteria block, Section 15]
[scam patterns, Section 16]

Recommendation values: shortlist, maybe, reject.

Be skeptical. False positives waste the operator's time more thanfalse negatives. Lean toward reject on ambiguous signals.

Drafter prompt (sketch)

You draft replies to NYC sublet listings on behalf of the operator.
The operator is a 30-something remote worker, based in Indonesia,
returning to NYC for a one-week to one-month working trip. Sober,
quiet, clean, normal sleep schedule, works on a laptop.

Reference two or three specific details from the listing so the reply
does not read as templated. Direct and warm tone. No em dashes. No
filler. Three to five sentences. Sign as the operator.

End with two specific questions: one about logistics (move-in date
confirmation, deposit terms), one about the space (WiFi speed, desksituation, neighborhood detail).

18. Infrastructure: Hermes plus VPS

Stack decision

Hermes Agent as the orchestrator. Small VPS as the always-on host. GitHub as source of truth. CC and Codex push commits, VPS pulls and restarts services via a small deploy script. Matches the Anchor workflow direction.

VPS sizing for v0

1 to 2 vCPU, 2 to 4 GB RAM is plenty

Hetzner, Vultr, or DigitalOcean at $5 to $10/mo

Ubuntu 22.04 or 24.04 LTS

Filesystem layout

/opt/sublet-radar/
  app/                  # Hermes config, prompts, tools
  data/
    listings.db         # SQLite for v0
    seen.json           # dedup cache
  logs/  .env                  # secrets

Services (systemd units)

hermes-agent.service, restart on failure

email-poller.service, IMAP fetch every 10 minutes

rss-poller.service, cron every 30 minutes

digest.service, daily at chosen hour

Secrets

IMAP credentials for a dedicated inbox (e.g., marcus.sublets@...)

Telegram bot token

Anthropic API key

Sentry DSN for error tracking

Hermes specifics to verify at setup

MEMORY.md and USER.md persistence locations on VPS

Firecrawl integration for white-hat web fetches

Tool registration syntax (read current docs, do not assume)

Token and spend ceiling configuration

19. Pre-v0: Manual Validation First

Before the VPS and Hermes setup, run the leanest possible version of the core question: does AI triage actually improve the housing search?

The manual validation flow:

Set up the dedicated Gmail inbox.

Subscribe to Craigslist alerts and Listings Project.

Wait two days for inbox to accumulate.

Export or copy 20 real listings into a text file.

Run the Normalizer and Evaluator prompts manually in Claude or ChatGPT.

Review the shortlist and drafts.

Answer the question: is this useful?

If yes, continue to the VPS and Hermes setup. If the triage is not useful (wrong criteria, poor extraction, noise dominates), fix the prompts before building infrastructure. This costs nothing and cannot fail in a way that consumes Anchor time.

This is the correct first session, not provisioning a VPS.

20. v0 Build Plan

Goal: working radar in three to five focused sessions after manual validation passes.

Session 0 (pre-v0): Manual Validation

See Section 19. Pass this before spending any infra money.

Session 1: VPS plus repo plus scaffold

Provision VPS

GitHub repo with basic structure

Install Hermes and the Python or Node runtime

Inbox already live from pre-v0

Session 2: Module 1 (Ingest and Normalize)

IMAP poller

RSS poller for Reddit and newsletter RSS

Normalizer prompt wired

Write to SQLite

Session 3: Module 2 (Score and Flag)

Scoring prompt

Scam pattern checks

Dedup against seen IDs

Test against 50+ real listings accumulated in inbox

Session 4: Module 3 (Digest and Draft)

Draft prompt

Daily Telegram digest

One-tap original listing link per item

Session 5: Hardening

Sentry wired

Dedup audit

Preference memory structure in Hermes

README in repo

Out of scope for v0

FB scraping in any form

Auto-send

Multi-user

Web UI

Any v0.5 feature

21. v0.5 Extensions

Only after v0 success criteria are cleared and Anchor is stable.

Manual FB link queue via Telegram paste

Reverse image search for photo-based scam detection

Auto-tagging of good vs. rejected listings for scoring tuning

Weekly inventory summary, this week vs. last week

Refactor three modules to six-agent model

22. v1 Roadmap

Only if a productization decision is made separately, and only if Anchor is stable.

Multi-user with per-user preference profiles

Web UI for review and one-tap reply

Partner APIs where they exist

Mobile push instead of Telegram

Subscription pricing

23. Risk Register

Build risk

Hermes integration may have edges at setup. Keep core logic in pure Python or Node, use Hermes for orchestration only.

LLM cost creep. Cap daily spend, batch where possible, use cheaper models for normalization.

Operational risk

VPS goes down. Systemd auto-restart plus weekly health-check ping.

Inbox fills with scam noise before scoring is calibrated. Aggressive rejection threshold.

Personal risk

Side-quest creep into Anchor time. The tripwire in Section 2 is the answer.

Scope expansion. This document is the boundary. v0 is the scope.

Legal risk under the white-hat plan

Effectively zero. Email alerts, RSS, opt-in newsletters, and user-pasted links are not actionable.

24. Cost Comparison

Item

White Hat

Adversarial

VPS

$5-10/mo

$5-10/mo

LLM credits

$20-50/mo

$20-50/mo

Anti-detect browser

$0

$99-200/mo

Residential proxies

$0

$50-300/mo

Aged accounts

$0

$50-300 setup

Captcha credits

$0

$5-20/mo

Engineering hours

10-15 hrs

30-60+ hrs

Ongoing maintenance

low

high (detection updates)

Ban risk

0

high

Legal exposure

0

meaningful

Trust signal to host

preserved

eliminated

Effectiveness for one sublet

strong

marginal

White hat dominates on every axis at this scale. "Trust signal to host" is the row that matters most. That is not a nice-to-have. It is why the sublet gets found.

25. Recommended Plan

Before anything: manual validation (Section 19). Two days of inbox accumulation, 20 listings, local prompt run. If useful, continue.

Build v0 over four to five focused sessions on the VPS plus Hermes stack. Three-module implementation. Drafts only. Use it to find a real NYC sublet.

If v0 ships and works, hold there during Anchor V4 production phase. No v0.5 scope until Anchor is stable and the bandwidth is genuine, not borrowed.

If a kill criterion is hit, the build stops. The doctrine document survives as a strategic artifact.

Order of operations:

Manual validation passes (inbox live, 20 listings processed, triage is useful).

VPS provisioned, repo scaffolded.

Module 1 working on real inbox data.

Module 2 tested against 50+ real listings.

Module 3 live: Telegram digest with drafts.

Hardening and documentation. Stop.

26. Consumer Agent Product Insight

The reason the adversarial stack is this expensive, brittle, and legally exposed is precisely why the legitimate consumer-agent opportunity exists. The market gap is real because brute-force is hard and getting harder.

Three patterns this work clarifies

Filter plus human closer is the durable shape for any consumer agent operating against hostile platforms. Any product that promises "we will message hosts for you" on FB Marketplace or CL is either a ban factory, running illegal infrastructure, or lying about what it does.

Trust signals are part of the architecture, not a UX layer. The human staying in the loop preserves the trust signal to the counterparty. In a market where a stranger decides who gets their keys, that is not a recoverable loss if it is broken.

The moat is integration with legitimate channels. Partner APIs, opt-in feeds, user-pasted content, and email-based ingestion are the real substrate of any consumer agent product. Companies that build there survive. Companies that brute-force anti-bot stacks get sued or commoditized by the next detection update.

This radar is a probe into that pattern. The thesis it tests applies far beyond sublets.
