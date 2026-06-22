---
title: "Anchor app user feedback + AI audits"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Audits/Anchor app user feedback + AI audits.docx"
status: reference
privacy: working
tags:
  - product
---

# Anchor app user feedback + AI audits

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Charlie 4/28/2026

Anchor app: n=1 product read

Honestly, this is starting to look like a real recovery companion, not just a pretty prototype.

The best thing I see from the screenshots is that the app gives you a mirror without becoming too complicated. It shows:

Mood rising today.
 Cravings moderate but manageable.
 Energy low.
 Focus improving.
 Sleep fairly steady.
 Eating mostly good.
 Sober contact still low.
 Meetings absent.
 Codependency/nicotine currently at zero-day vulnerability.
 Alcohol/weed/porn streaks showing meaningful early momentum.

That is useful. It gives the day a shape.

The strongest product insight is this:

Your subjective story says “I feel amazing.” The data says “mood 9, energy 4, cravings 4.”

That is gold.

Because the app catches the exact state where people get in trouble: high mood, low energy, moderate craving, relationship grief, and a sense of freedom. That combination can feel like clarity, but it can also become impulsivity if not contained. Anchor is doing the right thing by saying: mood is strong, energy is low, watch cravings, contact someone, write it down, attend a meeting.

That is not glamorous, but it is protective.

What is working well

The Insights dashboard is strong. The check-in streak, 7-day averages, commitment rate, and tracker streaks give you a quick sense of momentum.

The calendar colors are useful. Seeing green, yellow, red across days makes the week emotionally legible.

The habit section is very revealing. “Ate enough 5/6” is good. “Meeting attended 0/6” is important. “Sober person contacted 2/6” and “fellow called 1/6” show the social recovery layer is underbuilt.

The sobriety trackers are useful, especially because they separate alcohol, weed, porn, nicotine, codependency, masturbation, orgasm. That is not generic recovery. That is your actual relapse ecology.

The one move right now section is a good concept. It turns reflection into a single behavioral next step.

What I would improve

The language is a little too blunt in places. “Toxic dynamic” may be accurate, but the app should probably distinguish:

toxic dynamic
 from
 toxic person

That matters because you are trying not to demonize Yuni. A better line might be:

“Keep putting distance between you and the dynamic that has been destabilizing you.”

That is cleaner, less inflammatory, and less likely to turn grief into contempt.

The “reach out” card saying “Add sober contacts in Memory” is good product logic, but emotionally it feels like a dead end. If no contacts exist, it should offer a fallback:

“No sober contacts saved yet. Consider texting one trusted person, attending an online meeting, or writing a 5-minute note here.”

Also, the app should probably recognize high mood + low energy as a specific risk pattern. That combination deserves a distinct warning, because it can become overextension.

Something like:

“Your mood is high, but energy is low. Today’s risk is overdoing it. Keep plans simple and protect sleep.”

That would have been perfect for today.

The n=1 interpretation

Based on your screenshots, the app is already doing what it is supposed to do:

It helped you notice that today is not a pure celebration day. It is a moderate-risk recovery day hidden inside a beautiful island day.

That is exactly the point.

Mood 9 does not mean “go wild.”
 Energy 4 means “keep it measured.”
 Craving 4 means “watch the edges.”
 Codependency 0 days means “relationship contact is still a hot surface.”
 Nicotine 0 days means “do not add a casual cigarette because you’re island-walking.”
 Meetings 0/6 means “recovery community layer needs attention soon.”

That is a meaningful self-governance dashboard.

High Mood / Low Energy warning card

Something like:

“Your mood is high, but your energy is low. This can be an overextension risk. Keep plans simple, protect sleep, and avoid big decisions.”

That would have fit today perfectly.

Also, I’d soften “toxic dynamic” language to “destabilizing dynamic” in some places. It is cleaner and less likely to feed contempt.

Marcus 5/3/2026

Notes 5/3/2026

If a user picks a non-meeting based recovery program they should not have a 'meeting attended' box. That should only be for meeting-based programs.

Likewise, 'fellow called' and 'sober person contacted' are redundant and mean the same thing basically. 'Fellow' is a 12 step term too.

