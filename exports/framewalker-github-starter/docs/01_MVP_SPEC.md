# MVP Spec

## MVP Goal

Build a browser-playable tech demo of one mission-based AI adventure chapter.

The demo must feel visually impressive, slow, cinematic, and governed. It does not need deep gameplay. It needs to prove the design system and the engine pattern.

## Chapter

Title: **The Gate Beneath the Rain**

Mission:

> Enter the sealed city before dawn.

Starting resources:

- HP: 100
- Mana: 30
- Inventory: cracked sigil ring, wet cloak, old letter

Starting situation:

The player stands outside a sealed city gate during heavy rain. A weary gate captain blocks the archway. The city has been sealed for reasons the captain does not fully explain. The player carries an old letter and a cracked blue sigil ring.

## Required UI

Single screen:

- large scene frame
- chapter title
- mission text
- HP bar
- Mana bar
- inventory row
- win conditions
- failure conditions
- narration panel
- text input
- submit button
- optional debug toggle

## Required Mechanics

Natural-language player input maps to action primitives:

- speak
- ask
- persuade
- deceive
- threaten
- inspect
- use_item
- cast_spell
- attack
- defend
- move
- wait
- surrender

State reducer resolves outcomes.

Required state variables:

- HP
- Mana
- captain trust
- captain alarm
- sigil revealed
- seal reason learned
- gate unlocked
- captain alive
- battle active
- mission status

## Required Frame Types

The MVP should support these visual frame types:

- `chapter_card`
- `scene`
- `sigil_reveal`
- `battle_start`
- `victory`
- `death`
- `mission_failure`

For the first implementation, these may render as placeholder images or static generated images. The image prompt generator must still produce prompts for each major frame.

## Required Rules

Examples:

- Showing the cracked sigil ring reveals the sigil.
- Asking about the seal can reveal why the city was closed if captain trust is high enough.
- Threatening the captain increases alarm.
- Attacking starts battle.
- Killing the captain fails the mission.
- Casting magic costs Mana.
- Using the old letter can increase trust or reveal a contradiction.
- Entering the gate wins only if the gate is unlocked and failure conditions are false.

## Required Debug Panel

Debug panel shows:

- raw player input
- parsed intent
- rule fired
- state before
- state after
- state delta
- narrator allowed facts
- image prompt for current frame

This panel is part of the tech demo. It proves governance.

## Acceptance Criteria

Automated:

- state initializes correctly
- HP/Mana bars reflect state
- each action primitive can be parsed from fixtures
- reducer updates state deterministically
- mission win can be reached
- mission failure can be reached
- death can be reached
- image prompt generator includes style, scene, continuity anchors, and no UI/text instruction

Human:

- first screen feels visually compelling
- mission is legible
- input feels expressive
- outcomes feel constrained but not brittle
- debug panel makes the engine visible

