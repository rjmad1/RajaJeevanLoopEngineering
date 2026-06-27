---
# PROVENANCE METADATA
Original Path: docs/loops/examples/EXAMPLE-003-GATE1-Approval-Workflow.md
Original Version: 1.0
Extraction Date: 2026-06-27
Original Purpose: Loop specification or framework asset.
Generalized Purpose: Loop specification or framework asset.
Dependencies Removed: RajaJeevanLoopEngineering business workflow configurations
Dependencies Retained: None
Compatibility Notes: Fully compatible with standard loop orchestrators and documentation frameworks.
Migration Notes: Direct copy of the general loop framework specification.
---
# EXAMPLE-003 — GATE-1 Hard Gate: Approval Workflow

<!-- This file is a worked example demonstrating the complete GATE-1 Hard Gate workflow for LOOP-001: what the agent writes when it halts, what the human reviewer sees, what the reviewer writes to approve, and what happens when the loop resumes. This is the primary reference for the GATE-1 approval workflow. -->

---

## What This Example Shows

A hypothetical LOOP-001 run (`LOOP-001-20260627-002`) that encounters a Hard Gate condition: the `platform/messaging/` module was removed and replaced by `platform/messaging-core/` in PR #847. The loop detects this as `significant_change = true` and halts at Step 8. A Principal Engineer reviews the findings and approves in writing. The loop resumes at Step 9 and completes.

This example uses a hypothetical scenario — in the actual run history, this change was already captured at baseline (see EXAMPLE-002 §5). The scenario is realistic in structure and content.

---

## Part 1 — Gate Trigger: STATUS File When the Loop Halts

When Step 8 determines that GATE-1 must fire, the loop immediately writes to `STATUS-001.md` and halts. No file in `docs/architecture/` is modified. The STATUS file is the authoritative record that a Hard Gate is pending.

**What the STATUS file looks like at the moment the loop halts:**

```yaml
loop_id: "LOOP-001"
current_status: "awaiting_approval"
# The loop has halted. No further steps will execute until a human records
# an approval decision in gate_outcomes.GATE-1.decision.

current_run_id: "LOOP-001-20260627-002"
# This run is in progress (halted at a gate) — run ID is set.

current_task_id: "STEP-8-gate-evaluation"
# The loop halted during Step 8 gate evaluation.

last_updated: "2026-06-27T09:47:33Z"
# Timestamp when the loop wrote this halt state.

last_completed_run: "LOOP-001-20260627-001"
# The most recently fully completed run (not this halted one).

last_outcome: "completed"
# Outcome of the prior completed run, not this halted run.

open_blockers:
  - id: "BLK-001"
    description: >
      GATE-1 (Hard Gate) is pending approval. Trigger: significant_change = true.
      The platform/messaging/ module (previously 3 services: MessagingService,
      NotificationDispatcher, TemplateRenderer) is no longer present in the
      repository. A new module platform/messaging-core/ was found with 3 services:
      MessageRouterService, NotificationService, TemplateEngineService.
      This constitutes a module removal and replacement — a GATE-1 trigger condition.
      A Principal Engineer or Architecture Owner must review the drift report and
      approve or deny before documentation can be written.
      Drift report: docs/architecture/metadata/DRIFT-001-20260627-002.md
      Findings summary: docs/architecture/metadata/FINDINGS-001-20260627-002.md
    opened_at: "2026-06-27T09:47:33Z"

gate_outcomes:
  GATE-1:
    gate_type: "Hard"
    trigger_condition: >
      significant_change = true. Module platform/messaging/ (present in prior run
      LOOP-001-20260627-001) has no evidence in current scan. Module
      platform/messaging-core/ is present in current scan with no prior state entry.
      Condition: a module has been removed (FR-3 + Step 7 drift flag).
    reviewer: null
    reviewer_role: "Principal Engineer or Architecture Owner"
    decision: "pending"
    rationale: null
    timestamp: "2026-06-27T09:47:33Z"
    # timestamp records when the gate fired, not when it was approved.

emergency_stopped: false
```

**Key points about this state:**

- `current_status: "awaiting_approval"` signals to all other tooling that this loop is blocked. No other run of LOOP-001 may start while this status is set (PRE-3 would prevent it).
- `open_blockers` contains a human-readable description sufficient for a reviewer to understand what happened without reading the loop specification.
- `gate_outcomes.GATE-1.decision: "pending"` is the machine-readable signal the loop polls for. The loop resumes when this changes to `"approved"` or terminates if it changes to `"denied"`.
- No file in `docs/architecture/` has been modified. The prior run's outputs remain intact and authoritative.

---

## Part 2 — Notification to Reviewer

When GATE-1 fires, the loop produces a notification message to the designated reviewer. The notification channel defaults to a draft PR description (or a STATUS file comment, per `.loop-001.yml` configuration). Below is the content of that notification.

