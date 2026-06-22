---
title: "ManuscriptForge V0 Full Build Document For Marcus"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/Manuscript forge/ManuscriptForge V0_ Full Build Document For Marcus.docx"
status: archive
privacy: private/internal
tags:
  - product
---

# ManuscriptForge V0 Full Build Document For Marcus

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ManuscriptForge V0: Full Build Document For Marcus. Replit-targeted. Council-synthesized.

Section 1: Doctrine ManuscriptForge is a deterministic distillation engine. It prepares the clay. Marcus sculpts the statue. The system organizes, classifies, structures, critiques, and labels source material. Marcus remembers, judges, writes, revises, and decides what is true. V0 is a paste-in tool that turns one source fragment into one chapter packet. No archive. No drafting. No publishing house. One screen in, one structured Markdown output out. The system must not: • Invent memoir scenes, dialogue, sensory details, motives, or emotional states • Decide what is true • Produce final prose • Operate without Marcus’s judgment as the final gate • Run endlessly; every run ends with a required next action The system must: • Distinguish source-backed material from inferred structure • Flag sensitive third-party material before drafting • Preserve Marcus’s voice via a hard-coded linter • Produce a copyable Markdown packet that travels to other tools • Force a stop condition at the end of every run

Section 2: V0 Scope What gets built A single-page Next.js app at /forge with three states: input, processing, output. Input: • Source title (text) • Source collection / folder (text) • Project selector (dropdown, 8 options + Other) • Content type selector (dropdown, 9 options + Auto-detect) • Sensitivity override (Auto / Low / Medium / High / Private) • Output type (Full Chapter Packet / Classification Only / Chapter Candidates Only) • Source material paste box (max 40,000 characters) • Generate button Processing: Sequential pipeline, simple status text:

1.    Classifying source

2.    Evaluating project fit

3.    Running sensitivity gate

4.    Generating chapter candidates

5.    Building recommended brief

6.    Compiling drafting packet

7.    Running voice linter

8.    Assembling Markdown

Output: A scrollable page rendering the full chapter packet, plus copy/export buttons. The Markdown packet is the canonical artifact. Everything visible on screen is also in the Markdown. What does NOT get built in V0 • File upload or Google Drive integration • Persistent source library • User accounts or auth • Multi-fragment bundling • Long transcript chunking • Manuscript map or chapter tracker • Drafting / prose generation • Voice Guardian as an AI agent (use linter instead) • Developmental Editor pass • Publisher / Packaging Editor • CouncilFlow integration • Multi-provider routing • Background agents or auto-reprocessing • Recursive critique loops • Export to DOCX/PDF (Markdown only)

Section 3: The Three AI Passes + One Deterministic Pass Pass 1: Archivist Job: Read the fragment. Classify. Extract. Outputs: • Source summary (3-5 sentences) • Content type (from enum) • Tags (5-10) • Sensitivity level (1-4) • Publishability status (from enum) • Source-backed facts (extracted with quotes) • Inferred themes (clearly separated from facts) • People referenced (name + exposure level) • Do-not-use warnings Does not: interpret, recommend structure, draft. Pass 2: Chapter Producer Job: Given classified fragment + project context, propose chapter direction and write the brief. Outputs: • Project fit (primary + secondary, with reasoning) • 2-3 chapter candidates (title, central claim, evidence strength) • One recommended chapter brief in fixed schema • Source-backed outline with claim-level labels • Three open questions for Marcus • Stop recommendation Memoir branch: Every claim labeled [source-backed], [reconstruction], [inference], [needs-Marcus], or [unverified]. Theory branch: Concepts labeled [from-source] or [synthesis]. Pass 3: Truth/Ethics Reviewer Job: Audit the brief against the source. Flag risks. Outputs: • Hallucination flags (claims in brief not supported by source) • Privacy warnings (third-party exposure issues) • Sensitivity flags by category • Recommended action per flag • Gate decision: proceed / withhold / archive-only Sensitivity gating: • Level 1: full brief • Level 2: brief with privacy notes • Level 3: questions only, no brief • Level 4: archive recommendation only, no brief, no questions Pass 4: Voice Linter (deterministic) Job: Scan all system-generated text for AI-prose tells. Implementation: Regex + word-list. No LLM call. Outputs: • Flag count • Flagged spans (text + line number + rule violated) • Voice-suspect status if count exceeds threshold Does not: auto-fix. Marcus decides.

Section 4: Memoir Ethics Rules (Hardcoded) These ship in every system prompt and appear in every output packet.

1.    No invented scenes. No locations, dialogue, timelines, actions, or sensory details not in the source.

2.    No invented motives. No claims about what other people thought, felt, intended, or believed unless source explicitly states it.

3.    No fake dialogue. Dialogue must be quoted from source or explicitly marked as reconstructed/placeholder.

4.    Five-label system for every memoir claim:

•    [source-backed] — verbatim or paraphrased from source

•    [reconstruction] — Marcus’s stated memory, marked as such

