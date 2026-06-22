---
title: "Marcus Symposium AI Self Study Build Ladder and Glossary"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Leveling up /Education /Marcus_Symposium_AI_Self_Study_Build_Ladder_and_Glossary.docx"
status: active
privacy: working
tags:
  - planning
---

# Marcus Symposium AI Self Study Build Ladder and Glossary

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Marcus / Symposium AI Self-Study Build Ladder

Projects, terminology, and theory map for becoming dangerous without becoming a course addict

Verdict on the $2,000 course
The syllabus is useful as a map, not proof that Marcus needs permission to start. The right move is to treat it as a reference syllabus and build the projects directly. Buy the course only if the cohort access, instructor feedback, or accountability clearly saves more than $2,000 worth of time or confusion. Do not buy it from anxiety or because the terminology feels intimidating.

Operating principle
Marcus does not need to become an ML researcher before acting. The target is operator-level literacy: enough theory to scope, build, evaluate, sell, govern, and teach AI-assisted systems without pretending magic is happening.

1. Executive Summary

The ByteByteGo-style course outline is a strong survey of modern AI engineering: LLM foundations, RAG, agents, deep research, multimodal generation, and a capstone. None of it is alien to the work Marcus is already doing with Anchor, Kairos, Claude, Codex, Replit, and the emerging Symposium Studios delivery model. The missing piece is not raw permission. The missing piece is structured terminology and a deliberate build ladder.

This document converts the course syllabus into a Marcus/Symposium self-study program. The goal is not to memorize every acronym. The goal is to build enough intuition that Marcus can recognize the moving parts, ask better questions, direct agents and human builders more precisely, and package AI-native delivery work for clients.

Build first, learn terms in context. Every term should connect to a working artifact, not stay as vocabulary soup.

Prefer production-ish demos over toy notebooks. Tiny demos are fine, but each project should eventually map to something Symposium could show or sell.

Do not over-index on model-training theory. Useful literacy, but the business lane is delivery, systems, RAG, agents, evaluation, and workflow governance.

Use Kairos as the live capstone. The NYC Tech Week Signal Map is a perfect proof artifact: messy data in, decision-ready schedule out.

2. Learning Posture: Operator Literacy, Not Researcher Cosplay

There are three levels of learning here:

Level

What it means

Marcus target

Vocabulary literacy

Know what a term refers to and why it matters.

Required for almost everything.

Builder literacy

Can implement a small working version or direct an agent/dev to implement it.

Required for RAG, agents, tool calling, evals, workflow systems.

Research literacy

Can train or modify frontier methods from scratch.

Optional. Useful context, not the current business core.

The main trap is confusing “I do not know every term yet” with “I am behind.” The real skill is building a bridge between business problems and working AI-assisted systems. The terms help that bridge become more precise.

3. The Symposium Self-Study Build Ladder

Stage

Project

Main skill built

Portfolio / business relevance

0

AI Lab Setup and Evaluation Harness

A repeatable place to run experiments, log outputs, and compare models.

Foundation for all Symposium demos and client work.

1

LLM Playground

Foundational literacy: tokens, sampling, model families, generation parameters.

Shows you understand what models are doing before you build on top of them.

2

Customer Support Chatbot with RAG

Retrieval, chunking, embeddings, context injection, faithfulness checks.

Direct SMB/client offer: support, ops, knowledge-base assistant.

3

Ask-the-Web Agent

Tool calling, search, routing, multi-step reasoning, citations.

Kairos, research assistants, sales/market research, founder intelligence.

4

Deep Research System

Reasoning models, verification, synthesis, report generation.

High-value operator deliverable: market maps, diligence, strategy memos.

5

Multimodal Generation Agent

Image/video generation pipeline literacy and creative tool orchestration.

Useful for Symposium creative/prototype side, less urgent than agents/RAG.

6

Capstone: Kairos / Agentic Workflow System

End-to-end product: messy inputs to scored recommendations to usable UI.

