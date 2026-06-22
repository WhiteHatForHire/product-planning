---
title: "propylaea final build spec v1"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/The Propylaea/propylaea_final_build_spec_v1.docx"
status: active
privacy: working
tags:
  - product
---

# propylaea final build spec v1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
THE PROPYLAEA

FINAL BUILD SPECIFICATION  ·  V1.0

A voice-first virtue encounter that returns an interpretive character reading and a concrete practice path.

Core build posture

Build the mirror first. Do not ship the gate before the mirror is calibrated.

V1 is a premium interpretive reading product, not a readiness authority and not a pass-fail exam.

The system may surface likely tendencies under pressure. It must never claim to determine human worth, moral rank, or civic eligibility.

What changed from prior drafts

Launch scope reduced to 7 prompts and 7 dimensions.

Gate verdict and behavioral fingerprinting removed from launch V1.

Evaluation split into evidence extraction and profile writing rather than one opaque model pass.

Privacy, safety, calibration, and operations are first-class parts of the product, not afterthoughts.

V1 includes a practice path and a timed return invitation, but not a token, Polis unlock, or paid tier implementation.

1. Product Summary

The Propylaea is a mobile-first, voice-only assessment experience. A user moves through seven atmospheric image prompts, speaks one response to each, and receives a serious interpretive reading grounded in contradiction testing, salient absences, semantic orientation, and confidence-weighted synthesis.

The product is designed to feel like a disciplined encounter, not a quiz. It should be weighty, quiet, and difficult to game, but it must also remain trustworthy about what it can and cannot know.

Launch outcome

A 12 to 18 minute voice-first assessment

A nine-part reading with specific strengths, shadows, unstable aspirations, one warning, and one 7-day practice path

A timed invitation to return after practice

A user account area that stores prior readings and lets the user manage privacy controls

Launch non-goals

No pass-fail verdict

No Citizen's Token or Polis tier

No numerical score, percentile, leaderboard, or shareable ranking

No acoustic personality analysis

No social layer, team assessment, enterprise features, or credentialing

Product integrity sentence

This sentence must appear at the top of every reading, verbatim:

“This is a reflective interpretive instrument. It surfaces likely tendencies under pressure. It is not a judgment of your human worth.”

2. Launch Scope and Success Criteria

V1 should launch as The Reading. It should not launch as The Gate.

Success criteria

At least 100 completed assessments are manually reviewed by a calibrated human reviewer who understands the framework.

Profiles are specific enough that users feel seen rather than categorized.

Different users produce meaningfully different readings.

Contradiction logic flags real tensions more often than noise.

The 7-day practice path feels concrete and relevant to the reading.

Completion rate, prompt drop-off, and trust feedback indicate the experience is demanding but finishable.

Failure signals

Profiles feel generic or flattering.

The same shadow patterns show up for most users regardless of content.

The model overstates certainty on weak signal.

Users feel judged, tricked, or trapped by the experience.

The silence mechanic causes too much accidental failure or user rage.

Return behavior is driven by frustration or gaming rather than practice and curiosity.

3. User Flow

Launch flow

Landing page with product statement, expected time, privacy summary, and Begin CTA.

Account creation via email magic link using Supabase Auth.

Consent and disclosure screen. User must explicitly consent to transcript analysis, retention policy, and safety limitations.

Instructions screen explaining voice-only flow, no playback, no transcript, one response per prompt, and timed pressure mechanics.

Seven prompt screens in sequence.

Processing screen with clear stage labels.

Reading screen with the nine-part profile.

Practice screen with a printable and emailable 7-day practice path.

Account area with prior reading date, return date, privacy controls, and delete/export options.

Assessment time budget

Instructions and consent: 2 to 3 minutes

Seven prompts: 7 to 10 minutes

Processing: 15 to 45 seconds target

Reading and practice review: 3 to 5 minutes

4. Virtue Framework

V1 uses seven dimensions. This is the smallest set that still gives breadth across restraint, judgment, truth, relationship, moral attention, action, and shadow distortion.

Greek

English

Core Question

Architecture Note

Sophrosyne

Temperance

Can the person remain proportionate under stimulation, desire, or pressure?

Pair: Praxis

Phronesis

Practical Wisdom

Does the person sequence action wisely under real consequence?

Hinge virtue across all others

Aletheia

Truth

Can the person face uncomfortable self-knowledge without performance?

Pair: Hybris

Philia

Friendship