---

**LOOP-001 Hard Gate Review Required**

**Run:** LOOP-001-20260627-002  
**Gate:** GATE-1 (Hard Gate — Significant Structural Change)  
**Fired:** 2026-06-27T09:47:33Z  
**Reviewer role required:** Principal Engineer or Architecture Owner  

---

### What Was Detected

During this scheduled discovery run, LOOP-001 detected a **module removal**: `platform/messaging/` is no longer present in the repository. A replacement module `platform/messaging-core/` was found in its place.

This qualifies as `significant_change = true` under the GATE-1 trigger condition: "A module has been removed" (LOOP-001-Architecture-Discovery.md, Step 7).

**No documentation has been written.** All eleven architecture output files remain in the state produced by the prior run (LOOP-001-20260627-001). The loop is halted and waiting for your decision.

---

### What the Drift Report Shows

**Removed:**
- Module: `platform/messaging/`
  - Prior state: 3 services (`MessagingService`, `NotificationDispatcher`, `TemplateRenderer`)
  - Prior state: 7 REST API endpoints (internal stability)
  - Prior state: 4 event types produced (`message.sent`, `message.failed`, `notification.queued`, `template.rendered`)
  - Evidence: `platform/messaging/build.gradle` not found in current scan

**Added:**
- Module: `platform/messaging-core/`
  - Current state: 3 services (`MessageRouterService`, `NotificationService`, `TemplateEngineService`)
  - Current state: 6 REST API endpoints (internal stability)
  - Current state: 4 event types produced (`message.dispatched`, `notification.delivered`, `notification.failed`, `template.compiled`)
  - Evidence: `platform/messaging-core/build.gradle` found; `platform/messaging-core/src/main/java/com/conductor/messaging/` scanned

**Changed:**
- Event type names: all four prior event types have new names in the replacement module (e.g., `message.sent` → `message.dispatched`). This affects any downstream consumer configured for the prior event type names.
- API endpoint count: 7 → 6 (one endpoint, `POST /messages/batch`, is not present in the new module)

**Drift magnitude:** 17 items (module + 3 services + 7 APIs + 4 events removed; module + 3 services + 6 APIs + 4 events added)

---

### What You Need to Review

1. **Confirm the module removal is intentional.** The prior `platform/messaging/` module should have been deprecated per ADR or PR. If this removal was unintentional (e.g., a mis-merge), deny this gate and the loop will stop without writing incorrect documentation.

2. **Confirm the replacement module is correctly identified.** The discovery findings classify `platform/messaging-core/` with 3 services. Do those services accurately represent what PR #847 introduced?

3. **Confirm event type name changes are correctly recorded.** Downstream consumers in `platform/workflow/` and `platform/integrations/` may reference the prior event type names. The discovery findings flag this as technical debt (4 items in `technical-debt.md` for unverified consumer updates), which is correct behavior — the loop records the observation but does not resolve it.

4. **Confirm no security or tenant isolation implications.** The new module handles message routing. Confirm that the tenant scoping applied in `platform/messaging/` (via `TenantSecurityFilter`) is present in the equivalent layer of `platform/messaging-core/`.

---

### What Action to Take

**To approve:** Write your approval into `docs/loops/core/STATUS-001.md` under `gate_outcomes.GATE-1` with:
- `reviewer`: your name or role identifier
- `decision: "approved"`
- `rationale`: a brief statement confirming what you reviewed and why you approve
- `timestamp`: current ISO 8601 timestamp

The loop will detect the approval within its next polling interval and resume at Step 9 (Update Documentation).

**To deny:** Write `decision: "denied"` with your rationale and any correction notes. The loop will terminate with status `stopped`. Your correction notes will be recorded in STATUS-001.md and will become required context for the next run. A new run must be manually triggered after the underlying issue is resolved (either correcting the repository or providing `# ARCH:` annotations to guide future discovery).

**Artifacts available for review:**
- Drift report: `docs/architecture/metadata/DRIFT-001-20260627-002.md`
- Findings summary: `docs/architecture/metadata/FINDINGS-001-20260627-002.md`
- Current unknowns list: `docs/architecture/unknowns.md` (prior run state)
- PR #847: merged 2026-06-25, replacing messaging module

---

## Part 3 — Human Approval Record

After reviewing the drift report, the findings summary, and PR #847, the Principal Engineer writes the following directly into `docs/loops/core/STATUS-001.md`.

**The reviewer replaces the pending gate entry:**

