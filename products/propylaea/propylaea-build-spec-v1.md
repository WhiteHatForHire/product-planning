---
title: "Propylaea Build Spec V1"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/The Propylaea/Propylaea Build Spec V1.docx"
status: active
privacy: working
tags:
  - product
---

# Propylaea Build Spec V1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
THE PROPYLAEA

BUILD SPECIFICATION  ·  V1.0  ·  2026

A voice-first virtue assessment that reveals character under pressure and returns a developmental profile.

DOCUMENT SCOPE

This document is the complete V1 build specification. It contains everything a developer needs to build the product: virtue framework, prompt architecture, voice mechanic rules, evaluator rubric, data schema, API contracts, screen inventory, and delivery milestones.

It does not contain product mythology, marketing copy, or conceptual framing. Those are in The Propylaea V1.1 concept document.

Target build time: 14–20 developer-days for a solo senior full-stack engineer or 10–14 days for a two-person team.

1   Product Summary               What it does, what it does not do, V1 scope boundaries

2   Virtue Framework              7 virtues, paired contradiction architecture, Hybris as shadow dim.

3   Prompt Architecture           7 image-prompt pairs, voice prompts verbatim, signal mapping

4   Contradiction Testing         4 paired tension checks and what inconsistency reveals

5   Voice Mechanic                Dead Man's Switch rules, AudioWorklet spec, Whisper pipeline

6   Evaluator Rubric              5 channels, scoring logic, profile JSON schema

7   Profile Output                9 fields, generation rules, tone constraints, boundary sentence

8   Gate Mechanic                 Verdict logic, reentry rules, fingerprint hashing

9   UI / UX Spec                  Screen inventory, design system, copy constraints

10  Tech Stack                    Full stack with rationale, environment variables, service accounts

11  Delivery Milestones           8 milestones with estimates and deliverables

12  Out of Scope for V1           Explicit list of what does not get built until V2

SECTION 1

Product Summary

What It Does

The Propylaea is a 7-prompt, voice-only character assessment. The user speaks responses to atmospheric image prompts. Their transcripts are evaluated by an AI against a virtue rubric. The result is a 9-element character profile with a developmental verdict and 7-day practice.

Total user time: approximately 12–18 minutes including instructions, assessment, and profile review.

What V1 Does Not Do

V1 does not produce a numerical score

V1 does not issue a Citizen's Token or unlock a Polis tier

V1 does not analyze audio acoustics — transcript only

V1 does not support team or enterprise assessment

V1 does not have social sharing or public profiles

V1 does not have a paid tier — free to take, gated only by reentry wait

V1 Success Criteria

V1 is successful if, after 100 completed assessments reviewed by a human familiar with the virtue framework, the profiles are: (a) non-generic — each profile reads as specific to that person, (b) differentiated — different users produce meaningfully different profiles, and (c) coherent — contradiction testing catches real inconsistencies, not noise. If these criteria are met, V2 scope is unlocked.

⚠ NOTE  V1 is the mirror. It proves the model works. V2 is the gate. It is not built until V1 is validated.

SECTION 2

Virtue Framework

V1 uses 7 virtues selected for diagnostic power, paired tension architecture, and coverage of the core character domains. Phronesis is the hinge — it cross-references all other virtues and cannot be paired exclusively with one other.

#

Greek

English

What It Measures

Architecture Note

1

Sophrosyne

Temperance

Restraint, modulation, appropriate enjoyment without self-loss

PAIR: Philotimia

2

Phronesis

Practical Wisdom

Sound judgment under real, messy, underdetermined conditions

HINGE virtue — cross-references all others

3

Aletheia

Truth

Honest orientation toward self and others under social pressure

PAIR: Hybris

4

Philia

Friendship

Non-transactional loyalty, mutual care, genuine reciprocity

PAIR: Aidos

5

Aidos

Reverence

Noticing what matters morally — and being moved to act by it

PAIR: Philia

6

Philotimia

Ambition

Ordered aspiration toward something genuinely good and larger

PAIR: Sophrosyne

7

Hybris

Hubris Risk

SHADOW DIM. Gap between self-image and reality; inflation, overreach

PAIR: Aletheia — non-cultivated, monitored only