On 'trackers' might be nice to have a box with text that is customized to your day counts, AKA, 'keep going, you are only 10 days from a 30 days off alcohol milestone'.

On insights, a 'medals' section with awards for reaching milestones and getting check ins consecutively etc, keeping commitments, etc would be useful.

Also the 'meeting links' onboarding part should be skipped if not using a 12 step program.

Local deploy note:

Everything is working. Chat, check-ins, insights, all seem functional on local server. Note: server is a bit slow.

Claude Audit 5/3/2026

Anchor Codebase Audit — Action Plan

Source audit run May 3, 2026 by Claude Code background agent. Re-organized into buckets by Charlie.

The frame

The raw audit found ~50 issues. Most are real. Almost none are urgent. This document sorts them into what to do, in what order, against the V4 deployment doctrine. The doctrine: V4 is production, not features. Don't fix what isn't blocking the deployment arc unless it's a safety surface issue.

The audit is a snapshot. The codebase is fine. Real codebases always have 50 findings. The discipline is choosing what to act on.

Bucket 1: Pre-V4 critical (do before launch)

These three things should land before public launch. Each has a real reason that justifies acting before V4 doctrine would normally allow.

🚨 H3 — Crisis path silent downgrade on OpenAI outage

File: artifacts/api-server/src/routes/chat.ts:148-158, utils/v3helpers.ts:402

The hazard: If OpenAI's classifier API fails, the fallback returns risk: "moderate". A real crisis message during an OpenAI outage gets normal chat handling, never the crisis routing card with 988 resources.

Why this overrides doctrine: This is a recovery app. The single failure mode where someone in crisis gets handled as moderate distress is the worst possible silent failure. Recovery app safety surface is exactly the kind of thing where "wait for V4" is wrong.

Fix: Local keyword fallback on classifier error. Match against terms like 988, suicide, kill myself, overdose, hurt myself, end it. Bias toward crisis or high on error. Maybe 10-15 lines.

When: One focused session before Stage 2. Single PR, scoped to just this fix. Don't bundle anything else.

H1 + H2 — Auth gap (handled by Stage 3)

Status: Already on the deployment path. Stage 3 of the deployment plan is the multi-user code refactor that replaces the dev_user shim with real Supabase JWT auth. Once that lands, H1 (open CORS + single-user) and H2 (SSRF on email/test) are both closed.

No additional action required. Just don't skip Stage 3 or rush it.

P1 — api-server has no watch mode in dev

File: artifacts/api-server/package.json:7

The friction: Every change requires manual restart. Restart triggers full esbuild bundle (3.7 MB output). This is the "slow vs Replit" feel you flagged today.

Why this is pre-V4: Not a hazard, but a developer-experience tax. You'll spend the next two weeks doing Stage 2-11 work. Cutting restart time from "rebuild everything" to "tsx hot-reload" pays for itself in friction reduction over those weeks.

Fix: Switch dev script to tsx watch src/index.ts. Keep build.mjs for production builds only. Possibly 15 minutes of work.

When: Soon, but not tonight. Could be a "first 30 minutes of a fresh session" warm-up task before Stage 2.

Bucket 2: Stage 3 prerequisites (handle during multi-user refactor)

These items belong inside the Stage 3 work. They are not separate tasks. Mention them in the Stage 3 prep but don't act on them in isolation.

B2 — Drizzle schema default user_id drift

check_ins.ts:39 and sobriety-trackers.ts:20 default to "maxwell"; everything else defaults to "dev_user". Already flagged as W1 from your Stage 1 staging report.

Stage 3 action: Drop both defaults entirely. With real auth, no insert should rely on a default. Belongs in the same PR as the auth wiring.

B5 — requireAuth triple-any defeats type safety

app.ts:41-44. The auth middleware uses any casts that prevent the compiler from catching missing auth on new routes.

Stage 3 action: Add Express type augmentation via declare module "express-serve-static-core" so req.userId is properly typed and missing-auth becomes a compile error.

N3 — Magic strings "dev_user" / "maxwell" repeat across schema files

Stage 3 action: Promote to DEFAULT_USER_ID constant in a shared location, then drop entirely once auth is wired.

Test coverage gaps for cross-user isolation

