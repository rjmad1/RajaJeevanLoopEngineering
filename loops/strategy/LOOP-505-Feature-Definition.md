---
# PROVENANCE METADATA
Original Path: docs/loops/strategy/LOOP-505-Feature-Definition.md
Original Version: 0.1
Extraction Date: 2026-06-28
Original Purpose: Translate prioritized roadmap items into comprehensive Product Requirement Documents (PRDs).
Generalized Purpose: Translate prioritized roadmap items into comprehensive Product Requirement Documents (PRDs).
Dependencies Removed: None
Dependencies Retained: LOOP-503 — Roadmap Prioritization
Compatibility Notes: Fully compatible with standard loop orchestrators.
Migration Notes: New loop based on Product Loop Coverage Audit.
---
# LOOP-505 — Feature Definition

**Loop ID:** LOOP-505
**Name:** Feature Definition
**Version:** 0.1
**Status:** Active
**Category:** Strategy
**Depends On:** LOOP-503 — Roadmap Prioritization
**Human Gates:** Hard, Soft
**Owner:** Product Strategy Function
**Maintainer:** Product Strategy Function

---

## Purpose
Translate a prioritized roadmap item into a comprehensive Product Requirement Document (PRD), covering user experience, scope, and business acceptance criteria.

## Problem Statement
Technical planning (LOOP-004) requires a finalized feature specification as an input. Without a structured Feature Definition loop, engineering receives vague requirements, resulting in scope creep, mismatched expectations, and frequent rework during implementation.

## Why This Loop Exists
Defining the boundaries, UX, and requirements of a single feature requires its own feedback cycle with stakeholders before technical architecture begins. This loop ensures engineering only acts on fully scoped, validated product requirements.

## Scope
**In scope:**
- Defining PRDs from prioritized backlog items.
- Defining Acceptance Criteria and MVP boundaries.
- Generating UX/Wireframe text specifications.

**Out of scope:**
- Technical Architecture and Planning (LOOP-004).
- Roadmap prioritization (LOOP-503).

**Maximum run duration:** 4 hours.

## Inputs
- Prioritized roadmap item (from LOOP-503)
- User personas
- Business and compliance constraints

## Outputs
- `PRD-*.md`: Product Requirement Document.
- `STATUS-505.md`: Run state and metrics.

## Workflow
### Step 1 — Gather Feature Context
**Agent:** `PRODUCT-OWNER`
Read the prioritized roadmap item and relevant user personas.

### Step 2 — Draft PRD
**Agent:** `PRODUCT-OWNER`
Draft the PRD, including Objectives, Scope, UX Flows, and Non-Functional Requirements.

### Step 3 — Define Acceptance Criteria
**Agent:** `PRODUCT-OWNER`
Formulate testable business acceptance criteria.

**[GATE-1 — Hard Gate: PRD Approval]**
Stakeholders review and approve the PRD.

### Step 4 — Commit PRD
**Agent:** `PRD-WRITER`
Commit the approved PRD to the repository to serve as the input for LOOP-004 (Planning).

## Deliverables
- Product Requirement Document (PRD).
- Business Acceptance Criteria.
- UX/Wireframe text specifications.

**Strict Output Schema:** All deliverables must be strictly formatted. Markdown artifacts must comply with GitHub Flavored Markdown (GFM). No extraneous conversational text is permitted in final artifacts.
