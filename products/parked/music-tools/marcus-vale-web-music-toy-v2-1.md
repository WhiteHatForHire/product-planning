---
title: "Marcus Vale Web Music Toy v2 1"
source_archive: "Software Projects"
source_path: "####Software Projects/VSTs and music software /Marcus Vale Web Music Toy v2 1.docx"
status: archive
privacy: working
tags:
  - product
---

# Marcus Vale Web Music Toy v2 1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Marcus Vale Web-First Music Toy Development

v2.1 — Final Polish Before Archive

Browser prototypes first, Expo mobile ports second, native audio later. Author OS / Maker Track briefing — parked for later execution.

1. Core Thesis

Start with a web-first music toy, not VSTs and not native iOS. Build the first prototype as a browser app using Vite + React + TypeScript + Web Audio (with Tone.js as the V0 wrapper) + Canvas. Test with mouse and touch in the browser. Then port to Expo + react-native-audio-api when the concept is proven. Do not buy a Mac or enter Xcode setup until the project earns native audio depth.

Marcus does not need to become a traditional C++ audio engineer first. The first job is to direct a playable experience into existence. The browser is the cheapest proof layer. Expo + react-native-audio-api is the mobile packaging layer. Native audio is the later quality layer.

v2 strategic counter-frame worth considering:

POSSIBLE ALTERNATIVE PLAY

The strongest version of this lane might not be "Marcus ships Filter Creature." It might be: Marcus builds an open methodology for AI-directed music toys. Filter Creature is the first proof. The methodology is the asset. Same Director Model logic as the hardware doc. You're rare specifically because you can direct AI to build playable music software, test it as a real musician with taste, and document the process. The methodology plus a few small published toys is potentially a better long-term asset than one polished product. This doesn't replace shipping Filter Creature. It frames it.

The deeper goal: not just to make a toy, but to prove that Marcus can use AI to direct playable, expressive, educational music software from concept to demo. Filter Creature is proof. The method is the deeper product.

2. The Latency Reality — The Most Important Practical Truth

v1 buried this in a generic risk table. It deserves to be section 2 because it determines the whole strategy.

Expected/commonly observed latency ranges, to be validated on Marcus's actual devices in Sprint 0. These are benchmark hypotheses, not authoritative measurements — real numbers vary by browser version, device, OS version, and audio buffer settings.

Platform

Typical observed latency

Verdict

Desktop Chrome / Firefox

~5–20ms

Acceptable for almost everything.

Desktop Safari

~5–15ms

Fine.

iOS Safari

~50–150ms (varies by iOS version)

Often unusable for tight rhythmic interaction.

Android Chrome

~30–100ms (wildly variable by device)

Mediocre to bad.

iOS PWA (add-to-home-screen)

Same as Safari

No improvement over web. Distribution gain only.

Capacitor wrapper on iOS

