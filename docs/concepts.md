# Loop Engineering Concepts

This page explains the fundamental concepts of the Loop Engineering Framework.

---

## 1. Loop Document
A loop document is a Markdown specification conforming to the canonical standard format. It serves as the developer and agent contract, laying out step-by-step responsibilities.

## 2. Maker / Checker Pattern
A security and governance control where:
- The **Maker** generates an artifact (e.g., source code, spec, review).
- The **Checker** evaluates the artifact.
- **Rule:** The Maker and Checker must be separate, independent instances.

## 3. Human Approval Gates
Gating mechanisms placed in the execution workflow:
- **Hard Gate:** The execution halts completely. It cannot resume without manual human input (e.g., signed approval in a PR).
- **Soft Gate:** The execution notifies the human operator and waits for a timeout. If no objection is registered, the loop continues automatically.

## 4. Preconditions & Postconditions
- **Preconditions:** Programmatically verifiable conditions that must be met before starting.
- **Postconditions:** Verifiable assertions that must evaluate to true after execution before outputs are accepted.

## 5. Reflection Log
A per-run retrospective containing metrics, errors, anomalies, and learnings. It acts as an audit trail and feeds the agent's long-term memory.