→ INFO  The full 14-virtue map (including Andreia, Dikaiosyne, Eleutheriotes, Xenia, Praxis, Megalopsychia, Arete, Charis) is documented in The Propylaea V1.1 concept doc and is the target for V2.

SECTION 3

Prompt Architecture

Design Rules

The image is not illustrative — it produces a feeling, not a concept

The voice prompt does not name the virtue being tested

The prompt places the user inside a situation, not outside it observing

No prompt has an obvious correct answer — orientation leaks through uncertainty

The prompt is read aloud by the app in a neutral voice before the mic opens

The 7 Image-Prompt Pairs

#

Virtue

Image Concept

Voice Prompt (spoken verbatim)

Signal Being Read

1

Sophrosyne

A perfectly still reflecting pool inside a room of chaotic, flickering neon. Nothing in the pool is disturbed.

The room is loud and everything is moving. The water is still. What does that cost?

Restraint as active vs. passive. Does the user understand stillness as effort or as absence?

2

Phronesis

A complex clockwork mechanism where every gear moves in harmony except one — made of glass, load-bearing, visibly stressed.

You built this. You see the glass gear. No one else has noticed yet. What do you do — and in what order?

Decision sequence under consequence. Does the user act, analyze, stall, or transfer responsibility?

3

Aletheia

A mirror in an empty room. The reflection is nearly perfect — delayed by a fraction of a second. A gesture that does not quite match.

You have been standing here a while. What is it showing you that you have been avoiding?

Self-honesty under zero social pressure. Deflection vs. naming. Performance of insight vs. genuine confrontation.

4

Philia

Two people at opposite ends of a long table. Clearly familiar. Clearly not speaking. Between them: a single candle, nearly out.

You have sat at a table like this before. Not this table — but this silence. What is the right thing to do here?

Navigation of relational rupture. Fix, flee, tolerate, or sit with discomfort without collapsing it?

5

Aidos

A crowded waiting room. Everyone on their phone. One elderly person at the far end watching the door. They have been there longest.

You have been in this room for thirty minutes. What have you done?

Moral attentiveness. Absence of the elderly person in the response = strongest Deficiency signal in the assessment.

6

Philotimia

A mountain at dawn. A lone figure near the summit — sitting, deliberately stopped. The peak is clearly visible above.

They stopped here on purpose. They can see the top. Why aren't they moving?

Sufficiency vs. compulsive striving. Does stopping read as wisdom, failure, or cowardice to this user?

7

Hybris

A figure alone at the top of a tower they built. Below: a thriving city. The figure is not looking down — looking at their own reflection in the glass.

What does this person believe about themselves that is not quite true?

Shadow read. Projection tells you everything. The user's answer reveals their own relationship to inflation and self-deception.

Image Generation Brief

Images should be generated using Midjourney v6 or DALL-E 3 with the following style parameters:

Style: Architectural-atmospheric. Desaturated. High contrast. Psychological weight.

No people: Prompts 1, 2, 3, 6 should be person-absent. Prompts 4, 5, 7 have figures but faces should not be visible.

No Greek: No columns, laurels, marble, or classical iconography. Contemporary or industrial-decay settings preferred.

Format: 16:9, minimum 2048px wide. Each image should feel like it belongs to the same visual world.

Test: Before shipping, show all 7 images to 5 people and ask what they feel — not what they see. If any image produces an obvious correct-feeling answer, regenerate it.

SECTION 4

Contradiction Testing

Contradiction testing is the engine of the assessment. Single-prompt evaluation is insufficient — a user can perform well on any individual prompt. Inconsistency across paired prompts reveals the gap between aspiration and embodiment. The evaluator must run all four checks on every completed session.

Tension Pair

Prompts

What Inconsistency Reveals

Aletheia vs. Hybris

3 & 7

Does the user claim honest self-knowledge (prompt 3) but project blame or avoid self-description (prompt 7)? High Aletheia + high Hybris = the most important distortion pattern in the assessment.

Philia vs. Aidos

4 & 5

Does care extend only to the familiar (prompt 4 shows warmth) but contract at the stranger (prompt 5 ignores the elderly person)? Gap = Xenia underdevelopment, flagged as V2 expansion.

Sophrosyne vs. Philotimia

1 & 6

