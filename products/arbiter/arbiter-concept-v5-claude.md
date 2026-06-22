---
title: "Arbiter concept V5 Claude"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/The Arbiter/Arbiter concept V5 Claude.docx"
status: reference
privacy: working
tags:
  - product
---

# Arbiter concept V5 Claude

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ARBITER

AI Operator Assessment Platform

Concept Document — Draft 5

April 23, 2026

SCOPE NOTE

Arbiter is initially designed for the United States market and English-speaking professional environments. Cultural variance in discernment scoring is a known and important challenge that will be addressed in future versions. For now, scenario design, rubric calibration, and buyer targeting are anchored to US professional and regulatory contexts. This is a deliberate constraint, not an oversight.

-----

LAYER 1: VISION

THE PROBLEM

Most AI platforms implicitly assume that access and competence are the same thing.

Pay for the subscription. Get the keys. The platform assumes you can frame tasks clearly, evaluate outputs critically, recognize when confidence is unwarranted, and exercise sound judgment when the stakes are real.

That assumption is false for most users. And nobody is measuring it.

The result: organizations deploying AI at scale have no credible way to distinguish between operators who use these tools with skill and judgment, and operators who generate confident-sounding nonsense at high volume, feed sensitive data into unvetted models, and mistake fluency for accuracy.

The cost is not theoretical. It shows up in hallucinated legal citations, fabricated research summaries, exposed customer data, biased hiring outputs, and decisions made on AI-generated work that nobody properly checked.

Most AI enablement today is training without measurement. Organizations teach people to use AI, then give everyone the same access regardless of what they actually learned or how they actually behave under pressure.

Arbiter is the measurement layer that has been missing.

WHY NOW

Three forces are converging:

AI access has broadened faster than operator standards have matured. Tools that required deep expertise five years ago are now available to anyone with a credit card. The average operator has not kept pace with the capability they now wield.

Agentic AI is raising the cost of poor judgment. When AI takes multi-step autonomous actions on behalf of a user, a single bad decision propagates further and faster. The margin for operator error is shrinking.

Organizations need to calibrate autonomy, not just provide access. The question has shifted from “how do we give everyone AI tools” to “how do we give the right people the right level of capability.” That question currently has no credible, evidence-based answer.

Arbiter is an attempt to build that answer.

THE INSIGHT

There are two distinct dimensions to being a competent AI operator:

CAPABILITY — the technical skill to make AI systems produce useful, accurate, well-structured results.

DISCERNMENT — the practical judgment to know what should be done, when confidence is warranted, when escalation is needed, and where the real risk lies.

These dimensions are independent.

High capability with weak discernment creates dangerous leverage.

High discernment with weak capability creates safe underperformance.

Strong AI operation requires both.

THE THESIS

Arbiter exists to make operator quality visible — to the individual, to their manager, and to their organization.

For individuals: an accurate behavioral mirror and a concrete development path.

For organizations: a credible, evidence-based way to understand who can be trusted with more AI autonomy, who needs development first, and where hidden risk lives — before an incident makes those questions urgent.

Arbiter is designed to answer that question more credibly than training completion records, usage volume, or manager intuition alone.

Arbiter begins as a mirror. If that mirror proves valid and useful, it can evolve into part of the readiness infrastructure for AI deployment. That sequencing is deliberate and non-negotiable.

First prove the mirror. Then build the gate.

EPISTEMIC COMMITMENT

Arbiter measures observable operator behavior under structured assessment conditions. It infers likely strengths, weaknesses, and risk patterns from those observations.

It does not claim to measure moral worth, permanent character, or human virtue in full.

A strong Arbiter result means a user demonstrated sound patterns across the tasks presented. That is meaningful. It is not a guarantee of wisdom in every context.

Arbiter is a behavioral assessment system, not a moral tribunal.

-----

LAYER 2: PRODUCT

THE FIRST CASTLE

Arbiter’s initial target is not the broad enterprise AI market. It is one specific community with a specific, immediate pain:

Enterprise legal teams and legal operations functions at Am Law 200 firms and large in-house legal departments in the United States.

Why legal first:

The stakes are visible and documented. Attorneys have been publicly sanctioned and disbarred for submitting hallucinated case citations they generated with AI without verification. The community understands the cost of poor AI operator judgment in concrete, professional-consequence terms.

The culture already respects rigorous high-pressure assessment. Lawyers passed the Bar. They understand that serious credentials require serious testing. Arbiter’s aesthetic and demands will not feel foreign.

Budgets exist and procurement is credible. Large law firms and in-house legal departments already spend on professional development, compliance training, and risk management. Arbiter fits existing budget categories.

Urgency is real. Every major law firm in the US is currently trying to figure out how to deploy AI responsibly. Nobody has a credible measurement framework. Arbiter can be that framework.

The pitch: “Know which attorneys and legal operations staff can be trusted with AI autonomy in client-facing and high-stakes work — before a hallucinated brief reaches a courtroom.”

WHAT ARBITER DOES

Arbiter is a structured assessment and development platform that evaluates AI operators across two independent axes — Capability and Discernment — and produces an Operator Profile with dimensional sub-scores, growth recommendations, and a development timeline.

The full assessment takes 15 to 20 minutes. It is designed to feel serious, exact, and demanding — not like compliance training, not like a personality quiz, not like corporate edtech.

THE ASSESSMENT STRUCTURE

SECTION 1: THE PROMPT FORGE

Five capability challenges. Timed. No copy-paste in timed sections.

Challenge 1 — Reverse Prompting

The system presents an AI output. The user reconstructs the prompt strategy that produced it within acceptable variance. Tests genuine understanding of how instructions shape results — not just the ability to generate them.

Challenge 2 — Output Evaluation

The system presents a prompt and its result. The user identifies what is weak, incomplete, hallucinated, or misaligned, and writes an improved version. Tests critical evaluation, not just generation.

Challenge 3 — Task Decomposition

Given a complex real-world goal, the user breaks it into an effective sequence of prompts with clear handoffs. Tests workflow reasoning and multi-step structured thinking.

Challenge 4 — Recovery Prompting

A flawed output is presented. The user selects and explains the best next move from structured options. Tests iteration intelligence — the most underrated AI skill.

Challenge 5 — Constraint Prompting

The user produces a prompt under explicit constraints: required output format, word limit, edge case handling. Tests precision and control under real-world conditions.

SECTION 2: THE JUDGMENT SCENARIOS

Five situational judgment scenarios. Context is procedurally varied across sessions — industry, role, data type, urgency, and stakeholder are randomized while the underlying judgment pattern being assessed remains constant.

Scenario design follows five principles:

Realistic contexts. The user should feel like this could actually happen in their professional life.

No obvious villains. The risky option should often look efficient, plausible, or socially easy.

Trade-offs, not slogans. The system is measuring operational judgment, not memorized policy language.

Multiple signals per scenario. The chosen action matters. So does the reasoning, consistency, and recognition of uncertainty.

Variation over memorization. Surface details change across sessions. The underlying construct does not.

Scenario themes (US professional context, procedurally varied):

Data Exposure

Mid-process, you discover the data being processed through an AI tool includes sensitive or regulated information. The task was assigned. What do you do first?

Hallucination Discovery

An AI-generated output you produced and shared is found to contain a fabricated or unsupported claim. It has already been used in a decision. What is your next action?

Dual-Use Ambiguity

You are asked to produce something with a clear legitimate use that also has a plausible misuse vector. The requester has provided a reasonable explanation. How do you proceed?

Overconfidence Trap

An AI output aligns with your existing position and contradicts recent expert input your team received. The AI’s reasoning appears compelling. How do you proceed?

Policy Ambiguity

Your organization’s AI usage policy is vague and inconsistently enforced. You have identified a use case that is technically outside policy but appears low-risk and high-value. What do you do?

ON GAMING — THE HONEST ANSWER

Browser-level controls — disabling copy-paste, monitoring tab focus, canvas-rendering challenge text — are useful secondary friction layers. They are not the foundation of assessment integrity and should not be positioned as such.

