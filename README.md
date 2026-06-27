# RajaJeevanLoopEngineering Framework

**Version:** 1.0.0  
**License:** MIT  
**Target Platform:** Java 21+ & Any Language-Agnostic Agent Framework  

Welcome to the **RajaJeevanLoopEngineering** repository. This repository provides the infrastructure, guidelines, specifications, execution templates, and utility code for executing and auditing structured AI agent workflows.

Rather than executing open-ended prompts, this framework enables software developers and stakeholders to codify agent processes into formal, state-bound, auditable execution loops governed by the **Maker/Checker** pattern and human oversight.

---

## 🛠️ Instant Porting & Bootstrapping

We provide an interactive, single-command utility to port the loop infrastructure and container configurations directly to any target repository.

### Quick Start (PowerShell CLI)

Run the interactive bootstrap script from your terminal:

```powershell
.\interactive-bootstrap.ps1
```

The script will ask you **only two questions**:
1. **Target Project Location:** The absolute local path to your project folder (e.g. `C:\Users\rajaj\Projects\my-app`).
2. **Project Nature:** Select your project track:
   - `[1] Greenfield` — ADR designs, architecture mapping, documentation, test setup.
   - `[2] Brownfield` — Context assembly, regression testing, safe implementation, verification, refactoring.
   - `[3] Modernization` — System discovery, code review, decoupling, API contract verification.
   - `[4] Incident Response` — Reproduction test setups, hotfixing, targeted verification, post-mortems.
   - `[5] All Loops` — Installs the complete loop catalog.

### What is Configured?

The script automatically ports:
*   **Contextual Loops:** Copies only the necessary `.md` loop definitions to `docs/loops/<category>/`.
*   **General Standards:** Provisions cross-cutting standards to `docs/loops/shared/`.
*   **Customization Files:** Sets up `.agents/AGENTS.md` and templates for tasks and checklists.
*   **Rule Engine Java Code:** Copies the `loop-library/code` and a standalone Gradle wrapper for local testing.
*   **Dev Container Workspace:** Creates `.devcontainer/devcontainer.json` and a setup script to compile and test files automatically on startup.

---

## 📂 Directory Structure

*   **[`shared/`](shared/)** — Cross-cutting engineering standards, principles, naming conventions, and metrics.
*   **[`loops/`](loops/)** — Bounded loop specifications across different domains:
    *   **[`core/`](loops/core/)** — Foundational loops (Discovery, planning, implementation, verification, reflection).
    *   **[`engineering/`](loops/engineering/)** — Routine engineering tasks (Bug fixing, refactoring, testing).
    *   **[`platform/`](loops/platform/)** — Generalized integration and contract validations.
    *   **[`governance/`](loops/governance/)** — ADR generation, compliance reviews, release gates.
*   **[`templates/`](templates/)** — Document structures for authoring new loops, skills, or run-status indicators.
*   **[`examples/`](examples/)** — Sample execution logs demonstrating complete runs.
*   **[`recipes/`](recipes/)** — Copy-paste prompts and configs for agent personas.
*   **[`code/`](code/)** — Decoupled Java rule engine and circuit-breaker execution utilities.
*   **[`docs/`](docs/)** — In-depth conceptual, architectural, and troubleshooting guides.

---

## 🏁 Running the Java Rule Engine Natively

To build and verify execution modules natively without docker:
```bash
cd loop-library/code
./gradlew test
```

---

## 📖 Wiki Documentation

For in-depth explanations of the loop theory, classification matrices, and operational guides, visit the official [GitHub Wiki](https://github.com/rjmad1/RajaJeevanLoopEngineering/wiki).
