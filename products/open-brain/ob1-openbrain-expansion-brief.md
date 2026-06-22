---
title: "OB1 OpenBrain Expansion Brief"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /# Open Brain/OB1 _ OpenBrain Expansion Brief.docx"
status: reference
privacy: working
tags:
  - product
---

# OB1 OpenBrain Expansion Brief

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
OB1 / OpenBrain Expansion Brief

From manual memory capture to corpus-native AI operating layer

1. Executive summary

OB1/OpenBrain is a useful starting point, but it is not yet the full system Marcus needs.

The version currently tested works as a manual AI memory layer: an AI client can capture a thought, extract metadata, embed it, and retrieve it later through semantic search. That is real and useful. The smoke test passed.

But Marcus’s actual vision is larger: a full-corpus AI operating layer that can ingest an entire personal or enterprise knowledge corpus, preserve source documents in full, chunk and index them, retrieve exact source-grounded passages, and optionally extract durable memories on top.

The core distinction:

OB1 today: save and retrieve thoughts.
Marcus’s needed system: ingest and operate on an entire living corpus.

This is likely the real IP opportunity.

2. What OB1 can do today

Based on today’s test and the companion prompt documentation, OB1 currently supports:

Manual thought capture

A user or AI can save standalone memories such as decisions, observations, ideas, people notes, and references. The companion prompts describe this as saving “clean, standalone” thoughts that future AIs can understand without needing the original context.

Example:

“Marcus is at NYC Tech Week on June 1, 2026.”

This was successfully captured, tagged, embedded, and retrieved.

Metadata extraction

Captured thoughts can be classified by type, topic, people, dates, and action items.

Observed today:

Type: observation
Topic: NYC Tech Week
Person: Marcus
Date: June 1, 2026

Semantic search

The system can retrieve thoughts by meaning, not just exact keyword matching.

This means future AI clients can ask something like:

“What did Marcus capture about NYC Tech Week?”

and retrieve the stored thought.

MCP access from AI clients

The key value is not just storage. It is that OpenBrain can be accessed through MCP-connected AI clients. The companion doc is explicitly designed around use from Claude, ChatGPT, Gemini, Grok, and other MCP-connected tools.

Migration prompts

OB1 includes companion prompts for:

memory migration from AI platforms

second-brain migration from Notion, Obsidian, Apple Notes, text files, and other systems

personalized use-case discovery

quick capture templates

weekly review rituals

The companion documentation positions these prompts as the habit layer that makes OpenBrain compound.

3. What OB1 does not yet appear to solve

The current capture interface is not enough for Marcus’s real use case.

The companion migration prompt says the OpenBrain stores “thoughts, not document fragments,” and instructs the AI to transform notes into standalone thoughts before saving.

That is useful, but it creates a major limitation:

It does not guarantee preservation of the full source corpus as searchable, citeable raw material.

For Marcus, that is not acceptable.

Marcus does not only want:

“Summarize my 1,000 documents into memories.”

He wants:

“Preserve my 1,000 documents in full, chunk them, index them, embed them, retrieve them with source grounding, and extract durable memories on top.”

So the missing capabilities are:

full document ingestion

raw source preservation

document-level metadata

chunk-level storage

chunk-level embeddings

source citations

deduplication

file manifests

import reports

batch processing

approval queue for extracted memories

agentic scheduled ingestion

permissioning for enterprise use

audit trails

retrieval from original source chunks, not only distilled thoughts

4. What Marcus actually needs

Marcus needs a corpus-native AI operating system.

Working definition:

A system that preserves a person or company’s full knowledge corpus, indexes it for semantic retrieval, extracts durable operating memory, and gives AI agents governed access to that context across workflows.

This system should support both personal and enterprise use.

For Marcus personally, it should ingest:

journal threads

continuity briefs

build logs

product specs

Anchor history

Symposium notes

Marcus Vale essays

travel/base strategy notes

relationship context

