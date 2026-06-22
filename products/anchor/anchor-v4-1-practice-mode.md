---
title: "Anchor V4 1 Practice Mode"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Anchor V4/Anchor V4 1 Practice Mode.docx"
status: reference
privacy: working
tags:
  - product
---

# Anchor V4 1 Practice Mode

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ANCHOR V4.1

Practice Mode (Guided Skill Practice)

Master Spec • Working draft • April 26, 2026

What V4.1 Is

V4.1 adds Practice Mode — a focused practice surface where users rehearse recovery-relevant skills (urge surfing, asking for help, refusing offers, repair after a slip, holding a no when asked) inside short branching scenarios. AI generates the dialogue inside human-authored branch trees. Scenarios adapt to what the user is recovering from.

V4.1 is built on V4. It does not duplicate V4 architecture; it consumes it. Specifically:

Recovery focus comes from V4. V4 onboarding captures recovery_focus. Practice reads it from stable_profile.recovery_focus. There is no separate Practice focus picker.

The system prompt comes from V4. Practice calls buildChatSystemPrompt(memory, { surface: 'practice', ... }) for every AI generation inside a module. The persona, voice, crisis rules, milestone awareness, and forbidden-content rules are inherited from V4. Practice adds a surface-specific overlay with module-specific instructions.

Caching and invalidation come from V4. If a user crosses midnight mid-module, the next node's prompt rebuilds with the new day count. Practice does not maintain its own cache.

Experience level comes from V4. First-attempt vs returning vs chronic-relapse users get different repair-loop language and different synthesis tone, automatically, because the V4 assembler produces a different prompt.

V4.1 introduces: branch tree authoring format (JSON), the deterministic state machine, the dialogue generator that wraps buildChatSystemPrompt with module context, six modules (five substance-side + one codependency POC), need-state entry on Home, the "this doesn't fit my situation" affordance, Repair Loops, three-path completion, and immediate post-module rating.

V4.1 ships after V4 is stable. Estimated 4–6 weeks of solo AI-directed work (mostly module authoring, not engineering).

1. Dependencies on V4

V4.1 will not function without V4. Specifically, V4.1 requires:

stable_profile.recovery_focus populated for every user. V4 onboarding makes this required for new users; V4 existing-user migration handles upgrades.

stable_profile.recovery_method populated. Default 'none' is acceptable; the assembler handles it.

stable_profile.experience_level populated. Default 'unspecified' is acceptable.

stable_profile.sobriety_start_dates populated per focus where the user has set them. Null counts are handled.

buildChatSystemPrompt() function deployed and stable, with a 'practice' surface variant.

normalizeStableProfile() handling all V4 fields with safe defaults.

Cache invalidation working correctly across midnight rollover, profile edit, milestone state changes.

If V4 is not deployed and verified before V4.1 build begins, V4.1 will need to either ship its own stub for these or be blocked. The clean path is V4 first.

2. Product Invariants

V4.1 inherits all V3 and V4 invariants. These extend them specifically for Practice.

Practice is structured. Every module follows a designed branch tree authored as JSON. AI generates dialogue inside the branch, not the branch itself.

Branch trees are skill-shaped. Scenario specifics are conditioned on user recovery focus at runtime via the V4 assembler. Choice options are static and the AI may not rephrase or substitute them.

Every session ends with one of three outcomes: a written commitment, a tiny next-action selection, or save-without-commitment. Completion does not require performing readiness.

Practice never replaces Chat or Check-In. It is offered as one of the surfaces from Home.

Practice never disables crisis routing. If risk signals trigger mid-module, the module pauses and the standard crisis flow takes over.

Practice is not the answer to acute distress. If acute-distress detection fires when the user opens the Practice surface, a 60-second stabilization step or routing to Chat/SOS appears before any module launches.

Practice does not generate content the user could not get from a credible source. Modules are grounded in DBT, CBT, motivational interviewing, and recovery literature. The AI personalizes delivery; it does not invent psychology.