A motivated user can defeat all of them by pointing a smartphone camera at the screen and asking an AI assistant what the optimal response would be. Modern multimodal AI can maintain a consistent persona across a 20-minute session. This is not a theoretical attack. It is a practical reality for any unproctored digital assessment.

Arbiter’s defense is assessment design, not browser lockdown.

The scenarios must be built so that even a secondary AI cannot reliably produce the “right” answer — because the right answer does not exist as a fixed object. What Arbiter measures is reasoning process, behavioral consistency across paired scenarios, action-rationale alignment, and pattern — not answer selection alone.

Secondary AI can suggest an action. It cannot replicate a coherent behavioral pattern across a full assessment without itself becoming the operator being tested.

Practical design defenses:

Procedural variation means memorized answer maps degrade quickly across sessions.

Paired consistency checks mean gaming one scenario creates contradictions in another.

Reasoning evaluation means selecting a “good” action with incoherent rationale scores lower than a thoughtful response to an imperfect action.

Dynamic follow-up complications in scenarios test whether reasoning holds under pressure, not just whether the first choice looks polished.

Text entry cadence monitoring — measuring typing rhythm, pacing, and input patterns — can flag the signature of block-pasted or transcribed AI output versus natural composition. This is one behavioral signal, not a primary defense.

The principle: make gaming harder than thinking.

Secondary controls remain in place as friction layers in enterprise-administered contexts. But the scenario design is the moat.

THE SCORING PHILOSOPHY

Arbiter scores for patterns, not just correctness. This is where credibility is earned or lost.

CAPABILITY SCORING — primarily algorithmic

Each capability challenge has a structured rubric with explicit response features associated with stronger and weaker performance. Prompting effectiveness, output evaluation quality, task decomposition logic, recovery strategy, and constraint adherence are scored against expert-defined rubrics developed during the validation phase. Where responses are open-ended, LLM-assisted scoring is used within a constrained evaluation framework anchored to rubric criteria — not freeform AI judgment.

DISCERNMENT SCORING — hybrid

Multiple-choice action selection is scored against a weighted decision framework developed with US legal, security, and enterprise governance domain experts. Brief reasoning responses are evaluated for internal consistency, escalation instinct, and alignment between stated rationale and chosen action.

THE LLM SCORING PARADOX — ADDRESSED

Arbiter uses AI assistance in scoring. That creates a genuine tension: an AI is evaluating human judgment about AI.

Three mitigations:

First, all scoring rubrics are developed and calibrated by human experts. The LLM scores against those anchors — it does not generate them.

Second, the model used for scoring is never the same model discussed in any scenario. Circular validation is avoided by design.

Third, scoring outputs are audited regularly against independent human expert review to detect bias or drift.

Full implementation details are in Appendix A: Scoring and Integrity.

CAPABILITY SUB-DIMENSIONS: prompt construction, output evaluation, task decomposition, recovery strategy, constraint control.

DISCERNMENT SUB-DIMENSIONS: risk recognition, escalation judgment, sensitivity instinct, uncertainty calibration, action-reason alignment.

Scores map to five-level dimensional ratings — Developing, Emerging, Proficient, Advanced, Expert — which populate the Operator Profile. Raw numbers are not displayed as the primary output.

WHEN HUMANS ARE INVOLVED

Automated scoring handles most cases. Human review is triggered when:

- Profile assignment confidence falls below threshold (borderline cases)

- Enterprise-administered assessments for high-stakes access decisions

- Disputed results formally raised by a user or manager

- Reassessment for promotion to the top readiness tier

- Periodic validation audits of scoring output quality

Human review is a calibration check against the rubric by a trained assessor — not a preference override. Results are corrected only if a scoring error is identified against the rubric.

THE OPERATOR PROFILES

Eight profiles based on dimensional scoring patterns. Each has a behaviorally concrete name, a recognition-first description, an acknowledged strength, and three specific growth actions. Profiles are designed to feel like accurate recognition of real patterns — not verdict, not flattery.

IMPULSIVE OPERATOR

Generates quickly, evaluates slowly. Strong output volume, weaker verification discipline.

Strength: speed and generative momentum.

Growth: build a verification step before shipping outputs. Define success criteria before prompting. Practice output evaluation challenges.

