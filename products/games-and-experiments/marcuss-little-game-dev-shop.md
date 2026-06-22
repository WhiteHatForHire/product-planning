---
title: "Marcus’s Little Game Dev Shop"
source_archive: "Software Projects"
source_path: "####Software Projects/Games /Marcus’s Little Game Dev Shop.docx"
status: reference
privacy: working
tags:
  - product
---

# Marcus’s Little Game Dev Shop

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Marcus’s Little Game Dev Shop

A code-first, agentic roadmap for making 2D games with no human employees

Working thesis

You can become a small game producer without hiring a traditional team by treating AI agents like a tiny studio.

Not “AI makes a game.” That framing is childish and wrong. The better model is:

Marcus is the producer, creative director, taste gate, scope governor, and final integrator. Agents are staff.

One agent writes core gameplay. One agent builds UI. One agent prepares tests. One agent slices spritesheets. One agent cleans asset folders. One agent writes design docs. One agent audits bugs. One agent packages builds. You direct, review, decide, cut scope, and preserve taste.

That is the same Director Model that showed up in the Jamie Stern engagement, adapted to game development.

The real opportunity is not making one giant dream game. The opportunity is learning how to run a solo AI-native game shop that can repeatedly produce small, playable, polished 2D games.

The shop starts with one proof-strike game.

One room. One character. One mechanic. One win condition. One mood.

Then it grows.

1. Why games are newly realistic for you

You already have several pieces that matter.

You can code. You understand web stacks, GitHub, local dev, CSS, JS, deployment, and product thinking. You can write specs. You can direct agents. You can make music. You can do sound design. You have taste. You can produce. You can write. You can market. You can narrativize the process.

A traditional indie game team needs:

programmer

game designer

producer

artist

animator

sound designer

composer

QA tester

marketer

build engineer

release manager

You cannot replace all of those with AI equally well. Visual taste and animation consistency are still hard. But you can reduce the team to:

Marcus as director / taste / music / story / final review

AI agents for code, docs, QA, asset processing, boilerplate, refactors, tests, build automation

AI image tools for concept art, sprites, backgrounds, effects, and iteration

free or purchased asset packs where AI art is not worth the time

The key is to run it like a shop, not like a fantasy.

Games are dangerous because they invite infinite scope. Agentic coding makes that danger worse unless the producer function is strong.

So the core virtue here is not Techne. It is Sophrosyne. Right measure.

2. The shop model

Call it:

Marcus’s Little Game Dev Shop

The shop has no human employees, but it has roles.

Marcus, Producer / Creative Director

Your job:

choose the game concept

define the mood

set the scope

approve or reject visual direction

approve or reject mechanics

write the brief

decide what ships

cut features

make music and sound if desired

playtest

market the result

archive the process

You do not “ask AI to make a game.” You produce the game.

Cloud Claude Code, Senior Gameplay Engineer

Best for:

implementing mechanics

building Phaser / LittleJS / Macroquad systems

creating PRs

refactoring code

wiring scenes

adding input handling

fixing bugs

asset loader code

animation state machines

build scripts

Codex, Systems Analyst / QA / Documentation Lead

Best for:

game design docs

mechanics specs

bug triage

test plans

prompt packs

roadmap docs

codebase audits

architecture comparisons

issue breakdowns

balancing tables

release checklists

Local Claude Code, Verification Engineer

Best for:

running the game locally

checking browser console errors

taking screenshots

testing build output

validating sprites and animations

checking performance

confirming that PRs actually work

packaging local builds

Image generation tools, Concept Artist / Sprite Intern

Best for:

concept art

character direction

environment mood boards

tile ideas

visual effects concepts

UI style references

rough sprite sheets

Weak at:

perfect consistency over many frames

exact animation loops

clean pixel-perfect sheets without post-processing

preserving the same character across many poses unless tightly guided

Audio tools + Marcus, Composer / Sound Designer

You already have a major advantage here. You can make music yourself. That matters because most small indie games feel cheap when audio is generic. You can give the game a real sonic identity.

