---
title: "Anchor Parked Items"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Active directives/Anchor Parked Items.docx"
status: active
privacy: working
tags:
  - product
---

# Anchor Parked Items

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Parked Items

Last updated: 2026-05-13 (session, afternoon)

These are known issues, deferred features, and decision threads that are not being built now. Review when the relevant trigger condition is met. Do not reopen without a clear reason.

Active blockers / follow-ups (review soon)

saved_syntheses export is empty Trigger: V5.2 Data Export (PR #66) Severity: MEDIUM Detail: The saved_syntheses table does not exist in Neon production. All three export formats (JSON, Markdown, CSV ZIP) return an empty placeholder for this section. Export still works for all other tables. When saved_syntheses is created, wire it into the export composers. Next action: Add saved_syntheses table when it becomes relevant, then update export composers. No code debt in the meantime — the per-table try/catch handles gracefully.

practice_ tables may not be in Neon production Trigger: V5.2 Data Export (PR #66) Severity: LOW Detail: Per-table try/catch returns [] if tables are missing. Monitor after merge — if practice exports are empty for all users, confirm Neon migration state.

reflectionRouter V5.3 omission Trigger: Fixed in PR #66 (routes/index.ts) Severity: Resolved Detail: The Evening Reflection router was never registered in V5.3. Fixed as part of V5.2 Data Export PR. Confirm /api/reflection/evening is responding in production after #66 merges.

Deferred features (no timeline)

Evening notification email for Evening Reflection Context: Follow-up to V5.3 sub-features PR. Not included in the V5.3 directive. Needs EMAIL_OUTREACH_ENABLED and a Resend template. Trigger: When Evening Reflection usage data shows users are missing the evening check-in.

Micro Check-ins Context: Explicitly deferred. Old Quick/Full implementation removed. Needs fresh design post-V5.2 stable. Trigger: Post-V5.2 production signal.

Memory screen search UI Context: V5.4 or later. Memory Search Lite is chat-triggered only for V5.2. No search box in Memory screen until behavior proves useful in production. Trigger: Post-V5.2 production signal.

V5.4 Polish basket Context: No spec. Parked until production signal on what actually needs polish. Trigger: UX audit report + real user feedback.

Home commitment display refresh lag (~5 seconds) Context: Commitment created from Practice Mode "Commit to this" appears on Home with a ~5 second delay. POST succeeds and success message shows correctly. Lag is a stale fetch/polling interval issue — Home is not triggering an immediate refetch after the POST succeeds in CompletionScreen. Fix: Trigger a Home data refetch immediately after the POST succeeds rather than waiting for the next poll cycle. Trigger: V5.4 polish pass.

Streaming export path Context: V5.2 Data Export is synchronous. If large accounts hit Fly request timeout, a streaming path is needed. Trigger: Timeout errors in production logs, or user reports of export failure on large accounts.

Infrastructure debt

AUTONOMY_LAYER ANCHOR-N: dev/prod path resolution pattern Context: __dirname points to dist/routes/ in production, not src/routes/. Non-JS assets at dist/data/ require explicit "data" segment in path join. Add on next AUTONOMY_LAYER pass.

Staging environment Context: Identified as missing infrastructure. No timeline set.

CI: seedUsers CommonJS/ESM interop Context: Playwright CI failing on named import from CommonJS seedUsers module. Fixed in commit b2d1670, merged with PR #65. Severity: Resolved

Parked concepts (post-Anchor-stabilization)

Sober Garden Context: Symbolic recovery garden app. Full v0.2 spec exists. Build after Anchor V5 is stable.

Practice Mirror app Context: Symposium Studios portfolio concept. Buildable in a 1-day Director Model window when a clean slot opens after Anchor V5 stable.

Eval Harness Context: Markdown phase only. Not today's project.

Decision debt carried forward

Auth for Expo Mobile V1 Decision: Email-only is locked. Sign in with Apple deferred. Confirm this has not changed when starting the mobile build.

Billing entity for Anchor Decision: Running under Eagle Rocket LLC for now. Review when Anchor has revenue or is being pitched.

saved_syntheses schema Decision: Table not yet created. When it is, update export composers and confirm V5.2 export wiring.