Modules must not imply that abstinence-only, 12-step, sponsor-based, or willpower-based recovery is the only legitimate path. Where relevant, modules acknowledge MAT, secular recovery, harm-reduction, and professional care without centering them unless the user has selected that frame in V4 onboarding.

User-facing dialogue does not name recovery phases. Per V4 invariant.

The Practice surface variant of buildChatSystemPrompt may not access fields beyond what the V4 context schema permits. Practice cannot bypass V4's privacy posture.

User free-text input within a module (commitments, reflections) is sanitized at capture, stored in event_log, and never re-injected into subsequent node prompts within the same module.

Practice choices may be used for module continuity, user-visible reflection, and module recommendation. They may not be used for hidden risk scoring, automated clinical inference, or automated escalation unless explicitly defined and disclosed to the user.

Every AI-generated scenario carries a "this doesn't fit my situation" affordance with three actions: regenerate, tell us why, skip this node.

User progress is owned by the user. Modules can be replayed. Progress can be reset. Choice history can be deleted separately from sobriety history. Completion is not gamified beyond a quiet checkmark.

Practice is not a therapist portal. It does not diagnose, does not assign clinical labels, and does not claim therapeutic outcomes.

3. The Practice Surface Variant

V4 ships buildChatSystemPrompt with surfaces 'chat' and 'checkin_synthesis'. V4.1 adds a third: 'practice'.

Calling pattern

For every AI dialogue generation inside a module (hook node, concept node, practice node, repair loop reply, synthesis node), Practice calls:

const assembled = buildChatSystemPrompt(memory, {

surface: 'practice',

trigger: 'request_initiated',

practice_context: {

module_id: string;

module_version: string;

node_id: string;

node_type: 'hook' | 'concept' | 'practice' | 'repair_loop' | 'synthesis' | 'outcome';

node_prompt_template: string;     // from branch tree JSON

node_voice_constraints: string;   // from branch tree JSON

user_focus_for_this_session: string;  // user-chosen at module start

prior_choices_in_session: ChoiceRef[];  // for synthesis only

}

});

V4 must be extended to accept the practice_context option. This is a small change to V4's BuildOptions type:

// V4 BuildOptions, extended in V4.1:

type BuildOptions = {

surface: 'chat' | 'checkin_synthesis' | 'practice';

checkin_context?: string;

practice_context?: PracticeContext;     // new in V4.1

drift_signal?: boolean;

trigger: ...;

};

Per V4 invariants, adding a field to the assembler context requires explicit authorization. V4.1 is that authorization for practice_context. Other fields are not added. The schema lock holds.

Practice surface overlay

The Practice surface variant of the assembled prompt has the same six sections as Chat (identity, crisis, user context, time-aware framing, voice, forbidden content), but with three substantive differences:

Identity section: instructional persona, not conversational. "You are generating dialogue inside a structured recovery practice module. You are not having a conversation; you are filling in the words for a specific node in a designed scenario."

Voice section: the V4 chat voice carries forward (sponsor-adjacent, plain, grounded), but with practice-specific instructions: "You may not ask the user questions back unless the branch tree authored questions. You may not invent skills or psychology. You may rephrase the prompt for this node within the constraints provided, but you may not change the choices the user will see."

New section after voice: "Module context." Contains the node prompt template, the node voice constraints, the user's chosen focus for this session (which may be one of multiple in their profile), and — for synthesis nodes only — a list of which choices the user made earlier in the module. The AI generates the node text using these constraints.

All of identity, crisis, user context, time-aware framing, and forbidden content are unchanged from V4. The same first-attempt vs chronic-relapse voice differences apply automatically because they live in the User Context block of V4.

Per-node generation

Each node's AI-generated text is one buildChatSystemPrompt call followed by a single LLM completion. The user message is empty or contains only the node prompt template (depending on how the LLM is best prompted). Streaming token rendering for visible nodes (hook, concept, practice, repair loop, synthesis); non-streaming for outcome (no AI generation needed there).

Latency target: time-to-first-token under 1 second on 4G. If the LLM provider is slow or fails, fallback to a pre-generated default node text from the branch tree (see branch tree authoring, Section 5).

