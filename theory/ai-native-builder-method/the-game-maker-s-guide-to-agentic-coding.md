---
title: "The Game Maker s Guide to Agentic Coding"
source_archive: "Software Projects"
source_path: "####Software Projects/Techne /Game Development/The Game Maker_s Guide to Agentic Coding.docx"
status: active
privacy: working
tags:
  - studio-os
---

# The Game Maker s Guide to Agentic Coding

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
The Game Maker's Guide to Agentic Coding

A Mini Book for Building Small, Finished Games With AI

This guide is for the person who wants to make games, not manage a software cathedral.

You are allowed to start small. You are allowed to make strange little things. You are allowed to use an agent as a tireless collaborator, sketch partner, mechanic, tester, and sometimes patient rubber duck. The goal is not to become dependent on the agent. The goal is to become more capable because the agent helps you stay in motion.

Gili Drift is the right kind of beginning: one file, one loop, one mood, one promise to the player.

Collect anchors. Dodge jellyfish. Survive 60 seconds.

That is a game.

1. The Core Mindset

Agentic coding works best when you treat the AI like a junior-to-senior production partner with infinite patience but no lived taste unless you provide it.

The agent is good at:

Turning clear specs into code.

Keeping many details in working memory.

Refactoring without getting bored.

Writing tests and checklists.

Explaining code.

Generating variations.

Catching obvious bugs.

Translating fuzzy intent into implementation.

The agent is weaker at:

Knowing what feels fun without feedback.

Resisting overbuilding unless instructed.

Understanding your personal taste.

Judging visual charm without screenshots.

Knowing when a tiny imperfection is better than a perfect system.

Your job is not to write every line. Your job is to steer taste, scope, and judgment.

Use this rule:

The human owns the feeling. The agent owns the grind.

2. The Three Jobs of the Human

When building with an agent, the human has three jobs.

Taste

You decide what feels good, what feels ugly, what feels charming, and what belongs in the game.

The agent can generate ten variants. You decide which one stays.

Scope

You decide what not to build yet.

This is usually more important than deciding what to build. An agent left to its own scope will pad relentlessly. Saying no is your most-used verb.

Verification

You play the game. You test the loop. You notice what broke.

The agent can write code faster than you can read it. That makes verification more important, not less.

Agentic coding does not remove human responsibility. It moves the human higher up the stack.

3. The Small Finished Game Philosophy

A small finished game beats a huge unfinished one.

Every game should have:

A goal.

A verb.

A threat.

A feedback loop.

A start.

An ending.

A way to replay.

For Gili Drift:

Goal: survive 60 seconds.

Verb: drift and collect.

Threat: jellyfish.

Feedback: score, hearts, timer, glow, collision.

Start: title screen.

Ending: game over or victory.

Replay: restart and high score.

That is enough.

Before adding more content, ask:

Does this make the core loop better?

Can the player understand it in five seconds?

Can I finish it today?

Does it create a new testing burden?

Is it charm, depth, or clutter?

Good V0 games are not incomplete big games. They are complete tiny games.

4. Pick Your Fight: Tiny Game Archetypes

Before you can win your fight, you have to pick one. These archetypes are V0-friendly because each has a single dominant verb and a clear failure state.

One-Button Avoid-Em-Up

Move and dodge. One enemy type to start. Gili Drift fits here.

Good for: learning the full loop end-to-end. Trap: adding too many enemy types before the dodge feels good.

Timing Tap

Press at the right moment. Rhythm games, parry games, well-timed jumps.

Good for: instantly readable success and failure. Trap: making the timing window feel arbitrary instead of teachable.

Idle / Incremental Clicker

Click a thing, numbers go up, unlock more clicks.

Good for: zero-skill onboarding, satisfying number juice. Trap: never reaching a meaningful end state. Plan the ending early.

Falling Blocks Variant

Things fall. You sort, stack, match, or catch them.

Good for: clean grid logic, easy difficulty curves. Trap: thinking you have to clone Tetris exactly. Steal one mechanic, change the rest.

Memory / Pattern Matching

Simon-style. Show a sequence, repeat it, sequence grows.

Good for: minimal art, maximal tension. Trap: not enough variation between rounds.

