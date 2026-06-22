---
title: "Pre V4 Pre Deploy Prompts"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/Pre V4 Pre Deploy Prompts.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Pre V4 Pre Deploy Prompts

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
V3F5A (done)

V3F5A: DESKTOP CONTAINMENT PASS — CONSTRAINED COLUMN

Make a focused polish revision to the existing Anchor V3 app.

This is not a V4 rebuild. Make the smallest safe changes.

The app is currently mobile-optimized. On desktop, the content column floats off-center and the bottom nav stretches edge-to-edge of the viewport, making the app feel stranded rather than intentional. This revision treats desktop as a constrained, centered column — same mental model as Linear, Things, or a doc app — without redesigning any screen.

This is V3F5A (containment). A later revision V3F5B (expansion) may add a real desktop shell with sidebar nav and wider layouts. That is out of scope here.

Goals:

1. Center the app shell in the viewport on desktop with a sensible max-width.

2. Constrain the bottom nav to the same column width on desktop so it visually belongs to the app, not the browser window.

3. Make the Trackers home grid feel right inside the constrained column on desktop (no excessive single-column scroll).

4. Make the Chat input bar belong to the column, not float in dead space.

5. Preserve all mobile behavior exactly.

⸻

STACK CONTEXT

This app uses React/TypeScript on the frontend and Node.js/Express on the backend.

The app already has:

* App shell with bottom navigation

* Home page with sober trackers grid

* Check-in flow (Quick / Full)

* Chat tab with message list and input bar

* History list and History detail pages

* Trackers home page

* Settings page

* Established Tailwind / CSS variable theme system across 6 themes

* Existing V3 smoke test suite

Extend existing patterns. Do not rebuild from scratch.

⸻

STRICT RULES

* Do NOT redesign any screen.

* Do NOT change any copy.

* Do NOT change any colors, fonts, or theme variables.

* Do NOT change any component logic or state.

* Do NOT add new components beyond a layout wrapper if needed.

* Do NOT add packages.

* Do NOT change the mobile experience in any way.

* Do NOT touch backend code.

* Do NOT change routing.

* Do NOT change navigation behavior.

* Do NOT introduce a sidebar or top nav.

* Do NOT add desktop-only features (hover affordances, keyboard shortcuts, multi-pane layouts).

* Do NOT touch unrelated failing tests unless directly affected.

* Preserve all V3A through V3F4 behavior.

⸻

PRE-FLIGHT

Before editing, inspect and briefly report:

1. The top-level app shell component and how it currently wraps page content.

2. Current global CSS / Tailwind setup: where html, body, #root, and the app shell get their width and height rules.

3. The bottom nav component, its current positioning (fixed?), and whether it's a child of the app shell or a sibling.

4. The Trackers grid on Home: current grid CSS (columns, gap, breakpoints).

5. The Chat page layout: how the message list scrolls, how the input bar is positioned (sticky/fixed/in-flow), and what container it lives inside.

6. The Check-In page layout container.

7. Any existing breakpoint usage in the codebase (md:, lg:, etc.) — is the app currently using Tailwind breakpoints anywhere, or is it pure single-column?

8. The current natural width of tracker cards and check-in cards on mobile — measure approximate rendered width — to inform the max-width decision.

Then proceed.

Keep pre-flight short.

⸻

V3 SAFETY INVARIANTS

Preserve:

* getCurrentUserId() everywhere on backend user-specific operations.

* No hardcoded user IDs.

* Phone numbers never enter AI prompts.

* Phone numbers never enter TTS payloads.

* Raw check-in notes never enter TTS.

* Raw grateful text never enters TTS.

* Raw voice transcripts never enter TTS.

* Hidden memory never enters TTS.

* Full chat history never enters TTS.

* TTS is always user-initiated.

* Only one audio stream/request at a time globally.

* Audio stops on route/tab/view change.

* No audio files are written to disk.

* Existing /api/speak validation remains intact.

* Existing global audio manager remains the single playback source of truth.

* Crisis cards suppress normal result actions and TTS.

This revision is frontend layout only. None of the above should be touched. Listed for completeness.

⸻

DESIGN TARGET

The desktop experience is "mobile-first app in an intentional centered column," not a full desktop redesign. Constraints:

* Mobile (< 768px viewport): zero visual change. Pixel-identical to current behavior.

* Tablet and up (>= 768px): content column centered horizontally, constrained to a single max-width value used consistently across all pages.

* The bottom nav, on desktop, sits inside the same column width — not stretched edge-to-edge.

* Background outside the column remains the existing app background color (already dark — no change needed).

* No desktop-specific visual flourishes. No sidebars. No multi-pane layouts. No "desktop hero" sections. No hover-only affordances. The goal is "intentional, not stranded."

