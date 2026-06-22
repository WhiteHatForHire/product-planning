---
title: "Neskala Vision v6 3"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/#Neskala/Neskala Vision v6 3.docx"
status: reference
privacy: working
tags:
  - product
---

# Neskala Vision v6 3

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
CODENAME: NESKALA  v6.3

Trusted matching for Bali bodywork.

Operator-Grade Vision Document  ·  April 2026

Working title. Final name to be chosen by Yuni.

Version 6.3 — Founder: Marcus  ·  v6.2 added Track A priority, Ravi's Friday, scan-to-booking funnel, villa partner funnel, raw intake retention, pre-first-booking safety gate, Net IDR/min kill threshold, star_sign cut. v6.3 adds: automation boundary (calendar-backed not calendar-automated), booking state machine, "what V0 does not expose yet" list, Premium Tier pricing.

A Letter to Yuni — Read This First

Yuni,

You called the Momoyo corporate team and asked better questions on that first call than most experienced investors would think to ask. You got the territory data, the pricing breakdown, the royalty confirmation, the location criteria. That initiative matters and I noticed it.

We have done serious diligence on the franchise. That work was not wasted — you now understand how franchises are structured, how to read an investment breakdown, how to think about unit economics, and how to ask corporate teams the right questions. That education is yours.

But I want to be honest: the franchise is someone else's system, someone else's supply chain, someone else's rules. I have been in that situation before — investing in a physical operation from a distance — and the gravity always pulls you in as the shadow operator. I do not want that pattern again.

What follows is a different idea. One that is built around what you are actually good at: Bahasa, local relationships, the ability to walk into a room and make practitioners feel genuinely seen. Those are not supporting features of this business. They are the engine.

I am giving you genuine permission to say no. This only makes sense if the work feels alive to you. If recruiting massage therapists, pitching villas, and coordinating bookings sounds draining rather than exciting — tell me honestly. We find something else. No pressure either way.

If it sounds interesting: read everything below.

— Marcus

Part 1 — Founder Summary

The pitch, in plain English.

Open Yelp for massage in Bali. Tell me which one matches what you actually need right now. You can't. Nobody can. The whole category is broken because reviews tell you about the business, not whether it's right for you.

Booking platforms digitize inventory. Neskala digitizes the somatic state of the customer. We're rebuilding wellness discovery around fit instead of inventory — and the data that accumulates underneath (which states map to which providers map to which outcomes) is the first dataset of its kind that's ever existed.

First wedge: Ubud villa and guesthouse referrals for English-speaking travelers seeking trusted in-villa bodywork in the next 24–72 hours. A guest scans a QR code at reception, describes how their body and mind feel, and gets three vetted matches with a clear explanation of why each person fits.

Build the prototype first, then go to providers and partners with it. The app is the pitch. When Yuni walks into a Penestanan therapist’s home with a working product on her phone — clean UI, real intake, real match output, and a placeholder profile already mocked up for them — that is a fundamentally different recruiting conversation than “trust me, my partner is going to build something.” Behind the polished interface, V0 ops are still manual: Yuni confirms availability via WhatsApp, customers pay providers directly, Marcus or Yuni can override any match. But we ship the working software before week one of field recruitment, not after.

One-liner

Tell us how you feel. We'll match you with the right trusted practitioner in Bali.

What this is, honestly

V0 is a cashflow concierge experiment that may reveal a venture-scale marketplace.

Not the other way around. The first business is a working AI-matching prototype with manual operations behind it — not a manual concierge that gradually adds software. We build the app first because the app is the recruiting tool, the trust signal, and the differentiator. It has to prove three things before it earns the right to claim more: that customers prefer matched booking to browsed booking, that providers value our distribution and want to be on the platform, and that Yuni enjoys the field work. If those three are true, the dataset and the platform follow. If they’re not, we have a profitable concierge service and we move on without false stories.

This framing is non-negotiable. Pretending V0 is venture-scale from day one is how founders blow up small honest businesses chasing decks they wrote too early.

The wedge

Ubud villa and guesthouse QR referrals for English-speaking travelers seeking trusted in-villa bodywork within 24–72 hours.

Six things matter in that sentence:

Ubud first — densest wellness corridor, plannable distribution, Yuni's strongest network.

Villa and guesthouse partner channel — we don't acquire customers cold. We borrow trust from a host they already trust.

English-speaking travelers — filters for our addressable customer and our V0 provider English distribution.

In-villa bodywork — the highest-trust, most intimate service category. If matching matters anywhere, it matters here.

24–72 hours — enough urgency to convert. Enough time to coordinate. Not so urgent that customers only care about availability.

Trust over speed — the customer who books for fit reads the explanation, rebooks, and tells friends. The customer who panics for tonight just wants a body in the room.

What this looks like for one specific customer

Sarah's Wednesday.

Sarah is 34, from Melbourne. She's on day 4 of an 8-day yoga retreat at her villa in Penestanan. She didn't sleep well last night — third time this trip. Her shoulders are wrecked from a 19-hour flight she took in seat 47B. Her brain is loud. Her hips are tight from yesterday's hip-opener class. She's emotional in a way she can't name yet.

She walks past reception at 11am and sees a small card next to the welcome basket.

"Trusted in-villa bodywork. Tell us how you feel — we'll find the right person for you. Vetted by locals, paid in cash. Free to use."

She scans the QR. The page opens on her phone. One question:

"Rough day? Tell us how your body and mind are feeling right now."

She types for 90 seconds. Doesn't think about it. Mentions the flight, the hips, the bad sleep, the heaviness she can't articulate.

Two follow-ups. Any injuries or things to know? When? Gender preference?

She gets three matches.

"Wayan is matched to you because you mentioned emotional heaviness alongside physical depletion and asked for a quieter session. She specialises in nervous-system-aware traditional Balinese massage — most of her returning clients describe her as the right person after long flights or hard practice. Available at your villa Friday at 4pm."

Sarah picks Wayan. WhatsApp confirmation arrives 14 minutes later from "Yuni from Neskala." Friday at 4pm, 90 minutes, Rp 450,000, cash to Wayan, here's what to expect, message me if anything changes.

Friday afternoon Wayan shows up, kicks her sandals off at the door, and reads Sarah in the first thirty seconds. The session changes the trip.

Sunday morning Sarah books a second session before she flies home. Sunday afternoon she texts the WhatsApp number with a referral for her friend Anna. Monday she's home in Melbourne, posting a story tagging Neskala on Instagram.

That's the product. That's also the dataset growing by one labeled tuple.

Every Sarah teaches the system something about which providers resolve which states, in which contexts, for which kinds of customers. By session 1,000 we have the start of a real graph. By session 10,000 we have something nobody else has.

Ravi’s Friday — the case that tests the product.

(The narrative we need to tell ourselves alongside Sarah’s. Beautiful matches don’t test the system. Constraint collisions do. The business lives in how this case gets handled, not how Sarah’s gets handled.)

Ravi is 41, from London, in Bali for a week with his partner. They’re staying at a villa in Sayan that Yuni signed as a partner three weeks ago. It’s 7:40pm on Friday. He’s tight from a 14-hour flight, jet-lagged, and his partner has period cramps. He scans the QR card on the welcome desk.

He types: “Couples session, in our villa, tonight if possible, somewhere around 9pm. She has cramps, I have flight back. We’d prefer a female therapist for her, doesn’t matter for me. We can both speak basic English with the therapist.”

Now everything that can break, breaks.

9pm tonight is inside the Track A 24–72hr window only barely — this is the kind of urgent request we said we wouldn’t over-promise.

Couples-capable providers in our V0 pool: 2. Female + Couples + available 9pm Friday: 0 confirmed.

“Period cramps” is on the borderline of the safety classifier — not in the kill-switch list, but worth a moment of human review for pressure/area-to-avoid considerations.

Yuni is 90 minutes into a movie at home. Her phone is charging in the kitchen.

What needs to happen for the system to handle this well:

The match output does NOT show three confident matches at 9pm tonight. It shows: “Couples sessions usually take a day to coordinate well. Earliest realistic option: tomorrow afternoon. Want us to try for tonight, or shall we book tomorrow?”

Yuni gets a high-priority WhatsApp ping (different sound from normal bookings) because the request is <90 minutes from desired session start. She sees it within 10 minutes.

She messages Ravi: “Got your request, working on it now — will know in 15 minutes.” Sets expectations.

She finds one provider who can do single sessions for both at 9:30pm (not couples, not female-only-for-her), and one option at 11am tomorrow that’s a couples session with the right gender mix. Offers both honestly.

Ravi takes the 11am option. Pays the villa partner’s commission. Tells the front desk it was handled well. Gives the system a 5/5 in feedback specifically because it didn’t over-promise.

What this case reveals about the product:

Match cards must show provisional availability, not faked availability. Wording: “Best fit, availability to be confirmed by WhatsApp.”

Constraint collisions (couples + gender + late-night + same-day) need an early-decline path: “This combination usually takes 24+ hours to coordinate well.” Honesty wins more than over-promising.

Urgent requests need a separate alert path so Yuni catches them within minutes, not hours. Build a high-priority channel.

Single-couples-provider scarcity is real. The minimum viable provider bench (Part 9) needs at least 2 female + couples-capable providers with broad availability.

Product trust comes from honest constraint handling, not from making every request feel magical. Sarah loves us because we got it right. Ravi will love us because we didn’t fake it when we couldn’t get it right.

If V0 cannot handle Ravi’s case as well as Sarah’s, V0 isn’t ready.

What Changed From v5 → v6.2

v6.2 (build-ready patch):

Track A field-sprint prioritization: architecture supports all three; field work focuses on Track A. v6.1’s “all three V0” was focus debt.

Scan-to-booking funnel added — the real V0 dashboard with diagnostic interpretation per stage.

Villa partner acquisition funnel added (parallels provider funnel). Plus partner rejection-reason logging.

Raw intake retention policy added — resolves v6.1 internal contradiction (audit log vs. data minimization).

Pre-first-booking safety gate added as explicit checklist. Booking #1 cannot happen until every box is checked, signed off in writing.

Hard kill threshold for Net IDR/Yuni-minute: below Rp 2k after 20 sessions and not trending up = stop, automate, reprice, or kill. Plus weekly Yuni emotional-cost check-in.

