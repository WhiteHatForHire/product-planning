---
title: "Anchor V4 User Context Architecture"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Anchor V4/Anchor V4 User Context Architecture.docx"
status: reference
privacy: working
tags:
  - product
---

# Anchor V4 User Context Architecture

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ANCHOR V4

User Context Architecture

Master Spec • Working draft • April 26, 2026

What V4 Is

V4 is the foundational refactor that makes Anchor's AI surfaces personal. It does two things:

Adds the data Anchor needs to talk to a user as the specific person they are: their experience level (first attempt vs returning vs chronic relapse vs long-term stable), and a clean separation of recovery method (AA, SMART, secular, MAT, etc.) from recovery focus (alcohol, weed, porn, codependency, etc.). Recovery focus, sobriety dates, support style, and sobriety_why are already captured in V3.7; this spec extends that schema.

Builds a real prompt assembler. Today, the chat system prompt is concatenated inline in chat.ts lines 180–188. There is no function that constructs the system prompt as a unit. V4 introduces buildChatSystemPrompt(memory, options) as a dedicated, testable module, with milestone awareness, drift signal awareness, focus awareness, experience-level awareness, and trigger-based caching. Check-In synthesis migrates to consume the same builder.

V4 is the prerequisite for V4.1 (Practice Mode), V5 (predictive features and pattern intelligence), and any future AI surface. Without it, every surface re-implements its own context construction and the user experiences the AI as multiple uncoordinated personas.

V4 is NOT a rewrite of V3.7. The existing onboarding, the existing user_memory table, the existing buildMemoryContext function, the existing event_log, and the existing CHAT_SYSTEM_PROMPT constant are all preserved. V4 adds a thin layer on top, restructures one field, and adds one onboarding step.

1. Current State (V3.7, shipped)

V4 builds on what exists. This section documents reality, not aspiration.

user_memory table

All per-user memory lives in one table: user_memory. The full schema:

Column

Type

Nullable

Default

id

integer (serial PK)

NO

auto

user_id

varchar(100)

NO

'dev_user'

stable_profile

jsonb

YES

—

recent_summary

text

YES

—

event_log

jsonb

YES

—

updated_at

timestamptz

NO

now()

last_summarized_at_event_count

integer

NO

0

last_checkin_local_date

varchar(10)

YES

—

There is no separate stable_profile table. The recovery profile lives in the stable_profile jsonb column. This is good for V4: adding fields is a JSON change, not a Postgres schema migration.

stable_profile JSON shape (V3.7)

Set and read via normalizeStableProfile() in v3helpers.ts. 16 keys today:

recovery_focus            string[]

sobriety_start_dates      Record<string, string>

known_triggers            string[]

support_style             string

recovery_program          { primary: string; specific: string[] }

sobriety_why              string

sober_contacts            { name: string; phone?: string }[]

meeting_links             { label, day_of_week, time, timezone, url }[]

recurring_commitments     string[]

pinned_facts              string[]

email                     string

reminder_time             string      default '08:00'

timezone                  string      default 'America/New_York'

commitment_followup_hours number      default 4

reminder_enabled          boolean     default true

weekly_summary_enabled    boolean     default true

theme_preference          string?     optional

event_log shape (V3.7)

A flat array on user_memory.event_log, capped at 90 entries, oldest dropped first. Each entry has exactly three keys:

{

"type": "checkin_summary",

"summary": "2026-04-25: high risk, mood 1, craving 10.",

"timestamp": "2026-04-25T08:56:28.084Z"

}

Two types in production: 'checkin_summary' (written by checkin.ts) and 'chat_session' (written by chat/session-summary). The actor / source / kind taxonomy from older V4 planning docs is paper, not code. V4 does not introduce that taxonomy. Future expansion is V5+ scope.

app_settings table (V3.7)

Pure session/onboarding/scheduler-deduplication state. No user-facing settings. Columns:

id (serial PK), user_id (varchar)

last_opened_date, first_open_completed, prompt_for_date_shift

onboarding_version

last_daily_reminder_sent_date, last_missed_followup_sent_date, last_weekly_summary_sent_week

Anything the user actually changes (theme, timezone, reminder time, contacts) goes into stable_profile. V4 does not modify app_settings.

Onboarding flow (V3.7, 9 steps)

Captured today, in order:

Step 1. Welcome ("Good to have you here"). No data.