MAX-WIDTH DECISION

Use --app-max-width: 640px as the default.

Only deviate from 640px if pre-flight inspection shows that tracker cards or check-in cards would visibly cramp at this width. If deviation is necessary:

* Pick exactly one of: 600px, 640px, or 680px.

* Do not pick any value between these.

* Use the chosen value consistently across all containers.

* Briefly note in the report why the default was changed.

The intent: one decisive value, applied everywhere, not a per-page tuning exercise.

⸻

PART 1: APP SHELL — CENTERED COLUMN ON DESKTOP

Update the top-level app shell so that on viewports >= 768px, the main content column is:

* Horizontally centered.

* Constrained to --app-max-width.

* Full-height.

* The area outside the column shows the existing app background.

On viewports < 768px:

* Full-width as today.

* No max-width applied.

* No horizontal centering padding.

Implementation guidance:

* Prefer a single layout wrapper around <main> or equivalent.

* Use Tailwind's md: breakpoint (or whatever the codebase already uses if a different breakpoint is established).

* If a layout wrapper component already exists, modify it. Do not introduce a parallel one.

Verify visually after change:

* Mobile width unchanged.

* Desktop width centered and constrained.

* No horizontal scrollbars introduced.

* No content clipped.

⸻

PART 2: BOTTOM NAV — CONSTRAINED ON DESKTOP

The bottom nav currently spans the full viewport width. On desktop this makes the app feel stranded because the centered content column sits above an edge-to-edge nav bar.

Fix:

* On viewports < 768px: nav remains full-width fixed bottom (current behavior).

* On viewports >= 768px: nav width is constrained to --app-max-width, horizontally centered, still fixed bottom.

Implementation guidance:

* If the nav is `position: fixed; left: 0; right: 0;` with a width of 100%, change to: on desktop, fixed bottom but with `left: 50%; transform: translateX(-50%); width: 100%; max-width: var(--app-max-width);` — or the Tailwind equivalent.

* Alternatively, place the nav inside the layout wrapper as a sticky element. Either works. Pick whichever requires fewer changes to existing positioning.

* Whatever bottom safe-area inset behavior already exists for iOS must be preserved.

Do NOT replace the bottom nav with a sidebar or top nav. The nav stays at the bottom on all viewports. This is V3F5A. A future V3F5B may revisit nav placement.

Verify visually:

* Mobile nav unchanged.

* Desktop nav sits inside the column, aligned with the content above it.

* No layout shift on resize across the breakpoint.

⸻

PART 3: TRACKERS GRID ON HOME

The trackers grid currently renders 2 columns on mobile. Inside a 600-680px desktop column, 2 columns remains correct — do not change column count.

But verify:

* Card padding and gap read well at the constrained column width.

* No card text wraps awkwardly.

* The existing card styling is preserved.

Do not change the grid to 3 or 4 columns. The constraint is the column, not the grid.

⸻

PART 4: CHAT INPUT BAR

On desktop today, the chat input bar sits in a narrow constrained area while the surrounding viewport is empty, creating a floating-in-void effect.

After Part 1 and Part 2 are applied, the chat input should naturally inherit the column width. Verify:

* The chat input bar spans the full width of the constrained column on desktop.

* The input bar's positioning relative to the bottom nav is unchanged from current behavior.

* Mic button, send button, and "Say something..." input all remain visually consistent with mobile.

* Message list scroll behavior unchanged.

If the chat input was previously absolutely-positioned to the viewport rather than the column, refactor it to sit inside the column container. This is the only structural change Chat needs.

⸻

PART 5: CHECK-IN AND OTHER PAGES

Pages to spot-verify after the shell change:

* Check-In (Quick + Full)

* Check-In Complete result card

* Chat

* History list

* History detail

* Trackers home

* Settings

* Memory / Insights

For each:

* Renders correctly on mobile (no change).

* Renders correctly inside the centered column on desktop.

* No content clipped.

* No double-scroll situations (only one vertical scroll context per page).

* Bottom nav does not overlap content — existing bottom padding behavior preserved.

If any page has a hardcoded width that conflicts with the new shell constraint, change the page to be width-agnostic (use w-full inside the column) rather than fighting the shell.

⸻

PART 6: BREAKPOINT BEHAVIOR ACROSS RESIZE

Verify the resize behavior:

* Resizing from mobile width to desktop width crosses the md: breakpoint smoothly.

* No layout flashes or content jumps beyond the expected column-narrowing transition.

* The fixed bottom nav re-centers correctly at the breakpoint.

* No JavaScript layout recalculation required — this should all be CSS.

⸻