Stage 3 action: Section 6.9 of your deployment plan already specifies the cross-user isolation tests that must be added during Stage 3. The audit just confirms there's no current coverage.

Bucket 3: Pre-launch hardening (do before Stage 11 smoke test)

These are real correctness issues that should be cleaned before declaring production-ready. Each is small. None blocks earlier stages.

H4 — runMigrations() has no advisory lock

api-server/src/index.ts:23-155. Two instances booting in parallel during a rolling deploy could interleave the dedupe DELETE and lose data.

Fix: Wrap in pg_advisory_lock(<int>) ... pg_advisory_unlock(...). Or — better long-term — move to one-shot Drizzle migrations and stop running migrations on cold start at all.

When: Before Stage 4 (Fly deploy). Cold-start migrations on Fly with min_machines_running=1 won't hit this often, but a rolling deploy could.

H6 — Tracker reset is not atomic

routes/trackers.ts:81-113 and 181-198. Two-step DB writes without transaction. Same shape in tracker delete.

Fix: Wrap in db.transaction(). ~5 lines per route.

When: Before launch. Phantom reset rows in production data are bad.

B11 — commitments table missing withTimezone: true

schema/commitments.ts:9-11. Every other table uses { withTimezone: true }; commitments doesn't. Currently works because server is UTC, but will silently shift if the deployment region's TZ changes.

Fix: Add { withTimezone: true }, run a migration. ~5 lines.

When: Same PR as H6 or its own focused commit.

H5 + H7 — Email scheduler reliability

emailScheduler.ts. H5: window-based send logic can miss a day on cron drift. H7: two paths for "days since check-in" can disagree on TZ rollover.

Fix: Date-anchored "is reminder due AND not yet sent" check, with single source of truth for last-checkin date.

When: Before Stage 6 (enable email outreach). Until EMAIL_OUTREACH_ENABLED=true, this code is dead.

B4 — Insights streaks reset on UTC midnight, not user TZ

routes/insights.ts:33-74. PST user checking in at 9pm sees streak drop at 4pm next day (UTC midnight).

Fix: Read stableProfile.timezone and use it for day boundaries.

When: Before launch. User-facing correctness issue.

B6 — Memory-write fallback silently masks DB outage

v3helpers.ts:148-205. On DB error returns a fake empty memory row. Frontend acts as if user has no profile.

Fix: Return 503 instead of fake data.

When: Before launch. Silent data loss potential.

Bucket 4: Local dev quality of life (do whenever bored or stuck waiting)

These are perfect "while-waiting-on-something" tasks. Low stakes, no production impact, and they remove friction that's been mounting.

R1 — Delete lib/integrations/openai_ai_integrations/

Zero hits in source. Duplicate of lib/integrations-openai-ai-{server,react}. Remove the workspace entry from pnpm-workspace.yaml:40.

R2 — Delete artifacts/mockup-sandbox if unused

Confirm unused first. If yes, delete. Reduces install surface.

R5 + R10 — Delete attached_assets/ and the unused @assets Vite alias

40+ Replit prompt history files, ~30MB of bloat. The Vite alias points at it but no source uses @assets. Move outside repo or delete.

R4 + N1 + N2 — Dead imports cleanup

settings.ts:3 imports unused checkInsTable, sobrietyTrackersTable, sql. commitments.ts:2 imports unused gte. Delete the import lines.

N6 — Dead clerk Tailwind layer

index.css:1 declares @layer theme, base, clerk, components, utilities. The clerk layer is leftover from the Clerk era. Remove.

N7 — Replit residue in .replit

VITE_CLERK_PUBLISHABLE_KEY line 56 and the broader Clerk env block. Already flagged earlier today. Remove.

N10 — User-facing copy still says "Replit Secrets"

checkin.ts:221, email.ts:114 reference Replit. Misleading on local dev or production.

Total time estimate for this whole bucket: A focused 30-45 minute pass would knock out most of it. Or spread across multiple bored-while-waiting moments.

Bucket 5: Post-launch / V4.1 (file and forget for now)

These are real findings that don't justify pre-launch work. File them, revisit during Phase 3 (real usage signal-gathering) or V4.1 planning.

Architectural refactors (M-L effort, defer)

