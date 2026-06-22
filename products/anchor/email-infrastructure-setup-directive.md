---
title: "email infrastructure setup directive"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/email-infrastructure-setup-directive.md.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# email infrastructure setup directive

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Email Infrastructure Setup — Directive

Status: READY TO EXECUTE Branch: not applicable (no code changes to Anchor repo) Sequence: complete this BEFORE firing email-checkin-redesign-directive.md

Header block

Field

Value

Surfaces

External — DNS for sobrietyanchor.com, email provider account, mailbox config, auto-responder

Production impact

Adds receiving + auto-reply capability to support@sobrietyanchor.com

Council of Models

no

Auto-merge

not applicable (no PR)

Credentials

Domain registrar access, email provider account, Marcus's personal email

Agent

Marcus (primary executor) + CC Local optional for verification scripts

Role statement

You are setting up the email infrastructure that lets support@sobrietyanchor.com receive messages, auto-reply to senders with crisis resources and product context, and forward all replies to Marcus's personal inbox for review. This is operational/infrastructure work, not Anchor codebase work. No PR is opened by this directive. The Anchor repo does not change.

This directive is a precondition for the email-checkin-redesign-directive.md work. Do not fire the redesign directive until every checkbox in the Sign-Off section below is checked.

Why this matters first

The redesign directive ships code that sends FROM support@sobrietyanchor.com. Once that email lands in user inboxes, replies will start arriving. If the inbox is not wired with forwarding and auto-responder, those replies fall into a void. For a recovery app, silence when a user reaches out is the wrong outcome.

Provider recommendation

Google Workspace — $6/month per user. Full mailbox for support@sobrietyanchor.com, native auto-responder (vacation responder), forwards to personal Gmail, plus Workspace utilities (Drive, Calendar) under Eagle Rocket LLC. Recommended.

Alternatives:

Fastmail — $5/month, clean interface, good auto-responder, supports forwarding

Migadu — variable pricing, business-friendly

Cloudflare Email Routing + Gmail filter hack — free, but auto-reply comes from personal Gmail address. Not recommended for a public-facing recovery product.

Pick one before starting Phase A.

Phase plan

Phase A — Provider account + mailbox creation

Marcus executes:

Sign up for chosen email provider with Eagle Rocket LLC billing details

Verify domain ownership for sobrietyanchor.com per provider's instructions (usually a TXT record)

Create mailbox: support@sobrietyanchor.com

Set a strong password and store in LastPass under "Anchor Production Secrets"

Optional: enable 2FA on the mailbox account

Verification before moving to Phase B:

Mailbox login page accepts the new credentials

Mailbox shows zero messages (clean state)

Phase B — DNS MX records

Marcus executes:

Log into the domain registrar for sobrietyanchor.com

Add MX records as specified by the email provider (Google Workspace uses smtp.google.com with priority 1, or the older 5-record set depending on plan; Fastmail uses in1-smtp.messagingengine.com and in2-smtp.messagingengine.com)

Wait for propagation (5-30 minutes typically)

Add any required SPF, DKIM, and DMARC records per provider's deliverability docs

Verification (CC Local can run this if available):

dig MX sobrietyanchor.com +short

dig TXT sobrietyanchor.com +short

Expected: MX records resolve to the provider's mail servers; SPF/DKIM TXT records are visible.

Phase C — Forwarding rule to personal email

Marcus executes:

In the provider's settings for support@sobrietyanchor.com, configure a forwarding rule

Destination: Marcus's personal email address (Gmail or other)

Choose: keep a copy in support@ mailbox AND forward (recommended, gives Marcus an archive)

Save the rule

Verification:

Send a test email from any external account to support@sobrietyanchor.com

Confirm the forward arrives in Marcus's personal inbox within 1-2 minutes

Confirm the original message is also retained in the support@ mailbox

Phase D — Auto-responder configuration

Marcus executes:

In the provider's settings for support@sobrietyanchor.com, configure an auto-responder (vacation responder) with this verbatim copy:

Thanks for reaching out to Anchor.

This inbox is not monitored in real time. Replies are forwarded for review but you may not get a personal response.

If you are in crisis:

988 (US) — Suicide & Crisis Lifeline, call or text

SAMHSA — 1-800-662-HELP (4357), 24/7 support

For day-to-day support, the in-app chat with Anchor is the fastest way to be heard:

https://sobrietyanchor.com/chat

For product issues or account help, reach Marcus directly at [REPLACE WITH MARCUS'S PERSONAL EMAIL].

Take care.

— Anchor

Replace [REPLACE WITH MARCUS'S PERSONAL EMAIL] with the actual address before saving. Do not leave the placeholder.

Subject line for auto-reply: Anchor — thanks for reaching out

Frequency settings: respond to each unique sender once per 7 days (avoid responder loops with automated systems).

Verification:

Send a test email from an external account to support@sobrietyanchor.com

Confirm the auto-reply arrives at the external account within 1-2 minutes

Confirm the auto-reply contains the verbatim copy above with no placeholder text

Phase E — End-to-end verification

Marcus executes the full path test:

Send a test email from an external account (not the personal email used for forwarding — use a different address) to support@sobrietyanchor.com with subject "End-to-end test" and any body

Confirm three things happen:

The auto-reply arrives at the external test account

The forward arrives at Marcus's personal email

A copy is retained in the support@ mailbox

If any of the three fail: stop, fix that step, retest before continuing.

Phase F — Documentation

Marcus executes:

Create a run note at docs/run-notes/session-YYYY-MM-DD-email-infrastructure-setup.md in the Anchor repo with:

Provider chosen and why

Mailbox address(es) created

DNS records added (MX, SPF, DKIM, DMARC)

Forwarding destination

Auto-responder copy used

Verification test results

LastPass entry name for credentials

This becomes a permanent record of the infrastructure decision and lives alongside other Anchor operational notes.

Commit and push directly to main:

git checkout main

git pull

# create the run note

git add docs/run-notes/session-YYYY-MM-DD-email-infrastructure-setup.md

git commit -m "docs(ops): email infrastructure setup notes"

git push origin main

No PR needed — it's a documentation-only commit and main is the source of truth.

Sign-off checklist

Do not fire email-checkin-redesign-directive.md until every box below is checked:

Provider account active and billing set up

support@sobrietyanchor.com mailbox created and accessible

Mailbox credentials stored in LastPass

MX records propagated and verified via dig

SPF, DKIM, DMARC records added per provider deliverability guide

Forwarding to personal email confirmed working

Auto-responder configured with verbatim copy and Marcus's personal email substituted in

End-to-end test passed (auto-reply + forward + mailbox copy all received)

Run note committed to main

Forbidden side quests

Do NOT change Resend configuration in this directive (Resend handles outbound sends from Anchor; this directive only sets up inbound + auto-reply)

Do NOT add tracking pixels, link-tracking, or any analytics to the auto-reply

Do NOT use a free-mail address as the forwarding destination if compliance/professionalism is a concern (a personal email Marcus actually reads is fine)

Do NOT enable the auto-responder before verifying the verbatim copy has the correct personal-email substitution

Do NOT skip the end-to-end verification step

Hard stops

Stop and log to BLOCKERS_FOR_MARCUS.md if:

Domain registrar access is unavailable

MX records fail to propagate after 1 hour

Forwarding rule cannot be configured on chosen provider

Auto-responder is not supported by chosen provider (then re-pick provider)

End-to-end test fails after retry

GO

Marcus picks the provider, then begins Phase A. CC Local optional for Phase B verification via dig. No agent fires this directive; Marcus executes it manually.

When all sign-off boxes are checked, fire email-checkin-redesign-directive.md at CC Local.
