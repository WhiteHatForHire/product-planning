---
title: "V 4.1 prompts Replit"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Anchor V4/V 4.1 prompts Replit.docx"
status: reference
privacy: working
tags:
  - product
---

# V 4.1 prompts Replit

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Readme

# Anchor V4.1 Replit Prompts

12 prompts that take Anchor from V4 (the foundational refactor that adds experience_level, recovery_method, and the dynamic system prompt assembler) to V4.1 (Practice Mode — guided skill practice with branching scenarios, six modules, and the full UX surface).

## Read this first

V4.1 is BUILT ON V4. V4 must be deployed and stable before V4.1 build begins. V4.1 is non-functional without:

- stable_profile.recovery_focus, recovery_method, and experience_level populated

- buildChatSystemPrompt() deployed with cache invalidation working

- normalizeStableProfile() handling all V4 fields with safe defaults

If V4 isn’t shipped yet, ship V4 first using the v4_prompts directory. V4.1 is ~4-6 weeks of solo AI-directed work, mostly module authoring, not engineering.

The V4.1 spec is the source of truth. These prompts are the implementation plan, not the specification.

## How to use these prompts

Run them in order. Each prompt:

- Lists its dependencies on prior prompts.

- Has a Stack Context section explaining what already exists.

- Has Important Constraints (the “Do NOT” list) that prevent agent drift.

- Has a Pre-Flight inspection bullet list before any code is written.

- Has detailed implementation specs.

- Has unit tests.

- Has a Targeted Smoke Test verifying the prompt’s deliverables work end-to-end.

- Closes with an “At the End” report under a word limit, including the next step.

Copy the contents of one .txt file at a time into a Replit Agent (or Cursor / Claude Code) session. Watch the agent work. Read its end-of-prompt report carefully. If the report says “exact next step: V4.1 Prompt N”, proceed to that prompt.

If a prompt’s report flags an issue (test failure, voice quality concern, schema deviation), STOP. Read the issue. Either: revise the failing artifact yourself, or invoke the agent again with a focused fix prompt. Do not roll forward over flagged issues — V4.1’s correctness compounds across prompts.

## The 12 prompts

### Infrastructure (Prompts 1-7) — ~2-3 weeks

**Prompt 1: Practice surface variant + voice exemplars** (1-2 days)

Extends V4’s buildChatSystemPrompt with a ‘practice’ surface. Authors the voice exemplar markdown files (one per module, with samples per applicable focus). Voice exemplars are the prerequisite for every module — without them, voice eval is impossible and module authoring drifts.

**Prompt 2: Branch tree schema, loader, state machine** (1-2 days)

Defines the JSON schema for modules. Builds the validator, the loader (reads server/practice/modules/, validates each, caches in memory), and the deterministic state machine (advanceSession is a pure function — no DB, no AI, no side effects).

**Prompt 3: Database migrations** (1 day)

Creates practice_progress, practice_choices, practice_scenario_feedback tables. Adds new event_log types (practice_module_started/completed/paused/rated_immediate). Builds the practiceStore data access layer with sanitization, deletion (per-focus and full reset), and export. Wires the orchestration layer that connects state machine + persistence + event log.

**Prompt 4: Need-state entry + acute-distress detection + Library** (2 days)

Practice Quick Action on Home. Need-state screen with 6 options. Rule-based recommendation logic filtered by recovery_focus. Acute-distress detection at entry with stabilization step (static text, not AI). Library screen as secondary path.

**Prompt 5: Module session screen UI** (2 days)

Single-column conversational layout. Streaming token rendering. Choice rendering with static text (AI never rephrases). “Why am I seeing this?” affordance. “This doesn’t fit my situation” affordance with three actions. Pause/resume with version pinning. Mid-module crisis interrupt.

**Prompt 6: Synthesis + outcome + rating** (1-2 days)

Synthesis screen with three save options (save, edit-then-save, save-without-saving-the-summary). Outcome screen with three completion paths. Bridge-to-action: send_text, open_contacts, copy_message, save_for_later. Immediate post-module rating screen.

**Prompt 7: Contraindication checker + Settings + onboarding** (1 day)

Contraindication evaluation before module launch. Settings additions: Reset, Export, Reset-by-focus. Onboarding intro for new and existing users. V3.7-undetectable contraindications (driving, domestic_violence) are documented stubs.

### Modules (Prompts 8-11) — ~2-3 weeks

**Prompt 8: Module 1 — The 20-Minute Urge** (3-4 days, vertical proof)

Author for ALCOHOL focus FIRST. Walk through end-to-end. Revise. THEN expand to weed, nicotine, porn. This is the moment of truth: if the architecture works for one good module, it works for the rest.

**Prompt 9: Modules 2-3 bundled — Lapse vs Relapse + Ask for Help Without a Speech** (3-4 days)

Module 2 covers the abstinence violation effect, the shame spiral that turns a lapse into a relapse. Module 3 covers asking for help without a speech, with heavy bridge-to-action use (the AI generates short message options the user picks from).

**Prompt 10: Modules 4-5 bundled — Declining the Offer + What to Do After a Slip** (3-4 days)

Module 4 covers refusal of socially-pressured offers. Module 5 covers post-slip self-care and spiral interruption — the highest copy-sensitivity module in V4.1. Forbidden shame copy enforced in voice_constraints on every node.

**Prompt 11: Module 6 — Holding a No When Asked** (2 days)

Codependency proof of concept. Different shape from Module 4 (relational refusal, not offer refusal). Validates that the V4.1 format extends to relational recovery before V5+ commits to a full codependency track. Forbidden pathologizing copy enforced. DV hotline sentence required in Concept 1.

### Verification (Prompt 12) — ~1 day

**Prompt 12: Voice eval + full V4.1 smoke suite**

Voice eval matrix: 25 cases (~21 module-focus + 4 experience-level variations). Saved baseline outputs. Programmatic checks for forbidden phrases, phone numbers, recovery phase names, module-specific shame copy, module-specific pathologizing copy. Full smoke suite: 10 numbered suites covering surface assembly, state machine, persistence, entry path, session screen, synthesis/outcome, contraindications, settings/onboarding, V4 regression, voice consistency. Metrics scaffolding (no measurement yet — 90-day post-launch eval).

## Estimated total time

If everything goes well: ~4-5 weeks. Realistic estimate accounting for revisions, voice quality iteration, and integration debugging: 5-7 weeks. The success metric is frozen for the 90-day post-launch eval window, so resist the urge to ship a soft launch — V4.1 either ships clean or holds for fix.

## When to deviate

Each prompt is designed to be self-contained, but real implementation surfaces things specs don’t anticipate. When the agent flags an architectural pain point in its end-of-prompt report (e.g., “Module 5’s codependency case needs focus-conditional Practice 2”), evaluate whether to:

1. Adjust the schema and update later prompts.

1. Author around it (per-module workaround).

1. Defer to V5+.

Don’t let the prompts override your judgment. They’re a high-quality default, not a contract.

## Spec hierarchy

The spec is the source of truth. The prompts implement the spec. If the prompts and the spec conflict, the spec wins. Open Anchor_V4_1_Practice_Mode.docx and re-read sections 1-12 if any prompt feels off-spec.

## Pre-launch checklist

Before V4.1 ships:

- [ ] All 12 prompts completed.

- [ ] Voice eval baseline saved with zero forbidden phrase leaks across all 25 cases.

- [ ] Full smoke suite at 100% pass on programmatic cases, with manual review complete on cases flagged for human review.

- [ ] V4 regression: chat and check-in synthesis byte-identical to V4 baseline.

- [ ] Module 5 shame copy: zero leaks across baseline + 5 regenerations of hook/concept/synthesis.

- [ ] Module 6 pathologizing copy: zero leaks across baseline + 5 regenerations.

- [ ] Module 6 DV hotline sentence: 5/5 in concept 1 generations.

- [ ] Contraindication routing works for V3.7-detectable contraindications.

- [ ] Privacy posture verified: phone numbers never leak into practice surface output; user free-text never re-injected into next-node prompts; deletion controls work end-to-end.

If any item is yellow, hold for fix. V4.1 is for users in recovery — soft launches and partial corrections aren’t appropriate.

01

# V4.1 PROMPT 1: PRACTICE SURFACE VARIANT + VOICE EXEMPLAR SET

Extend V4’s buildChatSystemPrompt to support a ‘practice’ surface variant, and author the voice exemplar set that will be referenced by every V4.1 module. This is the prerequisite work before any branch tree authoring.

## STACK CONTEXT

V4 has shipped. buildChatSystemPrompt() lives in server/lib/buildChatSystemPrompt.ts with two surfaces (‘chat’, ‘checkin_synthesis’). The six-section assembly (identity, crisis, user context, time-aware framing, voice, forbidden content) is the canonical pattern.

V4.1 adds ‘practice’ as a third surface. The practice surface variant has the same six sections plus a seventh “Module context” section after voice. Practice is the surface used by every AI generation inside a module (hook, concept, practice nodes, repair loops, synthesis).

V4.1 also requires a voice exemplar set — short authored samples that show the desired voice for AI generation in each module. Exemplars are referenced by every module’s branch tree JSON via voice_exemplar_ref. Without exemplars, voice eval is impossible and module authoring drifts.

## IMPORTANT CONSTRAINTS

- Do NOT modify the ‘chat’ or ‘checkin_synthesis’ surface variants. They stay exactly as V4 shipped them.

- Do NOT add fields to BuildOptions beyond practice_context. The schema is locked.

- Do NOT include user free-text input from prior nodes in practice_context. Sanitized at capture, never re-injected.

- Do NOT include phone numbers, raw transcripts, or full chat history in the practice surface output.

- Do NOT bypass V4’s User Context block. The first-attempt vs chronic-relapse voice differences must apply automatically because they live in V4’s User Context.

- Do NOT build the state machine, branch tree loader, or module session screen yet. Those come in later prompts.

- Do NOT author actual modules yet. Voice exemplars only.

- Do NOT use clinical labels, recovery phase names, or coaching cadence in the exemplars.

## PRE-FLIGHT

Before writing code, inspect and confirm in 8 bullets:

1. Exact path of buildChatSystemPrompt.ts and the current BuildOptions type.

1. Exact structure of the existing six-section assembly (identity, crisis, user context, time-aware framing, voice, forbidden content).

1. Where surface-specific content currently lives (‘chat’ vs ‘checkin_synthesis’ branches in the assembler).

1. Where the assembled prompt’s “voice” section is sourced from for each surface.

1. Whether streaming is already supported in the LLM completion code path used by chat.ts (yes/no, and where).

1. Where new constants files have been placed in V4 (server/lib/ pattern).

1. Implementation plan: file structure for the practice surface, where exemplars live, how voice_exemplar_ref resolves at runtime.

1. Confirmation that the existing chat and checkin_synthesis tests still pass before any V4.1 changes.

## EXTEND BuildOptions

Update server/lib/buildChatSystemPrompt.ts:

```typescript

export type BuildSurface = 'chat' | 'checkin_synthesis' | 'practice';

export type ChoiceRef = {

node_id: string;

choice_id: string;

is_repair_route: boolean;

};

export type PracticeContext = {

module_id: string;

module_version: string;

node_id: string;

node_type: 'hook' | 'concept' | 'practice' | 'repair_loop' | 'synthesis' | 'outcome';

node_prompt_template: string;       // from branch tree JSON

node_voice_constraints: string;     // from branch tree JSON

user_focus_for_this_session: string;  // user-chosen at module start

prior_choices_in_session: ChoiceRef[];  // for synthesis nodes only

voice_exemplar_ref: string;         // from module JSON

};

export type BuildOptions = {

surface: BuildSurface;

checkin_context?: string;

practice_context?: PracticeContext;  // NEW in V4.1

drift_signal?: boolean;

trigger: BuildTrigger;

is_turn_zero?: boolean;

};

```

PracticeContext is the only new field. Adding it to BuildOptions is V4.1’s authorized schema extension. Adding any other field requires a separate explicit authorization.

## PRACTICE SURFACE OVERLAY

Add a new code path in buildChatSystemPrompt for surface === ‘practice’. The six existing sections behave as follows:

1. **Identity section**: Replace the chat-specific identity copy with practice-specific instructional persona text:

“You are generating dialogue inside a structured recovery practice module. You are not having a conversation; you are filling in the words for a specific node in a designed scenario. The user is not your conversation partner here; the branch tree is. Generate one node’s worth of text per request.”

1. **Crisis and safety rules**: UNCHANGED from V4. Use the same shared constants (server/lib/safetyRules.ts or wherever V4 placed them).

1. **User context**: UNCHANGED from V4. The full block (turn 0) for practice — practice generations always treat as turn-0 because each node is a fresh LLM call. So when practice_context is present, internal is_turn_zero defaults to true regardless of the BuildOptions value.

1. **Time-aware framing**: UNCHANGED from V4. Milestone awareness, drift signal, and other time signals carry through.

1. **Voice section**: V4 chat voice is the base layer (sponsor-adjacent, plain, grounded). Append practice-specific instructions after the chat voice copy:

“You may not ask the user questions back unless the branch tree authored questions explicitly. You may not invent skills, psychology, or recovery concepts. You may rephrase the prompt for this node within the constraints provided, but you may not change the choices the user will see — those are static and authored.”

1. **Forbidden content**: UNCHANGED from V4.

Then add the new seventh section:

1. **Module context** (NEW, only present when practice_context is supplied):

- Module ID and version (for traceability in logs).

- Node ID and node type.

- The prompt template verbatim. This is the instruction the LLM follows for this specific node.

- The voice constraints from the node (e.g., “max 4 sentences, second person, no questions back”).

- The voice exemplar referenced by voice_exemplar_ref, loaded inline as a “Voice exemplar:” block followed by the exemplar text.

- The user’s chosen focus for this session, resolved into the human-readable variable values needed by prompt_template.

- For synthesis nodes only: a list of which choices the user made earlier in the module (“In this session, the user chose: …” with non-shaming framing).

The module context section is concatenated after the voice section, joined with two newlines.

## FOCUS-TO-VARIABLE RESOLVER

Add a helper in server/lib/practiceFocusResolver.ts:

```typescript

export type FocusVariableMap = {

focus_substance_or_behavior_human: string;

focus_action_human: string;        // e.g., "drinking", "looking", "using"

focus_offer_phrase: string;        // e.g., "want a drink?", "want a hit?"

};

export function resolveFocusVariables(focus: string): FocusVariableMap;

```

Mappings (initial list, expandable):

```

alcohol → {

focus_substance_or_behavior_human: "a drink",

focus_action_human: "drinking",

focus_offer_phrase: "want a drink?"

}

weed → {

focus_substance_or_behavior_human: "a joint or a hit",

focus_action_human: "smoking",

focus_offer_phrase: "want a hit?"

}

nicotine → {

focus_substance_or_behavior_human: "a cigarette or a vape",

focus_action_human: "smoking",

focus_offer_phrase: "want one?"

}

porn → {

focus_substance_or_behavior_human: "a moment to look at something",

focus_action_human: "looking",

focus_offer_phrase: "(not applicable — porn is not 'offered' socially)"

}

codependency → {

focus_substance_or_behavior_human: "a request you don't want to say yes to",

focus_action_human: "saying yes when you mean no",

focus_offer_phrase: "(not applicable — codependency uses different scenarios)"

}

```

The resolver is invoked inside the practice surface assembly when expanding the prompt_template’s variables. Variable expansion is a simple string replace — no template engine.

If a focus is not in the resolver, throw a clear error. The system should never silently fall back to a wrong focus phrase.

## VOICE EXEMPLAR SET

Author voice exemplars for V4.1’s six modules. Each exemplar is a 200-400 word authored sample showing the desired voice across the focuses the module supports. Exemplars are stored as Markdown files in:

server/practice/voice_exemplars/

File structure:

```

server/practice/voice_exemplars/

├── urge_skills.md

├── communication_repair_offer.md       (for "Declining the Offer")

├── communication_repair_help.md        (for "Ask for Help Without a Speech")

├── foundations_lapse_vs_relapse.md

├── foundations_repair_after_slip.md

└── codependency_holding_no.md

```

Each file has this structure:

```markdown

# Voice Exemplar: [name]

## Used by modules

- [module_id]

## Voice notes

[2-3 sentences describing the voice — what it does and what it doesn't do]

## Sample 1 — alcohol focus

[200-400 word sample]

## Sample 2 — weed focus

[200-400 word sample]

[etc. for each applicable focus]

```

### Authoring guidelines (apply to every exemplar):

- Plain, grounded, instructional. Warm without performing intimacy.

- No coaching cadence (“Let’s break this down!”). No therapy cadence (“How does that make you feel?”).

- No clinical labels.

- No recovery phase names spoken to the user.

- No “this time will be different” language for chronic_relapse-aware exemplars.

- No false certainty.

- Second person where natural; third person otherwise.

- Sentences vary in length. Not all short. Not all long.

- The voice teaches through scenario and consequence, not through reassurance.

### Required exemplars for V4.1

Author one exemplar per module ID. Each exemplar covers the focuses the module supports.

For Module 1 (The 20-Minute Urge): urge_skills.md, with samples for alcohol, weed, nicotine, porn.

For Module 2 (Lapse vs Relapse): foundations_lapse_vs_relapse.md, with samples for alcohol, weed, codependency (since it applies to all focuses).

For Module 3 (Ask for Help Without a Speech): communication_repair_help.md, with samples for alcohol, codependency.

For Module 4 (Declining the Offer): communication_repair_offer.md, with samples for alcohol, weed, nicotine.

For Module 5 (What to Do After a Slip): foundations_repair_after_slip.md, with samples for alcohol, porn, codependency.

For Module 6 (Holding a No When Asked): codependency_holding_no.md, with samples for codependency only.

The samples need to be genuinely good. They’re the voice reference the LLM will be conditioned on for every node in every module. If the samples are weak, every module will be weak.

This authoring is judgment work. The agent should produce a first draft, then iterate. Acceptable to produce shorter samples on first pass and explicitly flag them as “draft, needs voice review” — this is more honest than producing 6 weak full-length exemplars.

## EXEMPLAR LOADER

Add a helper that loads exemplars by ref:

```typescript

// server/lib/voiceExemplarLoader.ts

export function loadVoiceExemplar(

exemplar_ref: string,

focus: string

): string;

```

The function reads the markdown file, finds the section for the requested focus, and returns the sample text. Returns the first sample if focus-specific is unavailable. Throws clear error if the exemplar file doesn’t exist.

The loader is invoked inside the practice surface assembly to populate the “Voice exemplar:” block.

## TESTS

Add unit tests for:

1. surface=‘practice’ with valid practice_context produces a 7-section prompt (existing 6 + module context).

1. surface=‘practice’ without practice_context throws clear error.

1. The ‘chat’ surface remains byte-identical to V4 output for the same memory + options.

1. The ‘checkin_synthesis’ surface remains byte-identical to V4 output.

1. Practice surface always uses full User Context block (treats as turn 0 internally regardless of BuildOptions.is_turn_zero).

1. resolveFocusVariables(‘alcohol’) returns the expected mapping.

1. resolveFocusVariables(‘codependency’) returns the expected mapping.

1. resolveFocusVariables(‘not_a_focus’) throws clear error.

1. loadVoiceExemplar(‘urge_skills’, ‘alcohol’) returns the alcohol sample.

1. loadVoiceExemplar(‘urge_skills’, ‘unsupported_focus’) returns the first sample (graceful fallback).

1. loadVoiceExemplar(‘does_not_exist’, ‘alcohol’) throws clear error.

1. Practice prompt for chronic_relapse user contains chronic_relapse experience-level framing (inherited from V4 User Context).

1. Practice prompt for first_attempt user contains first_attempt experience-level framing.

1. Practice prompt with phone numbers in stable_profile sober_contacts produces output with NO phone numbers.

1. The “module context” section appears after voice and before forbidden content sections (or wherever the spec places it relative to the existing six).

1. The synthesis node type triggers inclusion of prior_choices_in_session in the assembled prompt.

1. Non-synthesis node types do NOT include prior_choices_in_session even if supplied (sanitization).

## TARGETED SMOKE TEST

After implementation:

1. In a Node REPL, build a practice prompt for a fixture user (returning, day 47 alcohol, twelve_step):

```

buildChatSystemPrompt(memory, {

surface: 'practice',

trigger: 'request_initiated',

practice_context: {

module_id: 'urge_20_min',

module_version: '0.1.0',

node_id: 'hook',

node_type: 'hook',

node_prompt_template: 'Generate a brief 2-3 sentence scene where the user is alone after a hard day and notices the craving for {focus_substance_or_behavior_human}.',

node_voice_constraints: 'Max 3 sentences. Second person. No questions.',

user_focus_for_this_session: 'alcohol',

prior_choices_in_session: [],

voice_exemplar_ref: 'urge_skills',

}

});

```

1. Verify the assembled prompt_text contains: identity (instructional), crisis rules, user context (full block with chronic_relapse OR returning experience framing), time-aware framing (if any), voice section + practice voice overlay, forbidden content, and module context section with the prompt template, voice constraints, exemplar text, and resolved focus variable.

1. Verify NO phone numbers appear.

1. Verify the focus variable {focus_substance_or_behavior_human} is replaced with “a drink” in the module context section.

1. Run the same call with surface=‘chat’. Verify it produces the V4 chat prompt (no module context section, identity is conversational not instructional).

1. Run a synthesis-node practice call with three prior_choices_in_session entries. Verify they appear in the module context.

1. Run a hook-node practice call with three prior_choices_in_session entries. Verify they do NOT appear (sanitization).

1. Open one voice exemplar markdown file and read it end to end. Confirm the voice is plain/grounded, not coached/clinical.

## AT THE END

Report in under 300 words:

- Files created (paths) and modified.

- Confirmation that BuildOptions added only practice_context.

- Confirmation that ‘chat’ and ‘checkin_synthesis’ surfaces are byte-identical to V4.

- Number of voice exemplar files authored, with focus coverage per file.

- Honest self-assessment of the voice exemplars: are they ship-ready, or do they need a voice-review pass before module authoring begins?

- Number of unit tests added.

- Smoke test result.

