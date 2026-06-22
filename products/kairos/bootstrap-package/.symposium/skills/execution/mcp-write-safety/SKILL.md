---
name: mcp-write-safety
category: execution
trigger: Before any MCP-based remote file write, especially on files over 5KB or append-only logs.
---

# MCP Write Safety

## Purpose
Prevent destructive remote file truncation via the GitHub MCP write path. Invocable form of `AUTONOMY_LAYER.md` section 1.12.

## When to invoke
- About to call a GitHub MCP `create_or_update_file` (or equivalent)
- Direct git push is blocked or unavailable
- Writing to a known multi-section or append-only file (logs, build reports)

## Inputs
- Target file path
- Outgoing file content
- Remote SHA (must be fetched fresh, not cached)

## Process
1. Verify and log:
   - Target path
   - Current remote SHA (fetched fresh)
   - Byte length of outgoing content
   - First 200 characters of outgoing content
   - Last 200 characters of outgoing content
   - Explicit assertion: outgoing content is full file body, not placeholder, not diff, not template marker
2. Apply hard-stop checks:
   - Outgoing byte length is dramatically smaller than the last known remote size for that file (under 25% of remote size for files over 5KB)
   - Outgoing content matches placeholder patterns: `[paste content here]`, `<file body>`, single-line content for a known multi-section file
   - Remote SHA cannot be verified
3. If any hard-stop fires: do not write. Log the attempted-but-blocked write in `AUTONOMOUS_RUN_LOG.md` and `BLOCKERS_FOR_MARCUS.md`.
4. Preferred fallback: create a small new file (per-session run note at `docs/run-notes/session-YYYY-MM-DD-[context].md`) instead. Escalate to Marcus if the original file must be edited.
5. If all checks pass: execute the write.
6. Post-write: verify remote byte length matches expected. Log result.

## Output
- Pre-write checklist log
- Either: confirmed write with post-write verification, or blocked-write log with fallback action

## Stop conditions
- Hard stop the MCP write under any of the conditions in step 2. Do not proceed.
- Halt if post-write byte length does not match expected (recovery via `AUTONOMY_LAYER.md` section 2 ANCHOR-16-equivalent recovery path).

## Related
- `AUTONOMY_LAYER.md` section 1.12 (the protocol form of this skill)
- `skills/execution/atomic-commit` (preferred path: direct git push)