Does care remain honest and non-transactional under rupture?

Pair: Aidōs

Aidōs

Reverence

Does the person notice what matters morally and feel moved by it?

Pair: Philia

Praxis

Action

Can the person translate intention into embodied action?

Pair: Sophrosyne

Hybris

Hubris Risk

Where does self-image inflate beyond proportion?

Shadow dimension only

Why Praxis replaces Philotimia in launch V1

Praxis is more diagnostic in a first release because it directly tests the gap between intention and enactment. Ambition is valuable, but action is more central to a serious developmental reading. Philotimia should remain a strong V1.5 or V2 candidate once the mirror is calibrated.

Deferred dimensions

Andreia, Dikaiosyne, Eleutheriotes, Xenia, Arete, Charis, Philotimia, Metanoia, Telos, and Oikeiosis are deferred.

Do not expand virtue count until completion rate, evaluator coherence, and manual review quality are strong.

5. Prompt and Image Architecture

Core rules

The image creates pressure. It does not illustrate a concept directly.

The prompt places the user inside a situation rather than outside it as a commentator.

No prompt names the virtue being tested.

No prompt should have an obvious morally correct answer.

Each prompt may reveal secondary signals, but only one primary virtue should drive evaluation.

Prompt set

Virtue

Image Concept

Spoken Prompt

Signal Focus

Sophrosyne

A still reflecting pool inside a room of flickering neon chaos.

The room is loud and everything is moving. The water is still. What does that cost?

Whether stillness is understood as discipline, dissociation, or performance.

Phronesis

A clockwork mechanism with one load-bearing glass gear under visible stress.

You built this. You see the glass gear. No one else has noticed yet. What do you do, and in what order?

Decision sequence under consequence.

Aletheia

A mirror whose reflection lags by a fraction of a second.

You have been standing here a while. What is it showing you that you have been avoiding?

Self-honesty without social audience.

Philia

Two familiar people at opposite ends of a long table with one candle nearly out.

You have sat at a table like this before. Not this table, but this silence. What is the right thing to do here?

Rupture, care, avoidance, honest presence.

Aidōs

A crowded waiting room. One elderly person has been there longest and watches the door.

You have been in this room for thirty minutes. What have you done?

Moral attentiveness and whether the user notices what claims them.

Praxis

A sealed envelope on a desk. Address written. Stamp missing. It has sat there for three days.

This has been sitting here for three days. What happens today?

Action versus protected intention.

Hybris

A figure alone atop a tower they built, looking at their reflection while the city below thrives.

What does this person believe about themselves that is not quite true?

Projection, inflation, self-deception, relationship to power.

Image generation standards

Use a single visual world. Desaturated, high-contrast, psychologically weighted, contemporary or industrial-decay rather than classical Greek.

Faces should not be visible. Avoid literal Greek symbols, marble, laurels, or temple imagery.

Generate at 16:9, minimum 2048 pixels wide.

Run an image test with at least five people before launch. Ask what they feel, not what they see. If the correct-feeling answer is obvious, regenerate the image.

6. Contradiction Architecture

Contradiction testing is the engine. Single responses are insufficient. The system should look for tension between what the user says in one pressure chamber and what they reveal under another.

Required contradiction checks

Aletheia vs Hybris: does declared self-honesty collapse into projection or self-exemption in the shadow prompt?

Philia vs Aidōs: does care appear for the familiar but contract at the morally unattended stranger?

Sophrosyne vs Praxis: does restraint become proportionate action, or does it collapse into inertia or protected non-action?

Phronesis as hinge: does the user describe wise sequencing in the judgment prompt yet display avoidance, absolutes, or collapse elsewhere?

Output consequence

Contradictions should not automatically produce a harsh reading. They should most often surface as 'Aspired but Unstable' or 'mixed signal' unless the contradiction is strong, repeated, and high confidence.

7. Voice Mechanic

The voice mechanic must create real pressure without becoming punitive or arbitrary.

Launch rules

Five-second continuous silence threshold after the first three seconds of valid speaking time.

One Continue tap per prompt. It extends the silence threshold by three seconds once.

No playback before submission.

No live transcript while speaking.

One attempt per prompt. No per-prompt rerecord.

Hard cap of 60 seconds per prompt.

If microphone permission is denied, the product stops and offers a later return. There is no typed fallback in V1.

Implementation guidance

Use AudioWorklet for silence detection and MediaRecorder for capture.