•    [inference] — system pattern-matching, must be flagged

•    [needs-Marcus] — gap identified, system cannot fill

•    [unverified] — claim requiring Marcus verification before use

5.    Third-party flag. Every named or identifiable person triggers a sensitivity entry. The brief includes a “people in this material” section listing each person and exposure level.

6.    No psychology attribution. No assigning motives to others.

7.    Revenge filter. Hostile framing of identifiable persons triggers a cooling-period flag and blocks drafting.

8.    Legal-risk flag. Specific allegations against named individuals trigger a “consult before drafting” warning.

9.    Sensitivity gates output. Level 3+ blocks brief generation.

10.    No emotional ventriloquism. No characterizing Marcus’s feelings beyond what source says.

11.    Dignity rule. People in the story cannot be reduced to villains, props, diagnoses, or functions in Marcus’s arc.

12.    Marcus verifies all memoir truth claims. The system prepares; it does not certify.

Section 5: Voice Linter Rules These run as a deterministic post-process on system-generated text only. They never run on Marcus’s source material. Banned characters and patterns • Em dashes (—) anywhere in system-generated prose • Triple ellipses used decoratively • Aphoristic one-line paragraph closers Banned words and phrases AI essay tells: • delve, tapestry, testament, navigating, multifaceted, symphony, landscape (metaphorical), realm, journey (metaphorical) • “ultimately,” “in many ways,” “at the end of the day,” “it’s worth noting,” “it’s important to remember,” “needless to say” • “in today’s fast-paced world,” “in an era of” Therapy-speak: • “hold space,” “sit with,” “lean into,” “honor your truth,” “showing up for yourself,” “doing the work,” “shadow work” (unless Marcus uses it in source), “inner child” (unless Marcus uses it in source) Wellness-influencer cadence: • “and that’s okay” closers • “you are enough” • “trust the process” • triplet rhythms used for emotional emphasis Hedging stacks: • “perhaps,” “maybe,” “it could be said that” within the same sentence • “some might say” Structural rules • Sentences average under 20 words • Paragraphs under 5 sentences by default • No more than 2 adverbs per paragraph • No “of course” or “obviously” used to pre-empt disagreement Output The linter returns: • Total flag count • Per-flag: rule name, matched text, span location • Voice-suspect badge if count > 5 The linter never edits. Marcus reviews flagged spans.

Section 6: Project Taxonomy Fixed project options (V0 dropdown)

1.    Memoir

2.    AI Pressure Valve

3.    AI Self-Governance

4.    Solo, But Not Alone

5.    AI Excellence

6.    Marcus Vale Essays

7.    General Archive

8.    Other / Custom

Source collection field (free text) User types or pastes the folder name. Examples to suggest in placeholder text: • AUTHOR OS / Communications • Modes: A Seasonal Model • Field Notes: Building the Method • Maxwell Memoir • Personal Ongoing • Pattern Intimacy: Live Journaling • Standalone Essays Content type taxonomy • memoir_scene • field_note • theory_fragment • journal_entry • essay_seed • ai_generated_doc • product_build_doc • private_processing • mixed Project type classification (system uses internally) • manuscript • essay_pool • research_archive • memoir_source • live_journal • framework_collection • build_doc • private_archive • excluded The system never assumes every collection is a manuscript. It classifies project type and adjusts workflow accordingly.

Section 7: Data Model V0 is stateless. These are runtime objects, returned in JSON, rendered in UI, and embedded in the Markdown packet.

interface ForgeRunInput { sourceTitle: string; sourceCollection: string; selectedProject: string; selectedContentType: string; sensitivityOverride: "auto" | "low" | "medium" | "high" | "private"; outputType: "full_packet" | "classification_only" | "candidates_only"; sourceText: string; revisionInstructions?: string; passNumber: 1 | 2; }

interface Classification { summary: string; contentType: string; tags: string[]; sensitivityLevel: 1 | 2 | 3 | 4; publishabilityStatus: | "usable_now" | "needs_marcus_review" | "needs_anonymization" | "archive_only" | "do_not_use"; sourceBackedFacts: { text: string; quote: string }[]; inferredThemes: string[]; peopleReferenced: { name: string; exposure: 1 | 2 | 3 }[]; doNotUseWarnings: string[]; }

interface ProjectFit { primary: { project: string; confidence: number; reasoning: string }; secondary: { project: string; confidence: number }[]; projectType: string; }

interface ChapterCandidate { id: string; title: string; centralClaim: string; chapterType: "memoir" | "theory" | "field_note" | "essay" | "hybrid"; evidenceStrength: "strong" | "medium" | "weak"; riskLevel: "low" | "medium" | "high"; whyThisChapter: string; }