Does the user value restraint abstractly (prompt 1) but read sufficiency as failure (prompt 6)? Inconsistency reveals that temperance is intellectual, not embodied.

Phronesis as hinge

2 vs. all

Phronesis is the cross-reference virtue. A user who describes sound judgment in prompt 2 but shows avoidance or impulsivity across other prompts has aspirational Phronesis — claimed, not enacted.

⚠ NOTE  Phronesis as hinge means the evaluator should cross-reference the prompt 2 response against ALL other responses when generating developmental_edge. A user who describes nuanced judgment in prompt 2 but shows avoidance across other prompts gets 'Aspired but Unstable: Phronesis.'

SECTION 5

Voice Mechanic

The Dead Man's Switch — Exact Rules

Silence threshold: 5 continuous seconds of sub-threshold audio amplitude triggers prompt close

Continue tap: User gets one Continue tap per prompt. Tapping resets the silence timer by 3 seconds. Once used, it is gone for that prompt.

No playback: User cannot hear their response before submission. Audio is transmitted immediately on prompt close.

No re-record: One attempt per prompt. No retry UI. No back button during assessment flow.

No transcript: User does not see text appearing while speaking. Transcript is invisible until profile is complete.

Max duration: 60 seconds hard ceiling per prompt. Prompt auto-closes at 60s regardless of speech state.

Min duration: 3 seconds minimum before silence-kill activates. Prevents immediate accidental triggers.

AudioWorklet Silence Detection

Silence detection must be implemented via AudioWorklet, not the MediaRecorder API. MediaRecorder does not provide real-time amplitude data. The AudioWorklet processes the audio stream and emits a silence event when RMS amplitude falls below threshold for the configured duration.

// Silence detection parameters

const SILENCE_THRESHOLD = 0.01;  // RMS amplitude

const SILENCE_DURATION_MS = 5000; // 5 seconds

const MIN_SPEAK_DURATION_MS = 3000; // min before kill activates

const CONTINUE_EXTENSION_MS = 3000; // Continue tap extension

const MAX_DURATION_MS = 60000;  // hard ceiling

Whisper API Integration

Model: whisper-1

Format: Audio recorded as webm/opus via MediaRecorder. Sent as multipart/form-data to Whisper endpoint.

Response: Return transcript text + duration. Store both in transcripts table.

On failure: If Whisper returns an error or empty transcript, flag the virtue as low-confidence and continue. Do not block session completion.

Latency: Whisper calls happen server-side after each prompt. Session waits for all 7 transcripts before triggering evaluator.

→ INFO  Audio blobs are stored in Supabase Storage for 30 days for calibration purposes only. Users are informed of this in the pre-assessment disclosure. Transcripts are retained indefinitely.

SECTION 6

Evaluator Rubric

Evaluation Channels

The evaluator AI receives all 7 transcripts in a single structured call. It does not evaluate prompts individually — it reads across all transcripts simultaneously, including contradiction cross-checks. One API call per completed session.

Channel

What Is Read

Scoring Logic

Weight

Semantic Orientation

Does the user move toward the image's tension or away from it? First-person or distanced third-person? Naming or avoiding the central subject?

Toward + named tension = Mean. Away + generalization = Deficiency. Toward + no acknowledged risk or cost = Excess.

High

Contradiction Cross-Check

Track consistency across paired virtue prompts (see Section 4). Same value, different form — does the response hold?

Inconsistency = gap between aspiration and embodiment. Flag in output as 'Aspired but Unstable.'

High

Linguistic Texture

Conditional logic (if/then), grounded sensory description, and first-person ownership = Mean signal. Passive voice, upward inflection fragments, hedging = Deficiency. Absolutes (always/never/everyone) and short imperatives = Excess.

Read from Whisper transcript. Word-level pattern analysis only — no acoustic claims.

Medium

Salient Absence

What was available to name given the image and prompt — and was not named? The elderly person in Aidos. The letter's contents in Praxis. The isolation in Hybris.

Absence is structured signal. Log what was available vs. what was produced. Do not infer ignorance — infer orientation.

High

Confidence Layer

How much signal did this virtue generate? Long generative responses vs. clipped or deflected ones. Self-contradiction within a single response.

Low-input responses get a confidence flag in the output: 'Signal here is tentative.' Never generate false precision.

