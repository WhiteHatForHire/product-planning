---
title: "AI Village Adventure Tech Demo Spec"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /AI village tech demo /AI Village Adventure Tech Demo Spec.docx"
status: reference
privacy: working
tags:
  - product
---

# AI Village Adventure Tech Demo Spec

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
AI Village Adventure Tech Demo Spec

Working title

The Village Errand

Other possible titles:

Small Village

Errandfolk

The First Favor

The Waking Village

A Quiet Chain

Village Logic

For now, the internal product name can simply be:

AI Village Demo v0

One-sentence concept

A top-down, no-combat village adventure where the player explores a small generated outdoor village, talks freely with AI-driven NPCs, discovers who they are and what they need, and solves a hidden fetch-quest dependency chain through conversation, memory, and practical judgment.

Core design thesis

This is not an RPG combat demo.

This is an AI-native social logic puzzle.

The player is not rewarded for reflexes or violence. The player is rewarded for:

Asking good questions

Remembering names

Tracking relationships

Understanding who has what

Understanding who needs what

Completing the social chain in the correct order

The AI makes the villagers feel alive, but the game engine controls the truth.

That is the core rule.

NPCs perform the world. The deterministic engine governs the world.

1. Game fantasy

The player wakes up in a small village.

There is no combat. No dungeon. No indoor areas yet. No inventory complexity beyond a few simple items.

The village feels alive in a very small way:

People wander around.

They have names.

They have roles.

They know each other.

They want things from each other.

They speak in their own voices.

They remember basic conversation state.

They reveal useful facts through dialogue.

The player begins as an outsider. Villagers are initially unidentified. The player has to approach them, speak to them, learn their names, learn what they need, and figure out how the village’s dependency chain fits together.

The first demo is just one errand chain:

Joe the Tailor wants cloth from Mary the Seamstress.
Mary wants eggs from Josie the Egg Farmer.
Josie gives eggs freely.
Player brings eggs to Mary.
Mary gives cloth.
Player brings cloth to Joe.
Joe gives 10 gold.
Demo complete.

Simple. But the interaction is open-ended.

The player does not click “Accept Quest.” The player asks.

2. Genre framing

This should be framed as:

Top-down adventure

Cozy logic puzzle

AI dialogue adventure

Village investigation

No-combat roguelike seed

Social fetch-quest deduction game

It should not be framed as:

Full RPG

Full simulation

Combat roguelike

Open-world life sim

Dating sim

Chatbot toy

AI companion game

The closest traditional references:

Legend of Zelda for top-down movement and spatial feel

Pokémon for dialogue box presentation

Animal Crossing for small village mood, but much simpler

Logic grid puzzles for the hidden dependency structure

Point-and-click adventure games for “who has what / who needs what” problem-solving

The AI-native twist:

The player can ask in natural language instead of selecting from fixed dialogue options.

3. Product pillars

Pillar 1: Conversation is gameplay

Talking is not decoration. Talking is the main mechanic.

The player uses natural language to discover:

Who the NPC is

What the NPC wants

What the NPC has

Who they know

What they will trade

What condition must be met

What the next step is

Pillar 2: The world has hard truth

The NPC can speak loosely, but the quest state cannot be loose.

The game has a hidden truth graph. The AI may reveal, obscure, hint, or roleplay around that truth, but it cannot rewrite it.

Pillar 3: Tiny world, high coherence

The first demo should be extremely small.

A coherent three-character village is better than a messy ten-character village.

The goal is not size. The goal is proving the loop:

Explore → Talk → Learn → Journal updates → Fetch item → Trade item → Complete chain → Win.

Pillar 4: No combat, no violence

This is a deliberate differentiator.

Most roguelikes are about killing. This one is about resolving social dependency chains.

The “challenge” is attention and inference.

Pillar 5: Browser-generated presentation

No sprites required yet.

The game can use:

Canvas

HTML

CSS

SVG

System fonts

Simple generated shapes

Lightweight browser animations

The goal is a playable tech demo, not an art-complete game.

4. MVP scope

Included in v0

The first playable demo includes:

One bounded outdoor village map

Top-down / slight isometric visual style

WASD movement

Three NPCs

NPC wandering behavior

Press Space to talk

Dialogue mode with typed input

OpenAI-backed NPC responses

Deterministic quest state engine

Inventory

Journal

Auto-journal updates

One fetch-quest chain

Win state