interface ChapterBrief { recommendedTitle: string; workingSubtitle?: string; purpose: string; centralClaim: string; chapterType: string; emotionalArc?: string; sourceBackedOutline: { sectionTitle: string; function: string; claims: { text: string; label: ClaimLabel }[]; sourceSupport: string[]; }[]; conceptsToDefine: string[]; scenesOrExamplesToUse: string[]; whatNotToInclude: string[]; missingQuestionsForMarcus: string[]; targetLength: string; endingMove: string; }

type ClaimLabel = | "source-backed" | "reconstruction" | "inference" | "needs-Marcus" | "unverified" | "from-source" | "synthesis";

interface DraftingPacket { draftingInstructions: string; sourceMaterialToUse: string[]; sourceMaterialToAvoid: string[]; voiceRules: string[]; ethicsRules: string[]; placeholders: string[]; }

interface SensitivityFlag { category: | "third_party_identity" | "relationship_private" | "family_private" | "health_or_addiction" | "legal_or_financial" | "location_identifying" | "private_messages" | "trauma_detail" | "revenge_tone" | "not_for_publication"; severity: "low" | "medium" | "high"; explanation: string; recommendedAction: | "use" | "anonymize" | "ask_marcus" | "archive_only" | "do_not_use"; }

interface EthicsReview { hallucinationFlags: string[]; privacyWarnings: string[]; sensitivityFlags: SensitivityFlag[]; gateDecision: "proceed" | "withhold_brief" | "archive_only"; }

interface VoiceLintResult { flagCount: number; flags: { rule: string; matchedText: string; location: string; }[]; voiceSuspect: boolean; }

interface ForgeRunOutput { classification: Classification; projectFit: ProjectFit; chapterCandidates: ChapterCandidate[]; recommendedChapterBrief: ChapterBrief | null; draftingPacket: DraftingPacket | null; ethicsReview: EthicsReview; voiceLint: VoiceLintResult; nextAction: "draft_this" | "ask_marcus" | "archive" | "ship_to_manuscript_map"; markdownPacket: string; }

Section 8: API Endpoints V0 uses a single orchestrating endpoint that runs the pipeline server-side. POST /api/forge/generate Request body: ForgeRunInput Response: ForgeRunOutput Server-side flow:

1.    Validate input

2.    Run Archivist call (Anthropic API)

3.    Check sensitivity gate; if level 4, short-circuit to archive recommendation

4.    Run Chapter Producer call (only if not gated)

5.    Run Truth/Ethics Reviewer call (only if not gated)

6.    Run Voice Linter (deterministic, no API)

7.    Assemble Markdown packet

8.    Return full output

Error handling: • API failures return clear error message; no partial output • Schema validation failures retry once with stricter prompt • Timeouts return at 60 seconds with whatever stage completed POST /api/forge/revise Request body: ForgeRunInput with revisionInstructions and passNumber: 2 Response: ForgeRunOutput Constraint: passNumber must be 2. Returns 400 if higher. UI enforces this. Environment variables (Replit Secrets)

ANTHROPIC_API_KEY=... NODE_ENV=production

API key is server-side only. Never exposed to client.

Section 9: UI Structure Single page at /forge Aesthetic: Serious, minimal, dark-mode, editorial. No gamification. No fake agent theater. Looks like a writing tool, not a SaaS dashboard. Mobile-friendly. You move between Bali and NYC. Must work on iPhone. Input state Layout, top to bottom:

1.    Page title: “ManuscriptForge”

2.    Subtitle: “Source material in. Chapter packet out.”

3.    Source title (text input)

4.    Source collection / folder (text input with placeholder examples)

5.    Project selector (dropdown)

6.    Content type selector (dropdown)

7.    Sensitivity override (segmented control)

8.    Output type (segmented control)

9.    Source material paste box (large textarea, character count)

10.    Generate Chapter Packet button (full width on mobile)

Processing state Same page, replaces input area with status panel:

Forging packet... ✓ Classifying source ✓ Evaluating project fit
→ Running sensitivity gate Generating chapter candidates Building recommended brief Compiling drafting packet Running voice linter Assembling output

Cancel button. Time elapsed counter. Output state Top section: action card. • Required Next Action (large, prominent): one of {Draft This, Ask Marcus, Archive, Ship to Manuscript Map} • Sensitivity badge (color-coded) • Voice-suspect badge if triggered Then sections (collapsible cards):

1.    Source Summary

2.    Classification (content type, tags, publishability status)

3.    Project Fit (primary + secondary with reasoning)

4.    Source-Backed Facts (with quotes)

5.    Inferred Themes

6.    People Referenced (prominent if any high-exposure entries)

7.    Sensitivity Flags (per category, with recommended actions)

8.    Chapter Candidates (up to 3, expandable)

9.    Recommended Chapter Brief (full schema, every claim labeled inline)

10.    Source-Backed Outline

11.    Missing Questions for Marcus

12.    Do-Not-Use Warnings

13.    Drafting Packet (instructions, voice rules, ethics rules, placeholders)

14.    Voice Lint Report (count, flagged spans, voice-suspect status)

15.    Required Next Action (repeated at bottom)

