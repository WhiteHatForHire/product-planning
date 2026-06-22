---
title: "Anchor V5 Post V4 1 Roadmap"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Anchor V5 Post V4 1 Roadmap.docx"
status: active
privacy: working
tags:
  - product
---

# Anchor V5 Post V4 1 Roadmap

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ANCHOR V5

Post-V4.1 Feature Roadmap

Master Spec • Working draft • April 26, 2026

What V5 Is

V5 is the feature roadmap that comes after V4 (User Context Architecture) and V4.1 (Practice Mode). It supersedes the old "V4 master doc" and the "Predictive Features" wishlist, both of which were written before V4 architecture existed.

V5 is organized as five phases (V5.0 through V5.4), each scoped to a few weeks of solo AI-directed work. Phases are numbered to indicate suggested build order, not hard dependencies. Some phases can be reordered based on production data after V4.1 ships.

V5 is grounded in the V4 architecture. Every AI-touching V5 feature consumes buildChatSystemPrompt; no V5 feature builds its own context construction. Every V5 schema change uses stable_profile JSON or new tables with explicit authorization. Every V5 user-facing surface inherits V4's voice differentiation across experience levels and recovery methods automatically.

V5 explicitly defers the high-complexity items from the old planning docs: realtime voice, wearables, vector RAG, multi-agent orchestration, accountability partner multi-user architecture. Those remain deferred until production usage demonstrates need.

1. Re-evaluation of Old V4 + Predictive Features

Before specifying V5 phases, every feature from the old V4 master doc and the Predictive Features doc was re-evaluated against V4 architecture. The result:

Already shipped in V3.7 (no V5 work needed)

Runtime error fix (check-in yes/no buttons)

Phone-number AI prompt audit and redaction helper

Raw content minimization audit

Helper invariant tests (memory, risk, handoff, event log, background tasks)

Pending commitment card on Home

Source-of-truth audit

Scheduler hardening, email feature flag, last-run logs

Chat voice auto-submit alignment

System health/debug view

Home Command Center simplification

Absorbed into V4 (no V5 work needed)

Recovery program awareness — V4 splits into recovery_focus (existing) and recovery_method (new field).

Sobriety Why awareness — V4's User Context block references stable_profile.sobriety_why automatically.

Recovery method-specific framing — V4 conditions the assembled prompt on recovery_method.

Experience-level voice differentiation — V4 conditions on experience_level (first attempt vs returning vs chronic relapse vs long-term stable).

Milestone awareness — V4 computes approaching_milestone and recently_crossed_milestone and includes them in the assembled prompt's time-aware framing section.

Real V5 features (specified in Sections 3–7)

SOS Mode + Offline Safety Cache (V5.0)

Pattern Insight Engine + Pattern Insight Card (V5.1)

Drift Detection wired into V4's drift_signal hook (V5.1)

Data Export (V5.2)

Memory Search Lite (V5.2)

Relapse Response Protocol (V5.3)

Evening Reflection (V5.3)

Micro Check-ins (V5.3, optional)

Commitment Streak (V5.3)

Event Taxonomy expansion (V5.4)

Step Work integration (V5.4)

Milestone Intelligence (V5.4)

Deferred indefinitely (require dedicated specs if revived)

Realtime voice call mode — AI cocoon risk; defer until production usage justifies.

Wearables / Apple Health integration — high privacy complexity; defer until users ask.

Vector RAG memory — defer until deterministic Memory Search Lite proves insufficient.

Voice tone analysis (Hume AI) — third-party API, marginal value over text signals; defer.

CrewAI / AutoGen / multi-agent orchestration — reject for V5; revisit only if a specific feature genuinely requires it.

Accountability partner pairing — multi-user architecture change; its own product question, not a V5 feature.

Meeting integration via third-party APIs — the existing meeting_links field handles user-curated meetings; auto-discovery is V6+ if at all.

Custom check-in fields — power-user feature; defer until baseline check-in evolution settles.

Predictive Features doc re-evaluation

The Predictive Features doc proposed eight pillars. Their fate in V5:

Predictive Features pillar

V5 disposition

1. Predictive UX (craving spike, drift, overconfidence flag, time-based, seasonal)

Folded into V5.1 Pattern Insight + Drift Detection. Built deterministically against existing check-in data, not ML.

2. Biological / wearable integration