Public Tech Week proof artifact and direct template for client workflow systems.

Stage 0 - AI Lab Setup and Evaluation Harness

Before doing the projects, create a simple lab that makes experiments repeatable. This prevents every experiment from becoming a messy one-off chat thread.

Build steps:

One repo or workspace for AI experiments.

Model comparison harness: same prompt across GPT, Claude, Gemini, local models if relevant.

Logging: prompt, model, input data, output, cost, latency, notes.

Evaluation templates: accuracy, faithfulness, usefulness, style fit, failure modes.

A small dashboard or markdown report generator.

Terms this teaches:

Prompt/output logging, Model comparison, Evals, Cost/latency tracking, Regression tests for prompts

Output artifact:

A small internal “Symposium AI Lab” repo with example prompts, test cases, and output reports.

Stage 1 - Build an LLM Playground

Goal: build practical intuition for what an LLM is doing: how text becomes tokens, how generation choices change output, and what model families mean. Do not try to train a frontier model. Build a small playground that demystifies the basics.

Build steps:

Load a hosted LLM API and possibly a small local model.

Show tokenization visually: input text -> tokens -> token IDs.

Expose generation controls: temperature, top-k, top-p, max tokens, stop sequences.

Compare greedy, beam, top-k, and top-p sampling on the same prompt.

Add a “model family notes” panel for GPT, Claude, Gemini, DeepSeek, Qwen, Gemma.

Optional: tiny transformer notebook for architecture literacy.

Terms this teaches:

Tokenization, BPE, Transformers, Attention, Sampling, Greedy search, Beam search, Top-k, Top-p, SFT/RLHF overview

Output artifact:

A clean demo page called “LLM Playground” that helps non-technical founders understand why prompt and model settings matter.

Stage 2 - Build a Customer Support Chatbot with RAG

Goal: build the most commercially useful baseline AI system: a chatbot that answers from a company knowledge base instead of hallucinating from memory.

Build steps:

Ingest a small corpus: FAQs, SOPs, product docs, support tickets.

Parse documents and chunk them with several strategies.

Create embeddings and store chunks in a vector database or simple local index.

Retrieve relevant chunks for a user question.

Generate answer with citations and refusal behavior when context is missing.

Add eval set: context relevance, faithfulness, answer correctness.

Add admin panel to upload docs and test answers.

Terms this teaches:

RAG, Retrieval, Embeddings, Vector search, Chunking, ANN search, Faithfulness, Answer correctness, RAFT overview

Output artifact:

Direct client demo: “Give us your docs. We give you a support assistant with citations and review gates.”

Stage 3 - Build an Ask-the-Web Agent

Goal: build a Perplexity-like agent that searches the web, uses tools, cites sources, and can do multi-step information work without pretending it already knows the answer.

Build steps:

Add web search tool calling.

Add source extraction and citation handling.

Implement routing: simple question vs web-required question vs multi-step research.

Add parallel search: run multiple queries, compare results.

Add reflection/check pass: identify weak sources or missing angles.

Add simple UI for asking, refining, and exporting results.

Terms this teaches:

Agents, Tool calling, Tool formatting, Tool execution, Routing, Prompt chaining, Reflection, Orchestrator-worker, ReAct, MCP basics

Output artifact:

Core Kairos/market-research capability: “Ask the event/firehose/market what matters for this person.”

Stage 4 - Build Deep Research Capability

Goal: turn search + reasoning into long-form, verified synthesis. This is where AI becomes a research analyst, but with explicit verification and citations.

Build steps:

Use a reasoning model for planning and decomposition.

Generate multiple search plans and compare them.

Use a verifier pass to catch unsupported claims.

Require citations for factual claims.

Produce structured reports: executive summary, evidence, open questions, confidence levels.

Add human review gates before publishing or client delivery.

Terms this teaches:

Reasoning models, Inference-time scaling, CoT, Parallel sampling, Sequential sampling, Tree of Thoughts, Verifier, Self-refinement, ORM/PRM overview

Output artifact:

High-value deliverables: market maps, diligence memos, ICP research, role-language harvesting, Tech Week signal reports.

Stage 5 - Build a Multimodal Generation Agent

Goal: learn enough image/video generation terminology to direct creative and product prototypes without pretending to be a diffusion researcher.

Build steps:

Build a prompt-to-image workflow with a hosted model.

Add style references and brand constraints.

Generate multiple variants and score them against a brief.

Optional: simple image editing pipeline.

Optional: video generation exploration for creative prototypes.

Document what is hosted API vs what would require model training.

Terms this teaches:

VAE, GANs, Autoregressive models, Diffusion, Text-to-image, U-Net, DiT, Latent diffusion, CLIP score, FID overview

Output artifact:

Useful for Symposium creative tooling, pitch assets, visual prototypes, AI-native games, and Marcus Vale media.

Stage 6 - Capstone: Kairos or Agentic Workflow System

Goal: ship a public, portfolio-ready project that demonstrates the real Symposium method: messy inputs become structured data, AI enrichment, human-readable decisions, and a useful interface.

Build steps:

Use the NYC Tech Week ICS feed or another messy data source.

Parse and normalize events.

Enrich with categories, relevance scores, access requirements, alcohol/sober flags, location, conflicts.

Build searchable/filterable UI.

Add “Ask Kairos” assistant for schedule recommendations.

Add Marcus public route, but no real-time location or private meetings.

Write a case study: firehose -> signal map -> decision-ready schedule.

Terms this teaches:

End-to-end data pipeline, RAG/search, Agentic recommendation, Human-in-the-loop judgment, Evaluation, Product UI, Case study writing

Output artifact:

The strongest immediate proof artifact: live, useful, aligned with Tech Week, and legible as Symposium Studios work.

4. Recommended Sequence for the Next 30-60 Days

Order

Focus

Why now

1

Kairos / Tech Week Signal Map

Immediate public proof artifact and conversation opener.

2

RAG Support Chatbot

Most client-legible and closest to paid SMB/internal-tool work.

3

Ask-the-Web Agent

Strengthens research, sourcing, and Kairos-style intelligence.

4

Deep Research Capability

Turns research into high-value reports and strategy deliverables.

5

LLM Playground

Useful as teaching artifact, but not the urgent business wedge.

6

Multimodal Agent

Interesting and future-facing, but secondary to agentic delivery right now.

Buy vs build decision
At $2,000, the course is not crazy if it truly provides high-quality instruction, feedback, and cohort accountability. But for Marcus right now, $2,000 may be better spent on shipping proof artifacts, API/tooling budget, travel/event access, and targeted expert feedback. The recommended posture is: save the syllabus, build the ladder, and reconsider the course only if a specific gap remains after one or two projects.

5. Terminology Reference Glossary

This glossary is written for operator literacy. It does not try to be mathematically complete. Each term answers: what is it, why does it matter, and how should Marcus think about it?

LLM Foundations and Training

Term

Plain English

Marcus / Symposium relevance

LLM

Large Language Model. A model trained to predict and generate text-like token sequences.

The engine underneath chatbots, agents, and assistants. Marcus needs to know how to direct and evaluate them, not train frontier models from scratch.

Foundation model

A large general model trained on broad data before being adapted to specific tasks.

Think GPT, Claude, Gemini, Llama, Qwen, Gemma. Most products are built on top of these rather than training from zero.

Pre-training

The initial training phase where a model learns patterns from massive text/code/image data.

Important for theory, but not Marcus’s current build lane. He uses pre-trained models as power tools.

Data collection

Gathering raw data for model training or product knowledge bases.

For clients this usually means docs, support tickets, websites, CRMs, spreadsheets, and SOPs, not Common Crawl-scale training.

Common Crawl

A massive public web crawl often used as raw training data.