- Any deviations from spec, with justification.

- Exact next step: V4.1 Prompt 2 (Branch tree schema, loader, state machine).

02

# V4.1 PROMPT 2: BRANCH TREE SCHEMA, LOADER, AND STATE MACHINE

Build the deterministic plumbing that loads module JSON files and walks them node-by-node. This prompt is pure backend infrastructure with comprehensive unit tests. No UI, no DB writes yet, no real modules.

## STACK CONTEXT

V4.1 Prompt 1 added the ‘practice’ surface variant to buildChatSystemPrompt and authored voice exemplars. This prompt builds the module loader and state machine that Practice will use to walk users through branch trees.

Modules are stored as JSON files in server/practice/modules/. Each module is one file. Versioned via semver (e.g., urge_20_min_v1_0_0.json). The schema is defined in V4.1 spec Section 5.

The state machine is deterministic — it takes (current_node, choice) and returns next_node, with no AI involvement. AI is only invoked at node-text generation time via buildChatSystemPrompt.

## IMPORTANT CONSTRAINTS

- Do NOT write any module JSON files yet. The schema and loader are tested with fixture JSON only.

- Do NOT add database writes. State persistence is V4.1 Prompt 3.

- Do NOT build UI. Module session screen is V4.1 Prompts 5-6.

- Do NOT use a JSON schema library if a simple validator can do the job. Plain TypeScript validation is fine and easier to debug.

- Do NOT use a state machine library (no XState). Plain switch/conditional logic.

- Do NOT bypass V4 by reading raw memory inside the state machine. Memory access goes through buildChatSystemPrompt only.

- Do NOT include user free-text input in node prompts. Per V4.1 invariant, free-text from prior nodes is sanitized at capture and never re-injected.

- Do NOT silently skip invalid modules. Loading errors are loud.

## PRE-FLIGHT

Confirm in 6 bullets:

1. Where the existing server-side TypeScript modules live (server/lib/, server/practice/, etc.).

1. Whether there is an existing JSON loading pattern in the codebase (synchronous reads at startup, async on demand, etc.).

1. Whether there are any existing TypeScript types for module-like data structures that this should align with.

1. The existing error handling and logging patterns (so loader errors integrate cleanly).

1. Implementation plan: file structure for the loader, state machine, validator, and fixture modules used in tests.

1. Whether semver parsing is needed (yes — module_version is semver) and whether a small helper or a library is appropriate.

## BRANCH TREE SCHEMA

Define TypeScript types in server/practice/types.ts:

```typescript

export type ModuleId = string;

export type NodeId = string;

export type ChoiceId = string;

export type Track = 'foundations' | 'urge_skills' | 'communication_repair' | 'cognitive' | 'codependency';

export type NodeType = 'hook' | 'concept' | 'practice' | 'repair_loop' | 'synthesis' | 'outcome';

export type ContraIndication =

| 'acute_intoxication'

| 'driving'

| 'severe_withdrawal'

| 'unsafe_contact'

| 'suicidal_ideation'

| 'domestic_violence'

| 'eating_disorder_active';

export type Choice = {

choice_id: ChoiceId;

choice_text: string;          // STATIC. AI may not rephrase.

choice_explanation: string;   // surfaced via "Why am I seeing this?"

next_node_id: NodeId;

is_repair_route: boolean;

};

export type OutcomeOptionType = 'commitment' | 'tiny_action' | 'save_only';

export type OutcomeOption = {

option_id: string;

option_label: string;

option_type: OutcomeOptionType;

bridge_action?: 'send_text' | 'open_contacts' | 'copy_message' | 'save_for_later';

};

export type Node = {

node_id: NodeId;

node_type: NodeType;

prompt_template: string;

voice_constraints: string;

choices?: Choice[];

next_node_id?: NodeId;

outcome_options?: OutcomeOption[];

};

export type Module = {

module_id: ModuleId;

module_version: string;       // semver

display_name: string;

estimated_minutes: { floor: 3; ceiling: 7 };

internal_track: Track;

applicable_focuses: string[];

applicable_methods: string[]; // empty array = all methods

contraindications: ContraIndication[];

voice_exemplar_ref: string;

nodes: Node[];

fallback_default_text: Record<NodeId, string>;

entry_node_id: NodeId;        // explicit entry point

};

```

## VALIDATOR

Add server/practice/moduleValidator.ts. The validator runs at load time and rejects malformed modules with clear, specific errors. Required checks:

1. All required Module fields present and correctly typed.

1. module_version is valid semver.

1. internal_track is one of the allowed values.

1. applicable_focuses is non-empty array of strings.

1. contraindications is array (empty OK), each entry is one of the allowed enum values.

1. voice_exemplar_ref points to a file that exists in server/practice/voice_exemplars/.

1. nodes is non-empty array.

1. entry_node_id matches a node in nodes.

1. Every node has node_id, node_type, prompt_template, voice_constraints.

1. Every choice within practice nodes has 2-4 entries (not 1, not 5+).

1. Every choice’s next_node_id matches a node in nodes (no dangling refs).

1. Every node’s next_node_id (when present) matches a node in nodes.

1. Every is_repair_route=true choice points to a node with node_type=‘repair_loop’.

1. fallback_default_text has an entry for every node_id in the module.

1. Outcome nodes have outcome_options of length 3 (one of each option_type: commitment, tiny_action, save_only).

1. Modules contain exactly one outcome node and at least one synthesis node.

1. NO node has BOTH choices and next_node_id (these are mutually exclusive).

1. No cycles in the graph that don’t go through a repair_loop or back to a non-repair forward path. (Repair loops are allowed to route back; arbitrary cycles are not.)

Return a structured ValidationResult with success flag and detailed errors. Do not throw — let the loader handle.

## LOADER

Add server/practice/moduleLoader.ts:

```typescript

export type LoadModulesOptions = {

modulesDir?: string;          // default: server/practice/modules/

};

export type LoadedModule = {

module: Module;

source_path: string;

};

export function loadAllModules(opts?: LoadModulesOptions): LoadedModule[];

export function loadModule(module_id: string, version?: string): LoadedModule | null;

```

Behavior:

- loadAllModules reads every .json file in the modules directory at server startup, validates each, and returns valid modules in an array. Invalid modules are logged with clear errors but do NOT crash startup. Aggregated startup log: “Practice: loaded N modules, M invalid (see errors above).”

- loadModule returns the latest version of a module by module_id (semver-sorted) unless a specific version is requested.

- Modules are cached in memory after first load. Hot-reload is NOT required for V4.1.

## STATE MACHINE

Add server/practice/stateMachine.ts:

```typescript

export type SessionState = {

module_id: string;

module_version: string;

current_node_id: NodeId;

prior_choices: ChoiceRef[];

session_focus: string;        // user-chosen at start, immutable mid-session

started_at: string;           // ISO timestamp

};

export type AdvanceInput =

| { kind: 'start'; module_id: string; user_focus: string }

| { kind: 'choose'; state: SessionState; choice_id: ChoiceId }

| { kind: 'advance'; state: SessionState }      // for non-choice nodes

| { kind: 'pause'; state: SessionState }

| { kind: 'resume'; state: SessionState };

export type AdvanceResult = {

next_state: SessionState;

next_node: Node;

is_module_complete: boolean;

};

export function advanceSession(input: AdvanceInput): AdvanceResult;

```

Behavior:

- ‘start’: loads module by module_id, validates user_focus is in applicable_focuses, returns initial state at entry_node_id.

- ‘choose’: validates choice_id exists in current node, advances to choice.next_node_id, appends ChoiceRef to prior_choices.

- ‘advance’: for non-practice/non-outcome nodes, follows next_node_id.

- ‘pause’: returns state unchanged but marks intent to persist (DB write happens in V4.1 Prompt 3 wiring).

- ‘resume’: returns state unchanged but verifies the module + version still exists (handles version pinning).

- is_module_complete is true when next_node.node_type === ‘outcome’ AND outcome has been chosen (handled in advance flow).

The state machine is pure: same input → same output. No DB, no AI, no side effects.

### Version pinning

When a session is started on module v1.0.0 and v1.1.0 ships mid-session, the resume must work on v1.0.0 still. The loader returns specific versions on request. The state machine’s resume operation calls loadModule(state.module_id, state.module_version) — if that exact version is no longer available, return a clear error. (This case won’t happen in V4.1 since modules don’t get deleted, but it’s the correct behavior for future-proofing.)

## FIXTURE MODULE FOR TESTING

Create server/practice/fixtures/test_module_v1_0_0.json — a small, complete, validates-clean module used for state machine tests. Single focus (alcohol), 5 nodes (hook → concept → practice → synthesis → outcome), 1 repair loop. About 50-100 lines of JSON.

This fixture is for tests only. Real modules come in V4.1 Prompts 8-11.

## TESTS

Add unit tests for:

1. Validator: valid fixture module passes, returns success=true.

1. Validator: missing required field → success=false with specific error.

1. Validator: invalid semver → fail.

1. Validator: dangling next_node_id ref → fail.

1. Validator: repair_loop choice pointing to non-repair_loop node → fail.

1. Validator: outcome node missing one of the three option types → fail.

1. Validator: missing fallback text for a node → fail.

1. Validator: cycle without repair loop → fail.

1. Validator: voice_exemplar_ref pointing to nonexistent file → fail (mock the FS check in tests).

1. Loader: directory with two valid + one invalid → loads two, logs the third’s error, returns success.

1. Loader: empty directory → returns empty array (not an error).

1. Loader: latest-version selection picks v1.2.0 over v1.0.0 of same module_id.

1. Loader: specific version request returns that version.

1. State machine ‘start’: returns initial state at entry_node_id.

1. State machine ‘start’ with focus not in applicable_focuses → error.

1. State machine ‘choose’ with valid choice → advances to choice.next_node_id, appends prior_choice.

1. State machine ‘choose’ with invalid choice_id → error.

1. State machine ‘advance’ on non-choice node follows next_node_id.

1. State machine ‘pause’ returns state unchanged.

1. State machine ‘resume’ on valid version returns state.

1. State machine ‘resume’ on missing version returns error.

1. State machine reaching outcome node sets is_module_complete=true after outcome choice.

1. State machine: walking the entire fixture module from start to outcome produces the expected node sequence.

1. Repair loop path: choose a repair-routed choice, follow back to a forward node, complete normally.

## TARGETED SMOKE TEST

After implementation:

1. Run npm test (or equivalent). All unit tests pass.

1. In a Node REPL, call loadAllModules(). It loads zero real modules (none exist yet) plus the fixture in tests dir.

1. Walk the fixture module step by step:

- Start: advanceSession({kind:‘start’, module_id:‘test_module’, user_focus:‘alcohol’})

- Verify next_node.node_type === ‘hook’

- Advance through concept, into practice, choose first choice

- Verify state contains the prior choice

- Continue through synthesis to outcome

- Verify is_module_complete logic at end

1. Try invalid choice_id: confirm error.

1. Verify all validator errors produce useful messages (not “validation failed” — actual specific complaints).

1. Restart server. Confirm clean startup with no crashes despite real modules dir being empty.

## AT THE END

Report in under 300 words:

- Files created (paths).

- Confirmation that no real modules exist yet (only fixture for tests).

- Number of unit tests added (target: 24+).

- Test pass/fail summary.

- Smoke test result.

- Any concerns about the validator’s strictness (too lenient? too strict?).

- Confirmation that no DB writes were added.

- Confirmation that no UI was built.

- Exact next step: V4.1 Prompt 3 (Database migrations).

03

# V4.1 PROMPT 3: DATABASE MIGRATIONS

Add the three new Postgres tables Practice needs (practice_progress, practice_choices, practice_scenario_feedback) and add the new event_log types. Wire the state machine’s pause/resume into the new tables. No UI, no module content.

## STACK CONTEXT

V4.1 Prompts 1 and 2 built the practice surface variant and the in-memory state machine. This prompt adds DB persistence so paused sessions survive across app restarts and so usage data is captured for the eventual rating, deletion, and export flows.

V4 only modified user_memory.stable_profile JSON and added one column (app_settings.v4_modal_skipped_count). V4.1 Prompt 3 is the first V4.1 prompt with real Postgres migrations.

## IMPORTANT CONSTRAINTS

- Do NOT modify user_memory schema. stable_profile is locked.

- Do NOT modify check_ins, commitments, app_settings beyond what’s specified.

- Do NOT introduce a new ORM or migration tool. Use whatever the project already uses.

- Do NOT store user free-text from prior nodes. Sanitized at capture.

- Do NOT store synthesis text by default. Only when the user explicitly opts in to save it.

- Do NOT denormalize. Keep practice_progress, practice_choices, practice_scenario_feedback as separate tables.

- Do NOT add foreign key constraints to user_memory.user_id (project may use varchar ‘dev_user’ / ‘maxwell’ as user_id, not a real FK).

- Do NOT log user-identifying info inside event_log summaries.

- Do NOT modify the existing event_log shape (type, summary, timestamp). Just add new type values.

## PRE-FLIGHT

Confirm in 7 bullets:

1. The migration tool used in this project (e.g., raw SQL files, drizzle, prisma, knex, custom) and the conventional location of migration files.

1. The current schema of user_memory.event_log (jsonb array, capped at 90 entries, with three keys: type/summary/timestamp).

1. The user_id column convention (varchar(100), default values like ‘dev_user’ or ‘maxwell’).

1. The existing pattern for sensitive-data handling (any encryption at rest? row-level access control?).

1. The shape of timestamp columns elsewhere in the schema (timestamptz vs timestamp without timezone).

1. How session_id will be referenced — by integer FK to practice_progress.id, or by uuid?

1. Implementation plan: migration file naming, the order of CREATE statements, the helper functions added.

## MIGRATION

Create a new migration file (matching existing pattern). The migration must:

### Create practice_progress table

```sql

CREATE TABLE practice_progress (

id              SERIAL PRIMARY KEY,

user_id         VARCHAR(100) NOT NULL,

module_id       VARCHAR(100) NOT NULL,

module_version  VARCHAR(20)  NOT NULL,

started_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),

completed_at    TIMESTAMPTZ  NULL,

current_node_id VARCHAR(100) NULL,

synthesis_text  TEXT         NULL,

session_focus   VARCHAR(50)  NOT NULL,

outcome_path    VARCHAR(20)  NULL,        -- 'commitment' | 'tiny_action' | 'save_only' | NULL

paused_at       TIMESTAMPTZ  NULL,

CONSTRAINT practice_progress_uniq_session UNIQUE (user_id, module_id, started_at)

);

CREATE INDEX idx_practice_progress_user ON practice_progress(user_id);

CREATE INDEX idx_practice_progress_user_completed ON practice_progress(user_id, completed_at);

```

Notes on fields:

- synthesis_text is NULL by default. Populated only if user explicitly saves the AI-generated synthesis paragraph.

- current_node_id is NULL when completed; reflects pause state when non-NULL and completed_at is NULL.

- outcome_path is set when the user finishes the module (one of three values) or NULL if completed without choosing outcome (edge case — should be rare).

- paused_at is non-NULL when the session is paused; cleared on resume or completion.

### Create practice_choices table

```sql

CREATE TABLE practice_choices (

id          SERIAL PRIMARY KEY,

user_id     VARCHAR(100) NOT NULL,

session_id  INTEGER      NOT NULL REFERENCES practice_progress(id) ON DELETE CASCADE,

node_id     VARCHAR(100) NOT NULL,

choice_id   VARCHAR(100) NOT NULL,

is_repair_route BOOLEAN  NOT NULL,

timestamp   TIMESTAMPTZ  NOT NULL DEFAULT NOW()

);

CREATE INDEX idx_practice_choices_session ON practice_choices(session_id);

CREATE INDEX idx_practice_choices_user ON practice_choices(user_id);

```

### Create practice_scenario_feedback table

```sql

CREATE TABLE practice_scenario_feedback (

id          SERIAL PRIMARY KEY,

user_id     VARCHAR(100) NOT NULL,

session_id  INTEGER      NOT NULL REFERENCES practice_progress(id) ON DELETE CASCADE,

node_id     VARCHAR(100) NOT NULL,

action      VARCHAR(20)  NOT NULL,    -- 'regenerate' | 'tell_us_why' | 'skip'

user_text   TEXT         NULL,        -- only populated for 'tell_us_why', sanitized

timestamp   TIMESTAMPTZ  NOT NULL DEFAULT NOW()

);

CREATE INDEX idx_practice_feedback_session ON practice_scenario_feedback(session_id);

```

The migration is idempotent: include IF NOT EXISTS where appropriate so re-running does not fail.

The migration must roll back cleanly. Provide the down migration: DROP INDEX, DROP TABLE in reverse order.

## DATA ACCESS HELPERS

Add server/practice/practiceStore.ts with typed helpers. All functions are async.

```typescript

// Session lifecycle

export async function startSession(params: {

user_id: string;

module_id: string;

module_version: string;

session_focus: string;

entry_node_id: string;

}): Promise<{ session_id: number; started_at: string }>;

export async function getSession(session_id: number): Promise<PracticeSession | null>;

export async function getActiveSessions(user_id: string): Promise<PracticeSession[]>;

export async function getPausedSessions(user_id: string): Promise<PracticeSession[]>;

export async function getCompletedSessions(user_id: string, limit?: number): Promise<PracticeSession[]>;

export async function pauseSession(session_id: number, current_node_id: string): Promise<void>;

export async function resumeSession(session_id: number): Promise<PracticeSession | null>;

export async function updateCurrentNode(session_id: number, node_id: string): Promise<void>;

export async function completeSession(params: {

session_id: number;

outcome_path: 'commitment' | 'tiny_action' | 'save_only';

synthesis_text?: string;        // only saved if user opted in

}): Promise<void>;

// Choices

export async function recordChoice(params: {

session_id: number;

user_id: string;

node_id: string;

choice_id: string;

is_repair_route: boolean;

}): Promise<void>;

export async function getChoicesForSession(session_id: number): Promise<ChoiceRecord[]>;

// Feedback

export async function recordScenarioFeedback(params: {

session_id: number;

user_id: string;

node_id: string;

action: 'regenerate' | 'tell_us_why' | 'skip';

user_text?: string;             // sanitized before passing in

}): Promise<void>;

// Privacy controls

export async function deleteAllPracticeData(user_id: string): Promise<{ rows_deleted: number }>;

export async function deletePracticeDataForFocus(user_id: string, focus: string): Promise<{ rows_deleted: number }>;

export async function exportPracticeData(user_id: string): Promise<PracticeExport>;

```

### Sanitization

The recordScenarioFeedback helper accepts optional user_text. Before storing, the helper runs the existing redaction helpers (phone numbers stripped, raw notes minimized — same redaction used by buildMemoryContext). If after sanitization user_text is empty, store NULL.

The recordScenarioFeedback function never logs user_text to server logs — only the action.

## EVENT_LOG ADDITIONS

Add four new event_log types (preserving existing three-key shape):

- ‘practice_module_started’ — summary: “{module_id} started” (note: this is logged, not just session table). Useful for cross-source aggregation.

- ‘practice_module_completed’ — summary: “{module_id} completed (outcome: {outcome_path})”

- ‘practice_module_rated_immediate’ — summary: “{module_id} rated: {useful|not_really|not_sure}”

- ‘practice_module_paused’ — summary: “{module_id} paused at {node_id}” (logged once per pause, deduplicated within 5 minutes to avoid spam)

These propagate via the existing event_log push mechanism (90-entry rolling window). NO raw user text. NO node prompts. Just module/outcome/rating identifiers.

Add a helper in server/practice/practiceEventLog.ts to wrap the existing event_log helpers. It should expose:

```typescript

export async function logPracticeStarted(user_id: string, module_id: string): Promise<void>;

export async function logPracticeCompleted(user_id: string, module_id: string, outcome_path: string): Promise<void>;

export async function logPracticeRated(user_id: string, module_id: string, rating: 'useful' | 'not_really' | 'not_sure'): Promise<void>;

export async function logPracticePaused(user_id: string, module_id: string, node_id: string): Promise<void>;

```

Each wraps the existing event_log push helper. Each enforces the dedup-within-5min rule for pause events.

## WIRE STATE MACHINE TO PRACTICE STORE

V4.1 Prompt 2 built advanceSession() as a pure function with no DB. This prompt adds an orchestration layer that wraps it:

```typescript

// server/practice/sessionOrchestrator.ts

export async function startNewSession(user_id: string, module_id: string, user_focus: string): Promise<{

session_id: number;

state: SessionState;

current_node: Node;

}>;

export async function chooseOption(user_id: string, session_id: number, choice_id: string): Promise<{

state: SessionState;

next_node: Node;

is_module_complete: boolean;

}>;

export async function pauseSessionAtNode(user_id: string, session_id: number, current_node_id: string): Promise<void>;

export async function resumeExistingSession(user_id: string, session_id: number): Promise<{

state: SessionState;

current_node: Node;

}>;

export async function completeSessionWithOutcome(user_id: string, session_id: number, outcome_path: 'commitment' | 'tiny_action' | 'save_only', synthesis_text?: string): Promise<void>;

```

The orchestrator:

- Calls advanceSession() (pure state machine)

- Calls practiceStore methods (DB persistence)

- Calls practiceEventLog methods (event log additions)

Order matters: state machine first, then persistence, then event log. If persistence fails, throw and don’t log to event_log (avoid lying about completion).

## TESTS

Add tests:

1. Migration up creates all three tables with expected columns.

1. Migration up is idempotent (can run twice).

1. Migration down drops all three tables.

1. startSession inserts a row with correct fields.

1. recordChoice inserts a row linked to the session.

1. recordScenarioFeedback with user_text containing phone numbers stores sanitized version.

1. recordScenarioFeedback with user_text empty after sanitization stores NULL.

1. completeSession updates the row with completed_at and outcome_path.

1. completeSession with synthesis_text=’’ stores NULL synthesis_text (opt-in only).

1. completeSession with synthesis_text=‘valid text’ stores the text.

1. pauseSession sets paused_at and current_node_id.

1. resumeSession returns the paused state.

1. deleteAllPracticeData removes practice_progress rows; cascade deletes choices and feedback.