Step 2. Recovery focus. Multi-select chips: Alcohol, Weed, Nicotine, Porn, Gambling, Sugar, Codependency, Other. Required.

Step 3. Sobriety start date for the chosen focus(es). Date + time pickers. "I'll set this up later" skip.

Step 4. Support style. Single select: Direct and honest / Gentle and encouraging / Just the facts / Mix of all three.

Step 5. Recovery program. Single select: AA, NA, 12-Step (other), Codependency/Relationships, Sex/Love/Porn/Intimacy, SMART Recovery, Recovery Dharma, Refuge Recovery, Secular/No Program, Gambling/Money/Work, Food/Eating, Other/Not sure yet.

Step 6. Sobriety why. Free-text. "A sentence or two. Anchor will bring this back on hard days." Skip available.

Step 7. Sober contacts. Up to 3 (name + phone). Skip available.

Step 8. Meeting links. Label + day + time + URL. Skip available.

Step 9. Reminder time + email. Time defaults to 8:00 AM.

The Step 5 picker collapses two distinct dimensions: "Codependency / Relationships" and "Sex/Love/Porn/Intimacy" are recovery focuses (already captured at Step 2), while "AA, SMART, Refuge" etc. are recovery methods. V4 fixes this conflation.

Chat system prompt assembly (V3.7)

There is no dynamic prompt builder. The full assembly lives in chat.ts lines 180–188:

// Line 180 — base

let systemContent = memoryContext

? `${CHAT_SYSTEM_PROMPT}\n\n${memoryContext}`

: CHAT_SYSTEM_PROMPT;

// Lines 184–188 — one-shot check-in context

if (checkin_context && typeof checkin_context === 'string' && checkin_context.trim()) {

const safeCtx = checkin_context.trim().slice(0, 800);

systemContent += `\n\nCHECK-IN CONTEXT (...):\n${safeCtx}\n\nInstruction: ...`;

}

Three pieces:

CHAT_SYSTEM_PROMPT — hardcoded ~115-line constant defined at the top of chat.ts. Persona, mode detection, voice rules, crisis routing. Never changes at runtime.

memoryContext — built by buildMemoryContext() in v3helpers.ts. On turn 0 (empty history) this is the full block: pinned facts, recovery focus, program, why, triggers, support style, named contacts, recent summary (truncated to 1200 chars), last 5 event_log summaries. On subsequent turns it degrades to buildCondensedProfileContext() — a single line with only pinned facts, recovery focus, and support style.

checkin_context — optional, sent only from the post-check-in chat entry point. Capped at 800 chars. Appended last with a hardcoded instruction to reference it in the first reply.

This is the right target. V4 extracts the assembly into a dedicated module.

2. V4 Scope

Schema changes

All changes land in the stable_profile jsonb blob. No Postgres migrations.

Two new fields:

experience_level    'first_attempt' | 'returning' | 'long_term_stable' |

'chronic_relapse' | 'unspecified'

recovery_method     'twelve_step' | 'smart' | 'refuge_dharma' | 'secular' |

'mat' | 'harm_reduction' | 'moderation' |

'therapy_only' | 'none' | 'mixed'

One field restructured:

// V3.7 (current)

recovery_program: { primary: string; specific: string[] }

// V4 (new)

// recovery_program is removed.

// Its data splits into recovery_focus (already exists, becomes canonical)

// and recovery_method (new).

Migration logic (one-time backfill on first V4 read of any stable_profile):

If recovery_program.primary maps to a known method ("AA", "NA", "12-Step (other)" → 'twelve_step'; "SMART Recovery" → 'smart'; "Recovery Dharma" or "Refuge Recovery" → 'refuge_dharma'; "Secular/No Program" → 'secular'; "Other/Not sure yet" → 'none'), set recovery_method to that value.

If recovery_program.primary maps to a focus ("Codependency / Relationships" → add 'codependency' to recovery_focus; "Sex/Love/Porn/Intimacy" → add 'porn' or 'sex' to recovery_focus if not already present; "Gambling/Money/Work" → 'gambling'; "Food/Eating" → 'food'), update recovery_focus accordingly and set recovery_method to 'none' if not otherwise determined.

Set experience_level to 'unspecified' for all existing users.

Drop the recovery_program field after one full deploy cycle of confirmed reads.

Migration runs in normalizeStableProfile() so it happens automatically on every read; no separate migration job.

All other stable_profile fields are unchanged.

Onboarding changes