Top-Down Survival

Stay alive for N seconds while waves escalate.

Good for: classic arcade tension, easy to extend. Trap: spawning enemies on top of the player. Always reserve safe space.

Endless Runner

Auto-scroll, single obstacle type, one input.

Good for: mobile-friendly, instant restarts. Trap: visual monotony. Vary the background even if the gameplay doesn't change.

Single-Screen Platformer

One screen, one goal, gravity, jumping.

Good for: physics that teach themselves. Trap: jump physics. They are deceptively hard. Get jump feel right before anything else.

Pick one. Finish it. Then pick another.

5. The Agentic Workflow

Think in passes.

Pass 1: Playable Skeleton

Ask the agent for the smallest playable version.

Example prompt:

Build a complete single-file browser game. Prioritize playability over architecture.

It must have start, play, lose, win, restart. Use canvas. No external assets.

Do not start with menus, upgrades, settings, lore, particle systems, or save files.

Start with the loop.

Pass 2: Feel

Once it runs, tune:

Movement speed.

Collision size.

Spawn timing.

Enemy count.

Timer length.

Score pacing.

Visual readability.

Prompt:

Playtest this as if you are looking for feel problems. Do not rewrite architecture.

Suggest tuning changes for movement, difficulty, collisions, and readability.

Pass 3: Juice

Juice is feedback that makes actions satisfying.

Add:

Glow on collectibles.

Blink on damage.

Screen tint on pause.

Score popups.

Tiny particles.

Squash, bob, pulse, wobble.

Smooth transitions.

Prompt:

Add lightweight game juice without changing the core rules.

Keep it readable and single-file.

Pass 4: Content

Only after the core feels decent:

Add enemy variants.

Add collectible types.

Add weather.

Add levels.

Add unlocks.

Content multiplies complexity. Add it after the loop works.

Pass 5: Polish and Packaging

Before sharing:

Test start.

Test movement.

Test collisions.

Test win.

Test loss.

Test restart.

Test high score.

Test browser reload.

Test mobile layout if relevant.

Prompt:

Review this game like a release candidate.

Find bugs, unclear UI, missing states, and anything that blocks a player from finishing a run.

6. The Play-First Rule

Before asking the agent for another feature, play the current build at least three times.

After each run, write one sentence:

Run 1: What confused me?

Run 2: What felt good?

Run 3: What is the smallest change that would improve the game?

Do not let the agent decide the next feature before the game has taught you what it needs.

The agent can generate possibilities. The game gives evidence.

7. The Session Start Prompt

Use this every time you return to a project. It prevents the agent from wandering off into refactors and helps you re-anchor on the current state.

We are continuing work on [GAME NAME].

Current version:

- [What exists now]

- [Known bugs]

- [What feels good]

- [What feels bad]

Today's goal:

- [One small shippable improvement]

Constraints:

- Keep the game playable after every change.

- Do not refactor unrelated code.

- Do not add new systems unless needed.

- Preserve existing controls and rules unless I explicitly say otherwise.

First, summarize what you understand.

Then propose the smallest safe implementation plan.

Then make the change.

Finally, verify the full loop: start, play, pause, win, lose, restart, high score, console errors.

This is the single most useful prompt in this guide. Save it. Reuse it.

8. Save Points

Before every meaningful change, create a save point.

Use names like:

gili-drift-v0f1-playable.html

gili-drift-v0f2-score-popups.html

gili-drift-v0f3-sprites.html

Or commit to Git:

git add .

git commit -m "V0F2: add score popups and damage flash"

Never let an agent make a large change without a way back.

If a change makes the game worse, revert. That is not failure. That is editing.

This is the single most under-used habit by people who fail at agentic coding. Agents can silently break working charm. Save points let you undo what an agent does to your game's feeling, not just its code.

9. How to Prompt for Games

A strong game prompt contains:

Platform.

Scope.

Theme.

Core loop.

Controls.

Game states.

Win condition.

Lose condition.

Art constraints.

Technical constraints.

Verification checklist.

The Gili Drift prompt worked because it told the agent what mattered most.

Priority order is powerful:

1. Make it playable from start to finish.

2. Make it readable and bug-free.