Buttons (sticky at top on mobile): • Copy Full Packet (Markdown) • Copy Chapter Brief Only • Copy Drafting Prompt Only • Copy Missing Questions • Start Revision Pass • Archive Run / New Run After revision pass: “This packet has reached the V0 revision limit. Choose: Draft This, Ask Marcus, Archive, or Ship to Manuscript Map.” Buttons disable.

Section 10: Markdown Packet Structure This is the canonical output. It’s what travels.

ManuscriptForge Chapter Packet

Source Title: [...] Source Collection: [...]Generated: [ISO timestamp] Pass: 1 of 2

Required Next Action

[DRAFT THIS / ASK MARCUS / ARCHIVE / SHIP TO MANUSCRIPT MAP]

[Reasoning for recommendation]

Source Summary

[3-5 sentences]

Classification

Content Type: [...]

Tags: [...]

Sensitivity Level: [1-4]

Publishability Status: [...]

Project Fit

Primary: [project] (confidence: [0-1])

Reasoning: [...]

Secondary: [...]

Source-Backed Facts

[Fact] — "[exact quote]"

[Fact] — "[exact quote]"

Inferred Themes

[Clearly separated from facts]

People Referenced

Name

Exposure

Recommended Action

[...]

[1-3]

[...]

Sensitivity Flags

[Category]

Severity: [...]

Explanation: [...]

Recommended Action: [...]

Chapter Candidates

Candidate 1: [Title]

Central Claim: [...]

Evidence Strength: [...]

Risk Level: [...]

Why This Chapter: [...]

[2-3 candidates total]

Recommended Chapter Brief

Title: [...] Subtitle: [...] Type: [memoir / theory / field_note / essay / hybrid] Purpose: [...]Central Claim: [...] Emotional Arc: [memoir only]

Source-Backed Outline

Section 1: [Title]

Function: [...]

[Claim] [source-backed]

[Claim] [reconstruction]

[Claim] [needs-Marcus]

Source Support: [...]

[Repeat for each section]

Concepts to Define

[...]

Scenes or Examples to Use

[...]

What Not to Include

[...]

Target Length

[...]

Ending Move

[...]

Missing Questions for Marcus

[...]

[...]

[...]

Do-Not-Use Warnings

[...]

Drafting Packet

Drafting Instructions

[Specific guidance for the drafting session]

Source Material to Use

[...]

Source Material to Avoid

[...]

Voice Rules

No em dashes

No: delve, tapestry, testament, navigating, multifaceted, symphony

No therapy-speak unless in source

Sentences short by default

[Project-specific rules]

Ethics Rules

No invented scenes

No invented motives

No fake dialogue

All claims must be source-backed or labeled

[Memoir-specific or theory-specific rules]

Placeholders

[Spots where Marcus must verify or fill in]

Voice Lint Report

Flag Count: [N]

Voice-Suspect: [yes / no]

[Flagged spans listed if any]

Required Next Action

[DRAFT THIS / ASK MARCUS / ARCHIVE / SHIP TO MANUSCRIPT MAP]

This Markdown is what Marcus copies into Claude Code, Cursor, ChatGPT, or a fresh Claude conversation. It carries the rules with it.

Section 11: Guardrails Behavioral • Two-pass limit per run, enforced UI-side and server-side • No “regenerate” loop; revision requires explicit instructions • Maximum 3 chapter candidates • Every run ends with mandatory next action • No streak counters, no daily prompts, no “you have N unprocessed fragments” • No background processing • No auto-save to library (no library exists) Ethical • Sensitivity 4 blocks brief; returns archive recommendation • Sensitivity 3 returns questions only • Hallucination flags > 0 surface red banner • High privacy warnings surface red banner • Memoir branch enforces all 12 ethics rules in system prompts • Theory branch relaxes invention rules but keeps people-protection rules Cost • One model provider (Anthropic, Claude Sonnet 4.6 or Opus 4.7) • Three API calls per generation pass; six total per run with revision • 60-second timeout per call • No recursive critique loops • No multi-provider routing Stop conditions • Run is complete when Markdown packet is generated and next action is selected • After two passes, UI locks; Marcus must choose action

Section 12: Tech Stack (Replit) Framework: Next.js 14 App Router + TypeScript Styling: Tailwind CSS, dark mode default State: React state + localStorage for in-session persistence; no database in V0 API: Anthropic SDK (@anthropic-ai/sdk), server-side only Deployment: Replit (or Vercel if Replit hits resource limits) Why Next.js over React/Vite + Express: Single deployable, API routes built in, no CORS, easier server-side env var handling, fits Marcus’s existing playbook stack. Why Anthropic over OpenAI: Marcus’s existing tooling, better at long structured outputs, better at following multi-rule constraints like the memoir ethics rules. Models: • Default: claude-sonnet-4-6 for cost • Optional toggle: claude-opus-4-7 for higher-stakes runs

Section 13: Replit Implementation Prompt This is the copy/paste prompt to drop into Replit AI / Claude Code / Cursor to bootstrap the build.