What does NOT go into practice_context

Per V4 invariants, the assembler context schema is locked. Practice context may NOT include:

Phone numbers, raw transcripts, full chat history, raw notes, raw check-in text.

User free-text input from prior nodes in the same module (sanitized at capture, never re-injected).

Other users' practice data. Each session is isolated.

Pattern Insight signals beyond the drift_signal boolean already in V4.

These exclusions are tested at the V4 layer. Practice cannot bypass them.

4. Module Structure

Module anatomy

Every module follows the same six-stage structure. Length total: 3-minute floor, 7-minute ceiling.

Hook (1 screen, ~20 seconds). A single concrete moment that grounds the module in lived experience, generated from a skill-shaped template parameterized by user focus.

Concept (1–2 screens, ~60 seconds). The skill in plain language. AI personalizes delivery based on V4-provided context (focus, experience level, recovery method).

Branching practice (3–5 nodes, ~90–180 seconds). User picks from 2–4 multiple-choice responses. Each choice produces a different AI-generated reply and a different next node. Sub-optimal choices route through a Repair Loop. Every scenario node carries a "this doesn't fit my situation" affordance.

Synthesis (1 screen, ~30 seconds). What the user worked through, in one paragraph, AI-generated and tied to their actual choices. User-visible before save with edit / discard / save-completion-only options. Default action: save module completion only; saving the AI summary is opt-in.

Outcome (1 screen). Three completion paths: write a commitment, choose a tiny next action, or save without committing. For communication and repair modules, the tiny-next-action options include direct bridge actions ("Send the text now," "Open Contacts," "Copy this message," "Save for later") rather than generic suggestions.

Immediate rating (single tap). "Was this useful right now?" Three options: useful / not really / not sure. Non-gating; logged to event_log.

Repair Loops

When a user picks a sub-optimal choice, the AI generates a brief, non-shaming reframe ("that's the move that usually backfires — here's what tends to work better") and routes the user to a forward path. The choice is recorded in practice_choices (per the practice-choices invariant, this data is used for module continuity and user-visible reflection only, not for hidden risk scoring). Users do not get stuck or punished for sub-optimal choices in practice.

Repair Loops replace dead-ends entirely. There are no terminal failure nodes in any V4.1 module.

Need-state entry

Home gains a Practice Quick Action. Tapping it shows a need-state screen, not a library:

"I'm having an urge."

"I feel ashamed or stuck in my head."

"I need to ask for help or repair something."

"I have something coming up I'm worried about."

"I already slipped and I'm scared."

"I want to look around." — routes to Library.

Each need-state maps deterministically to recommended modules, filtered by user's recovery focus(es). The recommendation is rule-based, not AI-driven, in V4.1. The Library remains accessible as a secondary option.

Acute-distress detection at entry

If V3.7's existing risk classifier indicates the user is acutely dysregulated when they tap the Practice Quick Action (based on most recent check-in, current chat session if active, recent event_log entries), a 60-second stabilization step appears before the need-state options. The user can complete the stabilization or skip directly to SOS. Practice modules launch only after this step or its skip.

Stabilization content is fixed: a single TIPP-style breathing or grounding prompt. Not a module. Not AI-generated. Static text loaded from constants.

Library screen (secondary)

Modules organized by need-state moments. Each card shows estimated time, completion state, and one-sentence purpose. Track and focus metadata visible on module detail screen. No streaks, no XP, no leaderboards, no progress percentages across the catalog. Completion shown only inside Library, never on Home or in summaries.

Module session screen

Single column, conversational layout. Streaming token rendering on AI nodes.

Choices appear as 2–4 tappable buttons. Tap-only on practice nodes.

"Why am I seeing this choice?" affordance on each option.

"This doesn't fit my situation" affordance, quiet text link below choices on every scenario node, with three actions (regenerate / tell us why / skip).

Pause button. Pausing saves state. Resuming returns to same node, same module version.