1. deletePracticeDataForFocus removes only sessions with matching session_focus.

1. exportPracticeData returns structured export with all user’s practice rows.

1. logPracticePaused dedups within 5 minutes (second call within 5min is a no-op).

1. logPracticeStarted/Completed/Rated push to event_log in correct shape (type/summary/timestamp).

1. Orchestrator startNewSession creates session row, logs event, returns initial state.

1. Orchestrator chooseOption advances state, records choice, returns next node.

1. Orchestrator chooseOption with invalid choice_id throws and writes nothing.

1. Orchestrator pauseSessionAtNode persists pause and logs event.

1. Orchestrator completeSessionWithOutcome updates row, logs event, returns successfully.

1. Orchestrator completeSessionWithOutcome with persistence failure does NOT log to event_log.

## TARGETED SMOKE TEST

After implementation:

1. Run migration up against dev DB. Verify all three tables exist (e.g., \d in psql).

1. Run migration down. Verify tables removed.

1. Run migration up again. Verify clean.

1. Insert a fixture user_id (‘dev_user’).

1. Use orchestrator: startNewSession(‘dev_user’, ‘test_module’, ‘alcohol’). Verify session row created. Verify event_log has ‘practice_module_started’ entry.

1. chooseOption with a valid choice_id. Verify practice_choices row created.

1. pauseSessionAtNode. Verify paused_at column set. Verify event_log has ‘practice_module_paused’.

1. resumeExistingSession. Verify state returned matches.

1. completeSessionWithOutcome with outcome_path=‘commitment’ and synthesis_text=’’. Verify row updated, synthesis_text remains NULL.

1. Run another session, complete with synthesis_text=‘real text’. Verify text persists.

1. Call recordScenarioFeedback with user_text=‘Call me at 555-123-4567’. Verify stored user_text has phone redacted.

1. Call deleteAllPracticeData(‘dev_user’). Verify all rows gone, all event_log entries remain (event_log not modified by this).

1. Verify event_log push handles 90-entry cap correctly when adding multiple practice events.

## AT THE END

Report in under 300 words:

- Migration file paths.

- Tables created with column counts.

- Helper file paths.

- Number of unit tests.

- Test pass/fail summary.

- Smoke test results.

- Confirmation that user_memory and stable_profile schemas are untouched.

- Confirmation that event_log uses the existing three-key shape with new types.

- Confirmation that synthesis_text is opt-in.

- Any deviations from spec.

- Exact next step: V4.1 Prompt 4 (Need-state entry, acute-distress detection, Library screen).

04

# V4.1 PROMPT 4: NEED-STATE ENTRY, ACUTE-DISTRESS DETECTION, LIBRARY SCREEN

Build the Practice Quick Action on Home, the need-state screen that maps to recommended modules, the acute-distress detection at entry, and the Library screen as a secondary path. No module session UI yet (that’s V4.1 Prompts 5-6).

## STACK CONTEXT

V4.1 Prompts 1-3 built the practice surface, the state machine, and the database layer. This prompt is the user-facing entry path: Home → Practice Quick Action → need-state screen → recommended module(s).

Modules don’t exist yet (Prompts 8-11 will author them). For this prompt, all module-list rendering uses fixture metadata. The recommendation logic runs against the fixture metadata so the wiring is real even though no full modules play.

## IMPORTANT CONSTRAINTS

- Do NOT build the module session screen. That’s V4.1 Prompt 5.

- Do NOT build the synthesis or outcome screens. That’s V4.1 Prompt 6.

- Do NOT route based on AI inference. Need-state → module recommendation is rule-based.

- Do NOT show streaks, XP, leaderboards, or progress percentages.

- Do NOT auto-launch any module. User taps to start.

- Do NOT show modules that don’t apply to the user’s recovery_focus list.

- Do NOT bypass crisis routing. If V3.7’s existing classifier flags risk during need-state navigation, normal crisis flow takes over.

- Do NOT make the acute-distress stabilization step AI-generated. Static text from constants.

## PRE-FLIGHT

Confirm in 7 bullets:

1. Where Home lives (likely client/src/home/) and the existing Quick Actions pattern.

1. The existing routing/navigation pattern (React Router, Expo Router, etc.) and screen-to-screen transitions.

1. Where V3.7’s risk classifier signal lives (event_log entries? a state field? a recent check-in flag?). The acute-distress detection at entry needs to read it.

1. The existing modal/screen pattern and visual style.

1. Where recovery_focus is read in the client (presumably from a UserMemory hook/context).

1. The existing pattern for launching new screens (modal vs route).

1. Implementation plan: new components, routes, fixture data.

## PRACTICE QUICK ACTION ON HOME

Add a Practice card/button to the Home Quick Actions area, alongside existing actions (Check-In, Chat, etc.). The card has:

- Title: “Practice”

- Subtext: “Rehearse a moment before it happens”

- Tap → opens the need-state screen as a route or modal (match existing pattern)

The card is always visible. No conditional rendering based on time of day or last activity.

## ACUTE-DISTRESS DETECTION AT ENTRY

When the Practice card is tapped, before showing the need-state screen, check whether the user is currently in acute distress. The check uses signals already available in V3.7:

- Most recent check-in flagged as elevated risk by the existing risk classifier.

- A chat session active right now where the last 3 user messages contain risk language (re-use V3.7 risk detection).

- An event_log entry with kind=‘risk_classification’ marked ‘high’ or ‘crisis’ within the last 30 minutes.

If ANY of these signals are present, show the stabilization step before the need-state screen.

### Stabilization step

A one-screen modal:

- Title: “Let’s slow down for a minute first.”

- Body: A static TIPP-style grounding prompt (NOT AI-generated). Suggested copy:

> “You’re safe right now. Let’s do a quick reset before practice.

>

> Find five things you can see. Take your time.

>

> Take three slow breaths. In through the nose. Out through the mouth.

>

> Put both feet on the floor. Notice the contact.

>

> When you’re ready, choose where to go next.”

- Three buttons (vertical stack):

- “I’m ready for practice” → continues to need-state screen.

- “I need to talk to someone” → opens Chat.

- “I need real help right now” → opens SOS Mode (per V5.0 spec; if V5.0 not yet shipped, opens existing crisis card / SOS placeholder).

The stabilization step is logged in event_log with kind=‘practice_stabilization_shown’ (new event type, additive). NO raw text, just the type and timestamp.

The stabilization step does NOT require completion to proceed. The user can tap “I’m ready for practice” immediately. The point is to insert a pause and visible options, not to gate.

### Fallback behavior

If the existing risk classifier or signal source is unavailable or errors out, the stabilization step is NOT shown (fail-open). Better to show the need-state screen than to show a stabilization step incorrectly. Log the error for monitoring.

## NEED-STATE SCREEN

The need-state screen is a single screen with six options laid out as tappable cards or buttons (mobile-first). Order:

1. “I’m having an urge.”

1. “I feel ashamed or stuck in my head.”

1. “I need to ask for help or repair something.”

1. “I have something coming up I’m worried about.”

1. “I already slipped and I’m scared.”

1. “I want to look around.” → opens Library screen (no recommendation).

Title above the options: “What’s happening right now?”

Subtext: “We’ll match you with a quick practice.”

Each tap opens a confirmation/preview screen showing 1-3 recommended modules. Why a preview before launching: gives user agency and an opt-out before committing to a 3-7 minute session.

### Need-state → module mapping

Rule-based, not AI. The mapping is:

```

'urge'             → ['urge_20_min']

'shame_stuck'      → ['lapse_vs_relapse']

'ask_help_repair'  → ['ask_for_help', 'declining_offer']  // user picks

'something_coming' → ['declining_offer', 'ask_for_help']  // user picks

'already_slipped'  → ['after_slip']

'browse'           → null (route to Library)

```

Plus filtering by user’s recovery_focus:

- If a recommended module’s applicable_focuses doesn’t intersect user’s recovery_focus, exclude it.

- For codependency-only users, the mapping uses [‘holding_no’] for ‘ask_help_repair’, ‘something_coming’, and ‘shame_stuck’ (since urge_skills don’t apply). ‘urge’ need-state is hidden or replaced with a “this isn’t typically how codependency shows up — try one of these instead” message.

- For users with multiple focuses (alcohol + codependency), show the union.

Implement this via a function:

```typescript

// server/practice/needStateRecommender.ts

export function recommendForNeedState(

need_state: NeedState,

recovery_focus: string[]

): RecommendedModule[];

```

Where RecommendedModule is { module_id, display_name, estimated_minutes, one_line_purpose }.

The recommender returns at most 3 modules. If empty (no modules apply for this user’s focus), the screen shows: “No matches for that need state right now. Try Browse to see all modules, or open Chat instead.”

### Module preview / confirmation card

When user taps a need-state, show 1-3 cards. Each card:

- Module display_name

- One-sentence purpose

- Estimated time (“3-7 min”)

- Single button: “Start practice” → launches module (route to module session screen, V4.1 Prompt 5 to be implemented)

Tap-anywhere-to-start is fine; an explicit button is required for accessibility.

If only one module recommended, you can still show it as a card. Don’t auto-launch.

## LIBRARY SCREEN

The Library screen is a secondary path accessible via “I want to look around” or via a small Library link in Settings.

Layout:

- Section headers by need-state moment (“If you’re having an urge”, “If you need to ask for help”, etc.)

- Within each section, cards for each module that applies to the user’s recovery_focus.

- Each card shows: display_name, one-sentence purpose, estimated time, completion state (“Done” indicator if user has previously completed; nothing otherwise).

Completion state is read from practice_progress (most-recent completed_at IS NOT NULL session per module). It’s a quiet indicator, not a streak.

NO progress percentages across the catalog. NO streaks. NO XP. NO leaderboards. The Library is a list, not a game.

Modules with no applicable focus for the user are NOT shown in the Library. (A pure codependency user does not see urge_skills modules.)

A small footer text: “Anchor practice helps you rehearse moments before they happen. It’s not therapy or detox support.”

## FIXTURE DATA FOR THIS PROMPT

Since real modules don’t exist yet, use a fixture metadata file: server/practice/fixtures/v41_module_metadata.json

It contains module-shaped objects (display_name, applicable_focuses, applicable_methods, internal_track, estimated_minutes, one_line_purpose) for the six V4.1 modules. The fixture is replaced by real loadAllModules() output once Prompts 8-11 land. For now, the recommender and Library read from fixture.

The six fixture modules:

```

urge_20_min          | Urge Skills        | The 20-Minute Urge          | applicable: alcohol, weed, nicotine, porn

lapse_vs_relapse     | Foundations        | Lapse vs Relapse            | applicable: all

ask_for_help         | Communication/Repair| Ask for Help Without a Speech | applicable: all

declining_offer      | Communication/Repair| Declining the Offer        | applicable: alcohol, weed, nicotine

after_slip           | Foundations        | What to Do After a Slip    | applicable: all

holding_no           | Codependency       | Holding a No When Asked    | applicable: codependency

```

Document in code comments that this fixture will be replaced by loadAllModules() in V4.1 Prompt 7.

## TESTS

Add tests:

1. recommendForNeedState(‘urge’, [‘alcohol’]) returns [‘urge_20_min’].

1. recommendForNeedState(‘urge’, [‘codependency’]) returns [] (no urge module applies to codependency-only user).

1. recommendForNeedState(‘ask_help_repair’, [‘alcohol’]) returns 2 modules (ask_for_help, declining_offer).

1. recommendForNeedState(‘ask_help_repair’, [‘alcohol’, ‘codependency’]) returns 3 modules (union: ask_for_help, declining_offer, holding_no — verify ordering and dedup).

1. recommendForNeedState(‘something_coming’, [‘nicotine’]) filters correctly.

1. recommendForNeedState(‘already_slipped’, any focus) returns [‘after_slip’].

1. recommendForNeedState(‘browse’, any focus) returns null.

1. Acute-distress detection: when most recent check-in flagged risk, returns true.

1. Acute-distress detection: when none of three signals present, returns false.

1. Acute-distress detection: when classifier service errors out, returns false (fail-open) and logs error.

1. Library screen renders only modules whose applicable_focuses intersect user’s recovery_focus.

1. Library screen renders completion state correctly when practice_progress has completed sessions.

1. Stabilization step modal renders three buttons: ready / chat / SOS.

1. Tapping “I’m ready for practice” closes modal and routes to need-state screen.

## TARGETED SMOKE TEST

After implementation:

1. Open Home. Verify Practice Quick Action card visible.

1. Tap Practice. Verify need-state screen opens with 6 options.

1. Tap “I’m having an urge.” Verify preview card shows “The 20-Minute Urge” (the Start button doesn’t navigate yet — that’s V4.1 Prompt 5; the route is a placeholder).

1. Verify the recommender filtering works: switch user’s recovery_focus to codependency only. Re-open. Verify “I’m having an urge” shows “no matches” message.

1. Switch user back to alcohol + codependency. Re-open. Verify “I need to ask for help or repair something” shows three modules.

1. Verify Library screen renders with only applicable modules.

1. Manually inject a risk_classification ‘high’ event into event_log within the last 30 min. Open Practice card. Verify stabilization step appears with three buttons. Tap “I’m ready for practice” — need-state screen opens.

1. Tap stabilization “I need real help right now” — verify SOS placeholder opens (or current crisis card).

1. Disable the risk classifier (simulate error). Open Practice card. Verify stabilization step does NOT show; need-state screen opens directly.

1. Verify event_log gains ‘practice_stabilization_shown’ entry when stabilization shown.

## AT THE END

Report in under 300 words:

- New screens/components built (paths).

- Need-state mapping table actually shipped (verify it matches spec exactly).

- Acute-distress detection signal sources (which event_log fields and recent check-in flag the implementation reads).

- Confirmation that fail-open behavior is in place for classifier errors.

- Test pass/fail summary.

- Smoke test results.

- Any UI deviations (visual style adjustments to match existing patterns are OK; report them).

- Confirmation that no module session screen was built.

- Confirmation that fixture metadata is in place to be replaced when modules exist.

- Exact next step: V4.1 Prompt 5 (Module session screen).

05

# V4.1 PROMPT 5: MODULE SESSION SCREEN UI

Build the in-module UX: the screen the user sees while walking through hook → concept → practice nodes → repair loops. Streaming token rendering, choice rendering, “this doesn’t fit me” affordance, pause/resume, “Why am I seeing this choice?” affordance. Synthesis and outcome screens are V4.1 Prompt 6.

## STACK CONTEXT

V4.1 Prompts 1-4 built the practice surface, state machine, persistence, and the entry path. This prompt is the screen the user sees during a module. It calls the orchestrator from V4.1 Prompt 3 to advance state, and it calls buildChatSystemPrompt → LLM completion to render each node’s text.

Real modules don’t exist yet (Prompts 8-11). This prompt uses the fixture module from V4.1 Prompt 2 (test_module_v1_0_0.json) so the screen is end-to-end testable with real backend.

## IMPORTANT CONSTRAINTS

- Do NOT build synthesis or outcome screens. That’s V4.1 Prompt 6.

- Do NOT add fanfare animations, confetti, or progress bars. Quiet UI.

- Do NOT auto-advance non-practice nodes. Tap-to-continue on hook, concept, repair_loop.

- Do NOT skip the streaming token rendering. The user sees the AI text appear as it arrives, like in chat.

- Do NOT allow the AI to invent choice options. Choices come from the JSON, rendered statically.

- Do NOT pass user free-text from prior nodes into the next node’s prompt context.

- Do NOT render module text outside the buildChatSystemPrompt → LLM flow. There is no “client-side templating” of node text.

- Do NOT show streaks, completion percentages, or gamification elements during a session.

- Do NOT bypass crisis detection — if mid-module risk signal fires, the module pauses and crisis flow takes over.

## PRE-FLIGHT

Confirm in 7 bullets:

1. The existing chat streaming pattern (SSE? WebSocket? polling? OpenAI streaming SDK?). The module session screen will use the same.

1. The existing pattern for capturing taps and navigating between screens.

1. Where to add the route/screen — likely client/src/practice/ as a new directory.

1. The existing component library / styling approach (Tailwind classes? styled-components? shadcn/ui?).

1. Whether the orchestrator from V4.1 Prompt 3 can be called from a server endpoint, or if it’s exposed as a REST/RPC route.

1. The existing pattern for handling LLM errors (timeout, content filter, provider down) and showing fallbacks.

1. Implementation plan: route, components, state management for in-flight session, fallback behavior.

## THE MODULE SESSION SCREEN

Single-column conversational layout. Entered via route param: /practice/session/:session_id (or equivalent).

On mount:

- Fetch session state (orchestrator.resumeExistingSession or session_id from start).

- Determine current_node from state.

- For non-outcome nodes, render the node text via the streaming LLM call.

- For outcome nodes, navigate to the outcome screen (V4.1 Prompt 6).

### Layout, top to bottom

1. **Quiet header**: module display_name on the left, pause icon (or text “Pause”) on the right. No progress bar. No stage/phase label.

1. **Streaming text area**: the AI-generated node text, rendered as tokens arrive.

1. **For practice nodes**: 2-4 choice buttons, vertical stack, full-width.

1. **Below choices, only on practice nodes**: “Why am I seeing this choice?” inline expandable per choice.

1. **Below choices, on every scenario node** (hook, concept, practice, repair_loop): “This doesn’t fit my situation” — small text link.

1. **For non-practice nodes** (hook, concept, repair_loop): single Continue button after streaming completes.

1. **Footer text** (optional): “Pause and resume anytime.”

### Streaming behavior

For each visible node (hook, concept, practice, repair_loop, synthesis):

1. Call backend endpoint /api/practice/generate-node with { session_id, node_id }.

1. Backend invokes buildChatSystemPrompt with surface=‘practice’ and the appropriate practice_context.

1. Backend invokes the LLM with streaming.

1. Tokens stream to the client. Client renders progressively.

1. While streaming: choice buttons (if present) are disabled. Pause is enabled. “This doesn’t fit” is enabled.

1. Once streaming completes: enable choice buttons or Continue button.

Latency target: time-to-first-token under 1s. If TTFT exceeds 3s, show a subtle “thinking…” indicator.

### LLM fallback (must-ship)

If the streaming call fails (timeout, error, content filter):

- Load fallback_default_text[node_id] from the module’s JSON.

- Render the fallback text immediately (no streaming).

- Show a small banner: “Using offline practice text — personalization unavailable.”

- Continue normally with choices/continue button.

The fallback is per V4.1 spec Section 5 (fallback_default_text is part of every module). The fixture module’s fallback text is what’s used in this prompt’s smoke test.

### Choice rendering

Choices are rendered in the order defined in the JSON. The choice_text is rendered VERBATIM. The AI never rephrases choices.

When a choice is tapped:

1. Disable all choice buttons.

1. Call orchestrator.chooseOption(user_id, session_id, choice_id).

1. On success, navigate to the next node (re-render the screen with new current_node).

1. On error, re-enable buttons and show a non-shaming retry state.

### “Why am I seeing this choice?”

Each choice has a small icon or inline expandable showing choice_explanation from the JSON. Tap to expand inline. Doesn’t navigate away. Doesn’t disable other choices.

### “This doesn’t fit my situation” affordance

Quiet text link below the choices on every scenario node (hook, concept, practice, repair_loop). NOT shown on synthesis or outcome nodes.

Tap → opens a small modal with three options:

- “Try again” → invokes the same node generation again with a different LLM seed/temperature (call practice/generate-node with a force_regenerate flag; the backend re-runs buildChatSystemPrompt with a small prompt addendum or temperature bump). Logs scenario_feedback row with action=‘regenerate’.

- “Tell us why this doesn’t fit” → free-text input, max 200 chars. On submit: sanitize via existing redaction helpers, write to practice_scenario_feedback with action=‘tell_us_why’ and the sanitized user_text. Then re-generates the node (same as Try again).

- “Skip this node” → advances state machine forward as if the user picked the safest forward option (defined per module via a meta field skip_default_choice_id; if not defined, picks the first non-repair-route choice). Logs scenario_feedback with action=‘skip’.

The affordance is intentionally quiet — small font, gray text. It’s not the primary path but it’s always available.

### Pause / resume

Pause button is in the header. Tap → calls orchestrator.pauseSessionAtNode(user_id, session_id, current_node_id). Navigates back to Home. The session shows up in a “Continue practice” affordance on Home (and on Library) until completed.

Resume from Home → opens this screen with the saved current_node_id. The screen detects this is a resume (not a fresh start) and re-renders the current node from scratch (does NOT replay prior nodes). The fresh node generation may produce slightly different text from the original — this is expected and acceptable.

Module version pinning: the resume uses the module_version stored in the session, not the latest. If the version is no longer loadable (shouldn’t happen in V4.1), show a clear error and offer to start a fresh session.

### Mid-module crisis interrupt

The existing risk classifier monitors the chat sessions. For practice sessions, the user can’t easily generate “messages” with risk content (choices are static). But the “Tell us why this doesn’t fit” free-text input could theoretically contain risk language.

If the user enters risk language in the “Tell us why” textarea:

- The submission triggers the existing crisis flow.

- The module pauses (orchestrator.pauseSessionAtNode).

- Crisis card / SOS opens.

- The user can return to the paused module later or abandon.

The risk classifier integration: re-use V3.7’s existing chat-message risk classifier on the textarea content before storing. If high or crisis, do NOT store the user_text (don’t even pass it to recordScenarioFeedback). Open crisis flow.

## TESTS

Add tests:

1. The screen renders correctly for a freshly-started session at the entry node.

1. Streaming completes and choice buttons are enabled.

1. LLM error → fallback text shown with banner.

1. Tapping a choice advances to the next node and re-renders.

1. “Why am I seeing this choice?” expands inline without navigation.

1. “This doesn’t fit my situation” → “Try again” regenerates the node text and logs a feedback row.

1. “This doesn’t fit” → “Tell us why” with phone numbers in the text → sanitized version stored.

1. “This doesn’t fit” → “Tell us why” with risk language → crisis flow opens, no row stored.

1. “This doesn’t fit” → “Skip this node” → advances using skip_default_choice_id (or first non-repair forward choice).

1. Pause button → state persisted, navigation to Home.