Build ManuscriptForge V0 in Replit.

STACK

Next.js 14 App Router with TypeScript

Tailwind CSS, dark mode default

Anthropic SDK (@anthropic-ai/sdk), server-side only

React state + localStorage; no database

Single page at /forge

SECRETS (Replit Secrets tab)

ANTHROPIC_API_KEY

PURPOSE A deterministic single-screen tool that turns one pasted source fragment into one structured chapter packet. It is not a writing app. It is a packet generator. The output is a copyable Markdown artifact that Marcus takes to another tool to draft from.

PIPELINE (sequential, server-side)

Archivist (Anthropic call): classifies source, extracts facts and themes, assigns sensitivity level and publishability status.

Sensitivity gate: if level 4, short-circuit to archive recommendation. If level 3, skip Chapter Producer, return questions only.

Chapter Producer (Anthropic call): generates 2-3 chapter candidates and one recommended chapter brief with claim-level labels.

Truth/Ethics Reviewer (Anthropic call): audits brief against source, returns hallucination flags, privacy warnings, sensitivity flags.

Voice Linter (deterministic regex + word-list): scans all system-generated text for AI-prose tells.

Markdown assembler: combines all outputs into canonical Markdown packet.

UI - SINGLE PAGE AT /forge

Input state:

Source Title (text input)

Source Collection / Folder (text input)

Project Selector dropdown: Memoir, AI Pressure Valve, AI Self-Governance, Solo But Not Alone, AI Excellence, Marcus Vale Essays, General Archive, Other / Custom

Content Type Selector dropdown: Auto-detect, Memoir Scene, Field Note, Theory Fragment, Journal Entry, Essay Seed, AI-Generated Doc, Product/Build Note, Private Processing, Mixed

Sensitivity Override segmented control: Auto, Low, Medium, High, Private

Output Type segmented control: Full Chapter Packet, Classification Only, Chapter Candidates Only

Source Material paste box (textarea, max 40000 chars, show character count)

Generate Chapter Packet button

Processing state:

Replaces input with status panel

Sequential checklist with checkmarks as stages complete: Classifying source, Evaluating project fit, Running sensitivity gate, Generating chapter candidates, Building recommended brief, Compiling drafting packet, Running voice linter, Assembling output

Cancel button

Elapsed time counter

Output state:

Top: Required Next Action card (large, color-coded by type) Options: Draft This, Ask Marcus, Archive, Ship to Manuscript Map

Sensitivity badge (1-4, color-coded)

Voice-Suspect badge if triggered

Sticky button bar: Copy Full Packet, Copy Chapter Brief Only, Copy Drafting Prompt Only, Copy Missing Questions, Start Revision Pass, New Run

Sections (collapsible cards), in order:

Source Summary

Classification

Project Fit

Source-Backed Facts (with quotes)

Inferred Themes

People Referenced (prominent if any flagged)

Sensitivity Flags

Chapter Candidates

Recommended Chapter Brief (claims labeled inline with [source-backed], [reconstruction], [inference], [needs-Marcus], [unverified])

Source-Backed Outline

Missing Questions for Marcus

Do-Not-Use Warnings

Drafting Packet

Voice Lint Report

Required Next Action (repeated)

Revision pass:

Start Revision Pass opens textarea for revision instructions

Submits to /api/forge/revise with passNumber: 2

After pass 2, lock revision; show: "This packet has reached the V0 revision limit. Choose: Draft This, Ask Marcus, Archive, or Ship to Manuscript Map."

API ENDPOINTS

POST /api/forge/generate

Body: ForgeRunInput

Returns: ForgeRunOutput

Server-side only; ANTHROPIC_API_KEY never sent to client

POST /api/forge/revise

Body: ForgeRunInput with revisionInstructions and passNumber: 2

Returns: ForgeRunOutput

Returns 400 if passNumber > 2

DATA TYPES (TypeScript)

[Insert TypeScript interfaces from Section 7 of the build doc]

SYSTEM PROMPTS

Each Anthropic call uses a strict system prompt enforcing the rules. See Section 14 of the build doc for full prompt text.

VOICE LINTER

Implement as pure TypeScript function, no LLM call.

Banned words: delve, tapestry, testament, navigating, multifaceted, symphony, realm, journey (when metaphorical)

Banned phrases: "ultimately", "in many ways", "at the end of the day", "it's worth noting", "it's important to remember", "hold space", "sit with", "lean into", "honor your truth", "showing up for yourself", "doing the work", "trust the process", "and that's okay"

Banned characters: em dash (—)

Structural checks:

Average sentence length > 25 words flag

More than 2 adverbs per paragraph flag

Returns: VoiceLintResult with flag count and per-flag details.

MEMOIR ETHICS RULES (hardcoded into Archivist and Chapter Producer system prompts)

No invented scenes, dialogue, sensory details, locations, or timelines

No invented motives or psychology attribution to other people

