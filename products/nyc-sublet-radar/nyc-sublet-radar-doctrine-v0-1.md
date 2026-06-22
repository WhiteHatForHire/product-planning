---
title: "nyc sublet radar doctrine v0.1"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /NYC Sublet Radar/Archive/nyc-sublet-radar-doctrine-v0.1.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# nyc sublet radar doctrine v0.1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
NYC SUBLET RADAR

Build Doctrine v0.1

Eagle Rocket LLC

1. Phronesis Check

Before architecture, the practical-wisdom question.

Anchor V4 is mid-pivot from feature work to production. Year one of sobriety has a stated "no new entrepreneurial commitments" rule. This document exists because the sublet radar can be built in two registers.

Side quest dressed as need. Time pulled from Anchor, agent credit burn, half-finished system. Bad outcome.

Cofounder-grade portfolio piece executed lean. A working consumer-agent prototype on a hostile-information problem. Demonstrates the fCTO thesis (filter plus human closer over hostile platforms). Good if the budget is honest and Anchor stays primary.

The cleanest framing: this is a probe. Time-boxed evening build sessions, not a sprint. If it ships at v0 and finds a workable sublet, win. If it stalls, the architecture document survives as a portfolio reference. Treat it like the Momoyo evaluation: study the structure, do not buy the franchise.

This document presumes the second register. Every section below is sized for that.

2. Problem Statement

The operator is in Gili Air and wants a one-week to one-month NYC base for a field-test sprint. The market is fragmented across Craigslist, Facebook housing groups, Listings Project, Leasebreak, Roomi, SpareRoom, Reddit threads, and a long tail of Substack, Slack, and Discord channels.

The friction is not finding listings. The friction is signal-to-noise (scams, ghost listings, mismatched neighborhoods), speed of human response, and being a legible-enough stranger that a leaseholder hands over keys.

The product is not a scraper. The product is a sublet radar that does cognitive triage and hands a curated shortlist plus drafted replies to the operator. The operator presses send.

3. The Three Routes

White Hat

Legal sources only. Email alerts, RSS, opt-in newsletters, partner APIs, user-pasted links. Agent does scoring, dedup, drafting, and digest. Human sends every message. Zero ToS exposure, zero ban risk, full trust signal preserved.

Gray Hat

Same as above plus light reads of sites whose ToS is ambiguous or whose anti-bot posture is thin: Reddit JSON endpoints, public Substack archives, certain aggregators. Still no automated outbound. Modest risk profile, mostly contractual.

Black Hat

Active scraping and automated messaging against FB Marketplace, CL, and similar through anti-detect browsers, residential proxies, and aged accounts. Documented in this file for landscape literacy and to sharpen the white-hat case. Not recommended for this build.

4. White Hat Stack (full landscape)

Ingestion sources

Craigslist saved-search email alerts (multiple per neighborhood and price band)

Listings Project weekly email

Leasebreak email alerts

Roomi and SpareRoom alerts

Reddit RSS for r/NYCapartments, r/AskNYC, r/sublets

NYC sublet Substacks (Frank’s, others)

User-pasted FB Marketplace and FB group links (manual collection, agent processes the paste)

Curated Slack and Discord channels where invited

Processing layer

IMAP poller or forwarding rules into a dedicated inbox

RSS poller (small Python cron, or Feedly/Inoreader API)

LLM extraction agent turning raw email into structured JSON

Listing CRM (SQLite v0, Postgres later if needed)

LLM scoring and drafting agents

Daily digest to Telegram bot (recommended) or email fallback

Outbound

Drafts only. Human reviews and sends from the original platform, on the original account, in their own voice (lightly edited from the agent draft).

Why this is the real architecture

Zero ToS violations and zero captcha wars

Zero ban risk on the operator’s real accounts

Trust signal to leaseholder is preserved (human-sent reply)

Scales cleanly into a multi-user product later if desired