3. Add simple visual polish.

4. Do not overbuild.

Use priority order whenever you care about completion.

Good Prompt Pattern

Build [kind of game] called [name].

Hard scope:

- [files allowed]

- [libraries allowed]

- [asset rules]

- [runtime]

Core loop:

- [player action]

- [reward]

- [threat]

- [ending]

Must include:

- [states]

- [controls]

- [HUD]

- [restart]

Style:

- [mood]

- [visual direction]

Verification:

- [checklist]

Sharpening a Vague Prompt

The difference between a vague prompt and a workable one is rarely length. It is specificity.

Vague:

Make me a fun arcade game where you avoid stuff.

Workable:

Single-file browser game. Top-down. Player is a small boat. Three enemies move in slow sine waves. One collectible spawns every 3 seconds. 60-second timer. Win at survival. Lose at 0 hearts. Restart on key press.

Same idea. Same length. Wildly different output.

10. The Prompt Library

Add a Feature

Add [feature] to this game.

Keep it single-file.

Do not change unrelated behavior.

After editing, verify start, play, pause, game over, victory, restart, and high score.

Replace Art

Use these uploaded sprites for the boat, anchor, and jellyfish.

Keep collision fair and separate from sprite size.

Add fallback code art if an image fails to load.

Tune Difficulty

Tune this game for a 60-second run.

The first 15 seconds should be learnable, the final 15 seconds should be tense, and deaths should feel fair.

Give exact constants.

Add Polish

Add small visual polish only: particles, score popup, damage flash, and victory glow.

Do not add new game systems.

Explain Code

Explain this game code in sections.

Focus on game state, update loop, drawing, collision, input, and storage.

Show me where to modify common things.

Make a Release Checklist

Create a release checklist for this browser game.

Include gameplay, browser, responsive layout, localStorage, accessibility basics, and known limitations.

Bug Report Template

When something breaks, do not just say "it's broken." Use this:

Bug:

- What happened:

- What I expected:

- Steps to reproduce:

- Browser/device:

- Screenshot or console error:

- What changed right before this:

- Do not rewrite the whole game. Find the smallest likely cause.

Most bad debugging comes from vague bug reports. "Fix it" invites chaos. A good bug report gives the agent a target.

11. The Screenshot Loop

When something looks wrong, do not only describe it. Show the agent a screenshot.

Good screenshot prompts:

Here is the current game screen.

Review it as an art director and UI designer.

What is unclear, ugly, too small, too low contrast, or visually unbalanced?

Suggest specific changes, but do not change the rules of the game.

Use screenshots for:

UI layout.

Color contrast.

Sprite readability.

Mobile issues.

End screens.

Visual clutter.

Whether the game has charm.

Words explain mechanics. Screenshots reveal taste problems.

12. Game Theory for Tiny Games

Game design is not mainly about features. It is about decisions under pressure.

A player should constantly answer:

Where do I go?

What do I risk?

What do I gain?

Can I recover?

Should I be greedy?

In Gili Drift, the anchor asks:

Do you risk crossing near jellyfish for 10 points?

That is the whole game.

The Triangle of Tension

Most arcade games can be tuned with three forces:

Reward pulls the player.

Danger pushes the player.

Time pressures the player.

If the game feels boring:

Increase reward value.

Add more danger.

Reduce safe space.

Make the timer meaningful.

If the game feels unfair:

Reduce enemy speed.

Increase invulnerability.

Make collision radius smaller.

Spawn rewards away from enemies.

Give clearer warnings.

If the game feels random:

Make enemy movement more readable.

Give the player more control.

Avoid unavoidable spawns.

Keep threats visible before they matter.

The 5-Second Rule

Within five seconds, a player should know:

What they control.

What they want.

What hurts them.

Whether they are doing well.

If not, simplify.

The 60-Second Rule

For tiny games, one full run should be short enough that losing feels like an invitation, not a punishment.

Good run lengths:

20 seconds: toy or prototype.

60 seconds: arcade demo.

3 minutes: polished microgame.

10 minutes: session game.

Gili Drift uses 60 seconds because it is long enough for tension and short enough for replay.

13. Art Direction Without Being an Artist