Step 5 (recovery program) is restructured into two screens: a focus-completion check (if Step 2 already captured the focus, skip; otherwise prompt) and a recovery method picker. A new Step 6 captures experience level.

Revised onboarding flow (V4):

Step 1. Welcome. Unchanged.

Step 2. Recovery focus. Unchanged.

Step 3. Sobriety start date. Unchanged.

Step 4. Support style. Unchanged.

Step 5. Recovery method. "Are you working a program?" Single select: 12-step (AA/NA/etc), SMART Recovery, Refuge Recovery / Recovery Dharma, Secular / no program, Medication-assisted treatment, Harm reduction, Therapy only (no specific program), Not sure yet / I'll figure it out. Skippable, defaults to 'none'.

Step 6 (NEW). Experience level. "How would you describe where you are with this?" Single select: This is my first time trying. I've tried before — I'm back at it. I've been at this for a while and I'm stable. I keep relapsing and I'm tired. I'd rather not say. Skippable, defaults to 'unspecified.' Brief non-judgmental copy under each option.

Step 7. Sobriety why. Was step 6 in V3.7. Unchanged content.

Step 8. Sober contacts. Was step 7. Unchanged.

Step 9. Meeting links. Was step 8. Unchanged.

Step 10. Reminder time + email. Was step 9. Unchanged.

Onboarding goes from 9 steps to 10. The added step is single-select with a skip option, ~15 seconds. Acceptable cost for the value it produces.

Existing user migration: users on V3.7 have onboarding_version set. After V4 deploys, on first app open they see a single-screen modal: "Two quick questions Anchor uses to talk to you better" with the two new fields back-to-back. Both skippable. Modal dismissable; users prompted again on next app open if skipped, then never again.

Settings additions

Recovery Profile section in Settings (existing or new) gains:

Recovery focus (multi-select chip editor)

Per-focus sobriety dates

Recovery method (single select dropdown)

Experience level (single select dropdown)

Sobriety why (text editor, voice input, clearable)

Support style (existing)

All edits invalidate the cached system prompt (see Section 3).

buildChatSystemPrompt() — the new module

New file: server/lib/buildChatSystemPrompt.ts

New file: server/lib/CHAT_SYSTEM_PROMPT.ts (extracted constant from chat.ts)

Function signature:

export function buildChatSystemPrompt(

memory: UserMemory,

options: BuildOptions

): AssembledPrompt;

type BuildOptions = {

surface: 'chat' | 'checkin_synthesis';

checkin_context?: string;          // optional, capped at 800 chars

drift_signal?: boolean;            // from future Pattern Insight (V5)

trigger: 'request_initiated' | 'midnight_rollover' | 'profile_edit' |

'milestone_crossed' | 'tracker_reset' | 'manual_invalidation';

};

type AssembledPrompt = {

prompt_text: string;

built_at: string;

cache_key: string;

metadata: {

primary_focus: string;

day_counts: Record<string, number | null>;

approaching_milestone: ApproachingMilestone | null;

recently_crossed_milestone: CrossedMilestone | null;

experience_level: string;

recovery_method: string;

drift_signal: boolean;

invalidated_by: string;

};

};

Internally, buildChatSystemPrompt assembles six sections in order:

Identity and posture: surface-specific. For 'chat', loads CHAT_SYSTEM_PROMPT (extracted, unchanged). For 'checkin_synthesis', loads a shorter terse persona constant.

Crisis and safety rules: shared constants from existing safety helpers. Unchanged content.

User context: built from memory. Replaces what buildMemoryContext currently produces, with the additions of experience_level and computed milestone state. The full block on turn 0; the condensed version on subsequent turns (preserving V3.7 behavior).

Time-aware framing: NEW. If approaching_milestone is set, adds a line like "Alcohol focus is 13 days from a 60-day milestone. The user may benefit from light acknowledgment without pressure." If recently_crossed_milestone is set, adds "Alcohol focus crossed 60 days within the last 24 hours. Acknowledge quietly if user brings it up." If drift_signal is set (V5+), adds drift framing. None of these reference recovery phases by name to the user.

Voice and tone: surface-specific overlay. For 'chat', the conversational sponsor-adjacent voice. For 'checkin_synthesis', terse third-person summary voice.

Forbidden content rules: shared constants. No phone numbers, no clinical labels, no shame language, no phase attribution to user.

On subsequent chat turns within a session, the User Context section uses the condensed variant (preserving V3.7 behavior). The Time-Aware Framing section is preserved at full detail because milestone language matters per-turn.