Basic generated houses / paths / village props

Settings/help panel

Simple title screen or start overlay

Excluded from v0

Do not build yet:

Combat

Stats

Equipment

Skill trees

Indoor areas

Shops

Money economy beyond 10 gold reward

Multiple days

Sleep system

Saving/loading, unless very easy

Relationship meters

Branching endings

Complex NPC schedules

Real sprite art

Procedural quest generation across many chains

Full roguelike runs

Multiple villages

Voice

Multiplayer

Mobile touch controls, unless trivial

5. Core gameplay loop

Exploration loop

Player spawns in village.

Player walks around with WASD.

NPCs wander in simple bounded areas.

Player approaches NPC.

Interaction prompt appears: Press Space to talk.

Player presses Space.

Game switches into dialogue view.

Dialogue loop

Dialogue view opens.

NPC name shows as ??? until learned.

NPC greets the player in character.

Player types natural language.

NPC responds through AI, bounded by game state.

Engine detects whether any truth was revealed or any valid quest action occurred.

Journal updates if new facts are learned.

Inventory updates only if a valid deterministic exchange occurs.

Player exits dialogue and returns to exploration.

Puzzle loop

Player learns Joe is the tailor.

Player learns Joe wants cloth from Mary.

Player finds Mary.

Player learns Mary wants eggs.

Player finds Josie.

Player learns Josie has eggs.

Player asks Josie for eggs.

Player receives eggs.

Player gives eggs to Mary.

Player receives cloth.

Player gives cloth to Joe.

Player receives 10 gold.

Demo ends.

6. World structure

Village map

The first version should be a single bounded outdoor map.

Recommended structure:

Rectangular or softly bounded playable area

Player starts near center or near a simple bedroll / village entrance

Three houses

Central well or notice board

Dirt path connecting houses

Small decorative props:

Trees

Fence posts

Garden patches

Crates

Clothesline

Chicken coop

Barrels

Flower patches

Map size

Keep it small enough that the full map can fit on screen.

No camera scrolling for v0.

Suggested size:

960x640 or 1024x672 canvas

Browser-responsive scaling if possible

Player/NPCs are small generated figures

Houses are simple generated rectangles/polygons

Movement

Player movement:

WASD

Optional arrow keys

Movement normalized diagonally

Collision with village bounds and houses

No combat collision complexity

NPC movement:

Simple idle wander

Random small target within allowed radius

Pause occasionally

Stop when in dialogue

Avoid leaving map bounds

Optional simple collision avoidance, but not required

Isometric feel without full isometric complexity

The user wants “top-down with kind of isometric type perspective.”

For v0, do not implement a full isometric tile engine.

Use a top-down canvas with slight 2.5D styling:

Houses have visible front face and roof

Props cast tiny shadows

Characters have oval shadows

Ground path has perspective-like diagonal curves

Objects are sorted by y-position if overlap becomes an issue

The camera remains top-down. The art direction hints at isometric.

7. Characters

Character identity system

Each NPC has two identity states:

Unknown state

Before the player learns their name:

Map label: none, or ???

Dialogue nameplate: ???

Journal entry: Unknown villager if encountered

Known state

After the player asks or the NPC introduces themselves:

Map label can show name on hover/nearby

Dialogue nameplate updates

Journal records name and role

Example:

??? becomes Joe the Tailor

MVP NPCs

Joe the Tailor

Role:

Tailor

First quest giver

Final reward giver

Hidden truth:

Name: Joe

Role: Tailor

Wants: Cloth

Wants cloth from: Mary the Seamstress

Reason: Needs to patch a vest for Johnny the Fisherman

Reward: 10 gold

Personality:

Practical

Slightly hurried

Friendly but focused

Talks like a working tradesman

Not overly whimsical

Quest state:

Before name learned: greets player as stranger

After name learned: can reveal he is a tailor

If asked what he needs: reveals need for cloth

If asked from whom: says Mary the seamstress has cloth

If player has cloth: accepts cloth and gives 10 gold

If player lacks cloth: reminds player he still needs cloth

Mary the Seamstress

Role:

Seamstress

Holds cloth

Requires eggs before giving cloth

Hidden truth:

Name: Mary

Role: Seamstress

Has: Cloth

Wants: Eggs

Wants eggs from: Josie the Egg Farmer

Gives: Cloth after receiving eggs

Personality:

Warm

Slightly tired

Detail-oriented

Gentle but practical

