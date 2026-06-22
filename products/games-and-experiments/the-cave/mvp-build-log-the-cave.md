---
title: "MVP Build Log the cave"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /THE CAVE MVP/MVP Build Log the cave.docx"
status: parked
privacy: private/internal
tags:
  - product
---

# MVP Build Log the cave

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Prompt

Generate a Builder's Log entry for The Cave in the voice and structure of Marcus Vale's existing entries.

Format and tone:

- First person, reflective but grounded. Not journaling-as-therapy, not hype, not corporate progress report.

- Mix of narrative ("started this morning at..."), bulleted facts where they earn it, and direct calls-out of discipline moments.

- No em dashes anywhere in the entry.

- No horizontal divider lines.

- Heading hierarchy: bold section headers, no markdown # signs, plain bold sentence-style headers.

- Voice: a builder who is also a writer. Honest about fatigue, temptation, side quests resisted. Names where the discipline held and where it almost didn't.

- Avoid "just vibes," Gen Z "vibes," and AI-tell phrases.

Required sections (in this order, omit any that don't apply to the day):

1. Opening orientation. What day of the build, what stage, what the original plan for the session was.

2. What actually happened, more or less in order. Narrative, not bullets. Include the messy parts: tools breaking, false starts, side-quest temptations, mistakes caught and recovered.

3. Specific named moments worth banking. Pull out 2-4 things that would be easy to forget but matter to the case study or to future-me. Each one gets a short paragraph, not a bullet.

4. What I'm noticing about the work. Reflective. Pattern-level. Discipline-over-speed framing where it applies. Greek vocabulary if it earns its place (Phronesis, Sophrosyne, Aidōs, etc.) — never forced.

5. Where I am now. Precise about percent done and what "done" actually means as a checklist. Distinguish "emotionally done" from "actually done" when relevant.

6. A few things to lock in before stopping. Decision debt. Things deliberately parked. What's pinned for later vs. what's done. Each parked thing named explicitly so future-me doesn't reopen them all at once.

7. Cost ledger update if costs were incurred this session. Running tally for case study purposes.

8. What I'm taking with me on the break. What I want to be true at end of session. The win framing.

9. Optional: Note to future Marcus. Direct address. What you want future-you reading this later to remember about today. One paragraph max.

Inputs to use:

- The day's actual events (what shipped, what broke, what got pinned)

- The discipline calls (where I almost spun out and didn't, or where I did spin out and recovered)

- The cost ledger updates (Replit credits, API spend, infra costs, time)

- Any commits, PRs, or deployment milestones with their exact identifiers

- Side-quest temptations resisted (this is the case study evidence, name them explicitly)

What NOT to do:

- Don't manufacture drama. If a day was clean and uneventful, the entry is short and clean.

- Don't compress timeline. If it took 90 minutes, say 90 minutes.

- Don't claim more than was done. If a PR shipped but isn't merged, say "shipped, not merged."

- Don't write a case study in disguise. This is the private log. The public case study is downstream.

- Don't include sensitive personal content if the day didn't include it. The privacy boundary is real.

- Don't add em dashes, divider lines, or generic AI-style closing flourishes.

Stop after the entry. No meta-commentary about what was generated.

Retail Value Prompt

You are a senior technical cost analyst with 15 years of experience pricing software agency engagements, fractional CTO retainers, and solo builder projects. You price work honestly, not generously. No inflation, no hype.

I am going to paste the log or summary of a day's build work. Produce the full comparative analysis in this exact format.

1. Work inventory

List every discrete deliverable from the session in plain language. One line each. A client should be able to read this and understand what they received without knowing anything about the technical process. Group by category: Backend, Frontend, Infrastructure, QA and Testing, DevOps, Architecture and Design, Technical Leadership.

Discount any deliverable that was partially done and note it. Base everything on verified delivered work only, not work in progress.

2. 2022 pre-AI pricing and timelines

What this work cost and took before AI tooling existed. Two perspectives.

Agency or dev shop (external):

Show as a table: Category | Sr dev days | Labor cost | Agency billing at 2x

Total row at the bottom.

Use $150/hour blended senior dev rate. Use 2x for agency margin.

Then one line: Traditional agency timeline: X to Y calendar weeks with a team of 2 to 3.

Solo builder (internal):

What would a skilled solo freelancer or indie founder have paid in their own time to deliver the same scope without AI, contracting out nothing?

Show as a table: Category | Solo days | Opportunity cost at $100/hour

Total row at the bottom.

Then one line: Solo builder timeline: X to Y calendar weeks working full time.

Then one line: Realistic timeline for a solo founder splitting time with sales, ops, and life: X to Y months.

3. 2026 AI-native pricing and timelines

What this work is worth and costs now, in today's market where AI tooling is table stakes. Two perspectives.

fCTO or AI-native dev shop billing a client:

The client sees outcomes. They do not see which tools were used. Bill for results at current market rates.

Use these rates:

- fCTO strategy and architecture: $250/hour

- Senior engineering delivery: $200/hour

- QA, testing, verification: $150/hour

- DevOps and infrastructure: $175/hour

- Technical project management: $175/hour

Show as a table: Category | Hours | Rate | Billable amount

Total row at the bottom.

Then one line: AI-native fCTO timeline: X to Y days of director time.

Then one line: What a 2026 AI-native agency would quote for the same scope: $X to $Y over X to Y weeks.

Solo AI-native builder (internal):

Your actual cost in director hours. Use $150/hour as your floor personal rate unless I specify otherwise.

Show as a single line: Your actual cost: X director hours at $150/hour floor = $X in your time.

Then one line: Effective compression ratio versus 2022 solo builder: Xx.

4. Actual timeline versus 2026 market standard

This section compares what you actually did today against what a well-resourced 2026 AI-native team would consider normal delivery speed for the same scope.

Show as a table with four columns: Deliverable | Your timeline | 2026 market standard | Your delta

2026 market standard definitions to use:

- A well-resourced AI-native agency in 2026 still has coordination overhead, client review cycles, QA sign-off processes, and multi-person handoffs. They are faster than 2022 but not as fast as a focused solo director.

- A 2026 AI-native solo founder with your skill level and setup is the benchmark for the solo column.

- Use realistic estimates, not best-case. Account for context switching, tooling friction, and review cycles that exist even in AI-native shops.

After the table, two lines:

- Where you outpaced the 2026 market and why (one sentence, specific)

- Where the 2026 market would have matched or beaten you and why (one sentence, specific, honest)

5. Value delivered today

Four lines:

- 2022 agency would have billed a client: $X to $Y

- 2026 fCTO bills a client today: $X to $Y

- Your personal cost as AI-native solo: $X in director time

- Your timeline versus 2026 market standard: faster / slower / comparable (one word, then one clause of context)

Then one sentence on what drove the range in the billing figures.

6. Margin reality (private, not for client)

Billable amount at 2026 fCTO rates minus your personal cost, expressed as a dollar amount and a percentage margin.

One sentence on what this margin means for the Eagle Rocket fCTO business model.

7. Running context

If I give you prior session totals, add today to the running tally:

- Total billed this sprint/week/project at 2026 fCTO rates: $X

- Total director hours logged: X hours

- Effective hourly yield on your time: $X per hour

8. One honest caveat

Name one thing a 2022 senior dev, a 2026 AI-native agency, or a better-resourced solo builder would have delivered better or faster than you did today. Be specific, not generic. This is for your eyes only, not the client.

9. Conclusion

Three short paragraphs, plain language, no hype.

Paragraph one: What this session actually proved about the AI-native solo builder model. Ground it in the specific numbers from this analysis, not generic claims about AI.

Paragraph two: What the margin and compression ratio mean for Eagle Rocket as a business. Be honest about where the model is strong and where it has limits at current scale.

Paragraph three: One thing today's session revealed about how to run these sessions better next time. Operational, specific, forward-facing.

Rules:

- Bill for outcomes, not process. Clients do not pay less because AI helped. They pay for the result.

- Do not count infra costs unless I specify that I paid for them out of pocket.

- Discount partially completed work proportionally and note it.

- Base everything on verified delivered work only.

- Do not inflate to make AI look better. Honest numbers protect the business model long term.

- The margin reality section is private operator context. Do not frame it as something to share with a client.

- In the 2026 sections, assume AI tooling is standard across the market. The edge is not having AI. The edge is how well you direct it.

- In the actual timeline comparison, be honest when the 2026 market would have matched you. The point is calibration, not self-promotion.

Here is today's session log:

[PASTE BUILDER'S LOG OR PICK-UP NOTE HERE]

Builder's Log: The Cave Day 1

Builder's Log: The Cave Day 1. Session 1. Kuta Lombok, evening.

Opening orientation

The plan was simple and I held to it: build and deploy a working prototype of The Cave in a single evening session. Not a wireframe. Not a repo with aspirational folder structure. A live URL with a playable, state-governed AI world behind it. The thesis to prove was narrow: the designer writes the laws, the player speaks freely, the AI performs the world. One cave, one guide, one exit, one win condition. That's it.

What actually happened

Started the session with spec work and agent prompt drafting, which took longer than raw coding would have but that's the Director Model tax. Worth it. Once the prompts were written, Phase 0 went to a single CC instance to scaffold the monorepo. It came back clean in under 30 minutes. Foundation verified: client on 5173, server on 3001, health endpoint responding.

Phase 1 released six agents in parallel, each owning a disjoint file slice. Engine, backend, frontend shell, sidebar, state wiring, styling. The engine agent delivered 19 passing tests. The others committed on time with minor type issues that Phase 2 was explicitly tasked to resolve. The parallel build worked. No meaningful merge conflicts given the lane discipline in the prompts.

Phase 2 integrated, ran the happy path to B4_EXIT, confirmed the debug panel was proving governance rather than just displaying state. Committed 48ea06f phase 2: integration and ship. That was 55 minutes in.

The next 55 minutes were a different kind of work. First deploy to Fly hit the wrong directory, then a missing Dockerfile, then an interactive prompt that Git Bash couldn't handle cleanly. Got around it with fly apps create followed by direct fly deploy. The client went to Vercel but deployed from the root instead of the client folder. Redeployed from inside client. VITE_API_URL wasn't picked up until a manual vercel --prod after adding the env var.

Then the narrator started returning the fallback string for every failure outcome. Logs showed NARRATE INPUT: failure with no output following. Went through three agent fixes: open cors, narrator prompt update, timeout addition, keep-alive disabled on the OpenAI client. None of them fixed it. The real issue, finally visible in the logs on the fourth pass, was a 401. Wrong API key. The key set on Fly was invalid. Corrected it, redeployed, and the narrator came alive across all outcome types.

Last thing before stopping: the narrator prose was too long and ornate. A one-line prompt fix tightened the length constraint and stripped the purple language. Deployed. Usable.

Specific named moments worth banking

The parallel phase worked exactly as designed. Six agents, six file lanes, no conflicts at checkout. The key was locking the types in Phase 0 and making each prompt explicit about what files the agent owned and what it was not allowed to touch. That discipline paid forward into Phase 2 having clean integration work rather than archaeology. This is repeatable.

The 401 was the most instructive failure of the session. Three agent-level fixes were written, reviewed, committed, and deployed chasing a problem that turned out to be an invalid API key. The code was never the issue. The lesson is not "check the key first" though that is true. The lesson is that in cloud deployments, infrastructure configuration errors and application logic errors produce identical symptoms at the application layer. Logs are the only way to distinguish them and the logs have to be designed to be readable. The NARRATE FALLBACK log line, once it finally appeared, gave the answer in one line.

The debug panel is the proof, not the product. Several times during the session the question arose of whether something was working correctly. The answer came from the debug panel every time. Rule ID, outcome type, state changes, all visible in the sidebar. That panel is what separates this from a chatbot demo. It needs to be in every live demo of The Cave going forward.

The GitHub remote error early in the session was a simple case of the repo not yet existing on the remote. Wasted a few minutes on it. The fix was to create the repo on GitHub first, then push. Obvious in retrospect. Worth noting because it will happen again on the next project and future-me should check remote existence before debugging the push.

What I'm noticing about the work

The build itself was clean. The debugging was not hard, it was just iterative in a way that required staying patient with the process rather than spinning out into rewrites. There was a moment around the third narrator fix where the temptation was to restructure the whole model client from scratch rather than isolate the actual failure. Held the line. The clean rewrite was eventually necessary but only after the logs confirmed it was needed, not before.

Phronesis showed up here in the practical sense. Not the version that means general wisdom. The version that means knowing when to act and how much force to apply. The error was upstream of the code. Applying more code force to a configuration problem would have wasted another hour.

The side-quest temptation that came up at the start of the session, and was flagged and named before the build began, was the question of whether this belonged ahead of Anchor V4. The answer given and held: tonight is a proof of mechanism, one session, not a new primary track. That frame held through the full session. The Cave got built. Anchor remains the production commitment.

Where I am now

The prototype is live at a Vercel URL. The happy path is completable. The debug panel is working. The narrator is responding to all outcome types. The narrator prose is tighter after the final prompt fix.

What is not done: narrator tone is still slightly too formal and occasionally verbose despite the fix. The parser does not handle vague movement inputs like "I walk" or rhetorical questions like "who is the man" reliably. The win screen has not been tested all the way through in the live deployment. No custom domain.

Emotionally the build feels complete. Actually it is about 85 percent of what a clean demo-ready prototype needs to be.

Things to lock in before stopping

Parser gap on vague movement: "I walk," "I try to walk," "I move" are returning unknown instead of move with null destination. Parked. Not tonight.

Narrator tone: length constraint is better but the register still drifts toward literary in failure outcomes. A more specific negative example in the prompt would fix it. Parked.

Win screen live test: the happy path was confirmed locally by Phase 2 but has not been run end to end on the live Vercel deployment. Should be the first thing done next session.

Custom domain: not tonight. This is a proof, not a product.

LATER.md: voice for Socrates, multiple rooms, river crossing, post-game reflection layer, Anchor-adjacent recovery simulation, world editor. All named and parked. None reopened.

Cost ledger

Session time: 1 hour 50 minutes. Time to first live deploy: 55 minutes. Time in post-deploy debugging: 55 minutes. OpenAI API spend: nominal, a few dozen narrator and parser calls at gpt-4o rates. No meaningful cost. Fly.io: free tier, no charge. Vercel: free tier, no charge. CC agent instances: 8 across all phases. Sonnet 4.6 throughout. Running total for The Cave: under $1 in API costs.

What I'm taking with me

A working prototype of a state-governed AI world, deployed and accessible from a public URL, built in under two hours from an empty folder. The debug panel shows the mechanism. The narrator responds. The engine governs. That is what was promised at the start of the session and it is what exists now.

Note to future Marcus

The mechanism works. You proved it tonight in Kuta Lombok in under two hours with six parallel agents and a handful of CLI commands. When someone asks whether directed emergence is real or whether the Director Model is a real way to build, this session is part of the answer. The Cave is a small thing. The proof it represents is not small. Don't let the narrator tone or the parser gaps talk you into thinking the prototype failed. It shipped. It runs. It governs. That was the night's work and it was done.

Cost analysis

The Cave: Session 1 Cost Analysis Kuta Lombok. 1 hour 50 minutes. Single session, Day 1.

1. Work inventory

Backend

Deterministic rule engine, 11 rules in priority order, pure TypeScript, no I/O or mutation (delivered, 19 passing tests)

Express API server with /api/turn and /api/health routes

OpenAI integration: two-call architecture (parser via function calling, narrator via chat completions)

Parser system prompt with intent mapping and function schema

Narrator system prompt with hard governance constraints

Initial state export and type definitions

Frontend

React + Vite + TypeScript client application

Transcript component with auto-scroll and loading indicator

Input component with placeholder and example hints

Sidebar with location panel, inventory, discovered objects list

Debug panel (toggleable, shows parsed intent, matched rule ID, outcome type, state changes)

Win screen with closing narration and restart

Client-side state management with localStorage persistence

API client with error handling

Infrastructure and DevOps

npm workspaces monorepo with concurrent dev script

Vite proxy config for local development

Fly.io server deployment with Dockerfile

Vercel client deployment with VITE_API_URL environment variable

GitHub repo setup and master branch pushed

QA and Testing

19 passing engine unit tests covering full happy path, 8 failure cases, Socrates dialogue, look and inspect variants, and state immutability

Manual happy path verification through B4_EXIT in local environment

Invalid action testing (Z_INVALID confirmed, no state bleed)

Debug panel verified as accurate against engine output

Architecture and Design

Full system architecture: player input to parser to engine to narrator pipeline

Locked TypeScript type contracts shared across client and server

6-agent parallel build strategy with disjoint file ownership

Phase 0/1/2 sequencing design

Governance thesis: state owns truth, AI performs, engine governs

Technical Leadership

8 agent prompts written across all phases

Parallel coordination of 6 simultaneous build agents

Phase 2 integration triage and handoff

Post-deploy debugging triage across 4 iteration cycles

Partial or incomplete (discounted)

Narrator tone: functional but still occasionally verbose in failure outcomes. Estimated 75 percent done.

Parser coverage: vague movement inputs and rhetorical questions return unknown. Estimated 80 percent done.

Win screen: confirmed locally, not verified end to end on live deployment. Marked incomplete.

2. 2022 pre-AI pricing and timelines

Agency or dev shop (external):

Category

Sr dev days

Labor cost

Agency billing at 2x

Architecture and Design

2.5

$3,000

$6,000

Backend Engineering

4.0

$4,800

$9,600

Frontend Engineering

3.5

$4,200

$8,400

QA and Testing

1.5

$1,800

$3,600

Infrastructure

1.0

$1,200

$2,400

DevOps

1.0

$1,200

$2,400

Technical Leadership

1.0

$1,200

$2,400

Total

14.5

$17,400

$34,800

Traditional agency timeline: 2 to 3 calendar weeks with a team of 2 to 3.

Solo builder (internal):

Category

Solo days

Opportunity cost at $100/hour

Architecture and Design

2.0

$1,600

Backend Engineering

5.0

$4,000

Frontend Engineering

4.0

$3,200

QA and Testing

2.0

$1,600

Infrastructure

1.5

$1,200

DevOps

1.0

$800

Technical Leadership

1.0

$800

Total

16.5

$13,200

Solo builder timeline: 3 to 4 calendar weeks working full time. Realistic timeline for a solo founder splitting time with sales, ops, and life: 2 to 3 months.

3. 2026 AI-native pricing and timelines

fCTO or AI-native dev shop billing a client:

Category

Hours

Rate

Billable amount

Architecture and Design

4.0

$250

$1,000

Backend Engineering

5.0

$200

$1,000

Frontend Engineering

4.0

$200

$800

QA and Testing

1.5

$150

$225

Infrastructure

1.5

$175

$263

DevOps

2.0

$175

$350

Technical Project Management

2.0

$175

$350

Total

20.0

$3,988

AI-native fCTO timeline: 1 to 2 days of director time. What a 2026 AI-native agency would quote for the same scope: $6,000 to $12,000 over 1 to 2 weeks, accounting for client review cycles, QA sign-off, and handoff overhead.

Solo AI-native builder (internal): Your actual cost: 1.83 director hours at $150/hour floor = $275 in your time. Effective compression ratio versus 2022 solo builder: 72x.

4. Actual timeline versus 2026 market standard

Deliverable

Your timeline

2026 market standard

Your delta

Monorepo scaffold and type contracts

30 min

1 to 2 hours

Faster

6-slice parallel build

25 min wall clock

2 to 4 hours

Significantly faster

Integration and local happy path

20 min

1 to 2 hours

Faster

First live deploy (client and server)

55 min total

1 to 2 hours

Comparable

Post-deploy debugging

55 min

20 to 40 min

Slower

Narrator prompt tuning

15 min

30 to 60 min

Faster

Where you outpaced the 2026 market and why: The parallel Phase 1 build collapsed sequential feature development into simultaneous commits, which no multi-person agency pipeline matches without upfront coordination overhead that typically consumes the time saved.

Where the 2026 market would have matched or beaten you and why: A well-resourced AI-native team with a deployment pre-flight checklist would have caught the invalid API key in under 10 minutes rather than across four iteration cycles, saving roughly 35 minutes of the debugging session.

5. Value delivered today

2022 agency would have billed a client: $28,000 to $38,000 2026 fCTO bills a client today: $3,500 to $5,000 Your personal cost as AI-native solo: $275 in director time Your timeline versus 2026 market standard: Faster, primarily due to parallel agent coordination that collapsed the build phase below what any sequentially structured team achieves.

The range in the billing figures is driven by how the client values the governance architecture. A client who understands that the debug panel proves rule-based AI governance pays the top of the range. A client who sees a text adventure pays the bottom.

6. Margin reality (private, not for client)

Billable at 2026 fCTO rates: $3,988 Your personal cost: $275 Gross margin: $3,713 at 93 percent.

At 93 percent gross margin on a 1.83-hour engagement, the Eagle Rocket fCTO model is not a services business in any traditional sense. It is a leverage business where the constraint is director attention, not labor hours. The limit on scale is not capacity, it is how many engagements can be run simultaneously before triage quality drops.

7. Running context

Total billed this project at 2026 fCTO rates: $3,988 Total director hours logged: 1.83 hours Effective hourly yield on your time: $2,180 per director hour.

8. One honest caveat

A senior DevOps engineer on a well-resourced 2026 AI-native team would have written a pre-flight deployment script that validates the API key against the provider before deploying, which would have eliminated the longest single failure loop in the session. That is not a gap in the Director Model. It is a gap in the deployment runbook, and it is fixable before the next project.

9. Conclusion

What this session proved about the AI-native solo builder model is specific and numeric. A 14.5 senior dev day engagement was delivered in 1.83 director hours at 93 percent gross margin. The mechanism that made that possible was not AI in general. It was phase-locked parallel coordination with typed contracts established before any agent touched a file. The 6-agent parallel build is the unit to study. That is the replicable pattern, not the tools.

For Eagle Rocket, the margin reality points to a clear business constraint. At $2,180 effective hourly yield, the model works only if the director stays at director altitude. The 55 minutes of post-deploy debugging in this session were not fCTO work. They were hands-on DevOps work that could have been delegated to an agent with a better pre-flight prompt. Every minute of debugging that Marcus does personally is $2,180 per hour of leverage sitting idle. The model is strong on architecture and coordination. It has room to tighten on infrastructure runbooks.

The operational lesson from this session is to write a deployment pre-flight prompt before the first deploy on every future project, not after the first 401. The prompt should check API key validity, confirm correct working directory, verify environment variable propagation, and confirm health endpoint before releasing the client URL. That single prompt would have saved 30 to 40 minutes of this session and is now a standard asset for every Eagle Rocket build.