1. Resume from Home → screen opens at saved current_node, re-renders.

1. Module version pinning: resume uses session’s module_version even if a newer version is loaded.

1. Mid-module risk text in textarea → state pauses, no PII stored, crisis flow opens.

1. Choice text in DOM matches choice_text from JSON exactly (no AI rewriting).

## TARGETED SMOKE TEST

After implementation:

1. From Home, tap Practice → “I’m having an urge” → “Start practice” (using fixture module from V4.1 Prompt 2).

1. Verify hook node text streams in.

1. Verify Continue button appears after streaming.

1. Tap Continue. Verify concept node streams.

1. Tap Continue. Verify practice node streams with 2-4 choice buttons.

1. Tap “Why am I seeing this choice?” on one choice. Verify explanation expands inline.

1. Tap a choice. Verify next node loads.

1. If you picked a repair-routed choice, verify repair_loop node renders, then continues forward.

1. Tap pause. Verify navigation back to Home.

1. From Home, find the “Continue practice” affordance. Tap. Verify the screen re-opens at the saved node.

1. Tap “This doesn’t fit my situation” → “Try again”. Verify the node text regenerates.

1. Tap “This doesn’t fit” → “Tell us why” with text “this assumes I’m at a bar but I never go to bars”. Verify it logs to practice_scenario_feedback. Verify the node regenerates after.

1. Trigger LLM error (e.g., disconnect network). Verify fallback text appears with the banner.

1. Verify event_log gains ‘practice_module_started’ on entry, ‘practice_module_paused’ on pause.

1. Verify NO phone numbers ever appear in the rendered node text (the practice surface inherits this from V4).

1. Verify the choice text rendered matches the JSON exactly (no AI substitution).

## AT THE END

Report in under 300 words:

- Files created (route, components, hooks).

- Streaming approach used (matches existing chat pattern).

- LLM fallback behavior verified.

- Test pass/fail summary.

- Smoke test results.

- Any UI/UX adjustments from spec (mobile vs desktop layout differences are OK to flag).

- Confirmation that synthesis and outcome are not yet built (those are V4.1 Prompt 6).

- Confirmation that real modules are not yet authored (those are V4.1 Prompts 8-11).

- Any concerns about the current fallback flow’s quality (the pre-authored fallback text in the fixture module — is it good enough, or does it look obviously canned?).

- Exact next step: V4.1 Prompt 6 (Synthesis + outcome screens with bridge-to-action).

06

# V4.1 PROMPT 6: SYNTHESIS + OUTCOME SCREENS WITH BRIDGE-TO-ACTION

Build the closing screens of every module: synthesis (AI-generated paragraph summarizing what the user worked through), three-path outcome (commitment / tiny action / save without committing), bridge-to-action options for communication modules (Send the text now, Open Contacts, Copy this message), and the immediate post-module rating.

## STACK CONTEXT

V4.1 Prompts 1-5 built the practice surface, state machine, persistence, entry path, and module session screen up through practice/repair_loop nodes. This prompt completes the module experience: synthesis, outcome, and rating.

When the state machine reaches a synthesis node, the module session screen routes here. After outcome, the user returns to Home (or to a brief rating screen).

## IMPORTANT CONSTRAINTS

- Do NOT auto-save the AI-generated synthesis text. Saving it is opt-in.

- Do NOT require the user to write a commitment. The “Save without committing” path is fully supported.

- Do NOT auto-send anything. Bridge-to-action options open the existing native flow (system Messages/dialer) but the user sends the message themselves.

- Do NOT add fanfare. Quiet completion. Quiet checkmark, no confetti.

- Do NOT use language like “you completed” or “you achieved” — keep it grounded.

- Do NOT block the user from the rating step. It’s a tap, but skippable.

- Do NOT add streaks to the outcome screen.

- Do NOT pass user-edited synthesis text into the next node generation (no recursive personalization).

## PRE-FLIGHT

Confirm in 7 bullets:

1. Existing pattern for opening the native Messages app with a prefilled body (per V3.7 SOS pattern, if it exists).

1. Existing pattern for opening the native dialer with a prefilled number.

1. Existing pattern for clipboard copy with toast confirmation.

1. Where commitments are stored (commitments table from V3) and the helper to insert one with source=‘practice’.

1. Where the existing reminders / scheduling flow lives if commitments allow optional follow-up.

1. The route or screen pattern used for “completion” / “thank you” type screens.

1. Implementation plan: synthesis screen, outcome screen, rating screen, action handlers.

## SYNTHESIS SCREEN

When the state machine reaches a synthesis node, the module session screen calls /api/practice/generate-node with node_id of the synthesis node and node_type=‘synthesis’. The backend invokes buildChatSystemPrompt with practice_context that includes prior_choices_in_session.

The AI generates a single paragraph (2-4 sentences) summarizing what the user worked through. The paragraph references the actual choices the user made (e.g., “You chose to step away rather than push through. You picked the text-a-friend option instead of going it alone.”) without quoting the user back to themselves.

### Layout

- Title: “Here’s what you just did” (or similar grounded language).

- Streaming AI text area showing the synthesis paragraph.

- After streaming completes, three action buttons stacked vertically:

- **Save** (default visual emphasis): saves the module completion AND the synthesis_text. Routes to outcome screen.

- **Edit, then save**: opens an inline editor with the AI-generated paragraph as starting text. User edits, taps Save. Routes to outcome screen with the user-edited synthesis_text.

- **Save without saving the summary** (less prominent): saves the module completion ONLY. synthesis_text is NULL in the DB. Routes to outcome screen.

The third option is the spec’s default behavior for what gets saved. The visual emphasis on “Save” reflects that most users will keep the synthesis. But the third option must be visible and accessible.

### Edit flow

When user picks “Edit, then save”:

- Inline textarea pre-populated with the AI-generated paragraph.

- Character limit: 1000 chars (synthesis is meant to be short).

- Cancel button to exit without saving the edit (returns to “Save” / “Save without saving” state).

- Save button to commit the edited text.

The edited text is sanitized via the existing redaction helpers before storage.

## OUTCOME SCREEN

After synthesis is saved, the outcome screen presents three completion paths. The available paths are read from the module’s outcome node (outcome_options field), which always contains exactly three entries (one of each option_type).

### Layout

- Title: “What’s the next step?” or similar.

- Three large tappable cards, vertical stack:

#### Path 1: Write a commitment

- Card label: “Write a commitment for what you’ll actually do.”

- Tap opens an inline form:

- Text input (max 200 chars).

- “When?” dropdown: today / tomorrow / this week / specific date picker.

- “Remind me?” toggle (default OFF). If ON, schedules a reminder via the existing scheduler.

- “Save commitment” button.

- On save: insert into commitments table with source=‘practice’, text=user_input, due_date, reminder_enabled. Mark module session as completed with outcome_path=‘commitment’. Route to rating screen.

#### Path 2: Choose a tiny next action

- Card label: “Pick a small thing to do right now.”

- Tap reveals 3-5 options, defined per module by outcome_option entries with option_type=‘tiny_action’. Examples:

- For “The 20-Minute Urge”: “Drink a glass of water” / “Step outside for 5 min” / “Text a sober contact” / “Set a 20-minute timer and re-check in”

- For “Declining the Offer”: “Send the text now” (bridge action) / “Open Contacts” (bridge action) / “Save the message I just wrote” (bridge action) / “Save for later”

- For “Ask for Help Without a Speech”: “Send the text now” / “Open Contacts” / “Copy this message” / “Save for later”

- For “What to Do After a Slip”: “Drink water and eat something” / “Text a sober contact now” / “Open SOS resources” / “Save for later”

- User taps one option. Behavior depends on bridge_action field:

- ‘send_text’: prefilled body (defined per module / per option), open native Messages app with body. User sends manually.

- ‘open_contacts’: open the existing Contacts screen (V3 has sober_contacts).

- ‘copy_message’: copy a defined string to clipboard. Toast confirmation.

- ‘save_for_later’: just record the choice, no action. (Useful when user wants to acknowledge intent without acting.)

- none/null: just record the choice, no action.

- On any option selection: mark session completed with outcome_path=‘tiny_action’. Optionally also save the option_id chosen (small extension: add chosen_action_id to practice_progress, optional). Route to rating screen.

#### Path 3: Save without committing

- Card label: “Just save what I worked through. I’ll come back to it.”

- Tap → mark session completed with outcome_path=‘save_only’. Route to rating screen.

### Bridge-to-action mechanics

For ‘send_text’: the prefilled body is defined in the module JSON’s outcome_option. Example for “Ask for Help Without a Speech”:

```json

{

"option_id": "send_text_to_sober_contact",

"option_label": "Send the text now",

"option_type": "tiny_action",

"bridge_action": "send_text",

"prefill_body": "Hey, can we talk for a minute? I'm trying to stay grounded."

}

```

When user taps, the screen reads the user’s saved sober_contacts list (from stable_profile). If exactly one contact, open Messages prefilled. If multiple, show a quick contact picker first (matches existing V3.7 SOS contact picker if it exists). If none, show a graceful state: “You don’t have any sober contacts saved yet. Add one in Settings.” with a Settings shortcut.

For ‘open_contacts’: just open the contacts screen.

For ‘copy_message’: copy the option’s prefill_body to clipboard. Toast: “Copied. Send it when you’re ready.”

For ‘save_for_later’: record only.

### Sanity checks

The outcome screen MUST handle a session where the module’s outcome node has only 1 or 2 paths defined (validator should prevent this, but UI should not crash). If only one option is in outcome_options, show only that one. If outcome_options is empty (validator failure), show an error fallback that records save_only and lets the user exit.

## IMMEDIATE RATING SCREEN

After outcome, show a brief rating screen:

- Title: “Was this useful right now?”

- Three single-tap buttons:

- “Useful”

- “Not really”

- “Not sure”

- Below: “Skip” link.

Tapping any of the three records to event_log via logPracticeRated. Then routes to Home.

Tapping “Skip” or back button: routes to Home WITHOUT recording. (Skipping is logged separately as kind=‘practice_module_rated_immediate’ with rating=‘skipped’, if you want to track skip rate. Or simply not logged. Spec is silent — recommend logging skip as ‘not_sure’ equivalent, or as a fourth value ‘skipped’. Pick one and document the choice.)

The rating is non-gating. Skip is always available.

The rating is also write-only — it doesn’t surface elsewhere in the app. It informs system improvement, not user reflection.

## TESTS

Add tests:

1. Synthesis screen renders the AI-generated paragraph with three save options.

1. “Save” option: completeSession called with synthesis_text=AI-generated.

1. “Edit, then save”: user edits, completeSession called with synthesis_text=edited.

1. “Save without saving summary”: completeSession called with synthesis_text undefined/empty (stored as NULL).

1. Edited synthesis with phone numbers → sanitized version stored.

1. Outcome screen renders exactly the three paths defined in outcome_options.

1. Path 1 “Write a commitment”: form submission inserts commitments row with source=‘practice’.

1. Path 2 “Tiny action” with bridge_action=‘send_text’: clicking opens Messages app with prefill (test by mocking the native API).

1. Path 2 ‘send_text’ with no sober contacts saved: graceful empty state shown.

1. Path 2 ‘send_text’ with multiple contacts: contact picker shown.

1. Path 2 ‘copy_message’: clipboard write tested with toast.

1. Path 3 “Save without committing”: completeSession called with outcome_path=‘save_only’.

1. Rating screen records to event_log on tap.

1. Rating screen “Skip” button bypasses logging (or logs ‘skipped’ depending on chosen behavior — must match documentation).

1. Outcome screen with empty outcome_options: graceful error fallback recording save_only.

## TARGETED SMOKE TEST

After implementation:

1. Continue from V4.1 Prompt 5’s smoke test. Walk through the fixture module to a synthesis node.

1. Verify synthesis paragraph streams in, references the actual choices made.

1. Tap “Save”. Verify outcome screen appears.

1. Verify three outcome paths visible (the fixture module’s outcome should define all three).

1. Tap “Write a commitment”. Verify form opens. Type a commitment, set due date to tomorrow, leave reminder OFF, save.

1. Verify commitments table has new row with source=‘practice’.

1. Verify session is marked completed with outcome_path=‘commitment’.

1. Verify rating screen appears.

1. Tap “Useful”. Verify event_log has ‘practice_module_rated_immediate’ with rating=‘useful’.

1. Verify navigation back to Home.

1. Run the module again. This time at synthesis, tap “Edit, then save”. Edit the text. Save.

1. Verify the edited text is in practice_progress.synthesis_text.

1. Run the module again. At synthesis, tap “Save without saving the summary”. Verify synthesis_text is NULL in DB.

1. Run again. At outcome, tap “Save without committing”. Verify outcome_path=‘save_only’ in DB.

1. Run again. At outcome, tap “Pick a small thing to do right now” → “Save for later”. Verify outcome_path=‘tiny_action’ (and optionally chosen_action_id stored).

1. Verify Path 2 with bridge_action=‘send_text’ opens Messages prefilled with the right body (test on a real device or via mock).

1. Verify Path 2 with bridge_action=‘copy_message’ copies and toasts.

1. Skip the rating. Verify event_log behavior matches the documented choice.

## AT THE END

Report in under 300 words:

- Files created (synthesis screen, outcome screen, rating screen, action handlers).

- Bridge-to-action behavior verified per option type.

- Confirmation that synthesis_text is opt-in (default save_only).

- Confirmation that no auto-send happens.

- Test pass/fail summary.

- Smoke test results.

- Documented choice for “Skip rating” behavior (logs ‘skipped’ or doesn’t log).

- Confirmation that no streaks/percentages appear on these screens.

- Any deviations from spec.

- Exact next step: V4.1 Prompt 7 (Contraindication checker, Settings additions, onboarding update for V4.1).

07

# V4.1 PROMPT 7: CONTRAINDICATION CHECKER + SETTINGS ADDITIONS + ONBOARDING UPDATE

Cleanup work for V4.1’s infrastructure: contraindication evaluation before module launch, Settings additions for Practice (reset / export / per-focus deletion), and a one-screen onboarding update introducing Practice as a new surface for existing users.

## STACK CONTEXT

V4.1 Prompts 1-6 built the practice surface, state machine, persistence, entry path, module session screen, and synthesis/outcome screens. This prompt adds the remaining infrastructure that doesn’t fit cleanly into the module-authoring prompts that follow.

## IMPORTANT CONSTRAINTS

- Do NOT enforce contraindications that V3.7 cannot detect. Some are declared (driving, domestic_violence) but not enforceable until V5+. Build the framework; the actual checks for those are stubs.

- Do NOT add UI for power-user features beyond what’s specified. Settings stays focused.

- Do NOT block app access during onboarding update. The new screen for existing users is informational and skippable.

- Do NOT modify V4 onboarding flow content. The Practice introduction is added AFTER V4 onboarding completes for new users, or as a one-time modal for existing users.

- Do NOT auto-launch any module from the introduction screen. Users tap to explore.

- Do NOT modify the Practice surface or state machine in this prompt.

## PRE-FLIGHT

Confirm in 6 bullets:

1. The structure of V4 onboarding’s existing “complete” handler — where the user lands after Step 10.

1. The existing Settings screen structure and how new sections are added.

1. The existing Data Export pattern (V5.2 introduces JSON/CSV/Markdown export; V4.1 may not yet have it — confirm whether there’s an existing export framework or if V4.1 just adds a Practice-specific endpoint).

1. The existing pattern for “show this modal once” tracking (similar to V4’s existing-user migration modal pattern with v4_modal_skipped_count).

1. The existing pattern for reading event_log for evaluation of risk-state signals.

1. Implementation plan: contraindication checker file, Settings sections, onboarding intro screen.

## CONTRAINDICATION CHECKER

Add server/practice/contraindicationChecker.ts:

```typescript

export type ContraIndicationResult =

| { matched: false }

| { matched: true; type: ContraIndication; behavior: 'warn' | 'block' | 'route'; route_to?: 'sos' | 'medical_resources' };

export async function checkContraindications(

user_id: string,

module: Module

): Promise<ContraIndicationResult>;

```

The checker reads the user’s recent state and evaluates each contraindication declared on the module. If any matches, returns the strictest applicable result.

### Per-contraindication evaluation logic

- **‘acute_intoxication’** (warn-only):

- Check most recent check-in (within 6 hours) for elevated craving (>=8/10) AND a free-text note containing intoxication keywords. If matched, return warn.

- Behavior ‘warn’ = launch the module but show a one-screen pre-launch warning: “It sounds like you may be under the influence right now. This practice is here when you’re ready, but it works best when you’re sober. Want to continue or come back later?” Two buttons: Continue / Come back later.

- **‘driving’** (block, V3.7 not detectable — STUB):

- V3.7 has no driving signal. Return { matched: false } always. The check function exists but is a stub.

- Add a TODO comment referencing V5+: “Driving detection requires motion API integration; deferred to V5+. This stub returns false.”

- **‘severe_withdrawal’** (route to medical resources):

- Check most recent check-in for craving=10 AND free-text containing withdrawal keywords (shaking, sweating, hallucinating, can’t sleep, vomiting). If matched, return route to medical_resources.

- Behavior ‘route’ = pre-launch screen instead of module: “What you’re describing may be withdrawal. This isn’t something to handle alone. Some withdrawal (alcohol, benzos, opioids) can be medically dangerous.” Buttons: Open SAMHSA / Call 988 / Continue anyway / Go back.

- **‘unsafe_contact’** (warn — restricts repair/contact prompts):

- Check stable_profile.pinned_facts or recent event_log for entries marking certain contacts as unsafe to reach out to. (V3.7 may not have this directly. STUB if absent.) Return matched=false in stub case.

- Behavior ‘warn’ (when implemented): pre-launch warning that the module includes “reach out to someone” steps and asks the user to be selective.

- **‘suicidal_ideation’** (route to SOS):

- Check most recent risk_classification event in event_log within last 24 hours for ‘high’ or ‘crisis’. If matched, route to SOS.

- Behavior ‘route’ to ‘sos’: pre-launch screen: “I noticed something difficult came up recently. Practice is here when you’re ready, but right now might not be the moment. Talking to a person matters more than rehearsing.” Buttons: Open SOS / Open Chat / Continue anyway / Go back.

- **‘domestic_violence’** (V3.7 not detectable — STUB):

- Return { matched: false }. Add TODO comment for V5+.

- **‘eating_disorder_active’** (route away):

- Check stable_profile.recovery_focus for ‘food’ AND most recent check-in for restriction/purging keywords. (Likely STUB — V3.7 may not have this signal robustly. Return matched=false in stub case.)

- Behavior ‘route’: pre-launch screen referring user to NEDA / professional resources.

### Wiring into module launch

In the module session orchestrator (V4.1 Prompt 3) or the screen that launches a module, before calling startNewSession, call checkContraindications. If matched=true:

- ‘warn’: show warning screen with Continue / Come back later. If Continue, proceed; if Come back, return to need-state screen. Either way, log to event_log: ‘practice_contraindication_shown’ with type and user_choice.

- ‘block’: show blocking screen with Go back only. Log ‘practice_contraindication_blocked’.

- ‘route’: show route screen with appropriate destinations. Log ‘practice_contraindication_routed’.

The user always has the ability to bypass (except for explicit blocks). Per Anchor’s autonomy invariant.

## SETTINGS ADDITIONS

Add a new Settings section: “Practice History”.

### Section: Practice History

Below “Recovery Profile” (or wherever feels natural):

- **Reset practice history**: Tap → confirmation modal → calls deleteAllPracticeData. Toast: “Practice history cleared. Your sobriety history is unaffected.”

- **Export practice history**: Tap → calls exportPracticeData server-side, returns JSON file download. (If a project-wide Data Export framework doesn’t exist yet, this is a Practice-specific endpoint that can be subsumed into V5.2’s broader export later.)

- **Reset history for a specific focus**: Tap → opens a focus selector showing the user’s current recovery_focus list. Tap a focus → confirmation modal → calls deletePracticeDataForFocus(user_id, focus). Toast: “Practice history for {focus} cleared.”

Three subtle text descriptions below the buttons:

- “Reset practice clears all your module sessions, choices, and saved summaries. It does NOT touch your check-ins, sobriety dates, or chat history.”

- “Export creates a JSON file of all your practice data.”

- “Reset for a focus removes only sessions tied to that focus.”

### Section: Practice preferences (small)

- **Show pause hint on Home**: toggle, default ON. When ON, paused sessions appear as a “Continue practice” affordance on Home.

- **Allow practice notifications**: toggle, default OFF. (Doesn’t do anything yet — V5+. UI placeholder for future opt-in.)

The notification toggle is INTENTIONALLY non-functional in V4.1. It’s there to set expectations: Practice will never send notifications without opt-in. This communicates the privacy posture even before any notification feature ships.

## ONBOARDING UPDATE FOR V4.1

For V4 onboarding (10 steps total post-V4), add a one-screen “Welcome to Practice” intro that appears AFTER Step 10 completion for new users post-V4.1 deploy.

### Layout for new users

After completing Step 10 (reminder time + email), instead of routing to Home directly, route to:

- Title: “One more thing before you start.”

- Body: “Anchor includes Practice — short scenarios where you rehearse the moment, not just talk about it. Things like saying no to a drink, asking for help, getting through an urge.”

- Subtext: “It’s optional. You can always find it on Home.”

- Button: “Got it.” → routes to Home.

This is a one-screen modal, dismissed-once-shown via flag in app_settings (e.g., onboarding_practice_intro_shown=true). Never shown twice.

For users who completed V4 onboarding before V4.1 deploys (existing users post-V4 but pre-V4.1), the same screen appears as a one-time modal on first V4.1 open. Same dismissal flag.

### Schema impact

Add one column to app_settings:

```sql

ALTER TABLE app_settings ADD COLUMN onboarding_practice_intro_shown BOOLEAN NOT NULL DEFAULT FALSE;

```

Migration is small, additive, idempotent.

## TESTS

Add tests:

1. checkContraindications for module with ‘driving’ → returns matched=false (stub).

1. checkContraindications for module with ‘suicidal_ideation’ when recent risk=‘high’ event exists → returns route to SOS.