AI can help with:

placeholder sound effects

foley prompts

organizing stems

creating sound cue lists

generating implementation tables

normalizing files

naming assets

compressing/exporting audio

But the musical soul can be yours.

3. Engine options, ranked for your actual workflow

The question is not “what is the best 2D engine?”

The question is:

Which stack lets Marcus run multiple coding agents, keep clean Git diffs, test in browser, handle assets sanely, and eventually package native builds without editor-state chaos?

Option A: Phaser + TypeScript + Vite + Tauri

Best first choice.

This is the most practical first proof-strike engine for you.

Phaser has an official Vite + TypeScript template with hot reloading, TypeScript support, and production build scripts, which makes it a natural fit for Cloud Code, Codex, GitHub PRs, and browser-first development. Phaser also has an official Tauri template that combines Phaser, TypeScript, Vite, and Tauri for desktop-style packaging later.

Tauri matters because it lets a web game become a small desktop app without bundling a full Chromium instance like Electron. The Tauri docs describe it as a framework for tiny, fast binaries using the operating system’s native web renderer, with any frontend framework that compiles to HTML, JS, and CSS.

Why Phaser fits your shop:

TypeScript aligns with your web background.

Vite means fast iteration.

Browser playable from day one.

Git diffs are normal code diffs.

Cloud agents can reason about files easily.

Playwright can test menus, boot, canvas existence, console errors, and input.

Tauri gives a later native desktop path.

Asset pipelines are straightforward: PNGs, spritesheets, JSON atlases, audio files.

Trade-offs:

Phaser is more framework than rendering library.

It has its own architecture.

Bundle size is larger than micro-engines.

It can become messy if you let scenes become giant god files.

Verdict:

Use Phaser first for the proof-strike game.

Option B: LittleJS

Best tiny-engine / anti-scope-creep choice.

LittleJS is a fast, lightweight, open-source HTML5 game engine focused on simplicity and performance. Its own repo describes it as including rendering, physics, particles, sound, and input handling, with clean documented code and examples.

The important thing is that LittleJS is small enough to understand. That is powerful for agentic work because an agent can read the whole engine, understand conventions quickly, and modify a small codebase without dragging in a giant framework.

Why LittleJS fits:

tiny footprint

code-first

browser-first

low ceremony

good for one-room games

easier to fork and understand than Phaser

strong for “don’t let this become the new bat”

Trade-offs:

smaller ecosystem

fewer tutorials and production examples than Phaser

less built-in structure

you may need to build more systems yourself

Verdict:

Use LittleJS for the second bake-off or if Phaser feels too heavy.

Option C: Macroquad

Best Rust / WASM wildcard.

Macroquad is a Rust game library inspired by Raylib. The docs describe it as simple and easy to use, friendly to Rust beginners, and supporting Windows, Linux, macOS, HTML5, Android, and iOS.

It is attractive because it gives you Rust, WASM, native targets, and a simple immediate-mode game loop without Bevy’s complexity. Macroquad’s web publishing guide also explicitly supports compiling to WebAssembly so people can play in the browser.

Why Macroquad fits:

simple game loop

Rust discipline

browser and native paths

good for small 2D games

less architectural overhead than Bevy

more “spartan programmer” than Phaser

Trade-offs:

Rust learning curve

slower agent iteration than TypeScript

more build/toolchain friction

you lose some of your existing web-stack advantage

Verdict:

Great as a technical-growth track. Not first unless you want Rust chops more than shipping speed.

Option D: PixiJS

Best custom-renderer route. Not first.

PixiJS is a 2D rendering library, not a full game engine. Its GitHub describes it as an HTML5 creation engine for fast, flexible 2D WebGL rendering, and Pixi docs include WebGPU renderer support.

Pixi is powerful if you want to build your own engine architecture: your own scene manager, input, physics, audio, state machine, asset pipeline.

Why Pixi fits later:

beautiful rendering

flexible architecture

great for custom visual systems