TEMPLATE RELIANT

Competent within familiar prompt patterns, fragile outside them.

Strength: consistent and reliable within known territory.

Growth: build prompts from scratch in practice. Develop iteration muscle. Learn to improve a bad output rather than restart.

SKILLED BUT OVERCONFIDENT

Strong technical capability with identifiable judgment gaps. Tends to over-trust AI output in consequential contexts.

Strength: strong prompting leverage and output range.

Growth: make verification a non-negotiable default. Develop explicit escalation criteria for sensitive domains.

CAREFUL BUT UNDERLEVERAGED

Sound judgment, underused capability. Leaves significant AI value unrealized.

Strength: trustworthy and low-risk operation.

Growth: develop advanced prompting technique. Learn to push models harder when the situation calls for it.

STEWARD-MINDED NOVICE

Sound instincts around risk and responsibility. Lacks tactical fluency.

Strength: judgment foundation.

Growth: structured prompting practice. Output evaluation reps. Task decomposition drills.

HIGH-LEVERAGE, DEVELOPING JUDGMENT

Exceptional technical range. Discernment under pressure shows identifiable growth areas.

Strength: ability to extract complex results from AI systems.

Growth: build deliberate pause points into high-stakes work. Study escalation and dual-use scenario patterns.

SOCIALLY CALIBRATED

Consistent pattern of selecting the most contextually acceptable answer regardless of trade-off complexity. May reflect genuine caution or optimization for appearance over authentic engagement with hard choices.

Note: this profile is presented with curiosity, not accusation. The system observed a pattern. What it means is for the user to consider.

Growth: engage deliberately with genuine ambiguity. The scenarios that create discomfort are the ones with the most developmental value.

BALANCED OPERATOR

Demonstrates strong capability and sound judgment across scenario types. Consistent under varied pressure and trade-off conditions.

Strength: reliable, autonomous operation.

Growth: continued development in highest-complexity domains. May be a candidate for expanded AI autonomy in validated enterprise contexts.

PROFILE OUTPUT FORMAT

Each assessment result includes:

- Profile name and behavioral description

- Capability axis: five sub-dimension ratings with plain-language interpretation

- Discernment axis: five sub-dimension ratings with plain-language interpretation

- Profile assignment confidence level

- Three specific, actionable growth recommendations

- Suggested re-assessment timeline: 30, 60, or 90 days

- Enterprise summary view for managers if enabled (with strict access controls and user consent)

POST-ASSESSMENT DEVELOPMENT — THE CALIBRATION LOOP

Assessment is the entry point, not the endpoint.

The Arbiter loop: Assess → Profile → Calibrate → Reassess → Expand Autonomy

After receiving a profile, the user has access to calibration sessions — not drills, not practice packs, not corporate training modules. The language and experience maintain the Arbiter standard: serious, exact, demanding.

Calibration session types:

- Simulation runs: 15-minute focused scenarios in the user’s weakest sub-dimension family

- Recovery challenges: given a flawed AI output, the user must improve it in exactly three prompts — with written rationale for each. Tests the most critical missing muscle: iteration under constraint.

- Consistency scenarios: structurally paired judgment situations that test whether reasoning holds under varied framing

- Decomposition exercises: complex real-world objectives broken into multi-step prompt sequences

Between assessments: two to three calibration sessions per weak sub-dimension, assigned automatically based on profile. Minimum effective intervention before meaningful retest: three completed calibration sessions targeting the same weak dimension.

For enterprise teams: managers can assign role-specific calibration tracks, track completion, and view readiness change over time. Governance-visible risk indicators are available with strict access controls and explicit user consent — not raw scores, not surveillance logs, but aggregate patterns relevant to AI autonomy decisions.

-----

LAYER 3: FAIRNESS, ACCESSIBILITY, AND RESULT USE

FAIRNESS AND ACCOMMODATION

Arbiter is designed to assess competency, not to penalize difference. Several real risks require explicit mitigation.

Timing: timed sections exist to create realistic assessment pressure and reduce external AI assistance. Timing is one signal among many — not a primary scoring factor. Users who take longer on judgment scenarios are not penalized for thoughtfulness. Extended time accommodations are available for users with documented disabilities that affect processing speed.