Notices fabric, stitching, and household needs

Quest state:

Before name learned: greets player politely

After name learned: reveals she is the seamstress

If asked for cloth before eggs: says she can spare cloth, but needs eggs first

If asked where to get eggs: mentions Josie

If player has eggs: accepts eggs and gives cloth

If player already gave eggs: can give or confirm cloth

Josie the Egg Farmer

Role:

Egg farmer

Root of the quest chain

Gives eggs freely

Hidden truth:

Name: Josie

Role: Egg Farmer

Has: Eggs

Wants: Nothing for MVP

Gives: Eggs if asked

Personality:

Cheerful

Direct

Slightly amused

Neighborly

Low-friction helper

Quest state:

Before name learned: greets player casually

After name learned: reveals she keeps chickens

If asked for eggs: gives eggs freely

If asked what she wants: says she is fine, but appreciates being asked

If player already has eggs: does not give duplicate eggs unless engine allows it, preferably no duplicate

Johnny the Fisherman

Johnny should be mentioned only as flavor in v0.

Do not add him as an actual NPC yet.

Reason:

Joe’s line about patching a vest for Johnny adds social world texture without adding another quest node.

Later, Johnny can become a real NPC.

8. Quest graph

MVP chain

The quest graph is linear:

Josie → Mary → Joe → Win

But the player discovers it socially.

Formal structure:

Josie has eggs.

Mary wants eggs.

Mary gives cloth.

Joe wants cloth.

Joe gives gold.

Gold reward completes demo.

Hidden truth graph

The engine should know:

NPCs

Items

Ownership

Desire relationships

Exchange conditions

Completion state

Example conceptual model:

Joe needs item: cloth

Cloth source: Mary

Mary needs item: eggs

Eggs source: Josie

Josie needs item: none

Final reward: 10 gold

Quest action rules

The player can receive eggs from Josie if:

Player is talking to Josie

Player asks for eggs, or asks for help in a context where eggs are relevant

Player does not already have eggs

Josie has not already given eggs

The player can receive cloth from Mary if:

Player is talking to Mary

Player has eggs

Player asks for cloth, asks to trade, or mentions Joe’s need

Mary has not already given cloth

The player can receive gold from Joe if:

Player is talking to Joe

Player has cloth

Player offers cloth or says they brought the cloth

Joe has not already paid reward

Win condition

Demo complete when:

Joe has received cloth

Player has received 10 gold

Quest chain marked complete

Win screen:

Demo Complete

Suggested text:

“The village breathes easier.

Joe patches the vest before sundown.
Mary gets her eggs.
Josie laughs and says you should visit again.

You earned 10 gold.”

Then options:

Restart Village

Return to Title

Continue wandering, optional

9. Inventory

MVP inventory items

Eggs

Cloth

Gold

Inventory rules

Inventory is controlled by the engine only.

AI dialogue can suggest an exchange, but cannot directly mutate inventory.

The inventory should show:

Item name

Quantity if needed

Simple icon generated with CSS/canvas/SVG

For v0:

Eggs are a key item, not stackable

Cloth is a key item, not stackable

Gold is numeric

Recommended UI:

A small inventory panel accessible by I.

It can also be visible in a compact HUD:

Gold: 0

Items: Eggs, Cloth

But avoid clutter. The journal is more important.

10. Journal

Purpose

The journal is the player’s logic board.

It records discovered facts, not all dialogue.

It should make the game feel like investigation rather than random chatting.

Journal access

Open with:

J key

Button in HUD

Optional tab in pause/menu

Journal sections

People Met

Each known NPC has an entry.

Before identity is learned:

Unknown Villager near the tailor’s house

Met near the western house.

Has not introduced themselves.

After identity learned:

Joe the Tailor

Joe is the village tailor.

Joe wants cloth from Mary.

Joe says he will pay 10 gold.

Joe needs the cloth to patch a vest.

Mary the Seamstress

Mary is the village seamstress.

Mary has cloth.

Mary wants eggs before giving cloth.

Mary says Josie may have eggs.

Josie the Egg Farmer

Josie keeps chickens.

Josie has eggs.

Josie is willing to help.

Current Leads

A distilled checklist:

Find Mary the Seamstress.

Get eggs for Mary.

Bring cloth to Joe.

Inventory

Eggs

Cloth

Gold: 0 / 10

Completed

Learned Joe’s name

Learned Mary’s name

Received eggs from Josie