R7 — checkInsTable is a 22-field god table. Splitting ai_* fields into check_in_results would help, but only if you're touching that area for other reasons.

R8 — Mix of raw pool.query and Drizzle in scheduler. Standardize on Drizzle.

R9 — api-spec → api-zod → api-client-react pipeline is half-adopted. Decide whether to finish or rip it out.

R3 — Three near-identical /api/speak fetch sites. Consolidate into a useTtsButton hook.

R6 — Email helpers duplicated across two files. Extract to utils/email-core.ts.

Frontend bloat

P6 — 25 Radix UI packages, many likely unused. Prune to actually-imported.

P7 — Two charting libraries (chart.js + recharts). Pick one.

P8 — Replit-specific dev plugin (runtimeErrorOverlay) loads unconditionally. Gate on REPL_ID.

Performance (only if real users hit them)

P3 — DB pool has no connection limits. Add max, idleTimeoutMillis, connectionTimeoutMillis.

P4 — /api/insights/stats has N+1 on tracker_resets. One join query instead.

P5 — /api/checkin/today runs count(*) on every Home view. Cache totalCheckIns on app_settings.

Correctness edge cases

B1 — messages.ts and conversations.ts are orphan schema files. Delete.

B3 — Duplicate-tracker dedupe runs forever on every boot. Gate behind a flag or one-time migrate.

B7 — transcribe.ts extension parsing breaks on mobile Safari. Explicit mime-to-ext allowlist.

B8 — Speak route fallback retry burns budget on aborts. Don't retry on abort.

B9 — PATCH /api/checkin accepts unbounded mood/energy/craving. Add Zod validation.

B10 — last_summarized_at_event_count not advanced on parse-fail. Repeated bad LLM output → repeated cost.

H8 — DELETE /api/memory/event/:index uses array-index identity, can race with appendEventLog. Optimistic concurrency or move to a real table.

H9 — runBackgroundTasks race on recentSummary regeneration. Advisory lock.

H10 — /api/checkin backfillDate parsing accepts any date. Bound to a sane window.

Observability

N4 — console.log mixed with pino. JSON log shipping won't capture uniformly.

N5 — 100-line system prompt inline in chat.ts. Move to prompts/chat.system.txt.

N8 — loadUserMemory logs console.error per-request on DB outage. Flood risk.

N9 — safeBackgroundTask swallows errors with no metrics.

Bundling

P2 — The whole api-server is bundled into a 3.7 MB single file. No reason to bundle a Node server. Set packages: 'external' in esbuild, or drop bundling for dev (covered by P1).

Test coverage gaps to address during Stage 3

These belong in the Stage 3 testing pass per your deployment plan section 6.9, not as standalone work:

Crisis routing in chat and check-in (highest priority, ties to H3)

Cross-user isolation tests (Stage 3 mandate)

Tracker reset/delete atomicity (ties to H6)

Memory event ordering and concurrent updates (ties to H8, H9)

runMigrations idempotency (ties to H4)

PATCH /checkin/:id bounds (ties to B9)

Timezone-sensitive insights (ties to B4)

/api/transcribe multipart/mimetype handling (ties to B7)

Backend has zero unit tests today. Stage 3 is the natural moment to add them.

My recommended order, in plain English

This week (before Stage 2):

H3 crisis fallback. One focused session, single PR. Most important thing on this list.

P1 tsx watch mode. ~15 minutes. Removes friction for the next two weeks of deployment work.

During Stage 2 (Supabase setup): 3. No audit work. Stage 2 is dashboard work, not code.

During Stage 3 (multi-user refactor): 4. Bucket 2 items (B2, B5, N3, cross-user isolation tests). All inside the Stage 3 PRs.

Bored-while-waiting moments throughout: 5. Bucket 4 cleanup items. Low stakes wins.

Before Stage 11 (production smoke test): 6. Bucket 3 hardening (H4, H6, B11, H5, H7, B4, B6).

Post-launch, Phase 3 signal-gathering: 7. Bucket 5 items, in the order real users surface them as problems.

What to do tonight

Nothing. Save this doc. Wrap the session. Sleep on it. Tomorrow morning, decide whether H3 deserves a focused session this week before Stage 2 starts. That's the only audit-driven decision worth making in the next 24 hours.