useful for UI-heavy or visual-effect-heavy games

very compatible with web tooling

Why not first:

you have to assemble too much yourself

agents can make architecture messes if the spec is not very strong

risk of building an engine instead of a game

Verdict:

Study later. Use only when you intentionally want a custom engine layer.

Option E: Godot

Best full engine, but editor-state heavy.

Godot is powerful and very attractive for actual game-making. It has exports, scenes, animation, tilemaps, UI, and an editor that is legitimately useful. Godot also supports command-line export, which is useful for CI, and headless mode for environments without GPU access.

Why it fits later:

great 2D tooling

real editor

animation tools

tilemaps

scene composition

export pipeline

good for richer worlds

Why it is not first for your current agent stack:

.tscn scene files can be brittle under agent edits

editor state matters

local verification becomes more important

Cloud Code can edit scripts, but scenes should be touched carefully

more human visual work required

Verdict:

Use Godot later for a visually richer game. First proof-strike should be code-first browser stack.

Option F: Defold

Best lightweight production engine with serious web/native support, but less aligned with your stack.

Defold is a free cross-platform engine for 2D and 3D games across desktop, web, mobile, and consoles, and its docs have a dedicated HTML5 development manual.

Why it fits:

production-ready

lightweight

strong HTML5 support

desktop/web/mobile

Lua scripting

good for polished 2D

Why not first:

Lua plus editor hybrid is not your main muscle

agent edits may interact with project/editor state

smaller overlap with your web deployment habits

Verdict:

Interesting for later if web performance and small builds become central.

Option G: Raylib

Best spartan programmer path. Not first for the shop.

Raylib is a great pure-code option if the goal is to learn fundamentals: game loop, input, rendering, collisions, audio. It is satisfying and direct. But C/C++ plus Emscripten/native build tooling adds friction for agentic shipping.

Verdict:

Use later if the goal is chops. Not first if the goal is a playable game and repeatable shop workflow.

4. The recommended path

Do not pick one engine forever. Run a bake-off.

The three-stack bake-off

Build the same tiny game in three stacks:

Phaser + TypeScript

LittleJS

Macroquad

Each game must be:

one room

one player

one interaction

one win condition

playable in browser

agent-written under your direction

no external asset dependency beyond placeholder shapes

done in one to three sessions

Score each stack on:

agent editability

setup friction

hot reload speed

browser deploy friction

native export path

asset pipeline friendliness

testability

code readability

fun factor

“does this make me want to keep going?”

The winner becomes the default engine for Marcus’s Little Game Dev Shop.

My prediction:

Phaser wins for shipping.

LittleJS wins for smallness and taste.

Macroquad wins only if Rust starts feeling spiritually right.

5. The agentic game repo structure

The first repo should look like this:

marcus-game-shop/

README.md

AGENTS.md

GAME_BRIEF.md

MVP_SPEC.md

MECHANICS.md

ART_DIRECTION.md

ASSET_PIPELINE.md

AUDIO_PIPELINE.md

TEST_PLAN.md

RELEASE_PLAN.md

ROADMAP.md

DEVLOG.md

src/

scenes/

systems/

entities/

components/

ui/

data/

assets/

raw/

processed/

sprites/

backgrounds/

tiles/

fx/

audio/

music/

sfx/

ambience/

tools/

slice-spritesheet.ts

validate-assets.ts

optimize-pngs.ts

generate-atlas.ts

check-audio-levels.ts

tests/

smoke/

e2e/

fixtures/

screenshots/

builds/

AGENTS.md

Defines rules:

no scope expansion without approval

no new engine without approval

no rewrites of architecture without approval

no deleting assets without approval

no changing art direction without updating ART_DIRECTION.md

one PR per logical change

stop on asset ambiguity

all generated assets must be tracked with prompt/source metadata

no copyrighted asset use unless license is clear

build must pass before PR

browser console must be clean

GAME_BRIEF.md

Answers:

what is the game

what is the mood

what does the player do

what is the one mechanic

what is the win condition