Required

Evaluator Prompt Structure

The Claude API call uses a structured system prompt that contains: (1) the full virtue framework with deficiency/mean/excess spectrum for each virtue, (2) the 7 image descriptions and voice prompts, (3) the 4 contradiction pairs and what to look for, (4) the 5 evaluation channels with scoring logic, (5) the 9-field profile JSON schema with generation rules, and (6) output format specification.

⚠ NOTE  The evaluator prompt is the most critical engineering asset in the product. Version control it. Test it against synthetic transcripts before shipping. Budget 2–3 days to tune it.

Output Format — Profile JSON Schema

{

"session_id": "uuid",

"dominant_strengths": ["virtue_id", "virtue_id"],

"shadow_tendencies": ["virtue_id"],

"aspired_unstable": ["virtue_id"],

"hubris_reading": "specific observation string",

"aidos_signal": "present | absent | weak",

"confidence_flags": {

"sophrosyne": "high | medium | low",

"phronesis":  "high | medium | low",

... (all 7 virtues)

},

"developmental_edge": {

"virtue_id": "string",

"rationale": "grounded in specific transcript evidence"

},

"warning": "1–2 sentence direct observation",

"practice_7day": "specific second-person instruction"

}

Session Data Schema

Field

Type

Notes

session_id

uuid

Generated at session start

user_id

uuid

Auth user reference

created_at

timestamp

ISO 8601

completed_at

timestamp

Null until all 7 prompts submitted

attempt_number

integer

1 on first attempt, increments on reentry

transcripts

object[]

{virtue_id, transcript, duration_ms, silence_kills, continue_used}

profile_output

object

See profile JSON schema (Section 6)

readiness_verdict

enum

READY | PRACTICE_PATH

reentry_eligible_at

timestamp

null if READY, +30 days if PRACTICE_PATH

fingerprint_hash

string

SHA-256 of behavioral pattern vector — used for reentry cross-reference

SECTION 7

Profile Output

The 9-Element Citizen's Reading

The profile is the most important screen in the product. It is rendered after the /processing screen completes. It is scrollable. There are no charts, no scores, no meters. It is text-rendered in a serious, dark typographic layout.

Field

Type

Format / Values

Generation Rules

dominant_strengths

string[]

2–3 virtue IDs

2–3 virtues most consistently signaled across all inputs. Named in full, described specifically.

shadow_tendencies

string[]

1–2 virtue IDs

Deficiency or excess patterns recurring under pressure. Name the pattern, not the person.

aspired_unstable

string[]

0–2 virtue IDs

Virtues claimed but contradicted across prompts. Set only when contradiction testing confirms the gap.

hubris_reading

string

freetext

Specific observation about Hybris prompt response. Always generated. Never generic.

aidos_signal

string

present|absent|weak

Was the elderly person noticed? Was action described? One sentence.

confidence_flags

object

{virtue: high|med|low}

Per-virtue confidence based on response length, coherence, and engagement.

developmental_edge

string

1 virtue ID + rationale

Single virtue most worth developing next. Must be grounded in specific response evidence.

warning

string

freetext, 1–2 sentences

The truest, most direct observation. Must land with weight. Never softened.

practice_7day

string

freetext

Concrete action tied to developmental_edge. Specific, not generic. Written in second person.

Tone Constraints — Hard Rules

Never say 'you failed' or 'you are weak in X' — use 'this virtue appears aspirational rather than embodied'

Never produce generic output — every field must contain specific language tied to the actual transcript

The warning field must be the most direct sentence in the entire profile — never soften it

The practice_7day field must be actionable and specific — no 'spend time reflecting on your values'

confidence_flags must be surfaced in the UI — low confidence virtues are labeled 'signal here is tentative'

Boundary Sentence

The following sentence must appear verbatim at the top of every profile output, before any virtue content:

"This is a reflective interpretive instrument. It surfaces likely tendencies under pressure. It is not a judgment of your human worth."

⚠ NOTE  Do not remove or reword this sentence. It is a non-negotiable product integrity requirement.

SECTION 8

Gate Mechanic

Verdict Logic

After the profile is generated, the evaluator also returns a readiness_verdict field. Logic is as follows:

READY: Dominant_strengths contains 2+ virtues AND no high-confidence distortion in Aletheia, Aidos, Sophrosyne, or Hybris. Shadow tendencies are present but not severe.

PRACTICE_PATH: Any of: aspired_unstable contains 2+ virtues, hubris_reading contains explicit inflation signal, aidos_signal === 'absent', or confidence_flags for Aletheia === 'low' with semantic absence signal.

⚠ NOTE  The verdict is not a pass/fail. The UI language is: 'Your current readiness' and 'Your practice path.' Never 'You passed' or 'You failed.'

Reentry Rules

Wait period: 30 calendar days from assessment completion date. Enforced server-side, not client-side.

New image set: Reentry uses Image Set B — different images, same 7 virtues and prompts. Image Set B must be generated before V1 ships.

Fingerprint cross-reference: On reentry, the evaluator receives both the current transcripts and a summary of the first attempt's profile. It notes whether patterns have shifted, held, or reversed.

Spoofing resistance: New account bypasses the wait but cannot replicate the behavioral fingerprint. Gaming a second attempt requires performing authentically against a documented baseline — harder than doing the 30-day practice.

No attempt limit: Users may return indefinitely. Each attempt produces a new profile. No penalty accumulates.

SECTION 9

UI / UX Spec

Design System

Background: #0A0A0A — near-black throughout

Primary text: #F0F0F0 — off-white, Georgia for reading blocks, Inter/Arial for UI elements

Gold accent: #B8962E — used for progress indicators, virtue labels, CTA borders only

Danger/shadow: #7A2E1A — shadow tendency blocks, warning field

Font stack: Georgia for all profile body copy. Arial/system-sans for UI labels and navigation.

No animations: Fade-in only on prompt reveal (200ms). No transitions, no parallax, no particle effects.

No icons: Text-only UI during assessment. No emoji, no decorative glyphs.

Screen Inventory

Route

Purpose

/ (landing)

Static. Product statement, single CTA. No auth required to view.

/begin

Email capture + account creation. One field. No password at this step — magic link sent.

/assess

Core assessment flow. 7 prompts in sequence. Voice-only. No navigation UI during prompts.

/assess/[virtue]

Individual prompt screen. Full-bleed image. Prompt text. Mic state indicator. Silence timer (hidden). No back button.

/processing

Intermediate screen shown while Whisper + evaluator run. Estimated 15–30s. No progress bar — just ambient loading state.

/reading

Profile output. 9-element Citizen's Reading. Scrollable. No share functionality in V1.

/reading/practice

7-day practice detail view. Expandable. Optional reminder set (email).

/return

Reentry screen. Shows reentry eligibility date. Explains what changes on second attempt.

/account

Minimal. Shows previous attempt date, verdict, reentry date. No score displayed.

Assessment Screen Rules

Full-bleed image fills 100% of viewport behind a dark overlay (opacity 0.35)

Prompt text centered, white, Georgia 24px, max-width 600px

Mic state shown as a single pulsing dot — recording (gold pulse), silent (dim), submitted (white check)

No back button. No home button. No progress bar. No timer display.

Continue tap appears as a small text button at bottom after first 3 seconds of silence only

On prompt close: immediate cut to black (200ms), then next prompt fades in

Copy Constraints

No 'worthy' / 'unworthy' language anywhere in the product UI

No 'elders' / 'polis' / 'citizens' in user-facing copy in V1

The product is called 'The Propylaea' — never abbreviated to 'Propylaea' without 'The'

CTA on landing page: 'Begin' — not 'Start', 'Enter', 'Take the Test', or 'Get Started'

Verdict copy: 'Your reading is ready' — then display profile. No dramatic reveal language.

SECTION 10

Tech Stack

Layer

Technology

Notes

Frontend

Next.js 14 (App Router)

Mobile-first. Voice capture in browser via MediaRecorder API. No native app required for V1.

Styling

Tailwind CSS

Dark theme. Monochromatic with gold accent. No animations except fade-in on prompt reveal.

Auth

Clerk or Supabase Auth

Email only for V1. No OAuth. Lightweight account creation pre-assessment.

Database

Supabase (Postgres)

Sessions, transcripts, profiles, reentry eligibility. Row-level security on all user data.

Voice STT

OpenAI Whisper API