1. checkContraindications for module with ‘severe_withdrawal’ when check-in has craving=10 + withdrawal keywords → returns route to medical_resources.

1. checkContraindications for module with ‘acute_intoxication’ when check-in has craving=9 + intoxication keywords → returns warn.

1. checkContraindications for module with no contraindications declared → returns matched=false.

1. Module launch: matched=warn → warning screen shown, log entry created.

1. Module launch: matched=route → route screen shown, log entry created.

1. Settings: Reset practice → calls deleteAllPracticeData, toast appears, no other tables touched.

1. Settings: Export practice → JSON downloaded with all expected fields.

1. Settings: Reset for focus ‘alcohol’ → calls deletePracticeDataForFocus(‘dev_user’, ‘alcohol’), removes only matching session_focus rows.

1. Onboarding intro: shown to new user after Step 10.

1. Onboarding intro: shown once to existing user on first V4.1 open.

1. Onboarding intro: NOT shown on second app open after dismissal.

1. app_settings.onboarding_practice_intro_shown migration up creates column with default false.

## TARGETED SMOKE TEST

After implementation:

1. Open Settings. Verify “Practice History” section visible with three buttons.

1. Tap “Reset practice history” → confirmation modal → confirm. Verify all practice rows deleted. Verify check-ins and commitments untouched.

1. Restart with seeded practice data. Tap “Export practice history”. Verify JSON file downloads with practice_progress, practice_choices, practice_scenario_feedback contents.

1. Tap “Reset history for a specific focus” → tap “alcohol” → confirm. Verify only alcohol-focus sessions deleted.

1. Open Settings. Verify “Practice preferences” section with two toggles. Verify notifications toggle is functional in UI (state persists) but doesn’t trigger anything in V4.1.

1. Test contraindication checker:

- Inject a risk_classification ‘high’ event into event_log.

- Try to launch a module with ‘suicidal_ideation’ contraindication.

- Verify route screen appears with SOS / Chat / Continue / Back options.

- Tap Continue. Verify module launches anyway (autonomy preserved).

1. Test acute_intoxication warning:

- Insert a check-in with craving=9 and free-text “had a few drinks tonight”.

- Try to launch a module with ‘acute_intoxication’ contraindication.

- Verify warning screen appears.

- Tap Continue. Module launches.

1. Onboarding intro:

- Reset onboarding for a new dev user. Walk through V4 onboarding to Step 10. Verify “One more thing before you start” appears. Tap “Got it.” Verify Home opens.

- Re-open app. Verify intro NOT shown again.

- Take an existing user with onboarding_practice_intro_shown=false. Open app. Verify intro shown. Dismiss. Re-open. Verify NOT shown.

## AT THE END

Report in under 300 words:

- Files created (contraindication checker, Settings sections, onboarding intro).

- Migration applied.

- Confirmation that V3.7-undetectable contraindications (driving, domestic_violence, eating_disorder) are stubs with TODO comments.

- Confirmation that user can bypass non-block contraindications.

- Test pass/fail summary.

- Smoke test results.

- Practice notifications toggle is intentionally non-functional — confirmed.

- Any concerns about the intoxication detection heuristics (free-text keyword matching is rough — flag this).

- Exact next step: V4.1 Prompt 8 (Module 1: The 20-Minute Urge — vertical proof).

08

# V4.1 PROMPT 8: MODULE 1 — THE 20-MINUTE URGE (VERTICAL PROOF)

Author the first real V4.1 module: The 20-Minute Urge. Author it for ONE focus first (alcohol), validate the architecture against a real module, then expand to the other applicable focuses (weed, nicotine, porn). This is the vertical proof per V4.1 Section 9 build sequencing.

## STACK CONTEXT

V4.1 Prompts 1-7 built all the infrastructure. The Practice surface variant exists. The state machine works. The DB tables exist. The screens are built. The contraindication checker is wired in. The voice exemplar (urge_skills.md) was authored in Prompt 1.

This prompt is mostly authoring work, not engineering. The engineering surface area is small (one JSON file to commit, one focus mapping to verify) but the writing quality is what determines whether the module lands well.

## IMPORTANT CONSTRAINTS

- Do NOT skip the alcohol-only first pass. Author alcohol-only fully, walk through end-to-end as a user, adjust, THEN expand to other focuses.

- Do NOT invent psychology beyond what urge surfing literature establishes (DBT-derived, Marlatt’s model). The AI will personalize, not innovate.

- Do NOT use coaching cadence (“Let’s break this down!”) or therapy cadence (“How does that make you feel?”) in any prompt template or fallback text.

- Do NOT use “this time will be different” framing anywhere.

- Do NOT shame the user for picking sub-optimal choices.

- Do NOT add a withdrawal disclaimer to the module body — it’s added per-focus where applicable in voice_constraints, not in the user-facing copy.

- Do NOT exceed 5-7 minute total module length (3-min floor, 7-min ceiling per spec).

- Do NOT bypass the V4.1 schema. Every field validated by V4.1 Prompt 2’s validator must be correct.

## PRE-FLIGHT

Confirm in 6 bullets:

1. The voice exemplar urge_skills.md exists from Prompt 1 with samples for alcohol, weed, nicotine, porn.

1. The branch tree schema and validator from Prompt 2 are functional.

1. The module session screen, synthesis, and outcome screens (Prompts 5-6) work end-to-end with the fixture module.

1. The contraindication checker (Prompt 7) handles ‘severe_withdrawal’ and ‘acute_intoxication’ correctly.

1. The focus-to-variable resolver (Prompt 1) has mappings for alcohol, weed, nicotine, porn.

1. Implementation plan: branch shape, node count per phase, variable usage per node, fallback text length per node.

## MODULE OVERVIEW

**module_id**: urge_20_min

**module_version**: 1.0.0

**display_name**: The 20-Minute Urge

**internal_track**: urge_skills

**applicable_focuses**: [‘alcohol’, ‘weed’, ‘nicotine’, ‘porn’]

**applicable_methods**: [] (all methods)

**estimated_minutes**: { floor: 3, ceiling: 7 }

**voice_exemplar_ref**: ‘urge_skills’

**contraindications**: [‘acute_intoxication’, ‘severe_withdrawal’, ‘suicidal_ideation’]

### What the module teaches

Urges are time-limited and ride a wave. They peak then subside. The skill is creating a pause between trigger and action — and using that pause to do something simple that takes the user past the peak. 20 minutes is the canonical heuristic (urges tend to subside within 20-30 min if not acted on).

The module rehearses noticing the urge, naming what it actually wants (the relief, not the substance), making one small different choice for 20 minutes, and what to do if the urge is still strong after 20 minutes.

## BRANCH TREE STRUCTURE

The module has 9 nodes total:

1. **Hook** (node_type: hook) — A single concrete moment. Generated text: 2-3 sentences. The user is alone after a hard day; the craving for {focus_substance_or_behavior_human} arrives. Generates suspense.

1. **Concept** (node_type: concept) — The skill in plain language. 4-5 sentences. Urges are time-limited. They ride a wave. The pause is the practice.

1. **Practice 1: Notice** (node_type: practice) — A scenario continuation: the user is sitting with the urge. 3 choices.

1. **Repair Loop A** (node_type: repair_loop) — If user picked the “act on it now” choice. 2-3 sentences reframing without shame, then routes to Practice 2.

1. **Practice 2: Pause** (node_type: practice) — User has the pause; what does the urge actually want? 3 choices.

1. **Practice 3: Choose one different action** (node_type: practice) — The user picks a small action for the next 20 minutes. 3-4 choices.

1. **Repair Loop B** (node_type: repair_loop) — If user picked an action that’s clearly not different (e.g., “sit and stew”). Reframes, routes back to Practice 3.

1. **Synthesis** (node_type: synthesis) — One paragraph summarizing what the user worked through, referencing their actual choices.

1. **Outcome** (node_type: outcome) — Three completion paths.

### Forward path (no repair loops)

Hook → Concept → Practice 1 → Practice 2 → Practice 3 → Synthesis → Outcome

### Repair loop paths

- Practice 1’s “act on it now” choice → Repair Loop A → Practice 2 (forward path resumes)

- Practice 3’s non-action choice → Repair Loop B → back to Practice 3 with the same choices, choosing again

## NODE-BY-NODE AUTHORING

For each node, author:

- prompt_template (instruction to the AI)

- voice_constraints (max length, forbidden phrases, exemplar reference)

- choices (for practice nodes) — STATIC, AI never rephrases

- choice_explanations (“Why am I seeing this?”)

- next_node_id (for non-practice forwards)

- fallback_default_text (pre-authored, focus-agnostic, used if LLM fails)

### Node 1: Hook

```

prompt_template: "Generate a brief 2-3 sentence scene where the user is alone after a hard day and notices the craving for {focus_substance_or_behavior_human}. The scene is concrete: time of day (evening), location (their place), one sensory detail. End with the moment before deciding what to do. Voice: second person, plain, grounded. Do not editorialize. Do not name the urge as 'urge' yet — describe it."

voice_constraints: "Max 3 sentences. Second person. No questions. No editorializing. No clinical labels. Reference voice exemplar 'urge_skills'."

next_node_id: "concept"

fallback_default_text: "It's late. The day's been long, and you're sitting alone. The craving showed up the way it usually does — quiet, then loud."

```

### Node 2: Concept

```

prompt_template: "In 4-5 sentences, explain that urges are time-limited. They build, they peak, they subside — usually within 20-30 minutes if not acted on. The skill being practiced today is creating a pause between trigger and action. Use the user's focus ({focus_action_human}) as the example. Plain language. No coaching cadence. No therapy questions."

voice_constraints: "Max 5 sentences. No questions. No coaching cadence. Reference voice exemplar 'urge_skills'."

next_node_id: "practice_1_notice"

fallback_default_text: "Urges aren't permanent. They build, they peak, and they pass. Most peak within 20 to 30 minutes when you don't act on them. The skill today is making a pause — a small space between the urge and the action. The pause is where the choice lives."

```

### Node 3: Practice 1 — Notice

```

prompt_template: "Continue the scene. The user is sitting with the craving for {focus_substance_or_behavior_human}. 2-3 sentences describing the felt sense of the urge — physical, internal, not yet a decision. End the scene with a question to the reader: 'What do you do right now?' Then the choices appear separately."

voice_constraints: "Max 3 sentences before the question. No clinical labels. Voice exemplar 'urge_skills'."

choices:

- id: "notice_act_now"

text: "Act on it. Get {focus_substance_or_behavior_human}."

explanation: "This is the most common move — and the one that keeps the cycle going. We'll show you the pattern, not shame you for it."

next_node_id: "repair_loop_a"

is_repair_route: true

- id: "notice_name_it"

text: "Pause. Notice the urge is here, without doing anything about it yet."

explanation: "This is the harder move and the more useful one. Naming the urge creates space."

next_node_id: "practice_2_pause"

is_repair_route: false

- id: "notice_distract"

text: "Quickly do something else — anything — to not feel it."

explanation: "Distraction can work, but it skips the practice we're building today. Try the harder move first."

next_node_id: "practice_2_pause"

is_repair_route: false

fallback_default_text: "The urge is here. You feel it in your chest, in your hands. There's no decision yet — just the sensation. What do you do right now?"

```

### Node 4: Repair Loop A

```

prompt_template: "The user chose to act on the urge immediately. In 2-3 sentences, reframe without shame: this is the move that usually backfires, but the user is not in trouble — they're here in practice. Briefly note the cost (the cycle continues) without lecturing. Route forward."

voice_constraints: "Max 3 sentences. No shaming. No clinical labels. Voice exemplar 'urge_skills'."

next_node_id: "practice_2_pause"

fallback_default_text: "That's the move that usually backfires — not because you're weak, but because the urge wins by skipping the pause. Let's try the harder move."

```

### Node 5: Practice 2 — Pause

```

prompt_template: "The user has the pause. In 3 sentences, describe what's behind the urge — what does it actually want? Not the {focus_substance_or_behavior_human} itself, but the relief, the numbing, the escape, the rest. Pick the most likely one for an evening-alone moment. End with a question to the reader: 'What does the urge actually want right now?' Then the choices appear separately."

voice_constraints: "Max 3 sentences. Voice exemplar 'urge_skills'."

choices:

- id: "pause_relief"

text: "Relief. I'm trying to take the edge off something I don't want to feel."

explanation: "Most common. The urge is usually about regulation, not the substance."

next_node_id: "practice_3_action"

is_repair_route: false

- id: "pause_rest"

text: "Rest. I'm exhausted and I want to escape."

explanation: "Common after a hard day. Sleep or quiet matters more than the substance."

next_node_id: "practice_3_action"

is_repair_route: false

- id: "pause_connection"

text: "Connection. I don't want to be alone right now."

explanation: "Often hidden. Loneliness drives a lot of urges."

next_node_id: "practice_3_action"

is_repair_route: false

fallback_default_text: "The urge isn't really about the {focus_substance_or_behavior_human}. It's about something underneath — relief, rest, escape, company. What does it actually want?"

```

(Note: the {focus_substance_or_behavior_human} variable in fallback_default_text won’t be substituted — the fallback is focus-agnostic. Author it generically. The fallback above should be revised: “The urge isn’t really about the substance. It’s about something underneath — relief, rest, escape, company. What does it actually want?”)

### Node 6: Practice 3 — Choose one different action

```

prompt_template: "The user has named what the urge wants. Now they pick one small action to do for the next 20 minutes. Briefly: 1-2 sentences setting up that the action doesn't need to be heroic, just different from what the urge wants. End with question: 'What's the small different action for the next 20 minutes?'"

voice_constraints: "Max 2 sentences before question. Voice exemplar 'urge_skills'."

choices:

- id: "action_water_food"

text: "Drink a glass of water and eat something simple."

explanation: "Physical regulation. Cheap and effective. Often disrupts the urge."

next_node_id: "synthesis"

is_repair_route: false

- id: "action_step_outside"

text: "Step outside for 5 minutes. Just air, no goal."

explanation: "Change of state. Movement and outside air shifts internal state quickly."

next_node_id: "synthesis"

is_repair_route: false

- id: "action_text_someone"

text: "Text a sober contact. Don't make it a speech — just one line."

explanation: "Connection action. Doesn't have to be deep — being witnessed matters."

next_node_id: "synthesis"

is_repair_route: false

- id: "action_sit_through"

text: "Just sit. Don't do anything. Wait it out."

explanation: "Common move that often doesn't work. Sitting and stewing tends to amplify the urge. Try one of the other moves first."

next_node_id: "repair_loop_b"

is_repair_route: true

fallback_default_text: "Pick one small thing to do for the next 20 minutes. It doesn't need to be heroic — it just needs to be different from what the urge wants."

```

### Node 7: Repair Loop B

```

prompt_template: "The user chose to sit and stew through the urge. In 2-3 sentences, reframe: sitting through the urge without any action tends to amplify it, not reduce it. The 20-minute heuristic works better when paired with a small different action. Route back to Practice 3 to try again."

voice_constraints: "Max 3 sentences. No shaming. Voice exemplar 'urge_skills'."

next_node_id: "practice_3_action"

fallback_default_text: "Sitting and stewing tends to amplify the urge instead of reducing it. The 20-minute pause works better when paired with one small different action. Try one of the others."

```

### Node 8: Synthesis

```

prompt_template: "Generate one paragraph (2-4 sentences) summarizing what the user worked through. Reference the choices they actually made: 1) what they noticed (the urge arrived, they paused or didn't), 2) what they identified the urge wanted, 3) what action they chose. Don't quote the user. Don't add advice. Don't generalize beyond what they actually did. Plain, grounded, third-person ('You noticed...', 'You picked...')."

voice_constraints: "Max 4 sentences. Second person. Voice exemplar 'urge_skills'."

next_node_id: "outcome"

fallback_default_text: "You noticed the urge instead of acting on it. You named what it actually wanted. You picked one small action for the next 20 minutes. That's the practice — and it's the move that builds, every time you do it."

```

### Node 9: Outcome

```

node_type: outcome

outcome_options:

- option_id: "commit_pause_practice"

option_label: "Write a commitment about pausing the next time."

option_type: "commitment"

- option_id: "tiny_action_now"

option_label: "Pick a small thing to do right now."

option_type: "tiny_action"

(sub-options shown in outcome screen UI):

- "Drink a glass of water"

- "Step outside for 5 minutes"

- "Text a sober contact" (bridge_action: 'send_text', prefill_body: "Hey — having a hard moment. Could use one minute of your time.")

- "Save for later"

- option_id: "save_only"

option_label: "Save without committing. I'll come back to it."

option_type: "save_only"

```

## FALLBACK TEXT

Every node has fallback_default_text per the schema. The fallbacks are focus-agnostic — they reference “the urge” and “the substance” generically. Per V4.1 spec, fallbacks are acceptable, not great. They keep the module functional when the LLM fails.

Author all 9 nodes’ fallback text. Total length should be ~150-250 words across all fallback_default_text entries.

## ALCOHOL-FIRST WALKTHROUGH

After authoring all 9 nodes for alcohol focus, walk through the module end-to-end as a real user:

1. Open Practice → “I’m having an urge” → “Start practice”.

1. Walk through every node.

1. Test all three choice paths in Practice 1 (including the repair-routed one).

1. Test the repair loop in Practice 3.

1. Reach synthesis. Verify the paragraph correctly references the choices made.

1. Reach outcome. Test all three completion paths.

1. Test “This doesn’t fit” affordance: tap regenerate; tap “tell us why” with feedback; tap skip.

1. Verify session DB rows are correct.

If any node feels weak, off-voice, awkward, or doesn’t lead naturally to the next, REVISE before moving to weed/nicotine/porn.

This is the moment of truth for the V4.1 architecture. If the architecture works for one good module, it’ll work for the rest. If something needs to change in the schema, the loader, the assembler, or the screens — change it now.

## EXPAND TO OTHER FOCUSES

After alcohol-only is solid, walk through the same nodes for weed, nicotine, and porn focuses. The prompt_template uses {focus_substance_or_behavior_human} which the resolver maps. For most nodes, this works directly.

For porn focus specifically, the hook needs adjustment — porn doesn’t have the same evening-alone-with-substance scene. Update the hook’s prompt_template to handle porn focus differently (perhaps via a focus_specific_hook_prompt field on the hook node, or by including focus-conditional language in prompt_template itself).

Alternatively: have the hook’s prompt_template be focus-aware via a small conditional in the prompt itself: “If focus is alcohol/weed/nicotine: scene of evening alone with the craving for the substance. If focus is porn: scene of being alone, idle, the impulse to look at something arrives quietly.”

Pick one approach. Document it. Test all four focuses.

## TESTS

Add tests:

1. urge_20_min_v1_0_0.json validates clean against the V4.1 Prompt 2 validator.

1. State machine: walking the full forward path produces the expected node sequence.

1. State machine: walking through Repair Loop A returns to Practice 2.

1. State machine: walking through Repair Loop B returns to Practice 3.

1. Fallback text is present for all 9 nodes.

1. Variable expansion: hook prompt_template with {focus_substance_or_behavior_human} resolves to “a drink” for alcohol focus.

1. Synthesis-node prompt includes prior_choices_in_session.

## TARGETED SMOKE TEST

Walk through the module end-to-end for each focus (alcohol, weed, nicotine, porn). For each focus:

1. Open Practice → “I’m having an urge” → start.

1. Verify hook reads naturally for this focus.

1. Verify concept reads naturally.

1. Walk through Practice 1, 2, 3 making different choices each time.

1. Trigger Repair Loop A by picking “act on it now”. Verify reframe is non-shaming, routes correctly.

1. Trigger Repair Loop B by picking “sit and stew”. Verify reframe routes back.

1. Reach synthesis. Verify paragraph correctly references choices.

1. Reach outcome. Test all three paths.

1. For alcohol focus, verify the contraindication checker fires when severe_withdrawal flag is active.

1. Test “This doesn’t fit” with text “this assumes I’m at home but I’m at work right now” → verify regen reflects the feedback context (it might not — the regen has the same prompt, just different LLM seed; the user_text feedback informs YOUR module revision, not the next regen).

The “This doesn’t fit” affordance feedback isn’t fed into the regen prompt — it just stores the user’s complaint for later module improvement. Make sure this is clear in the smoke test interpretation.

## AT THE END

Report in under 400 words:

- Module file path: server/practice/modules/urge_20_min_v1_0_0.json

- Total module byte count.

- Number of nodes (target: 9).

- Per-focus walkthrough results: did each of alcohol/weed/nicotine/porn produce a coherent module experience?

- Any node that needed multiple revisions before feeling right.

- The approach picked for porn focus’s different hook scene.

- Test pass/fail summary.

- Smoke test results.

- Any architectural changes needed during the vertical (and what they were — schema additions, loader changes, screen changes).

- Honest voice quality assessment: does the module feel sponsor-adjacent, plain, and grounded? Or does it leak coaching/therapy cadence?

- Any “this doesn’t fit my situation” feedback observed during walkthroughs that should inform future module revisions.

- Exact next step: V4.1 Prompt 9 (Modules 2-3: Lapse vs Relapse + Ask for Help Without a Speech).

09

# V4.1 PROMPT 9: MODULES 2-3 — LAPSE VS RELAPSE + ASK FOR HELP WITHOUT A SPEECH

Author two modules in one prompt: Lapse vs Relapse (foundations track, shame-reduction concept module) and Ask for Help Without a Speech (communication & repair track, vulnerability/disclosure scenario). The vertical from Prompt 8 has proven the architecture — these two reuse the pattern.

## STACK CONTEXT

V4.1 Prompts 1-7 built infrastructure. Prompt 8 authored Module 1 (The 20-Minute Urge) as the vertical proof.

Modules 2 and 3 reuse the same authoring pattern. Both apply to all focuses (no focus-specific scene differences as fundamental as Module 1’s porn case). The voice exemplars from Prompt 1 (foundations_lapse_vs_relapse.md and communication_repair_help.md) are the voice references.

## IMPORTANT CONSTRAINTS

- Do NOT shame the user in any node, especially in Lapse vs Relapse where the topic is post-slip experience.

- Do NOT use clinical labels (“relapse disorder”, “addiction cycle”).