Synthesis screen presents the AI-generated paragraph with three actions: edit, save with module completion, save module completion only (default).

Outcome screen presents three completion paths.

After outcome, an immediate usefulness rating: "Was this useful right now?" with three options (useful / not really / not sure). Single-tap; not gating.

Tone

Plain, grounded, instructional. Warm without performing intimacy. Teaches through scenario and repair, not through excessive reassurance. Does not use coaching cadence. Inherited from V4 chat voice and adjusted by the practice surface overlay.

5. Branch Tree Authoring

Modules are authored as JSON files committed to the repo. Each module is one file. Versioned via semver (e.g., declining_the_offer_v1_0_0.json). New file: server/practice/modules/.

Schema

type Module = {

module_id: string;                    // e.g., 'declining_the_offer'

module_version: string;               // semver

display_name: string;                 // e.g., 'Declining the Offer'

estimated_minutes: { floor: 3, ceiling: 7 };

internal_track: 'foundations' | 'urge_skills' |

'communication_repair' | 'cognitive' | 'codependency';

applicable_focuses: string[];         // e.g., ['alcohol', 'weed', 'porn']

applicable_methods: string[];         // empty array means all

contraindications: ContraIndication[];  // module-level safety rules

voice_exemplar_ref: string;           // path to voice exemplar

nodes: Node[];

fallback_default_text: Record<string, string>;  // node_id → pre-gen text

};

type Node = {

node_id: string;

node_type: 'hook' | 'concept' | 'practice' | 'repair_loop' |

'synthesis' | 'outcome';

prompt_template: string;              // for AI generation

voice_constraints: string;            // max length, forbidden phrases, refs

choices?: Choice[];                   // 2–4 for practice nodes

next_node_id?: string;                // for non-practice nodes

outcome_options?: OutcomeOption[];    // outcome nodes only

};

type Choice = {

choice_id: string;

choice_text: string;                  // STATIC. AI may not rephrase.

choice_explanation: string;           // "Why am I seeing this?"

next_node_id: string;                 // forward path or repair loop

is_repair_route: boolean;             // true if this leads to a repair_loop

};

type ContraIndication =

| 'acute_intoxication'        // warns; does not block

| 'driving'                   // blocks

| 'severe_withdrawal'         // routes to medical resources

| 'unsafe_contact'            // restricts repair/contact prompts

| 'suicidal_ideation'         // routes to SOS

| 'domestic_violence'         // restricts refusal/disclosure prompts

| 'eating_disorder_active';   // routes away

The contraindication system is checked before module launch. The system reads recent event_log and current state to evaluate each declared contraindication. If matched, the launch behavior is determined by the contraindication type (warn, block, or route).

Prompt template format

prompt_template uses a simple variable syntax. Example for the hook node of "Declining the Offer":

Generate a 3-4 sentence scenario in which the user is offered

{focus_substance_or_behavior_human} by a familiar person at a

social gathering. The offer should be casual but pressured.

End with the offerer saying something dismissive of hesitation.

Voice: plain, grounded, second person.

The {focus_substance_or_behavior_human} variable resolves at runtime from the user's selected focus for this session. Mapping is a deterministic helper:

alcohol → 'a drink'

weed → 'a joint or a hit'

nicotine → 'a cigarette or a vape'

porn → 'a moment to look at something' (more abstract for this focus)

...

The variable list is part of V4.1 authoring documentation. Keep it small (3–6 variables max).

Voice exemplar set

Each module references one voice exemplar (a short authored sample showing the desired voice for AI generation in this module). Exemplars live in server/practice/voice_exemplars/. The voice eval harness (Section 7) tests AI output against exemplars.

The voice exemplar set must be authored before any modules are written. This is the V4.1 prerequisite analogous to V4's CHAT_SYSTEM_PROMPT extraction.

Fallback default text

If LLM generation fails (timeout, content filter, provider down), each node falls back to fallback_default_text[node_id]. These are pre-authored, focus-agnostic text strings that work for any user. Quality is acceptable, not great. Banner appears: "Using offline practice text — personalization unavailable."