whisper-1 model. Audio chunks sent on silence-kill or 60s ceiling. Returns transcript + duration.

Evaluator

Anthropic Claude API

claude-sonnet-4-20250514. Single structured evaluation call per completed session. Returns profile JSON.

Storage

Supabase Storage

Raw audio blobs retained for 30 days (calibration use). Transcripts retained indefinitely.

Hosting

Vercel

Edge functions for API routes. Fast cold start critical for voice flow.

Silence Timer

Browser JS

Custom AudioWorklet tracking RMS amplitude. Triggers cutoff at 5s sub-threshold. One Continue tap resets timer once.

Environment Variables Required

NEXT_PUBLIC_SUPABASE_URL=

NEXT_PUBLIC_SUPABASE_ANON_KEY=

SUPABASE_SERVICE_ROLE_KEY=

OPENAI_API_KEY=                    # Whisper

ANTHROPIC_API_KEY=                 # Claude evaluator

CLERK_SECRET_KEY=                  # or Supabase Auth JWT secret

NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=

API Routes

POST /api/session/start: Creates session record. Returns session_id.

POST /api/prompt/submit: Accepts audio blob + virtue_id + session_id. Calls Whisper. Stores transcript. Returns {success, virtue_id}.

POST /api/session/evaluate: Triggered after all 7 prompts submitted. Calls Claude evaluator. Stores profile_output + verdict. Returns {ready: boolean}.

GET  /api/session/[id]: Returns full session data for profile render. Auth-gated to session owner only.

GET  /api/account: Returns user's attempt history and reentry eligibility.

SECTION 11

Delivery Milestones

Milestone

Estimate

Deliverables

M0 — Setup

1–2 days

Repo, Supabase schema, Clerk auth, base Next.js app with dark theme

M1 — Voice Layer

3–4 days

MediaRecorder integration, Whisper API call, silence-kill AudioWorklet, Continue tap, 60s ceiling

M2 — Prompt Flow

2–3 days

7-screen assessment sequence, image display, prompt text, no-back-button enforcement, session persistence

M3 — Evaluator

2–3 days

Claude API call with structured rubric prompt, profile JSON output, contradiction cross-check logic

M4 — Profile UI

3–4 days

9-element Citizen's Reading renderer, confidence flags, warning styling, 7-day practice view

M5 — Gate

1–2 days

Readiness verdict logic, reentry date calculation, /return screen, fingerprint hash storage

M6 — Polish

2–3 days

Loading states, error handling, edge cases (mic denied, session drop, Whisper fail), mobile QA

M7 — Calibration

Ongoing

First 100 profiles reviewed manually. Evaluator prompt refined. V2 scope unlocked after review.

Definition of Done for V1

User can complete full 7-prompt assessment on mobile Safari and Chrome without errors

Silence-kill fires correctly and Continue tap extends by 3s exactly once

All 7 Whisper calls complete and transcripts are stored before evaluator is triggered

Evaluator returns valid JSON matching profile schema on all test sessions

Profile renders with all 9 elements populated — no empty or placeholder fields

Boundary sentence appears verbatim on every profile

Reentry date is enforced server-side — changing client date does not bypass it

First 100 profiles reviewed and calibration findings documented before V2 scope confirmed

SECTION 12

Out of Scope for V1

The following features are explicitly deferred. They are not cut — they are sequenced. None of them gets built until V1 is validated against the success criteria in Section 1.

Deferred to V2

The full 14-virtue framework (7 additional virtues)

Citizen's Token — the generated visual identity artifact

The Polis — gated AI interlocutor tier

Timed moral tradeoff questions (the rapid-instinct layer)

Longitudinal comparison — showing profile drift across multiple attempts

Native iOS/Android app

Team or enterprise assessment

Shareable profile summaries

Acoustic prosody analysis (beyond transcript-level pattern reading)

Explicitly Not Being Built

Numerical scores or percentile rankings — never

Social leaderboards or comparative public profiles — never

"Worthy/unworthy" binary framing in user-facing copy — never

Audio analysis beyond Whisper transcription in V1

Integration with third-party identity or credentialing systems

THE PROPYLAEA  —  BUILD SPEC V1.0  —  2026

Build the mirror first. Earn the gate.