- Do NOT use “you should” / “you need to” framing — practice teaches via scenario, not prescription.

- Do NOT use 12-step-specific language unless it’s broadly familiar (don’t say “powerless” / “amends” / “Step X” without context).

- Do NOT make the modules longer than 7 minutes. 9-12 nodes per module max.

- Do NOT bundle all four focuses into one walkthrough. Test alcohol first for each module, expand after.

- Do NOT skip the V4.1 Prompt 2 validator on either module. Both must pass.

- Do NOT have repair loops that loop infinitely. Every repair routes forward eventually.

## PRE-FLIGHT

Confirm in 4 bullets:

1. Module 1 (urge_20_min) shipped successfully and walked through clean.

1. Voice exemplars foundations_lapse_vs_relapse.md and communication_repair_help.md exist with samples.

1. Bridge-to-action infrastructure (V4.1 Prompt 6) handles ‘send_text’, ‘open_contacts’, ‘copy_message’, ‘save_for_later’. (Module 3 will use these heavily.)

1. Implementation plan: branch shapes for both modules, node counts, focus coverage strategy.

-----

## MODULE 2: LAPSE VS RELAPSE

**module_id**: lapse_vs_relapse

**module_version**: 1.0.0

**display_name**: Lapse vs Relapse

**internal_track**: foundations

**applicable_focuses**: [‘alcohol’, ‘weed’, ‘nicotine’, ‘porn’, ‘cocaine’, ‘opioids’, ‘codependency’, ‘food’, ‘sex’, ‘gambling’]

**applicable_methods**: [] (all)

**voice_exemplar_ref**: ‘foundations_lapse_vs_relapse’

**contraindications**: [‘suicidal_ideation’]

### What it teaches

The distinction between a lapse (a single instance of using/acting that doesn’t have to define everything) and a relapse (a return to the pattern). The shame spiral that turns a lapse into a relapse — the abstinence violation effect. The skill is interrupting the spiral, separating one event from a pattern.

### Branch shape

This is a CONCEPT-HEAVY module, less branchy than Module 1. The “branching” is around how the user responds to a lapse, not what action they take next.

Nodes (8 total):

1. **Hook** — A single concrete moment: the user is the morning after a slip. Internal feeling. 2-3 sentences.

1. **Concept 1: The lapse vs relapse distinction** — 4-5 sentences. A lapse is one instance. A relapse is when one instance becomes a pattern. The thing that turns one into the other is the shame spiral.

1. **Concept 2: The abstinence violation effect** — 3-4 sentences. After a lapse, the brain does a particular thing: “I broke the rule, so the rule is broken, so I might as well…” Naming it is most of the work.

1. **Practice 1: What happens internally after a lapse** — 3 choices reflecting common patterns. (Not “what should you do” — “what’s actually happening for you right now.”)

1. **Practice 2: One small move to interrupt the spiral** — 3-4 choices. Each is a small move. One choice is “I’m too far gone to do anything small” — leads to repair loop.

1. **Repair Loop** — Reframes “too far gone” as part of the abstinence violation effect itself. Routes back to Practice 2.

1. **Synthesis** — One paragraph referencing what the user identified internally and what action they picked.

1. **Outcome** — Three paths.

### Hook prompt_template

“Generate 2-3 sentences from the perspective of a user the morning after a {focus_action_human} slip. The voice is internal — what the user notices in themselves before any decision. Do not editorialize, do not preach. End on the moment before the choice between shame-spiraling and interrupting it. Voice: second person, plain, grounded.”

### Practice 1 choices (what happens internally after a lapse)

1. **“My head is doing the spiral — ‘I’m a fucking failure, I might as well keep going.’”** — Most honest. Routes forward.

1. **“I’m telling myself it didn’t really count, and I’m going to act normal.”** — Avoidance pattern. Routes forward.

1. **“I’m angry at myself but quietly. Functioning, but heavy.”** — Common middle path. Routes forward.

All three route to Practice 2. Each gets its own choice_explanation — none is “wrong”, they’re three patterns that exist.

### Practice 2 choices (one small move to interrupt the spiral)

1. **“Eat something and drink water.”** — Physical regulation. Cheap and effective.

1. **“Tell one person what happened. No speech, just one line.”** — Connection action. Disrupts shame.

1. **“Write down what happened in 2 sentences. Just the facts, not the story.”** — Externalizes the event so the brain can stop replaying it.

1. **“I’m too far gone to do anything small.”** — Routes to repair loop. The repair loop reframes this exact thinking as the abstinence violation effect.

### Module 2 outcome paths

- **Commitment**: “Write a commitment about what you’ll do the next time you have a lapse before it becomes a relapse.”

- **Tiny action now**:

- “Drink water and eat something” (no bridge_action)

- “Text a sober contact” (bridge_action: ‘send_text’, prefill_body: “Hey — slipped last night. Just wanted to tell someone. Not in crisis. Will check in later.”)

- “Write 2 sentences of what happened” (no bridge_action; could be enhanced later with notes integration)

- “Save for later”

- **Save without committing**: standard.

### Module 2 fallback text

Author focus-agnostic fallback for all 8 nodes. The fallback for the hook is the trickiest — it needs to convey morning-after-slip generically:

“It’s morning. You did a thing last night you wish you hadn’t. The body knows. The head’s already starting the spiral.”

Author the rest of the fallbacks (~20-30 words each).

### Module 2 walkthrough

Walk through end-to-end for alcohol focus. Then weed. Then codependency (different shape — what was the “slip”? People-pleasing, saying yes when meaning no, contact with an unsafe person — the module needs to make sense for codependency users too. The voice exemplar has a codependency sample for this reason).

For codependency walkthrough: verify the hook reads naturally. The “slip” for codependency might be saying yes when you meant no, or contacting someone unsafe. The Practice 2 actions might need adjustment (e.g., “drink water” makes less sense for codependency lapse than “name what just happened in one sentence”). Consider adding a focus-conditional adjustment to Practice 2.

-----

## MODULE 3: ASK FOR HELP WITHOUT A SPEECH

**module_id**: ask_for_help

**module_version**: 1.0.0

**display_name**: Ask for Help Without a Speech

**internal_track**: communication_repair

**applicable_focuses**: [‘alcohol’, ‘weed’, ‘nicotine’, ‘porn’, ‘cocaine’, ‘opioids’, ‘codependency’, ‘food’, ‘sex’, ‘gambling’]

**applicable_methods**: [] (all)

**voice_exemplar_ref**: ‘communication_repair_help’

**contraindications**: [‘suicidal_ideation’, ‘unsafe_contact’]

### What it teaches

Asking for help without making it a speech. Most users don’t reach out because they think they need to explain everything, justify themselves, prove they’re worth helping. The skill is sending a one-line message that’s enough.

### Branch shape

10 nodes:

1. **Hook** — A specific moment: the user is alone, struggling, and considering reaching out. The internal voice that says “I don’t want to be a burden” or “they don’t want to hear from me right now.” 2-3 sentences.

1. **Concept 1** — Asking for help is a skill. Most people overcomplicate it because they think the message has to be a confession or a manifesto. It doesn’t.

1. **Concept 2** — A good ask: short, specific, no apology preamble. Examples (3 short examples authored statically).

1. **Practice 1: Choose a person** — Choices are categories: a sober contact, a friend, a sponsor, a family member, “I don’t have anyone right now.” The “I don’t have anyone” choice routes to a special repair loop offering Chat or SOS as bridge.

1. **Practice 2: Identify what you actually need** — Choices: presence (“just witness me”), advice (“tell me what to do”), distraction (“talk about something else”), action (“come over”). Each is valid.

1. **Practice 3: Draft the message** — Choices show 3-4 different one-line messages, AI-generated using the focus and the chosen need. The user picks the one closest to what they’d send.

1. **Repair Loop A** — If user picked “I don’t have anyone right now” in Practice 1.

1. **Synthesis** — Paragraph referencing the choices made: who they picked, what they identified they needed, what message resonated.

1. **Outcome** — With heavy bridge-to-action options.

### Practice 1 choices

- **A sober contact** (from saved sober_contacts) — Routes forward. choice_explanation: “Someone who’s already in your recovery. Easiest to reach out to.”

- **A friend** (any) — Routes forward. choice_explanation: “Sometimes a non-recovery friend is the right call. Loneliness is what’s underneath.”

- **A sponsor / mentor** — Routes forward. choice_explanation: “If you have one. Sponsors expect this kind of contact.”

- **A family member** — Routes forward.

- **I don’t have anyone I can text right now.** — Routes to Repair Loop A. choice_explanation: “Common. There are still options — let’s look at them.”

### Practice 2 choices (what do you actually need)

- **Presence** — “I just need someone to sit with me through this. They don’t have to fix anything.”

- **Advice** — “I want someone to tell me what to do.”

- **Distraction** — “I want to talk about anything else.”

- **Action** — “I need someone to physically come over or do something concrete.”

### Practice 3: Draft the message

This is the most LLM-driven node. The prompt_template generates 3 different short messages based on the chosen need + focus.

```

prompt_template: "The user has chosen to reach out to {chosen_person_category}, and they identified they need {chosen_need_type}. Generate 3 different one-line text messages they could actually send. Each message should be under 25 words, no apology preamble, no manifesto. The messages should feel like real texts, not like lines from a recovery guide. Format as a numbered list with each message on its own line. Voice exemplar 'communication_repair_help'."

voice_constraints: "Each message under 25 words. No apologies. No 'I'm sorry to bother you.' No 'I know you're busy.' Plain, direct, real. Three messages."

```

After AI generates the three options, present them as choices in the UI.

Each choice routes to Synthesis. The user’s choice is recorded.

### Repair Loop A (no one to reach out to)

```

prompt_template: "The user said they don't have anyone they can text right now. In 2-3 sentences, acknowledge this without making it heavier. Reframe: 'Anchor itself is here, and there are crisis lines. None of them replace a person, but right now, they're real options.' Route to outcome with bridge actions to Chat and SOS."

next_node_id: "synthesis"

```

The repair loop in this module routes forward to synthesis, with the synthesis acknowledging “you didn’t have someone, and that’s part of what we worked on.” The outcome screen then offers Chat and SOS as bridge actions.

### Module 3 outcome paths

- **Commitment**: “Write a commitment about who you’ll reach out to and when.”

- **Tiny action now**:

- **“Send the text now”** (bridge_action: ‘send_text’, prefill_body: AI-generated based on choices made — pulled from the message they picked in Practice 3, pre-filled into Messages with their saved contact picker)

- **“Open Contacts”** (bridge_action: ‘open_contacts’)

- **“Copy this message”** (bridge_action: ‘copy_message’, body: AI-generated from Practice 3 choice)

- **“Save for later”** (no bridge_action)

- For users who routed through Repair Loop A: instead of “Send the text now”, show “Open Chat” and “Open SOS” bridge actions.

- **Save without committing**: standard.

### Module 3 walkthrough

Walk through end-to-end for alcohol focus. Then for codependency focus (the codependency case is interesting — asking for help is often the WORK in codependency recovery, not the support tool).

Verify Practice 3’s AI-generated messages are actually good — short, real-sounding, no apology preamble. If the LLM produces “I’m sorry to bother you, but…” style messages, the prompt_template needs hardening. Iterate until the messages feel real.

Verify the Repair Loop A path: walk through choosing “I don’t have anyone right now”. Verify the synthesis acknowledges this and the outcome screen offers Chat / SOS as bridges instead of Send Text.

Verify the Send Text bridge actually pre-fills with the message chosen at Practice 3, not a generic message.

-----

## TESTS

For BOTH modules:

1. JSON validates clean against V4.1 Prompt 2 validator.

1. State machine walks the forward path correctly.

1. State machine walks repair loop paths correctly (back to forward path or onward to synthesis depending on module).

1. Synthesis nodes include prior_choices_in_session.

1. Fallback text exists for every node.

Module 2-specific:

6. Codependency focus produces sensible hook text.

7. Practice 2’s “too far gone” choice routes to repair loop and back.

Module 3-specific:

8. Practice 3 generates 3 messages under 25 words each. (Test multiple times for consistency.)

9. Bridge-to-action ‘send_text’ pre-fills with the message picked at Practice 3.

10. Repair Loop A routes to synthesis (not back to Practice 1).

11. Outcome for repair-loop-A users shows Chat and SOS bridges, not Send Text.

## TARGETED SMOKE TEST

For Module 2 (Lapse vs Relapse):

1. Walk through for alcohol focus, picking each Practice 1 option in turn (3 separate runs).

1. Verify each option’s reframe in subsequent generation reads honestly without shaming.

1. Walk through for weed and codependency.

1. For codependency, verify the hook and Practice 2 actions feel right (drink water might not be the right move for codependency-focused users).

1. Trigger contraindication: suicidal_ideation — verify route to SOS appears.

For Module 3 (Ask for Help Without a Speech):

1. Walk through for alcohol focus, picking a sober contact in Practice 1.

1. Verify Practice 3 generates 3 short, real messages (not apologetic, not preachy).

1. Verify Send Text bridge opens Messages with the chosen message pre-filled.

1. Walk through choosing “I don’t have anyone right now” in Practice 1.

1. Verify Repair Loop A produces non-shaming text and routes to synthesis.

1. Verify outcome shows Chat and SOS bridges instead of Send Text.

1. Walk through for codependency focus — verify the module makes sense (asking for help is a recovery skill itself for codependency users).

1. Test Send Text with no saved sober_contacts — verify the empty state shows the Settings shortcut.

1. Test contraindication ‘unsafe_contact’ if mocked — verify warning shown.

## AT THE END

Report in under 400 words:

- Module file paths.

- Total bytes per module.

- Per-module walkthrough results (alcohol, weed, codependency for Module 2; alcohol, codependency for Module 3).

- Any nodes that needed multiple revisions.

- Practice 3’s message-generation quality (Module 3): are the LLM-generated messages actually good? If iteration was needed on the prompt_template, what changed?

- Bridge-to-action verification (send_text, open_contacts, copy_message all working).

- Test pass/fail summary.

- Smoke test results.

- Any architectural pain points discovered (e.g., should the focus-conditional Practice 2 in Module 2 be supported via a schema change? Document if so).

- Voice quality check: do these modules feel sponsor-adjacent? Or coaching-y / therapy-y?

- Exact next step: V4.1 Prompt 10 (Modules 4-5: Declining the Offer + What to Do After a Slip).

10

# V4.1 PROMPT 10: MODULES 4-5 — DECLINING THE OFFER + WHAT TO DO AFTER A SLIP

Author two more modules: Declining the Offer (communication & repair, social pressure scenario) and What to Do After a Slip (foundations / repair, post-event spiral interruption with care for safety).

## STACK CONTEXT

V4.1 Prompts 1-7 built infrastructure. Prompts 8-9 authored Modules 1-3. The voice exemplars and architectural patterns are proven.

These two modules are both communication/repair-shaped but different: Module 4 is a refusal scenario (the user is being offered the substance), Module 5 is a post-slip repair scenario (the user already used and needs to interrupt the spiral and take care of themselves).

Module 5 has the highest copy-sensitivity in V4.1 because shame is the dominant risk. The forbidden copy list from V4 spec must be enforced in voice_constraints on every node.

## IMPORTANT CONSTRAINTS

- Do NOT push amends, confession, or contact in Module 5 if unsafe_contact contraindication is active. (V3.7 may not detect this — but the module’s voice_constraints can still note the constraint, and the contraindication checker stub is in place.)

- Do NOT use shame copy in Module 5: no “you failed”, “you lost everything”, “start over from zero”, “you ruined your progress”. Per V5.3 Relapse Response Protocol forbidden list, applied early to Module 5.

- Do NOT teach refusal techniques in Module 4 that could increase risk in domestic_violence contexts (domestic_violence stub is in place from Prompt 7 but not yet detectable; voice_constraints can still note the concern).

- Do NOT make Module 5 longer than 5-6 minutes — post-slip users have low capacity for length.

- Do NOT do focus-specific scene differences for porn in Module 4. Per V4.1 spec, Declining the Offer is not applicable to porn (porn isn’t socially offered). Module 4’s applicable_focuses excludes porn.

- Do NOT make Module 5 imply tracker reset is the answer. The tracker reset decision is the user’s, made elsewhere.

## PRE-FLIGHT

Confirm in 4 bullets:

1. Modules 1-3 all walked through clean for at least 2 focuses each.

1. Voice exemplars communication_repair_offer.md and foundations_repair_after_slip.md exist with samples.

1. The contraindication checker handles ‘acute_intoxication’, ‘unsafe_contact’ stubs.

1. Implementation plan: branch shapes for both modules, applicable focuses, repair-loop logic.

-----

## MODULE 4: DECLINING THE OFFER

**module_id**: declining_offer

**module_version**: 1.0.0

**display_name**: Declining the Offer

**internal_track**: communication_repair

**applicable_focuses**: [‘alcohol’, ‘weed’, ‘nicotine’, ‘cocaine’, ‘opioids’]

**applicable_methods**: [] (all)

**voice_exemplar_ref**: ‘communication_repair_offer’

**contraindications**: [‘domestic_violence’, ‘acute_intoxication’]

### What it teaches

The skill of declining a socially-pressured offer without making it a confession or a dramatic exit. Most users overthink this — they want the perfect line that explains everything without revealing too much. The truth is: a short, calm, repeatable line works. Variations of “no thanks, I’m good” work. The harder skill is staying in the room after you’ve said it.

### Branch shape

10 nodes:

1. **Hook** — Specific scenario: user is at a familiar gathering. Someone offers {focus_substance_or_behavior_human}. The offer is casual but pressured.

1. **Concept 1: The myth of the perfect line** — 3-4 sentences. Most people delay this skill because they’re trying to find a line that explains everything without revealing too much. The line doesn’t matter as much as the calm.

1. **Concept 2: What actually works** — 3-4 sentences. Short. Repeatable. Doesn’t require justification. Examples: “No thanks, I’m good.” “Not tonight.” “Trying not to right now.” End on the harder part: staying in the room afterward.

1. **Practice 1: First response** — 3-4 choices.

1. **Practice 2: When they push back** — 3 choices for handling pushback.

1. **Practice 3: Staying in the room** — 3 choices.

1. **Repair Loop A** — If user picked an over-explainer in Practice 1.

1. **Repair Loop B** — If user picked a confrontational/exit response in Practice 2.

1. **Synthesis**.

1. **Outcome**.

### Practice 1 choices (first response)

- **“No thanks, I’m good.”** — Best move. Forward.

- explanation: “Short, calm, repeatable. The line everyone teaches because it works.”

- **“Not tonight.”** — Forward.

- explanation: “Even shorter. Sometimes works better — leaves no opening.”

- **“Oh, I can’t drink, I’m in recovery.”** — Routes to Repair Loop A.

- explanation: “Honest, but it tends to invite a conversation you don’t want right now. Disclosure is your call later — not under offer-pressure.”

- **“Long story, I’m not drinking these days.”** — Routes to Repair Loop A.

- explanation: “Implies a story you might not want to tell. Tends to invite questions.”

### Repair Loop A (over-explaining)

```

prompt_template: "The user picked an over-explainer response. In 2-3 sentences, reframe: justification invites pushback, and disclosure under offer-pressure is rarely a good idea. The shorter line is the move. Route to Practice 2."

next_node_id: "practice_2_pushback"

```

### Practice 2 choices (when they push back)

The setup: the offerer says “Come on, just one.” The user has to handle pushback.

- **“I’m good. Thanks though.”** — Repeat the original. Best move. Forward.

- explanation: “The boring answer is the right answer. Repetition wears down pressure.”

- **“Maybe later.”** — Routes to Repair Loop B.

- explanation: “This kicks the can. The pressure will come back, and now you’ve left a door open.”

- **“I said no.”** — Routes to Repair Loop B.

- explanation: “Confrontational. Sometimes necessary, but escalates the social moment unnecessarily here.”

### Repair Loop B (exit/confrontation)

```

prompt_template: "The user picked an exit or confrontation response. In 2-3 sentences, note: sometimes this is exactly right (when offerer is genuinely problematic). But for casual social pressure, repeating the calm 'no' is the move. Route back to Practice 2 to try the calm repeat."

next_node_id: "practice_2_pushback"

```

### Practice 3 choices (staying in the room)

- **“Stay engaged in the conversation. The moment passes.”** — Best move. Forward.

- **“Find a casual exit — bathroom, refill water, step outside briefly.”** — Also valid. Forward.

- **“Leave the gathering.”** — Sometimes the right call, sometimes overreaction. Forward with a note in choice_explanation.

All three route to Synthesis.

### Module 4 outcome

- **Commitment**: “Write a commitment about your default decline line — what’s yours?”

- **Tiny action now**:

- **“Save ‘No thanks, I’m good’ as my default line”** (no bridge_action; could store as a stable_profile.pinned_facts entry — small extension)

- **“Text a sober contact about something coming up”** (bridge_action: ‘send_text’, prefill_body: “Have a thing this weekend where I’ll be around drinking. Going to use the line. Wanted to tell you ahead.”)

- **“Save for later”**

- **Save without committing**.

### Module 4 walkthrough

Walk through alcohol → weed → nicotine. All three should produce coherent scenarios. The substance changes; the social dynamic doesn’t.

Verify the contraindication ‘domestic_violence’ stub: even though it’s not detectable in V3.7, verify that the module’s voice_constraints note that refusal language must not encourage refusal in physical-risk contexts. The voice_constraints text might say: “Do not encourage standing your ground if doing so could escalate physical risk. The default assumption is the user is in a benign social setting.”

Verify Practice 2’s repeat-the-calm-no actually generates a calm reframe and routes back, not a “no, you have to be more firm” reframe. The voice should match the exemplar.

-----

## MODULE 5: WHAT TO DO AFTER A SLIP

**module_id**: after_slip

**module_version**: 1.0.0

**display_name**: What to Do After a Slip

**internal_track**: foundations

**applicable_focuses**: [‘alcohol’, ‘weed’, ‘nicotine’, ‘porn’, ‘cocaine’, ‘opioids’, ‘codependency’, ‘food’, ‘sex’, ‘gambling’]

**applicable_methods**: [] (all)