V4.1 ships with fallback text for every node in every module. Authoring this is part of module authoring, not a separate task.

6. V4.1 Module Catalog

V4.1 ships six modules across six branch shapes. Five substance-side / cross-focus, one codependency POC.

Module

Internal Track

Branch shape tested

Lapse vs Relapse

Foundations

Shame-reduction concept module

The 20-Minute Urge

Urge Skills

Craving / urge-surfing scenario

Ask for Help Without a Speech

Communication & Repair

Vulnerability / disclosure scenario

Declining the Offer

Communication & Repair

Social-pressure / refusal scenario

What to Do After a Slip

Foundations / Repair

Post-event repair / spiral interruption

Holding a No When Asked

Codependency POC

Refusal of a request, not refusal of an offer

This set tests six different branch shapes (shame, craving, vulnerability, social pressure, repair, relational refusal). Codependency POC validates that the branch-tree format extends to relational recovery before V5+ commits a full codependency track.

Module-level applicable_focuses

Each module declares which focuses it works for. The need-state router and library only show modules whose applicable_focuses intersect the user's recovery_focus.

Lapse vs Relapse: applicable to all focuses.

The 20-Minute Urge: applicable to alcohol, weed, cocaine, opioids, nicotine, porn, sex. Not codependency (no urge structure).

Ask for Help Without a Speech: applicable to all focuses.

