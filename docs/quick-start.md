# Quick Start Guide

Get started with the Loop Engineering Framework in under 10 minutes.

---

## Step 1: Clone the Library

Clone or copy the library directory into your project structure:

```bash
cp -r RajaJeevanLoopEngineering/ /path/to/your/project/
```

---

## Step 2: Integrate Java Execution Helpers (Optional)

If your orchestrator is Java-based, declare the code dependencies in your `build.gradle`:

```gradle
dependencies {
    implementation project(':RajaJeevanLoopEngineering:code')
}
```

Or copy the source files from `code/src/main/java/com/rajajeevan/loop/` directly into your workspace.

---

## Step 3: Run your First Discovery Loop

1. Create a `status/` and `reflections/` directory in your workspace:
   ```bash
   mkdir -p docs/loops/core/
   mkdir -p docs/discovery/reflections/
   ```
2. Read the standard specification for discovery in [LOOP-001-Architecture-Discovery.md](../loops/core/LOOP-001-Architecture-Discovery.md).
3. Initialize the run using the template in [STATUS-TEMPLATE.md](../templates/STATUS-TEMPLATE.md) and save it as `docs/loops/core/STATUS-001.md`.
4. Trigger your agent or run a script to scan the workspace and generate the module catalog.
5. Once completed, write the per-run review using the template in [REVIEW-TEMPLATE.md](../templates/REVIEW-TEMPLATE.md) and commit the changes!