**voice_exemplar_ref**: ‘foundations_repair_after_slip’

**contraindications**: [‘suicidal_ideation’, ‘unsafe_contact’, ‘severe_withdrawal’]

### What it teaches

What to actually do in the hours after a slip. Not amends. Not confession. Not the recovery program homework. The basics: physical safety, getting out of the spiral, telling one person, deciding about tracker reset later (not now). The module’s main job is to interrupt the shame spiral and route to one small repair action.

### Branch shape

8 nodes (kept short — post-slip users have low capacity):

1. **Hook** — Concrete moment: the user is in the morning or hours after using/acting, body and head still processing. 2-3 sentences.

1. **Concept 1: First — physical** — 3-4 sentences. Before you do anything mental, take care of the body. Water. Food. Don’t drive. Don’t make decisions. Sleep if you can. (Conditional addendum: for alcohol/benzo/opioid focus, add “If you’re in withdrawal, that’s medical — see a doctor or call SAMHSA. Don’t tough it out alone.”)

1. **Concept 2: The shame spiral is the real risk** — 3-4 sentences. The slip happened. The thing that turns one slip into a relapse is the spiral. Naming it interrupts it.

1. **Practice 1: What’s happening for you right now** — 3 choices. Same shape as Module 2’s Practice 1 (shame spiral / minimization / quiet anger).

1. **Practice 2: One person, one line** — 3 choices for who and what to tell.

1. **Practice 3: One repair action for the next hour** — 3 choices.

1. **Synthesis**.

1. **Outcome**.

### Hook prompt_template

“Generate 2-3 sentences from the perspective of a user in the hours after a {focus_action_human} slip. The voice is internal — what they’re noticing in their body and head before any decision. Do not editorialize. Do not preach. Do not use the words ‘failed’, ‘lost’, ‘ruined’, ‘zero’. End on the moment before they decide what to do next. Voice: second person, plain, grounded. Reference exemplar ‘foundations_repair_after_slip’.”

### Voice constraints note (CRITICAL for Module 5)

Every node’s voice_constraints field includes the forbidden copy list:

“FORBIDDEN: ‘You failed.’ ‘You lost everything.’ ‘Start over from zero.’ ‘You ruined your progress.’ ‘Relapse risk detected.’ ‘This time will be different.’ These exact phrases and their variants must not appear in generated text. Use grounded, non-shaming language only. Reference exemplar ‘foundations_repair_after_slip’.”

### Practice 1 choices (what’s happening internally)

- **“My head is spiraling — I’m a failure, I should just keep going.”** — Forward.

- **“I’m minimizing it — telling myself it didn’t really happen / didn’t really count.”** — Forward.

- **“Quiet anger at myself. Functioning, but heavy.”** — Forward.

All three route to Practice 2. The follow-up acknowledges each pattern non-shaming.

### Practice 2 choices (one person, one line)

- **A sober contact (one line, no speech)** (bridge to text): forward.

- **My sponsor / mentor**: forward.

- **A friend who knows about my recovery**: forward.

- **Open Anchor Chat**: forward.

- **No one yet — I need a few hours first**: forward (this is valid; acknowledge it).

### Practice 3 choices (one repair action for the next hour)

- **“Eat something and drink water.”** — Most universal.

- **“Take a shower or wash my face.”** — Embodied repair.

- **“Sleep if I can.”** — Common right answer; the body needs reset.

- **“Sit and stew.”** — Routes to repair loop… but wait, Module 5 is short and shouldn’t have repair loops. Make this choice route forward with a non-shaming reframe in the next node’s prompt that acknowledges this is a valid choice but flags that sitting and stewing tends to extend the spiral.

Actually: keep Module 5 to 8 nodes total without any repair loop. The “sit and stew” choice routes forward to synthesis with the synthesis acknowledging it. This keeps the module short (a deliberate design choice for post-slip capacity).

### Module 5 outcome

- **Commitment**: “Write a commitment about what you’ll do the next time, before you reach for it.”

- **Tiny action now**:

- **“Drink water and eat something”**.

- **“Text a sober contact”** (bridge_action: ‘send_text’, prefill_body: AI-generated short message based on the user’s choices, e.g., “Hey — slipped last night. Just wanted to tell someone. Not in crisis. Will follow up later.”)

- **“Open SOS”** (for users where contraindication routing might not be clean).

- **“Save for later”**.

- **Save without committing**.

The tracker-reset decision is NOT in this module. The module ends with self-care and one small action. Tracker reset is a separate flow (V5.3 Relapse Response Protocol).

### Module 5 walkthrough

CRITICAL: walk through for alcohol focus first. Before any other focuses, verify NO forbidden copy appears in any generated node text. Run synthesis multiple times (regenerate via “this doesn’t fit my situation” affordance) to test consistency. If any forbidden phrase ever appears, harden the voice_constraints further.

Then walk through for porn focus and codependency focus. The “slip” for codependency is different (saying yes when meaning no, contact with unsafe person). The hook needs to handle this — either via focus-conditional prompt_template or by a small focus_specific_hook field.

For porn focus, verify the hook reads naturally without crassness or judgment.

Verify contraindication routing: with suicidal_ideation flag active, the module shows the route screen instead of launching.

-----

## TESTS

For BOTH modules:

1. JSON validates clean.

1. State machine walks forward path correctly.

1. State machine handles repair loops (Module 4 only — Module 5 has none by design).

1. Synthesis includes prior_choices_in_session.

1. Fallbacks present for all nodes.

Module 4-specific:

6. applicable_focuses excludes porn (porn isn’t offered socially).

7. Repair Loop A → Practice 2 forward path resumes correctly.

8. Repair Loop B routes back to Practice 2 (not to synthesis).

Module 5-specific:

9. Voice eval (manual): generate hook 5x, generate concepts 5x — verify NO forbidden phrases.

10. Conditional withdrawal addendum: alcohol/opioid/benzo focus shows the medical addendum in concept 1.

11. Contraindication ‘suicidal_ideation’ routes to SOS, blocks module.

12. Tracker reset is NOT mentioned in any node text or outcome.

## TARGETED SMOKE TEST

Module 4:

1. Walk through for alcohol. Verify all 4 Practice 1 choices route correctly.

1. Trigger Repair Loop A by picking an over-explainer. Verify reframe is non-judgmental.

1. Trigger Repair Loop B by picking an exit response in Practice 2.

1. Reach synthesis. Verify the paragraph references actual choices.

1. Reach outcome. Test “Save default line” → verify it saves to stable_profile.pinned_facts (or wherever).

1. Test bridge-to-action send_text → Messages opens with prefill.

1. Walk through for weed and nicotine.

Module 5:

1. Walk through for alcohol. CHECK GENERATED TEXT IN EVERY NODE for forbidden phrases.

1. Test all three Practice 1 patterns. Verify each gets non-shaming continuation.

1. Test “No one yet” choice in Practice 2. Verify it’s acknowledged as valid.

1. Test “Sit and stew” choice in Practice 3. Verify the synthesis flags this gently without shaming.

1. Reach outcome. Test bridge-to-action send_text — verify prefill is short, non-confessional.

1. Walk through for porn focus. Verify hook reads naturally.

1. Walk through for codependency focus. Verify hook handles the relational “slip” pattern.

1. Trigger contraindication: suicidal_ideation. Verify route screen.

1. Trigger contraindication: severe_withdrawal. Verify route screen.

## AT THE END

Report in under 400 words:

- Module file paths.

- Per-module walkthrough results.

- Forbidden copy verification for Module 5: zero occurrences across multiple generations? Or did any leak through?

- If any forbidden copy leaked, what was changed in voice_constraints to prevent recurrence.

- Tracker-reset confirmation: NOT mentioned in Module 5.

- Module 4 applicable_focuses verified to exclude porn.

- Bridge-to-action verification for both modules.

- Test pass/fail summary.

- Any architectural pain points (e.g., how was focus-conditional handled for Module 5’s codependency slip case?).

- Voice quality assessment.

- Exact next step: V4.1 Prompt 11 (Module 6: Holding a No When Asked — codependency POC).

11

# V4.1 PROMPT 11: MODULE 6 — HOLDING A NO WHEN ASKED (CODEPENDENCY POC)

Author the codependency proof-of-concept module. Different shape from Module 4 (refusal of a request, not refusal of an offer). Different applicable_focuses (codependency only). Different contraindication concerns (domestic violence is the most sensitive flag). This module’s job is to prove the V4.1 format extends to relational recovery before V5+ commits to a full codependency track.

## STACK CONTEXT

V4.1 Prompts 1-7 built infrastructure. Prompts 8-10 authored Modules 1-5 (substance-side focuses + foundations). Module 6 is the only codependency-focused module in V4.1.

Codependency is a contested term in some recovery communities. The module avoids using “codependency” in user-facing dialogue. The internal_track is ‘codependency’ for organization, but the user sees scenario-shaped content, not labeled categories.

The voice exemplar codependency_holding_no.md was authored in Prompt 1 with samples for codependency only.

## IMPORTANT CONSTRAINTS

- Do NOT use the word “codependency” in any user-facing copy (hook, concept, choices, repair loops, synthesis, outcome). The term is contested.

- Do NOT use language that implies the user is broken, sick, or has a “personality issue.” Codependency framings vary widely.

- Do NOT encourage refusal in contexts where saying no could escalate physical risk. The contraindication ‘domestic_violence’ is declared. Even though detection is a stub in V3.7, the voice_constraints on every node note the concern.

- Do NOT pathologize the asker. The module teaches the user to hold their own no, not to label the other person.

- Do NOT push specific recovery programs (CoDA, Al-Anon, etc.). Mention them in concept 1 as options, neutrally.

- Do NOT make the module bigger than 7 minutes (3-min floor, 7-min ceiling). 9 nodes max.

- Do NOT use therapy/coaching cadence. Stay in the V4.1 sponsor-adjacent voice.

- Do NOT bypass the voice exemplar — every prompt_template references ‘codependency_holding_no’.

## PRE-FLIGHT

Confirm in 5 bullets:

1. Voice exemplar codependency_holding_no.md exists with codependency samples.

1. Modules 1-5 walked through clean and shipped successfully.

1. The contraindication checker (V4.1 Prompt 7) handles ‘domestic_violence’ and ‘unsafe_contact’ (stubs returning matched=false in V3.7, but the framework exists).

1. The focus-to-variable resolver handles ‘codependency’ (returns “a request you don’t want to say yes to” for focus_substance_or_behavior_human).

1. Implementation plan: branch shape, applicable_focuses, the specific scenarios chosen.

-----

## MODULE OVERVIEW

**module_id**: holding_no

**module_version**: 1.0.0

**display_name**: Holding a No When Asked

**internal_track**: codependency

**applicable_focuses**: [‘codependency’]

**applicable_methods**: [] (all)

**voice_exemplar_ref**: ‘codependency_holding_no’

**estimated_minutes**: { floor: 3, ceiling: 7 }

**contraindications**: [‘domestic_violence’, ‘unsafe_contact’, ‘suicidal_ideation’]

### What it teaches

The skill of saying no — and holding it — when someone asks for something the user knows they shouldn’t say yes to. The hard part isn’t the “no” itself; it’s holding it through the pushback, the guilt, and the urge to repair the discomfort by reversing.

This is RELATIONAL refusal, not OFFER refusal (Module 4 covers offer refusal). The user isn’t being offered a substance; they’re being asked for something — time, attention, a favor, a return to a pattern, money, a yes they don’t want to give.

### Branch shape

9 nodes:

1. **Hook** — A specific moment: someone the user has a complicated relationship with asks them for something. The internal experience: the immediate pull to say yes, the body recognizing it before the brain.

1. **Concept 1: The pull is the practice** — 4-5 sentences. The pull to say yes when you mean no is the body asking for an old pattern. The skill is noticing it without acting on it. (Mention CoDA, Al-Anon, therapy as resources here, neutrally — one sentence.)

1. **Concept 2: A no without a story** — 3-4 sentences. The most common mistake is over-explaining the no. The longer the explanation, the more handles for negotiation. A short, calm no is harder to challenge — and harder for you to retract.

1. **Practice 1: The first no** — 4 choices for how to respond.

1. **Practice 2: The pushback** — 3 choices for how to handle when the asker doesn’t accept.

1. **Repair Loop A** — If user picked an over-explanation in Practice 1.

1. **Practice 3: After the no — staying with the discomfort** — 3 choices.

1. **Synthesis**.

1. **Outcome**.

### The example scenario

To keep the module concrete, the hook uses one canonical scenario type: a family member or close person asks the user for something the user knows isn’t healthy to say yes to. The specific ask is generated by the AI per session, but it’s grounded in this category. Examples (all generated by AI, not statically authored):

- A parent asking the user to mediate a fight between siblings (again).

- An ex asking to “just talk for a minute”.

- A friend asking the user to lie for them to a third party.

- A family member asking for money the user doesn’t have / shouldn’t lend.

- An adult sibling asking the user to take responsibility for the sibling’s child / pet / problem.

The module doesn’t push the user toward any specific relational answer. It rehearses the SKILL of holding the no — the user’s own decision about what they actually want to say no to is theirs.

-----

## NODE-BY-NODE AUTHORING

### Node 1: Hook

```

prompt_template: "Generate 2-3 sentences describing a specific moment where someone the user has a complicated relationship with asks them for something. Pick one of these scenario types and generate the specific ask: parent asking for mediation, ex asking to talk, friend asking the user to lie, family member asking for money, sibling asking for responsibility-shifting. The voice is internal — what the user notices in their body before any decision. The pull to say yes lands first. End on the moment before they decide what to do. Voice: second person, plain, grounded. Reference voice exemplar 'codependency_holding_no'."

voice_constraints: "Max 3 sentences. Second person. No labeling the asker. No therapy cadence. Reference exemplar 'codependency_holding_no'. Avoid 'manipulator', 'narcissist', 'toxic'."

next_node_id: "concept_1"

fallback_default_text: "Your phone buzzes. It's the message you knew was coming, asking for the thing you've been hoping they wouldn't ask for. Your stomach moves before your head does."

```

### Node 2: Concept 1 — The pull is the practice

```

prompt_template: "In 4-5 sentences, explain that the pull to say yes when you mean no is the body recognizing an old pattern. The skill being practiced is noticing the pull without acting on it. Mention CoDA, Al-Anon, and therapy as one-sentence options for users wanting more support. Plain language. No coaching cadence. Reference voice exemplar 'codependency_holding_no'."

voice_constraints: "Max 5 sentences. No coaching cadence. Mention recovery resources only neutrally — do not push any specific program. Voice exemplar 'codependency_holding_no'."

next_node_id: "concept_2"

fallback_default_text: "When someone asks you for something you know isn't right to say yes to, your body answers before your head does. The pull to say yes is old — it's the pattern you learned. The skill today is noticing the pull without acting on it. CoDA, Al-Anon, therapy — these exist if you want more support. None of them replace the work of holding your own no when it lands."

```

### Node 3: Concept 2 — A no without a story

```

prompt_template: "In 3-4 sentences, explain: the most common mistake is over-explaining the no. The longer the explanation, the more handles for negotiation. A short, calm no is harder to challenge and harder to retract. End on the harder part: the discomfort doesn't disappear after the no — it shows up. Voice exemplar 'codependency_holding_no'."

voice_constraints: "Max 4 sentences. Plain. Voice exemplar 'codependency_holding_no'."

next_node_id: "practice_1_first_no"

fallback_default_text: "The most common mistake is over-explaining the no. The longer your explanation, the more handles you give them to negotiate. A short, calm no is harder to challenge — and harder for you to take back. The discomfort doesn't disappear after the no. It shows up. That's what we practice next."

```

### Node 4: Practice 1 — The first no

```

prompt_template: "Continue the scene from the hook. The asker has just asked. The user is about to respond. In 1-2 sentences, set up the moment: the body is pulling toward yes, the head is somewhere else. End with the question to the reader: 'What's the first response?' Then the choices appear separately. Voice exemplar 'codependency_holding_no'."

voice_constraints: "Max 2 sentences before question. Voice exemplar 'codependency_holding_no'."

choices:

- id: "no_short"

text: "I can't do that."

explanation: "Short, calm, no story. The hardest version because it leaves nothing to argue with."

next_node_id: "practice_2_pushback"

is_repair_route: false

- id: "no_no_explain"

text: "No, that doesn't work for me."

explanation: "Clear and grounded. Doesn't justify, doesn't apologize."

next_node_id: "practice_2_pushback"

is_repair_route: false

- id: "no_with_reasons"

text: "I really wish I could, but I'm so busy and stressed and you wouldn't believe what's been going on..."

explanation: "Over-explanation. Each detail becomes a handle the asker can grab to negotiate."

next_node_id: "repair_loop_a"

is_repair_route: true

- id: "no_maybe"

text: "Maybe — let me think about it."

explanation: "Soft no that's actually a delayed yes. The pull won. We'll look at why."

next_node_id: "repair_loop_a"

is_repair_route: true

fallback_default_text: "The pull is there. Your stomach knows. Your head is trying to find the right words. What's the first response you give?"

```

### Node 5: Repair Loop A

```

prompt_template: "The user picked an over-explanation or a soft 'maybe'. In 2-3 sentences, reframe without shaming: this is the pattern the body remembers. The work isn't to never feel the pull; it's to notice it and choose differently. Route forward to Practice 2."

voice_constraints: "Max 3 sentences. No shaming. No labeling. Voice exemplar 'codependency_holding_no'."

next_node_id: "practice_2_pushback"

fallback_default_text: "That's the pattern your body knows. It's not that you failed — it's that the pull is real, and the old answer arrived first. The work isn't to never feel the pull. It's to notice it and choose differently. Let's see what happens next."

```

### Node 6: Practice 2 — The pushback

```

prompt_template: "Generate 2-3 sentences continuing the scene. The asker has not accepted the no. They're pushing back — guilt, escalation, or a softer 'come on'. Pick one based on the scenario type. End with the question: 'What do you do now?'. Voice: plain, grounded. Voice exemplar 'codependency_holding_no'."

voice_constraints: "Max 3 sentences before question. Voice exemplar 'codependency_holding_no'."

choices:

- id: "pushback_repeat"

text: "Repeat the same line, calmly. 'I can't do that.'"

explanation: "The boring move that works. Repetition wears down pressure."

next_node_id: "practice_3_discomfort"

is_repair_route: false

- id: "pushback_acknowledge"

text: "Acknowledge their feeling, hold the no. 'I can hear this is hard. The answer is still no.'"

explanation: "Empathy without retraction. Harder than it sounds, but it works."

next_node_id: "practice_3_discomfort"

is_repair_route: false

- id: "pushback_explain_more"

text: "Try to explain more, hoping they'll understand."

explanation: "Explaining more invites more pushback. The pattern this module is interrupting."

next_node_id: "practice_3_discomfort"

is_repair_route: false

```

(Note: even the “wrong” choice routes forward, not to a repair loop. Module 6 is intentionally structured to avoid bouncing the user back too many times — the repair work is in the synthesis, where choices are reflected back honestly.)

```

fallback_default_text: "They didn't accept it. The push is here — guilt, escalation, the softer 'come on'. The pull is back, stronger now. What do you do?"

```

### Node 7: Practice 3 — After the no, staying with the discomfort

```

prompt_template: "The user has held the no through the pushback (or attempted to). The conversation is winding down or the asker has left. Now the harder part begins — the internal discomfort that follows holding a no with someone you love or fear. In 2 sentences, describe this internal experience without labeling it. End with the question: 'What's the move for the next hour?' Voice exemplar 'codependency_holding_no'."

voice_constraints: "Max 2 sentences before question. No labeling. Voice exemplar 'codependency_holding_no'."

choices:

- id: "after_self_care"

text: "Take care of yourself physically. Water, food, walk."

explanation: "Embodied repair. The body absorbs the discomfort; help it through."

next_node_id: "synthesis"

is_repair_route: false

- id: "after_anchor_friend"

text: "Tell one person you held the no. Just one line, no story."

explanation: "Witness reduces the pull to retract. You don't need to perform recovery — just say it."

next_node_id: "synthesis"

is_repair_route: false

- id: "after_reach_back"

text: "Reach back out and take it back. The discomfort is too much."

explanation: "This is the move that undoes everything. We won't shame you for it — we'll name what's happening."

next_node_id: "synthesis"

is_repair_route: false

fallback_default_text: "They're gone, or the conversation is over. Now the harder part — the discomfort of having held the no. What's the move for the next hour?"

```

The “reach back out” choice routes to synthesis, not a repair loop, because the synthesis can honestly acknowledge: “you noticed the pull to retract. Whether you acted on it or not, naming it is the practice.”

### Node 8: Synthesis

```

prompt_template: "Generate one paragraph (3-5 sentences) summarizing what the user worked through. Reference what they actually picked: 1) what they noticed when the ask first arrived, 2) how they responded, 3) what they did with the discomfort after. Acknowledge if they picked the over-explanation or the take-it-back choice — non-shaming, just honest. The synthesis names the pattern, names the practice, names where the work continues. Voice exemplar 'codependency_holding_no'. Plain, grounded. Second person."

voice_constraints: "Max 5 sentences. No labeling. No therapy cadence. Voice exemplar 'codependency_holding_no'."

next_node_id: "outcome"

fallback_default_text: "You felt the pull and you noticed it. You held the no — or you saw yourself not holding it, which is also the practice. The discomfort that comes after holding a no is part of the work, not a sign you did it wrong. The pattern your body knows isn't going to disappear today, but you're learning to choose around it."

```

### Node 9: Outcome

```

node_type: outcome

outcome_options:

- option_id: "commit_default_no"

option_label: "Write a commitment about your default no when this comes up next."

option_type: "commitment"

- option_id: "tiny_action"

option_label: "Pick a small action for right now."

option_type: "tiny_action"

(sub-options shown in outcome screen UI):

- "Drink water and take a walk." (no bridge_action)

- "Text someone — one line — that you held a no." (bridge_action: 'send_text', prefill_body: "Held a no with [name] today. Just wanted to tell someone.")

- "Open Anchor Chat." (no bridge_action; opens Chat surface)

- "Save for later." (no bridge_action)

- option_id: "save_only"

option_label: "Save without committing. I'll come back to it."

option_type: "save_only"

```