The audit is a tool, not an obligation. The doctrine holds.

Charlie 5/9/26 product viability

Yes, I think Anchor is commercially viable, but not as “another sobriety tracker.”

It is viable if the positioning is:

A recovery self-governance companion that helps people notice patterns, tell the truth, and interrupt drift before it becomes relapse.

That is much more interesting than:

streak counter + daily quote + AA-ish check-in.

The market need is real. SAMHSA reported that in 2024 only about 19.3% of people who needed substance use treatment received it. That leaves a huge population between “I need help” and “I am in formal treatment.”   There are also market reports projecting strong growth in addiction recovery companion apps, though I would treat exact market-size numbers cautiously because those reports can be salesy.

Your wedge is not “sobriety app.” Your wedge is:

I need something with me at the exact moment I start lying to myself.

That is where mobile matters.

Native iOS makes sense because recovery moments happen away from the laptop: bed, scooter, restaurant, beach, bathroom, party edge, craving window, post-date shame spiral, 11 p.m. loneliness, waking dopamine desert. The app needs to be in the pocket, not just in a browser tab.

But your instinct is right: shared backend first. The architecture should be:

One account. One backend. Multiple surfaces.

Web app for desktop/reflection/admin.
 Mobile app for check-ins, urges, reminders, voice, quick logging, emergency grounding.
 Same user, same memory, same event log, same scores, same daily rollup.

I would not build “standalone iOS only.” That traps the product. The real asset is the longitudinal recovery graph and self-governance memory. The clients are just access points.

Commercially, I’d see the path like this:

Phase 1: Web MVP proves the loop.
 Can a real user check in daily? Does the app catch drift? Does it feel meaningfully better than journaling alone?

Phase 2: Mobile companion.
 Not full rebuild. Build the smallest native iOS experience around the highest-frequency actions: check in, urge button, daily score, streaks/counters, sponsor-style reflection, reminders, maybe voice.

Phase 3: Paid personal plan.
 Something like $8–15/month if the product is genuinely useful daily. Maybe higher later for advanced memory, analytics, audio, exports, or coach/clinician-facing features.

Phase 4: Optional B2B/B2B2C.
 Sober living houses, coaches, therapists, recovery communities, treatment alumni programs, accountability groups. But don’t start there too early. B2B will demand compliance, dashboards, procurement, and trust.

The biggest caution: be careful with medical claims. Apple’s App Store guidance has specific scrutiny around health, safety, medical, and regulated medical-device categories, and Apple separately notes that apps used for diagnosis, prevention, monitoring, or treatment of diseases may require regulated medical-device status depending on jurisdiction.   So Anchor should not initially present itself as “treatment,” “medical relapse prevention,” or a replacement for clinicians/sponsors/emergency care. Position it as self-reflection, recovery support, journaling, pattern awareness, and personal accountability.

My honest commercial score:

Current web MVP: 5.5/10 commercially viable.
 Useful proof, not enough distribution or polish yet.

With working production check-ins, real users, and daily retention evidence: 7/10.

With native iOS, strong onboarding, push reminders, urge mode, voice check-ins, and clear non-AA positioning: 8+/10.

The strongest product insight is the one you are living right now: recovery is not just “days sober.” It is moment-to-moment governance of replacement behaviors. YouTube, coding, sex, spending, AA identity, food, travel, gym, romance, all of it. If Anchor can track the whole substitution economy without becoming preachy or clinical, that is a real product.

But not today.

Today’s phronesis: close the web app gate first. Then write the mobile architecture spec. Native iOS is probably right. It is just not the next task before Stage 11 is clean.

5/9 Charlie AA dominance fix

The big Anchor correction is:

Stop assuming 12-step as the default recovery ontology.

Better onboarding:

What kind of recovery path are you on?

Then options like:

12-step / meetings
 Secular recovery
 Spiritual but not 12-step
 Virtue ethics / self-governance
 Harm reduction
 Not sure yet

And if they choose “not sure” or “no program,” Anchor can say something like:

“That’s okay. We can help you build a practical recovery structure. We recommend starting with a virtue-based self-governance path: daily check-ins, triggers, body care, honesty, restraint, repair, and purpose.”