Declining the Offer: applicable to alcohol, weed, cocaine, opioids, nicotine. Not porn/sex/codependency (offer structure doesn't fit).

What to Do After a Slip: applicable to all focuses.

Holding a No When Asked: applicable to codependency only.

Users with multiple focuses see the union of applicable modules. A user with alcohol + codependency sees all six.

7. Data Model

V4.1 adds new tables (or new event_log types). Schema changes require explicit authorization per V4 architecture. V4.1 authorizes the following:

Option A: New tables (preferred for V4.1)

Three new tables. All Sensitive Recovery Data per V4.

practice_progress:

id              integer (serial PK)

user_id         varchar(100) NOT NULL

module_id       varchar(100) NOT NULL

module_version  varchar(20)  NOT NULL

started_at      timestamptz  NOT NULL

completed_at    timestamptz  NULL

current_node_id varchar(100) NULL

synthesis_text  text         NULL    // populated only if user opts in

session_focus   varchar(50)  NOT NULL // user's focus for this session

UNIQUE (user_id, module_id, started_at)

practice_choices:

id            integer (serial PK)

user_id       varchar(100) NOT NULL

session_id    integer      NOT NULL  // FK to practice_progress.id

node_id       varchar(100) NOT NULL

choice_id     varchar(100) NOT NULL

timestamp     timestamptz  NOT NULL

practice_scenario_feedback:

id            integer (serial PK)

user_id       varchar(100) NOT NULL

session_id    integer      NOT NULL

node_id       varchar(100) NOT NULL

action        varchar(20)  NOT NULL  // 'regenerate' | 'tell_us_why' | 'skip'

user_text     text         NULL      // for 'tell_us_why' only

timestamp     timestamptz  NOT NULL

event_log additions

event_log gains two new types (preserving the existing three-key shape: type, summary, timestamp):

'practice_module_completed': summary includes module_id and outcome path. No raw user text.

'practice_module_rated_immediate': summary includes module_id and rating value (useful / not really / not sure).

These propagate normally through the existing 90-entry rolling window.

Sensitivity classification and user controls

practice_progress, practice_choices, practice_scenario_feedback, and synthesis_text are all Sensitive Recovery Data. Settings gains:

"Reset practice history" — clears the three Practice tables for this user. Sobriety history is unaffected.

"Export practice history" — produces JSON of Practice data, separate from existing memory export.

"Reset history for a single focus" — clears only sessions where session_focus matches.

8. Privacy and Safety

V4.1 inherits all V3 and V4 safety invariants. Practice-specific additions:

Module-level contraindications

Each module declares its contraindications. The system checks active state before module launch. Examples:

Declining the Offer: warns if acute_intoxication is suspected (recent check-in flagged it). Blocks if user appears to be driving (this signal is not currently detectable in V3.7; the contraindication is declared but checking logic is V5+ work).

What to Do After a Slip: warns if acute_intoxication, suicidal_ideation, or unsafe_contact is active. The module may not push repair, confession, amends, or contact under these states. Specific node prompts within the module include conditional language.

Ask for Help Without a Speech: includes "choose a safe person" as an explicit step in the branch tree. Warns if domestic_violence flag is active (this is also currently undetectable in V3.7; contraindication declared, future work for the check).

Holding a No When Asked: warns if domestic_violence flag is active. The module may not encourage refusal in situations where refusal increases physical risk.

Clinical boundary matrix

May teach: urge surfing, distress tolerance, refusal of offers, refusal of requests, journaling prompts, asking for support, repair after a slip, planning before a risky event, recognition of relational patterns.

May suggest: contacting a sponsor, friend, meeting, or clinician; using SOS; using Contacts.

Must redirect: detox advice, medication changes, suicidality, domestic violence, psychosis, severe withdrawal, acute intoxication, eating-disorder behaviors, self-harm urges. Each triggers a routing message and offers SOS or external resources.

Withdrawal invariant

No module may imply that all quitting is safe to do alone. Modules referencing alcohol, benzodiazepine, or opioid cessation include a footer noting that medically supervised detox may be required. This applies to The 20-Minute Urge module specifically when run for those focuses; the prompt template includes a footer instruction.

Disclosures

Visible in app and App Store: "Anchor Practice provides general recovery skill rehearsal. It is not medical care, therapy, detox support, or crisis care. Some recovery situations require human, clinical, or emergency support."

No claim of therapeutic outcome. No clinical labels. Per V4 invariant, the system does not name recovery phases to the user in any form.

9. Build Sequence

V4.1 is roughly 4–6 weeks of solo AI-directed work. Most of the time is module authoring and voice eval, not engineering.

V4.1 prerequisites

Must complete before V4.1 build begins:

V4 deployed and stable. buildChatSystemPrompt working with chat and checkin_synthesis surfaces.

Voice exemplar set authored. Without exemplars, voice eval is not possible and module authoring drifts.

Focus list and contraindication list locked. Adding either mid-build invalidates eval coverage.

Branch schema (including contraindications field) finalized.

V4.1 must-ship checklist

Practice surface variant added to buildChatSystemPrompt. Tests pass.

Branch tree JSON schema defined and committed.

Module loader and deterministic state machine implemented.

Voice exemplar set authored. 20-prompt voice eval harness covering at least 4 focuses runs before every prompt template change.

Need-state entry screen on Home Practice Quick Action with six need-states.

Library screen organized by need-state moment, filtered by user's recovery_focus.

Module session screen: streaming token rendering, choice rendering, pause/resume, three-path outcome capture, immediate usefulness rating.

"This doesn't fit my situation" affordance on every scenario node with regenerate / tell us why / skip actions.

Repair Loop pattern across all six modules.

Synthesis screen: user-visible before save, edit / save with completion / save completion only (default).

Bridge-to-action options on outcome screen for communication and repair modules.

Module-level contraindications check before module launch (for contraindications detectable in V3.7; others declared but not enforced until detection lands).

practice_progress, practice_choices, practice_scenario_feedback table migrations.

event_log integration for completion and immediate rating events.

commitments integration for module-generated commitments (commitments table is V3 existing).

Risk classifier integration: acute-distress detection at Practice surface entry, mid-module crisis interrupt.

Sensitive Recovery Data classification, separate reset/export/delete controls in settings, per-focus deletion.

Free-text input sanitization. Practice-choices invariant enforcement at the data access layer.

Six modules authored, reviewed, and tested end-to-end across applicable focuses.

Onboarding update introducing Practice as a third surface alongside Check-In and Chat (one-screen modal on first V4.1 open for existing users; integrated into V4 onboarding for new users).

Invariant tests: state machine transitions, dialogue context filtering (V4 tests cover this; V4.1 tests verify Practice doesn't bypass V4), pause/resume, version-pinned in-progress sessions, voice consistency, choice-text immutability, free-text sanitization, contraindication enforcement, focus-conditioning correctness.

V4.1 should-ship-if-easy

Cost monitoring at API gateway with per-module ceilings.

Module version pinning for in-progress sessions (user starts module v1.0.0; mid-session, v1.1.0 ships; user finishes on v1.0.0).

LLM fallback configuration: primary model + one fallback. Fallback default text is must-ship; fallback model is should-ship.

V4.1 defer

24-hour encrypted rolling debug buffer. Defer unless support tickets warrant it during V4.1 testing.

"You practiced this before" surfacing in Chat or SOS. V5+.

Pattern-Insight-driven module recommendation. V5 dependency.

Sponsor view of completion. V5+.

"Share this commitment" affordance to send to a real human. V5+.

V4.1 build sequencing

Recommended order for the 4–6 week timeline:

Week 1: Voice exemplar set authored. Branch schema finalized. Practice surface variant of buildChatSystemPrompt added and tested. State machine and module loader scaffolded. One full vertical module (recommend The 20-Minute Urge for alcohol focus only): hook, concept, three practice nodes with repair loops, synthesis, outcome. End-to-end working.

Week 2: Validate the architecture against the vertical. Adjust schema if needed. Author second module (Lapse vs Relapse) and second focus on first module (weed). Voice eval first run.

Week 3: Author Declining the Offer + Ask for Help Without a Speech. Need-state entry built. Library built. Acute-distress detection at entry.

Week 4: Author What to Do After a Slip + Holding a No When Asked. Repair Loops finalized for all six modules. "This doesn't fit my situation" affordance built and feedback table populated.

Week 5: Settings UI. Sensitive Recovery Data controls. event_log integration. Onboarding update for V4.1. Voice eval second run; adjust prompts.

Week 6: End-to-end QA across all six modules and all applicable focuses. Invariant tests. Cost monitoring. LLM fallback. Voice eval third run before ship.

V4.1 success metric (frozen for 90 days)

Per V2.1 council, this is committed in writing and not changeable for 90 days post-launch.

Definition of "started a module": a session counts as started only after the user makes the first active choice. Card taps and abandoned-at-hook sessions do not count.

Primary: 70% of started modules are completed (any of the three completion paths).

Primary: 50% of completed modules are rated useful at the immediate post-module rating.

Secondary: "This doesn't fit me" affordance triggered on fewer than 15% of scenarios per focus. Higher rates indicate the focus parameterization needs work.

Retention is not a V4.1 metric. DAU and weekly active are not tracked as success criteria.

If primary metrics are not met after 90 days, the response is to revisit module quality, branch design, focus parameterization, and need-state mapping. Not to add engagement loops.

10. Risks

V4 not stable when V4.1 build begins. Mitigation: V4.1 build is gated on V4 deployment + at least one week of V4 stability with no critical bug fixes.

Module authoring is slow. Six modules across multiple focuses is a substantial writing project. Mitigation: V4.1 ships only six modules; build one full vertical first; voice exemplar set locked before authoring; per-week author cadence in build sequence.

AI dialogue drift across modules and focuses. Mitigation: voice eval harness covering at least 4 focuses, run before every prompt template change. Voice exemplar reference in every node prompt.

Cross-focus generation quality. Some focuses (porn, sex, codependency) are harder to generate scenarios for tastefully. Mitigation: voice eval set explicitly covers harder focuses; "this doesn't fit me" feedback signals quality issues directly.

Choice paralysis. Mitigation: 2–4 options per node.

Confusion with Chat. Mitigation: need-state entry replaces "choose your surface" decision. V4.1 onboarding introduces Practice.

Over-engineering the AI. Multi-agent orchestration is tempting and would be a mistake. Mitigation: invariant prohibits agent frameworks. V4 assembler is the only AI integration point.

Clinical creep. The temptation to teach more clinically nuanced material grows over time. Mitigation: invariants cap content at education and rehearsal, not therapy. Clinical boundary matrix in Section 8 enumerates what may be taught vs. redirected. Module-level contraindications.

Lesson avoidance / "good student" trap. Users may use Practice as procrastination. Mitigation: acute-distress detector routes away from Practice. Bridge-to-action options on communication modules include "Send the text now" and "Call sponsor now" rather than abstract suggestions.

Focus mismatch. AI generates a scenario that does not fit the user's situation. Mitigation: per-scenario "this doesn't fit me" affordance with regenerate / feedback / skip actions; feedback feeds prompt template improvement.

Codependency module fit. POC may reveal the branch-tree format does not extend cleanly to relational recovery. Mitigation: V5+ codependency expansion is gated on V4.1 codependency POC outcomes.

Surveillance perception from choice tracking. Mitigation: practice-choices invariant constrains use scope; user-facing transparency about what choice data is used for; per-focus deletion.

Voice drift undetected. Mitigation: voice exemplar set authored as V4.1 prerequisite, not afterthought.

V4.1 modifies V4's BuildOptions. Mitigation: change is additive (adds practice_context field); existing chat and checkin_synthesis surfaces unaffected; tests for both surfaces re-run after the V4 type change.

11. Open Questions

Should multi-focus users be asked which focus to practice for at session start, or should the recommendation engine pick? V4.1 leans ask, with a sensible default. The need-state entry screen could include a focus selector when the user has multiple.

How should commitments from Practice surface in the existing commitments table? Marked source: 'practice'. Auto due-date follow-up or ungated? V4.1 leans ungated with "remind me" opt-in per commitment.

Replays: should the AI reference "last time you chose X" in the synthesis? V4.1 leans yes; this is a synthesis-node behavior, achieved by including prior session's choices in practice_context.

Modality tags surfaced to users in V4.1 or authoring-only? V4.1 leans authoring-only.

Codependency module language: how to refer to the user's situation without using the word "codependency" in user-facing dialogue (the term itself is contested in some recovery communities)? Open. Module copy needs careful authoring.

Should fallback default text be focus-conditioned (different fallback for alcohol vs porn) or focus-agnostic? V4.1 leans focus-agnostic for V1 to keep authoring tractable; V5+ may revisit.

Should the immediate rating be visible to the user later (in their progress view) or write-only? V4.1 leans write-only; the rating informs system improvement, not user reflection.

12. What V4.1 Is Not

V4.1 is not Pattern Insight. Module recommendation is rule-based, not insight-driven. V5+.

V4.1 is not a sponsor-view feature. Sponsors cannot see Practice progress in V4.1.

V4.1 is not an audio-only mode. Voice input on commitment field only; no audio playback of modules.

V4.1 does not introduce per-focus recovery method. V4 supports one method globally; V5 may extend.

V4.1 does not introduce custom-track creation, sponsor sharing, or step-work integration.

V4.1 does not modify V4's chat or checkin_synthesis surfaces beyond adding the practice surface variant.

V4.1 does not add additional focuses beyond what V4 onboarding lists. Adding food / gambling / screens / etc. as focuses requires V4 schema work and is V5+.

V4.1 does not add multi-agent orchestration, vector RAG, biometric integration, or wearables.

13. Closing Note

V4.1 is the surface that turns Anchor from a recovery companion into a recovery rehearsal environment. It is built entirely on top of V4: the user context, the system prompt, the milestone awareness, the experience-level voice differences — all inherited. V4.1 adds the branching mechanic, the module catalog, and the scenarios.

The thing V4.1 ships that nothing else in the recovery-app market ships: structured rehearsal of a specific recovery moment, adapted to what the user is actually recovering from, with no shame in sub-optimal choices and no gamification of the work. The user practices declining a drink before the wedding, practices texting their sponsor before the urge, practices the post-slip morning before they need it. The AI fills in the words; the human-authored rails ensure coverage and safety.

V4.1 is the wedge. V4 is the foundation. V5 is what comes next once we know which features actually matter to users in production.
