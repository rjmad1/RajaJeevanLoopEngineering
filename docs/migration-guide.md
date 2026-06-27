# Migration Guide

This guide describes how to migrate an existing application (such as the original `RajaJeevanLoopEngineering` system) or integrate a new repository into the standalone general-purpose loop framework.

---

## 1. Migrating Java Dependencies

If you are migrating an existing codebase that imports classes from `com.conductor.shared.execution` or `com.conductor.shared.rules`:

1. Add the standalone library gradle project or source files to your build.
2. Update all imports in your codebase:
   - Replace `import com.conductor.shared.execution.ExecutionContext;` with `import com.rajajeevan.loop.execution.ExecutionContext;`
   - Replace `import com.conductor.shared.execution.RetryPolicy;` with `import com.rajajeevan.loop.execution.RetryPolicy;`
   - Replace `import com.conductor.shared.rules.ConditionEvaluator;` with `import com.rajajeevan.loop.rules.ConditionEvaluator;`
3. If your code depended on `com.conductor.shared.execution.provider.WhatsAppProvider` or other integration-specific classes, leave those classes in your local application directory; they are domain-specific implementations and are not part of this general-purpose execution library.

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
