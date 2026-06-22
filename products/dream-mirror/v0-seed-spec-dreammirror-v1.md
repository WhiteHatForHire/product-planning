---
title: "V0 SEED SPEC DreamMirror v1"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Dream Mirror /Specs/V0_SEED_SPEC_DreamMirror_v1.md"
status: active
privacy: private/internal
tags:
  - product
---

# V0 SEED SPEC DreamMirror v1

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
# DreamMirror V0 Build Seed Spec

**Phase:** V0 — prove the behavioral loop  
**Target users:** ~50 beta users  
**Deploy target:** Vercel (frontend) + Fly.io (backend) + Supabase (database/auth)  
**Stack:** React + Vite + TypeScript + Tailwind + Shadcn UI / Express + TypeScript / Supabase Postgres + RLS  
**Document version:** 1.0

---

## V0 Success Definition

Users capture at least 3 dreams, read the analysis output, and return because the system helped them notice something meaningful.

The loop: **wake → capture → reflect → save → notice pattern → return.**

V0 is not about features. V0 is about whether this loop creates return behavior.

---

## Instrumented Events (Required from First Deploy)

Log all of these from day one:

```
capture_started
dream_saved
checkin_completed
analysis_requested
analysis_generated
analysis_saved
analysis_viewed
session_cta_clicked
export_requested
delete_requested
return_after_3_days
return_after_7_days
```

---

## Database Schema

All schema migrations are explicit SQL files in `/supabase/migrations/`. Do not use Supabase Studio drag-and-drop for schema changes. Do not use auto-generated migration files without review.

RLS must be enabled on every user data table before any user-facing feature is deployed against it.

### Users (managed by Supabase Auth)
Supabase Auth handles the `auth.users` table. Extend with a `profiles` table.

```sql
CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  display_name TEXT,
  timezone TEXT,
  dream_goal TEXT,            -- user's stated reason for using the app
  onboarding_completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own profile"
  ON profiles FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users can update own profile"
  ON profiles FOR UPDATE USING (auth.uid() = id);
```

### Dreams

```sql
CREATE TABLE dreams (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  dream_date DATE NOT NULL,                -- the date the dream occurred (not entry date)
  title TEXT,                              -- optional, user-set or AI-suggested
  raw_text TEXT NOT NULL,                  -- user's exact words, immutable after save
  clean_text TEXT,                         -- narrative reconstruction from Narrative Agent
  source_type TEXT CHECK (source_type IN ('voice', 'text')),
  privacy_level TEXT DEFAULT 'private' CHECK (privacy_level IN ('private', 'session_shared')),
  is_deleted BOOLEAN DEFAULT FALSE,        -- soft delete
  deleted_at TIMESTAMPTZ
);

ALTER TABLE dreams ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own dreams"
  ON dreams FOR SELECT USING (auth.uid() = user_id AND is_deleted = FALSE);

CREATE POLICY "Users can insert own dreams"
  ON dreams FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own dreams"
  ON dreams FOR UPDATE USING (auth.uid() = user_id);
```

### Dream Emotions

```sql
CREATE TABLE dream_emotions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  dream_id UUID NOT NULL REFERENCES dreams(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  emotion_label TEXT NOT NULL,
  intensity INTEGER CHECK (intensity BETWEEN 1 AND 10),
  waking_feeling TEXT,                     -- how they felt after waking
  life_context_note TEXT,                  -- "what in your current life feels similar?"
  user_confirmed BOOLEAN DEFAULT FALSE,    -- did user review/edit this emotion data?
  created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE dream_emotions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own emotions"
  ON dream_emotions FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own emotions"
  ON dream_emotions FOR INSERT WITH CHECK (auth.uid() = user_id);
```

### Dream Symbols

```sql
CREATE TABLE dream_symbols (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  dream_id UUID NOT NULL REFERENCES dreams(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  symbol_label TEXT NOT NULL,
  category TEXT,                           -- person / place / object / movement / nature / animal / motif
  possible_meanings JSONB,                 -- array of contextual meaning strings
  emotional_relevance TEXT,
  user_confirmed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE dream_symbols ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own symbols"
  ON dream_symbols FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own symbols"
  ON dream_symbols FOR INSERT WITH CHECK (auth.uid() = user_id);
```

### Analyses