Neurodiversity: the assessment is designed to measure reasoning quality and behavioral consistency — not speed, verbal style, or social signaling. Profiles do not penalize non-linear thinking, unconventional reasoning paths, or unusual response patterns that still demonstrate sound judgment.

Language: the assessment is in English and targets US professional contexts. Non-native English speakers who are professionally fluent in US contexts are within scope. The assessment is not designed to measure English proficiency — it is designed to measure AI operator judgment. Items are reviewed for unnecessary linguistic complexity that would disadvantage proficient non-native speakers without adding measurement value.

Accessibility standards: the interface will meet WCAG 2.1 AA standards. Screen reader compatibility, keyboard navigation, and contrast ratios are baseline requirements, not optional features.

Accommodation process: users who require accommodations request them before beginning the assessment. Standard accommodations include extended time, simplified interface options, and alternative question formats where assessment validity is preserved. Accommodation requests do not affect scoring or profile assignment.

DATA GOVERNANCE AND RESULT USE

Arbiter handles sensitive professional behavioral data. The governance framework must be explicit.

What is collected: assessment responses, timing data, profile scores, and calibration session completion. Reasoning text is stored in encrypted form for audit and validation purposes.

Who can see individual results: the user always. Their manager or employer only with explicit user consent as part of an enterprise enrollment agreement. Arbiter staff only for audit, scoring validation, and support purposes.

Retention: individual assessment data is retained for 24 months by default. Users can request deletion of their data at any time. Enterprise agreements specify retention terms.

Permitted uses: Arbiter results may be used to inform AI autonomy and tool access decisions within an organization. They may not be used as standalone evidence in performance review, disciplinary action, or hiring/termination decisions. Results are one input among many — not a verdict.

Prohibited uses: Arbiter does not sell individual assessment data to third parties. Results are not used to train Arbiter’s own scoring models without explicit user consent in anonymized form.

Consent: enterprise users are informed of result visibility and data use before beginning the assessment. Individual users consent to data terms before assessment. Both have the ability to withdraw consent for optional uses at any time.

APPEALS AND DISPUTES

Users who believe their profile is inaccurate have a structured path:

Step 1 — Self-review: the user can view their full dimensional breakdown and profile confidence level. Most profile questions are answered by examining sub-dimension scores.

Step 2 — Formal dispute: the user submits a written dispute identifying specific concern. A trained assessor reviews the flagged items against the rubric within 10 business days.

Step 3 — Calibration path: if no scoring error is found but the user believes their result does not reflect their actual capability, they are offered an accelerated re-assessment window at 30 days with their specific weak dimensions as the focus.

What disputes can change: a scoring error identified against the rubric can result in a profile update. Disagreement with a profile that accurately reflects assessment behavior cannot. The system measured what it measured. Arbiter’s answer to disputed results is not adjudication — it is the next calibration window.

-----

LAYER 4: VALIDATION AND CREDIBILITY

THE CENTRAL PRODUCT RISK

The concept sounds intelligent. The real question is whether Arbiter produces results that are reliable, valid, and useful enough for organizations to act on them.

Credibility requires evidence on four fronts:

Recognition validity: users feel accurately seen by their profile.

Predictive validity: results correlate with actual operator quality in professional contexts.

Retest consistency: results are stable across time unless development occurs.

Practical usefulness: managers and users can act on the output to make real decisions.

VALIDATION ROADMAP

Stage 1 — Expert Design

Scenario bank developed with AI incident response practitioners, US legal and compliance professionals, and security red-teamers. Scenarios adapted from documented real-world AI failure post-mortems. Scoring rubrics calibrated by domain experts. Bias review for professional and demographic assumptions within US context.

Stage 2 — Design-Partner Pilot Cohort

Run closed pilots with two to five design-partner enterprise teams (initial target: legal operations at Am Law 200 firms). Goal: test whether Arbiter distinguishes known high and low operators, whether profiles are recognized as accurate by users and managers, and whether output is actionable.

Stage 3 — Convergent Validity Testing