Then high-risk help should match the user. A 12-step person can get meeting links. A secular person can get coping plan / support contact / grounding / crisis resources. A virtue-ethics person can get return-to-body, sophrosyne, repair, next right action, self-governance prompt. Same safety seriousness, different container.

That is a real product insight.

Marcus Feedback 5/10/2026

M1 : Should have more options like “Opiates”, “Cocaine”.

M2: When you click “Other” the cursor should automatically go to the text box below it to save one click.

M3: Phrasing changes: Change “When did each one begin?” to “Let’s set up your trackers”

“When did you stop XYZ?” should be “When was the last time you had a slip with XYZ?”

That is better phrasing. Saying stopped assumes the person will stay stopped, a lot of people are struggling, slipping. Makes more sense to me.

M4: Date picking widget and time picking widget. There’s got to be a JS library with a better UI/UX for this on desktop and mobile.

M5: Change “Do you follow a recovery program” to “Please select a program to tune your recovery experience”. And “Pick the one that fits, or skip for now.” to “Select at least one, or select ‘No program’, don’t worry, you can change it later.”

M5a: Too many programs. Should just have: 12-step. Non 12-step, No program. Other. Only one of those three is selectable then it takes you to a screen to refine the choice. Note: on that second refining screen user can pick multiple programs.

M5b: Then IF 12 step is picked, list all the major 12 step programs on a separate screen, still step 5 just new options: Alcoholics Anonymous (AA), Narcotics Anonymous (NA), Al-Anon Family Groups (Al-Anon), Overeaters Anonymous (OA), Cocaine Anonymous (CA), Adult Children of Alcoholics (ACA), Gamblers Anonymous (GA), Co-Dependents Anonymous (CoDA), Sex Addicts Anonymous (SAA) / Sex and Love Addicts Anonymous (SLAA), Crystal Meth Anonymous (CMA), Heroin Anonymous (HA) / Pills Anonymous (PA), Emotions Anonymous (EA), Sex and Porn Addicts Anonymous (SPAA), Marijuana Anonymous (MA). NOTE: Users can pick more than one 12 step program. 

IF Non 12-Step is picked, list all these: SMART Recovery, LifeRing Secular Recovery, Women for Sobriety (WFS), Secular Organizations for Sobriety (SOS), Refuge Recovery, Moderation Management (MM), Recovery Dharma 

IF No Program is picked: Church / Religious Devotion, Virtue Ethics, Buddhism, Stoicism, Mindfulness Meditation, Natural Recovery (Spontaneous Remission), Existential Philosophy, Traditional Indigenous Healing, Holistic Wellness Practices, Self-Guided Study (Bibliotherapy), None.

IF None is picked

M5c: Logic for backend, the prompts should all be customized based on what program(s) they are in. The backend should know the program(s). Open AI should know it in the set-up and back and forth in chat. This is important. This requires a full rewrite of the logic system and creating a bank of new prompts for each program. And logic to smash them together if multiple are selected.

M5d: Make the Any Regular Meetings page gated first by a “Would you like to add meeting links for online meetings you attend?” with a “Yes” and “No button” as well as a “Find Meetings” button that opens the online meeting website for whatever program you have attended IF and only IF there is a website in the backend for that program, otherwise don’t show the “Find Meetings” button at all.

Data for this: "Program or non program Name","Has Meetings (Y/N)","Online Meeting Website Link (if exists)","In person meeting finder link (if exists)","Official program or organization website (if exists)","Has Sponsor concept in program (Y/N)"

"Alcoholics Anonymous (AA)","Y","aa-intergroup.org/meetings/","aa.org/meeting-guide-app","aa.org","Y"

"Narcotics Anonymous (NA)","Y","virtual-na.org","na.org/meetingsearch","na.org","Y"

"Al-Anon Family Groups","Y","al-anon.org","al-anon.org","al-anon.org","Y"

"Overeaters Anonymous (OA)","Y","oa.org","oa.org","oa.org","Y"

"Cocaine Anonymous (CA)","Y","ca.org/meetings","ca.org/meetings","ca.org","Y"

"Adult Children of Alcoholics (ACA)","Y","adultchildren.org/virtual-meetings-calendar/","adultchildren.org/meeting-search/","adultchildren.org","Y"