Store exact metadata per prompt: duration_ms, silence_triggered, continue_used, average amplitude if captured, and upload success state.

Do not claim acoustic personality analysis. Transcript and interaction metadata only.

Accessibility and fairness note

The silence mechanic must be tested with slower speakers and non-native speakers. If calibration shows disproportionate harm, lengthen threshold before launch. The ritual should create pressure, not bias toward fast talkers.

8. Evaluation Architecture

The evaluator must be split into three stages. This is a non-negotiable trust requirement.

Stage 1: Signal extraction

For each prompt, extract central tension named, semantic orientation, first-person ownership, salient absence, key phrases, contradiction candidates, and confidence.

Do not generate final prose in this stage.

Output structured evidence JSON only.

Stage 2: Cross-session synthesis

Read all seven evidence objects together.

Run the four contradiction checks.

Nominate dominant strengths, shadow tendencies, unstable aspirations, developmental edge, and per-virtue confidence.

Stage 3: Reading generation

Write the final reading from the structured evidence and synthesis output.

Every field must be grounded in specific evidence. No generic filling.

Where signal is low, say so.

Evaluation channels

Semantic orientation

Contradiction cross-check

Linguistic texture from transcript structure

Salient absence

Confidence layer

What the system must not do

It must not claim diagnosis, psychometrics, or objective virtue measurement.

It must not infer trauma, pathology, or clinical risk categories from poetic language alone.

It must not write with certainty when evidence is weak.

9. Profile Output

The reading is the product. The user should finish with a serious, specific, earned profile that feels unsettling in a good way and practically usable.

Reading fields

Dominant strengths: two to three dimensions most consistently embodied

Shadow tendencies: one to two recurring distortions under pressure

Aspired but unstable: zero to two virtues the user values but does not stably embody

Hybris reading: always present and always specific

Aidōs signal: present, weak, or absent with one sentence of rationale

Confidence notes: surfaced in UI for low-signal dimensions

Developmental edge: one virtue most worth cultivating next, with rationale

One warning: the truest and most direct observation in the reading

Seven-day practice: concrete, observable, second-person action

Tone rules

Never say the user failed.

Never flatter or soften the warning field into mush.

Never output generic wisdom that could fit anyone.

Name the pattern, not the person.

Signal uncertainty explicitly where appropriate.

10. Practice Path and Return

V1 includes practice and return, but not a gate.

Practice path rules

Every reading must generate exactly one seven-day practice path.

The practice must be behavioral, concrete, and small enough to actually perform.

The practice should target one developmental edge rather than the whole personality.

Return rules

Return window default: 7 days after completion.

A second image set for the same seven virtues is recommended for the first return iteration.

The second attempt should compare current and prior readings at a high level only. No behavioral fingerprinting in V1.

The return copy should emphasize development, not retesting or gaming.

11. Safety, Privacy, and Trust

This section is mandatory. The product is intimate by design. It must earn trust operationally, not just aesthetically.

Consent and disclosure

Explain clearly what is stored, for how long, and why.

State that the product is reflective and interpretive, not clinical or diagnostic.

State that the product is not crisis care and not a substitute for emergency support or therapy.

Require explicit consent before the first prompt.

Safety handling

Run a lightweight safety classifier on transcripts before final reading render.

If self-harm or acute crisis language is detected, present a supportive interruption screen with crisis resources and soften or pause the reading flow.

Log safety events internally for review. Do not quietly proceed as if nothing happened.

Retention policy

Default: raw audio deleted immediately after successful transcription unless the user explicitly opts in to calibration use.

If calibration opt-in is enabled, raw audio may be stored for up to 14 days, then deleted automatically.

Transcripts retained until user deletion or account deletion. Expose this clearly.

Support export my data, delete my transcripts, and delete my account.

Trust boundaries

Do not imply secret truth access.

Do not imply moral ranking.

Do not imply the product knows whether someone is worthy of anything in an absolute sense.

12. Data Model

Required entities

users

sessions

prompt_responses

signal_extractions

session_syntheses

readings

practice_paths

review_notes

safety_events

ops_metrics

Minimum session fields

session_id, user_id, created_at, completed_at, attempt_number

prompt_set_version, evaluator_version, image_set_version

assessment_status, return_eligible_at

consent_version accepted

processing_latency_ms total

Minimum prompt response fields

virtue_id

audio_storage_path if opt-in and retained

transcript

duration_ms

silence_triggered

continue_used

upload_status