You do not need masterpiece art. You need readable art.

Readable game art answers:

What am I?

What can I collect?

What can hurt me?

Where can I move?

What just happened?

For Gili Drift:

Boat: warm hull and sail, readable against teal water.

Anchors: yellow glow, clearly collectible.

Jellyfish: pink/purple, cute but dangerous.

Water: darker background, low-contrast motion.

UI: bright cream text, high contrast panels.

Code Art

The current game uses Canvas primitives:

Circles.

Ellipses.

Lines.

Curves.

Gradients.

Shadows.

Transparency.

Sine-wave animation.

This is perfect for prototypes because there are no asset files.

Use code art when:

You want a fast prototype.

You need everything in one file.

You want easy color changes.

You care more about readability than detail.

Sprite Art

Use sprites when:

You want personality.

You want a stronger visual identity.

You have custom art.

You want animation frames.

Good starting sprite sizes:

Player: 64x64.

Collectible: 32x32 or 48x48.

Enemy: 64x64 or 64x80.

Background tile: 256x256 or 512x512.

UI icons: 24x24 or 32x32.

Use transparent PNGs first. They are simple and reliable.

How to Add Your Own Sprites

Put files in an assets folder:

assets/

boat.png

anchor.png

jellyfish-pink.png

jellyfish-purple.png

Load them:

const images = {

boat: new Image(),

anchor: new Image(),

jellyPink: new Image(),

jellyPurple: new Image()

};

images.boat.src = "assets/boat.png";

images.anchor.src = "assets/anchor.png";

images.jellyPink.src = "assets/jellyfish-pink.png";

images.jellyPurple.src = "assets/jellyfish-purple.png";

Draw them:

ctx.save();

ctx.translate(player.x, player.y);

ctx.rotate(player.angle + Math.PI / 2);

ctx.drawImage(images.boat, -32, -32, 64, 64);

ctx.restore();

Keep collision separate from art:

player.radius = 18;

jelly.radius = 23;

The sprite can be pretty. The collision should be fair.

Sprite Checklist

Before using a sprite:

Is the silhouette clear?

Does it read at gameplay size?

Does it contrast with the background?

Is transparent padding reasonable?

Is the visual center where the collision center should be?

Does it still look good while rotating or moving?

14. Animation

Animation does not need many frames. Motion can come from math.

Cheap animation tricks:

Bob up and down with Math.sin(time).

Pulse glow with Math.sin(time * speed).

Rotate slowly.

Blink when damaged.

Move background waves.

Stretch particles outward.

Fade things out with alpha.

Examples:

const pulse = 1 + Math.sin(time * 4) * 0.08;

const bob = Math.sin(time * 3) * 4;

Animation should clarify state:

Invulnerable: blink.

Collectible: pulse.

Enemy: wobble.

Danger: flash or shake.

Victory: glow or brighten.

Do not animate everything equally. If everything moves, nothing matters.

Performance Budget

Tiny games can still tank if you spawn too much.

Rough budget for a single-file canvas game:

Particles: cap at 100 active.

Entities (enemies + collectibles + projectiles): cap at 50 active.

Per-frame Math.sin and Math.cos calls: cheap, do not worry.

Per-frame allocations: avoid creating new arrays or objects every frame inside the loop.

Shadows and gradients: nice once, expensive in quantity.

If FPS drops, the first three suspects are: too many particles, too many shadow effects, or new objects being created every frame.

Math-based motion (sine waves, lerps) is almost always cheaper than spawning new entities to fake motion.

15. Controls and Feel

Controls are the soul of small games.

Tune these before adding features:

Acceleration.

Max speed.

Friction.

Turn speed.

Collision radius.

Knockback.

Input buffering.

For a drifting boat:

Acceleration should feel soft.

Friction should keep motion under control.

Top speed should let you escape danger.

Turning should feel fluid, not slippery beyond control.

Ask the agent:

Help tune this movement. I want it to feel like a small boat drifting, but still responsive enough for an arcade game.

Suggest exact values and explain the tradeoffs.

Fair Collision

Players forgive danger they understand.

Use smaller collision than the sprite:

const hitDistance = player.radius + jelly.radius - 4;

Make collectibles generous:

const collectDistance = player.radius + 24;

That combination feels good:

Easy to collect.

Fair to avoid.

16. Difficulty Design

Difficulty should rise in a way the player can feel.

Simple patterns:

Add one enemy every 12 seconds.

Increase enemy speed slowly.

Spawn rewards in riskier positions.

Reduce safe areas.

Add a new enemy type halfway through.

Avoid:

Sudden unavoidable deaths.

Enemy spawning on top of the player.

Rewards spawning inside danger.

Difficulty spikes that feel random.

For V0, prefer one difficulty rule.

Gili Drift uses:

Start with 3 jellyfish.

Add one every 14 seconds.

Cap at 8.

Slightly increase drift speed over time.

That is enough.

Use the 60-second rule: a fresh player should be able to last long enough to understand the game. If most new players die in 10 seconds, the difficulty curve is broken, not the player.

17. The Build Ladder

Grow your game in versions.

V0F1: First Finished

Goal: playable from start to finish.

Features:

One player.

One collectible.

One enemy.

One win condition.

One lose condition.

Restart.

V0F2: Feel Pass

Goal: make the game nicer to touch.

Add:

Better movement tuning.

Score popups.

Particles.

Screen shake.

Better pause.

Improved mobile support.

V0F3: Asset Pass

Goal: replace code art with your sprites.

Add:

Boat sprite.

Anchor sprite.

Jellyfish sprites.

Water tile or background.

UI icons.

V0F4: Content Pass

Goal: add replay interest.

Add:

Rare golden anchor.

Fast jellyfish.

Slow pulsing jellyfish.

Current zones.

Floating hazards.

V1: Shareable Game

Goal: something you can show people.

Add:

Title polish.

Better instructions.

Balanced difficulty.

Save best time or score.

Browser and mobile checks.

Tiny credits.

This ladder keeps you from trying to build V1 before V0 exists.

18. How to Work With the Agent

Whether you are using Codex, Claude Code, Replit, Cursor, or another coding agent, the roles are the same.

Use the agent in roles.

Builder

Implement this feature. Keep scope tight. Do not refactor unrelated code.

Reviewer

Review this like a game bug pass. Prioritize bugs, broken states, and unfair gameplay.

Playtester

Pretend you played five runs. What feels confusing, too easy, too hard, or under-rewarded?

Tuner

Suggest exact tuning values for speed, spawn rate, timer, collision radius, and score.

Art Director

Give me an art direction for this game using simple sprites I can draw or upload.

Include palette, silhouette notes, and animation notes.

Producer

Make a version plan from V0F1 to V1. Keep each version shippable.

Teacher

Explain this code so I can modify it myself. Focus on the game loop, state, drawing, and collision.

Switching roles deliberately is how you get the most out of an agent. Don't ask the Builder for taste. Don't ask the Playtester for code. Name the role at the start of the prompt.

19. Avoiding Agent Traps

Agents love to help. Sometimes too much.

Common traps:

Too many files.

Too much architecture.

Features you did not ask for.

Fancy systems before the game is fun.

Generic visual style.

Hidden dependencies.

Broken interactions after large rewrites.

Silent rewriting of code that was already working.

Quietly added libraries that bloat the project.

Hallucinated APIs that look clean but do not exist.

Use constraints:

Do not add packages.

Do not change file structure.

Do not refactor unrelated code.

Keep this playable after every change.

Prefer simple code over clever code.

Ask for verification:

After editing, verify start, movement, pause, win, loss, restart, and console errors.

Pin behavior on what's working:

The boat movement currently feels right. Do not change boat acceleration, friction, or turn speed.

The best agentic coding habit is not prompting. It is insisting on finished increments.

Specific Polish vs Generic Polish

Beware of agentic polish that makes the game look smoother but less specific.

Generic polish says:

Neon glow.

Particle effects.

Cinematic UI.

Epic victory screen.

Specific polish says:

The anchor glints like sun on shallow water.

The jellyfish pulses like it is floating, not attacking.

The boat rocks after a hard turn.

The win screen feels like reaching shore.

Smooth is not the same as charming.