what is the visual style

what is the audio style

what is not in scope

MVP_SPEC.md

Defines the first playable vertical slice:

one scene

one player

one interaction

one fail or win state

placeholder art allowed

keyboard controls

browser build

one-minute play session

ART_DIRECTION.md

Defines:

resolution

palette

sprite dimensions

tile size

camera style

animation frame count

references

forbidden styles

UI style

export rules

ASSET_PIPELINE.md

Defines:

how concepts are generated

how sprite sheets are created

how backgrounds are made

how sprites are sliced

naming conventions

transparent backgrounds

atlas generation

compression

license tracking

human approval gates

AUDIO_PIPELINE.md

Defines:

music style

tempo range

loop length

file format

SFX categories

volume targets

naming conventions

implementation rules

6. The visual asset pipeline

Visuals are the hardest part.

Code is tractable with agents. Docs are tractable. Tests are tractable. Music is tractable because you can make it. Visual consistency is the major challenge.

So visual assets need a strict pipeline.

Rule 1: Placeholder shapes first

Never start with final art.

The first build uses:

rectangles

circles

colored zones

placeholder sprites

text labels

The first question is not “does it look cool?”

The first question is:

Is there a game loop?

Rule 2: Art direction before image generation

Before generating anything, define:

canvas resolution

target aspect ratio

tile size

sprite size

palette

line weight

camera distance

animation style

mood references

forbidden references

Example:

Visual style:

Moody 2D pixel art. 32x32 character sprites. 16x16 tiles. Limited palette:

black sand, moonlit blue, warm amber, moss green, faded coral. No glossy mobile-game look.

No chibi. No anime. No generic fantasy. No neon cyberpunk.

Rule 3: Generate concept art, not production sprites, first

Use AI image tools for:

mood boards

character silhouettes

environment compositions

UI direction

effects references

Then convert the best direction into game assets.

Rule 4: Sprite sheets need strict specs

For a player character:

Create a transparent-background pixel art sprite sheet.

Character: long-haired male island wanderer, shirtless or loose open shirt, black shorts, barefoot.

Style: moody 2D pixel art, limited palette, 32x32 frames.

Sheet layout:

Rows:

1. idle, 4 frames

2. walk down, 6 frames

3. walk up, 6 frames

4. walk left, 6 frames

5. walk right, 6 frames

6. interact, 4 frames

Frame size: exactly 32x32.

No shadows outside frame.

Transparent background.

Consistent character proportions across every frame.

AI may fail. That is expected. The pipeline includes rejection.

Rule 5: Agents process the sheet

Cloud Code can write tools to:

remove non-transparent backgrounds

slice frames

validate dimensions

generate atlas JSON

create animation metadata

optimize PNGs

detect inconsistent frame sizes

output a preview HTML page

build a contact sheet for review

Example tool outputs:

sprites/player/

idle_00.png

idle_01.png

idle_02.png

idle_03.png

walk_down_00.png

...

player.atlas.json

player.animations.json

Rule 6: Human taste gate

You approve:

does the character feel like the game?

are proportions consistent?

does movement feel alive?

does it look like generic AI sludge?

does it need to be redrawn, simplified, or replaced with an asset pack?

AI can make images. You decide whether they belong.

7. Animation pipeline

Start tiny.

Minimum animation set

For a first game:

idle

walk

interact

state change or “resolve” animation

Nothing else.

No combat animations. No inventory. No emotes. No cutscenes.

Animation implementation

Agents can wire:

animation keys

frame rate

looping behavior

directional mapping

idle fallback

state transitions

animation preview page

Example:

When player velocity is zero, play idle.

When moving horizontally, play walk_left or walk_right.

When moving vertically, play walk_up or walk_down.

When pressing interact near station, play interact once, then return to idle.

Animation acceptance criteria

no jitter

no wrong-facing frames

no frame bleeding

no broken transparent pixels

no inconsistent scale

animation works at 1x, 2x, and 3x scale

player remains readable against background

