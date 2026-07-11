# Design System

## Visual Direction

Framewalker should feel like an illustrated dark-fantasy adventure book with modern game UI restraint.

Keywords:

- cinematic
- painterly
- rain, stone, bronze, torchlight
- serious, not cartoony
- restrained UI
- readable mission state
- mythic but not ornate

## Layout

Desktop MVP:

```text
┌────────────────────────────────────────────┐
│              Generated Frame               │
│                                            │
├────────────────────────────────────────────┤
│ Chapter title / mission                    │
│ HP bar     Mana bar      Inventory         │
│ Win conditions / failure conditions        │
│ Narration                                  │
│ [ What do you say or do?              ]    │
│ Debug toggle                               │
└────────────────────────────────────────────┘
```

Mobile can come later. Desktop-first is fine for the tech demo.

## UI Rules

- The image is the hero.
- The mission is always visible.
- HP and Mana are always visible.
- Win conditions are visible, not hidden.
- Failure conditions are visible enough to shape decisions.
- Inventory is compact.
- Text input is large and inviting.
- Debug is present but collapsible.

## HP and Mana

HP:

- red or deep crimson
- thin bar
- numeric label

Mana:

- blue or violet
- thin bar
- numeric label

Do not use chunky MMO styling.

## Frame States

### Scene

Default adventure frame.

### Sigil Reveal

The ring glows blue. The captain notices. Rain appears suspended or lit by the ring.

### Battle Start

Camera tightens. Spear, cloak, torchlight. More contrast.

### Victory

Gate opens. Light spills through. Captain steps aside.

### Death

Desaturated, rain-heavy, low camera. No gore spectacle.

### Mission Failure

Alarm bells, closed gate, guards above, hostile light.

## Image Prompt Rules

Every image prompt includes:

- global style
- current location
- major character continuity
- player continuity
- current frame type
- camera/framing
- mood
- forbidden elements

Every image prompt says:

- no text
- no UI
- no captions
- no logos
- no extra characters unless state allows them

## Continuity Anchors

Player:

- soaked dark cloak
- cracked blue sigil ring
- seen from behind or three-quarter view

Captain Oran:

- weary gate captain
- dented bronze armor
- short dark beard
- spear
- blue torchlight on armor

Location:

- sealed stone city gate
- heavy rain
- blue torches
- wet black road