-----

## VOICE GUARDRAILS (CRITICAL FOR THIS MODULE)

Every node’s voice_constraints includes the codependency-specific forbidden phrases:

“FORBIDDEN: ‘codependent’, ‘codependency’, ‘narcissist’, ‘toxic’, ‘manipulator’, ‘gaslighting’, ‘enabler’. Do not pathologize the asker. Do not pathologize the user. Do not name the relationship dynamic — describe the moment instead. Reference exemplar ‘codependency_holding_no’.”

The module rehearses the skill in plain language. The user’s framing of their own situation is theirs.

-----

## CONTRAINDICATION HANDLING

The module declares ‘domestic_violence’ and ‘unsafe_contact’. V3.7 cannot detect these reliably (per V4.1 Prompt 7, both are stubs). For V4.1, the contraindication checker returns matched=false for these.

To still surface the safety concern, the Concept 1 node MUST include a single sentence acknowledging the limit: “If saying no in your situation could put you in physical danger, this module isn’t the right tool — please reach out to a domestic violence resource, like the National DV Hotline at 1-800-799-7233.”

This is a hard-coded sentence in the prompt_template for Concept 1 (focus-conditional in code: only included when applicable_focuses includes ‘codependency’). It’s not user-personalized; it’s a static safety note.

The agent should verify this sentence appears in every Concept 1 generation. If it doesn’t, harden the prompt_template.

-----

## ALCOHOL-FOCUS SAFETY: NOT APPLICABLE

The module’s applicable_focuses is [‘codependency’] only. The need-state recommender from V4.1 Prompt 4 will only show this module to users whose recovery_focus includes ‘codependency’.

If a user has BOTH codependency and a substance focus, this module appears alongside the substance modules. The user picks the relevant one in the moment.

-----

## TESTS

Add tests:

1. holding_no_v1_0_0.json validates clean against the V4.1 Prompt 2 validator.

1. State machine: walking forward path (no repair loop) produces expected sequence.

1. State machine: Repair Loop A → Practice 2 (forward).

1. State machine: synthesis includes prior_choices_in_session.

1. Voice eval: generate hook 5x, search output for “codependent”, “narcissist”, “toxic”, “manipulator”, “gaslighting”, “enabler”. Zero matches required.

1. Voice eval: generate concept 1 5x. Verify the DV hotline sentence appears in 5/5 generations.

1. Need-state recommender: ‘ask_help_repair’ need-state for codependency-only user includes holding_no.

1. Need-state recommender: ‘urge’ need-state for codependency-only user does NOT include holding_no.

1. Module’s applicable_focuses == [‘codependency’] (not [‘codependency’, ‘alcohol’, …]).

1. Bridge-to-action send_text in outcome: prefill body uses generic placeholder (no real name auto-filled — user adds the name themselves in Messages).

## TARGETED SMOKE TEST

1. Open Practice → set user recovery_focus to [‘codependency’] → tap “I need to ask for help or repair something” → verify holding_no appears as recommended module.

1. Start the module. Verify hook generates a specific scenario (mediation, ex, lying, money, sibling) and reads naturally.

1. Verify concept 1 includes the DV hotline sentence verbatim.

1. Walk through Practice 1 picking the over-explanation choice. Verify Repair Loop A reframes without shaming and routes forward.

1. Walk through Practice 2’s three choices in separate runs.

1. Walk through Practice 3 picking each of the three choices.

1. Reach synthesis. Verify the paragraph references actual choices including (if picked) the over-explanation and the reach-back-out moves, framed as the practice.

1. Reach outcome. Test all three paths.

1. Test bridge-to-action ‘send_text’ in tiny action: verify Messages opens with prefill “Held a no with [name] today. Just wanted to tell someone.” with [name] as a placeholder, not a real name.

1. Switch to dual-focus user (alcohol + codependency). Re-open need-state. Verify both substance modules and codependency module shown for relevant need-states.

1. Switch to substance-only user (alcohol). Re-open need-state. Verify holding_no does NOT appear.

1. Trigger contraindication: suicidal_ideation. Verify route screen.

1. Manually inspect every generated node text: search for forbidden phrases. Run 10+ regenerations to confirm voice consistency.

## AT THE END

Report in under 400 words:

- Module file path: server/practice/modules/holding_no_v1_0_0.json

- Total module byte count.

- Walkthrough results for codependency focus.

- Walkthrough result for dual-focus user (codependency + substance).

- Voice eval results: zero forbidden phrase occurrences across 10+ generations? Or did any leak?

- DV hotline sentence: appears in 5/5 concept 1 generations? If not, what was hardened?

- Honest assessment: does the module prove the V4.1 architecture extends cleanly to relational recovery? Or did the format strain in places?

- Any architectural changes needed for the codependency case (e.g., the “wrong” choice routing forward instead of to repair loop — does this need to be a schema option, or is it just an authoring decision per module?).

- Recommendation for V5+ codependency track: is the format ready, or does it need significant adjustment?

- Voice quality assessment.

- Exact next step: V4.1 Prompt 12 (Voice eval + full V4.1 smoke suite).

12

# V4.1 PROMPT 12: VOICE EVAL + FULL V4.1 SMOKE SUITE

The closing prompt for V4.1. Build the voice eval matrix that covers all six modules across applicable focuses, run the full smoke suite covering every behavior V4.1 introduced, save baseline outputs, and produce a definitive ship/no-ship report.

## STACK CONTEXT

V4.1 Prompts 1-11 built infrastructure and authored all six modules. This prompt is the final verification before V4.1 deploys.

V4 Prompt 6 established the voice eval pattern (16-case matrix saved to baseline file, manual review required) and the full smoke suite pattern (10 numbered suites, each with concrete pass criteria). V4.1’s eval mirrors that structure but expands coverage to module-shaped behavior.

This is verification work — no new feature code. Some scaffolding code is fine (the eval runner script, fixture data setup). The deliverable is the report and the saved baseline.

## IMPORTANT CONSTRAINTS

- Do NOT skip running every cell in the voice eval matrix.

- Do NOT auto-pass voice eval based on script logic alone. The agent must produce the outputs and the human (or a follow-up reviewer) must read them. This prompt’s report should clearly mark which cases were programmatically verified vs which need human review.

- Do NOT modify any module to make it pass eval. If a module fails voice eval, that’s a finding for the report, not a justification for stealth-editing the module JSON.

- Do NOT add new features to V4.1 in this prompt.

- Do NOT modify schemas. V4.1 schemas are locked.

- Do NOT skip the contraindication suite. Every contraindication declared must be tested (for the ones that are V3.7-detectable).

- Do NOT silently soften the success metric. The 70%/50% target is frozen for the 90-day post-launch eval window per V4.1 spec — this prompt establishes baseline; it doesn’t measure against the success metric (that’s a 90-day post-launch activity).

## PRE-FLIGHT

Confirm in 6 bullets:

1. All six modules exist as JSON files and validate clean.

1. The fixture metadata file from V4.1 Prompt 4 has been replaced with real loadAllModules() output.

1. All V4.1 screens (need-state, library, module session, synthesis, outcome, rating) work end-to-end.

1. Settings additions, contraindication checker, and onboarding update from V4.1 Prompt 7 are functional.

1. The V4 voice eval baseline file exists (from V4 Prompt 6) for comparison: V4.1 should not regress V4 chat or check-in voice.

1. Implementation plan: voice eval runner, smoke suite test cases, baseline file structure.

-----

## VOICE EVAL MATRIX

The matrix covers six modules × applicable focuses. For modules that apply to multiple focuses, the eval runs the module per focus. The matrix is roughly 24 cases.

### Cases (module × focus):

```

Module 1 (urge_20_min):

- alcohol

- weed

- nicotine

- porn

Module 2 (lapse_vs_relapse):

- alcohol

- weed

- codependency

- food (note: V4.1 lists this in applicable_focuses but no full focus coverage; verify the resolver and exemplar handle it)

Module 3 (ask_for_help):

- alcohol

- codependency

Module 4 (declining_offer):

- alcohol

- weed

- nicotine

Module 5 (after_slip):

- alcohol

- porn

- codependency

Module 6 (holding_no):

- codependency

```

Plus three experience-level variations to verify V4 conditioning carries through to practice:

```

Experience-level matrix (run on Module 1, alcohol focus only):

- first_attempt

- returning

- chronic_relapse

- long_term_stable

```

Total cases: ~21 module-focus + 4 experience-level = 25 cases.

### What each case generates

For each case, the eval script:

1. Sets up a fixture user with the appropriate recovery_focus, experience_level, and other relevant fields.

1. Walks the module from hook → concept → first practice node (3 nodes total).

1. Captures the LLM-generated text for each of the 3 nodes.

1. Saves the captured text to the baseline file.

1. Programmatically checks for:

- Forbidden phrases (from V4 forbidden list + V4.1 module-specific forbidden lists).

- Phone numbers (none should appear).

- Recovery phase names (none should appear).

- For Module 5 specifically: shame copy (“you failed”, “you lost everything”, “ruined your progress”, “start over from zero”, “this time will be different”, “relapse risk detected”).

- For Module 6 specifically: pathologizing language (“codependent”, “codependency”, “narcissist”, “toxic”, “manipulator”, “gaslighting”, “enabler”).

- For Module 6 Concept 1 specifically: the DV hotline sentence MUST appear.

1. Flags cases where programmatic checks fail (these are clear failures, no human review needed for those).

1. For all cases (including programmatic-pass), flags for human voice review.

### Baseline file format

Save to `eval/v41_voice_baseline.json`:

```json

{

"v41_voice_baseline_run_date": "ISO timestamp",

"model_version": "claude-sonnet-X.Y or whatever LLM",

"cases": [

{

"case_id": "module1_alcohol_returning",

"module_id": "urge_20_min",

"focus": "alcohol",

"experience_level": "returning",

"node_outputs": {

"hook": "...generated text...",

"concept": "...generated text...",

"practice_1": "...generated text..."

},

"programmatic_checks": {

"forbidden_phrases": [],     // empty = pass

"phone_numbers": [],

"recovery_phase_names": [],

"module_specific_forbidden": []

},

"human_review_status": "pending",

"human_review_notes": ""

},

...

]

}

```

After the eval runs, the file has 25 entries. The agent reviews programmatic results and flags any failures for the report. Human review is marked pending — the agent does NOT mark cases as “reviewed” without actual human review.

### Eval runner

Add a script: `scripts/run_v41_voice_eval.ts` (or similar). It:

- Loads all modules.

- Iterates the matrix.

- For each case, calls the orchestrator’s startNewSession then advances 3 nodes, capturing each node’s generated text.

- Saves to the baseline file.

- Prints a summary: total cases, programmatic pass count, programmatic fail count.

The runner is idempotent. Re-running overwrites the baseline. Optionally support `--save-as filename` to save additional baselines for comparison.

### Output review process

After running, the agent:

1. Lists every case where programmatic checks failed, with the failing phrase / pattern and the offending node text.

1. For cases with programmatic pass: produce a brief summary of voice quality observations across all 25 cases. Look for systematic issues (e.g., “Module 4 hook tends to over-describe the social setting” or “Module 5 synthesis sometimes uses second-person past tense awkwardly”). These are observational; they may or may not warrant module revisions.

The report does NOT recommend module changes inline. It surfaces issues for the user to decide whether to revise. Module changes are out of scope for this prompt.

-----

## FULL V4.1 SMOKE SUITE

10 numbered suites, each with concrete pass criteria. The suite verifies behavior end-to-end.

### Suite 1: Practice surface assembly

- 1.1: surface=‘practice’ produces 7-section prompt (6 standard + module context).

- 1.2: surface=‘chat’ remains byte-identical to V4 baseline.

- 1.3: surface=‘checkin_synthesis’ remains byte-identical to V4 baseline.

- 1.4: Practice prompt for first_attempt user contains first_attempt experience framing.

- 1.5: Practice prompt for chronic_relapse user contains chronic_relapse experience framing.

- 1.6: Practice prompt with phone numbers in stable_profile.sober_contacts produces output with no phone numbers.

Pass: all 6 cases assert clean.

### Suite 2: State machine and module loading

- 2.1: All six real modules load and validate.

- 2.2: State machine walks each module’s forward path without errors.

- 2.3: State machine handles repair loops in Modules 1, 4, 6.

- 2.4: Pause/resume preserves state across server restart.

- 2.5: Resume on pinned module_version works even after newer version is added.

### Suite 3: Database persistence

- 3.1: startSession creates row with correct fields.

- 3.2: recordChoice cascades on session deletion.

- 3.3: completeSession with synthesis_text=’’ stores NULL.

- 3.4: completeSession with synthesis_text=‘real text’ stores text.

- 3.5: deleteAllPracticeData removes all rows but leaves user_memory and check_ins intact.

- 3.6: deletePracticeDataForFocus removes only matching focus.

- 3.7: exportPracticeData returns structured JSON with all expected fields.

- 3.8: event_log gains new types (started, completed, paused, rated_immediate) without exceeding 90-entry cap.

### Suite 4: Need-state entry and acute-distress detection

- 4.1: Practice Quick Action visible on Home.

- 4.2: Need-state screen shows 6 options.

- 4.3: Need-state recommender filters by recovery_focus correctly (codependency-only user, substance-only user, dual-focus user).

- 4.4: Acute-distress detection fires on recent risk classification, shows stabilization step.

- 4.5: Acute-distress fail-open: classifier error → no stabilization step shown.

- 4.6: Stabilization step buttons: Ready → need-state. Chat → opens chat. SOS → opens SOS placeholder.

### Suite 5: Module session screen

- 5.1: Streaming token rendering on each AI node.

- 5.2: Choice buttons disabled during streaming, enabled after.

- 5.3: LLM error → fallback_default_text shown with banner.

- 5.4: “Why am I seeing this choice?” expands inline.

- 5.5: “This doesn’t fit” → regenerate produces new node text.

- 5.6: “This doesn’t fit” → tell us why with phone numbers → sanitized.

- 5.7: “This doesn’t fit” → tell us why with risk language → state pauses, no PII stored, crisis flow opens.

- 5.8: “This doesn’t fit” → skip → state advances correctly.

- 5.9: Pause → resume → screen reopens at saved node, regenerates fresh text.

- 5.10: Choice text in DOM matches JSON exactly (no AI substitution).

### Suite 6: Synthesis and outcome screens

- 6.1: Synthesis screen renders three save options.

- 6.2: “Save” stores AI synthesis text.

- 6.3: “Edit, then save” stores edited text.

- 6.4: “Save without saving the summary” stores NULL synthesis_text.

- 6.5: Outcome with all three paths defined renders all three.

- 6.6: Path 1 (commitment) inserts row in commitments table with source=‘practice’.

- 6.7: Path 2 (tiny action) with bridge_action=‘send_text’ opens Messages prefilled.

- 6.8: Path 2 ‘send_text’ with no sober contacts → graceful empty state.

- 6.9: Path 2 ‘copy_message’ copies to clipboard with toast.

- 6.10: Path 3 (save_only) marks completion without text or commitment.

- 6.11: Rating screen records to event_log.

- 6.12: Skip rating: documented behavior matches implementation.

### Suite 7: Contraindications

For each detectable contraindication, verify:

- 7.1: ‘suicidal_ideation’ (recent risk=‘high’ event) → route screen with SOS option. User can bypass.

- 7.2: ‘severe_withdrawal’ (check-in craving=10 + withdrawal keywords) → route screen with medical resources.

- 7.3: ‘acute_intoxication’ (check-in craving=9 + intoxication keywords) → warn screen.

- 7.4: ‘driving’ (V3.7 stub) → returns matched=false (no false positives).

- 7.5: ‘domestic_violence’ (V3.7 stub) → returns matched=false.

- 7.6: ‘unsafe_contact’ (V3.7 stub) → returns matched=false.

- 7.7: Module without contraindications declared → launches normally.

### Suite 8: Settings and onboarding

- 8.1: Settings “Practice History” section visible with three buttons.

- 8.2: Reset practice history clears all V4.1 tables, leaves V3 data intact.

- 8.3: Export practice history downloads structured JSON.

- 8.4: Reset history for focus removes only that focus’s sessions.

- 8.5: Practice preferences toggles persist; notifications toggle is intentionally non-functional.

- 8.6: V4.1 onboarding intro shows once for new users post-V4.1.

- 8.7: V4.1 onboarding intro shows once for existing users on first V4.1 open.

- 8.8: V4.1 onboarding intro does NOT show on second open after dismissal.

### Suite 9: V4 regression

V4.1 must not regress V4. Re-run the V4 Prompt 6 smoke suite end-to-end:

- 9.1: V4 chat surface byte-identical.

- 9.2: V4 check-in synthesis byte-identical.

- 9.3: V4 onboarding flow (10 steps) unchanged.

- 9.4: V4 user-context cache invalidation still works.

- 9.5: V4 milestone awareness still fires.

### Suite 10: Voice consistency under regeneration

Pick 3 modules (Module 1 alcohol, Module 5 alcohol, Module 6 codependency). For each:

- 10.1: Regenerate the hook 5 times via “this doesn’t fit” affordance. Voice consistent across 5 generations.

- 10.2: No forbidden phrases in any of 5 generations.

- 10.3: Module 5: no shame copy in any of 5 generations.

- 10.4: Module 6: no pathologizing copy in any of 5 generations.

- 10.5: Module 6 Concept 1: DV hotline sentence in 5/5 generations.

-----

## RUNNING THE SUITES

Add a script: `scripts/run_v41_smoke_suite.ts`. It runs each suite and produces a report:

```

V4.1 SMOKE SUITE RESULTS

========================

Run date: [ISO timestamp]

LLM model version: [version]

Suite 1: Practice surface assembly

1.1: PASS

1.2: PASS

...

Suite 7: Contraindications

7.1: PASS

...

OVERALL: 47/52 PASS, 5 FAIL

```

For any failures: include the test description, the expected behavior, and the actual behavior.

The suite is automatable for most cases (programmatic asserts). Some cases (voice consistency in Suite 10) require human review — those are flagged as “Manual review required” rather than auto-pass.

-----

## SUCCESS METRICS BASELINE

Per V4.1 spec Section 11, the success metrics frozen for 90 days post-launch:

- 70% of users who start a module complete it (reach outcome).

- 50% of completed modules rated “useful” within 24 hours.

This prompt does NOT measure against the success metric (no users yet at deploy time). It establishes the metrics tracking infrastructure:

- Verify event_log captures ‘practice_module_started’ and ‘practice_module_completed’ for each session.

- Verify the rating event is captured.

- Verify the rating-within-24h calculation is computable from event_log timestamps.

- Add a stub script `scripts/v41_metrics_snapshot.ts` that calculates start/complete/rate-useful percentages over a date range. Initially returns “0 sessions to measure” but the calculation logic is in place.

This is metrics scaffolding, not measurement.

-----

## DELIVERABLE

The agent produces:

1. `scripts/run_v41_voice_eval.ts` — voice eval runner.

1. `scripts/run_v41_smoke_suite.ts` — full smoke suite runner.

1. `scripts/v41_metrics_snapshot.ts` — metrics calculation stub.

1. `eval/v41_voice_baseline.json` — saved baseline outputs.

1. A markdown report `eval/v41_smoke_report.md` with:

- Voice eval summary (programmatic pass/fail counts).

- Smoke suite results per suite (pass/fail per case).

- Critical findings (any forbidden phrase leaks, any contraindication failures, any V4 regressions).

- Ship recommendation: ship / hold for fix / hold for human review.

## TARGETED SMOKE TEST

After running both scripts:

1. Open `eval/v41_voice_baseline.json`. Verify all 25 cases present.

1. Open `eval/v41_smoke_report.md`. Verify all 10 suites reported.

1. Manually review 3 cases at random from voice eval baseline. Confirm voice quality matches voice exemplars (sponsor-adjacent, plain, grounded).

1. Manually verify Module 5 baseline: open the case for after_slip alcohol focus. Read the hook, concept, practice_1 outputs. Confirm zero shame copy.

1. Manually verify Module 6 baseline: open the holding_no codependency case. Read the outputs. Confirm zero pathologizing copy. Confirm DV hotline sentence in concept 1.

1. Run `scripts/v41_metrics_snapshot.ts`. Verify it produces “0 sessions in window” (no real usage yet) without erroring.

## AT THE END

Report in under 500 words:

- Files created (eval scripts, baseline file, report).

- Voice eval results: 25 cases, programmatic pass/fail breakdown, list of any failed cases with specific issue.

- Voice quality observations across 25 cases (systematic patterns, not per-case).

- Smoke suite results: total cases, total pass, total fail, list of any failed cases with details.

- V4 regression check result: V4 chat/checkin still byte-identical? Pass/fail.

- Module 5 shame-copy review: zero leaks across 5+ generations? Confirmed.

- Module 6 pathologizing-copy review: zero leaks across 5+ generations? Confirmed.

- Module 6 DV hotline sentence: 5/5 generations or fewer? If fewer, what’s the failure rate?

- Contraindication coverage: which contraindications were programmatically tested vs which are stubs.

- Metrics scaffolding: confirmed in place, not yet measuring against thresholds.

- Honest ship recommendation: ship V4.1 now / hold for [specific fix] / hold for human review of [specific cases].

- Confirmation that no module JSON was modified during this prompt.

- Confirmation that no schemas were modified.

- The success metric is frozen for 90 days post-launch. This prompt is baseline establishment, not measurement.

If the recommendation is “hold for fix”, be specific: which module, which node, which voice_constraints field. If “hold for human review”, flag exactly which cases need eyes on them.

V4.1 is shippable when:

1. All programmatic voice eval cases pass (zero forbidden phrase leaks).

1. All smoke suite cases pass except those explicitly marked “manual review required”.

1. V4 regression: zero regressions.

1. Module 5 shame copy: zero leaks across baseline + 5 regenerations.

1. Module 6 pathologizing copy: zero leaks across baseline + 5 regenerations.

1. Contraindication routing works for all V3.7-detectable contraindications.

Anything short of that is a hold, not a soft launch.
