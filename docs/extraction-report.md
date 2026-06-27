# Repository Extraction Report

This report documents the extraction of the Loop Engineering Framework from the `Conductor` repository to create a standalone, general-purpose library.

## 1. Summary of Actions
- **Additive Execution:** A new root directory `general-purpose-loop-library/` was created. Zero modifications or deletions were performed on the original Conductor codebase.
- **Harvesting Specifications:** All loop files under `docs/loops/` were copied to `general-purpose-loop-library/loops/` and `shared/` respectively.
- **Adding Provenance Metadata:** A standard provenance block was prepended to every single markdown file, containing fields for:
  - Original Path
  - Original Version
  - Extraction Date
  - Original Purpose
  - Generalized Purpose
  - Dependencies Removed / Retained
  - Compatibility & Migration Notes
- **Decoupling Rules and Execution Engine:** General-purpose Java classes were moved into the `com.conductor.loop` namespace and set up as an independent build module.

## 2. Directory Mappings

| Source Directory | Destination Directory | Status |
| :--- | :--- | :--- |
| `docs/loops/shared/` | `general-purpose-loop-library/shared/` | Completed |
| `docs/loops/core/` | `general-purpose-loop-library/loops/core/` | Completed |
| `docs/loops/engineering/` | `general-purpose-loop-library/loops/engineering/` | Completed |
| `docs/loops/platform/` | `general-purpose-loop-library/loops/platform/` | Completed (Generalized) |
| `docs/loops/governance/` | `general-purpose-loop-library/loops/governance/` | Completed |
| `docs/loops/release/` | `general-purpose-loop-library/loops/release/` | Completed |
| `docs/loops/templates/` | `general-purpose-loop-library/templates/` | Completed |
| `docs/loops/examples/` | `general-purpose-loop-library/examples/` | Completed |
| `shared/rules/` | `general-purpose-loop-library/code/` (Rules package) | Completed |
| `shared/execution/` | `general-purpose-loop-library/code/` (Execution package) | Decoupled & Completed |
