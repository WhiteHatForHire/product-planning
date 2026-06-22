---
title: "Anchor V3 Production Deployment Plan"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/Anchor V3 Production Deployment Plan.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# Anchor V3 Production Deployment Plan

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ANCHOR V3 PRODUCTION DEPLOYMENT PLAN

Go-Live Operations Document

Working draft. April 25, 2026.

Maxwell / Eagle Rocket LLC

Preamble

This document is the operational companion to the Anchor V4 Master Doc v2. The master doc captures what is shipped, what is deferred, and the strategic doctrine. This document captures how to actually deploy Anchor V3 to production, in order, with concrete steps, configuration values, decision points, and known traps.

Audience: future Maxwell sitting at a desk with a few hours to make progress on go-live. The doc assumes familiarity with the Anchor codebase but no familiarity with the specific production stack until each section introduces it.

Doctrine: ship in stages. Each stage produces a working artifact. Do not move to the next stage until the current one is verified. The fastest way to a clean production deploy is to refuse to compress steps.

Scope: get Anchor V3 to a real domain with real auth, real database, real email, real error tracking, and the developer's own real production account. Onboarding additional users beyond the developer is out of scope for this document.

Table of Contents

1. Stack Overview

2. Pre-Flight Checklist

3. Stage 0: Domain and Accounts

4. Stage 1: Database (Neon)

5. Stage 2: Auth (Supabase)

6. Stage 3: Multi-User Code Refactor

7. Stage 4: Backend Deploy (Fly.io)

8. Stage 5: Frontend Deploy (Vercel)

9. Stage 6: Email (Resend Production Domain)

10. Stage 7: Error Tracking (Sentry)

11. Stage 8: Landing Page

12. Stage 9: Legal and Compliance

13. Stage 10: First Real Account

14. Stage 11: Smoke Test in Production

15. Go / No-Go Checklist

16. Rollback Plan

17. Post-Launch First Week

18. Cost Expectations

19. Common Traps and Gotchas

20. Appendix A: Environment Variable Reference

21. Appendix B: Useful Commands

1. Stack Overview

Final stack as decided in the V4 master doc:

Frontend: Vercel (static + edge functions if needed). React/TypeScript/Vite build.

Backend: Fly.io. Node.js/Express. Cron-compatible. Single region to start (probably iad or sjc).

Database: Neon Postgres. Serverless. Branching for staging.

Auth: Supabase Auth. JWT verified server-side on Fly.

Email: Resend. Production sender domain with verified DNS, SPF, DKIM.

Errors: Sentry. Free tier. Frontend + backend SDKs.

Analytics: None at launch. Sentry covers what is broken.

Landing page: Separate Vercel project, static site, one page.

Domain: TBD. Decision in Stage 0.

Why this stack: each piece has a real free or near-free tier, each piece is mainstream enough to credibly cite on a fCTO résumé, and no piece locks the project into a vendor that can't be migrated later. Fly + Neon + Supabase + Vercel is a portable architecture.

2. Pre-Flight Checklist

Before starting Stage 0, verify the following are true. If any are false, fix them first.

All 111 smoke tests pass on the current Replit dev URL.

No outstanding bug reports from field testing.

stable_profile shape is current and matches the V4 master doc reference.

Database schema is current. No pending migrations sitting uncommitted.

No secrets are committed to git history. Run a quick scan: git log --all -p | grep -iE 'sk-|RESEND|API_KEY' should return nothing meaningful.

Local repo is on main, clean, pushed to GitHub or wherever the source of truth lives.

A working backup of the current Replit dev DB exists, even if the data won't be migrated. pg_dump and save the .sql file somewhere safe.

The V4 master doc v2 is read and understood.

At least one uninterrupted 4-hour block exists on the calendar for the first 2-3 stages.

Note: Stages 0-2 are roughly 1 evening of setup. Stage 3 (multi-user refactor) is the real work and is its own multi-day effort. Stages 4-11 are 1-2 evenings if Stage 3 is clean.

3. Stage 0: Domain and Accounts

Goal: pick a domain, register it, create accounts on every required service.

3.1 Domain Selection

The domain matters less than getting started. Avoid spending more than 30 minutes on this. Constraints:

Short. 1-2 words ideal.

Spellable. If a sober person at midnight can't type it from memory, it's wrong.

Pronounceable. Has to work in conversation.

Not gimmicky. This is a recovery tool, not a SaaS startup.

.app, .recovery, .com all acceptable. .com is most trusted but most taken.

Candidates to evaluate (check availability):

useanchor.app

anchor.recovery

anchorapp.io

getanchor.app

anchorlog.app

tryanchor.app

Decision: Pick one. Buy it. Move on. Domains can be replaced later. The first domain does not have to be the final domain.

3.2 Registrar

Use Cloudflare Registrar if the TLD is supported (no markup, free WHOIS privacy). Otherwise Namecheap. Avoid GoDaddy.

3.3 Accounts to Create

Create accounts on each of these services. Use the Eagle Rocket LLC email if one exists, otherwise the personal recovery-app-ops email. Do not use a personal email tied to other services.

Vercel (vercel.com). Hobby tier sufficient.

Fly.io (fly.io). Pay-as-you-go. Add a credit card; small charges expected.

Neon (neon.tech). Free tier sufficient at start.

Supabase (supabase.com). Free tier sufficient at start.

Resend (resend.com). Free tier covers expected volume.

Sentry (sentry.io). Developer / free tier.

GitHub (already exists). Make sure repo is private.

