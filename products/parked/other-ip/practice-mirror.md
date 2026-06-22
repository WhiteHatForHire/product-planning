---
title: "# Practice Mirror"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/Other IP and ideas /# Practice Mirror.docx"
status: active
privacy: working
tags:
  - planning
---

# # Practice Mirror

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# Practice Mirror

**Live AI practice coach for piano and drums via MIDI**

A Symposium Studios product

Version 0.2 — Concept spec, parked but buildable

## Working name

Practice Mirror is the working name. Alternatives worth considering: Reprise, Cadence, Phrase, Session Sense, Rhythm Mirror. Decide before public demo.

## One-line concept

Practice Mirror listens to what you play through a MIDI instrument and gives you one focused piece of coaching at a time. No score reading. No sheet music. Plug in, play, get a useful response, keep playing.

## Core thesis

Most music practice tools either teach fixed lessons or record performance passively. Practice Mirror acts as a focused practice partner: it watches what the player is doing, understands the exercise or goal, gives only one useful correction at a time, tracks improvement across a session, and stays out of the way otherwise.

V1 does not need to be a full music education platform. It needs to be a sharp proof-of-concept and portfolio piece.

The architectural insight that makes this shippable in days: the AI is not responsible for raw real-time detection. The app computes structured musical facts deterministically from MIDI data, then asks the AI to translate facts into coaching language. Same pattern as Anchor’s V5.1 Pattern Insight Engine, different domain.

## Why this fits Symposium Studios

Combines AI-native product thinking, real-time interaction, music and creative tools, human feedback loops, lightweight agentic app building, and Marcus’s actual context as a musician. Portfolio piece visible in 30 seconds. Director Model proof-of-work in a second domain alongside Anchor.

## Hardware on hand

Marcus has an MPK25 (25 keys plus 8 drum pads). One controller covers both piano modes and drum modes. USB-MIDI, plug-and-play with Web MIDI API. No extra driver required on Chrome or Edge.

## MVP user story

A musician connects their MIDI keyboard or drum kit, chooses a simple practice mode, plays for two to five minutes, and receives clear feedback on timing, note accuracy, consistency, and one suggested improvement.

## V1 modes

### Free Play Listener

The app watches what the user plays and summarizes:

- common notes or chords

- tempo estimate

- timing steadiness

- repeated patterns

- strongest part of the session

- one improvement suggestion

Easiest mode to ship first. Works as a fallback for users without a specific exercise in mind.

### Scale Practice

User selects a key and scale. The app flags out-of-scale notes, repeated mistakes, uneven timing, hesitations, and overuse of one finger zone or note range.

Example feedback:

> You stayed mostly in A minor, but C# appeared four times. Your timing was steady in the first half and rushed slightly near the end. Focus on slower clean runs before increasing speed.

### Chord Recognition and Progression Coach

The app identifies chords from MIDI clusters and gives feedback on chord name, inversion guess, progression summary, repeated changes, awkward transitions, and suggested next chords.

Example feedback:

> You played Am, F, C, and G several times. The Am to F transition was slower than the others. Practice that change in isolation for one minute.

### Drum Groove Consistency

User selects a basic groove or plays freely. The app tracks kick and snare placement, hi-hat consistency, rushing or dragging, velocity spikes, and missed expected hits.

Example feedback:

> Your snare stayed consistent, but the kick rushed slightly before beat 3. Keep the hi-hat quieter and use it as the timing anchor.

## Feedback philosophy

The app must not flood the musician with commentary.

Rules:

- One correction at a time

- Prefer specific observations over praise

- Do not interrupt every mistake

- Let the user finish a phrase before feedback

- Separate live feedback from end-of-session summary

- Avoid vague feedback like “good job” or “nice feel” unless paired with a specific observation

- Prioritize timing, accuracy, and repeatable practice actions

Good feedback:

> Your right hand rushed the last two notes of the pattern. Slow the phrase down and repeat only that ending.

Bad feedback:

> Great playing. Keep going.

## Product shape

### Main screen

- Device connection status with MIDI device selector

- Practice mode selector

- Key, scale, or groove selector depending on mode

- Start session button

- Live event visualization (optional, for transparency)

- Current coaching note (one card at a time, replaces previous)

- Session timer

- End session button

### End session summary

- Total notes or hits

- Estimated tempo

- Timing consistency

- Accuracy score (if in structured mode)

- Most common mistake

- Best improvement signal

- Suggested next exercise

## Technical architecture

### Frontend

- React + Vite, single page app

- Web MIDI API (native browser, no library required)

- Tone.js for note name resolution and music theory helpers

- Local session state in memory for V1

- Minimal design, dark practice-room feel

### Backend

V1 has no backend if all session analytics run locally and the AI summary call goes straight from browser to OpenAI or Claude with a session-scoped key.

Optional minimal backend for AI summaries:

- Send compressed session stats only

- Never send raw audio (there is no audio captured anyway)

- Generate concise coaching summary

- Save practice history later (V2)

### AI layer

The AI is not responsible for real-time detection. The app computes structured musical facts first, then asks the AI to convert facts into coaching language.