Defensible as a portfolio piece, including on the Eagle Rocket site

5. Gray Hat Stack

Where the platform allows or tolerates light reads:

Reddit JSON endpoints via OAuth, low volume

Public Substack archives (typically scraping-tolerant)

Listings Project public archive

Aggregator sites with no aggressive anti-bot

Tools at this layer: Firecrawl, ScrapingBee, Apify, or BrowserUse for managed reads. Standard Playwright or Puppeteer for the rest. Residential proxies optional, usually not required at this volume. Outbound still human-only.

Risk profile: modest. Legal exposure is mostly contractual rather than statutory. Acceptable as an extension of v0 if a specific source justifies it.

6. Black Hat Stack (landscape literacy)

This section exists so the topology is understood, not as a how-to. Building this stack for a single sublet hunt is uneconomic, brittle, and exposed.

The four-layer counter-detection stack

Network. Residential proxies (Bright Data, Smartproxy, Oxylabs) at $5 to $15 per GB. Mobile proxies for the hardest targets. TLS fingerprint spoofing via curl-impersonate. Sticky session per account, rotating per identity.

Browser. Anti-detect browsers (Multilogin, GoLogin, Kameleo, AdsPower) at $99 to $200 per month. Consistent fingerprint per profile across sessions. Patched automation forks: Patchright, puppeteer-extra-stealth, undetected-chromedriver. WebRTC leak prevention.

Behavioral. Bezier mouse-movement curves. Variable typing cadence with backspaces. Randomized dwell times and scroll patterns. Browsing diversity beyond target pages so the session looks like a session.

Account / identity. Aged accounts from gray markets at $5 to $50 per FB account depending on age and verification status. Or self-warmed accounts grown over weeks. SMS verification farms. Strict isolation: dedicated proxy, fingerprint, device per account, never crossed.

Captcha. 2Captcha, CapSolver, Anti-Captcha at pennies per v2 solve. Arkose / FunCaptcha is significantly harder and more expensive. AI image solvers for some challenges.

Why it fails anyway

Meta runs internal velocity and graph-correlation models that test cohorts, not individuals. One bad profile burns the whole fleet.

Trust and safety teams manually review high-value flags.

Detection updates roll silently. Today’s working profile is next week’s ban.

Write actions (messaging) trigger spam classifiers stacked on top of bot classifiers. Read-only is hard. Write-with-volume is harder.

Operator burns hours fighting detection instead of finding housing.

7. Detection Mechanisms

What the platforms see when an automated session visits.

Network signals

IP reputation, ASN reputation, TLS fingerprint (JA3/JA4), HTTP/2 fingerprint, request rate, geographic consistency with the account’s prior history.

Browser signals

Canvas fingerprint, WebGL fingerprint, audio context fingerprint, font enumeration, screen resolution, timezone, language, plugin list, navigator.webdriver flag, presence or absence of chrome.runtime, WebRTC local IP leak.

Behavioral signals

Mouse-movement entropy, typing cadence, scroll velocity, page dwell time distribution, click target distribution, time-of-day patterns, navigation paths.

Account graph signals

Account age, friend graph density, posting history, login locations, device history, phone number reputation, cross-account fingerprint overlaps.

Meta in particular runs ML over the joint distribution of all of the above. The model has trained on billions of real users. A fleet of synthetic profiles looks like a fleet, not like users.

8. Legal Landscape

Three legal theories matter when scraping platforms:

Computer Fraud and Abuse Act (CFAA). Federal anti-hacking statute. The hiQ Labs v. LinkedIn line established that scraping technically public data (no login required, no auth bypass) probably does not violate CFAA. Case law is still evolving.

Breach of contract. Civil liability for ToS violations. Platforms have sued and won on this theory. Damages depend on harm and willfulness. Meta has filed and settled multiple suits against scrapers including commercial data brokers.

Tortious interference and unfair competition. State-law claims that often stack on top of contract claims.

