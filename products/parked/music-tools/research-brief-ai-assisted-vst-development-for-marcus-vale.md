---
title: "Research Brief AI Assisted VST Development for Marcus Vale"
source_archive: "Software Projects"
source_path: "####Software Projects/VSTs and music software /Research Brief_ AI-Assisted VST Development for Marcus Vale.docx"
status: reference
privacy: working
tags:
  - product
---

# Research Brief AI Assisted VST Development for Marcus Vale

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Research Brief: AI-Assisted VST Development for Marcus Vale

Core conclusion

The right first lane is AI-assisted VST effect prototyping, not full instruments, not Max for Live, and not a giant commercial plugin company.

Your strongest starting point is:

VST3 audio effect → built with JUCE → AI-directed C++/DSP/UI workflow → tested in a DAW → documented with demos.

For faster sonic sketching, use Faust, Cabbage, or plugdata as prototype engines. For serious “real plugin with custom UI,” use JUCE.

VST3 is the current target. Steinberg’s VST3 SDK is now available as open source under the MIT License, and the VST3 developer portal is the official source for VST3 plug-in and host development.

The main ways to build actual VSTs

1. JUCE: the main professional path

Best for: real commercial-style VSTs with custom UI, cross-platform builds, effects, instruments, MIDI tools, and long-term serious development.

JUCE describes itself as a widely used framework for audio application and plug-in development across Windows, macOS, Linux, iOS, Android, VST3, AU, AUv3, AAX, and related targets. It supports CMake and native project generation, which makes it a good fit for AI-assisted coding workflows using GitHub/Codex/Claude Code.

Why this is probably your main lane:

It creates real plugins, not toy patches.

It gives you UI control.

It has a large ecosystem.

AI coding agents will know it better than niche frameworks.

It fits the Director Model: spec → code → build → test → revise.

Downside: C++ and audio programming are real. AI can help a lot, but you still need testing, iteration, and eventually an audio dev reviewer.

Marcus fit: strongest long-term.

2. iPlug2: leaner C++ plugin framework

Best for: lighter-weight C++ plugin development with custom GUI and multi-format targets.

iPlug2 is a C++ audio plug-in framework that abstracts plug-ins through IPlug and provides IGraphics for audio-plugin GUI controls using bitmap or vector graphics.

Why it’s interesting:

Less heavyweight than JUCE.

Good for custom UI/audio effects.

AI can work with it, though there is less training/example density than JUCE.

Downside: smaller ecosystem, less “default industry path.”

Marcus fit: good second framework, not first.

3. DPF: open-source, minimal, raw plugin framework

Best for: open-source, custom UI, small efficient plugins, Linux-friendly development, VST3/CLAP/LV2 builds.

DPF can build LADSPA, DSSI, LV2, VST2, VST3, and CLAP from the same codebase and is designed around a simpler C++ API for audio plugins with custom UIs.

Why it’s interesting:

Lightweight.

Open-source oriented.

Good for experimental plugins.

Downside: rougher, more developer-ish, less hand-holdy than JUCE.

Marcus fit: later, if you want open-source/audio-nerd credibility.

4. Faust: DSP-first prototyping language

Best for: designing synth/effect algorithms quickly, then exporting or wrapping them into plugin architectures.

Faust is a functional language for sound synthesis and audio processing with a strong focus on synthesizers, musical instruments, audio effects, and high-performance signal processing; it targets plug-ins and many audio platforms.

Why it’s powerful:

Very good for DSP algorithms.

AI can help write Faust code for filters, delays, waveshapers, reverbs, compressors, modulation, etc.

Faust can be used with JUCE-style architectures and generated C++ workflows.

Downside: UI/product polish still needs another layer, usually JUCE or another framework.

Marcus fit: excellent for “sound engine first” experiments.

5. Cabbage: Csound-based plugin prototyping

Best for: fast audio instrument/effect prototypes using Csound with a GUI layer.

Cabbage is a framework for audio software development using markup text and the Csound audio synthesis language, targeting Windows, macOS, Linux, and Android from a single source file; its docs describe it as software for prototyping and developing audio instruments with Csound.

Why it’s interesting:

Good for quick audio experiments.

GUI possible.

Can be a strong “does this sound cool?” layer.

Downside: less ideal for polished commercial VST product identity unless you really commit to that ecosystem.

Marcus fit: good sketchpad, not main product stack.

6. plugdata: visual patching with VST3 export

Best for: visual DSP / Pure Data style patching, experimental plugins, fast sound exploration.

plugdata is a free open-source visual audio programming environment based on Pure Data, with VST3, AU, CLAP, and LV2 support; its docs describe DPF mode exporting self-contained versions of patches as plugin formats including VST3, LV2, CLAP, and JACK.

Why it’s interesting:

Visual patching may suit experimental audio.

Good for rapid sound sketches.

Could produce actual plugins, though workflow maturity needs testing.

Downside: may not be the best for polished custom UI/product-grade plugins.

Marcus fit: useful for play/prototyping. Not the core stack.

7. HISE: sample/instrument builder

Best for: sample-based instruments, hybrid instruments, Kontakt-like products, effects inside an instrument system.

HISE is an open-source toolkit for building virtual instruments, with modules like oscillators, samplers, envelopes, LFOs, EQs, convolution reverbs, routing, and containers; its GitHub description says it focuses on sample-based instruments and can export VST/AU/AAX plugins or standalone apps.

Why it’s interesting:

Strong if you want sample instruments.

Could be great for weird Marcus Vale instrument packs later.