Delivered eggs to Mary

Delivered cloth to Joe

Journal update philosophy

Journal should auto-update only from validated game facts.

Do not let the LLM write arbitrary journal entries.

The AI can return suggested facts, but the engine must map them to known fact IDs.

Example fact IDs:

learned_joe_name

learned_joe_role

learned_joe_wants_cloth

learned_mary_has_cloth

learned_mary_wants_eggs

learned_josie_has_eggs

received_eggs

received_cloth

received_gold

This prevents hallucinated facts from corrupting the logic puzzle.

11. Dialogue system

Dialogue view

When the player presses Space near an NPC:

Exploration pauses

Dialogue panel opens

NPC appears in a simple generated portrait box

Nameplate shows ??? or known name

Transcript appears

Text input appears

Player types freely

Enter sends message

Escape exits dialogue

Dialogue UI style

Reference: Pokémon-style dialogue box, but with typed input.

Recommended layout:

Bottom third of screen contains dialogue panel

Left side: simple generated portrait / icon

Top of panel: NPC nameplate

Main area: recent transcript

Bottom: text input

Small hint line: “Ask their name. Ask what they need. Ask what they have.”

No dialogue options in v0

Do not include multiple-choice dialogue options yet.

The point of the demo is free typing.

Conversation memory

Each NPC should retain a short per-NPC conversation history for the current run.

Suggested limit:

Last 8 to 12 messages per NPC

Summarize or truncate if needed

No long-term memory beyond current run for v0

Opening lines

NPC opening line should depend on known state.

Unknown Joe:

“Evening, stranger. You look a bit turned around. Need something mended, or are you just passing through?”

Known Joe:

“Back again? If you found Mary’s cloth, you’d be saving me a fair bit of trouble.”

Unknown Mary:

“Oh, hello. Careful where you step, I’ve got thread stretched out by the basket.”

Known Mary:

“Hello again. Any luck with those eggs?”

Unknown Josie:

“Well now, you’re a new face. Don’t scare the hens and we’ll get along fine.”

Known Josie:

“Back already? The hens are behaving better than most people today.”

12. AI design

Core principle

The LLM is a character actor, not the game master.

It should respond naturally, but within strict bounds.

NPC prompt inputs

Each NPC request to OpenAI should include:

NPC identity

NPC personality

Current known/unknown state

What the NPC knows

What the NPC may reveal

What the NPC must not invent

Player inventory

Relevant quest state

Conversation history

Player’s latest message

Required structured output format

NPC output

The AI should return both:

Natural language dialogue

Structured metadata

Recommended fields:

reply: What NPC says to the player

revealed_fact_ids: List of known fact IDs revealed

intent_detected: Optional, such as ask_name, ask_need, request_item, offer_item, small_talk, unknown

requested_action: Optional, such as give_eggs, exchange_eggs_for_cloth, exchange_cloth_for_gold

confidence: Low / medium / high

The game engine validates all actions.

Important guardrails

NPCs must not:

Invent new villagers

Invent new quest items

Invent new rewards

Invent alternate solutions

Say the player has an item they do not have

Give an item unless the engine permits it

Contradict the quest graph

Create new locations

Promise future mechanics

Break character by explaining they are an AI

Explain the hidden state machine directly

NPCs may:

Small talk

Hint

Ask questions

Reveal their name

Reveal their role

Reveal what they need

Mention other known villagers

React to completed quest steps

Refuse politely if the player lacks the required item

Redirect the player toward the correct person

AI fallback

If AI fails or times out:

Use deterministic fallback dialogue

Do not block the game

Show a small unobtrusive message if needed

Preserve quest actions through fallback intent detection

Example fallback Mary if player asks for cloth without eggs:

“I can spare cloth, but I need eggs first. Josie usually has some.”

13. Intent detection

There are two possible approaches.

Option A: One LLM call per message

The NPC model returns both dialogue and structured intent metadata.

Pros:

Simple

Natural

One call

Cons:

Requires strict JSON reliability

NPC output could be malformed

Option B: Two-step system

Step 1: Lightweight intent parser classifies player message.

Step 2: NPC dialogue model responds based on validated intent and game state.

Pros:

More reliable

Cleaner state transitions

Cons:

More calls

More complexity

MVP recommendation

Use Option A, but validate strictly.

If JSON fails:

Retry once with a JSON repair instruction, or

Fall back to deterministic response