Ravi’s Friday added — the failed-match narrative alongside Sarah’s Wednesday. Constraint collisions test the system; beautiful matches don’t.

star_sign removed from V0 schema. Astrology de-emphasized for trust-sensitive bodywork wedge; revisit in Phase 2 Spirit vertical.

Companion artifact: separate 2-page Yuni Brief, to be sent to Yuni in place of this full operator doc.

v6.0 / v6.1 (preserved):

Three customer tracks instead of one (tourists, nomads, residents). Each has different acquisition channels, different economics, different roles in the dataset.

Sharpened wedge. "Within their stay" → "24–72 hours." Vague urgency → bounded plannable urgency.

Founder Summary rewritten. Less buzzword, more contrast structure. Removed "first proprietary dataset" overclaim from the front.

Added Sarah's Wednesday — one specific customer's full experience, in narrative form.

Added Villa Partner Value Proposition (Part 12). v5 had customer and provider VPs; the third side of the marketplace was missing.

Added Landing Page Copy section (Part 13). The actual first screen, not just abstract trust surfaces.

Added Provider Acquisition Funnel — making real that 10 approved providers requires 40 leads.

Replaced V0 70/30 A/B test with post-booking counterfactual survey. A/B moves to V1 when traffic supports it.

Net IDR per Yuni-minute as headline KPI for the 30-day sprint.

Kill-fee restructured: tied to fieldwork completed (Rp 500k per onboarded provider + Rp 1m per signed villa partner, capped at Rp 8m).

Yuni capture system — voice memo to structured DB record, built day one.

Cashflow-vs-venture framing made explicit in Founder Summary.

Risk Register cut from 16 entries to 7 ranked risks with two starred existential.

Provider archetypes section condensed; tier/quality/English/bench tables consolidated.

Part 2 — Market Reality

The macro numbers (kept short on purpose)

The global wellness economy reached USD 6.8 trillion in 2024 (Global Wellness Institute). Bali's spa and wellness sector has grown 160%+ since 2003, with roughly 390 spas and thousands of independent practitioners. BPS reported ~6.95M direct foreign tourist arrivals in Bali in 2025, up 9.72% YoY.

These numbers tell us the category exists and the trend points up. They do not tell us anything useful about Year 1 obtainable market.

Honest TAM math

Year 1 SOM is a specific slice of arrivals: English-speaking, staying in Ubud/Canggu/Seminyak villas or guesthouses, willing to book matched in-villa wellness, reachable through partner distribution. Conservative: a few thousand bookings per month at saturation. The big TAM is the ambition. The Ubud villa-stay wedge plus the Canggu nomad track is the actual Year 1 business.

Why now

Wellness tourism is large and structural, not cyclical.

Bali has dense, under-distributed supply. Thousands of practitioners on WhatsApp/Instagram with no real digital channel.

AI changed user expectations. People want the system to understand them and narrow the field — not browse 200 listings.

Trust is the bottleneck. Generic search doesn't build trust. Matching and explanation do.

Payments are broken for the long tail. Most practitioners can't accept foreign cards. Solving this is real provider lock-in (V2+).

Part 3 — The Three-Track Customer Strategy

v5 collapsed all customers into one track. v6 separates them, because they have different economics, different acquisition channels, and different roles in building the company.

Track A: Tourists. 3–14 day stay. Premium pricing. Single booking per customer. Funded by villa/guesthouse referral distribution. The cashflow engine.

Track B: Nomads. 1–3 month stay. Mid-tier pricing. 2–6 bookings per stay. Acquired through coworking spaces and WhatsApp communities. Partial longitudinal data.

Track C: Residents. KITAS, business visa, married-to-Indonesian, long-term expats. Recurring monthly bookings. Acquired through community word-of-mouth and existing client referrals. The recurring revenue base and the deepest dataset signal.

The architecture supports all three tracks from day one. The field sprint prioritizes Track A first — villa/guesthouse tourist bookings — with opportunistic Track B/C capture only if they appear naturally through existing relationships or referrals. Month 2 deliberately activates the nomad channel (coworking, WhatsApp groups). Month 3 deliberately activates residents (community word-of-mouth). v5 deferred nomads and residents to "Phase 2" entirely — that was wrong because we lose the data thesis. v6.1 said "all three tracks are V0" — that was wrong because it spread Yuni’s field time across three different acquisition motions in the first month. v6.2 corrects: build the architecture for all three; sprint the field work on one.

Why three tracks, not one

Track

Stay length

Bookings/customer

Channel

Role in business

A: Tourist

3–14 days

1–2

Villa/guesthouse QR referral

Cashflow. High-margin premium bookings. Builds platform revenue immediately.

B: Nomad

1–3 months

2–6

Coworking spaces, WhatsApp groups, retreat-adjacent

Partial longitudinal data. Tests recurring booking hypothesis. Builds early dataset.

C: Resident

1+ years

8–24/year

Community referral, expat WhatsApp groups, gym/yoga partnerships

Recurring revenue base. Full longitudinal somatic profiles. The dataset thesis lives or dies here.

The Data vs. Cash structure

Tourists pay the bills. Residents prove the dataset. Nomads sit between, providing both partial revenue and partial longitudinal data. The architecture has to serve all three.

This resolves the cashflow-vs-venture question explicitly:

V0 is a cashflow business that builds the data acquisition for a venture business. The cashflow business funds the data acquisition. The data acquisition funds the eventual platform thesis. Both are true and they sequence naturally — but only if we don't pretend nomads and residents are a Phase 2 problem.

Persona priority for V0

Five personas in v5 was too many for a wedge document. v6 keeps the V0-relevant ones and drops the rest into Part 8.

Track

Primary V0 persona

Acquisition signal

Avg spend

A

The Overstimulated Tourist (jet-lagged, post-flight, anxious, sore from travel; villa or guesthouse; 3–14 day stay)

QR code at villa reception, partner referral

Rp 400–500k

A

The Couple (premium villa, 5–14 days, wants a shared experience)

Villa concierge upsell, anniversary/honeymoon flag

Rp 700–900k for couples

B

The Digital Nomad (Canggu/Ubud, 1–3 month stay, laptop sore, periodic recovery)

Coworking partnership, WhatsApp group, Instagram referral

Rp 350–450k, monthly

C

The Resident (KITAS/visa holder, 1+ years, recurring bodywork need)

Existing-customer referral, community word-of-mouth

Rp 350–450k, 1–2x/month

The Retreat Participant and Spiritual Seeker personas from v5 move to Phase 2 (Part 8). Adding them earlier creates focus debt.

Part 4 — Competitor Landscape

Neskala is entering a competitive category, not a blank space. The differentiation must be precise.

Direct: on-demand massage apps (Dewata Wellness)

Dewata markets itself as Bali's on-demand massage and beauty app — instant booking, nearby therapist discovery, certified therapists, secure payment.

Honest framing: If a customer wants the fastest available therapist, Dewata may win. We don't compete on speed. If the customer wants the right trusted person for their state, we should win. Different game.

Premium mobile spa operators (The Remedy, IRO, Bali Luxe)

Single-brand operators with their own staff, manual WhatsApp coordination, premium positioning, wide Bali coverage.

Honest framing: They have brand consistency. We have variety, matching, and breadth across independent providers. Their risk to us: a single-brand operator with great staff may outperform a loose marketplace on consistency. Our answer: managed marketplace, strong vetting, no open self-listings, trial tiers, private feedback loop.

OTAs (Klook)

Klook lists Bali home-service spa with tourist trust, SEO, payments, and discounting. Wellness as inventory, priced and proximity-ranked.

Honest framing: We can't compete on SEO or scale at first. We compete on fit, intimacy, and the villa-borrowed-trust wedge. The customer paying Rp 450k for a matched session is a different customer than someone clicking the cheapest Klook listing.

Wellness centers and healer hubs (Bali Healing, Heart Space Ubud, Yoga Barn)

Established trust, specific practitioner identity, venue-based.

Honest framing: Some of these are competitors. Some are eventual partners — the matching layer can route customers to the right center, not replace it. The most dangerous version of this category: a major retreat center (The Practice, Pyramid House, Soulshine) building their own matching tool for their participants, because they already own the highest-trust relationship with our highest-value cohort. We watch this carefully.

Global wellness booking infrastructure (Mindbody/ClassPass, BookRetreats)

Enterprise scheduling and payments. Retreat discovery globally.

Honest framing: We don't fight Mindbody on scheduling software or BookRetreats on retreats. Local trust, AI state matching, and informal-economy provider onboarding in WhatsApp-first markets — they cannot build what Yuni builds in two weeks of fieldwork.

If competitors copy AI intake

Anyone can wrap Claude around a wellness intake in a weekend. Assume Dewata or another operator does this within 60 days of seeing us. The interface is not the moat. Our response, in order:

Go deeper on provider quality. Personally vetted. Photographed. Profiled. Yuni's network.

Build the private feedback graph. Every session updates provider weighting. They start at zero. We don't.

Lock in priority providers in V1+ for first-availability commitments.

Improve villa partner economics so they don't switch.

Build the FX/foreign-card payment rail in V2 — switching cost for providers becomes real.

Own the category language before they recognize it as a category.

Part 5 — What Neskala Is and Is Not

Neskala IS

Neskala IS NOT

A state-based AI matching layer for wellness

An open marketplace where anyone can self-list

A managed marketplace — curated supply, controlled matching

A generic spa or massage directory

A high-trust local wellness concierge (V0 = supervised matching with human override)

An on-demand "book within an hour" app (not in V0 or V1)

A three-track business: tourists, nomads, residents

A medical or therapy platform

A data-rich provider graph built manually first, automated later

A spiritual authority or certification body

A payment bridge for practitioners who can't accept foreign cards (V2+)

A discount marketplace competing on price

A distribution engine for under-discovered Bali providers

A pure booking engine with no intelligence

Mobile web first — QR code, no install, no login

A retreat marketplace (much later)

A review site (private feedback only in V1)

An AI diagnosis tool of any kind

Part 6 — The Product

The core hypothesis — and how V0 actually tests it

Core Hypothesis

Customers will trust more, convert faster, and feel more satisfied when matched based on their state rather than browsing generic listings. The match explanation — the "why you" — is the product differentiator, not the inventory.

How V0 actually tests this — counterfactual survey, not A/B

v5 proposed a 70/30 A/B (intake vs. browse). At 20–30 bookings, that splits scarce demand and produces noise, not signal. v6 keeps every customer on the matched flow and asks them directly:

"Did the match explanation increase your trust in this booking?"

"Would you have booked without the explanation?"

"Did the provider feel matched to your state?"

"What made you decide to book?"

"Would you have preferred browsing a list?"

This gets us the same learning without sabotaging half the funnel. The actual A/B test moves to V1 when traffic supports it (50+ booking requests, real browse-page comparison, statistical signal possible).

The AI intake — conversational, not a form

The whole differentiation is not feeling like a form. If the intake feels heavier than browsing, we lose. The implementation must feel light enough that a jet-lagged tourist completes it without thinking.

The Intake — Conversational Design

Opening: "Rough day? Tell us how your body and mind are feeling right now."

The AI parses natural language. Free text or voice. No form. No dropdowns. No required fields.

From the natural response, the AI extracts:

Physical state · Emotional state · Body location of tension · Desired outcome · Energy preference · Implied pressure preference · Safety flags

Then 1–2 gentle follow-ups for essentials:

"Any areas, injuries, or health considerations we should know about before matching you?"

"Gender preference, or happy with whoever's the best match?"

"When — today, tomorrow, this week, or whenever you find the best match?"

"Budget and location?"

Optional woo layer (slider, not a prompt):

Practical only · Open to intuition · Spiritual · Surprise me

Output: Three matches with a two-sentence personalised explanation each.

"Wayan is matched to you because you mentioned emotional heaviness alongside physical depletion and asked for a quieter session. She specialises in nervous-system-aware traditional Balinese massage and is available at your villa Friday at 4pm."

Total time target: under 60 seconds for the intake. The match output should feel earned, not extracted.

Hard filters first, soft matching second

The AI never makes safety decisions. It ranks within a pre-filtered pool of safe candidates. Hard filters apply first; soft matching ranks within what's left.

Hard Filters (applied first)

Soft Matching (ranks within filtered pool)

Provider availability for requested time window

Emotional state and desired outcome

Location and travel radius

Energy style preference

Gender preference if required

Provider archetype match

Language requirement (provider English level)

Pressure preference

Pregnancy or injury suitability — certified providers only

Woo preference level

Budget range

Past session feedback (repeat bookings)

Provider tier (no Tier 2 for sensitive bookings)

Personality fit signals

Safety classifier flags (see Part 9)

Provider's stated best-client type

No banned provider/customer pairing

The data flywheel — and why it's the actual moat

Every completed session improves matching. Post-session private feedback updates each provider's match weighting. A provider who consistently receives "great for grounding" feedback gets weighted higher for anxious customers. After V1, this is automatic.

The accumulating asset is the mapping between unstructured human emotional states and specific physiological interventions that worked. Wellness is currently categorized by modality (Deep Tissue, Balinese, Shiatsu). Neskala categorizes by somatic state and learns which provider archetypes resolve which states.

That mapping is the IP. The chat interface is not.

Supervised matching with human override (V0 architecture)

v5 called this "Wizard of Oz." That language is wrong now — the AI safety classifier does real work and the matching engine genuinely matches; humans review, they don't fake it. v6 calls it what it is: supervised matching with human-in-the-loop override.

The customer experiences polished AI matching. Marcus and Yuni can review and override any match. Provider availability is confirmed via WhatsApp, not live calendar. Payments are direct customer-to-provider. The goal is learning, not automation.

Mobile web first. No native app.

V0 and V1 are mobile web only. A jet-lagged tourist at 9pm in a villa is not downloading an app. QR code → mobile web → no login → no install → conversational intake → match → WhatsApp confirmation handoff. Works on iPhone Safari and Android Chrome. Loads fast. No native app until repeat usage proves the case for one — which probably means never on the customer side.

Part 7 — Service Categories

One product. Two verticals at launch. Phase 3 added after Body and Spirit are stable. Body only for the first 60 days.

Phase 1 — Body — Massage, Bodywork & Physical Wellness

Launch vertical. Highest demand, clearest transaction, lowest liability, easiest to validate.

Balinese massage (60 or 90 min)

Deep tissue and therapeutic massage

Relaxation massage

Foot massage and reflexology

Couples massage (villa visit)

Prenatal massage — certified providers only

Post-yoga and sports recovery

Lymphatic drainage

Jet lag and travel recovery

Phase 2 — Spirit — Healers, Energy Work & Wellness Practitioners

Add after Body is stable and 50+ bookings are complete. Two internal lanes: Traditional Bali and Global Wellness.

Traditional Balinese healers (Balian) — special vetting and cultural care required

Sound healing and singing bowls

Reiki and energy work

Breathwork facilitation

Tarot and oracle reading

Private meditation guide

Somatic sessions

Private yoga (villa or studio)

Phase 3 — Concierge — Bali Life Services

Add after Body and Spirit are running consistently. Turns Neskala into the full Bali services layer.

Scooter rental, private driver and day trip

Babysitter and nanny (vetted, bilingual)

Private chef or cooking experience

Villa cleaning, laundry, beauty services

V0 service menu — kept tight on purpose

Matching only works if services are standardized enough to compare. V0 menu:

60-min Balinese · 90-min Balinese · 60-min deep tissue · 90-min deep tissue · Foot/reflexology · Couples in-villa (60 or 90 min) · Post-yoga recovery

Part 8 — Provider Network and Moats

Why the provider network is the product

The app delivers. The provider profiles are the data that makes matching intelligent. The richer the profiles, the better the matches. The better the matches, the more sessions. The more sessions, the more feedback. The more feedback, the richer the profiles. This is the flywheel.

Moat stack — ranked by defensibility

#

Moat

Why it compounds

1

Vetted provider relationships

Yuni personally interviews and approves every provider. Impossible to replicate at speed without a local operator on the ground.

2

Structured provider graph

Profiles richer than any listing — archetype, energy style, best-client type, boundaries, English level, equipment, travel radius.

3

Match feedback loop (the somatic dataset)

Every completed session improves provider weighting for specific customer states. Long-term IP. A competitor starts at zero.

4

Local distribution network

Villa, guesthouse, yoga studio, cafe, coworking partners. Each has a referral code. Compounds with every new partner.

5

Provider trust

Providers join because we send better-fit clients, screen out sketchy walk-ins, market in English, fill weekday gaps, and (V2+) accept foreign cards. They don't leave because alternatives are worse.

6

FX/payment rail (V2+)

Card-to-IDR settlement for providers who can't accept foreign payments. Real switching cost.

7

Brand and category ownership

"State-based wellness matching" becomes the category before competitors recognize it as one.

8

Operational playbook

Repeatable city-launch process. Proprietary. Hard to compress without having done it.

9

AI intake design

Not a moat. Anyone can clone the chat interface in a weekend. Listed last on purpose.

Provider archetypes — five for V0, expand later

V0 Archetype

Matches well with...

The Grounder

Anxious, overstimulated, scattered — needs earth energy, slow pace, quiet presence

The Deep Tissue / Recovery Pro

Athletic, tight, post-yoga, post-gym — wants strong pressure, physiological release

The Quiet Nurturer

Depleted, grieving, jet-lagged, emotionally tender — needs warmth without intensity

The No-Woo Professional

Practical, clinical — just wants good bodywork, no chat, no spiritual framing

The Premium Villa Specialist

High-end, villa visits, premium presentation, couples-capable

Phase 2 expansion archetypes (added after Body is stable): The Spiritual Guide, The Ceremonial Elder (Balian), The Energy Worker, The Post-Retreat Integrator, The Athlete Recovery Specialist.

Provider quality tiers

Tier

Description

Yuni's role

Tier 1: Verified Core

Personally interviewed, reliable, tested, ready for villa visits. Backbone of V1.

Full intake, reference check, photo. Monitor first 3 bookings.

Tier 2: Trial

Promising but not enough feedback. Bookings with oversight.

Promote to Tier 1 after 3+ clean sessions with good feedback.

Tier 3: Specialists

Healers, ceremony, deeper spiritual work. Extended vetting.

Yuni attends a session herself if possible before listing.

Do Not List

Boundary issues, unreliable, exaggerated claims, poor communication.

Yuni's judgment call. No second chances on safety.

Provider Acquisition Funnel — make the work real

v5 said "10 providers minimum." v6 makes the funnel explicit. 10 approved providers requires 30–40 leads.

Stage

Target

Notes

Initial provider leads

40

From Yuni's network, partner referrals, walking the studios

Responds to outreach

25

WhatsApp first contact, builds initial trust

Interview completed

15

30–45 min structured intake (modalities, boundaries, English, style)

Approved

10

Tier 1 candidates ready for the platform

Ready for first booking

8

Profile complete, photo, agreement signed, schedule shared

Completes first clean booking

5

Survives the field test

Becomes Tier 1 Verified Core

3

Three clean sessions with positive feedback

Track rejection reasons (provider learning data): unreliable communication, unclear pricing, weak boundaries, uncomfortable with villa visits, English mismatch with their target client, not interested in commission, can't travel, vibe mismatch. This becomes supply-side product feedback.

Minimum viable provider bench

Before flipping the V0 switch, the bench needs distribution — 10 providers all of the same type produces matching theatre.

3 strong Balinese / relaxation massage providers

2 deep tissue / therapeutic providers

2 villa / couples-capable providers

1–2 female providers for women customers

1–2 providers with conversational or fluent English

2 backup providers for evening windows

Provider minimum viable quality checklist

Arrives on time · Communicates clearly · Has own transport · Has oils/equipment · Signs no-sexual-services policy · Handles villa/hotel environment · Accepts cash and QRIS · Agrees to commission terms · Agrees to no medical claims · One reference or local recommender

English-level tagging

Basic: Provider can handle logistics in English but session conversation is limited. Matched to "quiet session" customers. Yuni sends pre-session brief in Bahasa.

Conversational: Can hold a session conversation. Matched broadly.

Fluent: Strong English. Premium villa, retreat-adjacent, and complex matching cases.

Private feedback only — no public reviews in V1

Public reviews create provider anxiety, punish new providers, and expose the platform to public disputes early.

After every session: match accuracy, pressure, energy, on time, rebook intent

Convert to public badges in V2: "Best for grounding" · "Strong pressure" · "Highly rebooked" · "Great for post-travel"

Never star ratings.

Part 9 — Safety: AI, Customer, Provider, Incident