Computed helpers

New helpers in v3helpers.ts (or a new file lib/recoveryProfile.ts):

function getDayCount(focus: string, profile: StableProfile): number | null

function getApproachingMilestone(profile: StableProfile): ApproachingMilestone | null

function getRecentlyCrossedMilestone(profile: StableProfile): CrossedMilestone | null

Milestone list (fixed for V4): 3, 7, 14, 30, 60, 90, 180, 365 days, then yearly. Approaching window is 5 days. Recently-crossed window is 24 hours.

getDayCount returns null if sobriety_start_dates[focus] is null or absent. The assembler handles null day counts gracefully ("You haven't started counting yet for this focus" framing).

Caching and invalidation

In-memory LRU cache keyed by user_id. Each entry stores the AssembledPrompt and the input that produced it (stable_profile.updated_at, computed day_counts, computed milestone state, drift signal state, surface).

On every chat or check-in synthesis request:

Compute current input hash (profile updated_at + day count signature + milestone state + drift signal + surface).

If cached entry's input hash matches current, return cached prompt.

Otherwise, rebuild and cache.

Invalidation triggers (each results in a different invalidated_by metadata value):

Day count rollover (midnight in user's timezone) — detected by comparing today's date in user_tz against last_built_for_date in cache entry. If they differ, rebuild.

Profile edit — detected by stable_profile.updated_at change.

Milestone crossed — detected by comparing approaching/crossed milestone state in cache vs computed.

Tracker reset — a sobriety_start_date change is a profile edit; caught automatically.

Drift signal change — V5 introduces this; V4 just exposes the flag.

Cache TTL is 24 hours as a backstop. The midnight-rollover trigger should fire first.

Wiring chat.ts and checkin synthesis

chat.ts changes (lines 180–188 area):

// Old:

let systemContent = memoryContext

? `${CHAT_SYSTEM_PROMPT}\n\n${memoryContext}`

: CHAT_SYSTEM_PROMPT;

if (checkin_context ...) { systemContent += ... }

// New:

const assembled = buildChatSystemPrompt(memory, {

surface: 'chat',

checkin_context: checkin_context,

trigger: 'request_initiated',

});

const systemContent = assembled.prompt_text;

CHAT_SYSTEM_PROMPT moves from the top of chat.ts to its own file. buildMemoryContext is preserved as a helper called from inside buildChatSystemPrompt.

Check-in synthesis (currently uses buildMemoryContext or similar inline assembly; verify exact location during implementation):

const assembled = buildChatSystemPrompt(memory, {

surface: 'checkin_synthesis',

trigger: 'request_initiated',

});

The checkin_synthesis surface variant uses a shorter Identity section and tighter Voice section, but consumes the same User Context block. Voice differs; data is the same.

3. V4 Invariants

These extend the existing V3 invariants. Every consumer of the assembled prompt must preserve them.

buildChatSystemPrompt is the canonical assembler. No surface concatenates its own system prompt inline.

Given the same memory state and options, the assembler is deterministic. Same input → byte-identical output. AI is not used in assembly.

The assembled prompt never contains phone numbers, raw transcripts, full chat history, or raw notes. Existing V3 redaction helpers run on memory before it enters the assembler. Sober contact phone numbers in memory.stable_profile.sober_contacts are stripped from the prompt; only names appear.

Recovery phase language is never named to the user in any AI-generated text. Phase data is internal metadata only and may inform tone but not vocabulary.

Day count rollover at midnight in the user's timezone always invalidates the cache. The system never serves a prompt whose day count is from yesterday.

Profile edits propagate to the next AI call within one second (cache invalidation is fast).

System-generated inferences (drift signal, milestone state, etc.) are attached as prompt metadata. They are never written into stable_profile or treated as user-generated facts.

experience_level is a self-report field. The system does not infer or override it. Users can edit it anytime.

recovery_method is also a self-report field. Multi-method users (different methods per focus) are deferred to V5; V4 supports one method per user globally.

If sobriety_start_date is null for a focus, day count is null. The assembler handles null counts gracefully and never invents a number.

4. Example Assembled Prompts

Three illustrative cases. The User Context, Time-Aware Framing, and Voice sections are shown; identity, crisis, and forbidden-content sections are loaded from constants and not reproduced here.

Case 1: Returning user, day 47 alcohol + day 12 porn, twelve-step + therapy_only

(In V4, recovery_method is single-valued globally; this case treats the user as twelve_step. Multi-method per focus is V5.)

[User context]

This user is in active recovery from:

- Alcohol: 47 days

- Porn: 12 days

Recovery method: twelve-step program.

Experience level: returning. They have tried before.

Acknowledge that they're here without celebrating the return

as if it's the first time.

The user said their reason for doing this is:

'to be present for my kids.'

Reference this only when relevant; do not quote it back every

conversation.

[Time-aware framing]

Alcohol focus is 13 days from a 60-day milestone. The user may

benefit from light acknowledgment of progress without pressure.

Do not force the topic; if it comes up naturally, you can name it.

Case 2: First-attempt user, day 4 alcohol, secular method

[User context]

This user is in active recovery from:

- Alcohol: 4 days

Recovery method: secular / no specific program.

Experience level: first attempt.

This is their first time trying. Use orientation-friendly

language. Encourage simple actions. Do not assume recovery

vocabulary. Hope is appropriate; pressure is not.

The user did not provide a reason.

[Time-aware framing]

Alcohol focus is 3 days from a 7-day milestone. Early days are

their own kind of work. If they reach 7 days, acknowledge

simply, without fanfare.

Case 3: Chronic relapse user, day 2 alcohol, mat method

[User context]

This user is in active recovery from:

- Alcohol: 2 days

Recovery method: medication-assisted treatment.

Experience level: chronic relapse.

This user has tried multiple times. Do not use 'this time will

be different' language. Do not project false confidence. Treat

each day as its own day. Do not shame past attempts. The work

they have done before is not erased; today is just today.

The user said their reason for doing this is:

'I am tired of being tired.'

Reference this only when it's actually useful, not on schedule.

[Time-aware framing]

No milestone approaching. Day 2 is its own thing.

These examples show the design payoff: same architecture, three different voices, no per-surface code duplication. The assembled prompt does the work; the LLM's response calibrates accordingly.

5. Build Sequence

V4 is roughly 1–2 weeks of solo AI-directed work. Suggested order:

Week 1

Day 1–2: Add experience_level and recovery_method to normalizeStableProfile() with defaults. Add migration logic from recovery_program (preserves data; runs on every read; safe). Verify in dev that existing user_memory rows still load and serialize correctly.

Day 2–3: Extract CHAT_SYSTEM_PROMPT from chat.ts to its own file. Verify chat still works. Pure refactor; no behavior change.

Day 3–5: Build buildChatSystemPrompt() module. Implement six-section assembly. Wire up all helpers (getDayCount, getApproachingMilestone, getRecentlyCrossedMilestone). Implement caching with invalidation triggers. Unit tests against fixture user_memory rows.

Day 5–7: Switch chat.ts to use buildChatSystemPrompt. Verify with manual QA: existing user, day count rolls over, profile edited, milestone approached, milestone crossed.

Week 2

Day 8–9: Onboarding additions. New Step 5 (recovery method) and Step 6 (experience level). Existing-user migration modal. Verify both new-user and existing-user flows.

Day 9–10: Settings UI updates. Add experience_level and recovery_method editors. Verify edit → invalidate → next AI call uses fresh prompt.

Day 10–12: Switch check-in synthesis to use buildChatSystemPrompt with surface = 'checkin_synthesis'. Verify check-in synthesis output remains tonally appropriate.

Day 12–14: Voice eval pass. Manual review of assembled prompts across the case matrix (first attempt / returning / long-term stable / chronic relapse) crossed with (no milestone / approaching / crossed). 16 check cases. Adjust prompt copy in the User Context section as needed.

Tests required

Unit: normalizeStableProfile migration from V3.7 recovery_program to V4 recovery_method. Verify all 12 V3.7 program values map cleanly.

Unit: getDayCount handles null sobriety_start_date, timezone edge cases, leap days.

Unit: getApproachingMilestone correctly identifies the 5-day window and returns null outside it.

Unit: getRecentlyCrossedMilestone returns the most recent crossing within 24h, null otherwise.

Unit: buildChatSystemPrompt is deterministic. Same inputs produce byte-identical output.

Unit: phone numbers in sober_contacts are stripped from assembled prompts.

Unit: Cache invalidation fires correctly for each trigger. Cache hit/miss logged in metadata.

Integration: chat.ts produces same output as V3.7 for a fixture user with all V4 fields at default ('unspecified', 'none', no milestone). V4 should not break existing behavior for users who skip everything.

Integration: chat.ts produces different, appropriate output for first-attempt vs returning vs chronic-relapse fixtures.

Integration: midnight rollover triggers cache rebuild in a fixture timezone scenario.

Manual QA: full onboarding new-user path. Full existing-user migration modal path. Settings edit → immediate effect in next chat turn.

6. Risks

Migration of recovery_program data. Some V3.7 users picked options that don't map cleanly (e.g., "Other / Not sure yet"). Mitigation: those users get recovery_method = 'none' and a settings prompt encouraging them to update. No data loss.

Onboarding length growth. 9 → 10 steps. Mitigation: Step 6 is single-tap with skip; total added time ~15 seconds.

Existing user surprise. Migration modal pops up on first V4 open. Mitigation: dismissable; reappears once on next open; never again. Modal copy is brief and explains why.

Cache invalidation correctness. Stale prompts produce wrong day counts. Mitigation: comprehensive trigger tests; midnight rollover tested across multiple timezones; observability on cache state.

Voice drift. The assembler must produce prompts that feel consistent across surfaces and across user states. Mitigation: 16-case voice eval pass before V4 ship; fixture tests for prompt determinism.

CHAT_SYSTEM_PROMPT extraction breaking chat. Pure refactor risk. Mitigation: do this first, separately, with regression tests, before adding any new logic.

Multi-method users. A user on MAT for opioids and twelve-step for alcohol gets one method globally in V4. Mitigation: V4 picks the user's most recently set method or asks them to choose; per-focus method is explicitly V5.

Codependency users without sobriety dates. Day count is null. Mitigation: assembler omits day-count framing for that focus; the user is still acknowledged in recovery.

Drift signal hook is exposed but unused. V5 dependency. Mitigation: V4 ships drift_signal: false default; future V5 wiring is one-line change.

7. Open Questions

Should the existing-user migration modal be one screen with both questions or two screens? V4 leans one screen.

Where should the recovery-method picker live in Settings: a new section or inside the existing Recovery Profile area? V4 leans inside Recovery Profile.

Should the assembler log every assembly to a SafeLogEvent for cost observability? V4 leans yes; minimal metadata.

How should multi-method users (per-focus method) be handled in V5? Open.

Should milestone language reference per-focus or only per-primary-focus? V4 leans per-focus when relevant; the assembler picks which to mention based on which is approaching/crossed.

Should the system prompt include the user's display name when set? V4 leans no by default; mentioning the name in every chat feels mechanical. The name is in memory if needed.

Voice exemplar set: do we need one for the User Context block specifically, or does CHAT_SYSTEM_PROMPT carry the voice? V4 leans CHAT_SYSTEM_PROMPT carries the voice; the User Context block is descriptive prose, not voiced text.

8. What V4 Is Not

V4 is not a full event taxonomy refactor. The actor/source/kind taxonomy from older planning docs remains paper. V5 may revisit.

V4 is not Pattern Insight. The drift_signal hook is exposed but not wired. V5 builds Pattern Insight.

V4 is not Practice Mode. V4.1 is Practice Mode; it consumes V4.

V4 does not introduce the Insight Engine, Drift Detection, SOS Mode, Home Command Center, Data Export, Memory Search, Relapse Response Protocol, or any other V5 surface. Those are V5 scope, evaluated against V4 architecture.

V4 does not introduce schema changes outside the stable_profile JSON blob. No Postgres migrations.

V4 does not introduce multi-agent orchestration, vector RAG, biometric integration, or wearables. Those remain deferred.

V4 does not modify the event_log shape. event_log stays at three keys (type, summary, timestamp).

9. Closing Note

V4 is the smallest possible foundation that lets every AI surface speak to the user as the specific person they are. It adds two fields to a JSON blob, restructures one field, adds one onboarding step, extracts one constant to its own file, and creates one new function. The new function is the entire architectural payoff: a deterministic, testable, cacheable assembler that knows how to talk to a first-attempt user differently than a chronic relapse user, knows what's coming up in the user's milestone calendar, and knows when to invalidate itself.

Everything we want to build next — Practice Mode, Pattern Insight, Drift Detection, milestone celebrations, focus-aware recommendations — reads from buildChatSystemPrompt or extends it. The cost of doing it now is one to two weeks. The cost of not doing it now is every future surface re-implementing context construction differently and the user experiencing the AI as multiple uncoordinated personas.

V3.7 already collects most of the data. V4 just makes the data work.