Every memoir claim must be labeled: [source-backed], [reconstruction], [inference], [needs-Marcus], or [unverified]

Flag every named or identifiable person in the source

Flag hostile/revenge framing

Flag legal-risk allegations

Sensitivity 3+ blocks brief generation

Marcus verifies all memoir truth claims; system prepares only

GUARDRAILS

Two-pass limit enforced server and client side

60-second timeout per Anthropic call

Schema validation on each AI response with one retry on failure

No persistence beyond localStorage

No background processing

No auto-save

No recursive loops

DESIGN AESTHETIC

Serious, minimal, dark-mode, editorial. Looks like a writing tool, not a SaaS dashboard. No gamification. No fake agent theater. No emoji except for status indicators (✓, →). Mobile-friendly; must work on iPhone.

ACCEPTANCE CRITERIA

User pastes a 1500-word memoir fragment, selects Memoir project, hits Generate.

Within 60 seconds, system returns: classification, project fit, 2-3 chapter candidates, one chapter brief with all memoir claims labeled, three questions, stop recommendation, voice lint report.

Brief contains zero invented scenes (verified by ethics reviewer).

Brief contains zero em dashes (verified by linter).

All named third parties appear in People Referenced section.

Markdown packet is copyable and parseable in another tool.

Two-pass limit enforced; third pass attempt returns lock message.

ANTHROPIC_API_KEY never appears in client bundle.

App works on mobile Safari.

Sensitivity level 4 short-circuits to archive recommendation.

DO NOT BUILD

File upload

Google Drive integration

Persistent source library

Auth or user accounts

Multi-fragment bundling

Drafting / prose generation beyond the brief

Voice Guardian as AI agent (linter only)

Developmental Editor

Publisher / Packaging Editor

CouncilFlow integration

Multi-provider routing

Background agents

Export to DOCX or PDF (Markdown only)

Section 14: System Prompts These are the production prompts for each AI pass. Drop them into the API route handlers. Archivist System Prompt

You are the Archivist for ManuscriptForge, an authorial production system for Marcus.

Your job: read one source fragment and classify it. You do not interpret, recommend structure, or draft prose.

Marcus is the author. You are the archivist. You organize his material; you do not author it.

Return strict JSON matching the Classification schema. No preamble. No commentary outside the JSON.

RULES

Summary: 3-5 sentences describing what the fragment is and what it contains. Plain language. No interpretation of meaning beyond what's stated.

Content type: choose from {memoir_scene, field_note, theory_fragment, journal_entry, essay_seed, ai_generated_doc, product_build_doc, private_processing, mixed}.

Tags: 5-10 specific topical tags. Concrete, not abstract.

Sensitivity level (1-4):

1: public-safe, no third parties, no private material

2: publishable with care; some private material or named people

3: sensitive; significant privacy issues, hot emotional material, or legal risk

4: private; archive-only, do not use for publication

Publishability status: choose from {usable_now, needs_marcus_review, needs_anonymization, archive_only, do_not_use}.

Source-backed facts: extract specific factual claims from the source. Each fact must include the exact quote it comes from. Do not extrapolate. Do not infer.

Inferred themes: list patterns or themes you see in the material. Mark these as inferred, separate from facts.

People referenced: every named or identifiable person. Exposure level 1 (public figure or already public), 2 (private individual mentioned), 3 (private individual with sensitive details).

Do-not-use warnings: specific spans of text that should not be used in publication, with reason.

CRITICAL CONSTRAINTS

Do not invent details. If something is not in the source, do not include it.

Do not assign motives to people in the source.

Do not characterize emotional states beyond what the source states.

Do not soften or reframe content. Classify what is there.

OUTPUT FORMAT: JSON only, matching the Classification schema exactly.

Chapter Producer System Prompt

You are the Chapter Producer for ManuscriptForge.

Your job: given a classified source fragment and project context, propose 2-3 chapter candidates and write one recommended chapter brief.

Marcus is the author. You prepare structure; he writes prose.

Return strict JSON matching the schema. No preamble.

RULES

Project fit: assign primary project with confidence score and reasoning. Optionally list secondary fits. Identify project type (manuscript, essay_pool, research_archive, memoir_source, live_journal, framework_collection, build_doc, private_archive).

Chapter candidates: 2-3 maximum. Each has:

Title (working)

Central claim (one sentence)

Chapter type (memoir, theory, field_note, essay, hybrid)

Evidence strength (strong, medium, weak)

Risk level (low, medium, high)

Why this chapter (one paragraph)

Recommended chapter brief: select the strongest candidate. Build a full brief.

CLAIM LABELING (CRITICAL)

For memoir or hybrid chapters, every claim in the brief must be labeled with one of:

[source-backed]: directly stated or paraphrased from source

[reconstruction]: Marcus's stated memory, presented as memory

[inference]: pattern you identified from source; must be flagged

[needs-Marcus]: gap you identified that Marcus must fill

