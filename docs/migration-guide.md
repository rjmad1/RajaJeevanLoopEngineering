# Migration Guide

This guide describes how to migrate an existing application (such as the original `RajaJeevanLoopEngineering` system) or integrate a new repository into the standalone general-purpose loop framework.

---

If you are migrating an existing codebase that imports classes from legacy packages:

1. Note that legacy packages (like `com.legacy.shared.execution` and `com.legacy.shared.rules`) containing `ExecutionContext`, `RetryPolicy`, and `ConditionEvaluator` are **not implemented** in the current standalone release.
2. Instead, migrate your applications to interface directly with the standalone `LoopEngineServer` REST API using standard HTTP clients (e.g. `curl`, Python `requests`, or Java `HttpClient`) or using the provided CLI wrapper script `loop-control.sh`.
3. If your code depended on legacy integration-specific provider classes (such as database or notification integrations), leave those classes in your local application directory; they are domain-specific implementations and are not part of the decoupled loop engine server.

---

## 2. Standardizing Loop Specifications

If you are migrating existing loop markdown specs:

1. Copy the loop markdown documents to the corresponding categorised folders under `loops/`.
2. Add a `PROVENANCE METADATA` header block at the very top of each file (inside HTML/markdown comment tags or YAML frontmatter) to maintain traceability:
   ```yaml
   ---
   # PROVENANCE METADATA
   Original Path: [original-path]
   Original Version: [version]
   Extraction Date: [date]
   ...
   ---
   ```
3. Remove any application-specific workflow naming conventions. For example, replace instances of "RajaJeevanLoopEngineering-specific API verification" with "Target API Contract Validation".
