---
title: "DIRECTIVE M5c Fragment Bundling Fix"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/Old/DIRECTIVE_ M5c Fragment Bundling Fix.docx"
status: archive
privacy: working
tags:
  - product
  - archive
---

# DIRECTIVE M5c Fragment Bundling Fix

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
DIRECTIVE: M5c Fragment Bundling Fix (v2)

Apply AUTONOMY_LAYER.md (Anchor edition v1.1, repo root) before executing. Doctrine, playbook, phase protocol, deferred-issues format, BUILD_REPORT format, and hard stops all live there. Do not duplicate them in this directive.

Header

Surfaces:          artifacts/api-server/build.mjs

artifacts/api-server/src/lib/prompts/composeFromRows.ts

artifacts/api-server/tests/unit/composeFromRows.test.ts (new)

Production impact: API change (program-aware AI starts working in prod)

Council of Models: no

Auto-merge:        no

Credentials:       gh, pnpm

Agent:             CC Cloud

Why Auto-merge: no — Playwright CI (PR #43) is not yet merged. No required CI status checks exist. Auto-merge with no checks would fire immediately, defeating the gate. Marcus reviews and merges this PR.

Current state

Branch fix/m5c-fragment-bundling already exists at 4254a36. Working files (ISSUE_EXECUTION_PLAN.md, AUTONOMOUS_RUN_LOG.md) already created and committed. No code changes yet. Begin at Phase A pre-flight. Do not re-cut the branch.

Role

You are the implementation agent for the M5c fragment bundling fix. The 35 prompt fragment .txt files exist in source but are silently absent from the production bundle. Every user gets the static base prompt instead of their program-aware fragment. Make the bundle include the fragments, fix path resolution at runtime, add observable failure logging so this category of silent failure never ships again. Open a PR and stop.

Stack

See AUTONOMY_LAYER.md section 0.1.

Background (read once, do not paraphrase)

May 10 diagnostic confirmed:

composeFromRows.ts resolves fragments dir via fileURLToPath(import.meta.url) dirname

esbuild bundles src/index.ts into /app/dist/index.mjs — non-JS assets not copied

/app/dist/fragments/ does not exist in production

Every loadFragment() call returns null silently

composeFromRows returns "" — chat.ts falls through to static CHAT_SYSTEM_PROMPT

Zero log lines surface this failure

Fragments are correct. Compose logic is correct. Only bundling and observability are wrong. This is the ANCHOR-3 fix.

Deployment posture

PR-only. Auto-merge: no. Marcus reviews and merges.

CD redeploys api-server on merge (touches artifacts/api-server/ and build.mjs). No migration. No Fly secrets. No Vercel env changes.

Known deviations from prior directive version

Pre-flight confirmed these corrections — apply everywhere:

Old assumption

Actual

Correction

Vitest

node:test

Use import { test, mock } from "node:test" + import assert from "node:assert/strict"

vi.spyOn(console, "warn")

node:test mock API

mock.method(console, "warn", () => {})

src/lib/prompts/__tests__/

runner scans tests/unit/ only

Place test at artifacts/api-server/tests/unit/composeFromRows.test.ts

pnpm -F api-server test

script is test:unit

Run pnpm -F api-server test:unit

File structure

Modified:

artifacts/api-server/build.mjs

artifacts/api-server/src/lib/prompts/composeFromRows.ts

New:

artifacts/api-server/tests/unit/composeFromRows.test.ts

Deleted: none.

Design data

build.mjs — copy step

Add this function and call it immediately after the esbuild call resolves. Do not change the esbuild config. No new dependencies — node:fs/promises is stdlib.

import { cp, mkdir } from "node:fs/promises";

async function copyPromptAssets() {

const srcDir = "src/lib/prompts";

const destDir = "dist/lib/prompts";

await mkdir(destDir, { recursive: true });

await cp(srcDir, destDir, {

recursive: true,

filter: (src) => {

if (src.includes("__tests__") || src.includes("__test_prompts__")) return false;

if (src.endsWith(".ts") || src.endsWith(".tsx")) return false;

return true;

},

});

console.log(`[build] Copied prompt assets: ${srcDir} → ${destDir}`);

}

// Call after esbuild resolves:

await copyPromptAssets();

composeFromRows.ts — path resolution

Replace current path constants with:

import { statSync } from "node:fs";

const __dirname = dirname(fileURLToPath(import.meta.url));

// Bundled prod: __dirname === /app/dist, assets at /app/dist/lib/prompts/

// Dev/test: __dirname === src/lib/prompts (colocated)

function resolvePromptsDir(): string {

const bundledPath = join(__dirname, "lib", "prompts");

try {

statSync(join(bundledPath, "default.txt"));

return bundledPath;

} catch {

return __dirname;

}

}

const PROMPTS_DIR = resolvePromptsDir();

const FRAGMENTS_DIR = join(PROMPTS_DIR, "fragments");

console.log(JSON.stringify({

event: "compose_from_rows_init",

prompts_dir: PROMPTS_DIR,

fragments_dir: FRAGMENTS_DIR,

}));

composeFromRows.ts — loadFragment with miss logging

function loadFragment(slug: string): string | null {

const filePath = join(FRAGMENTS_DIR, `${slug}.txt`);

try {

return readFileSync(filePath, "utf-8");

} catch (err) {

console.warn(JSON.stringify({

event: "fragment_load_miss",

slug,

attempted_path: filePath,

error_code: (err as NodeJS.ErrnoException).code,

}));

return null;

}

}

composeFromRows.ts — empty result logging

Add before return "" when all parts are null/empty:

if (parts.length === 0) {

console.warn(JSON.stringify({

event: "compose_from_rows_empty",

reason: "all_fragments_missed_or_no_rows",

row_count: rows.length,

row_slugs: rows.map(r => r.slug),

}));

return "";

}

Do NOT log user content, prompt content, or message text. Slug names and paths only.

Unit tests — tests/unit/composeFromRows.test.ts

Use node:test and node:assert/strict. Match import patterns from tests/unit/composeSystemPrompt.test.ts.

Read the actual exports from composeFromRows.ts before writing — match exact function names.

import { test, mock } from "node:test";

import assert from "node:assert/strict";

// Adjust import path to match actual compiled output location

import { loadFragment, composeFromRows } from "../../src/lib/prompts/composeFromRows.js";

test("loadFragment returns content for existing slug", () => {

const result = loadFragment("default");

assert.ok(result !== null && result.length > 0, "expected non-empty string for default slug");

});

test("loadFragment returns null and logs fragment_load_miss for missing slug", () => {

const warnCalls: unknown[][] = [];

mock.method(console, "warn", (...args: unknown[]) => {

warnCalls.push(args);

});

const result = loadFragment("bogus-slug-xyz-does-not-exist");

assert.equal(result, null);

const logged = warnCalls.some(args =>

JSON.stringify(args).includes("fragment_load_miss") &&

JSON.stringify(args).includes("bogus-slug-xyz-does-not-exist")

);

assert.ok(logged, "expected fragment_load_miss warn log for missing slug");

});

test("composeFromRows returns non-empty string for valid rows", () => {

const result = composeFromRows([{ slug: "default", category: "no-program", is_primary: true }]);

assert.ok(result !== null && result.length > 0, "expected non-empty composed prompt");

});

test("composeFromRows returns empty string and logs compose_from_rows_empty when all fragments miss", () => {

const warnCalls: unknown[][] = [];

mock.method(console, "warn", (...args: unknown[]) => {

warnCalls.push(args);

});

const result = composeFromRows([{ slug: "nonexistent-slug-xyz", category: "no-program", is_primary: true }]);

assert.equal(result, "");

const logged = warnCalls.some(args =>

JSON.stringify(args).includes("compose_from_rows_empty")

);

assert.ok(logged, "expected compose_from_rows_empty warn log");

});

If direct import fails (module resolution issues with the compiled path), check how composeSystemPrompt.test.ts imports its target and match that pattern exactly.

Working files (AUTONOMY_LAYER.md section 0.4)

Already created on this branch. Append to AUTONOMOUS_RUN_LOG.md throughout. Update ISSUE_EXECUTION_PLAN.md as phases complete.

Phase plan

Every phase: pre-flight → smoke-first → implement → health check → commit.

Phase A — Build step copies prompt assets

Goal: pnpm -F api-server build produces dist/lib/prompts/ with all .txt assets.

Pre-flight:

git status          # must be clean

git log --oneline -3  # confirm at 4254a36

pnpm install --frozen-lockfile

pnpm -F api-server build  # baseline — record that dist/lib/prompts/ does NOT exist

Smoke (write first, run, expect red):

Write a Node check script (inline or as a temp file, deleted after) that asserts:

import { existsSync } from "node:fs";

const checks = [

"artifacts/api-server/dist/lib/prompts/fragments/default.txt",

"artifacts/api-server/dist/lib/prompts/fragments/virtue-ethics.txt",

"artifacts/api-server/dist/lib/prompts/safety-override.txt",

"artifacts/api-server/dist/lib/prompts/crisis-classifier.txt",

];

let failed = false;

for (const f of checks) {

if (!existsSync(f)) { console.error(`MISSING: ${f}`); failed = true; }

else { console.log(`OK: ${f}`); }

}

if (failed) process.exit(1);

console.log("All smoke checks passed.");

Run it. Expect red (files missing). Do not proceed until red is confirmed.

Implementation:

Read current build.mjs.

Add copyPromptAssets function per design data above.

Call it after esbuild resolves.

Run pnpm -F api-server build.

Re-run smoke script. Expect green.

AUTOMATED acceptance:

Build exits 0

Smoke script exits 0

No .ts/.tsx files under dist/lib/prompts/

No __tests__ dir under dist/lib/prompts/

HUMAN_REVIEW: none.

Commit:

chore(build): copy prompt assets to dist during api-server build

esbuild bundles TypeScript but does not copy non-JS assets. The 35 .txt

fragment files and top-level prompt files (safety-override,

crisis-classifier, crisis-response) must land in dist/lib/prompts/ for

production runtime path resolution.

Phase: A

Deferrals: 0

Tests: build smoke green

Phase B — composeFromRows path resolution + miss logging

Goal: loadFragment finds files in bundled environment. Every miss logs. Every empty return logs.

Pre-flight:

git log --oneline -1  # Phase A commit exists

pnpm -F @anchor/lib-db build && pnpm -F @anchor/lib-api-zod build  # ANCHOR-1

pnpm -F api-server typecheck  # baseline clean

pnpm -F api-server test:unit  # record baseline pass count

Smoke (write first, run, expect red):

Write artifacts/api-server/tests/unit/composeFromRows.test.ts with the four tests from the design data section. Run:

pnpm -F api-server test:unit

Expect tests 2 and 4 to fail (logging not yet added). Confirm red before implementing.

Implementation:

Update path resolution in composeFromRows.ts — replace current __dirname / PROMPTS_DIR / FRAGMENTS_DIR constants with resolvePromptsDir() pattern from design data.

Add module init log (compose_from_rows_init).

Update loadFragment to log on miss (fragment_load_miss).

Add empty-result log to composeFromRows (compose_from_rows_empty).

Run pnpm -F api-server test:unit. All four new tests pass.

Run pnpm -F api-server typecheck. Clean.

Run pnpm -F api-server build. Verify dist/lib/prompts/ still populated.

Run all existing unit tests. No regression.

AUTOMATED acceptance:

4 new tests pass

Typecheck clean

Build succeeds with assets in dist

Existing unit tests still pass

HUMAN_REVIEW: none. Post-merge production validation in Phase C BUILD_REPORT.

Commit:

fix(prompts): resolve fragment paths in bundled dist, add miss logging

composeFromRows resolves fragments via dist/lib/prompts/ in bundled

production and falls back to colocated src/ in dev/test. Every

loadFragment miss logs slug and attempted path. Every empty compose

result logs the reason. Module init logs resolved fragments dir.

Phase: B

Deferrals: 0

Tests: 4 new unit tests pass

Phase C — BUILD_REPORT and PR

Goal: PR open against main. BUILD_REPORT.md committed. Agent stops.

Pre-flight:

git log --oneline -1  # Phase B commit exists

git status            # clean

Smoke: BUILD_REPORT.md exists at repo root after generation. PR URL returned by gh pr create.

Implementation:

Generate BUILD_REPORT.md at repo root per AUTONOMY_LAYER.md section 5.

Commit:

docs(m5c): BUILD_REPORT and working files

Phase: C

Deferrals: 0

Push branch.

Open PR:

gh pr create \

--title "fix(prompts): M5c fragment bundling — assets land in dist, miss logging added" \

--body "$(cat BUILD_REPORT.md)"

Do NOT register auto-merge.

Log PR URL in AUTONOMOUS_RUN_LOG.md. Stop.

AUTOMATED acceptance:

PR exists on GitHub

BUILD_REPORT.md committed and pushed

Branch pushed and PR open

HUMAN_REVIEW (log in BUILD_REPORT.md as MANUAL_PLAYTEST_REQUIRED):

Post-merge, after CD redeploys api-server:

Chat as the Virtue Ethics user (7705e15c-6ca7-47d0-9f2c-b99511fb3055). Send "How am I doing?"

Verify response includes: phronesis, eudaimonia, habituation, akrasia, character formation, flourishing, practical wisdom.

Check Fly logs:

flyctl logs --app anchor-api-misty-river-3483 | grep -E "(compose_from_rows_init|fragment_load_miss|compose_from_rows_empty)"

Expect: compose_from_rows_init present, zero fragment_load_miss events during normal operation.

If chat response is still generic after deploy: open new directive to investigate.

Directive-specific self-repair entries

M5C-1 — cp filter copies unwanted files into dist A1: Verify filter checks full paths. Adjust string-contains assertions. A2: Switch to explicit readdir + per-file copyFile loop with .txt-only allowlist. DEFER: HARD STOP — production bundle must not include .ts files.

M5C-2 — statSync at module load throws or blocks A1: Already wrapped in try/catch in design pattern. Default to colocated path on any error. A2: Move to lazy first-call init rather than module load. DEFER: Use NODE_ENV check to pick path explicitly. Log chosen path. Continue.

M5C-3 — mock.method does not capture console.warn in node:test A1: Call mock.method before the function-under-test runs. Verify console.warn is the global being mocked. A2: Refactor the log call in composeFromRows.ts into an injectable logger param. Mock that directly. DEFER: test.skip the log assertion tests with message "DEFERRED: mock capture pattern TBD". Verify logging manually post-merge via Fly logs grep. Log as MEDIUM in deferred-issues.md.

References

Deferred-issues format: AUTONOMY_LAYER.md section 4

BUILD_REPORT format: AUTONOMY_LAYER.md section 5

Hard stops: AUTONOMY_LAYER.md section 6

GO

Branch fix/m5c-fragment-bundling already exists at 4254a36. Working files already committed. Do not re-cut the branch.

git checkout fix/m5c-fragment-bundling

git status  # confirm clean

Append session start entry to AUTONOMOUS_RUN_LOG.md. Execute Phase A → B → C without stopping between phases.