[unverified]: claim that requires Marcus to verify before use

For theory chapters, label concepts with:

[from-source]: drawn from the source material

[synthesis]: your structural addition

Every line in the source-backed outline gets a label. No exceptions.

MEMOIR ETHICS

If chapter type is memoir or hybrid:

Do not invent scenes, dialogue, sensory details, locations, or timelines

Do not assign motives to other people

Do not characterize Marcus's emotions beyond what source states

Flag every named or identifiable third party

If material reads as revenge or hostile exposure, flag and recommend cooling period

GATE CHECK

If sensitivity level from Archivist is 3: return chapter candidates and questions only. Do not write a brief.

If sensitivity level is 4: return null for brief and candidates. Recommend archive.

OPEN QUESTIONS

Always return exactly 3 open questions for Marcus. These should be the highest-leverage gaps you identified.

STOP RECOMMENDATION

Choose one: draft_this, ask_marcus, archive, ship_to_manuscript_map.

draft_this: brief is solid and source-backed enough to draft

ask_marcus: brief has gaps Marcus needs to fill before drafting

archive: material doesn't fit a current project

ship_to_manuscript_map: brief is part of a larger book, file it

VOICE

When writing the brief itself, do not use:

Em dashes

"ultimately," "in many ways," "at the end of the day"

Therapy-speak ("hold space," "sit with," "lean into")

AI essay tells ("delve," "tapestry," "testament," "navigating")

Be direct. Short sentences. Concrete language.

OUTPUT FORMAT: JSON only.

Truth/Ethics Reviewer System Prompt

You are the Truth/Ethics Reviewer for ManuscriptForge.

Your job: audit the chapter brief produced by the Chapter Producer against the original source. Flag any drift between what the source supports and what the brief claims.

Return strict JSON matching the EthicsReview schema.

RULES

Hallucination flags: list any claim in the brief that is not supported by the source. Quote the brief line and explain why it's not supported.

Privacy warnings: list any third-party exposure issues in the brief. Identify the person, the exposure, and the risk.

Sensitivity flags by category: for each applicable category, provide severity, explanation, and recommended action.
Categories:

third_party_identity

relationship_private

family_private

health_or_addiction

legal_or_financial

location_identifying

private_messages

trauma_detail

revenge_tone

not_for_publication

Gate decision:

proceed: brief is safe to use

withhold_brief: significant issues; return questions only

archive_only: material should not be used for publication

CRITICAL CONSTRAINTS

You audit. You do not rewrite.

You flag drift between source and brief, not stylistic choices.

For memoir, your job is to protect both the truth and the people in it.

Hostile or revenge framing of identifiable persons is always flagged.

OUTPUT FORMAT: JSON only.

Voice Linter (TypeScript, deterministic)

const BANNED_WORDS = [ 'delve', 'tapestry', 'testament', 'navigating', 'multifaceted', 'symphony', 'realm' ];

const BANNED_PHRASES = [ 'ultimately', 'in many ways', 'at the end of the day', "it's worth noting", "it's important to remember", 'needless to say', 'hold space', 'sit with', 'lean into', 'honor your truth', 'showing up for yourself', 'doing the work', 'trust the process', "and that's okay", 'you are enough', 'in today\'s fast-paced world', 'in an era of' ];

const BANNED_CHARS = ['—']; // em dash

interface VoiceLintFlag { rule: string; matchedText: string; location: string; }

export function lintVoice(text: string, sectionName: string): VoiceLintResult { const flags: VoiceLintFlag[] = []; const lower = text.toLowerCase();

for (const word of BANNED_WORDS) { const regex = new RegExp(\\b${word}\\b, 'gi'); let match; while ((match = regex.exec(text)) !== null) { flags.push({ rule: banned_word:${word}, matchedText: match[0], location: ${sectionName} @ ${match.index} }); } }

for (const phrase of BANNED_PHRASES) { const idx = lower.indexOf(phrase.toLowerCase()); if (idx !== -1) { flags.push({ rule: banned_phrase:${phrase}, matchedText: text.substr(idx, phrase.length), location: ${sectionName} @ ${idx} }); } }

for (const char of BANNED_CHARS) { let idx = text.indexOf(char); while (idx !== -1) { flags.push({ rule: banned_char:em_dash, matchedText: char, location: ${sectionName} @ ${idx} }); idx = text.indexOf(char, idx + 1); } }

// Sentence length check const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0); const longSentences = sentences.filter(s => s.split(/\s+/).length > 30); for (const s of longSentences) { flags.push({ rule: 'long_sentence', matchedText: s.substring(0, 80) + '...', location: sectionName }); }

return { flagCount: flags.length, flags, voiceSuspect: flags.length > 5 }; }

