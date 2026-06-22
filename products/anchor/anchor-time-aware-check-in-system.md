---
title: "Anchor — Time Aware Check In System"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/Anchor — Time-Aware Check-In System.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor — Time Aware Check In System

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor — Time-Aware Check-In System

VNext Feature Spec / Saved May 8, 2026

Working title

Anchor VNext: Time-Aware Recovery Check-Ins

Alternative names under consideration: Daily Arc System, Temporal Check-In Engine, State Delta Recovery System, Morning / Midday / Evening Anchor.

The core problem

The current check-in flow is time-blind. It asks the same questions regardless of when in the day the user is checking in. A morning check-in asking about exercise, eating, and daily choices produces artificially low scores because the day has not happened yet. The app accidentally punishes early check-ins by assuming an end-of-day context. If the user answers honestly, their score suffers. If they game the answers to protect their score, the data is worthless.

This is a use-case failure, not a feature gap. The fix is not adding questions. It is routing the right questions to the right moment.

A secondary problem is 12-step language saturation. The current question set leans on 12-step framing as a default ontology, which excludes users in secular recovery, harm reduction, non-AA pathways, or AI self-governance frameworks. The overhaul is an opportunity to rewrite the question library with inclusive language while keeping the recovery-supportive intent fully intact.

The product thesis

Anchor should become a temporal relapse-prevention mirror.

Not “how are you today” but: how did you wake up, how are you drifting, what changed between morning and now, what pattern is emerging, what intervention is available before risk escalates.

Relapse is rarely a single event. It is a trend. A person may wake up stable, become dysregulated by midday, skip food, get socially activated, flirt with old patterns, and act out in the evening. Anchor should detect that slope while there is still time to intervene.

The proposal: three time-aware check-in types

The app detects local time and serves the appropriate check-in flow automatically. The user can always check in outside their window — the app serves the nearest appropriate type. No check-in is penalized for being early.

Morning is for baseline. Midday is for drift detection. Evening is for review. These are not the same thing and should not be scored the same way.

Morning check-in — baseline

Purpose: establish the user’s starting condition before the day has made any demands.

Does not ask about exercise, eating, or daily choices. Those have not happened yet. Asks only about what is already knowable.

Question categories: sleep quality, wake-up mood, energy level, anxiety level, body state, dreams, cravings or urges on waking, primary risk today, primary intention today, what support the user needs before the day begins.

Example questions: How did you sleep? What was your waking mood? How does your body feel? Any dreams worth capturing? What is the main risk today? What is your sobriety intention for today? What would help you stay anchored this morning?

Optional future feature: dream dictation. Voice or text entry, stored separately from the recovery score. Used for emotional pattern archiving, not scored. Light AI dream reflection is a later build, not part of this spec.

Midday check-in — drift detection

Purpose: catch destabilization before it becomes evening risk. This is the most relapse-preventive check-in because it catches changes while there is still time to act.

Compares against the morning check-in if one exists. The AI response should reference the delta explicitly.

Question categories: food, hydration, movement, stress, social activation, romantic activation, spending urges, substance urges, avoidance patterns, work spirals, emotional charge, body tension, fatigue, current risk level, needed course correction.

Example questions: Has your mood changed since this morning? Any urges showing up? Are you getting pulled into a loop? What is the smallest course correction available right now? Do you need food, rest, movement, connection, solitude, or a boundary?

Example AI response when drift is detected: “You woke up relatively steady, but your stress and urge levels are higher now. This looks like drift, not failure. Eat, hydrate, and delay major decisions for one hour.”

Evening check-in — full review

Purpose: review the full day and generate the primary daily recovery record. This is the required anchor check-in. Morning and midday are optional and encouraged. Evening is the one that closes the day.

Question categories: sobriety, substance avoidance, relevant behavioral sobriety if applicable, food, exercise, sleep setup, spending behavior, relationship behavior, emotional regulation, integrity, gratitude, repair needed, tomorrow’s risks, tomorrow’s setup.

Example questions: Did you stay sober today? Did you act in alignment with your values? Where did you self-govern well? Where did you drift? Is there any repair needed? What is tomorrow’s main risk? What is one thing you can do tonight to make tomorrow easier?

The evening check-in generates the main daily summary and the primary daily score.

Scoring model

Morning, midday, and evening measure different things and must not be scored with identical logic.

Morning score: baseline stability, sleep recovery, waking risk level, intention clarity.

Midday score: drift status, basic needs met, urge level, course-correction availability.

Evening score: day integrity, sobriety, behavior alignment, emotional regulation, recovery completion.

Default weighting for daily roll-up: morning 25%, midday 25%, evening 50%. Evening carries the most weight because it has the most complete information. This weighting is a hypothesis, not a locked default. Real user data should inform it before it is hardened.

If only evening exists, evening stands alone as the daily score. If morning exists but evening does not, the day is labeled partial data, not scored as complete. The app should never manufacture a full daily score from incomplete data.

Partial day labels: morning baseline captured, midday drift check captured, evening review complete, daily score complete, partial day record, insufficient data for full daily score.

Delta intelligence

This is the most important part of the feature.

Anchor should compare check-ins within the same day and surface changes in plain language. The goal is not surveillance. It is pattern visibility while the pattern is still actionable.