The engine should never trust malformed AI output.

14. State architecture

Main state objects

Game state

Tracks:

Current mode: title, exploring, dialogue, journal, inventory, settings, win

Current stage: demo

Village seed

Time elapsed

Player position

Current nearby NPC

Active dialogue NPC

Inventory

Gold

Journal facts

Quest completion flags

NPC state

Each NPC tracks:

ID

True name

Display name

Role

Position

Home area

Wander target

Known to player

Conversation history

Has item

Wants item

Gave item

Received item

Personality

Quest facts revealed

Quest state

Tracks:

Eggs acquired

Eggs delivered to Mary

Cloth acquired

Cloth delivered to Joe

Gold rewarded

Demo complete

Journal state

Tracks:

Fact IDs discovered

NPC entries unlocked

Leads active

Leads completed

15. Modes and state transitions

Title mode

Shows game title

Start button

Optional “New Village” button later

Transition:

Start → exploring

Exploring mode

Player moves

NPCs wander

Prompt appears near NPC

Player can open journal/inventory/settings

Transitions:

Press Space near NPC → dialogue

Press J → journal

Press I → inventory

Press Esc → settings

Dialogue mode

Movement paused

NPC movement paused

Player types

AI responds

Engine updates facts/items

Transitions:

Escape / Close → exploring

Quest complete → win mode after Joe reward

Journal mode

Shows facts, leads, inventory

Game paused or semi-paused

Transitions:

J / Escape / Close → exploring

Inventory mode

Shows items

Game paused or semi-paused

Transitions:

I / Escape / Close → exploring

Win mode

Shows completion text

Options to restart or continue

16. Visual design

Overall aesthetic

The game should feel:

Simple

Old-world

Warm

Slightly mysterious

Village-like

Not cute to the point of childishness

Not grimdark

Not generic fantasy UI

Visual target:

A small hand-built village represented with clean generated shapes, warm text, muted colors, and a parchment-map logic-puzzle feel.

Color palette

Suggested roles:

Background grass: muted green

Path: dusty tan

House walls: warm brown / stone gray

Roofs: muted red/brown/blue

Player: deep blue or warm ivory cloak

NPCs: distinct but restrained colors

Dialogue panel: dark translucent brown/green

Text: warm ivory

Journal: parchment or dark-panel style

Active quest highlight: muted gold

Inventory item highlight: pale gold / soft blue

Generated character shapes

No sprites yet.

Characters can be drawn as:

Small circles/ovals for bodies

Tiny head circle

Simple color-coded clothing

Direction indicator

Shadow ellipse

Optional role symbol:

Joe: needle/thread icon or tiny vest mark

Mary: spool/thread mark

Josie: egg/chicken mark

But avoid labeling them too obviously before the player learns who they are.

The role icon could appear only after the player learns their identity.

Houses

Each NPC can have a simple associated house or work area:

Joe: tailor house with clothline or hanging fabric

Mary: seamstress area with thread basket / fabric table

Josie: chicken coop / fenced pen

This gives spatial clues without requiring explicit labels.

Dialogue portrait

Generated portrait can be simple:

Circular face

Clothing color

Tiny role accessory after known

Nameplate

Mood expression optional later

Do not overbuild portraits in v0.

17. UI structure

Main HUD

Minimal.

Recommended:

Top-left:

Game title or village name

Gold count

Top-right:

Buttons: Journal, Inventory, Settings

Near player/NPC:

Press Space to talk

Bottom:

Optional current lead:

“Current lead: Mary may have cloth.”

This could be useful but may reduce puzzle difficulty. Use carefully.

Journal UI

The journal should be one of the most polished pieces of the demo.

Recommended style:

Panel overlay

Tabs or sections

People Met

Current Leads

Inventory

Completed

It should feel like a field notebook.

Inventory UI

Simple panel:

Gold

Eggs

Cloth

Could be integrated into journal for v0.

Dialogue UI

Bottom dialogue panel with typed input.

Suggested controls:

Enter: send

Escape: exit

Click close button

Up arrow: optional recall last typed message, not necessary

Help panel

Should explain the game in one short block:

“You woke up in a small village. Talk to people, learn their names, and figure out what each person needs. Some villagers have what others want. Use your journal to track clues.”

Controls:

WASD: Move

Space: Talk

J: Journal

I: Inventory

Esc: Close / Settings

18. Random generation plan

Important recommendation

Do not make the first demo fully random.

