# Architecture

## Core Principle

State owns truth. AI performs the world.

## Recommended MVP Stack

Use one of these:

Option A:

- Vite
- React
- TypeScript
- Express server

Option B:

- Next.js App Router
- TypeScript
- route handlers for LLM/image calls

Vite + Express is simpler for a pure tech demo. Next.js is fine if deployment speed matters.

## System Layers

### 1. Client

Displays:

- frame image
- mission card
- HP/Mana
- inventory
- win/failure conditions
- narration
- input
- debug panel

Client does not decide mission truth.

### 2. Intent Parser

Input:

- player text
- current public state
- allowed action primitives

Output:

```ts
type ParsedIntent = {
  action: ActionType;
  target: string | null;
  secondaryTarget: string | null;
  item: string | null;
  spell: string | null;
  tone: "calm" | "urgent" | "hostile" | "deceptive" | "respectful" | "afraid" | "unknown";
  riskLevel: "low" | "medium" | "high";
  confidence: number;
  needsClarification: boolean;
  clarifyingQuestion: string | null;
};
```

### 3. State Reducer

Pure deterministic function:

```ts
resolveTurn(state, intent): TurnResolution
```

It decides:

- rule fired
- outcome type
- state delta
- allowed facts for narrator
- whether frame should update
- whether battle starts or ends
- whether mission is won/lost

### 4. Narrator

Receives:

- allowed facts
- outcome type
- current style
- current scene

Returns:

- short narration
- optionally one NPC line

Narrator may not introduce new facts.

### 5. Image Prompt Generator

Receives:

- frame type
- visual style packet
- current state
- allowed visual facts
- continuity anchors

Returns:

- prompt
- negative prompt
- continuity notes

The prompt can be sent to an image model or displayed as proof in MVP.

## Data Types

```ts
type ActionType =
  | "speak"
  | "ask"
  | "persuade"
  | "deceive"
  | "threaten"
  | "inspect"
  | "use_item"
  | "cast_spell"
  | "attack"
  | "defend"
  | "move"
  | "wait"
  | "surrender"
  | "unknown";

type MissionStatus = "active" | "won" | "lost";

type FrameType =
  | "chapter_card"
  | "scene"
  | "sigil_reveal"
  | "battle_start"
  | "victory"
  | "death"
  | "mission_failure";

type GameState = {
  chapterId: "gate_beneath_rain";
  sceneId: string;
  hp: number;
  mana: number;
  inventory: string[];
  battle: {
    active: boolean;
    enemyHp: number;
    enemyPosture: "guarded" | "aggressive" | "staggered" | "afraid" | "defeated";
  };
  flags: {
    alarmRaised: boolean;
    captainTrust: number;
    captainAlarm: number;
    sigilRevealed: boolean;
    gateUnlocked: boolean;
    learnedSealReason: boolean;
    captainAlive: boolean;
    letterShown: boolean;
  };
  mission: {
    status: MissionStatus;
    winConditions: {
      getPastGate: boolean;
      hpAboveZero: boolean;
      learnedSealReason: boolean;
      captainNotKilled: boolean;
    };
    failureConditions: {
      hpZero: boolean;
      alarmRaised: boolean;
      captainKilled: boolean;
      manaZeroBeforeSigil: boolean;
    };
  };
  visual: {
    frameType: FrameType;
    style: string;
    continuityAnchors: string[];
    lastImagePrompt: string;
  };
  turnCount: number;
};
```

## Turn Flow

```text
player input
  -> parse intent
  -> resolve deterministic state
  -> generate narrator allowed facts
  -> generate narration
  -> generate/update image prompt if major beat
  -> render next frame
```

## Image Generation Timing

Do not generate images every turn in MVP.

Generate or update frames on:

- chapter start
- scene transition
- sigil reveal
- battle start
- victory
- death
- mission failure

Text-only turns inside a scene are allowed.