Yuni context

Greek virtue logs

AI self-governance frameworks

screenshots and transcripts

voice memo transcripts

project documents

ChatGPT / Claude exports

For enterprise clients, it should ingest:

internal docs

meeting notes

SOPs

product specs

customer notes

sales calls

support tickets

Slack exports

email history, where permitted

project management data

codebase docs

onboarding docs

leadership decisions

client histories

5. Product thesis

The thesis:

Most individuals and companies do not have an AI problem. They have a context problem.

Their knowledge is scattered across documents, meetings, chats, people’s heads, project tools, and old AI conversations.

LLMs are powerful, but every new AI session starts context-poor unless someone manually explains the world again.

The opportunity is to build a system that turns scattered knowledge into an operational corpus.

Positioning:

OB1/OpenBrain is the seed. Marcus/Symposium builds the full corpus operating layer.

Possible product language:

“We build AI memory and corpus systems for founder-led teams, operators, and companies whose knowledge is scattered across documents, meetings, tools, and people.”

Sharper version:

“We turn your company’s scattered knowledge into a source-grounded AI operating memory.”

6. Architecture

The system should have four layers.

Layer 1: Raw corpus layer

This preserves full source material.

Nothing gets reduced or replaced by summaries.

Sources may include:

markdown

PDFs

text files

Google Docs exports

Notion exports

Obsidian vaults

ChatGPT exports

Claude logs

meeting transcripts

audio transcripts

screenshots with extracted text

code docs

CSVs

Core principle:

Raw source stays intact.

Layer 2: Chunk/index layer

Documents are split into retrievable chunks.

Each chunk should include:

document ID

chunk index

content

embedding

token count

source path or URL

date

topics

people

project

start and end position if available

checksum / dedup fingerprint

This is the actual RAG layer.

Layer 3: Memory/thought layer

This is where OB1’s current model fits.

The system extracts durable memories from the corpus:

decisions

operating principles

preferences

people notes

project state

recurring patterns

action items

lessons learned

product constraints

relationship context

These are not replacements for documents. They are the operating layer above the corpus.

Layer 4: Agent/workflow layer

This is where OpenClaw or a similar agentic layer comes in.

Agents can:

watch folders

run cron jobs

ingest new files

classify documents

chunk documents

embed chunks

deduplicate content

propose memories

ask for approval

run weekly reviews

answer questions from the corpus

generate citations

create build directives

create continuity briefs

7. Proposed database structure

Minimum useful schema:

documents

Stores the source document.

Fields:

id

title

source_type

source_path or storage_url

original_filename

created_at

document_date

imported_at

author, if known

project

checksum

metadata_json

full_text, or pointer to full text storage

document_chunks

Stores searchable chunks.

Fields:

id

document_id

chunk_index

content

embedding

token_count

start_char

end_char

topics

people

metadata_json

created_at

thoughts

The existing OpenBrain-style memory layer.

Fields:

id

content

type

topics

people

action_items

dates_mentioned

embedding

created_at

updated_at

thought_source_links

Connects extracted memories back to source material.

Fields:

id

thought_id

document_id

chunk_id

confidence

extraction_method

created_at

import_jobs

Tracks ingestion runs.

Fields:

id

source

status

started_at

completed_at

documents_processed

chunks_created

thoughts_proposed

failures

cost_estimate

report_json

8. Agentic ingestion pipeline

The build should be agentic but governed.

Pipeline:

Discover
Agent scans an import folder or connected source.

Manifest
Agent creates a manifest of all files, dates, sizes, types, and checksums.

Prioritize
Agent ranks files by likely value or user-provided priority.

Parse
Agent extracts text from each document.

Chunk
Agent splits documents into semantically useful chunks.

Embed
Agent creates embeddings for each chunk.

Index
Agent stores documents and chunks in the database.

Extract
Agent proposes durable memories from the chunks.

Review
User approves, edits, or rejects proposed memories.

