# Loop Architecture and Directories

The Loop Engineering Framework structure is designed to separate standards, specifications, execution templates, recipes, and utility code.

```
RajaJeevanLoopEngineering/
├── README.md               # Root framework index and orientation
├── LICENSE                 # License terms
├── CHANGELOG.md            # Version change history
├── VERSION.md              # Framework version metadata
├── docs/                   # Conceptual and user guides
├── shared/                 # Core specs, governance, and naming standards
├── loops/                  # Executable loops specifications
│   ├── core/               # Base discovery, planning, and implementation
│   ├── engineering/        # Coding, bug fixing, test generation
│   ├── platform/           # Validation and integration
│   └── governance/         # ADRs, compliance, release readiness
├── templates/              # Markdown templates for new loop assets
├── examples/               # Worked example runs
├── recipes/                # Immediate copy-paste guides for different personas
└── code/                   # Reusable Java rules and execution modules
```

## Module Interaction

1. **Trigger:** The loop runner reads the loop specification (under `loops/`) and resolves dependencies.
2. **Context:** The environment variables and state mapping are populated into `ExecutionContext` (under `code/`).
3. **Execution Steps:** For each step in the `## Workflow`:
   - The runner invokes the designated **Maker** agent.
   - The output is validated by the **Checker** using `ConditionEvaluator` rules.
4. **Verification:** The postconditions are verified.
5. **Gating:** Human gates are resolved via notifications or blocking hooks.
6. **Reflection:** A reflection artifact is saved, and metrics are recorded.