```sql
CREATE TABLE analyses (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  dream_id UUID NOT NULL REFERENCES dreams(id) ON DELETE CASCADE,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  model_version TEXT NOT NULL,             -- e.g., "claude-sonnet-4-20250514"
  prompt_version TEXT NOT NULL,            -- e.g., "prompt_v1.0"
  summary TEXT,
  emotional_themes TEXT,
  symbol_map JSONB,
  life_mirror TEXT,
  pattern_note TEXT,
  integration TEXT,                        -- the closing question or action
  care_note TEXT,                          -- populated if Safety Agent flagged crisis-adjacent content
  output_json JSONB NOT NULL,             -- full structured output from pipeline
  safety_flags JSONB DEFAULT '{}',        -- e.g., {"crisis_adjacent": true}
  token_cost_by_stage JSONB NOT NULL,     -- e.g., [{"stage": "narrative", "model": "...", "input_tokens": 120, "output_tokens": 80}]
  user_found_accurate BOOLEAN,            -- user feedback: did this feel right?
  is_cached BOOLEAN DEFAULT FALSE         -- served from cache vs. freshly generated
);

ALTER TABLE analyses ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own analyses"
  ON analyses FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own analyses"
  ON analyses FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own analyses"
  ON analyses FOR UPDATE USING (auth.uid() = user_id);
```

### User Pattern Summaries

```sql
CREATE TABLE user_pattern_summaries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  period_start DATE NOT NULL,
  period_end DATE NOT NULL,
  dream_count INTEGER DEFAULT 0,
  recurring_symbols JSONB,                -- [{"label": "water", "count": 4}, ...]
  recurring_emotions JSONB,               -- [{"label": "anxiety", "count": 3}, ...]
  recurring_life_themes JSONB,            -- [{"theme": "transition", "count": 3}, ...]
  generated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE user_pattern_summaries ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own pattern summaries"
  ON user_pattern_summaries FOR SELECT USING (auth.uid() = user_id);
```

### App Settings

```sql
CREATE TABLE app_settings (
  user_id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email_notifications BOOLEAN DEFAULT FALSE,
  weekly_summary_enabled BOOLEAN DEFAULT FALSE,
  data_export_requested BOOLEAN DEFAULT FALSE,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

ALTER TABLE app_settings ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can read own settings"
  ON app_settings FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can update own settings"
  ON app_settings FOR UPDATE USING (auth.uid() = user_id);
```

---

## Screen Inventory and Build Spec

### 1. Landing / Orientation

**Purpose:** Explain the product quickly and set the right expectations.  
**Required elements:**
- One-line product promise (reflective, not predictive)
- Short method description (Yuni Method — no jargon)
- Privacy note (your dream data is private and yours to delete)
- CTA: "Record my first dream"
- Secondary CTA: "Book a session with Yuni" (external link)

**Success test:** User understands this is reflective, not predictive, before they register.  
**Legal requirement:** Short disclaimer visible on this page.

---

### 2. Onboarding Lite

**Purpose:** Collect minimum context to personalize the first analysis.  
**Required elements:**
- Display name (for personalization)
- Timezone (for dream date accuracy)
- Dream goal: why they are here (free text or 3–4 options)
- Optional: current life context note ("Is anything significant happening in your life right now?")
- CTA: "Start recording"

**Success test:** User can complete onboarding in under 60 seconds.  
**Builder note:** Do not gate onboarding with email verification before first dream capture. Capture first, verify after.

---

### 3. Dream Capture

**Purpose:** Core wedge. User records the dream before it fades.  
**Required elements:**
- Voice input (browser MediaRecorder API, transcribed server-side)
- Text input (fallback and alternative)
- Save draft (auto-save every 30 seconds minimum)
- Timestamp (auto-set to now; user can adjust date)
- Dream title (optional — can be AI-suggested after save)
- CTA: "Save and reflect"

**Success test:** User records a dream and saves it. The raw text is stored immutably.  
**Builder note:** Do not run the AI pipeline at capture time. Capture first, analyze on explicit user request.

---

### 4. Emotional Check-In

**Purpose:** Collect the emotional data that makes analysis personal.  
**Required elements:**
- Mood tags (multi-select from common dream emotions: peaceful, anxious, confused, sad, joyful, scared, neutral, strange, other)
- Intensity slider (1–10)
- Waking feeling: "How did you feel when you woke up?" (free text, short)
- Life context: "What in your current life feels similar to this dream?" (free text, optional but encouraged)
- CTA: "Generate my reflection"

**Success test:** AI output explicitly references the user's emotional check-in data. If it does not, the pipeline is broken.

---