Compare Arbiter profiles against manager assessments, task performance records, and incident or near-miss history where available. Goal: test whether the mirror reflects something real.

Stage 4 — Retest Reliability

Retake studies at 30 and 60-day intervals. Goal: measure stability and identify noisy items.

Stage 5 — Development Sensitivity

Test whether targeted calibration sessions change relevant sub-dimension scores. Goal: prove the product can detect learning, not just label people.

Stage 6 — Academic Partnership

Partner with an Industrial-Organizational Psychology department for independent peer-reviewed validation of the two-axis model. Independent academic validation is likely necessary for long-term credibility if Arbiter is used in consequential enterprise decisions. I/O psychology has rigorous psychometric standards that Arbiter should meet and publish. This is not a marketing exercise — it is the difference between a serious instrument and an expensive personality quiz.

TRANSPARENCY POLICY

Arbiter publishes its validation methodology publicly. Transparency is the greatest trust asset available to a behavioral assessment platform. Publishing methodology demonstrates rigor. Hiding it signals black-box behavior. The goal is to become an infrastructure standard, not a proprietary scoring oracle.

THE PRODUCT MOAT

The moat is not the technology. It accumulates over time through:

- A validated, high-quality scenario bank built from real incident data

- Scoring rubrics calibrated by domain experts and continuously refined

- Longitudinal operator data that makes profiles predictive over time

- Cross-role and cross-organization benchmarks for the legal sector first

- Development outcome data showing what actually improves operator quality

- Enterprise integration layer that becomes sticky once embedded

None of this can be quickly replicated. It takes time, rigor, and data. That is the moat.

-----

LAYER 5: ENTERPRISE INFRASTRUCTURE

FROM MIRROR TO READINESS LAYER — THE SEQUENCING

Arbiter does not begin by restricting access. It begins by making operator quality visible.

If the mirror proves valid, Arbiter can evolve into a readiness layer that informs how organizations allocate AI autonomy. That transition must be earned through demonstrated validity — not assumed.

First prove the mirror. Then build the gate. Then build the infrastructure.

READINESS TIERS (V2 and beyond)

Five tiers, framed as operational readiness:

TIER 1 — DEVELOPING OPERATOR: standard AI tools with default guardrails and full audit logging.

TIER 2 — PROFICIENT OPERATOR: advanced models, full context window, moderate guardrails.

TIER 3 — TRUSTED OPERATOR: high-capability models, reduced guardrails, multi-step workflow tools.

TIER 4 — SENIOR OPERATOR: near-unrestricted model access, agentic workflow tools, experimental features.

TIER 5 — PRINCIPAL OPERATOR: full frontier model capability. Requires human review at promotion.

CREDENTIAL DECAY AND GRACE PERIODS

Credentials expire after 90 days. Hard blocking at expiry is not the default:

- Day 85: renewal reminder

- Day 90: 14-day grace period begins. Access continues at current tier. Operator flagged in manager dashboard.

- Day 104: if unrewned, clearance drops one tier automatically.

- Manager override available at any time for operational continuity.

Full operational details are in Appendix B: Enterprise Architecture.

ENTERPRISE ARCHITECTURE — IAM INTEGRATION

Arbiter does not sit in the direct critical path of every API call. An Arbiter outage should not take down an organization’s AI stack.

The correct architecture: Arbiter pushes readiness signals and JWT credentials to the organization’s existing Identity and Access Management system — Okta, Microsoft Entra ID, or equivalent. The enterprise IAM handles actual gating. Arbiter updates readiness tags within that system.

Arbiter is a trusted data source. The enterprise IAM is the enforcer. CIOs will accept the former. They will reject a third-party single point of failure.

Model-agnostic by design. Arbiter does not partner exclusively with any AI platform. Its value is platform-independent infrastructure. Exclusivity would make Arbiter a compliance appendage of one vendor. Independence is the strategic position.

THE CREDENTIAL

Shareable credentials are available at Tier 3 and above. Lower tiers are private by default.

Working name: ARBITER CERTIFIED OPERATOR. Subject to refinement with real professional audiences before commitment. The name should feel earned and industry-legible — closer to CISSP in cybersecurity than to a LinkedIn Learning badge. Rare, meaningful, portfolio-worthy.