Non-negotiable from booking one. Neskala sends people into private spaces. The platform's reputation, legal exposure, and ethical responsibility depend on getting this right before scale.

AI Safety Architecture

The AI is not one blob. It is a pipeline with a safety classifier in front. The classifier runs

before any recommendation.

AI Pipeline — V0

1. Safety classifier

2. Hard filter engine (availability, location, gender, language, certifications, budget)

3. Provider candidate retrieval (semantic search across remaining pool)

4. Soft ranking (state, archetype, feedback weights)

5. Explanation generator (two-sentence why-this-person)

6. Human override option (Yuni or Marcus can flip a match)

7. Audit log (raw intake, safety flags, providers considered, hard filters applied, final match, manual overrides — all stored)

AI Safety Kill-Switch — auto-escalate to human-only review

If the intake includes any of the following, the system halts automated matching and routes to human review. Customer sees: "Thanks — we want to match you safely. Our team will reach out within an hour."

Pregnancy (any trimester — only certified prenatal providers, manual confirmation)

Recent surgery or stitches

Chest pain, heart conditions, shortness of breath

Dizziness, fainting, balance issues

Severe pain, numbness, tingling, fever

Acute injury (sprain, fracture, recent fall)

Blood pressure issues or blood thinners

Medication that affects bodywork

Intoxication signals (slurred typing, current drug/alcohol use)

Trauma disclosure (PTSD, recent assault, abuse history)

Self-harm language or suicidal ideation

Anything involving minors — Neskala does not match minors in V0/V1

"I need medical help" or equivalent

Critical principle: The AI never decides that deep tissue is safe for a medical situation. It only ranks within a pool already pre-filtered by hard safety rules. The AI's job is fit, not safety.

Provider vetting minimum standards

Identity: KTP or passport, phone, address, photo, face matches ID

Reference: At least one known recommender. Yuni speaks to them.

Interview: 30–45 min structured intake (modalities, experience, boundaries, English, style)

Trial status: First 3 bookings monitored

Agreement: Signs no-sexual-services, no-medical-claims, boundary respect, incident reporting

Customer-side session safety

Customer provides hotel/villa address before confirmation

One boundary violation = permanent ban

Customer agrees to no-sexual-services terms before booking

First-time customers in private villas get a confirmation call from Yuni

Provider-side safety — symmetric, non-negotiable

The provider is also entering a private villa with a stranger. Good providers don't work with platforms that protect only customers.

Provider receives customer name, address, WhatsApp, booking details before accepting

Provider can refuse any booking — no penalty, no explanation

Late-night bookings (after 9pm) require extra approval; limited or disabled in V0

Optional check-in/check-out via WhatsApp for late-night or first-time villa sessions

Provider can leave immediately, full payment, if customer is intoxicated, sexual, aggressive, unsafe

Customer permanently banned after any sexual request or boundary violation — first time, no warning

Platform supports the provider in disputes. Default: believe the provider on safety claims.

Consent-to-share intake data

The customer may tell the AI: "I feel emotionally heavy after a breakup and don't want to talk." The provider does not need that text. They need a session-relevant brief.

Private intake text: stored internally, never shared by default

Provider-safe summary: only session-relevant details ("prefers quiet, nurturing session, avoid heavy conversation")

Explicit safety flags: injury, pregnancy, areas to avoid, boundaries — always shared

Optional share: customer can choose to share more context if they want

Customer sees what the provider will see before booking

Incident response protocol

Incident type

Response

Provider reports unsafe customer

Booking paused immediately. Customer statement collected. Customer banned if pattern or severity warrants. Default to believing the provider.

Customer reports boundary violation

Booking paused. Both statements. Refund decision. Provider suspended pending review. Escalated if serious.

Provider no-show or cancellation

Customer offered immediate alternative. Provider flagged. 3 strikes = removal.

Serious safety incident

Platform suspended for both parties. Statements collected. Authorities involved if required. No cover-up.

AI safety classifier failure (medical condition matched anyway)

Booking paused. Audit log reviewed. Classifier rules updated. Customer contacted by human. Provider not penalized — system failure, not theirs.

Refund and service guarantee policy

V0 Refund Policy (payment is direct customer-to-provider, so Neskala does not process automatic refunds)

Provider no-show: replacement provider or full booking credit. Provider strike (3 = removal).

Provider arrives 30+ min late without warning: customer offered Rp 50–75k platform credit toward next booking.

Service quality complaint: up to 50% future-booking credit at Marcus/Yuni discretion.

Customer cancellation 4+ hours before session: free.

Customer cancellation under 4 hours: provider may bill Rp 50–100k transport fee at their discretion.

Safety/boundary violation overrides all refund logic and triggers the incident protocol.

Cultural respect

Yuni and local cultural advisors decide what's appropriate to list. Marcus does not override.

Not every traditional practice should be productized. Some Balinese healing is not appropriate to commodify.

Balian listings require special permission, extended vetting, careful cultural framing.

No "ancient secrets," "mystic healing," or exoticizing copy in marketing.

Use Indonesian and Balinese language respectfully and accurately.

V2 consideration: a portion of Spirit-vertical revenue allocated to a Balinese cultural advisory fund or temple/community organization, named publicly.

Data privacy

Collect only what's needed for matching. No indefinite storage of emotional intake.

No selling, sharing, or using customer emotional/health data outside the match.

Customers can request deletion at any time.

Indonesia's Personal Data Protection Law (UU PDP) applies. Compliance scoping required before V1 public launch (Part 18).

Language to use and avoid

Use

Never use

Wellness support, relaxation, bodywork

Medical treatment or diagnosis of any kind

Grounding, restoration, nervous system support

Cure, heal, or fix as guaranteed outcomes

Spiritual guidance and personal ritual

Treat anxiety, depression, trauma, or addiction

Preference-based matching

AI diagnosis or medical recommendation

For serious concerns, consult a qualified professional

Any claim Neskala replaces professional care

Part 10 — Business Model and Unit Economics

The Premium Tier — the customer who pays Rp 4M for a healer they trust

Earlier drafts capped healer pricing at Rp 1M. That captured the floor. It missed the ceiling.

Bali has a real premium-healer market. Practitioners with deep word-of-mouth chains charge Rp 1.5M–4M per session and are fully booked through referral alone — no Instagram, no platform, no SEO. Customers who pay these rates are usually long-term residents (Track C), repeat-visit nomads (Track B), or specific high-trust seekers (Track A premium subset). They do not price-shop. They wait weeks for the right person.

Yuni's network already includes some of these practitioners — a Russian healer doing Karsai work, a master practitioner named Amaji whose bookings are referral-only, and others. This tier is real, structurally different from the standard pricing table, and v6.3 names it explicitly.

Premium tier session types and pricing

Premium specialist healer (60 min): Rp 1.5M–2.5M, provider receives Rp 1.1M–1.85M, platform 25–30%

Master practitioner (90 min): Rp 2M–3.5M, provider receives Rp 1.4M–2.45M, platform 30%

Top-tier ceremonial healer or specialist: Rp 3M–4M+, provider receives Rp 2.1M–2.8M, platform 30%

Premium couples (90 min, two practitioners): Rp 1.5M–2.5M, providers receive 75%, platform 25%

Why this changes the business shape:

A single premium booking can produce more platform margin than 5–10 standard massage bookings.

Premium customers write the testimonial that closes the next premium customer. The dataset effect is concentrated here.

Premium providers are the ones whose endorsement recruits other premium providers. The supply-side network effect is concentrated here too.

Premium customers are predominantly Track C (residents) and high-trust Track B (nomads). Track A tourists at premium tier exist but are fewer.

Premium tier is V0 only by introduction, not by primary distribution. We do not chase Rp 4M bookings in the first 30 days — but if Amaji is on the bench and a long-term resident asks for her, we route the booking and we capture the data.

Tiered pricing — and the right take rate per tier

Session type

Customer price

Provider receives

Platform take

Take %

Standard 60-min massage (direct app)

Rp 350,000

Rp 280,000

Rp 70,000

20%

Matched massage (via villa partner)

Rp 400,000

Rp 280,000

Rp 120,000 (villa Rp 25–50k)

30% gross

Premium matched therapist (90 min)

Rp 500,000

Rp 375,000

Rp 125,000

25%

Couples massage (in-villa, 60 min)

Rp 800,000

Rp 600,000

Rp 200,000

25%

Spirit / healer session (60 min)

Rp 700–1,000k

Rp 500–700k

Rp 200–300k

28–30%

Concierge fee (complex match)

Rp 75–150k flat

Provider full rate

Flat fee

Variable

FX conversion (V2)

+2–4% surcharge (disclosed)

Full IDR

FX margin

2–4%

The real money is in couples, premium therapists, healer sessions, villa-partner bookings, and (V2) the FX conversion layer. The matching output should default to premium and 90-minute options, not the Rp 350k floor.

Contribution margin per booking — the truth after costs

Booking Type

Platform Gross

Referral Fee

Yuni Ops

Pmt Fee

Refund Reserve

Est. Net

Direct Rp 350k

Rp 70k

Rp 0

Rp 10–15k

Rp 0–8k

Rp 5k

Rp 42–55k

Villa-referred Rp 400k

Rp 120k

Rp 25–50k

Rp 10–15k

Rp 0–10k

Rp 5k

Rp 40–80k

Premium Rp 500k

Rp 125k

Rp 0–35k

Rp 12–18k

Rp 0–12k

Rp 8k

Rp 52–105k

Couples Rp 800k

Rp 200k

Rp 30–80k

Rp 15–20k

Rp 0–20k

Rp 10k

Rp 70–145k

Healer Rp 1m

Rp 250k

Rp 0–75k

Rp 20–25k

Rp 0–25k

Rp 20k

Rp 105–210k

The hidden truth metric: Net IDR per Yuni-minute

Net IDR per ops minute = net platform margin / total human coordination minutes

This is the single number that determines whether the model can scale. v5 listed time-cost accounting in the abstract. v6 makes it the headline KPI for the 30-day sprint.

Targets:

Week 1: Rp 1,000–2,000 / minute (acceptable while learning)

Week 4: Rp 3,000–5,000 / minute (must be trending here)

V1: Rp 5,000+ / minute

Scale: Rp 8,000–10,000+ / minute

