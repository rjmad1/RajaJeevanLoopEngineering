---
# PROVENANCE METADATA
Original Path: docs/loops/strategy/LOOP-503-Roadmap-Prioritization.md
Original Version: 0.1
Extraction Date: 2026-06-28
Original Purpose: Continuously evaluate, rank, and schedule discovered opportunities into actionable roadmap items.
Generalized Purpose: Continuously evaluate, rank, and schedule discovered opportunities into actionable roadmap items.
Dependencies Removed: None
Dependencies Retained: LOOP-502 — Product Intelligence Architect
Compatibility Notes: Fully compatible with standard loop orchestrators.
Migration Notes: New loop based on Product Loop Coverage Audit.
---
# LOOP-503 — Roadmap Prioritization

**Loop ID:** LOOP-503
**Name:** Roadmap Prioritization
**Version:** 0.1
**Status:** Active
**Category:** Strategy
**Depends On:** LOOP-502 — Product Intelligence Architect
**Human Gates:** Hard
**Owner:** Product Strategy Function
**Maintainer:** Product Strategy Function

---

## Purpose
Continuously evaluate, rank, and schedule discovered opportunities into a sequence of actionable, committed roadmap items based on engineering capacity and strategic timelines.

## Problem Statement
While opportunities can be discovered and ranked theoretically, doing so does not account for actual engineering capacity, quarterly timelines, or cross-team constraints. Without a prioritization loop, the backlog becomes an unmanageable wishlist rather than a committed, executable plan.

## Why This Loop Exists
Deciding *what* to build next based on capacity and timeline constraints is a discrete, continuous system distinct from strategy and execution. It requires its own feedback cycle to ensure that the committed roadmap is always achievable and aligned with business goals.

## Scope
**In scope:**
- Consuming ranked opportunities from LOOP-502.
- Evaluating engineering capacity against strategic timelines.
- Producing a committed Product Roadmap and Prioritized Feature Backlog.

**Out of scope:**
- Defining individual features (LOOP-505).
- Discovering new opportunities (LOOP-502).

**Maximum run duration:** 4 hours.

## Inputs
- Ranked Opportunities (from LOOP-502)
- Engineering Capacity Data
- Strategic Target Dates

## Outputs
- `ROADMAP.md`: The committed product roadmap.
- `FEATURE-BACKLOG.md`: Prioritized feature backlog.
- `STATUS-503.md`: Run state and metrics.

## Workflow
### Step 1 — Ingest Opportunities
**Agent:** `ROADMAP-ARCHITECT`
Consume ranked opportunities from LOOP-502.

### Step 2 — Evaluate Capacity and Timelines
**Agent:** `ROADMAP-ARCHITECT`
Align top opportunities with available engineering capacity and strategic target dates.

### Step 3 — Draft Roadmap
**Agent:** `ROADMAP-ARCHITECT`
Produce a draft roadmap and updated backlog.

**[GATE-1 — Hard Gate: Roadmap Approval]**
Stakeholders must review the trade-offs and approve the committed timelines.

### Step 4 — Finalize Roadmap
**Agent:** `ROADMAP-WRITER`
Commit the approved roadmap to the repository.

## Deliverables
- A complete and validated Product Roadmap.
- A prioritized Feature Backlog ready for Feature Definition.

**Strict Output Schema:** All deliverables must be strictly formatted. Markdown artifacts must comply with GitHub Flavored Markdown (GFM). No extraneous conversational text is permitted in final artifacts.