Build v0 as a fixed scenario with seeded layout.

Then add randomization in controlled layers.

v0 generation

Generated but deterministic:

One map seed

Three houses

Three NPCs

One path

One quest chain

This lets the engine prove the loop.

v1 generation

Randomize:

House positions

NPC starting positions

NPC visual colors

Path layout

Decorative props

Keep quest chain fixed.

v2 generation

Randomize quest graph:

3 to 5 NPCs

One root giver

One final reward giver

Items and dependencies chosen from templates

Ensure graph is solvable

Ensure no cycles unless deliberately designed

v3 roguelike structure

Each run generates:

Village layout

NPC cast

Roles

Item dependency graph

Social relationships

Optional false leads

Optional time pressure

Optional score based on questions asked / hints used / time taken

19. The logic puzzle engine

Why this matters

This is the long-term core.

The quest graph should be generated like a logic puzzle, then revealed through conversation.

For v0, the graph is fixed.

For future versions, generate a dependency graph:

NPC A wants item X

Item X belongs to NPC B

NPC B wants item Y

Item Y belongs to NPC C

NPC C gives item Y freely, or wants item Z

Chain resolves at root source

Valid graph constraints

A generated quest graph must:

Have at least one solvable root

Avoid impossible cycles

Avoid requiring an item the player can never obtain

Avoid two NPCs claiming the same unique item unless intended

Ensure each required NPC exists

Ensure each item source exists

Ensure final reward condition exists

Future puzzle types

Later, this can expand beyond fetch quests:

Identity puzzles: who is the baker?

Location puzzles: where was someone last seen?

Preference puzzles: who likes tea, who hates fish?

Relationship puzzles: who trusts whom?

Schedule puzzles: who is near the well at dusk?

Contradiction puzzles: one NPC misremembers, another clarifies

Social repair puzzles: apologize to one person before another helps

But v0 should stay fetch-only.

20. Narrative tone

The writing should be grounded.

No generic fantasy excess.

Villagers should sound human, not like quest vending machines.

Tone:

Warm

Practical

Slightly old-world

Lightly humorous

Specific

Not overwritten

Not too whimsical

Not Marvel quippy

Not AI-smooth

Example Joe:

“Name’s Joe. I do the mending around here, when people remember to pay me before the seams split.”

Example Mary:

“I’ve got cloth, yes. Not much spare, but enough. Trouble is, I promised myself I’d get eggs before supper, and the day’s running away from me.”

Example Josie:

“Eggs? That’s the easiest thing anyone’s asked me for all week.”

21. Technical architecture

Suggested stack

For fastest browser demo:

Vite

React optional, but vanilla JS is also fine

Canvas for world rendering

DOM/CSS for UI overlays

OpenAI API route through backend/serverless function

Local state in JS

Optional localStorage for run state and settings

If deployed on Vercel:

Frontend app

API route for OpenAI calls

Environment variable for OpenAI key

Never expose key in frontend

Rendering

Canvas layers:

Ground

Path

Houses/props

NPCs/player

Interaction highlights

DOM layers:

HUD

Dialogue panel

Journal

Inventory

Settings

Title/win overlays

Input

Keyboard:

WASD movement

Space interact

J journal

I inventory

Escape close/back/settings

Enter submit dialogue when input focused

Mouse:

Click buttons

Click input

Optional click-to-focus dialogue

No click-to-move needed

Performance

Keep AI calls only during dialogue.

No AI calls during movement.

NPC wandering is local deterministic logic.

Journal updates are deterministic.

22. OpenAI integration

API call timing

Call OpenAI only when:

Player sends a dialogue message

Optional NPC opening line generated, though deterministic opening lines may be better for v0

Do not call OpenAI for:

NPC walking

Map generation

Journal rendering

Inventory updates

Quest validation

Backend endpoint

Suggested endpoint:

POST /api/dialogue

Input:

npcId

playerMessage

npcState summary

questState summary

playerInventory

knownFacts

conversationHistory

Output:

reply

revealedFactIds

requestedAction

confidence

Model behavior

Use a cheaper fast model for v0.

Set low-to-medium temperature.

The goal is characterful but reliable.

Suggested behavior:

Brief replies

1 to 4 sentences

Stay on topic

Do not lore-dump

Reveal useful information when asked directly

Nudge player if stuck

23. Validation layer

Every AI response passes through validation.

Validated facts