3.4 Password Hygiene

Use a password manager. Each account gets a unique generated password. Enable 2FA on every account that supports it, especially the registrar, GitHub, Vercel, Fly, and Supabase. The registrar is the highest-value target; treat it like a bank.

3.5 A Single Source of Truth for Secrets

Create one password-manager note titled "Anchor Production Secrets" with all environment variables, database URLs, API keys. Each stage adds to this note. This becomes the disaster recovery document.

4. Stage 1: Database (Neon)

Goal: a production Postgres database with the Anchor schema applied, ready to receive connections from a deployed backend.

4.1 Create Neon Project

Sign in to neon.tech.

Create new project. Name: anchor-prod.

Region: pick whichever is closest to where Fly will deploy. iad (us-east) is a safe default if undecided.

Postgres version: latest stable.

Save the connection string immediately. Format: postgres://user:pass@host/db?sslmode=require

4.2 Branch Strategy

Neon supports branching. Create:

main branch — production database. Never write to it directly.

staging branch — for pre-deploy verification. Branched from main.

The dev environment continues to use Replit's Postgres until that environment is sunset. The Neon staging branch is for verifying production deploys before promoting.

4.3 Apply Schema

Schema is captured in the existing migration files (or schema.sql equivalent). Apply to main:

psql "postgres://...neon-main..." -f schema.sql

Then verify the tables exist:

psql "postgres://...neon-main..." -c "\dt"

Expected tables (per V4 master doc Section 3):

user_memory

app_settings

commitments

chat_sessions

check_ins

sobriety_trackers

tracker_resets

4.4 The user_id Column Audit

Critical: Every user-data table must have a user_id column with an index. Verify before going further.

Run this query to find any table missing user_id:

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_name NOT IN (
    SELECT table_name FROM information_schema.columns
    WHERE table_schema = 'public' AND column_name = 'user_id'
  );

If anything other than utility tables (e.g. migrations) shows up, fix it now. user_id is the foundation of multi-user safety. Adding it later is much harder.

4.5 No Data Migration

Production database starts empty. Existing dev data is dev data. Do not migrate it. The developer creates a fresh production account on first launch.

4.6 Save the Connection Strings

Add to the Anchor Production Secrets password-manager note:

NEON_DATABASE_URL_PROD (main branch)

NEON_DATABASE_URL_STAGING (staging branch)

5. Stage 2: Auth (Supabase)

Goal: a Supabase Auth project that issues JWTs, with magic link and at least one OAuth provider enabled.

5.1 Create Supabase Project

Sign in to supabase.com.

Create new project. Name: anchor-auth.

Choose a region. Pick the same region family as Neon and Fly to minimize cross-region latency.

