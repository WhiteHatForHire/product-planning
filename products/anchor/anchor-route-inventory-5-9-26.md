---
title: "Anchor Route Inventory 5 9 26"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/References/Anchor Route Inventory 5_9_26.docx"
status: archive
privacy: working
tags:
  - product
---

# Anchor Route Inventory 5 9 26

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Anchor Route Inventory 5/9/26

Step 1 — All registered backend routes

Mounted at /api/* in app.ts, defined across 11 router files in artifacts/api-server/src/routes/:

Method

Path

File

GET

/api/healthz

health.ts

POST

/api/checkin

checkin.ts

GET

/api/checkin/history

checkin.ts

GET

/api/checkin/today

checkin.ts

GET

/api/checkin/latest

checkin.ts

GET

/api/checkin/history/:id

checkin.ts

PATCH

/api/checkin/:id

checkin.ts

POST

/api/chat

chat.ts

POST

/api/chat/session-summary

chat.ts

GET

/api/trackers

trackers.ts

POST

/api/trackers

trackers.ts

GET

/api/trackers/:id

trackers.ts

PATCH

/api/trackers/:id

trackers.ts

DELETE

/api/trackers/:id

trackers.ts

POST

/api/trackers/:id/reset

trackers.ts

POST

/api/trackers/:id/archive

trackers.ts

POST

/api/trackers/:id/unarchive

trackers.ts

GET

/api/trackers/:id/resets

trackers.ts

GET

/api/settings

settings.ts

PATCH

/api/settings

settings.ts

POST

/api/settings/complete-onboarding

settings.ts

POST

/api/settings/reset-onboarding

settings.ts

POST

/api/settings/update-last-opened

settings.ts

GET

/api/insights/stats

insights.ts

GET

/api/insights/trends

insights.ts

GET

/api/insights/calendar

insights.ts

GET

/api/memory

memory.ts

PATCH

/api/memory/profile

memory.ts

DELETE

/api/memory/event/:index

memory.ts

POST

/api/memory/reset

memory.ts

POST

/api/commitments

commitments.ts

GET

/api/commitments/due

commitments.ts

GET

/api/commitments/pending

commitments.ts

GET

/api/commitments/stats

commitments.ts

PATCH

/api/commitments/:id

commitments.ts

GET

/api/email/settings

email.ts

POST

/api/email/settings

email.ts

POST

/api/email/test

email.ts

POST

/api/speak

speak.ts