Practical exposure for an LLC operator

Even a successfully defended suit costs six figures in legal fees.

Discovery is invasive (subpoenas to proxy providers, VPS hosts, payment processors).

Federal subpoena to a VPS provider produces server logs.

Insurance does not cover intentional ToS violations.

Eagle Rocket LLC is a named, real entity. Scraping infrastructure attaches to it.

This is the structural reason the white-hat plan dominates. The cost of an adverse outcome is not the cost of a banned Facebook account. It is the cost of legal exposure to a real entity.

9. Source Inventory

White-hat sources ranked by signal-to-noise for NYC short-term sublets:

Listings Project. Curated, low volume, high signal, weekly email. Best single source.

Craigslist email alerts. High volume, medium signal. Requires aggressive scoring.

Leasebreak. Purpose-built for sublets and lease breaks. Medium volume.

Roomi. Roommate and room-share focused.

SpareRoom. Larger, more national, decent for NYC.

Reddit r/sublets, r/NYCapartments, r/AskNYC. Variable, occasional gems.

NYC sublet Substacks. Hyper-curated, low volume.

Friend-of-friend Slack and Discord channels. Highest trust signal, hardest to find.

FB Marketplace and FB groups, manual save only in white-hat mode.

Each source gets a dedicated feed adapter in the Scout agent. Adapters are thin, isolated, and easy to disable individually.

10. Six-Agent Architecture

Agent 1: Scout

Polls each ingestion source. IMAP fetch from the dedicated inbox, RSS pulls, processes user-pasted URLs from a queue. Outputs raw listing payloads to the Normalizer.

Agent 2: Normalizer

Takes raw payload, outputs structured JSON: source, title, url, neighborhood, borough, price, dates, room type, furnished status, transit notes, contact method, raw text, photos present, posted at. LLM-driven, prompt-engineered for housing-specific extraction.

Agent 3: Evaluator

Scores each normalized listing against the criteria in Section 12. Outputs a 0-100 score, a reasons string, and a risk_flags array. Also runs Section 13 scam-pattern checks.

Agent 4: Drafter

For listings above the score threshold, generates a human-sounding reply tailored to specific details in the listing. References two or three concrete details so it does not read as templated. Avoids AI tells (no em dashes, no "I hope this finds you well," no aggressive enthusiasm).

Agent 5: Review Queue

Pushes the daily shortlist to a Telegram channel (recommended). Each item carries top-line summary, score, reasons, risk flags, drafted reply, and a one-tap link to open the original listing. Optional later: inline approve/reject controls via Telegram bot callbacks.

Agent 6: Memory / Deduper

Maintains persistent state. Hermes MEMORY.md and USER.md are fine for preferences and seen patterns (style preferences, scoring tweaks). Listing-level history goes in SQLite, not in agent memory, because volume exceeds Hermes’ intended memory scope.

11. Data Model

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

12. Scoring Criteria

Must-have (auto-reject if missing)

NYC or close-in Brooklyn/Queens

Short-term flexibility (1 week to 1 month)

Workable WiFi (mentioned or reasonably inferable)

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

Wire transfer or Western Union or crypto payment request

Name mismatch between listing and payment request

Stock-photo apartment images

"Kindly send payment" phrasing

Unwilling to do video tour

No physical address even at neighborhood granularity

13. Scam Detection Patterns

Classic NYC sublet scam signatures the Evaluator should flag.

Linguistic

"Kindly", "dear", "my good friend", "blessings"

Grammar inconsistent with claimed nationality

Phrasing imported from West African or Eastern European scam templates

Excessive religious framing ("God bless this transaction")

Urgency without justification ("must rent today")

Logistical

Owner is "out of the country" or "on a missionary trip"

Cannot show in person, only video, and resists requests for a live tour

Deposit via Zelle, Venmo, wire, or crypto before key handoff

Price more than 30 percent below comparable units in the neighborhood