Deferred. Apple Health, voice tone analysis, biometric prediction — all gated on production demand.

3. Intelligent conversation (pattern narrative, milestone intelligence, step work, relapse response)

Folded across V5.1 (pattern narrative), V5.4 (milestone intelligence, step work), V5.3 (relapse response).

4. Community without social media (accountability partner, meeting integration, sponsor comm layer)

Mostly deferred. Sponsor message drafting tool — V5.3+ candidate as part of relapse response. Accountability partner pairing — deferred. Meeting integration via APIs — deferred.

5. Emotional intelligence (emotion wheel, resentment tracker, gratitude bank, trigger mapping)

Trigger mapping folded into V5.1 Pattern Insight. Emotion wheel — V5.4 candidate as check-in enhancement. Resentment tracker, gratitude bank — V5.4 candidates if user demand exists.

6. Radical personalization (recovery program, custom fields, personal mantras, sobriety why)

Recovery program awareness and sobriety why — absorbed into V4. Custom fields, personal mantras — V6+.

7. Trust and transparency (explainable AI, data sovereignty, privacy by default, AI honesty)

Explainable AI — V5.1 Pattern Insight uses "why am I seeing this?" explanations. Data sovereignty — V5.2 Data Export. Others already baked into V3 / V4 invariants.

8. Habit architecture (streaks, micro check-ins, evening reflection, commitment streak)

All absorbed into V5.3.

2. V5 Invariants

V5 inherits all V3, V4, and V4.1 invariants. These extend them for the V5 phases.

Every AI-touching V5 feature consumes buildChatSystemPrompt. No V5 feature constructs its own system prompt inline.

Pattern Insight (V5.1) is deterministic. AI is not used to compute signals; AI is only used to phrase the resulting card via buildChatSystemPrompt.

Pattern Insight surfaces insights only when the data basis is sufficient. Returns null when not. The card does not appear with thin data.

Drift Detection writes to V4's drift_signal hook. It does not bypass V4 or write directly to user context.

"Why am I seeing this?" affordance is required on every Pattern Insight surface. Every insight cites computed signals, not raw notes or chat content.

System-generated inferences (insights, drift signals, phase hypotheses) are never written into stable_profile or treated as user-generated facts. Per V4 invariant.

Pattern Insight may not be used for hidden risk scoring or automated escalation beyond what is explicitly disclosed to the user. Per V4.1 practice-choices invariant, extended to all behavioral data.

V5 features may not introduce engagement loops, streak shame, variable rewards, or social comparison patterns. Per V3 / V4.1 anti-gamification stance.

Crisis routing remains uninterruptible across all V5 features. SOS Mode (V5.0) bypasses AI and is available from every major surface.

Data Export (V5.2) must include all user data: stable_profile, event_log, check-ins, commitments, practice_progress, practice_choices, practice_scenario_feedback, synthesis paragraphs the user opted to save. Phone numbers excluded by default; user can opt in to include them.

Relapse Response Protocol (V5.3) must not contain shame copy. The forbidden copy list is enforced at the prompt template level.

Event taxonomy expansion (V5.4) is opt-in, additive, and backward-compatible with the V3.7 three-key event_log shape. Existing entries are not migrated.

3. V5.0 — Safety Access

Goal: make human handoff and crisis resources reachable without depending on AI inference, network availability, or current app state.

Estimated effort: 1–2 weeks solo.

Features

SOS Mode:

Persistent route to real people and crisis resources. Available from Home, Check-In, Chat, Practice (V4.1), and Settings.

Header: "Need a person or immediate support?"

Subtext: "Anchor will not send anything automatically. You stay in control."

Primary actions: call saved contact, text saved contact (prefilled message, user sends manually), open meeting link, copy tell-on-myself message.

Crisis resources: 988, SAMHSA, local emergency note for non-US users.

Tiny grounding fallback at the top: "Put both feet on the floor. Take one breath. Then tap one person."

No AI chat inside SOS Mode.

Logs sos_opened event to event_log when entered.

Offline Safety Cache:

Local cache (localStorage or IndexedDB) of: sober_contacts (names + phones), meeting_links, 988/SAMHSA contact info, tell-on-myself template text.

Refreshed on every app open and on every relevant profile edit.

Accessible from SOS Mode even when offline. Banner: "Showing offline safety info — last updated [date]."

No AI required. No network required.

Settings includes "Clear safety cache" control.

