---
title: "ANCHOR — Post V3 Field Test Backlog"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/ANCHOR — Post V3 Field Test Backlog.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# ANCHOR — Post V3 Field Test Backlog

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ANCHOR — Field Test Backlog v1

April 25, 2026

BUGS (fix first)

1.	“Ate enough today” defaults to Yes — pre-selected green on check-in form load. Should default to unselected like all other binary fields. This is also inflating the “Ate enough” stat in Recovery Habits (showing 100% / 3/3 days).

2.	Commitments this week showing 32 — query is not scoped to current week correctly. Likely counting all-time commitments or using wrong date boundary.

3.	Recent Patterns rendering raw markdown — the ### headers and **bold** text are rendering as literal characters instead of formatted text. Either render markdown properly or replace the AI-generated summary with a structured plain-text format.

4.	Recovery Habits not counting correctly — Insights shows 0/3 days for Meeting attended, Sober person contacted, Fellow called, Exercised — even when those were marked Yes during check-ins. Query may be broken or field mapping is wrong.

5.	Multiple check-ins in one day: binary fields not aggregating correctly — if you say “sober person contacted: no” in check-in 1 and “yes” in check-in 2, the second answer doesn’t override or average correctly. No defined algorithm for multi-check-in days. Needs explicit rule: last value wins for binary fields, average for numeric fields (mood, craving, sleep, energy, focus).

6.	Emails not working — scheduled outreach not sending. Investigate: is EMAIL_OUTREACH_ENABLED set to “true” in Replit Secrets? Is RESEND_API_KEY valid? Is the cron actually running? Test email endpoint works independently — use that to isolate.

7.	“Sober today” and “Ate enough today” should default to unselected — user should have to actively choose. No field should pre-select an answer. Consider applying this rule to all binary fields on the check-in form.

UX / FEATURES (do after bugs)

8.	Memory screen is read-only — no way to edit sober contacts, meeting links, or any profile fields without resetting onboarding. Need inline edit capability for: sober contacts (add/remove/edit), meeting links (add/remove/edit), and ideally all stable_profile fields.

9.	Multiple sober contacts in Reach Out — currently only shows one contact (Andrew). Should show all contacts from sober_contacts array. Nice-to-have: rotate suggested contact — “Maybe reach out to Andrew, David, or Vova” — so the app surfaces the whole network.

10.	“Find a meeting” should link somewhere useful — currently unclear where it goes. Should open AA Meeting Guide, Online Intergroup (aa-intergroup.org), or a configurable URL. Not a dead button.

11.	Light theme font contrast — some text hard to read on the light theme. Needs contrast audit, particularly on secondary/helper text.

12.	Meeting links section feels disconnected — currently sits inside Memory alongside contacts. Consider a dedicated “Meetings” section separate from sober contacts.

13.	Recent Patterns section utility unclear — even if markdown is fixed, the wall of AI-generated text is hard to parse. Consider replacing with a structured 3-bullet summary: top triggers this week, mood trend, one pattern worth noting. Or remove entirely and let Insights carry this.

14.	Event log — consider collapsing by default — raw event log visible in Memory is useful for debugging but not for daily users. Default collapsed with a “Show event log” toggle.

15.	Notes placeholder copy could be stronger — “Context, triggers, wins…” is fine but generic. Could be more inviting.

16.	Triggers / Feelings list — current list (fatigue, loneliness, comparison, boredom, conflict, resentment, anxiety, lust, financial stress, isolation, shame, anger, restlessness, overwhelm, grief, self-pity, pride, excitement, perfectionism, people-pleasing, avoidance, FOMO, hunger, physical pain, nostalgia) is actually solid. Low priority to change.

DEFERRED / FUTURE

17.	Onboarding V4 — deeper intake, more sober contacts during setup, coaching style preference. Schema changes required. Do not combine with any of the above.

18.	Native mobile app — PWA works but native would unlock push notifications, better audio, home screen presence. Long-term.​​​​​​​​​​​​​​​​