OUT OF SCOPE — DO NOT TOUCH

* Any color, font, or theme change.

* Any copy change.

* Any new desktop-only features (sidebars, multi-pane, hover-only affordances, keyboard shortcuts).

* Any change to mobile.

* Any change to the chat AI, check-in AI, memory, scheduler, email, or backend.

* Any animation changes.

* Any change to the audio manager or TTS behavior.

* Any change to authentication or user-id behavior.

* Any restructuring of the nav (no sidebar, no top nav, no hamburger).

If a change feels like it requires touching anything in this list, stop and ask.

⸻

VERIFICATION CHECKLIST

After implementation, verify:

* [ ] Mobile width <= 480px renders pixel-identically to current (visually compare before/after).

* [ ] Desktop width >= 1200px shows centered column at chosen max-width with bottom nav constrained to that column.

* [ ] Tablet width ~768-1024px shows centered column.

* [ ] No horizontal scroll at any width.

* [ ] All 6 themes render correctly at desktop width (background outside column is correct theme color).

* [ ] Existing V3 smoke test suite still passes.

* [ ] No console errors or warnings introduced.

* [ ] No new packages installed.

* [ ] No backend files modified.

Briefly report:

* What changed and which files were touched.

* The chosen --app-max-width value and the reason if not 640px.

* Any pages that needed width adjustments to fit the new shell.

Neon Setup (done)

You are helping me complete Stage 1 only of the Anchor V3 production deployment plan.

I have created a Neon project with two branches:

production

staging

The Neon connection strings are stored in Replit Secrets as:

NEON_DATABASE_URL_STAGING

NEON_DATABASE_URL_PROD

Important:
Use NEON_DATABASE_URL_STAGING first. Do not touch production yet. Do not print either connection string. Do not write secrets into files. Do not commit secrets.

Goal:
Apply the current Anchor database schema to the Neon staging branch, verify it, and report exactly what happened.

Hard boundaries:

Stage 1 only.

Do not refactor application code.

Do not touch auth.

Do not modify getCurrentUserId.

Do not start Supabase setup.

Do not start Fly, Vercel, Resend, or Sentry setup.

Do not apply anything to production unless I explicitly approve it after staging is verified.

Do not delete or overwrite migrations.

Tasks:

Inspect the repository and identify the canonical database schema or migration files.

Tell me which file or files define the current Anchor schema.

Confirm whether the expected tables are represented:

user_memory

app_settings

commitments

chat_sessions

check_ins

sobriety_trackers

tracker_resets

Generate the exact command you plan to run against NEON_DATABASE_URL_STAGING.

Ask me for approval before running the schema apply command.

After approval, apply the schema to the staging branch only.

Verify the tables exist.

Run a user_id column audit and report any user-data table missing user_id.

Produce a Stage 1 staging report with:

schema source used

commands run, with secrets redacted

tables created or found

user_id audit result

warnings

recommended next step

Reminder:
Accuracy matters more than speed. Refuse to compress steps.

DONE login UX

AUTH SCREEN UX REDESIGN SPEC

Objective:

Redesign the Anchor login screen so it feels like a modern, trustworthy production auth page instead of a raw developer auth form.

Current problem:

The current auth screen exposes Google SSO, magic link, email/password, forgot password, multiple dividers, and multiple input groups all at once. This creates visual noise, weak hierarchy, and low trust.

The Google sign-in button is especially bad because it lacks the Google "G" icon and does not resemble a standard Google SSO button.

Primary UX principle:

Show one primary login path at a time. Do not display magic link and password login fields simultaneously.

Target hierarchy:

1. Google SSO as the primary action

2. Magic link as the default email fallback

3. Password login hidden behind a secondary "Use password instead" action

4. Forgot password shown only in password mode

Default screen layout:

- Anchor wordmark / simple brand title

- Heading: "Sign in to Anchor"

- Short subheading: "Continue your recovery check-in."

- Primary button: "Continue with Google"

- Divider: "or"

- Magic link email field

- Primary email action button: "Send sign-in link"

- Secondary text button: "Use password instead"

Do not show password fields on initial page load.

Google SSO button:

- Must include the official multicolor Google "G" icon

- Text should be "Continue with Google" or "Sign in with Google"

- Button should look like a standard Google SSO button

- Use white background, dark text, subtle border, normal button height, and left-side Google icon

- Icon should not be a font-awesome G, generic G, monochrome G, or fake brand mark

- Prefer the Google-rendered button if compatible with the current Supabase auth flow

- If using a custom button, use approved Google branding assets and match Google button conventions closely

- The entire button must be clickable

- Do not use the current plain dark outlined button without icon

Email auth modes:

There should be two mutually exclusive email modes:

Mode 1: Magic link mode

- Visible by default

- Shows only:

- Email field

- "Send sign-in link" button

- "Use password instead" secondary button

- Does not show password field

- Does not show forgot password link

Mode 2: Password mode

- Activated only when user clicks "Use password instead"

- Shows:

- Email field

- Password field

- "Sign in" button

- "Forgot password?" link

- "Use magic link instead" secondary button

- Does not show magic link send button at the same time

Mode switching behavior:

- Clicking "Use password instead" replaces the magic link form with the password form

- Clicking "Use magic link instead" replaces the password form with the magic link form

- Preserve the typed email value when switching modes

- Do not create a second duplicate email field if the user already typed an email

- Use a subtle transition only if already consistent with the app style

- No layout jump that feels broken

Visual design requirements:

- Keep the dark Anchor aesthetic

- Make the auth card narrower and more intentional

- Use one clean card or centered auth panel

- Reduce vertical clutter

- Remove duplicate "or" dividers

- Use one divider between Google and email auth only

- Use consistent spacing between sections

- Use consistent button heights

- Use consistent input heights

- Use clear labels, not just placeholders

- Remove any unexplained red ellipsis icons or unlabeled input adornments

- Do not show decorative controls inside inputs unless they have a clear purpose, label, and accessible behavior

- Password field may include a normal show/hide password control if desired

Suggested visual structure:

Top:

Anchor

Card:

Sign in to Anchor

Continue your recovery check-in.

[ Google G icon ] Continue with Google

──────── or ────────

Email

[ you@example.com ]

[ Send sign-in link ]

Use password instead

Password mode structure:

Anchor

Card:

Sign in to Anchor

Continue your recovery check-in.

[ Google G icon ] Continue with Google

──────── or ────────

Email

[ you@example.com ]

Password

[ Password ]

[ Sign in ]

Forgot password?

Use magic link instead

Copy:

- Use "Sign in to Anchor" instead of generic "Sign in to your account."

- Use "Continue with Google" for the SSO button

- Use "Send sign-in link" for magic link

- Use "Use password instead" as the password-mode toggle

- Use "Use magic link instead" as the return toggle

- Keep copy calm, short, and non-cute

Error handling:

- Errors should appear directly under the relevant field or form

- Error text should explain what happened and what to do next

- Do not use unexplained icon-only errors

- Do not use red icons without text

- Invalid email error: "Enter a valid email address."

- Wrong password error: "Email or password is incorrect."

- Magic link success message: "Check your email for your sign-in link."

- Rate-limit message: "Too many sign-in attempts. Wait a bit, then try again."

Loading states:

- Google button shows loading state after click

- Magic link button shows loading state after click

- Password sign-in button shows loading state after click

- Prevent duplicate submissions while loading

- Loading state should not shift layout

Accessibility:

- All fields must have real labels

- Buttons must have accessible names

- Google icon must be decorative if button text is present

- Mode toggle must be a real button, not a fake clickable div

- Error messages should be associated with the relevant field

- Keyboard navigation should work through the full form

- Focus should move sensibly when switching modes

- Color contrast must remain readable on the dark background

Technical constraints:

- Preserve existing Supabase auth behavior

- Do not change auth providers, schema, environment variables, redirects, or backend auth logic unless absolutely necessary

- This is a UX/component refactor, not an auth architecture rewrite

- Do not touch unrelated pages

- Do not change production settings

- Do not introduce a new UI library unless one is already being used

- Keep implementation small and targeted

Implementation expectation:

- Find the current auth/login component

- Replace the current all-methods-visible layout with a stateful auth mode component

- Add Google icon asset or approved inline SVG

- Implement mode state: "magic-link" or "password"

- Preserve email field value across modes

- Keep existing auth function calls where possible

- Add clear success/error/loading states

- Remove duplicate dividers and visible password fields from default screen

Required verification:

- Default page shows Google SSO and magic link only

- Default page does not show password field

- Google button includes Google G icon

- Clicking "Use password instead" shows password mode

- Password mode shows email, password, sign in, forgot password, and "Use magic link instead"

- Clicking "Use magic link instead" returns to magic link mode

- Email value persists when switching modes

- Magic link submission still calls the existing Supabase magic link flow

- Password sign-in still calls the existing Supabase password flow

- Google sign-in still calls the existing Supabase Google OAuth flow

- Error and loading states render correctly

- Mobile layout remains clean

- No unrelated files changed

Output required:

1. Summary of UX change

2. Files changed

3. Auth flows touched

4. Screenshots or Playwright verification if available

5. Commands run

6. Test results

7. Risks or unknowns

8. Branch name and commit hash, if applicable