Same photos appearing on multiple listings (reverse image search)

Listing claims furnished but photos show empty rooms

Identity

New account, no history

Profile photo is a stock image or known celebrity

Name on listing differs from name on payment request

Phone number is VOIP

The Evaluator flags these. Single flag pushes to a review-with-caution bucket. Two or more flags drops the score below the shortlist threshold.

14. Prompt Library

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
- Prices: normalize to USD per month. If weekly, multiply by 4.33.- Neighborhoods: use canonical names (Williamsburg, not "Wburg").

Evaluator prompt (sketch)

You score NYC short-term sublet listings for the operator, a
30-something remote worker visiting NYC for a one-week to one-month
sprint. Score 0-100 against the criteria below. Output JSON:
{ score, reasons, risk_flags, recommendation }.

[criteria block, Section 12]
[scam patterns, Section 13]

Recommendation values: shortlist, maybe, reject.

Be skeptical. False positives waste the operator's time more thanfalse negatives. Lean toward reject on ambiguous signals.

Drafter prompt (sketch)

You draft replies to NYC sublet listings on behalf of the operator.
The operator is a 30-something remote worker, currently based in
Indonesia, returning to NYC for a one-week to one-month working trip.
Sober, quiet, clean, normal sleep schedule, works on a laptop.

Reference two or three specific details from the listing so the reply
does not read as templated. Direct and warm tone. No em dashes. No
filler. Three to five sentences. Sign as the operator.

End with two specific questions: one about logistics (move-in date
confirmation, deposit terms), one about the space (WiFi speed, desksituation, neighborhood detail).

15. Infrastructure: Hermes plus VPS

Decision

Hermes Agent as the orchestrator, a small VPS as the always-on host. Source of truth in GitHub, deploys pulled to the VPS. Matches the Anchor workflow direction.

VPS sizing for v0

1 to 2 vCPU, 2 to 4 GB RAM is plenty for a polling agent plus small DB

Hetzner, Vultr, or DigitalOcean. ~$5 to $10/mo.

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

IMAP credentials for a dedicated inbox (e.g., marcus.sublets@... )

Telegram bot token

Anthropic API key

Sentry DSN for error tracking

Source of truth

GitHub repo eagle-rocket/sublet-radar. CC and Codex push commits, VPS pulls via a small deploy script and restarts services. No agent credit burn for routine code work.

Hermes specifics to verify on setup

MEMORY.md and USER.md persistence locations on the VPS

Firecrawl integration for the few white-hat web fetches needed

Tool registration syntax (read current docs, do not assume)

Token/cost ceiling configuration

16. v0 Build Plan

Goal: working radar in three to five focused sessions. Drafts only, zero outbound automation.

Session 1: VPS plus repo plus scaffold

Provision VPS

Set up GitHub repo with basic structure

Install Hermes and the Python or Node runtime

Create dedicated Gmail inbox

Set up Craigslist saved searches forwarding to that inbox

Subscribe to Listings Project from that inbox

Session 2: Scout plus Normalizer

IMAP poller for the dedicated inbox

RSS poller for Reddit and any newsletter RSS available

Normalizer agent with the prompt from Section 14

Write to SQLite

Session 3: Evaluator plus scam detection

Scoring prompt

Scam pattern flags

Test against 50+ real listings accumulated in the inbox

Session 4: Drafter plus Digest

Draft prompt with reference-detail logic

Daily digest to Telegram bot

One-tap "open original listing" link per item

Session 5: Hardening

Sentry wired

Dedup audit

Memory file structure for preferences

README in the repo

Out of scope for v0

FB scraping in any form

Auto-send

Multi-user

Web UI

17. v0.5 Extensions

Only after v0 is stable and the operator has actually used it to find a sublet.

Manual FB link queue. Operator pastes FB URLs into a Telegram channel, agent fetches the public preview if available, otherwise asks for pasted listing text. Processes through the same pipeline.