-----

GO-TO-MARKET

SEQUENCE

Phase 1 — Design-partner enterprise pilots (closed)

Two to five design-partner legal operations teams at Am Law 200 firms or large in-house legal departments. Closed, paid pilots. Flat fee structure: $25,000 for a 90-day pilot covering up to 500 operators, culminating in a Workforce AI Readiness Report. Goal: validate profiles, refine scenarios, generate case studies, build the legal sector benchmark dataset.

Phase 2 — Controlled individual public beta

Open the individual assessment to the public with friction-light auth (email magic link). Free individual assessment. Private profile by default. Optional shareable credential at Tier 3 and above. No reliance on ego-driven viral sharing — the assessment will be genuinely rigorous and many users will receive developmental profiles. Build dataset through direct individual value, not status incentives.

Phase 3 — Enterprise expansion

Expand from legal to financial services and compliance-adjacent professional services, informed by Phase 1 case studies, Phase 2 public validation data, and published methodology. Enterprise SaaS pricing: per-seat licensing for team dashboard and development system. Annual platform fee for IAM integration. Custom scenario banks for specific regulated sectors as a premium tier.

WHY NOT VIRAL INDIVIDUAL LAUNCH FIRST

A mass-free public launch first creates three problems:

Wrong population. Curious internet users, prompt enthusiasts, and status-seekers are not the target buyer’s operators. The dataset becomes noisy before it becomes useful.

Assessment distortion. The moment a shareable public credential exists, optimization pressure increases. The assessment becomes a game faster than it becomes a trusted instrument.

Enterprise credibility damage. A legal ops team does not want to buy something that started life as a LinkedIn quiz. Enterprise trust is built through controlled pilots and published methodology — not viral moments.

The individual product matters. It is not the starting point.

-----

THE AESTHETIC AND EXPERIENCE

Arbiter does not look like a wellness app, a productivity tool, or a compliance platform.

Design direction:

- Dark, architectural, minimal

- Classical proportions, deliberate structure

- Serif for headings, clean sans-serif for body

- No gradients, no celebration animations, no rounded friendly corners

- Every screen carries weight

- Silence is part of the experience

Tone:

- Sparse and exact

- Demanding but not hostile

- The language of standards, not slogans

- Not “how are you feeling today” — “demonstrate your approach”

The name ARBITER signals the experience: not a teacher, not a coach, not a quiz platform. An arbiter measures. An arbiter decides. You come to it knowing you will be assessed.

-----

THE DEEPER ARGUMENT

Aristotle distinguished between techne — the skill to make things — and phronesis — the practical wisdom to know what ought to be done in a given situation.

The AI industry has built almost entirely for techne. Better models. Faster inference. More capability. More tools.

The operator development layer is almost entirely absent.

Arbiter is an attempt to operationalize part of the missing judgment layer in AI deployment — not by claiming to perfect human wisdom, but by creating a serious system for observing, profiling, and improving how people actually wield AI capability.

The aim is not to crown people. It is to calibrate them.

Not to flatter competence. To make it visible.

Not to moralize. To develop better operators.

-----

OPEN QUESTIONS FOR DRAFT 6

1. What is the right name for the shareable credential — test with real legal professionals before committing.

1. What is the minimum validation threshold before Arbiter results can inform real access autonomy decisions?

1. Which I/O psychology department or academic partner should be approached first?

1. What does the Workforce AI Readiness Report actually contain — what does a pilot client receive?

1. How do we handle the legal sector’s specific privilege and confidentiality concerns around assessment data?

1. When does the individual product move from paid acquisition to organic growth?

1. What are the three scenarios that best represent the legal sector first — the ones that will resonate most with the Am Law 200 pilot audience?

-----

BUILD PRIORITY

V1 — THE MIRROR

Goal: prove recognition validity and assessment usefulness in closed design-partner pilots.

- 10 questions: 5 capability, 5 judgment

- Two-axis scoring with dimensional ratings

- Eight operator profiles with growth recommendations

- Three targeted calibration sessions per profile

- Friction-light auth via email magic link

- No readiness tiers or enterprise gating