Same as Safari (it's still WebView)

Not recommended for low-latency synthesis.

Expo + react-native-audio-api

~10–30ms on iOS (claimed)

Big win if validated. The mobile path.

Native iOS (AudioKit / AVAudioEngine)

~5–15ms

The gold standard.

WHY THIS MATTERS

Filter Creature is touch-based and needs sub-50ms feel. Above 50ms, the brain stops perceiving direct cause-and-effect. A child swiping the blob and hearing the pitch change 100ms later won't feel taught — they'll feel confused. The browser/PWA path is therefore a desktop-first product and a demo on mobile. The actual mobile product likely needs Expo + react-native-audio-api or native to feel right.

SPRINT 0 BENCHMARK TASK

Before committing to any architectural decisions based on these numbers, run a minimal tap-to-beep latency test on Marcus's actual devices: desktop Chrome, iPhone Safari, Android Chrome (if available), and later Expo + react-native-audio-api on a real iPhone. Feel-test rather than measure. The numbers in the table above are hypotheses to validate, not facts to plan around.

3. Why This Route Fits Marcus

The earlier VST and hardware tracks remain valid, but the browser-first music toy is the best first move. It combines synthesis, visuals, touch, education, play, and product taste without DAW compatibility, plugin signing, App Store native setup, PCB manufacturing, inventory, or Mac-only Xcode work.

Uses the current Windows machine and current AI builder workflow. No Mac required for V0–V1.

Creates a demoable object quickly: a URL anyone can open.

Lets sound design, visual metaphor, and learning design emerge before committing to native code.

Aligns with Marcus as orchestrator: concept, system, interaction, curriculum, sound, demo.

Can later become a mobile app, VST, hardware controller concept, or educational product.

Correct sequence: browser toy → mobile web → Expo app with real native audio → native/audio-engine rewrite if necessary → VST/hardware spinouts.

4. Competitive Landscape

v1 didn't engage with this. There's real existing product in the "teach synthesis in browser" space. Don't ship in the dark.

Product

What it is

How Filter Creature differs

Ableton Learning Synths (learningsynths.ableton.com)

Free, browser-based, beautifully designed synthesis tutorial. The gold standard.

Theirs is clean, instructive, sterile. Filter Creature is weird, alive, charming. Personality is the differentiator.

Chrome Music Lab (musiclab.chromeexperiments.com)

Google's free browser music experiments. Song Maker, Spectrogram, Strings, Chords.

Theirs is a collection of toys. Filter Creature is a single living creature with depth.

Moog Animoog / Model 15 / Filtatron

Native iOS synth apps. Paid. Polished.

Native, expensive, app-store. Filter Creature is browser-first, free or freemium, viral by URL.

Patchwerk (defunct)

Was a modular synth toy on iOS. Notable precedent.

Cautionary tale: niche audio apps are hard to keep alive. Plan for sustainability.

The honest positioning: Filter Creature competes most directly with Ableton Learning Synths on "teach synthesis in browser." Differentiator is charm and aliveness, not pedagogy alone. Lead the marketing with the creature, not the lesson.

Positioning note on kids: Filter Creature should be kid-friendly, not kid-targeted. Marketing it explicitly as a children's product triggers COPPA, App Store kids category requirements, and other compliance burdens that kill velocity. Build a delightful music toy that happens to work for any age. Revisit explicit kid-targeting only after compliance is understood.

5. Web-First Architecture

Build the browser prototype like a small instrument, not a generic website.

Layer

V0 choice

Reason

Build tool

Vite + React + TypeScript

Fast local dev, simple deployment, strong AI coding support.

Audio engine V0

Tone.js OR raw Web Audio

See section 7 for the real decision. Tone.js is faster for V0 but creates porting cost.

Audio engine V1

Raw Web Audio + AudioWorklet

More control, lower-latency custom DSP, ports cleanly to react-native-audio-api.

Visual layer V0

Canvas 2D + requestAnimationFrame

Plain Canvas runs at 60fps for organic shapes on any modern device. SVG is wrong for animated organisms.

Visual layer V1

PixiJS (WebGL)

Only when V0 Canvas hits perf limits. Most music toys never need this.

State

Zustand

Small, no-ceremony state for parameters, presets, modes.

Persistence

localStorage (V0), IndexedDB (V1)

Save creature presets locally without accounts or backend.

Hosting

Vercel or Netlify

Shareable URL is the first distribution mechanism.

Key browser-design rule

Do not build a full synth workstation first. Build one tiny instrument that feels alive within 60 seconds. The browser prototype proves interaction, not commercial audio depth.

Mouse/touch horizontal position → pitch.

Vertical position → filter cutoff or brightness.

Color → waveform or filter state.

Blob shape → resonance, envelope, LFO, or modulation depth.

Small lesson cards → explain what the user just heard.

Presets → save a creature state, not a boring technical patch.

6. AudioContext Unlock and Lifecycle — The Gotcha That Breaks Most Web Audio Apps

This is the single most common cause of "why is there no sound" in web music apps. Browsers (especially iOS Safari) require a user gesture to start audio. Sloppy implementations cause silence on first load, random silence after the screen sleeps, stuck notes when the AudioContext suspends, and crackling on resume.

The required pattern

Wrap audio init behind an explicit user gesture: "Tap the creature to wake it up."

Call Tone.start() (or audioContext.resume()) inside the gesture handler, not on page load.

Listen for the visibilitychange event. When the tab is hidden, suspend audio. When it comes back, resume.

Listen for AudioContext state changes (suspended, running, closed) and surface state in the UI.

On every meaningful gesture (tap, click, key), call resume() defensively. iOS Safari sometimes silently suspends.

Handle the iOS "silent switch" — by default, web audio respects the hardware mute switch on iOS. Use a webaudio-controlled audio element or accept the limitation.

Implement parameter smoothing on all knob/touch inputs. Unsmooth parameter changes click and pop. Use linearRampToValueAtTime() or setTargetAtTime().

Audio safety basics

Web synth toys can blow out ears. Build in protections from V0:

Default master volume low. Don't ship a toy that starts at full scale.

Limiter on master output (Tone.Limiter or a Web Audio DynamicsCompressorNode with aggressive settings) to catch parameter spikes.

No sudden full-scale bursts on first interaction. Ramp in.

Visible mute/panic button at all times. Tap it, sound stops immediately.

Quiet first-load message if relevant: "Start gentle. Headphones recommended."

7. The Tone.js → Mobile Porting Decision

v1 implied you could port Tone.js code to mobile easily. You can't. Tone.js is built on Web Audio but uses higher-level primitives (Tone.Synth, Tone.Filter, Tone.Transport) that don't exist in react-native-audio-api. You have to choose your strategy upfront.

Three options, ranked by long-term efficiency

Strategy

V0 speed

Mobile cost

Recommended for

Option 1: Write at Web Audio API level from the start

Slower (more verbose)

Low — code ports directly to react-native-audio-api

Experienced web audio devs. Best long-term.

Option 2: Build a thin abstraction layer (createSynth, createFilter, createTransport) with web and native implementations

Medium — extra week of architectural work upfront

Low — just swap implementations

RECOMMENDED for Marcus's use case. Best balance.

Option 3: Use Tone.js for V0, accept full audio rewrite for mobile

Fastest

High — full mobile audio rewrite later

Throwaway prototypes only.

Recommendation: Option 2. The extra week of architectural work upfront saves a month later. If the project gets parked after V0, no harm done. If it ships to mobile, you've already done the hard work.

8. Mobile Path — The Honest Version

v1 said "no Mac required" too generously. v2 is honest about the staircase.

Stage

Mac required?

Notes

V0 browser prototype

No

Build and deploy from Windows. Test on real iPhone via deployed URL.

V1 mobile web polish / PWA

No

Tune for iPhone Safari. Add-to-home-screen flow. Still served from URL.

V2 Expo development build with react-native-audio-api

Helpful but not required

EAS Build produces iOS binaries in the cloud. Apple Developer account needed ($99/year). Local debugging is easier on Mac but possible without.

V3 native iOS audio (AudioKit / AVAudioEngine / AUv3)

Required

Xcode is Mac-only. This is the quality tier.

V4 App Store submission

Strongly recommended

Possible without Mac via EAS, but App Store Connect quirks are easier to handle on Mac.

Practical: Marcus can ship V0–V2 from Windows. Buy a Mac when V3 native audio is justified by V2 traction. Don't buy a Mac speculatively.

9. Mobile Audio Libraries — The Real Landscape

v1 listed react-native-audio-api and expo-audio as somewhat interchangeable. They're not.

Library

What it actually does

Use it?

react-native-audio-api (Software Mansion)

Web Audio API–compatible implementation for React Native. Aims to bring synthesis, routing, and real-time audio control to RN. Actively developed.

LEADING CANDIDATE — not a guaranteed final engine. Validate with a one-oscillator latency test before porting Filter Creature.

expo-audio

Audio file playback and recording. NOT a synthesis engine.

Only for sample playback or recording. Cannot replace Tone.js.

react-native-track-player

Background audio playback for music apps. Not synthesis.

No, for our use case.

JUCE for React Native (community wrappers)

Bring native JUCE C++ audio into RN. Heavy. Powerful.

Maybe at V3 if native audio depth is needed.

CRITICAL DETAIL

react-native-audio-api requires an EAS development build. It will NOT run in Expo Go. Plan for this from sprint 1 of the mobile work, not later. Skipping straight to development builds saves time.

Mobile visuals: react-native-skia

Not in v1. Should be. Skia is the GPU-accelerated 2D rendering engine that powers Flutter. Software Mansion's react-native-skia brings it to RN. For animated organic visuals (Filter Creature's blob), it's dramatically better than the alternatives.

