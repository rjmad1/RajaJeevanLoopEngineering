# Troubleshooting Guide

This guide covers common issues encountered during loop setup, execution, and verification, along with remediation steps.

---

## 1. Loop Run Hangs or Fails to Terminate

### Symptoms
- The agent runs indefinitely without producing outputs.
- Token consumption climbs rapidly.

### Causes
- Missing or misconfigured `Max Run Duration` in the loop specification.
- Recursive loops or infinite retry policies on failure events.
- Hard Gate blocking execution without notification channels set up.

### Resolution
- Check that the runner parses and respects `Max Run Duration`.
- Verify the retry count in `RetryPolicy` (default is 3, make sure it is not set to infinite).
- Check the run's `STATUS` document to see if a Hard Gate is active. Locate the approver and record approval or termination.

---

## 2. Transition Request Blocked (HTTP 409 Conflict)

### Symptoms
- The engine rejects a transition request, returning HTTP status code `409` and transition_allowed = `false`.

### Causes
- **Circuit Breaker is Tripped (OPEN):** The loop has encountered consecutive transition errors reaching its threshold.
- **Phase Mismatch:** The `source_phase` provided in the request body does not match the actual current phase of the loop in server memory.
- **Invalid Transition Chain:** The target phase requested is not a valid successor of the current phase (e.g. jumping directly from `DISCOVERY` to `IMPLEMENTATION`).

### Resolution
- Query the status endpoint `GET /api/v1/loops/{loopId}/status` to inspect `current_state` and `circuit_breaker` tripped flag.
- If the circuit breaker is tripped, restart the loop engine server (since states are transient in-memory map).
- Correct the client-side state sequence in your agent code to proceed step-by-step (`DISCOVERY` -> `PLANNING` -> `IMPLEMENTATION` -> `VERIFICATION` -> `REFLECTION`).

---

## 3. Provenance Check Fails

### Symptoms
- Upstream dependencies reported as stale.
- Git SHA checks return mismatched errors.

### Causes
- The branch HEAD changed since the last execution of LOOP-001.
- Running loops out of order (e.g., executing LOOP-005 without updating LOOP-002 context).

### Resolution
- Always execute loop sequences sequentially: `Discovery` -> `Context` -> `Planning` -> `Implementation` -> `Verification`.
- Re-run `LOOP-001` to refresh the architecture catalog before starting a new execution plan.