The app should detect and name: mood improvement, mood worsening, stress increase, urge escalation, energy crash, food or hydration missing, sleep debt showing, romantic or social activation increase, spending impulse increase, work spiral emerging, isolation increasing, self-governance improving, evening recovery after a rough start.

Example outputs:

“You woke up anxious but stabilized by evening. That is a recovery win.”

“You started the day steady, but stress rose sharply by midday. This may be a risk window.”

“You skipped food and your urge score increased. Eat before making any decisions.”

“You felt worse at midday but recovered by evening. The course correction worked.”

“You had no morning or midday data today, so this evening score is based only on day review.”

Over time, the app builds a pattern picture: morning person or evening person, which days of the week are hardest, whether cravings correlate with sleep quality, what interventions actually work. None of this requires complex ML. It requires consistent timestamped data and honest comparisons.

AI behavior — temporal awareness

The AI must be aware of: current local time, current check-in type, previous check-ins from the same day, recent trend history, user recovery style, known risk patterns, known stabilizers, known goals.

The AI should not generate generic advice when temporal context makes it wrong.

At 8am it should not say “you didn’t exercise today.” It should say “exercise is still available later — for now, the relevant question is how you woke up.”

At midday: “You woke up clear, but your stress is higher now. This is the moment to intervene.”

At evening: “Looking at the full day, the main recovery win was that you noticed drift and corrected it before acting out.”

Recovery style settings

Anchor should allow users to select or customize their recovery framework. This affects language, question phrasing, and suggested actions throughout the app.

Possible options: AI self-governance, virtue-based recovery, DBT-informed recovery, secular recovery, spiritual but non-12-step, 12-step and AA-informed, therapy-supported, harm reduction, custom.

Example of inclusive reframe: instead of “did you reach out to another sober person today,” ask “what support did you use today?” Then offer examples that span the full range: AI check-in, journal, sponsor, meeting, friend, therapist, prayer, exercise, walk, meal, boundary, meditation, creative work, rest.

This makes Anchor broader without being anti-AA. The 12-step path remains fully supported. It just stops being the assumed default.

Notifications

Evening check-in notification is the only required one. Time is user-configured during onboarding.

Morning and midday notifications are optional and opt-in. All notifications should be local push where possible.

Possible default schedule: morning notification 30 to 60 minutes after usual wake time, midday in early afternoon, evening at user-selected primary check-in time.

Timezone handling must be explicit. Users travel. The app should track local time, not server time, and adjust gracefully when timezone changes.

Home screen concept

The home screen should show the user’s daily arc at a glance.

Possible layout: morning baseline status, midday drift check status, evening review status, today’s state trend (improving, stable, drifting, high-risk), next recommended action.

Example state: morning steady but tired, midday stress rising, evening pending, suggestion is eat and hydrate before making decisions.

The app should make the user feel tracked in a helpful way, not surveilled or graded.

Data model — directional

Each check-in stored as its own timestamped record: user ID, date, local date, timezone, check-in type, created timestamp, local time, answers, domain scores, risk level, AI summary, detected deltas, daily roll-up ID.

Daily summary as a separate object aggregating multiple check-ins: daily score, recovery status, risk trend, key wins, key risks, most important intervention, tomorrow setup, number of check-ins completed, data completeness level.

This is directional. Schema decisions belong in the V5 engineering spec, not here.

MVP feature set

Time-aware check-in routing. Morning, midday, and evening check-in templates. Timezone-aware local check-in logic. Optional morning and midday check-ins. Primary required evening check-in. Separate scoring semantics by check-in type. Daily roll-up summary. Basic intraday comparison and delta detection. Home screen daily arc indicator. Reduced 12-step default language. Recovery style setting. Notification settings for each check-in window.

Later features — parked cleanly

Dream dictation and archive. Light dream analysis. Advanced trend graphs. Relapse-risk slope detection. Pattern alerts. Personalized question adaptation based on prior history. Travel-aware timezone adjustment. Wearable integration if user chooses. Voice-first check-ins. Anchor-generated weekly pattern review. Mode-aware check-ins mapped to Exploration, Integration, Build, and Arena phases. The mode-aware concept is significant enough to warrant its own spec when the time comes — do not let it stay buried as a bullet point.

Non-goals for the first VNext pass

Do not add wearable dependency. Do not require biometric data. Do not overbuild dream analysis. Do not make every check-in mandatory. Do not turn the app into a generic habit tracker. Do not make 12-step language the default. Do not use the same score formula for all times of day. Do not let morning check-ins damage the daily score unfairly. Do not build any of this before production deployment is complete.

Product philosophy

Anchor should not be a shame machine. It should not punish the user for being early in the day, tired, imperfect, or in process.

The questions Anchor is really asking are: where am I right now, what has changed since earlier, what is the risk slope, what is the next stabilizing action, what did I learn today, how do I protect tomorrow.

The deeper product is not daily check-ins. The deeper product is self-governance across time.

Sequencing note

This spec is saved and parked. It does not touch the current deploy sequence.

Current sequence remains: Stage 7 Sentry, Stage 8 Landing page, Stage 9 Legal, Stage 10 First real account, Stage 11 Production smoke test.

After Stage 11 closes and the first real accounts are live, this becomes the highest-priority product overhaul. Real users on the current flow will surface which specific questions are failing in practice. That data should inform the first VNext build session before a single line is written.​​​​​​​​​​​​​​​​