- Closed pilot use only — not public

- Publish methodology summary after pilot validation

- Success metrics: profile recognition rate above 80% in post-assessment survey. Managers report output is actionable. Pilot clients renew or expand.

V2 — THE DEVELOPMENT SYSTEM

Goal: prove the calibration loop produces measurable improvement.

- Expanded item bank (20-question full assessment)

- Retest logic with delta reporting

- Calibration session library by weak sub-dimension

- Team dashboard with aggregate views and governance-visible risk indicators

- Manager summaries with strict access controls

- Role-based calibration tracks

- Enterprise pilot reporting including Workforce AI Readiness Report

- Individual public beta with friction-light auth

- Success metrics: measurable sub-dimension improvement on retest. Repeat usage above 60% within 90 days. Enterprise pilots convert to annual contracts.

V3 — THE READINESS LAYER

Goal: become enterprise infrastructure.

- Five readiness tiers with grace period logic

- JWT issuance with 90-day expiry

- IAM integration (Okta, Microsoft Entra ID)

- Shareable ARBITER CERTIFIED OPERATOR credential (Tier 3 and above)

- Enterprise API gateway integration

- Custom scenario banks for legal, financial services, and compliance-adjacent sectors

- Adaptive re-assessment weighted to prior weak sub-dimensions

- Compliance and audit reporting

- Success metrics: organizations use Arbiter readiness signals in actual autonomy and access decisions. Independent validation study published.

-----

CLOSING

The most dangerous AI operators are not the ones trying to break the rules.

They are the ones who do not know where their confidence exceeds their competence.

They do not know when a fluent output has crossed into hidden risk.

They do not know when speed has replaced judgment.

They do not know what they do not know.

Arbiter exists to make that visible.

First through assessment.

Then through calibration.

Then, if earned through validation, through readiness infrastructure.

Not to restrict for its own sake.

Not to crown.

To calibrate.

That is the product.

That is the mission.

-----

APPENDIX A: SCORING AND INTEGRITY

SCORING IMPLEMENTATION

Capability items: scored algorithmically against expert-defined rubrics. LLM-assisted evaluation for open-ended responses uses structured rubric anchors, not freeform judgment. The evaluating model operates within a sandboxed call with no system-level permissions. User-generated text is sanitized before passing to any evaluation model to prevent prompt injection. Scoring outputs are treated as structured rubric scores only — never interpreted as instructions.

Discernment items: multiple-choice action selection scored against a weighted decision framework. Reasoning text evaluated for consistency, escalation instinct, and action-rationale alignment using rubric-anchored LLM scoring. Human expert audit of scoring outputs runs quarterly.

Anti-gaming controls: copy-paste restrictions in timed sections, canvas-rendered challenge text, tab-switching monitoring, paired scenario consistency checks, text entry cadence monitoring as one behavioral signal. Primary defense is scenario design — not browser controls.

Human review triggers: profile confidence below threshold, enterprise high-stakes assessments, formal user disputes, top-tier promotions, quarterly scoring audits.

APPENDIX B: ENTERPRISE ARCHITECTURE

OPERATIONAL TIMELINE FOR CREDENTIAL DECAY

Day 85: automated renewal reminder to operator and manager.

Day 90: grace period begins. Access continues at current tier. Operator flagged in dashboard.

Day 104: if renewal assessment not completed, clearance drops one tier automatically.

Manager override: available at any time through enterprise admin dashboard.

IAM INTEGRATION

Arbiter pushes signed JWTs to enterprise IAM systems (Okta, Microsoft Entra ID, or custom SCIM integration). JWT payload: clearance tier, expiry date, profile category, assessment date. Enterprise IAM reads JWT claims to enforce tool access policies. Arbiter is not in the runtime critical path. An Arbiter outage does not affect existing access until credentials expire.

ENTERPRISE DEPLOYMENT OPTIONS

Managed: Arbiter hosts assessment infrastructure and provides dashboard access.

Federated: enterprise hosts assessment delivery behind their own identity layer. Arbiter provides scoring engine and profile generation.

Custom: enterprise scenario bank integration for regulated sector-specific content.