"Gamblers Anonymous (GA)","Y","gamblersanonymous.org/virtual-meetings/","gamblersanonymous.org/find-a-meeting/","gamblersanonymous.org","Y"

"Co-Dependents Anonymous (CoDA)","Y","coda.org/find-a-meeting/online-meetings/","coda.org/find-a-meeting/","coda.org","Y"

"Sex Addicts Anonymous (SAA) / Sex and Love Addicts Anonymous (SLAA)","Y","slaafws.org/meetings/","slaafws.org/meetings/","slaafws.org","Y"

"Crystal Meth Anonymous (CMA)","Y","crystalmeth.org/meetings/","crystalmeth.org/meetings/","crystalmeth.org","Y"

"Heroin Anonymous (HA) / Pills Anonymous (PA)","Y","virtual-na.org (HA)","pillsanonymous.org/find-a-meeting (PA)","pillsanonymous.org (PA)","Y"

"Emotions Anonymous (EA)","Y","emotionsanonymous.org","emotionsanonymous.org","emotionsanonymous.org","Y"

"SPAA (sex and porn addicts anonymous)","Y","spaa-recovery.org","spaa-recovery.org","spaa-recovery.org","Y"

"MA (Marijuana anonymous)","Y","ma-online.org","ma-sandiego.org","marijuana-anonymous.org","Y"

"SMART Recovery","Y","meetings.smartrecovery.org","meetings.smartrecovery.org","smartrecovery.org","N (Facilitators)"

"LifeRing Secular Recovery","Y","meetings.lifering.org","meetings.lifering.org","lifering.org","N (ePals)"

"Women for Sobriety (WFS)","Y","womenforsobriety.org/meetings/","womenforsobriety.org/meetings/","womenforsobriety.org","N"

"Secular Organizations for Sobriety (SOS)","Y","sos-nys.org","sossobriety.org","sossobriety.org","N"

"Moderation Management (MM)","Y","moderation.org","moderation.org","moderation.org","N"

"Refuge Recovery","Y","refugerecovery.org","refugerecovery.org/start-a-new-in-person-meeting","refugerecovery.org","Y (Mentorship)"

"Recovery Dharma","Y","recoverydharma.online","recoverydharma.org/meetings/","recoverydharma.org","Y (Wise Friends)"

"Buddhism (Buddhist Recovery Network)","Y","buddhistrecovery.org/recover/online-meetings/","buddhistrecovery.org/meetings","buddhistrecovery.org","Y (Mentorship)"

"Mindfulness Meditation","N","N/A","N/A","N/A","N"

"Church / Religious Devotion (Celebrate Recovery)","Y","celebraterecovery.com/weekly-online-recovery-meetings/","crlocator.com","celebraterecovery.com","Y (Christ-centered sponsors)"

"Traditional Indigenous Healing (Wellbriety)","Y","wellbriety.com/circles.html","wellbriety.com/circles.html","wellbriety.com","Y (Firestarters)"

"Stoicism (Stoic Recovery)","Y","stoicrecovery.com","stoicperformancerecovery.com","stoicrecovery.com","N"

"Virtue Ethics","N","N/A","N/A","N/A","N"

"Existential Philosophy","N","N/A","N/A","N/A","N"

"Holistic Wellness Practices","N","N/A","N/A","N/A","N"

"Natural Recovery (Spontaneous Remission)","N","N/A","N/A","N/A","N"

"Self-Guided Study (Bibliotherapy)","N","N/A","N/A","N/A","N"

M5e: Possible bug, daily summary emails have never landed. Not sure if these are created or not but I’ve yet to receive one. Test emails work but look terrible, need to make a new test email template.

M5f: New card structure for Yes No questions. 

IF Morning. No cards. 
drop morning cards entirely.

Midday

Have you eaten today?

Have you spoken to another person today?

Have you had a moment to yourself today?

Evening

Did you move your body today?

Did you attend any recovery support today?

Did you reach out to someone who supports your recovery today?

Did you eat enough today?

Did you do something that was good for you today?

Update the backend to track these. 



M5g: If someone selects “no” for “Sober Today” it should ask them which sobriety(s) they need to reset. Not sure if that is in the app yet but we need to check and add it if not.