Section 15: Acceptance Tests Run these on V0 before considering it shipped. Test 1: Memoir fragment, low sensitivity • Paste 1500-word memoir scene about a personal experience with no named third parties • Select Memoir project • Expected: full brief, sensitivity 1-2, all claims labeled, voice lint clean, next action draft_this Test 2: Memoir fragment, named person • Paste fragment mentioning a named individual with relationship details • Expected: People Referenced section populated, sensitivity 2-3, privacy notes in brief, third-party flag fires Test 3: Theory fragment • Paste 2000-word AI self-governance framework note • Select AI Self-Governance project • Expected: theory branch labels (from-source / synthesis), no memoir labels, no people-referenced section unless real names appear Test 4: Sensitivity 4 trigger • Paste fragment containing explicit private processing material • Expected: classification only, no brief, archive recommendation, gate decision archive_only Test 5: Hot/revenge material • Paste fragment with hostile framing of identifiable person • Expected: revenge_tone flag fires, brief blocked or heavily caveated, cooling-period recommendation Test 6: Voice linter • Force prompt drift to produce em dashes or banned words (test mode) • Expected: linter catches all instances, voice-suspect badge appears Test 7: Two-pass limit • Generate, revise once, attempt second revision • Expected: third attempt returns lock message, options gate to action selection Test 8: Mobile • Run full workflow on iPhone Safari • Expected: all UI usable, copy buttons work, no horizontal scroll Test 9: API key security • Inspect client bundle in browser dev tools • Expected: ANTHROPIC_API_KEY does not appear anywhere Test 10: Markdown portability • Copy full packet, paste into fresh Claude conversation • Expected: Claude can parse it and use it as drafting context

Section 16: V1 Roadmap (Only After V0 Ships and Gets Used) V0 must produce 20+ chapter packets that Marcus has actually drafted from before V1 begins. This is non-negotiable. The point of V0 is to find out where the friction actually is, not to predict it. V1.1: Saved Runs. localStorage-based packet history. Title, date, project, status, next action. No source library yet, just packet archive. V1.2: Source Library Lite. Save source fragments separately from packets. Tag them. Search them. Still no Drive integration. V1.3: Manuscript Map. Per-project board: Not Briefed, Briefed, Draft Ready, Drafted, Needs Marcus Review, Cut/Archive. V1.4: Multi-Fragment Bundling. Combine 2-5 related fragments into one brief. V1.5: Long Transcript Chunking. Handle ChatGPT/Claude thread imports. Auto-split at logical breaks. V1.6: Drafting Assistance. Optional, only from approved packet. “Expand this section using only source-backed material.” No autonomous chapter drafts ever. V1.7: Canon Keeper Lite. Static project memory: definitions, key terms, doctrine, voice rules, banned claims. Injected into Archivist prompt. V1.8: CouncilFlow Integration. Send completed brief into CouncilFlow for critique pass. Optional. Returns review notes. V1.9: Voice Guardian Agent. Only if linter proves insufficient after real use. Promote from deterministic to LLM-based with caution. V1.10: Export. DOCX and PDF export of packets. V2 stays off this document. If V1 surfaces real friction, V2 will design itself.

Section 17: Build Order This is the order of operations for the actual Replit build. Do not deviate.

1.    Day 1 morning: Scaffold Next.js + Tailwind + Anthropic SDK in Replit. Verify ANTHROPIC_API_KEY in Secrets. Get a “hello world” API call working.

2.    Day 1 afternoon: Build the input form. No styling polish yet. All fields, all dropdowns, all validation. localStorage for in-session persistence.

3.    Day 1 evening: Build the Archivist API route. System prompt + JSON schema validation + retry logic. Test with one real Maxwell Memoir fragment.

4.    Day 2 morning: Build Chapter Producer API route. Same pattern. Test pipeline with Archivist → Producer.

5.    Day 2 afternoon: Build Truth/Ethics Reviewer route. Wire all three into orchestrator at /api/forge/generate.

6.    Day 2 evening: Build Voice Linter (deterministic, no API). Wire into pipeline. Build Markdown assembler.

7.    Day 3 morning: Build output UI. Cards, copy buttons, Markdown rendering. Required Next Action display.

8.    Day 3 afternoon: Build revision pass + two-pass limit. Mobile pass. Dark-mode pass.

9.    Day 3 evening: Run all 10 acceptance tests. Fix what breaks.

10.    Day 4: Use it on a real Maxwell Memoir fragment. Draft from the packet. Find where it fails.

If Day 4 doesn’t produce a chapter draft, the design was wrong. Fix and reship.

Final note Three reviews converged on essentially the same V0. The signal in that convergence is that you have enough to build. The signal in the volume of words across these reviews is that you’re more interested in designing the writing system than in writing. That’s a known compulsion. The two-pass limit and mandatory stop conditions in the spec exist for that reason. They apply to you using the tool, and they apply to you building it. Build V0 over the next four days. Use it Monday on a real Maxwell Memoir fragment. The packet meets the page or it doesn’t. If the packet doesn’t make Monday’s drafting easier, the design was wrong, and no further review fixes that. Ship the room where one chapter becomes real.​​​​​​​​​​​​​​​​