Database password: generate, save in Anchor Production Secrets. (This is for the Supabase-managed Postgres, which is NOT used for app data — Anchor uses Neon for that. Supabase's DB just stores auth users.)

5.2 Auth Configuration

In the Supabase dashboard, Authentication → Providers:

Enable Email (magic links). Disable email/password if not needed; magic links are simpler and more secure.

Enable Google OAuth. Requires a Google Cloud project with OAuth consent screen configured. Set authorized redirect URI to https://[supabase-project].supabase.co/auth/v1/callback.

Optionally enable Apple OAuth. More setup work; defer unless launching iOS soon.

Optionally enable GitHub OAuth (useful for the developer's own account during testing).

5.3 Site URL and Redirects

Authentication → URL Configuration:

Site URL: https://[your-domain] (the production frontend domain, even if not deployed yet — set it to what it will be).

Redirect URLs: add https://[your-domain]/auth/callback and https://[your-domain]/* as a wildcard for development.

For local dev: also add http://localhost:5173/* or whatever the Vite dev server uses.

5.4 JWT Secret and Public Keys

Settings → API. Copy and save:

Project URL (public).

anon key (public, for the frontend).

service_role key (secret, server-side only). NEVER ship to the frontend.

JWT secret (secret, used by the backend to verify JWTs without calling Supabase).

Critical: service_role key bypasses all row-level security. If this leaks, every user's data is exposed. Treat it like a password.

5.5 No Row-Level Security on Anchor Tables

Anchor's data lives in Neon, not Supabase. Supabase's RLS does not apply. Multi-user safety in Anchor is enforced by application code in the Fly backend. Every API route must verify the JWT and scope queries by user_id.

5.6 Save the Keys

Add to Anchor Production Secrets:

SUPABASE_URL

SUPABASE_ANON_KEY

SUPABASE_SERVICE_ROLE_KEY

SUPABASE_JWT_SECRET

6. Stage 3: Multi-User Code Refactor

Addition:

Read the HANDOFF.md file (or wherever the Stage 3 prep notes live) and add the following items to the Stage 3 prerequisites section. Do not modify anything else.

Additional Stage 3 prereqs surfaced from Stage 1 audit:

- tracker_resets direct query risk: audit every query that touches tracker_resets and confirm it always joins through sobriety_trackers. Any direct SELECT on tracker_resets without the join is an authorization bug.

- tracker_resets ON DELETE NO ACTION → should be CASCADE: if a sobriety_trackers row is deleted, tracker_resets rows should cascade. Add this to the schema migration in Stage 3.

- tracker_resets missing index on tracker_id: add alongside the other missing user_id indexes in the Stage 3 index pass.

Goal: replace the single-user APP_USER_ID shim with real session-derived user IDs from Supabase JWTs.

Critical: This is the highest-risk stage. A bug here means cross-user data leakage. Take it slowly. Add tests as you go.

6.1 The Chokepoint: getCurrentUserId()

Right now, getCurrentUserId() returns process.env.APP_USER_ID || "dev_user". Every backend route already calls this function. That is the entire reason the function exists — to be a single replaceable chokepoint.

The plan: replace the implementation, not the call sites. The signature stays the same. The internals change.

6.2 Add JWT Verification Middleware

Install dependencies:

npm install @supabase/supabase-js jsonwebtoken

Create a new helper, e.g. utils/auth.js:

const jwt = require('jsonwebtoken');

function verifyJwt(token) {
  if (!token) return null;
  try {
    const payload = jwt.verify(token, process.env.SUPABASE_JWT_SECRET);
    return payload.sub; // Supabase user UUID
  } catch (err) {
    return null;
  }
}

function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization || '';
  const token = authHeader.startsWith('Bearer ') ? authHeader.slice(7) : null;
  const userId = verifyJwt(token);
  if (!userId) {
    return res.status(401).json({ error: 'unauthorized' });
  }
  req.userId = userId;
  next();
}

module.exports = { verifyJwt, authMiddleware };

6.3 Wire authMiddleware Into Every Protected Route

In the route registration file:

const { authMiddleware } = require('./utils/auth');

// All routes that touch user data go through authMiddleware
app.use('/api/check-in', authMiddleware);
app.use('/api/chat', authMiddleware);
app.use('/api/commitments', authMiddleware);
app.use('/api/memory', authMiddleware);
app.use('/api/trackers', authMiddleware);
app.use('/api/email-status', authMiddleware);
// ... every /api/* route except health checks

6.4 Replace getCurrentUserId() Implementation

In utils/v3helpers.js (or wherever the helper lives):

// OLD:
// function getCurrentUserId() {
//   return process.env.APP_USER_ID || "dev_user";
// }

// NEW:
function getCurrentUserId(req) {
  if (!req || !req.userId) {
    throw new Error('getCurrentUserId called without authenticated request');
  }
  return req.userId;
}

Note: The signature changes from () to (req). Every call site must be updated to pass req. This is intentional — the compiler will tell you exactly where the call sites are.

6.5 Update All Call Sites

Find every call to getCurrentUserId() across the codebase:

grep -rn "getCurrentUserId()" artifacts/ utils/ src/

Each one needs to be updated to pass the request object. Most are inside Express route handlers, so the change is mechanical:

// Before:
const userId = getCurrentUserId();

// After:
const userId = getCurrentUserId(req);

6.6 Helper Functions That Don't See req

Some helpers (e.g. inside the email scheduler cron job) don't have a req object. They need a different path:

Scheduled jobs: iterate over all users via direct database queries (SELECT DISTINCT user_id FROM user_memory), then pass user_id explicitly into per-user logic.

Helper functions called from routes: accept user_id as an explicit parameter rather than calling getCurrentUserId() themselves.

Background tasks via safeBackgroundTask(): the calling route passes user_id into the closure.

6.7 Frontend: Send the JWT

The frontend already makes API calls. Each one now needs the JWT in the Authorization header. Centralize this in a fetch wrapper:

// src/lib/api.ts
import { supabase } from './supabase';

export async function apiFetch(path: string, init: RequestInit = {}) {
  const { data: { session } } = await supabase.auth.getSession();
  const headers = {
    ...(init.headers || {}),
    'Content-Type': 'application/json',
    ...(session?.access_token
      ? { Authorization: `Bearer ${session.access_token}` }
      : {}),
  };
  return fetch(path, { ...init, headers });
}

Replace every direct fetch('/api/...') with apiFetch('/api/...'). This is mechanical but tedious. Do it in one pass per file.

6.8 Frontend: Login Screen

Create a Login page. Use Supabase's built-in UI or roll a minimal one. Magic link is simplest:

import { supabase } from '../lib/supabase';

async function sendMagicLink(email: string) {
  const { error } = await supabase.auth.signInWithOtp({
    email,
    options: { emailRedirectTo: `${window.location.origin}/auth/callback` },
  });
  if (error) throw error;
}

Add a route guard so unauthenticated users land on /login. Wouter pattern:

// In App.tsx
const { data: { session } } = await supabase.auth.getSession();
if (!session) {
  // redirect to /login
}

6.9 Test Cross-User Isolation

Add a Playwright test (or two) that creates two test users and verifies they cannot see each other's data. This is the single most important test in the whole suite from this point forward.

Test: user A creates a check-in. user B logs in. user B's /api/check-ins should not return user A's check-in.

Test: user A creates a commitment. user B's /api/commitments should not include it.

Test: user B sends a request without the Authorization header. Server returns 401.

Test: user B sends a request with an expired or tampered JWT. Server returns 401.

6.10 Verification Checklist for Stage 3

Every grep for getCurrentUserId() returns calls with req argument.

Every API route except health checks has authMiddleware.

All 111 existing smoke tests still pass (against staging branch).

New cross-user isolation tests pass.

No hardcoded user IDs anywhere in the codebase. Final grep: grep -rn '"dev_user"\|"maxwell"' . — must return nothing.

APP_USER_ID env var is no longer required (but can stay as a fallback for local dev, gated by NODE_ENV !== 'production').

7. Stage 4: Backend Deploy (Fly.io)

Goal: the Anchor backend running on Fly.io, reachable at a Fly-assigned URL, talking to the Neon staging branch.

7.1 Install flyctl

curl -L https://fly.io/install.sh | sh
fly auth login

7.2 Initialize Fly App

From the backend project root:

fly launch --no-deploy

Answers:

App name: anchor-api (or similar — must be globally unique on Fly).

Region: pick to match Neon. iad if undecided.

Postgres? No. (Using Neon.)

Redis? No.

Deploy now? No.

This creates fly.toml. Open it and verify the internal_port matches what Express listens on (probably 3000 or 8080).

7.3 Dockerfile

Fly auto-generated a Dockerfile. Review it. For a Node/Express app, the typical shape:

FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
EXPOSE 8080
CMD ["node", "artifacts/api-server/src/index.js"]

Adjust the CMD to match the actual entry point.

7.4 Set Production Secrets on Fly

fly secrets set \
  DATABASE_URL="postgres://...neon-staging..." \
  SUPABASE_URL="https://...supabase.co" \
  SUPABASE_JWT_SECRET="..." \
  SUPABASE_SERVICE_ROLE_KEY="..." \
  OPENAI_API_KEY="sk-..." \
  RESEND_API_KEY="re_..." \
  RESEND_FROM_EMAIL="hello@anchor-domain.app" \
  EMAIL_OUTREACH_ENABLED="false" \
  OPENAI_TTS_MODEL="tts-1" \
  OPENAI_TTS_VOICE="onyx" \
  NODE_ENV="production"

Note: Start with EMAIL_OUTREACH_ENABLED=false. Turn it on only after Stage 6 verifies the Resend production domain. Do not send a single email until DNS is verified.

Note: Initial deploy points at the Neon staging branch, not main. This is intentional — verify the deploy works against staging data before pointing at production.

7.5 Deploy

fly deploy

Watch the build output. Common failures:

Build context too large: add a .dockerignore. Exclude node_modules, .git, tests/, *.log.

Port mismatch: Fly expects the app to listen on the port in fly.toml. Check process.env.PORT in the app.

Health check fails: Fly probes / by default. Add a GET / route that returns 200, or configure a /health endpoint in fly.toml.

7.6 Verify Backend Reachability

curl https://anchor-api.fly.dev/health

Should return 200. If not, check fly logs:

fly logs

7.7 Cron Compatibility

Fly supports cron via two patterns:

In-process: the app uses node-cron and stays running. Works because Fly keeps the machine alive while it has traffic. Risk: if the machine sleeps due to no traffic, cron stops. Mitigation: configure fly.toml with min_machines_running = 1.

External cron: use Fly's scheduled machines (fly machine run --schedule daily ...). Cleaner but more setup.

For Anchor V3, in-process node-cron with min_machines_running = 1 is sufficient. Add to fly.toml:

[[services]]
  internal_port = 8080
  protocol = "tcp"
  min_machines_running = 1

8. Stage 5: Frontend Deploy (Vercel)

Goal: the Anchor frontend on Vercel, talking to the Fly backend, served at a Vercel-assigned URL.

8.1 Install Vercel CLI (Optional)

npm install -g vercel
vercel login

Or use the Vercel dashboard's GitHub integration. Dashboard is simpler for first deploy.

8.2 Connect Repo

Vercel dashboard → Add New → Project.

Import the Anchor frontend repo. (If frontend and backend are in one repo, set the root directory in Vercel project settings.)

Framework preset: Vite.

Build command: npm run build.

Output directory: dist.

8.3 Frontend Environment Variables

Vercel project → Settings → Environment Variables. Add:

VITE_SUPABASE_URL

VITE_SUPABASE_ANON_KEY

VITE_API_BASE_URL = https://anchor-api.fly.dev

Critical: Only the anon key goes in frontend env. Never the service_role key. Vite exposes any VITE_-prefixed variable to the browser. Anything secret must NOT have the VITE_ prefix.

8.4 First Deploy

Trigger a deploy. Vercel assigns a URL like anchor-frontend.vercel.app. Open it. Expected: the login screen renders. If it errors, check the browser console for env var or CORS issues.

8.5 CORS

The Fly backend must accept requests from the Vercel domain. Update CORS config in the Express app:

const cors = require('cors');
app.use(cors({
  origin: [
    'https://anchor-frontend.vercel.app',
    'https://[final-domain]',
    'http://localhost:5173', // dev
  ],
  credentials: true,
}));

Redeploy the backend. Verify a request from the Vercel frontend reaches the Fly backend without CORS errors.

8.6 Custom Domain

After verifying the Vercel-assigned URL works:

Vercel project → Settings → Domains.

Add the production domain (e.g. app.anchor-domain.app).

Vercel shows DNS records to add. In Cloudflare (or whichever registrar), add the CNAME or A records as instructed.

Wait for DNS propagation (usually under 5 minutes; can be up to an hour).

Vercel auto-issues SSL via Let's Encrypt.

8.7 Backend Custom Domain (Optional)

Optional but cleaner: add a custom domain to Fly too (e.g. api.anchor-domain.app):

fly certs add api.anchor-domain.app

Add the DNS record Fly tells you to add. Update VITE_API_BASE_URL in Vercel to point at the custom domain. Redeploy.

9. Stage 6: Email (Resend Production Domain)

Goal: a verified production sender domain on Resend, with SPF, DKIM, and DMARC records, ready to send transactional email.

Critical: Do not enable EMAIL_OUTREACH_ENABLED until this stage is complete and a test email has successfully landed in inbox (not spam).

9.1 Add Domain to Resend

Resend dashboard → Domains → Add Domain.

Domain: anchor-domain.app (the apex, not a subdomain — Resend recommends apex for brand alignment).

Resend shows DNS records to add: typically 1-2 MX, 1 SPF (TXT), 1-3 DKIM (CNAME), 1 optional DMARC (TXT).

9.2 Add DNS Records

In the registrar's DNS panel:

SPF: a TXT record at the root, value v=spf1 include:_spf.resend.com ~all (or whatever Resend specifies). If an SPF record already exists, MERGE — only one SPF record per domain is allowed.

DKIM: CNAME records. Copy from Resend exactly. Order matters; copy the host and target as displayed.

DMARC (optional but recommended): TXT at _dmarc with value v=DMARC1; p=none; rua=mailto:postmaster@anchor-domain.app — start with p=none to monitor; tighten later.

MX (if Resend asks for them): only needed for inbound. Skip if not handling replies.

9.3 Wait for Verification

DNS propagation. Usually 5 minutes; can be up to a few hours. Resend's dashboard shows green checkmarks when records are detected. Don't proceed until all are green.

9.4 Update RESEND_FROM_EMAIL

On Fly:

fly secrets set RESEND_FROM_EMAIL="hello@anchor-domain.app"

Pick a from-address that's not 'noreply@'. For a recovery app, the email should feel human. 'hello@' or 'anchor@' is appropriate.

9.5 Send a Test Email

Trigger a manual send via the /api/email-status diagnostic or a temporary test endpoint. Send to a real inbox you control. Verify:

Email arrives.

Lands in inbox, not spam. If it lands in spam, check SPF/DKIM/DMARC alignment.

From-address shows the production domain.

Reply-to is correct (or absent — depends on whether replies are handled).

Body renders correctly. No broken images, no broken links.

9.6 Enable Outreach

fly secrets set EMAIL_OUTREACH_ENABLED="true"

Note: From this moment, the scheduler will send daily reminders, missed follow-ups, and weekly summaries to any user with email enabled in stable_profile. At launch, that's only the developer's account. Verify the schedule is sane before adding users.

10. Stage 7: Error Tracking (Sentry)

Goal: errors from both frontend and backend land in Sentry with enough context to debug.

10.1 Create Sentry Project

Sentry dashboard → Create Project.

Frontend: select 'React'. Note the DSN.

Backend: separate project. Select 'Node.js'. Note the second DSN.

10.2 Frontend SDK

npm install @sentry/react

// src/main.tsx
import * as Sentry from '@sentry/react';

Sentry.init({
  dsn: import.meta.env.VITE_SENTRY_DSN,
  environment: import.meta.env.MODE,
  tracesSampleRate: 0.1,
  // Recovery app: never capture user input or DOM content.
  beforeSend(event) {
    // Strip any 'extra' that might contain note text or memory content
    if (event.extra) delete event.extra;
    return event;
  },
});

Critical: For a recovery app, Sentry must NOT capture user content. No replay, no breadcrumbs that include input values, no extra context that includes memory or chat. Strip aggressively in beforeSend.

10.3 Backend SDK

npm install @sentry/node

// At the top of artifacts/api-server/src/index.js
const Sentry = require('@sentry/node');

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 0.1,
  beforeSend(event) {
    // Strip request body, which could contain notes / chat / memory.
    if (event.request) {
      delete event.request.data;
      delete event.request.headers; // headers contain JWT
    }
    return event;
  },
});