Downside: not the cleanest first choice for an effects-pedal-style VST.

Marcus fit: later for sample instruments, not first.

8. SynthEdit / RNBO / visual-builder routes

SynthEdit offers drag-and-drop VST plugin building with no programming, but it is more of a visual construction kit than a from-scratch AI-directed coding workflow.

RNBO can export Max-like patches to targets including VST, Max External, and Raspberry Pi, but it requires the Max/RNBO ecosystem, and you already said you do not want Max for Live or a Max-centered workflow.

Marcus fit: useful to know exists, but not the main path.

Recommended Marcus stack

Main stack

JUCE + CMake + VST3 + GitHub + Codex/Claude Code

This is the real VST product path.

Sonic experiment stack

Faust for DSP kernels
 Use Faust to prototype the sound algorithm, then wrap into JUCE if it becomes real.

Experimental sketch stack

plugdata or Cabbage
 Use for weird sound ideas, quick sketching, and learning DSP intuitively.

Later instrument stack

HISE
 Use when the idea is a sample-based instrument, not an effects plugin.

Best first VST category

Start with an effect, not an instrument.

Best first concepts:

Character delay

Tape-ish, dub-ish, weird modulation, one or two signature controls.

Easy to demo on synth, guitar, drums, vocals.

Saturation / dirt / color box

Waveshaper, filter, tone, mix, maybe “instability.”

Very pedal-like.

Creative filter / movement plugin

LFO, envelope follower, stereo motion, resonance, drive.

Good for Todd Terje-ish movement.

Simple performance utility

One-knob riser, stutter, gated delay, freeze, DJ-ish moment tool.

Useful for live sets.

Marcus-style “pressure valve” audio effect

A weird conceptual plugin that turns chaos into controlled motion.

Could bridge your writing/product identity with music.

Do not start with:

full synth

advanced reverb

mastering compressor

pitch correction

AI audio generation plugin

multi-format commercial suite

sample library platform

Those are too big for V1.

How AI helps

AI can help with:

Product definition

plugin concept

user story

core controls

differentiator

reference plugins

MVP scope

“do not build” list

DSP design

delay line logic

filter choice

waveshaper math

LFO/envelope follower behavior

gain staging

oversampling notes

dry/wet mix behavior

anti-click smoothing

JUCE implementation

project skeleton

AudioProcessor structure

parameter tree

GUI layout

knobs/sliders

preset system

build instructions

VST3 export

Testing

DAW load test

bypass behavior

silence test

mono/stereo test

automation test

CPU test

clipping test

sample-rate test

preset save/load test

Brand/demo

plugin name

UI direction

demo session

before/after examples

landing page copy

short video script

beta tester checklist

But AI should not be trusted blindly for:

DSP correctness

real-time audio thread safety

memory allocation issues

denormals

latency reporting

licensing

installer/notarization

commercial release readiness

That’s where testing and possibly a human audio dev reviewer come in.

The first prototype workflow

V0: concept

Write a one-page plugin brief:

name

what it does

who uses it

3–5 controls

reference sounds

what makes it different

what is explicitly out of scope

V1: JUCE skeleton

AI builds:

basic VST3 plugin

UI with controls

dry/wet

gain staging

simple effect core

V2: sound engine

AI iterates the DSP:

delay/filter/drive/modulation

smoothing

anti-click

level matching

V3: DAW testing

Test in:

Reaper first, because it is lightweight and forgiving

Ableton/Logic/Cubase later depending platform

V4: demo

Make:

3 guitar demos

3 synth demos

3 drum loop demos

dry/wet comparisons

screen capture

V5: beta

Give it to a few musicians. Ask:

did it install?

did it crash?

did it sound useful?

what control confused you?

would you pay $19, $29, $49?

Do you need China?

For VSTs, no.

That is the beauty. Software music tools are the best first Maker Track because they avoid:

tooling cost

inventory

shipping

customs

returns

hardware QA

factory communication

minimum order quantities

VSTs are the cleaner first maker lane. Hardware later.

The order should be:

VST effects → VST instruments → MIDI utilities → hardware controller/pedal later.

That lets you build product taste, sound identity, demos, and audience without inventory risk.

What the game plan doc should be called

Marcus Vale AI-Assisted VST Prototyping Game Plan

Possible subtitle:

How to build real music plugins with AI, without becoming a traditional C++ audio engineer first

Proposed document outline

Executive Summary

Why VSTs Before Hardware

The Core Thesis: Marcus as AI-Native Audio Product Director

What “Actual VST” Means

The Development Paths

JUCE

iPlug2

DPF

Faust

Cabbage

plugdata

HISE

SynthEdit/RNBO

Recommended Stack

Best First Plugin Types

The First Plugin Sprint

AI’s Role in the Workflow

What AI Cannot Be Trusted With

Testing and QA Checklist

Release / Beta Strategy

How This Connects to Anchor, Director Model, and Music Work

Guardrails: No Side Quest Until Anchor Is Stable

Parking Lot of Plugin Ideas

First Prompts to Use Later

Final Recommendation

My recommendation

Your first VST should be a character effect, not an instrument.

Something like:

Drift Box
 A delay/filter/saturation/modulation plugin for synths, guitars, drum loops, and vocals. Five controls max. Beautiful UI. Island-dub/Todd-Terje-adjacent. Useful immediately.

This is much more realistic than a synth and much cleaner than hardware.

The lane is real. But park it until after Anchor production and a few more stable Build-mode days. This is a Maker Track, not today’s rabbit hole.
