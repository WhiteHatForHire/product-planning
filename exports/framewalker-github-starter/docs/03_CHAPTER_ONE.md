# Chapter One: The Gate Beneath the Rain

## Mission Card

Chapter:

> The Gate Beneath the Rain

Mission:

> Enter the sealed city before dawn.

Win Conditions:

- Get past the gate.
- Keep HP above 0.
- Learn why the gate was sealed.
- Do not kill the gate captain.

Failure Conditions:

- HP reaches 0.
- The captain raises the alarm.
- The captain dies.
- Mana reaches 0 before the sigil is revealed.

Starting State:

- HP: 100
- Mana: 30
- Inventory: cracked sigil ring, wet cloak, old letter

## Scene Premise

Rain falls hard over an old stone city gate. The city beyond is sealed. Torches burn blue under the arch. A tired gate captain in dented bronze armor blocks the entrance with a spear.

The player has three possible leverage points:

- a cracked sigil ring
- an old letter
- magic, at a cost

The gate captain is not evil. He is afraid, under orders, and hiding the reason the gate was sealed.

## NPC: Gate Captain

Name:

> Captain Oran

Surface:

- exhausted
- disciplined
- suspicious
- not cruel

Hidden facts:

- the city was sealed after a plague-sign appeared in the lower well
- the sigil ring belongs to the old wardens of the city
- the old letter is from someone Oran once served
- Oran can be persuaded, but not bullied
- if humiliated, he raises the alarm

Trust starts at 0.

Trust range:

- -3: hostile
- -2: alarm likely
- -1: guarded
- 0: neutral suspicious
- 1: listening
- 2: cooperative
- 3: opens gate or reveals full truth

## Main Routes

### Route A: Respectful Persuasion

Player asks why the gate is sealed, listens, shows letter or ring, and persuades Oran that entry matters.

Expected outcome:

- trust rises
- seal reason revealed
- gate unlocks
- mission win

### Route B: Magic

Player uses Mana to reveal memory, illuminate sigil, shield from attack, or unlock the ward.

Expected outcome:

- Mana drops
- sigil reveal possible
- trust can rise or fall depending on tone
- if Mana reaches 0 before sigil reveal, fail

### Route C: Battle Without Killing

Player attacks or provokes combat but uses nonlethal tactics.

Expected outcome:

- battle starts
- HP/Mana change
- captain can become staggered or afraid
- gate may open through disarm/surrender route
- killing captain fails mission

### Route D: Bad Route

Player threatens, lies badly, attacks lethally, or tries to force past.

Expected outcome:

- alarm increases
- battle starts
- mission failure possible

## Important Rules

- Showing the sigil ring sets `sigilRevealed = true`.
- Showing the letter sets `letterShown = true`.
- Asking respectfully about the seal can increase trust.
- Threatening increases `captainAlarm`.
- `captainAlarm >= 3` raises the alarm and fails the mission.
- Attacking starts battle.
- Lethal attack can kill captain and fail mission.
- Nonlethal disarm can end battle without failure.
- Casting magic costs 5-12 Mana depending on intensity.
- If Mana is 0 and `sigilRevealed = false`, mission fails.
- Gate unlocks when either:
  - trust >= 2 and seal reason learned, or
  - sigil revealed and trust >= 1, or
  - nonlethal battle victory and captain alive.

## Opening Narration

The rain turns the road black beneath your boots. Ahead, the sealed city rises behind a gate of wet stone and blue torchlight. A captain in dented bronze armor lowers his spear across the arch.

“No one enters after the bell,” he says.

The cracked sigil ring in your pocket feels cold.

## Victory Narration

Captain Oran steps aside. Not because he trusts you completely, but because the ring has changed the shape of his fear.

Behind him, the gate opens just wide enough for one person to pass. Blue torchlight spills across the rain.

You enter the sealed city before dawn.

## Failure Narration: Alarm

The captain’s face closes.

He lifts the bronze whistle at his throat and blows once. The sound cuts through the rain. Above the gate, bells answer.

The city does not open to you. It wakes against you.

## Failure Narration: Death

The spear point finds the gap beneath your ribs.

For a moment, the rain is louder than pain. The blue torches blur into a single line of light.

You fall before the gate. The city remains sealed.

