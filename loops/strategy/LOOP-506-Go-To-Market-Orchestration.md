---
# PROVENANCE METADATA
Original Path: docs/loops/strategy/LOOP-506-Go-To-Market-Orchestration.md
Original Version: 0.1
Extraction Date: 2026-06-28
Original Purpose: Plan and execute the launch strategy, positioning, and customer communication for new features or products.
Generalized Purpose: Plan and execute the launch strategy, positioning, and customer communication for new features or products.
Dependencies Removed: None
Dependencies Retained: None
Compatibility Notes: Fully compatible with standard loop orchestrators.
Migration Notes: New loop based on Product Loop Coverage Audit.
---
# LOOP-506 — Go-To-Market Orchestration

**Loop ID:** LOOP-506
**Name:** Go-To-Market Orchestration
**Version:** 0.1
**Status:** Active
**Category:** Strategy
**Depends On:** None
**Human Gates:** Hard, Soft
**Owner:** Product Marketing Function
**Maintainer:** Product Marketing Function

---

## Purpose
Plan and execute the launch strategy, product positioning, and customer communication for new features or products.

## Problem Statement
Engineering deployment loops (e.g., LOOP-401, LOOP-402) focus strictly on code safety and operational readiness. They do not prepare sales, marketing, or customers for new features. Without a GTM loop, features are deployed silently without driving adoption, pricing updates, or marketing enablement.

## Why This Loop Exists
Orchestrating a launch is a commercial operation that requires its own independent state (launch readiness) and feedback cycle. Separating this from technical release checklists ensures that commercial activities do not block code safety, while guaranteeing that every major feature has a planned launch.

## Scope
**In scope:**
- Generating GTM Strategy.
- Planning marketing communication and launch dates.
- Producing marketing collateral and positioning.

**Out of scope:**
- Technical release checklists (LOOP-401).
- Customer-facing release notes drafting (handled by LOOP-104-Documentation).

**Maximum run duration:** 4 hours.

## Inputs
- Feature completion status
- Market research
- Target release dates

## Outputs
- `GTM-STRATEGY.md`: GTM Strategy and positioning.
- `LAUNCH-PLAN.md`: Marketing launch plan and timelines.
- `STATUS-506.md`: Run state and metrics.

## Workflow
### Step 1 — Review Launch Readiness
**Agent:** `GTM-ORCHESTRATOR`
Assess the feature completion status and strategic positioning.

### Step 2 — Draft GTM Strategy
**Agent:** `GTM-ORCHESTRATOR`
Draft the positioning, target audience, pricing impact, and marketing channels.

### Step 3 — Plan Launch Timeline
**Agent:** `GTM-ORCHESTRATOR`
Create the chronological launch plan and collateral checklist.

**[GATE-1 — Hard Gate: Launch Plan Approval]**
Marketing and Product stakeholders approve the launch plan.

### Step 4 — Finalize Documents
**Agent:** `GTM-WRITER`
Commit the GTM Strategy and Launch Plan to the repository.

## Deliverables
- GTM Strategy.
- Launch Plan.
- Marketing Collateral Checklists.

**Strict Output Schema:** All deliverables must be strictly formatted. Markdown artifacts must comply with GitHub Flavored Markdown (GFM). No extraneous conversational text is permitted in final artifacts.