Hardware-accelerated, 60fps even on older devices.

Drop-in replacement for Canvas/PixiJS-style work on mobile.

Same vendor as react-native-audio-api, so they integrate cleanly.

Recommended visual layer for V2+.

Capacitor: not recommended for low-latency synthesis

v1 called Capacitor a "legitimate route." For a real-time synthesis app like Filter Creature, it's not — Capacitor wraps your web app in a WebView, and WebView audio = browser audio = same iOS Safari latency. You gain App Store distribution and lose nothing on the web side, but you don't get the audio improvement that's the whole point of going native.

Capacitor can still be useful for non-real-time music education tools, content libraries, account systems, or playback-heavy apps where direct touch-to-sound feel isn't the product. Just not for music toys where the latency is the experience.

10. Product Concepts — Trimmed to Three

v1 listed seven concepts. v2 keeps three: the V0 prototype, the long-term franchise candidate, and the adjacent direction worth parking.

Concept A — Filter Creature (V0 prototype, recommended start)

Difficulty: Low/Medium. The right call for V0.

One animated organism teaches oscillator, filter, resonance, and envelope through touch.

Single screen, single sound source, single living visual object, one learning layer.

Concept B — Patchlings (long-term franchise candidate)

Difficulty: High. Don't start here, but worth parking.