### 5. Analysis Result

**Purpose:** The wow moment. Deliver the Yuni Method output.  
**Required elements (in this order):**
- Care note (if Safety Agent flagged crisis-adjacent content — appears first)
- Dream Summary (clean narrative reconstruction)
- Emotional Themes
- Symbol Map (symbols as possibilities, not facts)
- Life Mirror (connection to waking life)
- Recurring Pattern (or "watch for" if insufficient history)
- Question for Reflection (the closing integration)
- Optional Gentle Closing (poetic line if the emotional tone calls for it)
- User feedback: "Did this feel right?" (thumb up / thumb down — stored in analyses table)
- CTA: "Save to journal" / "Book a session with Yuni"

**Success test:** User says the output felt specific and grounded, not generic.  
**Builder note:** The analysis must not feel like a wall of text. Use clear visual hierarchy between sections. Generous whitespace.

---

### 6. Dream Detail / Journal

**Purpose:** Store and revisit past dreams and analyses.  
**Required elements:**
- Dream list (chronological, most recent first)
- Each entry: date, title or first line, emotional tone indicator
- On tap: full dream detail view (raw text, clean narrative, full analysis, date)
- Edit (dream title only — raw text is immutable)
- Soft delete with confirmation

**Success test:** User can find a dream from last week in under 10 seconds.

---

### 7. Pattern Dashboard (Lite)

**Purpose:** Show value beyond a single dream.  
**Required elements:**
- Total dream count
- Top 3 recurring symbols (with count)
- Top 3 recurring emotions (with count)
- Recent themes (from pattern summaries)
- Note: "Patterns become clearer with more dreams" if fewer than 5 recorded

**Success test:** Even with 3 dreams, user sees the beginning of trend data.  
**Builder note:** Do not show a blank dashboard. Show the "collecting" state with encouragement.

---

### 8. Book with Yuni

**Purpose:** Connect the product to revenue. Bridge from AI reflection to human session.  
**Required elements:**
- Short Yuni introduction (method, positioning — not therapist)
- Session types with descriptions and price range
- Booking CTA (external calendar or inquiry link — not in-app payment in V0)
- Session disclaimer visible on this page

**Success test:** User can reach Yuni's booking page in two taps.

---

### 9. Settings / Legal

**Purpose:** Protect user trust and data rights.  
**Required elements:**
- Export all my data (JSON or CSV — required before beta launch)
- Delete my account (with confirmation — soft delete, with 30-day hard delete)
- Privacy policy link
- Full disclaimer
- Contact / feedback link
- Notification preferences

**Success test:** User can export their data and delete their account without contacting support.  
**Legal requirement:** Data export and delete must be functional before any real user is onboarded.

---

## AI Pipeline Technical Requirements

### Cost Controls

- Cache all analysis results. Serve from cache on re-open. Only regenerate on explicit user request.
- Use cheaper/faster models for extraction stages (Narrative, Emotion, Symbol, Pattern).
- Reserve stronger model calls for synthesis stages (Life Mirror, Coach, Safety).
- Log token count per stage on every run. Structure: `{ stage: string, model: string, input_tokens: number, output_tokens: number }`.
- Do not send the user's full dream history into every prompt. Summarize prior dreams into a pattern object and pass that instead.

### Pipeline Execution

- All AI calls server-side (Express backend).
- No client-side model calls. No API keys in the browser.
- Safety Agent runs last, before any output is returned to the client.
- Store full `output_json` from the pipeline on every Analysis record.

### Error Handling

- If any pipeline stage fails, do not return a partial analysis to the user. Return a fallback message (see Prompt Library — Fallback) and log the failure.
- Do not expose error details to the user. Log internally.

---

## What Is Explicitly Out of V0 Scope

Do not build, stub, or scaffold:

- Native iOS / Android app
- Social features / shared feeds
- Stripe in-app payments
- Therapist marketplace
- Multilingual support
- GraphQL
- Push notifications (beyond email — and email is optional in V0)
- Any feature not in the screen inventory above

---

## V0 Completion Criteria

V0 is complete when:

1. All 9 screens are deployed and functional on the production URL
2. RLS is verified on all user data tables
3. Data export and delete are functional
4. Token cost logging is in place and verified on a test analysis run
5. Safety Agent has been manually tested with a crisis-adjacent dream input
6. Minimum disclaimer copy is live on landing, analysis result, and settings pages
7. At least one real user has completed the full loop: capture → check-in → analysis → save