8. Backgrounds, tiles, and environments

For the first game, avoid complex parallax and giant maps.

Use one of three approaches:

Approach A: One painted background

Good for atmospheric narrative games.

Pros:

beautiful quickly

no tilemap complexity

strong mood

Cons:

less flexible

collision must be hand-defined

Approach B: Tilemap

Good for repeatable game systems.

Pros:

scalable

easy collision layers

reusable environments

Tiled integration possible

Cons:

more asset work

tile consistency matters

Approach C: Hybrid

One painted background plus invisible collision zones and interactive hotspots.

This is probably best for the first prototype.

Example:

beach background image

invisible rectangles for walkable area

three stations: Body, Work, Water

interaction prompts

simple state-routing mechanic

9. Effects pipeline

Effects matter because small games feel cheap without juice.

Start with simple effects:

screen shake

fade

pulse

particle burst

glow

vignette

noise overlay

thought bubble drift

sunrise transition

ocean shimmer

Agents can implement most of these.

Prompt rule:

Add juice, not scope.

Good prompt:

Improve game feel without adding new mechanics.

Add:

- subtle interaction pulse

- 150ms camera shake when state is misrouted

- small particle burst when state is resolved

- fade-to-sunrise win transition

Do not add:

- new levels

- new enemies

- inventory

- dialogue

- new UI screens

10. Music pipeline

This is your unfair advantage.

Most solo devs rely on asset packs or AI loops. You can make original music.

Music roles

For a tiny game:

title loop

gameplay loop

tension layer

resolution layer

short stinger when player wins

maybe one ambient bed

Marcus-made music workflow

Define mood in AUDIO_PIPELINE.md.

Record a 30-90 second loop.

Export stems:

drums/percussion

bass

pads

lead/melody

ambience

Agent normalizes and encodes files.

Game engine crossfades layers based on state.

For example, in Archipelago Mode:

low ambient ocean loop

soft percussion when player is regulated

noisy tension layer when too many thought bubbles stack

warm guitar/pad layer at sunrise

File format

For web:

OGG if supported

MP3 fallback

WAV only in source/raw, not deployed build

Naming

audio/music/archipelago_base_loop_90bpm.ogg

audio/music/archipelago_tension_layer_90bpm.ogg

audio/music/archipelago_sunrise_stinger.ogg

audio/sfx/resolve_state_01.ogg

audio/sfx/misroute_state_01.ogg

audio/ambience/ocean_night_loop.ogg

11. Sound effects pipeline

SFX can be:

handmade

recorded with phone

synthesized

generated by AI

from licensed packs

Start with a small SFX list:

interaction confirm

hover/select

state bubble appears

state bubble resolved

misroute

station activate

win sunrise

ambient ocean

soft UI click

Agents can help by:

creating cue sheets

checking missing files

normalizing loudness

converting formats

generating implementation maps

wiring sound triggers

12. QA pipeline

Games need QA earlier than apps because “it runs” does not mean “it feels good.”

Automated checks

For Phaser:

npm run build

browser opens

canvas mounts

no console errors

title screen appears

pressing start enters game

player moves

interaction prompt appears

win condition triggers

scene can restart

audio unlocks after user gesture

Playwright can test basic browser behavior, but it cannot fully judge game feel.

Manual smoke test

Every PR gets:

boot test

input test

collision test

interaction test

win-state test

audio test

screenshot check

console check

Game-feel review

Human only:

does movement feel good?

does the mood land?

does the loop make sense?

is it too busy?

is it boring?

is the visual style coherent?

is the audio annoying after 2 minutes?

13. Release pipeline

First release target:

Browser playable link.

Not Steam. Not iOS. Not Android. Not desktop app.

Release order:

local browser

deployed web link

itch.io page

Tauri desktop build

Steam someday, maybe

Web deploy

For Phaser/LittleJS:

Vercel, Netlify, Cloudflare Pages, or GitHub Pages

static build

no backend required

Desktop deploy

For Phaser:

Tauri

package for Windows/macOS/Linux later