Example structured payload from app to AI:

```json

{

"mode": "scale_practice",

"key": "A minor",

"duration_seconds": 180,

"total_notes": 243,

"out_of_scale_notes": {

"C#": 4,

"D#": 2

},

"timing": {

"estimated_bpm": 92,

"rushing_detected": true,

"rushing_window": "final_45_seconds"

},

"most_repeated_pattern": ["A", "C", "E", "G"],

"suggested_focus": "reduce rushing at phrase endings"

}

```

Example AI response:

```json

{

"headline": "Good scale focus, slight rushing near the end.",

"observations": [

"You stayed mostly inside A minor.",

"C# appeared 4 times.",

"Your timing became less steady in the final 45 seconds."

],

"next_exercise": "Play the same pattern at 70 BPM for two minutes and focus only on clean endings."

}

```

This separation is the architectural unlock. Deterministic analytics produce trustworthy facts. AI handles only the language layer. Same pattern as Anchor’s Pattern Insight Engine.

### Browser support

Web MIDI API is supported in Chrome and Edge. Not supported in Safari or Firefox. Note this in onboarding and gate the connection flow accordingly. A future native wrapper (Electron or Tauri) can extend support if demand justifies it.

## Phrase detection

A short silence (configurable, default 1.5 seconds) signals the end of a phrase and triggers analysis. The AI does not interrupt mid-note. It waits for a natural pause. This prevents the “AI talking over the musician” failure mode.

## V1 scope

Ship these:

- MIDI device connection UI with device selector

- Instrument mode toggle: Piano or Drums

- Four practice modes (Free Play, Scale Practice, Chord Recognition, Drum Groove)

- Live MIDI event display (optional toggle)

- Phrase detection with configurable silence threshold

- AI feedback display: one card per phrase, replaces previous

- Session log: last 10 feedback cards, exportable as text

- End-of-session summary screen

Stretch if quick: chord name displayed in real time as notes are held (piano mode only).

## V1 no-go scope

Do not include in V1:

- Full curriculum

- User accounts

- Payments

- Social features

- Audio transcription

- Advanced music theory engine

- Fingering detection

- Marketplace of lessons

- Teacher dashboards

- Mobile app stores

- Polished gamification

- AI improvising over the user

- Live voice interruption

The proof is simple: can the app observe structured musical input and return useful coaching?

## V2 candidates

- Save practice history

- Weekly progress summaries

- Custom practice goals

- Drum rudiment mode

- Chord progression library

- Call-and-response ear training

- Multi-instrument sessions (piano melody over drum groove)

- Shareable session summary link

- Native wrapper for Safari/Firefox support

- Practice streaks without cheesy gamification

- Integration with Marcus’s full studio MIDI setup

## Demo script

A strong public demo:

1. Open Practice Mirror in Chrome

1. Connect MPK25

1. Choose “A minor scale practice”

1. Play for 60 seconds

1. App shows detected notes live

1. End session

1. App says:

> You played 86 notes over 60 seconds. You stayed mostly in A minor, but hit C# three times. Your timing drifted faster near the end. Practice the same run at a slower tempo and focus on clean endings.

Legible as a working AI-native creative tool in under a minute.

## Quick ship path

Day 1: MIDI connection, phrase detection, OpenAI feedback loop working end-to-end in browser. Piano modes (Free Play and Scale Practice).

Day 2: Chord Recognition mode, Drum Groove mode, coaching posture tuning, session log, UI polish.

Day 3: Deploy to Vercel, public URL, portfolio write-up, demo video.

## Portfolio positioning

Possible headline:

> Practice Mirror: a real-time MIDI-aware music practice coach. Built by Symposium Studios.

Positioning angle:

- Not a toy chatbot

- Not generic music theory

- Not a lesson library

- A small real-time AI feedback loop

- Proof of human-in-the-loop creative tooling

This sits well alongside Anchor as a Symposium Studios portfolio piece because it shows the same architectural pattern in a different domain: observe state, interpret behavior, give bounded feedback, help the human improve.

Marcus is the user. Drummer, guitarist, vocalist. Demos it himself. The maker plays it.

## Director Model proof-of-work

Practice Mirror built via the Director Model in a short session is a strong secondary case study alongside Anchor. The methodology generalizes across product categories: recovery tech and music tech, same Director Model, same agentic build process, same deterministic-facts-plus-AI-language pattern.

## Open questions before building

- Feedback latency tolerance: is two to three seconds per phrase acceptable, or does it need to be under one second?

- Should drumless piano (pure melody) be supported in V1, or assume chordal/harmonic playing?

- Demo-first or feature-first: build for the demo video first, then fill in edge cases?

- Public domain choice: practicemirror.app, symposiumstudios.com/practice-mirror, or other?

## Restraint note

This is interesting and shippable quickly, but it should not interrupt active Anchor build cycles or higher-priority obligations. Best use right now is to keep this parked as a Symposium Studios concept and build only when a clean window opens (Anchor V5 phases complete, no production fires, no other commitments compressing the schedule).