M5h: https://www.sobrietyanchor.com/insights on desktop the calendar section is way too big. Remake it to be much smaller and actually useful. It takes up the whole screen right now.

M5i: Redo Triggers/Feelings.
Have two sections, one in a lightly green outlined box one in a lightly red outlined box. Positive ones in one, negative in another. These words all need to be sent to the chat prompt if they chat with the AI and saved in history of that check in.

Negative States Label: Triggers & Risks

Fatigue, loneliness, boredom, conflict, resentment, anxiety, financial stress, guilt, shame, anger, restlessness, overwhelm, grief, hopelessness, overconfidence, perfectionism, people-pleasing, avoidance, FOMO, hunger, physical pain, nostalgia, stress, burnout, apathy

Positive States Label: Anchors

Gratitude, serenity, motivation, connection, optimism, pride, energy, groundedness, relief, clarity, joy, resilience, accomplishment, contentment, celebration, peace, empowerment, excitement

M5j: When you click the check in button “Checking risk level…” should be changed to “Crunching data…”

5/10/2026 Post Check in Screen

5/10/2026 Post Check in Screen

Post Check-In Completion Screen — Redesign Spec

Design principle: The check-in is done. This screen is a moment of landing, not a report. One reflection. One signal. One question. Two CTAs. Everything else is removed.

Section 1 — Header (minimal)

"Check-in complete." Unchanged.

Below it, one quiet streak line: 12 days · Alcohol — small, muted text, no animation, no celebration mechanics. Just the number as a grounding anchor. If multiple trackers are active, show the primary one or the longest streak. Not both.

Remove "Here's your reflection." as subtitle — it's redundant when the reflection follows immediately.

Section 2 — The Reflection (single card)

One AI-generated paragraph. No sub-headers. No split into WHERE YOU'RE AT / SOMETHING TO WATCH. The AI speaks in one voice, one block.

Craving risk rendered as a small inline badge at the bottom of this card only: ● Moderate — dot color keyed to level, one word, no section header, no separate card.

TTS moves here too: small speaker icon in the top-right corner of the card. Remove the full-width "Listen to full summary" button at the top of the page entirely.

AI output shape change required: currently the API likely returns multiple labeled fields. New shape:

{

reflection: string,       // one consolidated paragraph

cravingRisk: 'low' | 'moderate' | 'high',

coachQuestion: string     // one open question, no attribution

}

Section 3 — A question to sit with

One question. No label. No attribution. No "From your sponsor" — that section is gone permanently. Render it as a single italicized line or a minimal blockquote style, visually distinct but not in a heavy card.

The question comes from the AI (coachQuestion field). It should be open, recovery-neutral, grounded in what the user actually reported. Not a generic prompt.

Section 4 — CTAs

Two buttons. That's all.

Primary: Chat with my coach (accent color)

Secondary: Done (muted, takes them to Home)

Remove "Check in again." Completing a check-in and immediately being invited to do another one is confusing UX and undermines the grounding intent of the screen.

What gets cut entirely

SOMETHING TO WATCH (folds into reflection)

NEXT MOVES bullets (prescriptive, program-coded, gone)

REACH OUT card (dead UI, wrong moment — resurface in Memory or Home when contacts exist)

SUPPORT section (redundant)

REMEMBER quote (unmoored, no attribution, not useful)

FROM YOUR SPONSOR (must go — program language, fictional attribution)

Full-width "Listen to full summary" button (replaced by icon in card)

"Check in again" CTA

Static copy audit

Do a pass on all static strings on this screen and anywhere the completion flow touches. Remove: sponsor, sober buddy, sober network, attend a meeting, text a sober buddy. These are not edge cases — they're in the current Next Moves bullets and the Support section. Replace with nothing, or with recovery-neutral equivalents only where a replacement genuinely adds value.

Implementation order

AI response shape change (backend) — update the prompt and the response parser to return { reflection, cravingRisk, coachQuestion }

Frontend component rebuild — strip the current section stack, build the three-section layout

Static copy audit — remove all program-specific language

TTS button reposition — icon in card corner, full-width button removed

This is its own branch. Does not touch the tracker detail redesign or Block 2. Want me to write the CC prompt for step 1 now?