Publish
Approved memories enter the OpenBrain thought layer.

Report
Agent produces an import report with failures, duplicates, top topics, and coverage.

Core governance rule:

Full document ingestion can be automatic. Durable memory extraction should start as approval-based.

9. MVP build plan

MVP 0: Current state

Already achieved:

OpenBrain MCP connected

capture works

metadata extraction works

semantic search works

retrieval works

MVP 1: Local corpus ingestion

Goal:

Drop 10 markdown or text files into an import folder and index them.

Acceptance criteria:

system creates document records

system creates chunk records

chunks are embedded

search returns relevant chunks

results include source document names

user can ask questions against the chunk index

MVP 2: Source-grounded retrieval

Goal:

Search returns citeable source chunks.

Acceptance criteria:

every answer can show source document and chunk

search results distinguish raw chunks from distilled memories

system can answer: “show me the source material for this claim”

MVP 3: Memory extraction queue

Goal:

Agent proposes durable memories from indexed documents.

Acceptance criteria:

agent extracts decisions, people notes, project facts, and action items

proposed memories are shown in a review queue

user can approve, edit, reject

approved memories are saved to OpenBrain thoughts

memories link back to source chunks

MVP 4: 100-document batch

Goal:

Run import across 100 high-signal corpus docs.

Acceptance criteria:

import report generated

failures logged

duplicates detected

topics clustered

cost/time measured

retrieval quality manually tested

MVP 5: 1,000-document corpus

Goal:

Full Marcus corpus ingestion.

Acceptance criteria:

all files manifest

all valid files indexed

retrieval works across major life/project domains

extracted memories are reviewed in batches

system can answer high-context questions with source grounding

10. Enterprise version

Enterprise clients need a more controlled version.

Required enterprise features:

permissions by user/team/project

source citations

audit logs

document deletion and re-indexing

private deployment option

ingestion reports

admin dashboard

connector framework

approval workflows

data retention policy

role-based access

redaction tools

source-of-truth hierarchy

Enterprise pitch:

“We do not replace your documents with AI summaries. We preserve your source material, index it, and build an AI-accessible operating memory on top.”

Client examples:

Founder-led company

Problem:

Founder repeats context constantly to team, contractors, and AI tools.

System:

Ingest founder docs, Slack exports, SOPs, client notes, product specs, and meeting transcripts. Build founder/company memory.

Agency or studio

Problem:

Client context gets lost between proposals, calls, deliverables, and implementation.

System:

Ingest client docs, call notes, scopes, emails, and deliverables. Build client-specific AI memory.

Internal operations team

Problem:

Processes live across Notion, Google Docs, Slack, and old employee knowledge.

System:

Ingest SOPs and historical decisions. Build queryable operational knowledge base.

11. Marcus’s likely IP

The IP is probably not “a vector database.”

The IP is:

the ingestion methodology

the agentic pipeline

the review workflow

the memory extraction taxonomy

the operator UX

the enterprise implementation playbook

the “corpus plus memory” architecture

the Director Model applied to knowledge systems

the Pattern Intimacy methodology

the ability to convert messy personal/company history into AI-usable operational context

OB1 can be a starting point, but Marcus’s product is bigger.

Potential names later:

OpenClaw

Corpus OS

Symposium Memory OS

Pattern Engine

External Brain

CorpusVault

Aristotle OS

OpenBrain Enterprise Layer

Do not name it permanently yet. Build the architecture first.

12. Strategic conclusion

OB1 is not worthless. It proves the MCP memory pattern.

But manual thought capture alone is not the product Marcus needs.

The real system must preserve and index the full corpus.

The correct build direction is:

Full corpus ingestion → chunked retrieval → source citations → extracted operating memory → agentic workflows.

That is the personal system Marcus needs.

That is also the enterprise wedge Symposium can sell.

Core line:

The corpus is the ground. Memory is the operating layer. Agents are the workforce.