If a Rp 350k session nets Rp 50k margin and takes 45 minutes of coordination, that's Rp 1,100/min — bad. If a Rp 800k couples session nets Rp 100k and takes 12 minutes, that's Rp 8,300/min — interesting. The matching output should push customers toward the high-IDR-per-minute SKUs by default.

Track failed bookings too. Time spent on requests that don't convert is real ops cost. A marketplace dies in those gaps.

CAC — both sides of the marketplace

Cost

What it includes

V0 estimate

Provider Acquisition Cost

Yuni outreach + interview + photo + profile + first-3-booking monitoring + onboarding bonus

~3–5 hours of Yuni time + Rp 75–100k bonus per approved provider

Customer Acquisition Cost (villa-referred)

Villa partner relationship time + flyer/QR + per-booking referral payout

Rp 25–50k per booking + amortized partner-pitch time

Customer Acquisition Cost (nomad/social)

Coworking partnership, Instagram, WhatsApp group seeding

~10–20 min admin time per inbound + occasional gifted session

Customer Acquisition Cost (resident)

Existing-customer referral credit, community word-of-mouth

Lowest CAC of the three tracks once flywheel begins

Revenue streams

Stream

How it works

When live

Booking commission (20–30%)

Standard cut on every completed session, varying by tier.

Day 1

Villa referral split

Test Rp 25k / Rp 50k / 10% to find adoption sweet spot.

Month 2

Concierge fee

Flat Rp 75–150k on Spirit/complex bookings.

Month 3

FX conversion (V2)

2–4% on foreign card payments via Midtrans/Xendit.

V2 (months 5–8)

Featured provider placement

Monthly fee for better match visibility.

Year 2

Provider tools / SaaS layer

Scheduling, customer notes, income tracker.

Year 2+

City licence (expansion)

Operators in new hubs pay rev-share to use platform.

Year 2+

Booking volume targets — conservative

Milestone

Bookings/month

Gross platform revenue/month

Notes

30-day validation

10–20

Rp 1–2m

Real go signal: 20 requests, 10–15 paid (see Part 16)

Month 3

50–100

Rp 4–10m

Body stable. Spirit soft launch.

Month 6 base

150–300

Rp 12–25m

Villa channel producing. Repeat customers appearing (residents track activating).

Month 6 stretch

500

Rp 40m

If one channel fires (likely resident referral)

Month 12

500–1,000

Rp 40–80m

Real business. Margin improving as couples/premium grow.

Year 2 base (multi-city)

2,000–5,000

Rp 160–400m

Platform revenue, not just Bali.

Part 11 — Provider Value Proposition

Without a real provider VP, Yuni is recruiting on personal goodwill alone — and goodwill does not scale to 30 providers.

Provider segmentation — who we actually want

The best V0 providers are not necessarily the most famous in Bali. They are the best

under-distributed providers with availability.

Good but under-marketed practitioners who can't fill their schedule

Good but weak-English providers who need translation and distribution

Villa-capable providers with weekday gaps

Practitioners who already work with foreigners but hate sketchy WhatsApp inquiries

Not the superstar already fully booked.

They don't need us. They won't perform on the platform.

The pitch to a provider

"Neskala fills your empty weekday slots with better-screened foreign clients. You stay independent. You only pay commission when a booking happens."

"We screen out sketchy customers before they reach you. We translate your style into English. We send you clients who fit your style — not random walk-ins. You can refuse any booking. Your feedback is private; no public reviews. If a customer crosses a line, they're banned, not you."

Provider benefits in plain terms

Better-fit clients — pre-matched to your archetype and style, not random walk-ins

Fewer sketchy WhatsApp inquiries — we screen for sexual-services language and intoxication before you see the booking

Weekday and dead-hour bookings — most providers are full Friday-Sunday and starving Tuesday-Thursday afternoon

English-language marketing without you needing English fluency

Villa and tourist customer access without your own SEO or Instagram strategy

Higher-ticket bookings — couples and premium villa customers routed to qualified providers

Foreign card payment access in V2 — solves the single biggest tourist pain point

Private structured feedback you can learn from — not public 4.3 stars

No exclusivity required — keep your own clients, social media, word-of-mouth network

Marketplace leakage — the honest position

If we send a great therapist to a villa and the customer asks for the therapist's WhatsApp, we don't police it. The customer's ongoing relationship with that practitioner is theirs.

Two things make this manageable:

Tourist churn. Track A turns over every 3–14 days. Most customers never come back. Neskala is an acquisition engine more than recurring revenue per tourist.

On-platform value > off-platform value. In V2+, the provider settling foreign cards through us gets the customer's transaction handled cleanly. The customer who books direct via WhatsApp pays cash or sends a confused IDR transfer. The platform offers something the side channel can't replicate.

In V1, we don't fight leakage. In V2, we make leakage worse for both sides than staying on-platform.

For the resident track (C), leakage matters more. Residents book monthly. Their lifetime value is real. The V2 payment rail and provider-side scheduling tools become the retention mechanism specifically for the resident segment.

Provider exclusivity — phased, not demanded early

V0: Providers take bookings anywhere. We compete on quality of inbound, not exclusivity.

V1: Top performers get "preferred" status — better matching weight, profile placement, premium-booking priority.

V2: Benefits for priority availability — guaranteed minimum bookings/month for first-availability commitments.

V3: Optional exclusive relationships with top performers, with structured economics.

Part 12 — Villa Partner Value Proposition

v5 had a customer VP and a provider VP. The third side of the marketplace was missing. The villa partner is not a passive referrer — they are a customer of the system. Without their adoption, the wedge doesn't work.

The pitch to a villa or guesthouse

"Give your guests a better wellness recommendation without managing therapists yourself. We handle the matching, vetting, confirmation, and feedback. You earn a referral fee on every completed booking."

"One QR card at reception. Free to refer. Vetted local practitioners only — never anyone we wouldn't send to our own friends. We confirm every booking by WhatsApp before anyone shows up at your villa. Issue resolution within an hour, by us, not by you."

What villa managers actually need

Simple QR card and one-page partner packet

WhatsApp referral link (their unique referral code embedded)

Commission tracking visible to them

Payout clarity — bi-weekly, IDR, no surprises

"What to tell guests" script — single paragraph, memorable

Confidence that providers won't embarrass them in front of their guests

Fast issue resolution — Yuni responds within an hour during operating hours

No dashboard required in V0 (overkill); maybe a simple partner page in V1

Villa partner benefits

Better guest experience — guests who get matched well rate the stay higher

Zero operational burden — no therapist management, no scheduling, no cash handling

No need to maintain a personal therapist list or worry when their guy is unavailable

Trust-safe vetted providers — the villa's reputation is protected

Referral revenue on every completed session — additive income stream

Backup providers when their existing referral isn't available

Fast WhatsApp support if anything goes wrong

Beating the "we already have our guy" objection

Many villa managers already refer guests to a therapist they trust. Our pitch is not to replace that. It's to complement it.

"Keep referring Made when he's available. Use Neskala when he isn't, when the guest needs a couple's massage Made doesn't do, when the guest wants something specific Made can't offer, or when the guest wants a female therapist. We're your backup and your range — and you earn commission either way."

Villa partner economics — to be tested, not assumed

v4/v5 assumed Rp 20–30k per booking. That's likely too low. Test three offers in the first month:

Tier A: Rp 25k flat per completed booking — baseline

Tier B: Rp 50k flat per completed booking — generous

Tier C: 10% of booking value (Rp 35–80k depending on tier) — performance-aligned

After 4 weeks, we know which structure drives adoption. The villa-referred customer price can rise to Rp 400–450k to absorb the higher referral.

Channel sequence beyond villas

Yoga studios and wellness cafes — post-yoga recovery, intent already activated. Counter cards, small posters.

Coworking spaces (for the nomad track) — Outpost, Tropical Nomad, Dojo Bali, BWork. Their members are the nomad customer.

Existing-customer referrals (for the resident track) — booking credit for both referrer and referee. The cheapest CAC by far.

Provider referrals — therapists know therapists. 5% of new provider's revenue for 3 months to whoever referred them.

Micro-influencers — yoga teachers, retreat facilitators, villa managers, Bali TikTok creators, WhatsApp group admins. High trust per follower beats raw reach.

SEO (V1, plant seeds early) — "AI-matched massage Ubud," "in-villa massage Ubud," "post-yoga massage Ubud," "find a healer in Bali." Compounds slowly, pays off Year 2.

Part 13 — Landing Page Copy

For a product where the first screen is the conversion event, the actual copy matters more than another architectural diagram. v5 talked about "trust surfaces" abstractly. v6 writes them.

The first screen, V0

Headline:

Feel sore, tired, or overstimulated? We'll match you with a trusted Bali bodywork practitioner.

Subhead:

Tell us how your body and mind feel today. We'll recommend three vetted local practitioners who fit your needs, your preferences, and your villa.

Trust row (a single horizontal strip of small icons + text):

Personally vetted practitioners

In-villa or in-area sessions

WhatsApp confirmation before anyone arrives

You choose gender preference

Wellness only — never sexual services

Cash or QRIS direct to provider

Primary CTA:

Find my match →

Secondary link:

How it works

Trust copy principles

Calming, not legalistic. The customer's instant fear is "am I about to invite a random person to touch my body in my villa?" Answer it with warmth, not waivers.

Six trust cues maximum. More feels like an insurance form. Fewer feels suspicious.

No medical claims. "Wellness support" not "treatment."

Specific over abstract. "WhatsApp confirmation before anyone arrives" beats "trusted process."

After the click — what they see next

Single open question. No form. No dropdown.

"Rough day? Tell us how your body and mind are feeling right now."

Free text or voice input. Then 1–2 follow-ups. Then three matches with two-sentence explanations. Then booking. The whole flow: under 90 seconds.

Confirmation page copy

"Got it. Yuni from our team will message you on WhatsApp within 30 minutes to confirm Wayan's availability. She'll send a short brief about what to expect, the address she's coming to, and how to pay (cash or QRIS, direct to her). If anything changes, message us back."

Part 14 — V0 Build Specification

The minimum version that tests the core hypothesis. Build the architecture to scale gracefully. Operate manually behind the scenes. One-week tech sprint by Marcus, finished — including landing page copy — before Yuni begins field recruitment. The working app is the recruiting pitch and the credibility artifact. Yuni demos a real product to providers and partners; she does not pitch a future one.

