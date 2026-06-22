---
title: "Symposium OS structure 5 16 26"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/#Studio OS/#SYMPOSIUM OS/Symposium OS structure 5_16_26.docx"
status: active
privacy: working
tags:
  - studio-os
---

# Symposium OS structure 5 16 26

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
.symposium/

README.md                           # what this folder is, how to navigate

AUTONOMY_LAYER.md                   # v1.3 stripped to generic (Anchor specifics removed)

META_PROMPT.md                      # v1.3 stripped to generic

CONTEXT.md                          # project glossary, ubiquitous language

skills/

planning/

generate-directive/             # spec + meta-prompt + autonomy-layer → runnable directive

grill-with-docs/                # planning interview, updates CONTEXT.md and ADRs

diagnostics/

api-surface-diagnostic/         # read actual handlers before any FE/mobile wave

ics-feed-diagnostic/            # Kairos-specific: validate Carly feed before ingest

execution/

mcp-write-safety/               # section 1.12 preflight, invocable form

deployment-preflight/           # env vars, project IDs, secrets, build cmd, health endpoint

review/

council-review/                 # multi-model lens review for PRs and prompts

public-surface-qa/              # external-facing surface audit

build-report-ledger/            # session-to-receipt compression with 2022 baseline

handoff/

session-handoff/                # agent-to-agent or end-of-session context transfer

templates/

directive-template.md

handoff-template.md

build-report-template.md

adr-template.md

adr/

0001-skills-marketplace-architecture.md

0002-file-first-no-db-v1.md

0003-carly-as-source-of-truth.md

0004-two-pass-relevance-scoring.md