```yaml
gate_outcomes:
  GATE-1:
    gate_type: "Hard"
    trigger_condition: >
      significant_change = true. Module platform/messaging/ (present in prior run
      LOOP-001-20260627-001) has no evidence in current scan. Module
      platform/messaging-core/ is present in current scan with no prior state entry.
      Condition: a module has been removed (FR-3 + Step 7 drift flag).
    reviewer: "Principal Engineer"
    reviewer_role: "Principal Engineer or Architecture Owner"
    decision: "approved"
    rationale: >
      Confirmed: platform/messaging/ was deprecated in PR #847 (merged 2026-06-25)
      and replaced by platform/messaging-core/ per ADR-007. The discovery findings
      accurately reflect the repository state. Documentation of the new module
      boundaries is correct. The event type name changes (message.sent →
      message.dispatched, etc.) are correctly identified as technical debt items
      requiring downstream consumer updates — this is appropriate behavior, not
      an error in the findings. Tenant scoping is present in the new module via
      TenantContextPropagator in shared/middleware/. Approving for documentation
      write.
    timestamp: "2026-06-27T11:23:00Z"
```

**What makes a valid approval record:**

- `reviewer` is populated with a human identity (name, role, or handle — enough to trace who approved)
- `reviewer_role` confirms the approver has the required authority (`Principal Engineer or Architecture Owner`)
- `decision` is `"approved"` (or `"denied"` — no other values are valid)
- `rationale` is substantive: it explains what was reviewed and why the decision was made; it is not a rubber-stamp
- `timestamp` is the moment the approval was written, not the moment the gate fired

**What makes an invalid approval record (do not do these):**

- `reviewer: "auto-approved"` — GATE-1 is a Hard Gate and has no timeout; no auto-approval is possible
- `rationale: "LGTM"` — does not demonstrate that the reviewer examined the findings
- Approving without having read the drift report — the gate exists precisely because the drift requires human judgment; the approval record is the audit trail that a review occurred
- Modifying the `trigger_condition` field — this field records what the loop detected; it must not be edited by the reviewer

---

## Part 4 — Post-Approval: What Happens Next

### Immediate Resume

When the loop's polling detects that `gate_outcomes.GATE-1.decision` has changed from `"pending"` to `"approved"`, it updates STATUS-001.md to reflect the resumption:

```yaml
current_status: "running"
current_task_id: "STEP-9-update-documentation"
last_updated: "2026-06-27T11:25:00Z"

open_blockers: []
# BLK-001 is cleared when the gate is approved and the loop resumes.
```

The loop then proceeds to Step 9 (Update Documentation), writing all eleven output artifacts with the validated post-refactor findings. The approved drift report becomes the basis for those writes.

### Permanent Audit Trail

The `gate_outcomes.GATE-1` record is permanent. It is never expunged, overwritten, or reset between runs. When the next run of LOOP-001 completes (even if that run does not trigger GATE-1), the gate outcomes from this run are preserved in the Reflection artifact at `docs/architecture/reflections/REFLECTION-001-20260627-002.md`. The STATUS file's `gate_outcomes` map holds the current run's gate state; historical gate outcomes live in Reflections.

### Final STATUS After Completion

After Steps 9–13 complete:

```yaml
loop_id: "LOOP-001"
current_status: "idle"
current_run_id: null
current_task_id: null
last_updated: "2026-06-27T14:18:47Z"
last_completed_run: "LOOP-001-20260627-002"
last_outcome: "completed"
open_blockers: []
gate_outcomes:
  GATE-1:
    gate_type: "Hard"
    trigger_condition: >
      significant_change = true. Module platform/messaging/ removed;
      platform/messaging-core/ added.
    reviewer: "Principal Engineer"
    reviewer_role: "Principal Engineer or Architecture Owner"
    decision: "approved"
    rationale: >
      Confirmed: platform/messaging/ deprecated in PR #847; replaced by
      platform/messaging-core/ per ADR-007. Findings accurate. Approving for
      documentation write.
    timestamp: "2026-06-27T11:23:00Z"
emergency_stopped: false
```

### If Approval Had Been Denied

Had the reviewer written `decision: "denied"`, the following would have occurred:

1. The loop records `current_status: "stopped"`, `last_outcome: "stopped"`, and the denial rationale.
2. No file in `docs/architecture/` is written. The prior run's outputs remain authoritative.
3. `open_blockers` is updated with a new entry describing the denial and the correction required.
4. A partial Reflection is produced: `docs/architecture/reflections/REFLECTION-001-20260627-002.md` with status `stopped` and the denial rationale recorded in Section 5 (Gate Outcomes) and Section 6 (Failures and Anomalies).
5. Any correction notes the reviewer wrote in their denial rationale become required context for the next run (the agent must read STATUS-001.md before beginning, per Required Context item 3).
6. A new run must be manually triggered after the underlying issue is resolved — either by correcting the repository (if the discovery was wrong) or by providing `# ARCH:` annotations to guide future classification (if the repository is correct but the loop cannot infer it).

The denied run's gate record is permanent and cannot be removed. It becomes part of the audit history referenced in the next run's Reflection.