// Express integration:
app.use(Sentry.Handlers.requestHandler());
// ... routes ...
app.use(Sentry.Handlers.errorHandler());

10.4 Add Sentry Secrets

Vercel: VITE_SENTRY_DSN.

Fly: SENTRY_DSN.

10.5 Test

Throw a deliberate error in a non-critical route (e.g. /api/test-sentry that does throw new Error('sentry test')). Hit it. Verify the error appears in Sentry within ~30 seconds. Remove the test route.

11. Stage 8: Landing Page

Note: smoke test expansion is a Stage 11 prep task.

Goal: a one-page static site at the apex domain that explains what Anchor is and links to the app.

11.1 Approach

Separate Vercel project. Plain HTML or Astro or Next static site — whichever is fastest to build. The landing page is not the product. Keep it small.

11.2 Required Sections

Hero: name, one-line tagline, CTA button to the app.

What it does: 3-5 short paragraphs or a small feature list. Plain language. No jargon.

Why it exists: 2-3 paragraphs. The honest case for the product. Not marketing copy.

Crisis disclaimer: 'Anchor is not a substitute for professional care. If you are in crisis, call 988 (US) or your local emergency line.' Visible without scrolling, ideally near the CTA.

Privacy note: a short paragraph linking to the full privacy policy.