Useful to recognize in model-training discussions. Rarely something Marcus directly needs for client builds.

RefinedWeb / Dolma / FineWeb

Curated/cleaned large text datasets used in training or evaluating open models.

Useful dataset vocabulary. Not urgent unless doing model-training research.

Data cleaning

Removing junk, duplicates, unsafe content, broken formatting, and low-quality text.

Very relevant in RAG and client systems. Bad data in, garbage assistant out.

Tokenization

Breaking text into pieces called tokens that models process.

Explains why models count tokens, why weird text splits happen, and why context windows cost money.

BPE

Byte Pair Encoding. A common tokenization method that merges frequent character sequences.

Not something to obsess over, but useful for understanding token counts and model weirdness.

Neural network

A layered mathematical system that learns patterns from data.

Base concept. Operator-level understanding is enough.

Transformer

The architecture that made modern LLMs work well by using attention over sequences.

Core model architecture. Know the term, do not need to derive it.

Attention

Mechanism that lets a model weigh which tokens are relevant to other tokens.

Helps explain why context matters and why long-context recall can still fail.

GPT family

Generative Pre-trained Transformer models such as OpenAI GPT models.

One major family of LLMs used through APIs.

DeepSeek / Qwen / Gemma

Model families from different labs/companies, often available as open or semi-open models.

Good to know for model selection, local deployment, and cost/performance comparisons.

Text generation

The process of producing output tokens after a prompt.

The basic model behavior underneath chat, tools, and agents.

Greedy decoding

Always choosing the most likely next token.

Predictable but can be dull or brittle.

Beam search

Keeps several likely output paths and chooses among them.

Common in older NLP/generation tasks. Less central to chat UX than sampling controls.

Top-k sampling

Samples only from the k most likely next tokens.

A control for randomness/variety.

Top-p sampling

Samples from the smallest set of tokens whose probabilities add up to p.

Also called nucleus sampling. Controls diversity.

Temperature

Controls randomness in generation. Lower is more deterministic, higher is more varied.

Practical lever for product behavior. Use lower for factual/business output, higher for ideation.

SFT

Supervised Fine-Tuning. Training a model on examples of desired inputs and outputs.

How base models become more instruction-following. For Marcus: useful concept, but usually use APIs or light fine-tuning only when needed.

RLHF

Reinforcement Learning from Human Feedback. Training models to prefer outputs humans rate better.

Explains why chatbots become more helpful/safe. Not usually something Marcus implements directly.

Reward model

A model trained to score outputs according to preferences or correctness.

Important in RLHF and agent evals. In business terms: a scoring layer.

PPO

Proximal Policy Optimization. A reinforcement learning algorithm used in some RLHF systems.

Know the name. Not urgent unless going deep into model training.

Verifiable tasks

Tasks where correctness can be checked automatically, like math, code tests, or exact answers.

Very relevant to agentic delivery: use tests/verifiers wherever possible.

Benchmark

A standardized test set for comparing models.

Useful but limited. Real product evals matter more than leaderboard worship.

Human evaluation

Humans judge output quality, usefulness, safety, or fit.

Still essential for taste, client fit, and high-stakes outputs.

Prompting, Adaptation, and RAG

Term

Plain English

Marcus / Symposium relevance

Fine-tuning

Further training a model on specialized data.

Useful when prompts/RAG are insufficient, but adds complexity. Do not reach for it first.

PEFT

Parameter-Efficient Fine-Tuning. Fine-tuning a small subset of model parameters.

A cheaper/lighter way to adapt models. Mostly relevant if working with open models.

Adapters

Small trainable modules added to a model to specialize behavior.

A PEFT technique. Useful vocabulary, not urgent for hosted API workflows.

LoRA

Low-Rank Adaptation. A popular PEFT method that trains small low-rank matrices instead of the whole model.

Often used to adapt open models cheaply. Good to know, not a first move for most client systems.

Prompt engineering