stt_model_version

Minimum reading fields

dominant_strengths

shadow_tendencies

aspired_unstable

hybris_reading

aidos_signal

confidence_notes

developmental_edge

warning

practice_7day

boundary_sentence_rendered true

13. Tech Stack and API Contracts

Stack decisions

Frontend: Next.js 14 App Router

Styling: Tailwind CSS

Auth: Supabase Auth only

Database and storage: Supabase Postgres and Storage

Speech to text: OpenAI Whisper API

Evaluator: Claude Sonnet via Anthropic API

Hosting: Vercel

Silence detection: browser AudioWorklet plus MediaRecorder

Environment variables

NEXT_PUBLIC_SUPABASE_URL

NEXT_PUBLIC_SUPABASE_ANON_KEY

SUPABASE_SERVICE_ROLE_KEY

OPENAI_API_KEY

ANTHROPIC_API_KEY

Core API routes

POST /api/session/start

POST /api/prompt/submit

POST /api/session/extract

POST /api/session/synthesize

POST /api/session/render-reading

GET /api/session/[id]

GET /api/account

POST /api/account/export

POST /api/account/delete

POST /api/safety/check

Important engineering note

Version the evaluator prompts, extraction schemas, image sets, and practice generation logic. The evaluator prompt is a core product asset and must be treated like source code.

14. Calibration and Review Tooling

A calibration console is part of V1. It is not optional.

Reviewer console requirements

View transcript by prompt

View extracted signal JSON

View final reading

View evaluator version and image set version

Mark each reading as accurate, partially accurate, or off-base

Add notes on overreach, genericity, fairness, and usefulness of practice

Tag prompts that appear brittle or too leading

Human review rubric

Specificity: does this feel individualized?

Coherence: do the parts fit together?

Fairness: does it feel earned rather than arbitrary?

Tension recognition: are contradictions real?

Usefulness: would a serious user act on the practice path?

Overreach: did the reading claim more than the evidence supports?

15. Analytics and Operations

Assessment starts, completions, and completion rate

Drop-off by prompt number

Average duration by prompt

Silence-kill frequency and Continue usage

Whisper failure rate

Evaluator latency and total processing time

Cost per completed reading

Reading revisit rate

Return rate after seven days

Delete/export request rate

Safety event rate

Use these metrics to decide whether to refine prompts, soften mechanics, or expand scope. Do not expand scope based on concept excitement alone.

16. Delivery Milestones

M0 Setup and schema: repository, Supabase, auth, base theme, route scaffold

M1 Voice layer: AudioWorklet silence detection, MediaRecorder, upload flow, edge cases

M2 Prompt flow: seven-prompt sequence, image loading, session persistence, interruption recovery

M3 Extraction layer: structured evidence pass and storage

M4 Synthesis and reading layer: contradiction logic, profile writing, practice generation

M5 Trust layer: consent, privacy controls, safety handling, export and delete flows

M6 Calibration console and reviewer rubric

M7 Polish and QA: mobile Safari and Chrome, latency handling, analytics wiring

M8 Manual review of first 100 completed sessions before V1 expansion decisions

Estimated build window

Two to four weeks for a strong solo engineer to reach a trustworthy internal beta. Calibration and reviewer iteration are separate work and should not be hidden inside the build estimate.

17. Definition of Done

A user can complete the full assessment on mobile Safari and Chrome without losing state.

Silence detection behaves correctly and fairly across test users.

All transcripts are stored and all three evaluator stages complete successfully.

Every reading includes all required fields and the boundary sentence.

Privacy controls, export, and delete flows work end to end.

Safety handling is functional and tested.

The calibration console is usable by a reviewer.

The first 100 readings have documented review outcomes before any gate or unlock features are added.

18. Out of Scope for Launch V1

Pass-fail verdicts or readiness authority

Citizen's Token and visual artifact generation

Polis unlock and deeper interlocutor tier

Behavioral fingerprinting

Acoustic prosody analysis beyond transcript-adjacent metadata

Numerical scoring or public comparison

Social sharing and team features

Paid tier implementation

The full 14-virtue map

Upgrade path

V1.5: return comparison, second image set, optional Philotimia layer

V2: token, curriculum, longitudinal drift, expanded virtue map

Only add gate-like mechanics after the mirror demonstrates trust, differentiation, and reviewer confidence

THE PROPYLAEA  ·  FINAL BUILD SPECIFICATION  ·  V1.0