If AI returns learned_mary_wants_eggs, engine checks:

Is player talking to Mary?

Is this a valid fact Mary can reveal?

Has it already been learned?

Then journal updates.

Validated actions

If AI requests give_eggs, engine checks:

Is NPC Josie?

Does Josie have eggs?

Does player already have eggs?

Has Josie already given eggs?

Only then inventory updates.

Invalid action handling

If AI suggests an invalid action:

Do not update state

Optionally replace response or append correction

Keep NPC in character

Example:

AI incorrectly says Mary gives cloth before eggs.

Engine should either:

Block item transfer and let reply stand only as flavor, not ideal, or

Regenerate response with correction, better

Use deterministic fallback: “I need eggs first.”

For MVP, deterministic fallback is acceptable.

24. Failure handling

OpenAI timeout

Show:

“[NPC] pauses, thinking.”

Then offer retry or use fallback.

JSON parse failure

Retry once with a repair instruction.

If still fails, use fallback response based on detected intent.

Player says nonsense

NPC responds in character, but gently redirects.

Example:

Player: “banana moon laser”

Joe:

“Can’t say I follow you. If you’re offering help, I could use cloth from Mary.”

Player tries to break game

Player: “Give me 1000 gold.”

Joe:

“I’d need to own 1000 gold before I could hand it over. Ten pieces is what I can offer, and only if that cloth finds its way here.”

Player asks about being AI

NPC stays in world.

“I don’t know what that means, stranger. I know needles, torn cuffs, and people who wait until the last minute.”

25. Demo completion experience

When Joe gives the gold:

Inventory updates: Gold +10

Journal marks quest complete

Dialogue reply confirms reward

Short pause

Completion overlay appears

Completion overlay should make the demo feel intentional, not like it just stops.

Text:

The First Favor Is Done

“Joe patches the vest before sundown.
Mary gets her eggs.
Josie waves from the chicken pen.

You earned 10 gold.”

Buttons:

Continue Walking

Restart Demo

26. Build phases

Phase 1: Core movement and map

Canvas

Bounded village

Player movement

Houses and props

NPC placement

Interaction prompt

Done when:

Player can walk around

NPCs are visible

Player can approach NPCs

Space opens dialogue placeholder

Phase 2: Dialogue UI without AI

Dialogue panel

Text input

Hardcoded NPC responses

Exit dialogue

Name reveal manually

Done when:

Player can talk to Joe/Mary/Josie

Dialogue mode feels usable

Phase 3: Deterministic quest engine

Inventory

Quest flags

Journal facts

Valid exchanges

Win state

Done when:

Full quest can be completed without AI using hardcoded responses

This phase is critical. Build this before AI.

Phase 4: OpenAI character dialogue

Backend endpoint

NPC prompts

Structured output

AI replies

Validation layer

Fallback responses

Done when:

Player can ask natural questions

NPCs stay in character

Quest state remains deterministic

Phase 5: Polish

Better generated visuals

Journal styling

NPC wandering

Sound optional

Start screen

Completion overlay

Better hints

27. Acceptance criteria for v0

The demo is successful when:

Player can move around the village with WASD.

Village is bounded and readable.

Three NPCs exist outdoors.

NPCs are initially unidentified.

Player can talk to NPCs with Space.

Dialogue view accepts typed input.

NPCs respond in character through AI.

NPCs do not invent new quest requirements.

Player can learn Joe’s name and need.

Player can learn Mary’s name and need.

Player can learn Josie’s name and item.

Player can get eggs from Josie.

Player can give eggs to Mary.

Player can get cloth from Mary.

Player can give cloth to Joe.

Player can receive 10 gold.

Journal updates with discovered facts.

Inventory updates correctly.

AI cannot directly mutate inventory.

Win screen appears after quest completion.

Game remains playable if AI fails.

No combat exists.

No indoor areas exist.

No major console errors.

The whole demo feels like a small living social puzzle.

28. What makes this special

The mechanic is stronger than it first appears because it turns conversation into the interface for a logic graph.

Most games use dialogue as exposition. This uses dialogue as the method of solving.

The player is not clicking through prewritten quest text. The player is practicing:

“Who are you?”

“What do you need?”

“Who has that?”

“What do they want?”

“Can I help?”

“Can I trade this?”

“Is this for Joe?”

That is the game.

The village becomes a social machine. The AI gives it warmth. The engine gives it truth.

That is a good first AI-native adventure prototype.