Small cartoon synth modules connect like living creatures. Drag cables to learn signal flow.

Modular synth as living creatures is a real pedagogical idea. Strongest "long-term franchise" concept.

Not a V0. Possibly a V3+ once Filter Creature ships and the methodology is proven.

Concept C — Drift Box Web (adjacent direction, parked)

Difficulty: High. Not for V0.

Browser-based dub delay / filter / saturation toy for guitar, synth, voice, drum loops.

Live audio input from the browser is its own world of pain — getUserMedia() permissions, latency stacking, mobile microphone routing, AGC issues.

Adjacent to the hardware Drift Box concept. Could be a software version of the hardware design later.

Cut from v1: Sound Garden, Orbital Synth, Analog Lab Kids (Arturia owns the name anyway), Pocket Sequencer Terrarium. All revisitable later. None for now.

11. Filter Creature — V0 Spec

Small, teachable, playable, demoable. One screen, one sound source, one living visual object, one learning layer. No accounts. No backend. localStorage only if trivial.

One animated blob/creature on screen.

Click/touch and hold starts sound.

Horizontal movement → pitch.

Vertical movement → low-pass filter cutoff.

Tap/click cycles waveform: sine, triangle, square, saw.

Mouse wheel or small slider → resonance.

Blob color changes with waveform.

Blob brightness/size changes with amplitude or filter cutoff.

Short learning card explains the active concept: pitch, filter, waveform, resonance, envelope.

Presets later become creatures: Warm, Glass, Bug, Bass, Ghost.

Success test (cognitive): someone should understand the relationship between motion, visual change, and sound change within one minute, without reading a manual.

Success test (behavioral): a user keeps touching the creature for 60 seconds without being instructed to. Charm first. This is the real music-toy test.

12. Development Phases

Sprint 0: Setup

Create React + Vite + TypeScript repo.

Decide audio strategy upfront (see Section 7). Recommended: build the abstraction layer.

Deploy a hello-audio page to Vercel/Netlify.

Confirm sound starts on click/touch and works on iPhone Safari.

Implement the AudioContext unlock pattern from Section 6.

Sprint 1: One-screen sound blob

Build the organism on Canvas with requestAnimationFrame.

Map pointer position to pitch and filter cutoff.

Add waveform cycle on tap.

Add basic visual response (color, size, brightness).

Implement parameter smoothing on all audio params.

Sprint 2: Learning overlay

Add labels and lesson cards.

Explain pitch, filter, waveform, resonance in plain language.

Lead with charm. The creature is the teacher.

Sprint 3: Presets and mutation

Add five creature presets: Warm, Glass, Bug, Bass, Ghost.

Add a random mutation button.

Save state to localStorage if easy.

Sprint 4: Mobile web polish

Tune for touch (large hit areas, no hover-dependent UI).

Test portrait mode.

Implement the full AudioContext lifecycle from Section 6.

