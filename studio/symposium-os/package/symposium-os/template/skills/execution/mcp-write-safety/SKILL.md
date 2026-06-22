---
name: mcp-write-safety
category: execution
trigger: Before any MCP-based remote file write, especially on files over 5KB or append-only logs.
---

# MCP Write Safety

## Purpose
Prevent destructive remote file truncation via MCP (Model Context Protocol) write paths. Invocable form of `AUTONOMY_LAYER.md` section 1.12.

## When to invoke
- About to call an MCP `create_or_update_file` (or equivalent write tool)
- Direct git push is blocked or unavailable
- Writing to a known multi-section or append-only file (logs, build reports, run notes)
- Operating from an environment that lacks shell access for direct version control operations

## Inputs
- Target file path
- Outgoing file content
- Remote SHA (must be fetched fresh, not cached)
- Expected baseline remote byte length, if known

## Process
1. Verify and log:
   - Target path
   - Current remote SHA (fetched fresh)
   - Byte length of outgoing content
   - First 200 characters of outgoing content
   - Last 200 characters of outgoing content
   - Explicit assertion: outgoing content is full file body, not placeholder, not diff, not template marker
2. Apply hard-stop checks:
   - Outgoing byte length is under 25% of the last known remote size for files over 5KB
   - Outgoing content matches placeholder patterns: `[paste content here]`, `<file body>`, `// TODO`, single-line content for a known multi-section file
   - Remote SHA cannot be verified
3. If any hard-stop fires: do not write. Log the attempted-but-blocked write in `AUTONOMOUS_RUN_LOG.md` and `BLOCKERS_FOR_OPERATOR.md`.
4. Preferred fallback: create a small new file (per-session run note at `docs/run-notes/session-YYYY-MM-DD-[context].md`) instead. Escalate to the operator if the original file must be edited.
5. If all checks pass: execute the write.
6. Post-write: verify remote byte length matches expected. Log result.

## Output
- Pre-write checklist log (in `AUTONOMOUS_RUN_LOG.md`)
- Either: confirmed write with post-write verification, or blocked-write log with fallback action in `BLOCKERS_FOR_OPERATOR.md`

## Stop conditions
- Hard stop the MCP write under any of the conditions in step 2. Do not proceed.
- Halt if post-write byte length does not match expected. The write may have truncated. Escalate to the operator with both the attempted content and the resulting remote state captured.
- Halt and route to the operator for any safety-adjacent file (`AUTONOMY_LAYER.md` section 1.11) regardless of preflight pass.

## Related
- `AUTONOMY_LAYER.md` section 1.12 (the protocol form of this skill)
- `AUTONOMY_LAYER.md` section 1.11 (production safety boundaries)
- Direct git push: always preferred when available
