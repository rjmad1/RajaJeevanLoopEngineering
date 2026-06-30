---
# PROVENANCE METADATA
Original Path: docs/loops/core/LOOP-008-Loop-Creation.md
Original Version: 1.0
Extraction Date: 2026-06-29
Original Purpose: End-to-end loop creation based on user prompt.
Generalized Purpose: End-to-end loop creation based on user prompt.
Dependencies Removed: None
Dependencies Retained: None
Compatibility Notes: Fully compatible with standard loop orchestrators and documentation frameworks.
Migration Notes: N/A
---
# LOOP-008 — Loop Creation

**Loop ID:** LOOP-008
**Name:** Loop Creation
**Version:** 1.0
**Status:** Active
**Category:** Core
**Depends On:** None
**Human Gates:** Soft
**Owner:** Principal Architecture Function
**Maintainer:** Principal Architecture Function

---

## Purpose

To establish a standardized, automated, and frictionless process for generating new engineering loops. This loop allows an engineer to provide a brief 1-2 line description of a required loop, and the agent will automatically handle deduplication, ID assignment, markdown generation, and comprehensive catalog updates.

## Problem Statement

Manually creating a new loop requires high cognitive load: finding the next available ID, ensuring no duplicate exists, creating the loop markdown file according to the strict schema, and correctly updating 6-8 different documentation catalogs (GitHub, Wiki, HTML reckoners). This manual overhead discourages the formalization of new workflows.

## Scope

**In scope:**
- Parsing a 1-2 line description to deduce loop category and intent.
- Checking `docs/loop-catalog.md` and `shared/SPEC-010-Loop-Catalog.md` for duplicates.
- Determining the next available ID within the chosen category (e.g., `LOOP-NNN`).
- Generating the loop Markdown file following standard schema (e.g., `LOOP-005-Implementation.md`).
- Updating `docs/loop-catalog.md`.
- Updating `shared/SPEC-010-Loop-Catalog.md`.
- Updating `shared/loops-manifest.json`.
- Updating `docs/aeos-loop-instructions-by-project-type.md` and `docs/project-loops-ready-reckoner.md`.
- Updating Wiki files under `RajaJeevanLoopEngineering.wiki/`.
- Updating the HTML Quick Reckoner files (`docs/loops-quick-reckoner.html` and `remote-loops-quick-reckoner.html`).
- Updating `USER_GUIDE.md` (if relevant).

**Out of scope:**
- Modifying the underlying execution engine.
- Writing the detailed loop steps beyond a robust initial draft (the user can refine the generated draft later).
---

## Scheduling

- **Cadence:** On-demand / Trigger-based
- **First Run Behavior:** Fire immediately on start
- **Durability:** Durable (survives session restarts via status file)
- **Off-Hours Behavior:** Paused overnight
- **Self-Cleanup:** Automatically deletes scheduler when watchlist is empty

## Preconditions

- User provides a 1-2 line description of the desired loop.
- Agent has read/write access to all catalog files and the `loops/` directory.

## Workflow (Agent Instructions)

When executed, the Agent must strictly follow these steps:

1. **Intent Analysis & Deduplication:**
   - Parse the user's request.
   - Read `docs/loop-catalog.md` to ensure a loop with the same or highly similar intent does not already exist. If a duplicate exists, stop and inform the user.
2. **Category & ID Assignment:**
   - Map the request to a category (Core 001-099, Engineering 100-199, Platform 200-299, Governance 300-399, Release 400-499, Strategy 500-599).
   - Find the highest existing ID in that category and add 1 to get the new ID.
3. **Loop Generation:**
   - Create `loops/<category>/LOOP-<ID>-<Name>.md`.
   - Populate it with standard sections (Provenance Metadata, Header, Purpose, Problem Statement, Scope, Workflow, Verification, etc.) tailored to the user's request.
4. **Markdown Documentation Updates:**
   - Append or insert the new loop into `docs/loop-catalog.md` in the appropriate category table.
   - Insert the new loop into `shared/SPEC-010-Loop-Catalog.md`.
   - Add the loop path to the appropriate arrays in `shared/loops-manifest.json`.
   - Add references in `docs/aeos-loop-instructions-by-project-type.md`, `docs/project-loops-ready-reckoner.md`, and `USER_GUIDE.md`.
5. **Wiki & HTML Updates:**
   - Clone the live GitHub Wiki (`https://github.com/rjmad1/RajaJeevanLoopEngineering.wiki.git`) if not already available, update the corresponding `.md` files, and commit/push the changes.
   - Using targeted string manipulation or Regex (DO NOT overwrite the entire file blindly), insert the new loop's data into the table/data structures within `docs/loops-quick-reckoner.html` and `remote-loops-quick-reckoner.html`.
6. **Finalization:**
   - Summarize the newly created loop and all files updated.

## Verification

The agent will verify that:
- The new `LOOP-XXX` file exists.
- The ID does not conflict with any existing ID.
- The JSON manifest is syntactically valid after the update.

## Failure Recovery

- If HTML injection fails, the agent must rollback the HTML file to its previous state and escalate to the user.