Designing instructions, context, examples, and output formats to get better model behavior.

A real skill, but not enough by itself. It becomes powerful when paired with data, tools, and review gates.

Zero-shot prompting

Asking the model to do a task without examples.

Fast baseline.

Few-shot prompting

Including a few examples of desired behavior in the prompt.

Very useful for style, classification, extraction, and consistent formatting.

Chain-of-thought prompting

Prompting the model to reason step by step.

Can improve reasoning, but user-facing systems should often ask for concise answers and use hidden/internal reasoning patterns carefully.

Role-specific prompting

Giving the model a role such as support agent, analyst, CTO assistant, or scheduler.

Useful if it is paired with specific rules and context. Role alone is not enough.

User-context prompting

Injecting relevant user/company/project context into the model prompt.

This is Pattern Intimacy and product personalization. Powerful but needs privacy and scope control.

RAG

Retrieval-Augmented Generation. Search relevant external knowledge, then generate an answer using that context.

One of the most important commercial patterns. Lets AI answer from client docs instead of guessing.

Retrieval

Finding relevant documents, chunks, or records for a query.

The quality of retrieval often determines answer quality.

Document parsing

Extracting text/structure from PDFs, docs, websites, spreadsheets, or emails.

A real pain point in client systems. Bad parsing breaks RAG.

Chunking

Splitting documents into pieces small enough to retrieve and fit into context.

Chunk size and boundaries matter a lot. Bad chunking creates missing or misleading answers.

Indexing

Preparing data so it can be searched quickly.

Can be keyword, full-text, vector, knowledge graph, or hybrid.

Keyword search

Search based on exact words or terms.

Still useful. Do not assume vector search solves everything.

Full-text search

Search across full document text with ranking.

Strong baseline for many internal tools.

Knowledge-based indexing

Structuring information as entities, relationships, or knowledge graphs.

Useful for complex domains, but often overkill for V1.

Vector search

Search by semantic similarity using embeddings.

Core RAG pattern. Good for meaning-based retrieval.

Embedding model

A model that turns text into numeric vectors representing meaning.

The retrieval backbone for vector search.

Exact nearest neighbor

Finds the truly closest vectors, usually slower at scale.

Technical retrieval concept.

Approximate nearest neighbor (ANN)

Finds close-enough vectors faster for large indexes.

Common in vector databases.

RAFT

Retrieval-Augmented Fine-Tuning. Training models to use retrieved context better.

Advanced. Good to know, not V1 for most projects.

Context relevance

Whether retrieved chunks actually match the question.

Core RAG eval metric.

Faithfulness

Whether the answer sticks to the retrieved context and does not hallucinate.

Critical for client trust.

Answer correctness

Whether the final answer is actually right.

Needs tests, human review, or trusted references.

Agents and Agentic Systems

Term

Plain English

Marcus / Symposium relevance

Agent

A system where an LLM can plan or decide steps and use tools to accomplish a goal.

The word is overused. For Marcus, the value is practical: tool use, workflows, review gates, and useful autonomy.

Agentic system

A broader system with some agency: workflows, tools, routing, memory, planning, or multi-step execution.

Most real products are agentic systems, not fully autonomous agents.

Workflow

A structured sequence of steps, often deterministic or semi-deterministic.

Underrated. Reliable workflows beat free-roaming agents in many business settings.

Prompt chaining

Breaking work into multiple LLM calls where one output feeds the next.

Core pattern for controlled agentic systems.

Routing

Sending different inputs to different prompts, models, tools, or workflows.

Important for cost, quality, and safety.

Parallelization

Running multiple tasks or model calls at once.

Useful for search, brainstorming, classification, and comparison.

Voting

Using multiple outputs and selecting/combining the best.

Can improve reliability, especially with judging/verifier layers.

Reflection

A model reviews its own or another model’s output and suggests fixes.

Useful, but not magic. Needs concrete criteria.

Orchestrator-worker pattern