Why V5.0 first

SOS Mode and Offline Safety Cache are the only V5 features that materially improve safety access. They have no V4 dependencies (they don't use buildChatSystemPrompt at all because there is no AI inside SOS) and ship cleanly without prerequisites. Building them first means safety access is no longer dependent on V4.1's stability or any subsequent phase.

Schema impact

No new tables. SOS state is computed from stable_profile.sober_contacts and stable_profile.meeting_links.

event_log gains 'sos_opened' as a new type (preserving the existing three-key shape).

localStorage keys defined for offline cache.

Risks

Offline cache staleness. Mitigation: refresh on every app open; show last-updated timestamp; warn if older than 7 days.

Phone numbers in the cache. Privacy concern. Mitigation: cache is local-only; never synced; never sent to AI; user can clear from Settings.

Accidental contact from prefill. Mitigation: prefilled SMS/call always opens the system dialer/messages app and requires user confirmation to send. Per V3 invariant.

4. V5.1 — Pattern Insight and Drift Detection

Goal: produce one deterministic, explainable insight on Home that helps the user notice drift earlier or take a useful next action. Wire drift detection into V4's drift_signal hook.

Estimated effort: 2–3 weeks solo.

Pattern Insight Engine

One canonical engine that produces ranked signals. Replaces the duplicate-system risk where each future feature might compute its own pattern logic.

Inputs:

user_memory (stable_profile, recent_summary, event_log, last_checkin_local_date)

check_ins table

commitments table

practice_progress, practice_choices (V4.1 surfaces)

Tracker state (sobriety_start_dates per focus)

Computed signals (deterministic; no AI):

Signal

Min data

Allowed copy / forbidden copy

Missed check-in drift

3 recent check-ins, then 2 expected check-ins missed

OK: "Your pattern changed a little. Worth checking in." NOT: "Relapse risk detected."

Rising craving

3 numeric craving values

OK: "Craving has been trending higher. Keep the next action small." NOT: "You are about to relapse."

Low sleep + high craving

4 check-ins with both sleep and craving

OK: "Low-sleep days have lined up with harder craving days. Keep tonight simple." NOT: "Your sleep caused your craving."

Repeated incomplete commitments

2 recent incomplete commitments

OK: "The follow-through loop needs attention. Pick one smaller promise today." NOT: "You keep failing commitments."

No recent contact

Reliable contact tracking required

OK: "You have not logged contact recently. Consider one low-pressure text." NOT: "You are isolating dangerously."

Time-of-day risk (Sunday evening, Friday night, etc.)

60+ days of check-in data

OK: "Sundays around this time have been harder for you historically. Stay close to your people tonight." Surfaces only when 3+ historical instances of elevated craving at same time.

Anniversary / seasonal awareness

90+ days of data including a hard week prior

OK: "Last [month] had some hard days. This week worth being intentional about." Tied to recurring dates.

Approaching milestone (consumed from V4)

V4 computes; V5 surfaces it as an insight when relevant

OK: "You're 5 days from 90 days on alcohol. Strong stretch coming up." Light, not pressure.

Ranking:

Safety signals (drift after recent crisis, very high craving) rank first.

Drift signals (missed check-ins, rising craving) rank second.

Commitment / action loop signals rank third.

Encouragement signals (approaching milestone) rank fourth.

The engine returns at most one primary insight. Returns null if data is insufficient. Secondary insights may live in an Insights screen later (V5.4 or beyond).

Pattern Insight Card on Home

One card on Home below the primary next action. Shows:

One-line title

Two-to-three-sentence body, generated via buildChatSystemPrompt with surface = 'pattern_insight' (new surface variant added in V5.1)

Suggested action button: check in, chat, contact someone, complete commitment, or SOS

"Why am I seeing this?" expandable affordance citing computed signals, not raw notes

Dismiss button — dismissed insights don't repeat the same signal for 24 hours

Pattern Insight surface variant

V5.1 adds 'pattern_insight' as a fourth surface to V4's buildChatSystemPrompt:

// V4 BuildOptions, extended in V5.1:

type BuildOptions = {

surface: 'chat' | 'checkin_synthesis' | 'practice' | 'pattern_insight';

...

pattern_signal?: PatternSignal;   // new in V5.1; the computed signal

};

The pattern_insight surface variant produces terse, single-paragraph copy. The User Context block from V4 ensures the language matches experience level (first-attempt user gets gentler insight phrasing; long-term-stable user gets more direct phrasing). The Voice section is constrained: cite the data, never the chat content.

Drift Detection

Drift Detection is one specific signal computed by the Pattern Insight Engine: the missed-check-in-drift signal, optionally combined with other signals (no recent contact + missed check-ins is stronger drift than either alone).

When drift is detected, the engine sets V4's drift_signal flag. V4's assembled prompt then includes a more grounded tone instruction in the Time-Aware Framing section across Chat, Practice, and Check-In synthesis. This is the V5.1 wiring of V4's drift_signal hook.

Drift signal clears when the user checks in or otherwise re-engages. Stale drift signals are cleared by a daily background task.

Schema impact

No new tables. Pattern Insight is computed on demand from existing data.

event_log gains 'pattern_insight_generated' and 'pattern_insight_dismissed' types.

Optional: a small pattern_insight_state table for caching drift signal state to avoid recomputation on every Home load. Or compute on demand. Performance call during build.

Risks

False positives. Mitigation: minimum data requirements per signal; the engine returns null if data is insufficient; user can dismiss.

Surveillance perception. Mitigation: every insight has "why am I seeing this?" with explicit signal citations; insights cite data not raw text.

Insight fatigue. Mitigation: one card max on Home; dismissal suppresses same signal for 24 hours.

Over-engineering ML. Mitigation: deterministic only in V5.1; ML deferred until rule-based proves insufficient.

5. V5.2 — Trust and Memory

Goal: give users full ownership over their data and let them retrieve relevant past events from chat without vector RAG complexity.

Estimated effort: 2 weeks solo.

Data Export

Three export formats, generated server-side, downloaded as files:

JSON: complete machine-readable export of all user data.

CSV: per-table CSVs zipped together (check_ins.csv, commitments.csv, practice_progress.csv, etc.).

Markdown: human-readable narrative "recovery record" — your sobriety dates, your commitments completed, your check-in trends, your practice modules done. Suitable to share with a sponsor or therapist.

Tables included:

user_memory (stable_profile, recent_summary, event_log)

app_settings

check_ins

commitments

practice_progress, practice_choices, practice_scenario_feedback (V4.1)

Saved synthesis paragraphs (those user opted to save)

Privacy:

Phone numbers excluded from exports by default. Settings option to include them in user's own export.

AI-generated content is labeled as such in the export (e.g., synthesis paragraphs marked "generated").

Export logs an export_generated event without including user content in the log.

Account deletion (already supported but reaffirmed): full deletion removes everything, including backups. User can request and confirm.

Memory Search Lite

Search event_log by keyword and filter by date or kind. Used to power chat queries like "when has this happened before?" or "what helped last time?".

Backend helper:

function getRelevantPastEvents(

query: string,

filters: { kind?: string; dateRange?: [Date, Date] },

limit: number

): Promise<EventLogEntry[]>

Scoring is deterministic: keyword match in summary, kind match boost, recency boost, actor=user boost (when actor field exists per V5.4 expansion). No AI used in search.

Chat integration:

Memory Search Lite is invoked from chat only when the user explicitly asks something memory-shaped: "when has this happened before?", "what helped last time?", "do I have a pattern with this?", "have I felt this before?"

Detection is keyword/intent based, not AI inference.

Results are summarized into the chat response via the existing buildChatSystemPrompt flow with retrieved events appended to memory context. Phone numbers and raw notes excluded.

Old events are not auto-injected into normal chat. Only on memory-search intent.

Optional UI: search box and filters in the existing Memory screen. Defer if mobile UI bandwidth is tight.

Memory source labeling

Existing user_memory.event_log shape is three keys (type, summary, timestamp). V5.2 does not modify this. V5.4's event taxonomy expansion is where actor / source / kind get added.

In V5.2, Memory Search Lite filters by 'type' (the existing field). When V5.4 ships, it gains actor/source filtering as an additive enhancement.

Schema impact

No new tables for V5.2.

Export endpoints added (server-side).

event_log gains 'export_generated' as a new type.

Risks

Export size for long-term users. Mitigation: streaming generation; size warning; resumable downloads if very large.

Phone number leak in exports. Mitigation: default exclusion; explicit opt-in; tested redaction.

Memory Search Lite over-injection in normal chat. Mitigation: invoked only on explicit memory-shaped queries; tested.

False matches in keyword search. Mitigation: results displayed as "possibly relevant past events" not asserted as definitive matches.

6. V5.3 — Recovery Protocols and Habit Architecture

Goal: handle the highest-stakes user state (relapse) carefully, and add optional low-friction habit support that doesn't compete with the main daily check-in.

Estimated effort: 3 weeks solo (mostly copy work and edge-case handling, not engineering).

Relapse Response Protocol

Triggered when the user reports not sober today in the existing structured check-in, or directly opens "I already slipped" via Practice's need-state entry, or via a new Home affordance.

Flow:

Acknowledge without shame.

Run existing risk classifier on any free text. If crisis: standard crisis card, stop normal flow, route to SOS.

Offer human contact shortcuts via SOS / handoff.

Ask what happened in plain language if appropriate. Free text or skip.

Offer one cleanup action: drink water and eat something simple, remove substances from immediate reach if relevant and safe, text a saved sober contact, open a meeting link, set next check-in for later today, write one honest sentence.

Offer tracker reset confirmation. Do NOT auto-reset. User explicitly confirms.

Save compact event_log entry: tracker_reset (existing in V3.7 if applicable) and a relapse_response_completed event. No raw confession text stored.

Suggest next check-in time.

Approved copy (use or adapt; framing only, not script):

"I'm glad you told the truth. This is not the moment for shame."

"First we make sure you are safe. Then we take one repair step."

"This does not erase the work you have done. It does mean today needs honesty and support."

"Do you want to reset the tracker now, or decide after you contact someone?"

"One repair step is enough for this moment."

Forbidden copy (enforced at prompt template level):

"You failed."

"You lost everything."

"Start over from zero."

"You ruined your progress."

"Relapse risk detected."

AI assembly: dialogue inside the protocol uses buildChatSystemPrompt with surface = 'chat' but with a special protocol_context that loads the approved copy bank as a positive constraint and the forbidden copy as a hard negative constraint. The chronic-relapse experience-level voice from V4 applies automatically and matters most here.

Tracker reset:

Explain clearly what reset means: "This will set your alcohol day count back to 0. Your total clean days across all attempts is preserved."

Require user confirmation.

Do not reset automatically.

After confirmation, log compact event_log entry with kind: tracker_reset.

Sponsor message drafting

Optional addition to Relapse Response Protocol: pre-written templates for common moments ("I had a slip last night and want to talk", "craving help", "resentment", "gratitude", "update").

User picks a template, edits if desired, then taps to copy or open in Messages with a saved contact prefilled. Per V3 invariant, never auto-sends.

This is a Predictive Features doc item that survives V4 absorption. Cheap to add as part of V5.3.

Evening Reflection

Optional end-of-day prompt, separate from the main check-in:

"One win today." Free text, ~50 chars.

"One thing to do differently tomorrow." Free text, ~50 chars.

Two fields. ~30 seconds. Stored in event_log with kind: evening_reflection (new type, three-key shape preserved).

Surfaces in weekly summary email if enabled.

No AI response. Pure logging.

Trigger: optional end-of-day notification (configured time per user, default 9pm) OR a Home affordance late in the day. Notification opt-in.

Micro Check-Ins

Only if the daily check-in feels heavy in production. V5.3 ships this as a feature flag, not enabled by default.

10-second pulse check between full check-ins.

Three taps: mood selector, craving rating, one optional word.

No AI response. Pure logging.

Surfaces in event_log with kind: micro_checkin.

If shipped, micro check-ins must not compete with the main check-in. UI placement is below primary actions, clearly labeled "quick pulse — not a full check-in."

Commitment Streak

Track days of follow-through on commitments separately from sobriety streak.

Days where the user completed at least one due commitment count as on-streak.

Days with no due commitments don't break the streak.

Days with due commitments and no completion break the streak.

Display: small text in Insights, not on Home. "You've followed through on commitments [N] days running."

No notifications. No streak shame. The number is for self-awareness, not pressure.

Schema impact

event_log gains: relapse_response_completed, evening_reflection, micro_checkin. Three-key shape preserved.

No new tables in V5.3.

commitment_streak is computed from existing commitments table; no storage.

Risks

Forbidden copy slipping through. Mitigation: prompt template includes explicit forbidden list; tested with adversarial inputs; voice eval covers relapse scenarios.

Tracker reset confusion. Mitigation: clear copy on what reset does; confirmation required.

Evening reflection becoming homework. Mitigation: optional, no notification by default, no shame for skipping.

Micro check-ins fragmenting the daily ritual. Mitigation: feature flag; ship only if production demand.

Commitment streak becoming streak shame. Mitigation: hidden from Home; no notifications; framed as self-awareness.

7. V5.4 — Polish, Expansion, and Optional Differentiators

Goal: address the lower-priority items from old planning docs, expand event taxonomy if production data warrants, add step work integration if user demand exists.

Estimated effort: variable. V5.4 is a basket of optional features. Pick based on production signal after V5.0–5.3 ship.

Event Taxonomy Expansion

V3.7 event_log has three keys (type, summary, timestamp). V5.4 may add actor, source, kind as optional fields, additive and backward-compatible.

New shape (additive):

type EventLogEntry = {

type: string;          // existing

summary: string;       // existing

timestamp: string;     // existing

actor?: 'user' | 'system' | 'ai' | 'scheduler';   // V5.4

source?: string;       // V5.4

kind?: string;         // V5.4

};

Old entries stay as-is. New entries written by V5.4-aware code include the new fields. Memory Search Lite filters by actor/source when present.

Why optional and not a hard migration: the V3.7 shape works for current consumers. Migration of 90+ entries per user is fine but unnecessary. The benefit (filtering, governance) is realized only for new entries; old entries are functionally fine without the metadata.

Milestone Intelligence

When the user crosses a milestone, generate a brief reflection grounded in their own data:

"You hit 30 days. Your craving average this month was 3.2, down from 6.1 in week one. The thing that moved most: sleep."

Computed deterministically from check-in data; phrased via buildChatSystemPrompt.

Surfaces as a one-time card on milestone day. Not a recurring thing.

Quiet acknowledgment, not fanfare. Per V4 voice rules.

This is the milestone celebration that matters: not a confetti animation, but a sentence about what the user actually did.

Step Work Integration (Optional, if user demand exists)

Optional prompts based on AA/NA/SMART/current program.

Settings field: which step the user is on (free text, optional).

Occasional prompts in Chat or Check-In tied to the current step (e.g., "You mentioned you're working step 4. Want to journal one resentment now or save it for later?").

Not a replacement for sponsor work. Supplement only.

Content design is the hard part. Defer until a content collaborator is available or until production data shows clear demand.

Emotion wheel check-in

Optional alternative to the 1-10 mood slider:

Visual emotion wheel (Plutchik or similar).

User taps where they are; richer emotional data than a number.

AI uses the specific emotion in its response via buildChatSystemPrompt's existing flow.

Settings option: "Use emotion wheel instead of mood slider."

Engineering effort: small. UX design effort: medium. Worth it only if mood-slider data turns out to be a poor signal.

Resentment tracker, gratitude bank, trigger mapping

Three Predictive Features candidates that are real but optional:

Resentment tracker: dedicated space to log resentments with structured fields. The AI helps process via existing chat flow. Useful for 12-step users; optional otherwise.

Gratitude bank: cumulative storage of gratitude entries. On hard days, surface 3 random past entries. Pattern: gratitude entries correlate with lower craving following day; surface this if data supports it.

Trigger mapping: aggregate existing trigger tag data into a personal heatmap or ranked list. "Loneliness and comparison show up together 70% of the time before your hardest days."

Each is its own small feature. Pick based on user requests after V5.0–5.3 ship.

"Pattern narrative" weekly summary upgrade

Existing weekly summary email becomes more grounded: not just stats but a narrative tied to data. "Over the last 90 days, your hardest weeks were when sleep dropped below 6 hours AND you missed a meeting in the same week. Your strongest weeks had one thing in common: you called someone on Monday."

Built on the V5.1 Pattern Insight Engine (extended to 90-day windows). Renders the email via buildChatSystemPrompt with a new surface variant 'weekly_summary'.

Schema impact

event_log: actor/source/kind become optional fields (V5.4 only writes new entries with them).

Possible new tables: resentments, gratitude_entries (V5.4 add-ons; only if shipping).

stable_profile may gain: current_step (string, optional), use_emotion_wheel (boolean, default false). Per V4 schema lock, these require explicit authorization.

8. What V5 Is Not

V5 is not a rewrite. It builds on V3.7, V4, and V4.1.

V5 is not a multi-agent or vector RAG system. Both remain deferred.

V5 is not a wearable or biometric integration. Apple Health, Whoop, Oura, Hume voice analysis — all deferred.

V5 is not realtime voice. Defer until production usage justifies.

V5 is not a multi-user / accountability partner architecture. Single-user remains the assumption.

V5 is not a meeting-finder integration. Existing user-curated meeting_links remain the model.

V5 is not a custom check-in field system. Power-user feature; deferred to V6+.

V5 is not a complete event taxonomy refactor. V5.4 adds optional fields, not a hard migration.

V5 is not a step-work content library. Step Work integration is a hook for user-driven step tracking, not curated content.

V5 does not introduce engagement loops, streak shame, or social comparison patterns.

9. Build Sequencing

Suggested phase order:

V4: User Context Architecture. Prerequisite for everything.

V4.1: Practice Mode. Built on V4.

V5.0: Safety Access (SOS Mode + Offline Cache). 1–2 weeks.

V5.1: Pattern Insight + Drift Detection. 2–3 weeks.

V5.2: Trust and Memory (Data Export + Memory Search Lite). 2 weeks.

V5.3: Recovery Protocols and Habits (Relapse Response, Evening Reflection, Micro Check-ins, Commitment Streak). 3 weeks.

V5.4: Polish and Optional Expansion. Variable.

Total V5 effort: 8–10 weeks for V5.0 through V5.3, plus open-ended V5.4 work.

Reordering rules:

V5.0 can ship before V4.1. SOS Mode has no V4 dependency and improves safety access immediately.

V5.1 should follow V4.1 because it benefits from Practice's behavioral signals.

V5.2 (Data Export) can ship anytime after V4.1. Memory Search Lite benefits from V5.4 event taxonomy expansion but does not require it.

V5.3 (Relapse Response specifically) is high-value and can ship anywhere in the sequence after V4 stabilizes. Copy work is the bottleneck.

V5.4 is opportunistic. Pick based on user signal.

Production data after V4.1 ships should inform V5 phase order more than this spec does. If users heavily use Practice but rarely engage SOS, V5.0 may be lower priority than V5.1. If conversely, V5.0 jumps to first.

10. Open Questions

Should V5.1 Pattern Insight surface multiple cards over time (rotating insights) or always one primary? V5 leans one primary; rotation is V6 if needed.

Should the V5.3 Relapse Response Protocol auto-trigger Practice's "What to Do After a Slip" module after the cleanup action? V5 leans optional offer, not auto-trigger. Practice is opt-in.

Should the V5.2 Markdown export be shareable via a generated link (with expiry) or download-only? V5 leans download-only; sharing surface is its own product question.

Should V5.4 emotion wheel replace or supplement the existing mood slider? V5 leans Settings option to choose; both work the same downstream.

Should V5.4 milestone intelligence include cross-focus context ("You hit 30 days on alcohol. Your porn focus is at 47 days.") or single-focus only? V5 leans single-focus for clarity; cross-focus mention only if user has both at meaningful counts.

Should V5.3 commitment streak count practice module completions as commitments? V5 leans no; commitments and practice are different surfaces.

Should V5.4 step work integration support multiple programs simultaneously (a user doing AA steps + a SMART exercise)? V5 leans single program at a time, switchable.

11. Closing Note

V5 is what the old V4 master doc and Predictive Features wishlist actually become once V4 architecture exists. Most of the predictive UX features fold neatly into V5.1 Pattern Insight (because V4 made the assembled prompt aware of state changes, V5.1 just has to compute the signal and phrase the surface). Most of the personalization features were absorbed into V4 itself (because V4 added experience_level and recovery_method, the AI already speaks differently to a chronic relapser than to a first-attempt user without V5 having to do anything). The trust features are real and ship in V5.2. The recovery protocols are real and ship in V5.3. The high-complexity items (wearables, vector RAG, multi-agent, accountability partners) remain deferred.

V5 is a basket of small, well-scoped features. None of them require multi-week architectural work. All of them produce visible user value. The phase order should be informed by what V4.1 production data reveals.

V5.0 (Safety Access) is the one phase that should ship regardless of any other consideration. SOS Mode and Offline Safety Cache materially improve user safety without depending on AI inference, network availability, or any V4 surface. Build it first, regardless of whether V4.1 is stable.