not needed for prototype

Itch.io

Best first public home:

simple upload

playable in browser

devlog

screenshots

small audience

feedback

14. First prototype candidates

Prototype 1: Archipelago Mode

The most “you” concept.

A small self-governance game set on a beach at night.

Player stands on black sand. Islands sit on the horizon. Thought bubbles drift in from the edges. Each bubble represents a state: urge, work, loneliness, body, travel, money, relationship, fatigue.

The player routes states to stations:

Body

Work

Water

Rest

Connection

If routed well, the sky clears. If ignored, the screen gets noisy. If enough are resolved, sunrise.

Why it works:

autobiographical but not literal

one room

clear mechanic

visual mood

music-friendly

easy to scope

can become poetic without being a “mental health app”

Prototype 2: Agent Dispatcher

A Director Model game.

You are running a tiny AI shop. Tasks arrive. You route them to Cloud Code, Local Verify, Codex, or Human Review. Wrong routing creates bugs. Good routing ships PRs. Too much fatigue causes hallucinations.

Why it works:

directly linked to Jamie Stern

funny and meta

good for case-study content

mechanics are natural

Risk:

could become too inside-baseball

Prototype 3: Kuta Loop

A small island-life routine game.

Wake up. Choose gym, code, beach, social, food, rest. Energy, focus, and temptation shift. The goal is not maximum productivity, but right measure.

Why it works:

simple sim

body/work/temptation loop

Bali/Lombok visual identity

Risk:

can become too broad unless brutally scoped

Prototype 4: One-Room Vampire-Survivors Variant

Very mechanical.

One arena. Enemies represent distractions. Player survives by routing energy, not shooting.

Why it works:

proven loop

easy to tune

replayable

Risk:

less unique unless theme is strong

15. The first 30-day roadmap

Week 0: Shelf document and research

Goal: no build yet.

Artifacts:

this document

engine bake-off plan

asset pipeline notes

first prototype shortlist

do-not-start-yet rule

Week 1: Engine bake-off

Build the same micro-loop in:

Phaser

LittleJS

Macroquad

Each gets one short sprint.

Deliverable:

three browser-playable demos

one comparison doc

selected stack

Week 2: First proof-strike game

Using winning stack:

one room

one character

one mechanic

placeholder art

placeholder audio

win condition

Deliverable:

playable link

repo

devlog entry

Week 3: Art and sound pass

Add:

first real visual direction

one sprite

one background

one music loop

5-8 SFX

basic juice

Deliverable:

version 0.2 playable

Week 4: Polish and release

Add:

title screen

instructions

restart

itch.io page

short devlog

screenshots

one trailer/gif

Deliverable:

public microgame release

16. The operating rules

These are non-negotiable.

Rule 1: First game is not the dream game

It is a proof-strike.

Rule 2: One playable loop before any art obsession

If the game is not fun as boxes, art will not save it.

Rule 3: Add juice, not scope

Polish the loop. Do not add systems.

Rule 4: Agents do not own taste

Agents can generate options. You approve.

Rule 5: No engine switching mid-game

Bake-off first. Then commit.

Rule 6: No new mechanic without removing one

Scope stays finite.

Rule 7: All assets need provenance

Every asset must be:

made by Marcus

generated by AI with prompt/source stored

bought/licensed

free asset with license saved

Rule 8: Public release beats private perfection

Ship the tiny thing.

Rule 9: Archive the process

The making is part of the work. Devlog, screenshots, prompts, failures, fixes.

Rule 10: Anchor still has priority

This track is shelved until the active priorities allow it.

17. How this relates to your larger life

This is not random.

Jamie Stern proved that you can direct AI agents through a real inherited codebase. Neskala is teaching you how to write safety-critical prompt packs and build specs. Anchor is your personal/technical self-governance product. Game-making is the creative mirror of those systems.

A game is where:

music

code

visual taste

philosophy

self-governance

play

narrative

systems

can become one artifact.

That is why it feels attractive.