One controller delegates subtasks to specialized workers.

Very close to Marcus’s Director Model.

Tool calling

The model requests a tool/action such as search, database query, email draft, code execution, or API call.

Core agentic capability.

Tool formatting

The schema/rules that define how a model should call tools.

Bad schema design causes brittle systems.

Tool execution

Actually running the requested tool and feeding the result back to the model.

Needs permissions, error handling, and logs.

MCP

Model Context Protocol. A standard for connecting AI tools/models to external context and tools.

Important for agent/tool ecosystems. Think: a plug/socket standard for AI assistants and tools.

Planning autonomy

How much freedom the agent has to decide steps without human intervention.

Higher autonomy means higher need for review gates and constraints.

ReAct

Reason + Act pattern where a model alternates reasoning and tool use.

Classic agent pattern. Good mental model for tool-using agents.

Reflexion

Agent pattern where the system learns from feedback/reflection across attempts.

Useful concept for iterative improvement.

ReWOO

Reasoning Without Observation. Plans tool calls separately from executing/observing them.

Advanced agent architecture vocabulary.

Tree search for agents

Exploring multiple possible action paths and choosing the best.

Useful for difficult planning but can be expensive.

Multi-agent system

Multiple agents with different roles collaborating or debating.

Powerful but easy to overcomplicate. Use when roles genuinely help.

A2A

Agent-to-Agent protocol/communication. A way for agents from different systems to coordinate.

Emerging infrastructure idea. Important for future interoperability, not always needed in V1.

Agent evaluation

Testing whether agents accomplish tasks safely, correctly, and reliably.

One of Marcus’s moats. Speed without evals becomes garbage.

Reasoning and Deep Research

Term

Plain English

Marcus / Symposium relevance

Reasoning model

A model designed or tuned to spend more compute on reasoning before answering.

Useful for planning, code, math, research, and complex decomposition.

OpenAI o-family

OpenAI reasoning models built for harder reasoning tasks.

Useful when judgment and multi-step thinking matter more than raw speed.

DeepSeek-R1

A reasoning-focused model family known for open reasoning capability.

Important market/reference point.

Inference-time scaling

Spending more compute at answer time to improve reasoning quality.

Practical idea: harder tasks deserve more thinking passes.

Parallel sampling

Generate multiple answers/plans at once and choose or synthesize.

Good for research and strategy.

Sequential sampling

Generate, critique, revise, and continue in sequence.

Good for deep research and writing workflows.

Tree of Thoughts (ToT)

Explore a tree of reasoning paths rather than one linear answer.

Useful concept for complex planning; expensive if overused.

Verifier

A system or model that checks whether an answer/step is correct.

Key to agentic delivery. Tests, evals, and validators are verifiers.

Search against a verifier

Explore possible answers/plans and use a verifier to pick stronger ones.

Very relevant to coding agents and high-stakes research.

STaR

Self-Taught Reasoner. Training approach using generated rationales and refinement.

Research-level term. Good to know, not immediate client work.

ORM

Outcome Reward Model. Scores final answer quality.

Useful concept for evaluating outputs.

PRM

Process Reward Model. Scores intermediate reasoning/process steps.

Useful concept for complex reasoning systems.

Self-refinement

A model improves its output through critique and revision.

Useful when paired with criteria and limits.

Meta-CoT

Approaches that internalize or train reasoning/search behavior into the model.

Advanced research term. Not urgent.

Local deployment

Running models on your own machine/server instead of hosted APIs.

Useful for privacy, cost, control, or offline work. Not always worth the ops burden.

Multimodal Generation

Term

Plain English

Marcus / Symposium relevance

Multimodal model

A model that handles more than text: images, audio, video, or combinations.

Relevant for future creative/video/product work.

VAE

Variational Autoencoder. Compresses data into latent representations and reconstructs it.

Important in image generation theory and latent diffusion.

GAN

Generative Adversarial Network. Generator and discriminator compete to create realistic outputs.