Test on real iPhone Safari and Android Chrome.

Acknowledge: mobile web latency is not great. This is the demo, not the final product.

Sprint 5: Decision point

If concept proves out on web, proceed to Sprint 6 (mobile native).

If concept doesn't prove out, archive and start over with a different toy.

The Director Model says: ship V0, decide from evidence, don't sunk-cost.

Sprint 6: EAS development build with react-native-audio-api

Set up Expo project with react-native-audio-api and react-native-skia.

Create EAS development build (NOT Expo Go — won't work).

Port the audio abstraction layer's native implementation.

Test audio latency on real iPhone.

v1 had this as two sprints (5 and 6). Wrong: react-native-audio-api requires EAS dev build from day one. Don't waste a sprint testing in Expo Go.

Sprint 7: Mobile polish

Port visuals to react-native-skia.

Test on multiple iPhone models and one Android.

Compare audio feel to browser version. The latency improvement should be obvious.

Sprint 8: Product decision

Decide: continue web/PWA path, ship Expo to App Store, pivot to native iOS, or spin sound engine into VST.

This is also the point to decide on the methodology counter-frame: is Filter Creature the asset, or is the methodology the asset?

13. AI-Assisted Workflow

The AI workflow mirrors the Director Model. Marcus remains the product director and musician. AI agents create drafts, code, test plans, explanations, UI options. Marcus tests the feel and decides what survives.

AI role

Output

Product Design Agent

MVP brief, feature boundaries, user stories, do-not-build list.

Audio Engine Agent

Tone.js / Web Audio graph, parameter smoothing, synth voices, filters, effects. Write at Web Audio level for portability.

Visual Interaction Agent

Canvas 2D animation, organic blob behavior, audio→visual parameter mappings.

Learning Design Agent

Synthesis lesson progression. Beginner-friendly language. Charm-forward, not classroom-forward.

QA Agent

Test checklist for browser, iPhone Safari, Chrome, headphones, latency, stuck notes, touch gestures, AudioContext unlock, parameter smoothing.

Mobile Porting Agent

Translate web audio to react-native-audio-api. Identify incompatible browser-specific APIs. Port visuals to react-native-skia.

Demo Agent

Demo script, screen recording plan, landing page copy, beta invite.

14. Technical Risk Map

Risk

Mitigation

Audio must start from user gesture

Implement the full pattern from Section 6 (AudioContext lifecycle). Start every sprint with this in mind.

iOS Safari audio is high-latency

Acknowledge browser is desktop-first product. Mobile native (Sprint 6+) is where mobile feels right.

Mobile latency varies by device

Test on real devices, not just simulators. Plan for variation.

Tone.js → mobile is not lift-and-shift

Pick porting strategy in Section 7 upfront. Recommended: build abstraction layer.

Expo Go can't run react-native-audio-api

Use EAS development builds from day one of mobile work.

Parameter changes click and pop

Use linearRampToValueAtTime or setTargetAtTime on every audio param. Smooth touch input too (one-pole filter is fine).

AudioContext suspends on tab hide / device sleep

Listen for visibilitychange. Resume on every gesture defensively.

iOS silent switch mutes web audio

Document the limitation or work around with audio element trick.

Live mic input (Drift Box Web)

getUserMedia() permissions are user-hostile on mobile. AGC interferes. Latency stacks. Treat as a separate engineering project.

Overbuilding lessons before toy is fun

Charm first. Lessons follow charm. If the creature isn't fun, no lesson saves it.

Kid-focused privacy and App Store compliance

Don't claim "for kids" until COPPA/App Store kids category compliance is understood. Just ship a music toy that happens to be kid-friendly.

Scope creep

One screen first. One creature first. One sound first.

15. Prompt Pack

Use these prompts later. Do not run them today unless this becomes the active Maker sprint.

V0 browser prototype prompt

You are helping me build a web-first experimental music toy called Filter Creature.

Goal: React + Vite + TypeScript browser app where a single animated creature teaches basic synthesis through sound and motion.

Stack: React, Vite, TypeScript, Web Audio API (with thin abstraction layer for future mobile portability), Canvas 2D, no backend, no accounts.

V0 requirements: one screen, large animated blob, click/touch-and-hold starts sound, horizontal pointer = pitch, vertical pointer = low-pass filter cutoff, tap cycles waveform, slider/wheel = resonance, color maps to waveform, size/brightness maps to amplitude/cutoff. Include AudioContext unlock pattern, parameter smoothing on all params, visibilitychange handling. Include one learning card. Must run with npm install / npm run dev.

Deliver: file structure, full code, setup commands, testing checklist (including iPhone Safari), known limitations, next steps.

Code review prompt

Review this React/Web Audio music toy for correctness, simplicity, audio safety. Check for: stuck notes, AudioContext start/unlock issues, missing parameter smoothing (clicks/pops), excessive CPU use, mobile Safari risks, visibilitychange handling, overcomplicated React state, accessibility, touch problems. Suggest minimal fix list. Do not rewrite unless necessary.

Mobile porting prompt

We have a working browser prototype using a Web Audio abstraction layer. Plan the port to Expo + react-native-audio-api. Evaluate: which abstraction-layer code ports directly, what needs native-specific implementation, react-native-skia for visuals, EAS development build setup, audio latency expectations on iOS vs Android, minimum proof-of-concept tasks. Return clear porting plan and risk list.

16. Later Upgrades — VST, Native iOS, Hardware

VST later: if the sound engine becomes musically useful, rebuild as a JUCE VST3 effect or instrument. Different skill stack — C++ — and probably a contractor or AI-directed C++ effort, not Marcus hand-coding.

Native iOS later: if the mobile toy needs deeper low-latency audio or App Store polish, move to Swift/AudioKit or JUCE on a Mac.

Hardware later: if a touch controller or pedal-like interaction emerges, consider a hardware prototype after software proof. Connects to the hardware track doc.

Education later: if users actually learn from the toy, build a structured synthesis course inside the app. But charm first.

17. Immediate Parking-Lot Instructions

Do not start this tonight. This is a Maker Track document. Anchor, sobriety stability, and the active AI builder workflow remain the priority. The music toy track becomes active only when Marcus intentionally starts a sprint.

Save this document in Author OS / Maker Track.

Create a project folder later: /Maker Track/Music Toys/Filter Creature.

When ready, start Sprint 0 only: create repo, hello audio, deploy URL, run the latency benchmark from Section 2.

Stop after a playable 60-second web demo before deciding Expo, VST, or hardware.

Pre-commit to the methodology counter-frame question (Section 1): is the asset Filter Creature, or is the asset the documented methodology that produced it?

ARCHIVE NOTE

This document is done enough to park. The next improvement should come from a working prototype, not more theory. The remaining unknowns — does AI build the creature reliably, does it feel fun in 60 seconds, does iPhone Safari feel too laggy, does the abstraction layer actually port — can only be answered by Sprint 0. More document refinement at this point would be fake precision. Next step is Sprint 0, not v3.

18. References

Competitive landscape (new in v2)

Ableton Learning Synths — https://learningsynths.ableton.com/

Chrome Music Lab — https://musiclab.chromeexperiments.com/

Moog Animoog (iOS) — https://www.moogmusic.com/products/animoog

Web audio core

MDN Web Audio API — https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API

MDN AudioWorklet — https://developer.mozilla.org/en-US/docs/Web/API/AudioWorklet

Tone.js official docs — https://tonejs.github.io/

Mobile audio (the named answer)

React Native Audio API (Software Mansion) — https://docs.swmansion.com/react-native-audio-api/

React Native Skia (Software Mansion) — https://shopify.github.io/react-native-skia/

Expo Audio SDK (for playback only, not synthesis) — https://docs.expo.dev/versions/latest/sdk/audio/

Expo and EAS

Expo EAS Build introduction — https://docs.expo.dev/build/introduction/

Expo development builds — https://docs.expo.dev/develop/development-builds/create-a-build/

Expo custom native code — https://docs.expo.dev/workflow/customizing/

React Native environment setup — https://reactnative.dev/docs/environment-setup

Web framework and tooling

Vite guide — https://vite.dev/guide/

React build app from scratch — https://react.dev/learn/build-a-react-app-from-scratch

PixiJS — https://pixijs.com/

Zustand — https://zustand.docs.pmnd.rs/