Forbidden side quests:

- Do not redesign the whole app

- Do not change the landing page

- Do not change auth architecture

- Do not add passkeys

- Do not add registration/onboarding changes

- Do not modify Supabase settings

- Do not refactor unrelated components

- Do not fix unrelated TypeScript errors

DONEANCHOR V3 — MODEL EVALUATION SESSION

ANCHOR V3 — MODEL EVALUATION SESSION

This is a focused 2-3 hour session to evaluate and select the OpenAI model(s) used by Anchor V3 in production, before the multi-user refactor (Stage 3 of the deployment plan).

This is not a refactor. This is an evaluation that ends with a decision and a small config change.

CONTEXT

Anchor V3 currently uses gpt-4o-mini for all AI calls. Daily usage of the app has surfaced a recurring sense that check-in reflections occasionally feel "generic or off-tone." This may be a model-fit problem, a prompt-specificity problem, or both.

The eval session has three jobs:

1. Determine whether the off-tone issue is the model or the prompt.

2. If it's the model, pick the right replacement.

3. If it's the prompt, tighten the prompt.

The decision must be made before Stage 3 of the deployment plan (multi-user refactor), so that production launches on the chosen model rather than swapping models post-launch.

CANDIDATE MODELS (verify current pricing at session start)

* gpt-4o-mini — current default, cheapest, known off-tone risk

* gpt-5-mini — mid-tier, August 2025 release, ~3x output cost vs 4o-mini

* gpt-5.4-mini — newer mini, March 2026 release, ~7x output cost vs 4o-mini, designed for production chat workloads

* gpt-5.4-nano — cheapest 5.4-tier, candidate for classifier/lightweight calls

* gpt-5.5 — flagship, NOT a candidate for default user-facing chat (cost prohibitive at scale, overkill for the use case)

Working hypothesis from prior research: gpt-5.4-mini is likely the right default for main chat and check-ins. gpt-5.4-nano is likely the right choice for the crisis classifier and lightweight memory summarization. gpt-5.5 stays out of the user-facing path entirely.

The session validates or rejects this hypothesis with real data.

⸻

ROUTING TARGETS (post-eval, what the config should look like)

The current code likely uses a single OPENAI_MODEL env var or hardcoded model string. Part of this session's deliverable is to introduce per-purpose routing if the eval supports it.

Target routing structure:

* CLASSIFIER_MODEL — for crisis detection, mode detection, intent routing. Cheap and fast. Likely gpt-5.4-nano or gpt-5.4-mini.

* MAIN_CHAT_MODEL — for chat responses and check-in reflections. The most user-visible call. Likely gpt-5.4-mini.

* SUMMARY_MEMORY_MODEL — for memory event_log summarization, recent patterns. Cheap, runs in background. Likely gpt-5.4-nano or gpt-5.4-mini.

* PREMIUM_DEEP_REFLECTION_MODEL — for the heaviest reflection generation if/when a "deep mode" is added. Reserved for future use. Default: same as MAIN_CHAT_MODEL until premium tier exists.

If introducing routing during this session feels like scope creep, the alternative is to swap the single OPENAI_MODEL value and defer routing to a later session. Make that call early.

⸻

SESSION PHASES

Phase 1: Diagnose prompt vs model (45 minutes)

Before any model swap, evaluate whether the "generic or off-tone" feeling is fixable at the prompt level.

Tasks:

1. Open the current check-in system prompt and the chat system prompt.

2. Read each prompt out loud or carefully. Score on a checklist:

* Does the prompt name specific words or phrases to AVOID? (Mini models need explicit blocklists, not abstract guidance.)