Footer: links to Privacy Policy, Terms of Service, contact email.

11.3 What to Skip

No testimonials at launch (no real users yet).

No pricing page (free at launch).

No blog.

No newsletter signup (yet).

No analytics tracker (no GA, no Plausible — see V4 master doc on analytics).

No social proof, no founder story, no investor pitch.

11.4 Domain Routing

Decide the structure:

Apex (anchor-domain.app) → landing page.

Subdomain (app.anchor-domain.app) → the actual Anchor app on Vercel.

This is the standard pattern. The apex is the marketing surface; the app lives at a subdomain. Configure DNS and Vercel domains accordingly.

12. Stage 9: Legal and Compliance

Goal: a privacy policy, terms of service, account deletion flow, and crisis disclaimer, all live before the first non-developer user sees the app.

12.1 Privacy Policy

Anchor handles sensitive mental health and recovery data. Privacy policy is not optional. For launch:

Use a generator (Termly, Iubenda, or similar) as a starting draft.

Customize for the actual data Anchor collects: check-in data, chat messages, voice transcripts (transient), memory facts, email, sober contact info. Be specific.

Note explicitly: data is stored on US servers (Neon, Fly, Supabase, Vercel), encrypted in transit and at rest.

Note explicitly: data is not sold, not shared with third parties, except OpenAI for AI processing (and OpenAI is configured to not train on API data — verify this is still true at launch and link to OpenAI's data usage policy).

Note explicitly: the user can request data export and account deletion at any time.

Disclose Sentry (error tracking) and Resend (email delivery) as data processors.

Before any public marketing or external user beyond invite-only, have a lawyer review. Generated docs are acceptable for closed alpha and TestFlight.

12.2 Terms of Service

Standard ToS plus mental-health-specific clauses:

Anchor is a wellness tool, not medical care.

Anchor does not diagnose, treat, or cure any condition.

If experiencing crisis, the user must contact emergency services.

AI responses are generated and may be wrong; do not rely on them for safety decisions.

User is responsible for their own safety planning and human support network.

Limitation of liability: Anchor and Eagle Rocket LLC are not liable for outcomes related to recovery, mental health, or use of the AI features.

12.3 Account Deletion

Required by law in most jurisdictions (GDPR, CCPA). Build:

A Settings → Delete Account button.

Confirmation flow: type the word 'delete' and confirm.

On confirmation: cascade delete from user_memory, app_settings, commitments, chat_sessions, check_ins, sobriety_trackers, tracker_resets — every table with a user_id column.

Also delete the Supabase Auth user via the admin API.

Show a final confirmation: 'Your account has been deleted.' Log out.

Add a Playwright test that exercises this flow end-to-end.

12.4 Data Export

Less urgent than deletion but a strong trust signal. A simple JSON export of all user data is sufficient for launch:

Settings → Export My Data.

Server-side: gather all rows for user_id across all tables, return as JSON.

Client downloads as anchor-export-YYYY-MM-DD.json.

If launch timing is tight, this can be deferred to V4.1 — but no later.

12.5 Crisis Disclaimer Visibility

The 988 disclaimer must be:

On the landing page, near the hero.

On the login screen.

In the onboarding flow.

Inside the app's About / Help section.

In every crisis routing card (already built — verify wording is consistent).

13. Stage 10: First Real Account

Goal: a real production account belonging to the developer, exercising the full app on real infrastructure.

13.1 Switch Backend to Production Database

Up to this point, Fly has been pointing at the Neon staging branch. Switch to the main branch:

fly secrets set DATABASE_URL="postgres://...neon-main..."

Fly auto-redeploys. Verify health endpoint still returns 200.

13.2 Confirm Database Is Empty

psql "postgres://...neon-main..." -c "SELECT COUNT(*) FROM user_memory;"

Should return 0. If it returns anything else, stop and investigate before continuing.

13.3 Sign Up

Open the production frontend URL.

Click sign in / sign up.

Use a real email address — the one that will be the developer's primary account from now on.

Complete magic link or OAuth flow.

Land on the home screen. Should be empty / fresh-install state.

13.4 Complete Onboarding

Run through the full 9-step sponsor intake onboarding. Choose real values. This data is the developer's actual recovery data going forward.

Verify after onboarding:

stable_profile is populated correctly in the database.

Recovery program selection wrote both primary and specific.

Sobriety start dates wrote correctly.

Email field matches the auth email (or is set explicitly if different).

Timezone and reminder time are correct.

13.5 Do a Real Check-In

A complete check-in. Verify:

Check-in saves.

AI response generates without error.

If a commitment was offered, it appears on Home.

Memory event_log shows the new entry.

Sentry shows no errors.

14. Stage 11: Smoke Test in Production

Goal: confirm every core surface works in production before considering go-live complete.

Manual smoke pass. Treat each as a hand-checked test against the production URL with the developer's real account. Write notes if anything is off.

14.1 Auth

Sign out works.

Sign in works (magic link delivered via Resend).

Refresh on a protected page does not log out.

JWT expiry is handled gracefully (refresh token works).

14.2 Home

Loads.

Shows correct sober time.

Shows pending commitment if one exists.

Quick action buttons all route correctly.

14.3 Check-In

Full check-in flow completes.

Voice input works.

AI summary generates.

TTS plays on user tap (does not autoplay).

Chat with my coach button carries context to chat.

14.4 Chat

Send a normal message; receive a response.

Send a crisis message (e.g. 'I want to hurt myself'); crisis card fires; normal AI response is suppressed.

Send a moderate distress message; handoff banner appears.

Commitment offer fires once per session, no repeat.

Mode detection silent (mode never named to user).

Banned phrases never appear in output.

14.5 Memory

All stable_profile fields render.

Inline edit works for every editable field.

Recovery program picker works (primary + specific).

Sober contact CRUD works.

Meeting links CRUD works (5-field structured form).

Recent Patterns displays 3 sections (or insufficient-data fallback).

Memory pause toggle works.

Reset memory works (with typed confirmation).

14.6 Trackers

Trackers home page renders without scroll bar issue.

Tracker reset flow works.

Calendar heatmap renders.

14.7 Find a Meeting

Routes to correct URL based on recovery program.

Multi-program picker shows when specific has multiple entries.

Fallback to aa-intergroup.org works for empty/unknown programs.

Opens in new tab.

14.8 Email

Daily reminder email arrives at scheduled time.

Lands in inbox (not spam).

Renders correctly on iOS Mail and Gmail web.

Unsubscribe / disable in settings works.

14.9 Settings

Theme picker works for all 6 themes.

Theme preference persists across reloads.

Account deletion flow works (test with a throwaway second account, not the real one).

Data export works (if shipped).

14.10 Observability

Fly logs show no errors during the smoke pass.

Sentry shows no errors during the smoke pass.

Neon shows reasonable query volume, no slow queries.

15. Go / No-Go Checklist

Before declaring V3 production-live, every item below must be true.

Infrastructure

Domain registered and DNS propagated.

Vercel frontend deployed and reachable at production domain.

Fly backend deployed and reachable.

Neon production database live.

Supabase Auth live with at least magic link enabled.

Resend production domain verified (SPF, DKIM green).

Sentry frontend and backend projects live, errors flowing.

Code

All 111 smoke tests pass against production (or at minimum staging).

Cross-user isolation tests pass.

No hardcoded user IDs anywhere in the codebase.

authMiddleware on every protected route.

Phone numbers never enter AI prompts (re-verify in production).

Compliance

Privacy policy live at /privacy.

Terms of service live at /terms.

Account deletion flow works end-to-end.

Crisis disclaimer visible on landing, login, onboarding, app.

Personal

Developer's real production account created.

Real onboarding completed.

First real check-in completed.

First real chat session completed.

First daily reminder email received and verified.

Decision: If every box above is checked: go-live. Update the V4 master doc to reflect the production URL. Begin Phase 3 (real usage and signal gathering) per the V4 master doc.

Decision: If any box is unchecked: do not declare go-live. Fix it. Re-run the affected smoke tests. Then re-evaluate.

16. Rollback Plan

Things will break. The plan for when they do.

16.1 Frontend Rollback

Vercel keeps every deploy. To revert:

Vercel dashboard → Deployments.

Find the last known-good deploy.

Click 'Promote to Production'.

Production is restored within ~30 seconds.

16.2 Backend Rollback

Fly keeps a deploy history:

fly releases
fly deploy --image registry.fly.io/anchor-api:deployment-XYZ

Or simply redeploy from the last known-good git commit.

16.3 Database Rollback

Neon supports point-in-time restore on paid tiers. On the free tier, the safest pattern is:

Take a manual pg_dump backup before any schema change.

If a schema change breaks production, restore from the dump into a new Neon branch and point Fly at the new branch.

16.4 Auth Rollback

Supabase Auth is largely stateless from the app's perspective. The only rollback risk is if the JWT secret rotates — which it shouldn't. If a rollback of Supabase config is needed, it's done via the Supabase dashboard (manual).

16.5 Communication During an Incident

At launch, the only user is the developer. No external comms needed. As beta users join, add a status mechanism (a simple status.anchor-domain.app static page is sufficient — manually edited).

17. Post-Launch First Week

The week after go-live is observation, not building.

17.1 Daily Habits

Use Anchor every day. Real check-ins. Real chat. Real commitments.

Check Sentry every morning. Triage any errors. Most will be benign; capture the ones that aren't.

Check Fly logs once per day. Look for 500s, slow queries, cron failures.

Check Resend dashboard once per day. Verify scheduled emails actually sent and were not bounced.

17.2 What to Capture

Anything that breaks.

Anything that's slow.

Anything that's confusing.

Anything that's missing.

Anything that surprises in a good way.

Capture in a notes file or voice memo. Do not act on every observation. The point of Phase 3 (per V4 master doc) is to listen for a month before deciding what to build next.

17.3 What Not to Do

Do not add new features.

Do not refactor.

Do not invite users beyond the developer in week 1.

Do not show the app on social media. (See V4 doctrine on engagement optimization.)

Do not adjust the AI prompts unless something is broken.

17.4 Allowed Changes in Week 1

Hot fixes for actual bugs.

Copy fixes for actual typos.

Configuration changes (cron timing, scheduler windows, error sampling rates).

Sentry filter adjustments to reduce noise.

18. Cost Expectations

Approximate monthly cost at launch with one user (the developer). All figures are rough. Verify against current pricing pages at launch time.

Free or Near-Free

Vercel: $0 (Hobby tier).

Neon: $0 (Free tier, ~0.5 GB storage).

Supabase: $0 (Free tier, up to 50K monthly active users).

Sentry: $0 (Developer tier).

GitHub: $0 (private repo on free tier).

Domain: ~$10-15 per year (Cloudflare or Namecheap, .app or .com).

Paid

Fly.io: ~$2-5 per month for a small always-on machine. Single shared-cpu-1x with 256MB RAM is enough for one user.

Resend: $0 for first 3,000 emails per month, then $20 for 50,000. Anchor at one user is well under the free tier.

OpenAI API: variable. At one active user with a few check-ins per day plus occasional chat: roughly $5-15 per month at gpt-4o-mini and tts-1 pricing.

Total Estimate

Roughly $10-25 per month at one user. Domain is $10-15 per year on top. As beta users join, the dominant variable cost is OpenAI usage. Email and database stay negligible until volume grows substantially.

Cost Watch

Set billing alerts on:

OpenAI: alert at $50/month (well above expected).

Fly: alert at $20/month.

Resend: alert at any paid usage (means crossing the free tier).

19. Common Traps and Gotchas

19.1 Auth

Magic links going to spam: SPF/DKIM not verified yet. Fix DNS before relying on auth emails. As a workaround during setup, use an OAuth provider that doesn't depend on email delivery.

JWT expires mid-session: refresh tokens must be configured. Supabase handles this client-side if the SDK is set up correctly. Verify by leaving the app idle for an hour and seeing if the next request still works.

CORS errors after deploy: backend's CORS origin list does not include the Vercel preview URL. Either add specific domains or use a regex matcher.

Service role key leaked into frontend: anything prefixed with VITE_ in env files is exposed to the browser. Service role key must NEVER have VITE_ prefix.

19.2 Database

Neon connection limits: free tier has a low concurrent connection cap. Use connection pooling (Neon provides a pooled connection string — use it).

SSL required: Neon requires sslmode=require. If the connection string drops it, queries fail.

Cold start: Neon scales to zero on free tier. First query after idle takes ~1-2 seconds. Acceptable for low traffic; budget for it in tests.

19.3 Email

Multiple SPF records: only one SPF record is allowed per domain. If an existing one exists, MERGE the includes, do not add a second record.

DKIM CNAME at apex: most registrars don't allow CNAME at apex. Resend's DKIM records are usually subdomain-scoped (e.g. resend._domainkey.anchor-domain.app), so this is rarely an issue. But verify.

DMARC too strict at launch: starting with p=reject can cause legitimate email to bounce. Start with p=none, monitor for a few weeks, then tighten.

19.4 Fly.io

Machine sleeps: by default Fly machines auto-stop after a period of inactivity. Cron will not fire while sleeping. Set min_machines_running = 1 for the API.

Region mismatch with Neon: cross-region latency adds 50-100ms per query. Pin Fly and Neon to the same region.

Health check fail loop: if the / route doesn't return 200, Fly will restart the machine in a loop. Verify health endpoint behavior before deploy.

19.5 Vercel

Build env vars vs runtime env vars: VITE_-prefixed vars are baked into the build. If they change, redeploy. Edge functions can read non-VITE secrets at runtime.

Wildcard subdomain SSL: if using app.* subdomain, Vercel's auto-SSL covers it. Custom wildcard certs are not needed.

19.6 OpenAI

Rate limits: gpt-4o-mini has high limits but they exist. Add retry-with-backoff to chat and check-in response generators.

Whisper file size: 25MB max. Voice input cap of 60 seconds is well under, but verify.

Privacy: ensure API usage is set to 'do not train on data' in OpenAI dashboard. This is the default for API usage but verify.

19.7 Sentry

Capturing user content: Sentry by default captures request bodies, breadcrumbs, and console output. For a recovery app this is a privacy violation. Strip aggressively in beforeSend.

Sample rate too high: 100% trace sampling on a free tier blows through the quota fast. 10% is a safer starting point.

20. Appendix A: Environment Variable Reference

Backend (Fly Secrets)

DATABASE_URL — Neon Postgres connection string (production).

SUPABASE_URL — Supabase project URL.

SUPABASE_JWT_SECRET — Used to verify JWTs server-side.

SUPABASE_SERVICE_ROLE_KEY — Used for admin operations (e.g. deleting an auth user during account deletion). Never expose.

OPENAI_API_KEY — OpenAI API key.

OPENAI_TTS_MODEL — Default 'tts-1'.

OPENAI_TTS_VOICE — Default 'onyx'.

RESEND_API_KEY — Resend API key.

RESEND_FROM_EMAIL — Production sender address.

EMAIL_OUTREACH_ENABLED — 'true' to enable scheduled sends. Default 'false'.

SENTRY_DSN — Backend Sentry DSN.

NODE_ENV — 'production' on Fly.

Frontend (Vercel)

VITE_SUPABASE_URL — Supabase project URL (public).

VITE_SUPABASE_ANON_KEY — Supabase anon key (public).

VITE_API_BASE_URL — Backend URL (e.g. https://anchor-api.fly.dev or https://api.anchor-domain.app).

VITE_SENTRY_DSN — Frontend Sentry DSN.

Local Dev (.env, not committed)

All of the above with dev-tier values.

APP_USER_ID = 'dev_user' — kept as a fallback for local dev, gated by NODE_ENV !== 'production'.

21. Appendix B: Useful Commands

Fly

fly logs                    # tail logs
fly status                  # current status
fly secrets list            # list secret keys (not values)
fly secrets set KEY=VALUE   # set a secret
fly deploy                  # deploy current branch
fly releases                # deploy history
fly ssh console             # shell into a running machine

Neon

psql "postgres://..." -c "\dt"          # list tables
psql "postgres://..." -c "\d table_name" # describe a table
pg_dump "postgres://..." > backup.sql    # backup
psql "postgres://..." < backup.sql       # restore

Vercel

vercel              # deploy current dir to preview
vercel --prod       # promote to production
vercel logs <url>   # logs for a deployment
vercel env ls       # list env vars

Quick health checks

# Backend health
curl https://api.anchor-domain.app/health

# Frontend reachable
curl -I https://app.anchor-domain.app

# Auth flow (manual, browser)
# Open app, sign in, verify magic link arrives

# Email scheduler diagnostic (after auth)
curl -H "Authorization: Bearer $JWT" \
     https://api.anchor-domain.app/api/email-status

Smoke test against production

cd anchor-frontend
PLAYWRIGHT_BASE_URL=https://app.anchor-domain.app \
  npx playwright test tests/e2e/anchor-smoke.spec.ts

— end —