But that is also why it is dangerous. It can become a giant symbolic container for every identity at once. Musician, writer, coder, philosopher, game designer, founder, artist. That is too much for a first game.

So the right frame is:

Do not make the game that proves who you are. Make the tiny game that proves the shop can ship.

18. Recommended first build brief

Working title:

Archipelago Mode

Concept

A tiny 2D self-governance game set on a moonlit Indonesian beach. Thought-states drift toward the player. The player routes each state to the right station before the screen becomes too noisy. If enough states are resolved, sunrise arrives.

Engine

Phaser + TypeScript + Vite.

Platform

Browser first. Tauri later.

MVP

one beach scene

one controllable character

five drifting thought-state types

three stations

one routing interaction

one clarity/noise meter

one sunrise win state

Visual style

Moody 2D pixel art or low-res painterly pixel hybrid.

Palette:

black sand

deep blue

moon gray

warm amber

moss green

coral accent

Audio

Marcus-made ambient loop:

ocean bed

low percussion

warm guitar or synth layer

sunrise chord

Out of scope

inventory

dialogue

enemies

combat

procedural generation

multiple levels

save system

mobile controls

character customization

online leaderboard

Acceptance criteria

browser playable

no console errors

player can move

player can route states

win condition triggers

one music loop plays after user gesture

one screenshot looks good enough to share

full play session under 3 minutes

19. First agent prompts

Prompt 1: Scaffold

You are scaffolding a tiny 2D Phaser + TypeScript game.

Read:

- GAME_BRIEF.md

- MVP_SPEC.md

- AGENTS.md

Goal:

Create a Vite + Phaser + TypeScript project with one playable scene.

Constraints:

- One room only

- One controllable player

- One interaction

- One win condition

- No inventory

- No procedural generation

- No dialogue system

- No combat

- No external asset packs

- Use placeholder shapes first

- GitHub is source of truth

- Do not rewrite git history

- Stop on ambiguity that affects architecture

Acceptance criteria:

- npm install passes

- npm run dev starts

- npm run build passes

- Player can move with keyboard

- Player can interact with one object

- Win state appears

- Browser console has no errors

Prompt 2: State routing mechanic

Implement the first real mechanic.

Game:

Thought-state bubbles drift into the scene.

Each bubble has a type: body, work, water.

The player can pick up one bubble at a time and deliver it to the matching station.

Correct delivery increases clarity.

Wrong delivery increases noise.

When clarity reaches 5, trigger sunrise win state.

Do not add:

- new stations

- new levels

- inventory

- dialogue

- enemies

- new art

Acceptance criteria:

- bubbles spawn every 5 seconds

- player can pick up one bubble

- stations detect delivery

- clarity/noise UI updates

- sunrise triggers at clarity 5

- npm run build passes

Prompt 3: Juice pass

Add juice, not scope.

Improve:

- player movement feel

- interaction prompt

- bubble drift motion

- correct-delivery particle burst

- wrong-delivery screen pulse

- sunrise fade

Do not add:

- new mechanics

- new levels

- new bubble types

- dialogue

- inventory

- combat

Acceptance criteria:

- game loop unchanged

- scene feels more alive

- browser console clean

- build passes

Prompt 4: Asset pipeline

Create the first asset pipeline scripts.

Build tools:

- validate sprite dimensions

- slice spritesheet into frames

- generate animation metadata JSON

- optimize PNGs

- produce an asset report

Do not modify gameplay code.

Acceptance criteria:

- tools run via npm scripts

- invalid dimensions fail loudly

- output filenames are deterministic

- asset report lists every sprite and frame count

20. Final recommendation

Start with Phaser + TypeScript.

Run a bake-off against LittleJS and Macroquad later, but do not let the engine decision become the new bat.

The first real shop artifact should be:

A browser-playable tiny game made through the Director Model.

Not because it will be commercially successful. Because it proves the workflow.

Your real product is not one game yet.

Your real product is the ability to produce games.

That is Marcus’s Little Game Dev Shop.