Older major image-generation paradigm. Good history/context.

Autoregressive model

Generates output one step/token/pixel/frame at a time based on previous steps.

Common in language and some image/video systems.

Diffusion model

Generates data by learning to denoise from noise into a final image/video.

Core modern image/video generation concept.

T2I

Text-to-image generation.

Prompt -> image.

T2V

Text-to-video generation.

Prompt -> video. More complex and expensive than images.

U-Net

A neural architecture often used in diffusion models for image denoising.

Know the term. Do not need to build from scratch now.

DiT

Diffusion Transformer. Transformer-based architecture for diffusion models.

Current-generation diffusion vocabulary.

Forward process

In diffusion, gradually adding noise to data during training.

Theory term.

Backward process

In diffusion, learning to denoise from noise back to data.

Theory term.

Diffusion sampling

The process of generating an image/video by iterative denoising.

Practical because samplers affect quality/speed.

LDM

Latent Diffusion Model. Runs diffusion in compressed latent space instead of raw pixels.

Important for efficient image/video generation.

Compression network

Model that compresses media into a smaller latent representation.

Relevant to LDM and video generation.

Video latent caching

Precomputing/storing compressed video representations for training efficiency.

Advanced video-generation infrastructure term.

IS

Inception Score. Automated image quality/diversity metric.

Research metric. Less important than human taste for creative work.

FID

Fréchet Inception Distance. Measures generated image distribution vs real images.

Common benchmark metric. Useful but not product truth.

CLIP score

Measures alignment between image and text using CLIP-like models.

Useful for image-text alignment but can be gamed.

6. How This Maps to Symposium Offers

Offer

Underlying technical pieces

Client-visible outcome

AI Workflow / Agentic Delivery Audit

Workflow mapping, model selection, RAG feasibility, agent risk assessment, eval design.

Clear map of where AI can safely reduce manual work and where humans must stay in the loop.

Prototype Sprint

RAG, tool calling, routing, lightweight UI, eval checklist.

A working demo that proves one workflow can be AI-assisted.

Internal Tool Build

Document parsing, embeddings, database, auth, UI, logging, review gates.

Usable internal system for support, sales, ops, research, or admin workflows.

Agentic Delivery Governance Retainer

Evals, regression tests, prompt/version control, human review gates, monitoring.

AI workflows keep working instead of becoming brittle demos.

CTO / Dev Lead Training

Prompt decomposition, agent tasking, review discipline, MCP/tooling, eval culture.

The internal team learns how to direct agents without letting speed become chaos.

7. What Not to Chase Right Now

Full model training from scratch. Good theory, bad immediate ROI.

Diffusion model training. Interesting, but not the current business wedge.

Every acronym as a new side quest. Terms should attach to a build, not fragment attention.

Generic AI course addiction. A course is useful only if it compresses time or creates accountability.

Autonomous-agent fantasy. Most valuable client systems need constrained workflows, tool use, and human review gates.

Working standard
A term is “learned enough” when Marcus can explain it in plain English, identify when it matters, direct an AI/dev to implement or use it, and name at least one failure mode. Memorization is not the target. Operational control is the target.

8. Quick Reference: Highest-ROI Terms First

RAG, embeddings, chunking, vector search, context relevance, faithfulness, answer correctness.

Tool calling, routing, prompt chaining, orchestrator-worker, reflection, agent evaluation.

MCP and A2A as interoperability concepts.

SFT, RLHF, LoRA, PEFT as adaptation vocabulary, but not first moves.

Reasoning models, verifier, inference-time scaling, parallel/sequential sampling for research and planning.

Diffusion, VAE, GAN, U-Net, DiT as multimodal literacy, secondary to the current agentic-delivery lane.

Bottom line
The $2,000 course can be treated as a syllabus. The Marcus/Symposium move is to build the ladder directly, document the artifacts, and convert the strongest projects into public proof and client-facing offers.