* Does the prompt specify opening behavior? (Don't open with affirmations / restatements.)

* Does the prompt specify length constraints in concrete terms? (Word count, sentence count.)

* Does the prompt give examples of the desired voice vs the undesired voice?

* Does the prompt distinguish "warm" from "saccharine" with concrete instances?

3. For each "no" on the checklist, draft a tightening edit. Don't apply yet — just draft.

4. If the prompt has 3 or more "no" answers, the off-tone issue is plausibly a prompt problem first. Apply the tightenings and re-test on 4o-mini before declaring the model insufficient.

5. If the prompt is already specific and outputs still drift, the issue is the model. Move to Phase 2.

Phase 2: Eval set construction (30 minutes)

Build a real eval set from production data.

Tasks:

1. Pull 10 historical check-ins from the developer's account that span:

* 3 normal-result reflections

* 2 moderate-distress reflections (handoff banner triggered)

* 1 crisis-routed check-in (verify suppression behavior)

* 2 high-craving / high-stakes reflections

* 2 low-mood, gratitude-heavy reflections

2. For each, capture:

* Full input (sliders, notes, voice transcript if applicable)

* Current 4o-mini output

* Subjective rating: 1-5 on tone fit, 1-5 on specificity, 1-5 on restraint

* One-sentence note on what's missing or wrong if anything

3. Save the eval set as a JSON file in /eval/checkin_eval_v1.json. This becomes a reusable artifact for future model decisions.

Same exercise for chat: pull 10 representative chat exchanges with the same coverage spread.

Phase 3: Side-by-side model runs (45 minutes)

Run the eval set through each candidate model.

Tasks:

1. Write a small Node script (one file, /eval/run_eval.js) that:

* Loads the eval set.

* For each item, calls the API once per candidate model with the SAME system prompt.

* Saves outputs to /eval/results_<model>_<timestamp>.json.

2. Run against:

* gpt-4o-mini (baseline)

* gpt-5-mini

* gpt-5.4-mini

* gpt-5.4-nano (chat eval only — likely too small for check-ins)

3. Verify pricing at run time. Log the actual cost per model run. The eval itself should cost under $1 total — abort and investigate if it spikes.

4. Do NOT use the production database. Stub any DB-dependent logic with the captured eval inputs.

Phase 4: Subjective scoring (45 minutes)

Score the outputs.

Tasks:

1. For each eval item across all candidate models, blind-score (hide which model produced which output).

2. Score on the same scale used in Phase 2: tone fit, specificity, restraint.

3. Note specific failure modes: which models produce affirmations? which restate the user? which use banned phrases? which over-explain?

4. Tally the results.

Decision rule:

* If gpt-5.4-mini scores meaningfully higher than 4o-mini AND gpt-5-mini, pick gpt-5.4-mini.

* If gpt-5-mini scores comparably to gpt-5.4-mini, pick gpt-5-mini for cost reasons.

* If 4o-mini with the tightened prompt scores comparably to either upgrade, stay on 4o-mini and ship the prompt change.

* If results are inconclusive across the eval set, default to gpt-5.4-mini as the safer choice for production.

Phase 5: Apply decision (15 minutes)

Tasks:

1. Update env config:

* If single-model: change OPENAI_MODEL to the chosen value.

* If introducing routing: add CLASSIFIER_MODEL, MAIN_CHAT_MODEL, SUMMARY_MEMORY_MODEL env vars. Default routing per the targets above.

2. Update the relevant call sites in the codebase to read from the new env var(s).

3. Apply any prompt tightenings from Phase 1 if they were drafted.

4. Update Anchor Production Secrets note with the new env var values.

5. Update Fly secrets if Fly is already provisioned (it may not be at this point in the deployment sequence).

Phase 6: Re-run smoke tests (15 minutes)

Tasks:

1. Run the full V3 smoke suite against the new model.

2. Address any tests that fail because of legitimate output-shape changes (different word choices that break string-match assertions).

3. Tests that fail for behavior reasons (banned phrases appearing, crisis suppression breaking) are real regressions and need investigation.

Do not move forward to Stage 3 until smoke tests are green.

⸻

SPEND ALERT (must be done by end of session)

Set an OpenAI usage alert at $50/month before any user beyond the developer touches the app. Current usage is trivial; growth is unpredictable; the alert is cheap insurance.

Task:

1. Open OpenAI dashboard → Settings → Limits.

2. Set monthly hard limit at $100.

3. Set email alert at $50.

4. Verify the email alert recipient is the production ops email.

⸻

OUT OF SCOPE FOR THIS SESSION

* Do NOT swap embedding models (if any are used).

* Do NOT change Whisper (voice transcription) — that's a separate model class.

* Do NOT change TTS (tts-1) — separate decision.

* Do NOT add fine-tuning. The eval is base-model only.

* Do NOT introduce streaming or other API features. Model selection only.

* Do NOT touch the auth or multi-user code. That's Stage 3.

* Do NOT add new prompt features (longer reflections, new modes, etc.). The prompt edits in Phase 1 are tightenings only.

⸻

DELIVERABLE AT END OF SESSION

A short written summary in the deployment notes:

* Models evaluated and pricing at run time.

* Decision: chosen model(s) and rationale.

* Prompt changes applied, if any.

* Eval artifacts saved (eval set + results JSONs) for future model reviews.

* Spend alert configured at $50/month.

* Smoke tests green.

Then: proceed to Stage 3 of the deployment plan (multi-user refactor).

DONE Desktop layout

V3F5B: TRUE DESKTOP LAYOUT — FULL-WIDTH, DENSER, LESS SCROLL

Make a focused desktop-responsive layout revision to the existing Anchor V3 app.

This is not a V4 rebuild. Preserve the mobile experience exactly. The goal is to make desktop feel like a real desktop app, not a centered mobile column.

Current issue:

The app is still too mobile-on-desktop:

- Content is constrained too narrowly.

- Pages require too much vertical scrolling.

- Cards are tall and stacked when desktop space could reduce scroll.

- Bottom nav still feels like a mobile pattern.

- Home, Check In, History, Trackers, Chat, and Insights should use desktop width more intelligently.

Goals:

1. Preserve mobile behavior and layout.

2. On desktop, use a wider app canvas.

3. Compress vertical spacing and card heights on desktop.

4. Use responsive grids/columns where appropriate.

5. Reduce scrolling on Home, Check In, History, Trackers, and Insights.

6. Make Chat feel like a stable desktop chat workspace.

7. Keep all app logic, backend behavior, copy, colors, themes, routing, TTS, and data behavior unchanged.

STRICT RULES:

* Do NOT rebuild the app.

* Do NOT change mobile layout.

* Do NOT change copy.

* Do NOT change colors, fonts, or theme variables.

* Do NOT change backend code.

* Do NOT change check-in logic.

* Do NOT change chat logic.

* Do NOT change TTS/audio behavior.

* Do NOT add packages.

* Do NOT add database tables or columns.

* Do NOT change routing.

* Do NOT touch unrelated failing tests.

* Preserve all V3A through V3F4 behavior.

PRE-FLIGHT:

Before editing, inspect and briefly report:

1. App shell/root layout and current desktop max-width behavior.

2. Bottom nav component and positioning.

3. Shared page container classes.

4. Home tracker grid and card sizing.

5. Check-In form/card layout and spacing.

6. Chat page scroll/composer structure.

7. History list card layout.

8. Trackers page list/card layout.

9. Insights grid/card layout.

10. Existing breakpoint usage.

Keep pre-flight short, then proceed.

DESKTOP DESIGN TARGET:

Desktop should feel like a quiet, functional recovery dashboard.

Use available width without becoming huge or loose.

Recommended desktop shell:

- Mobile < 768px: unchanged.

- Tablet 768px-1023px: centered readable layout is okay.

- Desktop >= 1024px: use a wider content canvas.

- Large desktop >= 1280px: max content width around 1100-1280px.

Do NOT keep desktop locked to a narrow 520-680px mobile column.

Desktop pages should generally use:

- max-width: around 1120px or 1200px

- responsive grids

- reduced vertical gaps

- shorter card padding where safe

- full-width sections only where they help scanning

PART 1: APP SHELL

Update the desktop app shell so the main content uses a wider desktop canvas.

Desktop requirements:

- Main content centered in viewport.

- Width should be close to full available space with side padding.

- Max width around 1120-1280px.

- No horizontal scroll.

- Desktop should not feel like a phone screen.

- Preserve mobile full-width behavior.

If there is a previous --app-max-width around 520-680px, replace it with separate responsive values:

- mobile: 100%

- tablet/readable: around 680-820px if needed

- desktop: around 1120-1280px

PART 2: NAVIGATION

Desktop bottom nav currently still feels mobile-like.

Preferred desktop behavior:

- Keep mobile bottom nav unchanged.

- On desktop, either:

A. Convert nav to a compact top nav/header within the desktop canvas, or

B. Keep bottom nav but make it feel desktop-appropriate, constrained to the wider desktop canvas and less dominant.

Pick the smallest safe change that fits the existing code.

If converting to top nav is not too invasive:

- Desktop nav should use the same nav items.

- Same active states.

- Same routing.

- No behavior changes.

- It should not cover content.

- Remove desktop bottom padding that only exists for mobile bottom nav.

If keeping bottom nav:

- Use wider desktop canvas alignment.

- Reduce its visual dominance.

- Ensure content is not artificially shortened by nav spacing.

PART 3: HOME DESKTOP

Make Home use desktop width to reduce scrolling.

Requirements:

- Header/date/settings align cleanly across the wider canvas.

- Tracker cards should use a responsive grid:

- mobile: current behavior

- desktop: 3 or 4 columns depending on available width

- Tracker cards should be shorter on desktop.

- Commitment check-in and Ready to check in should not require excessive scrolling.

- If appropriate, place secondary sections in a two-column desktop layout.

- Preserve all text and behavior.

PART 4: CHECK-IN DESKTOP

Make Check-In less vertically exhausting on desktop.

Requirements:

- Mobile check-in flow unchanged.

- Desktop check-in should use a wider form canvas.

- Reduce desktop card height/padding where safe.

- Sliders should not become comically long.

- Consider a two-column layout for rating cards on desktop if the current flow allows it:

- Mood and Energy side by side

- Craving and Sleep side by side

- Other sections grouped logically

- Preserve form order, labels, validation, and state.

- Do not alter check-in submission behavior.

If two-column layout risks breaking logic, keep single column but reduce vertical spacing and max card height.

PART 5: HISTORY DESKTOP

Make History easier to scan.

Requirements:

- Mobile history list unchanged.

- Desktop history list should use wider cards or a two-column responsive grid.

- Cards should be more compact vertically.

- The “Log missed” button should align neatly with the heading.

- Text truncation should still work.

- Preserve click/detail behavior.

PART 6: TRACKERS DESKTOP

Trackers page should not be a long single-column list on desktop.

Requirements:

- Mobile unchanged.

- Desktop tracker items should use a responsive grid, preferably 2 columns.

- Cards should be compact and scannable.

- Add button remains aligned with heading.

- Preserve tracker timing/calculation behavior.

PART 7: INSIGHTS DESKTOP

Insights is already partly grid-based, but should use desktop space better.

Requirements:

- Mobile unchanged.

- Desktop stat cards should use 3 or 4 columns where appropriate.

- Large summary sections should align to the wider canvas.

- Reduce unnecessary vertical gaps.

- Preserve all metrics, export behavior, filters, and calculations.

PART 8: CHAT DESKTOP

Make Chat feel like a desktop chat workspace.

Requirements:

- Mobile chat unchanged.

- Desktop chat should use a wider but readable chat column, around 900-1040px.

- Message area should use height intelligently.

- Composer should align with the chat content.

- Composer should not float awkwardly in empty space.

- Preserve new chat, sending, microphone, message history, and session behavior.

PART 9: DESKTOP DENSITY RULES

At desktop breakpoints only:

- Reduce large vertical page gaps.

- Reduce excessive card padding.

- Avoid giant single-column stacks when grids are more appropriate.

- Keep readability and touch/click targets acceptable.

- Do not make mobile denser.

- Do not change typography globally unless there is already a desktop text scale pattern.

VERIFICATION:

After implementation, verify:

Viewport sizes:

- 390x844 mobile

- 430x932 mobile

- 768x1024 tablet

- 1280x800 desktop

- 1440x900 desktop

- 1600x1000 large desktop

Check:

- Mobile looks unchanged.

- Desktop uses wider canvas.

- Home tracker cards fit in fewer rows.

- Check-In requires less scrolling.

- History scans faster.

- Trackers are not a single long list.

- Insights uses 3/4-column stat grid where appropriate.

- Chat composer is aligned and stable.

- No horizontal scroll.

- No nav overlap.

- No console errors.

Run existing build/typecheck/test command if available.

Report briefly:

- Files changed.

- Desktop breakpoint strategy.

- Which pages were made denser.

- Tests run.

DONE risk level fix

UX COPY REFINEMENT: RISK LABELING FOR CHECK-IN RESULT CARD

Objective:

Update the check-in result card language so the risk/status labeling is clear, recovery-specific, and internally consistent.

Current issue:

The UI currently says "ATTENTION LEVEL" with a red dot and "Elevated" while the message above says the craving is at the maximum level. This is confusing. "Attention level" is vague, and "Elevated" under-describes a maximum craving state.

Required change:

Replace "ATTENTION LEVEL" with a clearer label.

Preferred label:

"CRAVING RISK"

Acceptable fallback:

"RISK LEVEL"

Do not use:

"ATTENTION LEVEL"

Severity language:

Use severity labels consistently:

- Low

- Moderate

- Elevated

- High

- Critical

If the craving score is at or near the maximum, the displayed severity should be "Critical" or "High", not merely "Elevated".

Recommended copy:

Section heading:

SOMETHING TO WATCH

Message:

"Craving is very high right now. This is a high-risk moment, so choose one support action before doing anything else."

Risk label:

CRAVING RISK

Risk value:

Critical

Implementation requirements:

- Find where the check-in result card renders "ATTENTION LEVEL"

- Rename that label to "CRAVING RISK"

- Ensure the severity label matches the underlying score/severity mapping

- If the current logic maps maximum craving to "Elevated", fix the mapping

- Do not redesign the whole card

- Do not alter scoring logic unless required to fix the displayed label

- Do not touch unrelated result card sections

Required verification:

- Maximum craving state no longer displays "Attention Level"

- Maximum craving state displays "Craving Risk"

- Maximum craving state does not display "Elevated" unless the actual score is only mid-high

- Copy remains readable on mobile

- No unrelated files changed

Output required:

1. Summary of copy/label changes

2. Files changed

3. Whether severity mapping was changed

4. Screenshots or test output if available

5. Risks or unknowns