Build sequence — full vertical slice, then polish

Day 1–2: Skeleton vertical slice

Landing page with QR target — placeholder copy fine for now

Provider database schema in Postgres (Replit/Supabase)

Single Claude API call for intake parsing → match output

Booking request form → admin table

Yuni admin dashboard — bookings list, status, provider assignment

Manual WhatsApp link generation (not automated send)

Day 3–4: Safety and provider intake

Hard-code AI safety classifier kill-switch list — runs before matching

Audit log for every match decision

Provider onboarding form (auto-populates DB from Yuni's field interviews)

Yuni voice-memo capture: WhatsApp bot transcribes 60-second voice memos and structures into provider DB. Removes the SPOF risk of provider info living only in Yuni's head.

Trust surfaces on landing page (Part 13 copy)

Day 5–7: Polish and end-to-end test

Match output design — three cards, two-sentence explanations, screenshot-worthy

Private feedback form — sent 30 minutes after session end time, includes counterfactual questions

Net IDR per minute logging built into ops dashboard

End-to-end dry run with Marcus and Yuni as fake customer + fake providers

Mobile QA on iPhone Safari and Android Chrome

Database schema

Table

Key fields

providers

id, name, photo, bio, location, travel_radius, archetypes[], tier, modalities[], pressure_style, energy_style, best_client_types[], languages[], english_level, gender, certifications, availability_notes, price_range, own_words, boundaries_notes, internal_notes, customer_track_fit[]

provider_services

provider_id, service_name, duration_mins, price_idr, description

customer_intakes

id, created_at, raw_input, extracted_state, body_areas, desired_outcome, energy_pref, woo_level, safety_flags, gender_pref, language_pref, location, budget, timing_pref, contact, customer_track (A/B/C)

safety_audit_log

intake_id, classifier_flags, hard_filters_applied, providers_considered, final_match, manual_overrides, timestamp

match_results

id, intake_id, provider_1_id, provider_1_explanation, provider_2_id, provider_2_explanation, provider_3_id, provider_3_explanation, manual_override_notes

booking_requests

id, intake_id, matched_provider_id, requested_datetime, location, status, payment_method, commission_idr, referral_partner_id, time_to_book_mins

booking_status_events

booking_id, status, timestamp, notes

referral_partners

id, name, type (villa/coworking/yoga/cafe/customer), location, contact, referral_code, fee_structure, total_bookings, total_payout_idr

provider_feedback

booking_id, match_accurate, energy_right, pressure_right, on_time, rebook_intent, private_notes, submitted_at

customer_feedback

booking_id, overall_rating, match_accurate, would_have_booked_without_explanation, trust_increase_from_explanation, would_have_preferred_browse, notes, customer_quote, submitted_at

commissions

booking_id, gross_idr, platform_idr, provider_idr, referral_idr, payment_fee_idr, net_idr, settled

ops_time_log

booking_id, yuni_minutes, marcus_minutes, whatsapp_message_count, failed_match_attempts, net_idr_per_minute

The automation boundary — calendar-backed, not calendar-automated.

Architect for the future. Operate manually until reality earns automation. The system has a calendar internally, but it does not trust the calendar enough to autonomously promise reality to the customer. Yuni confirms availability via WhatsApp before any booking is final. The match output explicitly says “availability to be confirmed.”

This is a deliberate CTO decision, not a limitation. A calendar that lies is worse than no calendar. Provider availability in independent Bali wellness work is fundamentally WhatsApp-first — therapists do not maintain live schedules and will not in V0. Building the customer experience around a fake live calendar would create the trust problem the product is supposed to solve.

V0 builds the full state machine and admin tooling. It does not expose autonomous booking to the customer.

Booking state machine

Build the full state machine on day one. The customer experience is constrained, but the architecture is real.

V0 booking state machine

intake_started → match_generated → customer_requested → provider_pending → provider_confirmed → customer_pending → customer_confirmed → completed → commission_settled

Cancellation paths:

any_state → canceled_by_customer (free if >4hr; transport fee allowed if <4hr)

any_state → canceled_by_provider (provider strike; replacement offered)

scheduled_state → no_show_customer (provider may bill transport fee)

scheduled_state → no_show_provider (full credit; 3 strikes = removal)

any_state → rescheduled (returns to provider_pending)

Issue paths:

any_state → issue_reported → under_review → resolved_refund_credit / resolved_no_action / escalated

any_state → safety_incident (overrides all other paths; triggers Part 9 protocol)

Allowed transitions are enforced in the database, not just the UI. Every state change writes to booking_status_events with timestamp, actor, and reason. This is the audit trail for both operations and (eventually) regulatory inquiry.

What V0 does not expose yet

The system is built for it. The customer-facing surface area is deliberately constrained.

No provider-facing self-serve calendar. Therapists do not maintain live availability. Yuni confirms via WhatsApp every time. V1 may add availability ping to top-tier providers. V2 may add real provider-side calendar tooling. V3 may add it for everyone.

No automatic booking confirmation. Match output is provisional. Yuni confirms with provider, then with customer. The two-step confirmation is the trust mechanism in V0.

No payment custody or platform escrow. V0 is cash/QRIS direct customer-to-provider. V2 introduces deposits via Midtrans/Xendit. V3 introduces full marketplace payments and FX rails.

No provider portal beyond a structured profile. Providers don't log in to anything in V0. They get WhatsApp messages from Yuni. V1+ may add a basic dashboard for top performers.

No instant book anywhere in the customer flow. The closest we get is “available within 24–72 hours” with provisional matching. Same-day instant confirmation is a V2+ question.

No public reviews or star ratings. Private feedback only in V1. Public badges in V2.

No autonomous safety decisions. AI flags route to human-only review.

“Architect for the future. Operate manually until reality earns automation.” The first time a piece of automation is allowed to go live is when the manual version has produced enough data to write the rule with confidence.

Booking status flow

requested → reviewing → provider_contacted → provider_confirmed → customer_confirmed → completed → commission_settled

Cancellation: canceled_by_customer · canceled_by_provider · no_show_customer · no_show_provider

Issue: issue_reported → under_review → resolved_refund_credit · resolved_no_action · escalated

AI architecture — keep it boring

V0 uses a single Claude API call with a structured prompt that handles safety classification, state extraction, hard-filter generation, and explanation writing. Postgres handles provider retrieval. No CrewAI, no AutoGen, no multi-agent framework.

Reasoning: Multi-agent frameworks add debugging surface area we don't need at 10–50 bookings. The director-model thesis says ship fast, not architect like a Fortune 500. We add complexity when volume justifies it.

Part 15 — First 20 Booking Playbook

Step

Who

Action

1

Customer

Scans QR from villa, cafe, coworking, or yoga studio. Lands on Neskala mobile web.

2

Customer

Sees landing page (Part 13). Submits intake.

3

AI

Safety classifier runs first. If flagged, routes to human-only review.

4

AI + Marcus

AI generates 3 matches with explanations. Marcus reviews, can override (V0 supervised matching).

5

Customer

Sees matches. Reads explanations. Picks one or 'You choose.' Submits booking with timing, location, contact.

6

Yuni

Receives booking in admin dashboard. Checks provider availability via WhatsApp.

7

Yuni

If unavailable: offers next match. If available: confirms with provider, sends customer-safe brief.

8

Yuni

Confirms to customer via WhatsApp: provider, time, what to expect, payment.

9

Customer + Provider

Session happens. Customer pays provider direct — cash or QRIS.

10

Yuni

Sends private feedback form 30 minutes after session end. Includes counterfactual questions.

11

Yuni

Records commission. Marks complete. Logs ops minutes. Captures customer quote.

12

Marcus

Reviews feedback weekly. Updates provider weights. Iterates intake or match logic.

The learning from steps 10–12 is more valuable than the revenue from step 9. First 20 bookings are a research sprint, not a revenue sprint. What we learn about how customers describe state, which match explanations build trust, and which provider archetypes perform — that data shapes everything that follows.

Part 16 — The 30-Day Validation Sprint

This is a research sprint, not a launch.

What the sprint tests

Do customers prefer matched booking to browsed booking? Counterfactual survey on every booking.

Does the match explanation increase trust? Direct question, every customer.

Do providers value our distribution? Provider satisfaction survey at week 2 and week 4.

Does Yuni enjoy the field work? As important as any booking metric.

Is net IDR per Yuni-minute trending up? The hidden truth metric.

Do all three customer tracks show signal? Tourist track must produce. Nomad track must show repeat. Resident track must surface even one referral.

Validation thresholds

Minimum learning signal (proceed with caution)

10 booking requests

5 completed paid sessions

Counterfactual survey returns directional answer

Real go signal — all must be true to proceed to Phase 1

20 booking requests received

10–15 completed paid sessions

10 providers onboarded with full profiles, distribution per Part 8 bench

3 referral partners (villa/coworking/cafe) actually generating leads

70%+ customers say match felt right for their state

50%+ customers say match explanation increased trust

30%+ customers say they would rebook (high bar for tourist churn)

70%+ providers say they want more bookings through the platform

Yuni minutes per booking trending below 30 by week 4

Net IDR per Yuni-minute > Rp 3,000 by week 4

Yuni honest self-assessment: work felt energising, not draining

Marcus honest self-assessment: build felt creative and manageable

Stop criteria

Signal

Meaning

Yuni finds provider recruitment uncomfortable or draining

Wrong role fit. Restructure or stop before equity conversations.

Providers consistently cancel or go unreliable

Supply quality issue. Fix vetting before scaling.

Customers only want cheapest massage, no interest in matching

Value prop not landing. Counterfactual survey will reveal this.

No bookings after 4 weeks of real distribution

Discovery problem. Rethink acquisition channels before building more.

Safety incident in first 10 sessions

Stop immediately. Review and fix before any new bookings.

Counterfactual survey shows match explanation does not increase trust

Matching layer may be decorative. Rethink core thesis before building further.

Net IDR per Yuni-minute not trending up by week 4

Coordination cannot scale. Automation required before volume.

Customer quote capture for marketing

Every good session should produce a line of copy. After feedback:

"In one sentence, how did this match feel?"

If the product works, customers will write the marketing. "It felt like she knew exactly what I needed" beats any landing page tagline we'd write ourselves.

Part 17 — Roles, Compensation, Kill-Fee, Equity

Ownership — honest and clear

This is Marcus's company. Marcus is founder, builder, majority owner, and strategic decision-maker. Yuni is the first and most important early team member. The structure reflects that honestly rather than using co-founder language that creates expectations neither party can fulfill.

Marcus — Founder, Builder, Majority Owner

Yuni — Field Operations Lead, Early Team

Owns the company and the system

Recruits and interviews providers in Bali

Builds the app and AI matching logic

Verifies provider quality — vibe, reliability, safety

Designs provider database and onboarding

Builds referral relationships with villas, guesthouses, coworking, studios

Builds admin dashboard and payment infrastructure

Places flyers and materials at distribution points

Sets product direction and technical decisions

Coordinates all bookings manually in V0 and V1

Manages future investors and advisors

Collects session feedback from customers and providers

Handles English-facing brand, marketing, copy

Manages provider communications (Bahasa first)

Controls equity and financial decisions

Is the local face and voice of Neskala in Bali

Staged compensation — earned, not assumed

Principle: do not replace Yuni's Marco income until the role earns it.

Run a trial first.

Phase

Timing

Compensation

Phase 0: Trial

30 days, part-time

Project stipend Rp 1.5–2m. Per-provider bonus Rp 75–100k per approved onboarding. Per-booking bonus Rp 15–20k. No base salary. No equity. Keep Marco job.

Phase 1: Part-Time Launch Lead

After 10+ bookings confirmed

Rp 2.5–3.5m/month base (part-time). Provider, booking, partner bonuses continue. 90-day review. Still no equity.

Phase 2: Full-Time Bali Ops

After 50+ bookings/month, clear demand

Rp 4–4.5m/month base — replaces Marco income. Full-time. Booking, provider, villa bonuses. 90-day review. Phantom equity or profit-share discussed.

Phase 3: Head of Bali

After 150+ bookings/month, expansion signal

Rp 5–7m/month base. Performance bonus. Formal vesting equity begins.

Kill-fee — protecting Yuni

If Marcus stops the experiment for any reason during or after the 30-day trial, after Yuni has completed agreed fieldwork, kill-fee is calculated:

Rp 500,000 per onboarded provider (Tier 1 or Tier 2 with at least one clean booking)

Rp 1,000,000 per signed villa or coworking partner producing at least one lead

Capped at Rp 8,000,000 total

Plus all unpaid project stipend amounts

Plus all earned per-provider and per-booking bonuses

Provider relationships she built remain hers — she can take them anywhere

This is non-negotiable and written into Phase 0 from the start. Tying it to fieldwork completed (rather than a flat number) means it scales with her actual contribution. The relationship matters more than the project.

Equity — conservative and earned

Stage

Equity available

Condition

30-day trial

0%

No equity during trial. No exceptions.

90 days post-trial

1–3% phantom equity or profit-share

After 90 days of Phase 1/2 with positive metrics and both parties satisfied.

6–12 months

2–5% formal vested equity

After consistent execution, provider network growth, booking volume. 2-year vest.

Head of Bali (Year 2)

Up to 5–8% total

If she becomes the irreplaceable operator for Bali and expansion training. Annual review.

Mitigating key-person risk

If Yuni becomes the only person who knows the providers, the company has a single point of failure. From day one:

Provider info goes into the database — never lives only in Yuni's head or phone

Yuni's voice-memo capture system structures her interviews into DB records automatically

All agreements are documented in writing

Provider relationships are warm with Yuni but contractually with Neskala

By Month 3, another person should be able to read the database and operate without her

Referral commission program

Provider referrals: 5% of new provider's booking revenue for 3 months to whoever referred them

Customer referrals: Booking credit to customers who refer first-time bookers (especially important for the resident track)

Villa/coworking/cafe partners: Tested at Rp 25k / Rp 50k / 10% — adopt whichever drives partner adoption

City field agents (expansion): Same commission-first model as Yuni in Phase 0 — prove before base salary

Part 18 — Payment Roadmap, Legal, Entity, and Insurance

Payment roadmap

Phase

Payment model

V0 (30 days)

Cash or QRIS direct customer-to-provider. Neskala tracks commission manually. Zero payment custody, zero complexity, zero chargeback risk.

V1 (months 2–4)

Optional booking deposit via bank transfer. Commission recorded manually. Provider paid at session or within 24 hours.

V2 (months 5–8)

Payment links via Midtrans or Xendit. Platform collects booking fee upfront. Provider settlement within 24–48 hours.

V3 (Year 2)

Full marketplace payments. Automated split. FX conversion: foreign card received, IDR distributed to provider bank account. Payment moat becomes real.

Use Midtrans or Xendit for Indonesian payment infrastructure. Both support GoPay, QRIS, bank transfer, cards, e-wallets. Xendit publicly markets marketplace/platform payment flows. Not Stripe — limited Indonesia support.

Payment custody risk

The moment Neskala collects full customer payment and later pays providers, complexity rises sharply.

V0 keeps it simple: customer pays provider directly. Manual commission tracking. No custody. No chargeback. No refund processing. No PCI exposure.

V2 introduces deposits and payment links. V3 explores split payouts. Each step requires:

Local legal review

Indonesian accountant sign-off

Refund and dispute policy update

Provider agreement update

Tax treatment confirmation

Do not accidentally become a payments company before we are ready.

Legal questions to resolve before V1 public launch

These don't block V0. They block scaled V1 operation.

What entity owns brand, code, data, and customer relationships? Eagle Rocket LLC, Indonesian PT, local partner structure, or other?

What can Marcus legally operate in Indonesia on his current visa status?

Does Neskala need Private Scope PSE registration through OSS/RBA per Komdigi guidance? At what user threshold?

Does Indonesia's UU PDP require specific compliance steps for emotional state, location, pregnancy/injury, and astrology data?

Are providers contractors, platform vendors, or something else under Indonesian labor law?

Who is liable if a customer is injured during a session?

Is professional liability insurance available for in-villa wellness in Bali, and at what cost?

What customer ToS and provider agreements are enforceable under Indonesian law?

What tax applies to platform commission? GST? PPh? Are referral commissions deductible?

How are referral commissions to villa partners documented and taxed?

What happens to customer/provider data if the company is sold or shut down?

Action: Month 2 of V0 — retain a Bali-based startup lawyer for a 2-hour consultation to scope which questions matter for current operations and which need solving before V1 public launch. Budget: Rp 5–10m for initial scoping.

V0 positioning

During the 30-day test, Neskala is positioned as: a small private referral and concierge experiment for vetted wellness sessions.

Not yet a public marketplace. This gives operational and legal flexibility while we learn. Public marketplace positioning waits for V1, after legal scoping.

Part 19 — Global Expansion (Earned After Bali)

Expansion Rule: Do not launch a second city until Bali hits all of these.

100 completed bookings · 30+ verified providers · Repeat booking rate established (resident track active) · 10+ referral partners active · Local operator playbook documented · Customer satisfaction above 80% · No major safety incidents · Yuni confirmed as stable Bali lead · Legal/PSE/PDP compliance scope resolved

Target expansion hubs

Hub

Why it fits

Launch approach

Bali, Indonesia

Proof of concept. Deepest supply, strongest demand, Yuni on the ground.

Build the model here. Earn the right.

Koh Phangan, Thailand

Spiritual tourism, growing wellness infrastructure, high foreigner density.

3-day visit. 15 providers. 5 referral partners. Hire local field agent.

Rishikesh, India

Yoga capital. Ashram culture. Growing international market.

Requires local Indian ops partner — Yuni cannot scale here solo.

Goa, India

Long-stay foreigners, healing scene, techno and wellness crossover.

Similar playbook to Koh Phangan. High expat density.

Tulum, Mexico

Wellness boom, more competitive. Enter only after two Asia hubs are stable.

Later stage.

Lisbon / Madeira

Digital nomad + wellness crossover. Different product shape.

Different intake design needed. Year 3.

City launch playbook

3–4 day visit by Marcus, Yuni, or trained local operator

Walk every wellness studio, healer space, retreat centre, guesthouse. Onboard 10–15 providers in person.

Sign 5 villa or coworking referral partners before leaving.

Add city to app, flip switch, launch. Core matching product unchanged.

Hire local field agent on Phase 0 commission model.

Wedge → expansion logic

Massage proves same-day trust-sensitive matching works

Premium and couples prove higher AOV is reachable

Resident track proves recurring revenue and longitudinal data

Spirit proves deeper matching and higher willingness to pay

Other hubs prove city-launch repeatability

Provider tools prove SaaS expansion potential

Part 20 — Vadim and the Advisor Approach

Who Vadim is

Vadim is a Ukrainian founder in Canggu who built and scaled GigRadar.io — a SaaS platform Marcus was one of the first customers of. Real operational SaaS experience, in Bali, with a network of villa contacts, expat operators, payment stack people, and local dev talent.

Right posture for the lunch

Not: "I have this big Bali wellness platform idea, want to invest?"

But: "I'm testing a tiny AI-matching experiment for Bali wellness. First wedge is Ubud villa-referred massage. Customer says how they feel, system matches them with the right provider. Trying to validate 20 paid bookings before building anything big. Want your operator brain on whether this is a real wedge or a tourist toy."

Questions to ask Vadim

"Does this sound like a real wedge or a tourist toy?"

"How messy and expensive was supply acquisition at GigRadar?"

"Would you build this as marketplace, SaaS, or agency-assisted marketplace?"

"What would make you kill this idea completely?"

"Where is the false moat — what looks defensible but actually isn't?"

"What metric would prove this is more than a service business?"

"Who in Bali should I talk to about Indonesian PT structure, PSE registration, contractor status?"

"Who else in Bali should I talk to that I'm probably not thinking of?"

The text to send him

"Hey man, we should finally get that lunch. I'm in Bali riffing on a new AI/local services idea and I'd love your operator brain on it."

"Not pitching, not raising. Tiny validation experiment: AI-powered wellness matching for Bali. Customer says how they feel, system matches them with the right massage therapist or healer. First wedge is Ubud villa-referred in-villa massage. Trying to validate 20 paid bookings before building anything bigger."

"Could grow into massage/healers/events/local services if it works, but I'm staying disciplined. Would be great to get your marketplace sanity check."

Keep Vadim in advisor lane — not investor — until there is a working landing page, 10 provider profiles, first booking attempts, and actual customer feedback. No equity talk until there is something to price.

Part 21 — Risk Register (Top 7, Ranked)

v5 had 16 entries. That's anxiety, not a risk register. v6 ranks the seven that actually matter, with two starred existential.

Rank

Risk

Severity

Mitigation

★ 1

AI safety classifier misses a medical flag

Existential

Hard-coded kill-switch list, audit log, conservative defaults — when in doubt, route to human review. Reviewed weekly.

★ 2

Safety incident in a private villa

Existential

Vetting protocols, provider agreement, check-in/check-out option, ban policy, incident response operational before first booking.

3

Counterfactual survey shows match explanation doesn't increase trust

High

Stop and rethink core thesis. Could mean we have a concierge business, not a venture business. Both are valid; we want to know which.

4

Yuni finds the field work draining

High

30-day trial before salary or equity. Kill-fee protects her downside. Honest weekly check-ins.

5

Marcus becomes shadow operator

High

Clear role separation in Part 17. If Marcus is coordinating bookings, stop and restructure.

6

Cultural backlash on Spirit vertical

High

Yuni and local advisors gate-keep healer category. V2 cultural advisory fund. Body-only for first 60 days.

7

Providers cancel or go unreliable

Medium

Quality tiers, trial status, backup providers, no last-minute unverified bookings

Part 22 — The Name

Working title: Neskala. A blend of Niskala (the unseen, spiritual) and Sekala (the visible, physical). It holds both — body and spirit, tangible and intuitive.

Final name is Yuni's decision, after cultural validation.

v6 explicitly does not lock the name. The risk is whether Balinese people feel it is respectful, awkward, fake, sacred, or tourist-coded.

Name

Why it works / risks

Check

Neskala (working title)

Deep Balinese roots. Phonetically clean. Covers body and spirit. Risk: tourist-coded mispronunciation, may feel like exoticizing.

Yuni asks 2–3 Balinese people: respectful or appropriative?

Rasa

Indonesian for feeling/sense/taste. "Tell us your rasa." Conceptually strongest.

rasa.com taken by enterprise AI. Check rasa.app, rasa.id, IG, TikTok.

Pulih

Recover/restore. Strong wellness connotation.

Slightly medical. Yuni's gut check.

Teduh

Sheltered, calm, shaded. Evocative and warm.

Less obvious. Good for premium.

Selaras

Harmony/alignment. Elegant.

Harder for foreigners to spell.

Yuni names this. Before locking: domain (.com, .app, .id), Instagram, TikTok. 2–3 Balinese gut reactions in 10 seconds. Rasa is conceptually strongest if domains work; Neskala is the elegant compromise.

Part 23 — What Happens This Week

The most important question first — for Yuni.

Does recruiting massage therapists, meeting healers, pitching villas and coworking spaces, and coordinating bookings sound like work you want to do? Not "could you" — does it actually sound alive and interesting? If uncertain: talk about it. No answer needed today.

This week — Yuni (if yes)

Read this document fully. Ask questions about anything unclear or that doesn't feel right.

List 10 massage therapists you know or know of in Ubud. Name, contact, style. First provider candidates.

List 5 villas or guesthouses where you have a personal contact. First referral partner targets.

List 2–3 coworking spaces in Canggu/Ubud. Outpost, Tropical Nomad, Dojo, BWork. Nomad-track distribution.

Give Marcus your instinct on the name shortlist. Which feels right in Bahasa? Which sounds wrong? Ask 2–3 Balinese people.

This week — Marcus

Register the domain (neskala.com / .app / .id, plus rasa.app / rasa.id as backup)

Text Vadim. Message from Part 20. Set up the lunch.

Build the V0 prototype FIRST — one-week sprint, before Yuni recruits. Landing page (Part 13 copy), intake, match output, admin dashboard, provider onboarding form, AI safety classifier, audit log, voice-memo capture, counterfactual survey. End-to-end before polish. The working app is what Yuni shows providers and partners — not a manual concierge dressed up as software. The prototype is the recruiting pitch. No field recruitment until the demo works on her phone.

Hard-code AI safety kill-switch list on day one. Existential risk, cheap to build now.

Research Midtrans and Xendit. Understand V2 options. Don't implement yet.

Identify a Bali startup lawyer for Month 2 consultation on entity, PSE, PDP, contractor status.

A final word.

There is a version of this where we put Rp 700 million into a ruko in Gianyar and hope the landlord, the supply chain, the staff, and the franchise system all behave from a distance. That is a version I know how to do. I have done it. It cost me more than money.

This is a different version. Marcus builds the system. Yuni builds the network. The first test costs almost nothing and takes four weeks. If it works, we keep going. If it does not, we stop and Yuni gets a kill-fee scaled to the work she actually did, because the relationship matters more than the project.

Right now you are selling vegan cheese to restaurants in Gianyar. Same skill set. Just not the most interesting application of it. Bali has thousands of practitioners who are unknown, underpaid, and undiscovered. They are genuinely good at what they do. They just have no distribution. We can be that distribution — and the matching intelligence that makes the right person show up at the right villa, the right co-working space, the right resident's home, at the right time during their stay or their year.

That is a real thing to build.

— Marcus

Appendix A — Marcus-Only Strategy Notes

Not for Yuni. Delete before sending the doc to her. Keep a private copy.

This appendix exists because the project has a second purpose alongside the Bali business itself, and being honest about that with yourself is not the same as being honest about it with Yuni. Including this in the main document would let her wonder if the project is partially instrumental — even though her own answer would probably be "yes, of course, and that's fine."

The NYC builder narrative

This project is not just a Bali business experiment. It is a live case study that builds Marcus's positioning as an AI-native founder and technical builder entering the New York startup and VC ecosystem.

"I built an AI wellness matching platform in Bali. Validated it with real bookings across three customer tracks. Expanded to three wellness hubs. Here's how the matching logic works and what the somatic dataset looks like at 10,000 sessions."

That sentence covers: product thinking, AI-native building, marketplace dynamics, three-track customer strategy, international execution, and disciplined scaling — in one line.

The fCTO thesis is: technical architect who directs AI tools rather than framework specialist who implements code. The person NYC startups want in 2026 is not someone who writes React components — it is someone who ships a full product, validates it in a real market, and can speak clearly to every AI-native decision made along the way.

Document everything as it happens. The build decisions. The provider acquisition challenges. The first booking. The first bad match. The iteration. The expansion. By the time Marcus is in NYC, this is not a side project — it is a live, revenue-generating case study in AI-native product development that he owns, built, and can speak to in depth. That is what gets meetings.

The somatic dataset as the investor pitch

Don't say: "I built an AI massage app in Bali." Investors yawn.

Say: "I built the first proprietary dataset mapping unstructured human emotional states to specific physiological wellness interventions, validated in a high-trust same-day-booking context with real revenue across three customer cohorts — tourists, nomads, and residents." Investors lean forward.

The substance is the same. The positioning is not. The labeled dataset of (state → provider archetype → outcome) tuples accumulating session by session is what makes this venture-scale rather than a Bali services business.

The three-track strategy makes the dataset thesis credible. Tourists give breadth. Nomads give partial longitudinal data. Residents give the multi-month somatic arcs that prove the dataset thesis works. Without the resident track, the dataset is shallow and the venture story collapses to "AI massage app." With the resident track, the dataset is deep enough to license, extend, and defend.

Why the wedge has to be villa-distribution, not retreat-integration

The earlier teardown suggested retreat-integration as a sharper wedge. Considered seriously, it has problems:

Retreat operators are competitors-in-waiting. They own the high-trust relationship; they could build their own matching tool faster than they would partner.

Retreat schedules are rigid. The customer's window for integration sessions is narrow. Operationally fragile.

Retreat customers are concentrated; lose one operator partnership and a quarter of acquisition disappears overnight.

Villa distribution is structurally fragmented — many small partners, no single point of failure. More resilient.

Retreat-integration becomes a Phase 2 channel after villa distribution proves out. Not the wedge.

Things to track for the NYC narrative

Every decision log entry — what we tried, what failed, why we changed direction

Customer quotes verbatim — screenshot of "I would not have found this person on Google" beats any metrics slide

First match the AI got dramatically wrong, and what it taught about archetypes

First time a provider said "this changed my booking volume"

The exact moment Marcus had to resist becoming the shadow operator, and how he didn't

Week-by-week shrinking of Yuni-minutes-per-booking and Net-IDR-per-minute climbing

Audit log analysis — "the safety classifier caught X cases where matching would have been inappropriate, including pregnancies and trauma disclosures"

First resident customer who hit 6+ sessions — the dataset thesis proof point

The long-term "State Orchestration" vision

Not for v6. Not for V0. Not for V1. But the Year-3 investor pitch:

If a user trusts Neskala to touch their physical body and alter their emotional state, Neskala owns the highest-trust relationship in that user's life at that moment. In 18+ months: Neskala knows you are "jet-lagged and anxious" and books the grounding massage, partners with local kitchens to deliver a magnesium-heavy meal post-session, provides a binaural beat playlist for sleep. Wellness wallet, food-delivery wallet, digital-health wallet — all routed through state-based intent. The "API for human restoration" line.

What to actually pitch in NYC

The somatic dataset (the IP)

The provider graph (the moat)

The validated three-track wedge (proof we can ship and acquire across cohorts)

The director-model build approach (10x faster than traditional teams)

The expansion playbook (this becomes a venture, not a service)

Do not pitch: AI massage app. Bali wellness booking. The intake design. Anything that makes this sound like a feature instead of a category.

What happens when Yuni leaves

This is a question neither v5 nor any of the teardowns addressed. Year 3, Year 5 — at some point Yuni either takes equity and stays, or moves on. If she moves on:

The provider relationships are warm with her but contractually with Neskala — provider agreements signed with the company, not her personally

All provider info, partner info, and customer data lives in the database, not her phone — the voice-memo capture system enforces this from day one

The dataset belongs to the company

The brand belongs to the company

Customer relationships flow through the platform, not through her

Structure provider agreements explicitly so this is unambiguous: providers contract with the entity (Eagle Rocket LLC or Indonesian PT), not with Yuni personally. This protects the company and also protects Yuni — if she ever wants to step back, she's not chained to the role by being the only person with the keys.

End of Appendix A.

Codename Neskala  v6.3  ·  Private and confidential  ·  April 2026  ·  Working document, not a legal agreement. All names, plans, and concepts subject to change.