Reverse image search for photo-based scam detection.

Auto-tagging of "good" listings the operator engaged with vs. "bad" rejections, for scoring tuning.

Weekly summary comparing this week’s inventory to last week’s.

18. v1 Roadmap

Only if a decision is made to productize for others, and only if Anchor is stable.

Multi-user with per-user preference profiles

Web UI for review and one-tap reply

Partner APIs where they exist (Zillow, Apartments.com)

Mobile push instead of Telegram

Subscription pricing or one-time-fee for a sprint

This is a real consumer-agent product opportunity. It is not v0 work and it is not Anchor work.

19. Risk Register

Build risk

Hermes is newer; tool integration may have edges. Keep core logic in pure Python or Node, use Hermes for orchestration only.

LLM cost creep. Cap daily LLM spend, batch where possible, use cheaper models for normalization.

Operational risk

VPS goes down. Systemd auto-restart plus weekly health-check ping.

Inbox fills with scam noise. Aggressive Evaluator rejection threshold.

Personal risk

Side-quest creep into Anchor time. Time-box build sessions, no work after 9pm, single weekly review.

Future-focused expansion ("this could be a SaaS"). This document is the boundary. v0 is the scope. Productization is a later decision under different conditions.

Legal risk under the white-hat plan

Effectively zero. Email alerts, RSS, opt-in newsletters, and user-pasted links are not actionable. The legal landscape section is there for landscape understanding, not because v0 touches it.

20. Cost Comparison

Item

White Hat

Black Hat

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

10-15

30-60+

Ongoing maintenance

low

high (detection updates)

Ban risk

0

high

Legal exposure

0

meaningful

Effectiveness for one sublet

strong

marginal

White hat dominates on every axis that matters at this scale. The black-hat stack only becomes interesting at multi-user scale, and at that scale it becomes a different business with active legal exposure.

21. Recommended Plan

Build v0 of the white-hat radar over three to five focused sessions on the VPS plus Hermes stack already being set up. Ship to drafts-only. Use it to find an actual NYC sublet. Document the build in the repo as a future fCTO portfolio piece showing how to operate consumer agents over hostile information environments without violating ToS or platform integrity.

If v0 ships and works, hold there. Do not extend during Anchor V4 production phase. v0.5 work happens only if Anchor is stable and there is genuine bandwidth, not stolen bandwidth.

If v0 stalls, this document survives as a strategic artifact. The Master Playbook gets a new chapter on consumer-agent architecture against hostile platforms. No loss, clean exit.

Order of operations:

VPS provisioned, repo scaffolded, dedicated inbox live, alerts subscribed.

Scout and Normalizer working end-to-end on real inbox data.

Evaluator and scam detection tested against 50+ real listings.

Drafter and Telegram digest live.

Hardening and documentation, then stop.

22. Consumer Agent Product Insight

The reason the adversarial stack is this expensive, brittle, and legally exposed is precisely the reason the legitimate consumer-agent opportunity exists. The market gap is real because brute-force is hard and getting harder.

Three patterns this work clarifies

Filter plus human closer is the durable shape for any consumer agent operating against hostile platforms. Any product that promises "we will message hosts for you" on FB Marketplace, CL, or similar is either a ban factory, running illegal infrastructure, or lying about what it does.

Trust signals are part of the architecture, not a UX layer. The human staying in the loop preserves the trust signal to the counterparty. Replacing the human with a bot replaces trust with friction, especially in markets like housing where strangers exchange keys based on perceived legibility.

The moat is integration with legitimate channels. Partner APIs, opt-in feeds, user-pasted content, and email-based ingestion are the real substrate of any consumer agent product. Companies that build there survive. Companies that brute-force anti-bot stacks get sued or get commoditized by the next detection update.

This radar is a probe into that pattern. The thesis it tests applies far beyond sublets, to any consumer-agent product operating where the platforms are adversarial.