If you ask an agent for "polish," you will get the generic version every time. Describe the specific feeling you want, in your own words, with your own metaphors. The agent can implement specificity. It cannot generate it.

20. Debugging With the Agent

Most debugging time is wasted on bad communication, not bad code.

When something breaks:

Use the Bug Report Template (Section 10).

Take a screenshot if it's visual.

Copy the console error verbatim.

Note what changed right before the bug appeared.

Resist the urge to ask the agent to "rewrite it."

Useful debugging prompts:

Add console.log statements to help me understand why [behavior] is happening.

Do not change the logic yet.

Walk me through what this code does step by step.

I think the bug is in [specific area].

What are three possible causes of this bug, ranked by likelihood?

Do not change code yet.

The "do not change code yet" line is doing a lot of work. It keeps the agent in diagnosis mode instead of jumping to fix mode and possibly making things worse.

Always have a save point before letting the agent fix anything substantial. Always.

21. The Asset Pipeline

When you upload sprites later, use this workflow.

Step 1: Name Assets Clearly

Good:

boat-player.png

anchor-glow.png

jellyfish-pink.png

jellyfish-purple.png

water-tile.png

heart-ui.png

Bad:

image1.png

newfinalfinal.png

thing.png

Step 2: Ask for an Asset Audit

Prompt:

Inspect these uploaded sprites for gameplay use.

Tell me their dimensions, transparency, readability, likely draw size, and any collision concerns.

Step 3: Replace One Asset at a Time

Do not replace everything at once.

Order:

Boat.

Jellyfish.

Anchor.

UI icons.

Background.

After each replacement, test.

Step 4: Keep Fallback Art

If an image fails to load, draw the old code-art shape.

Pattern:

if (images.boat.complete && images.boat.naturalWidth > 0) {

ctx.drawImage(images.boat, -32, -32, 64, 64);

} else {

drawCodeBoatShape();

}

This prevents a missing asset from breaking the game.

22. UI and Screens

Small games need clear state.

Minimum screens:

Start.

Playing.

Paused.

Game over.

Victory.

Minimum HUD:

Score.

Health.

Timer or progress.

High score if replay matters.

UI rules:

Put important numbers at the top.

Use high contrast.

Do not cover gameplay during play.

Keep instructions short.

Repeat restart instructions on end screens.

Good copy:

Collect anchors. Dodge jellyfish. Survive 60 seconds.

Bad copy:

In this immersive aquatic survival experience, you must navigate a procedurally animated oceanic environment...

Tiny games need tiny words.

Accessibility Is Clarity

Even tiny games should be playable and readable. The good news: accessibility is not bureaucracy. It is clarity.

Quick checks:

Text contrast is strong.

Font size is readable on mobile.

The game does not rely on color alone (shape and motion matter too).

There is a mute button if sound exists.

Motion effects are not excessive.

Touch controls are large enough.

A game that's accessible is a game where intent reads cleanly. That's the same goal you already have.

23. Sound, When You Are Ready

Gili Drift currently has no sound. That is fine.

When you add sound, start with:

Collect.

Damage.

Victory.

Game over.

Button click.

Then add:

Soft water loop.

Gentle ambient tone.

Rules:

Sounds should be short.

Damage should be clear but not harsh.

Collect should feel rewarding.

Music should not fatigue after 60 seconds.

Always include mute if sound starts automatically.

For browser games, user interaction is often required before audio can play. Start sounds only after the player presses Start.

24. Testing Like a Game Maker

Do not only test that code works. Test that the player can have the intended experience.

Technical Checklist

Page loads.

No console errors.

Start button works.

Keyboard works.

Pause works.

Restart works.

Timer reaches zero.

Game over triggers at zero hearts.

High score persists.

Canvas resizes cleanly.

Gameplay Checklist

Can I understand the goal immediately?

Can I dodge reliably?

Can I recover from one mistake?

Can I see collectibles clearly?

Can I tell when I am invulnerable?

Do I want to try again after losing?

Does victory feel earned?

Balance Checklist

First 10 seconds: safe enough to learn.

Middle 30 seconds: interesting decisions.

Final 20 seconds: tense but fair.

Average new player can survive long enough to understand the game.

25. Definition of Done

A tiny game is done when:

A new player understands it within five seconds.

A full run can be completed.

Losing and winning both work.

Restart works.

There are no console errors.

The game has one memorable feeling.

The next feature would make it bigger, not better.

Done does not mean perfect.

Done means the promise was kept.

If the next feature would make the game bigger but not better, the game is done. Ship it. Start a new one.

26. The Charm Pass

After the game works, ask what makes it feel like itself.

Charm can come from:

A funny title.

A tiny animation.

A specific sound.

A weird enemy.

A local detail.

A victory phrase.

A satisfying collectible.

A visual motif.

For Gili Drift, charm might come from:

Anchors that sparkle like little treasures.

Jellyfish that wobble lazily instead of charging aggressively.

A boat that rocks after turning.

End-screen copy that feels breezy instead of dramatic.

Do not confuse charm with complexity. Charm is often one specific detail done with care.

Charm is usually born from imperfection that you decided not to fix. The thing that's slightly off, slightly weird, slightly yours. The agent will try to smooth those things out. Don't let it.

27. Your Personal Game Design Notebook

Keep a small design log.

Each session, write:

Date:

Version:

What changed:

What feels better:

What feels worse:

Next smallest shippable step:

This gives you memory across days.

Agents can summarize your log, but your taste comes from noticing.

28. Good Next Features for Gili Drift

Here are good additions in order.

Score Popups

When collecting an anchor, show +10 floating upward.

Why:

Better feedback.

Low risk.

Feels rewarding.

Damage Flash

Brief red edge glow when hit.

Why:

Makes damage obvious.

Helps players learn.

Golden Anchor

Rare collectible worth 50 points.

Why:

Adds greed.

Creates risk choices.

Current Zones

Soft water currents that push the boat.

Why:

Fits theme.

Adds movement variety.

Jellyfish Variants

Examples:

Pink: normal drift.

Purple: slow but larger.

Blue: faster but smaller.

Why:

Adds depth without new controls.

Sprite Pass

Replace code art with uploaded assets.

Why:

Gives identity.

Makes the game feel yours.

29. Bad Next Features for Gili Drift

Avoid these for now:

Inventory.

Shop.

Skill tree.

Multiple levels.

Dialogue.

Procedural map.

Complex physics.

Multiplayer.

Account system.

Online leaderboard.

These can be good later. Right now they would bury the clean loop.

30. From One File to a Real Project

Single-file games are wonderful for V0.

Eventually, you may want:

index.html

src/

game.js

drawing.js

input.js

entities.js

assets/

boat.png

anchor.png

jellyfish.png

Do this when:

The file becomes hard to navigate.

You have real assets.

You want multiple levels.

You want a build or deployment process.

Do not split early just to feel professional.

Professional means the player can play it.

31. The Taste Loop

The most important loop is not the game loop. It is the taste loop.

Build a tiny change.

Play it.

Notice one thing.

Adjust.

Play again.

Ask:

What did I feel?

What did I expect?

What confused me?

What made me smile?

What made me tense?

What made me bored?

This is where you become a game maker.

The agent can implement. The game teaches.

32. The North Star

For Gili Drift, the north star might be:

A breezy tropical dodging game where every anchor is a tiny temptation.

That sentence can guide decisions.

Does a feature support breezy? Does it support tropical? Does it support dodging? Does it support temptation?

If yes, consider it.

If no, save it for another game.

33. Your Next Session

When you come back, a good next prompt would be:

Let's make Gili Drift V0F2.

Add score popups, a small damage flash, and better victory polish.

Keep it single-file and do not add external assets yet.

Verify the full game loop after editing.

Or, if you have sprites:

I uploaded sprites for the boat, anchor, and jellyfish.

Integrate them into Gili Drift.

Keep fallback canvas art.

Keep collisions fair.

Do not change the game rules.

Better yet: use the Session Start Prompt from Section 7 as your default opener. Plug in the current state, today's goal, and let the agent re-anchor before touching code.

Closing

You are not trying to become someone who perfectly commands an AI.

You are becoming someone who can imagine a game, express it clearly, shape it through play, and use an agent to keep the work moving.

That is a real craft.

Start small. Finish often. Play your own work. Keep the charming parts.
