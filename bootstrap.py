#!/usr/bin/env python3
# bootstrap.py
#
# Cross-platform interactive python utility to initialize the loop framework in any project.
# Replaces PowerShell bootstrapping scripts for standard Linux/macOS dev containers and CI/CD pipelines.

import os
import sys
import shutil
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_devcontainer_json():
    return {
        "name": "Loop Engineering Dev Environment",
        "image": "mcr.microsoft.com/devcontainers/universal:2",
        "features": {
            "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {
                "moby": True,
                "version": "latest"
            },
            "ghcr.io/devcontainers/features/java:1": {
                "version": "21"
            }
        },
        "remoteUser": "vscode",
        "runArgs": [
            "--cap-drop=all",
            "--security-opt=no-new-privileges"
        ],
        "customizations": {
            "vscode": {
                "extensions": [
                    "redhat.vscode-yaml",
                    "vscjava.vscode-java-pack"
                ]
            }
        },
        "postCreateCommand": "bash .devcontainer/devcontainer-setup.sh"
    }

def get_setup_script_sh():
    return """#!/usr/bin/env bash
set -euo pipefail

echo "=== Initializing Loop Engineering Dev Container ==="

# Compile rule engine core and run unit validations
if [ -d "RajaJeevanLoopEngineering/code" ]; then
    echo "Bootstrapping loop Java rule engine..."
    chmod +x RajaJeevanLoopEngineering/code/gradlew || true
    (cd RajaJeevanLoopEngineering/code && ./gradlew test) || echo "Warning: Initial unit tests failed or skipped."
fi

echo "=== Dev Container Loop Setup Completed Successfully ==="
"""

def main():
    clear_screen()
    print("==========================================================")
    print("     RAJA JEEVAN - LOOP ENGINEERING BOOTSTRAP UTILITY     ")
    print("==========================================================")
    print()
    print("This utility configures structured AI agent execution loops and")
    print("Dev Container workspace settings in any target repository.")
    print()

    # 1. Prompt for Project Location
    target_dir = ""
    while not target_dir:
        input_path = input("Enter the absolute local path to your target project folder: ").strip()
        if not input_path:
            print("Error: Path cannot be empty.")
            continue
        
        resolved_path = os.path.abspath(input_path)
        if not os.path.exists(resolved_path):
            print(f"Directory does not exist: {resolved_path}")
            choice = input("Do you want to create this directory? (Y/N): ").strip().upper()
            if choice == 'Y':
                try:
                    os.makedirs(resolved_path, exist_ok=True)
                    target_dir = resolved_path
                except Exception as e:
                    print(f"Error creating directory: {e}")
        else:
            target_dir = resolved_path

    # 2. Prompt for Project Type
    print()
    print("Select the nature of your target project:")
    print("  [1] Greenfield        - Architecture ADR design, Spec Authoring, Test Setup, Initial Code Gen.")
    print("  [2] Brownfield        - Context Assembly, Regression Tests, Safe Mod, verification, refactoring.")
    print("  [3] Modernization     - System Discovery, Code Review, Decoupling, API Contract validation.")
    print("  [4] Incident Response - RCA, Reproduction Tests, Hotfixing, Verification, Post-Mortem Reflection.")
    print("  [5] All Loops         - Installs the entire loop catalog suite.")
    print()

    project_type = ""
    while not project_type:
        choice = input("Select Project Type [1-5]: ").strip()
        if choice == "1":
            project_type = "Greenfield"
        elif choice == "2":
            project_type = "Brownfield"
        elif choice == "3":
            project_type = "Modernization"
        elif choice == "4":
            project_type = "IncidentResponse"
        elif choice == "5":
            project_type = "All"
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

    print()
    print("Starting loop provisioning...")

    src_root = os.path.dirname(os.path.abspath(__file__))

    # Target Subdirectories
    target_agents_dir = os.path.join(target_dir, ".agents")
    target_docs_dir = os.path.join(target_dir, "docs", "loops")
    target_code_dir = os.path.join(target_dir, "RajaJeevanLoopEngineering", "code")
    target_devcontainer_dir = os.path.join(target_dir, ".devcontainer")

    for directory in [target_agents_dir, target_docs_dir, target_code_dir, target_devcontainer_dir]:
        os.makedirs(directory, exist_ok=True)

    # 3. Copy Shared Standards
    print("[+] Porting shared standards and principles...")
    shared_src = os.path.join(src_root, "shared")
    shared_dest = os.path.join(target_docs_dir, "shared")
    if os.path.exists(shared_src):
        if os.path.exists(shared_dest):
            shutil.rmtree(shared_dest)
        shutil.copytree(shared_src, shared_dest)
        print("    - Copy complete: docs/loops/shared/")

    # 4. Contextual Loop Selection
    print("[+] Porting contextual loop workflows...")
    manifest_path = os.path.join(src_root, "shared", "loops-manifest.json")
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                loops_map = json.load(f)
        except Exception as e:
            print(f"Error reading manifest: {e}")
            loops_map = {}
    else:
        print(f"Warning: Manifest file not found at {manifest_path}. Using empty map.")
        loops_map = {}


    if project_type == "All":
        loops_src = os.path.join(src_root, "loops")
        if os.path.exists(loops_src):
            for item in os.listdir(loops_src):
                s = os.path.join(loops_src, item)
                d = os.path.join(target_docs_dir, item)
                if os.path.isdir(s):
                    if os.path.exists(d):
                        shutil.rmtree(d)
                    shutil.copytree(s, d)
                else:
                    shutil.copy(s, d)
            print("    - Copied all loops recursively to docs/loops/")
    else:
        selected_loops = loops_map[project_type]
        for loop_path in selected_loops:
            full_src = os.path.join(src_root, "loops", loop_path)
            if os.path.exists(full_src):
                category = os.path.dirname(loop_path)
                category_dest = os.path.join(target_docs_dir, category)
                os.makedirs(category_dest, exist_ok=True)
                shutil.copy(full_src, category_dest)
                print(f"    - Imported loop: {loop_path}")
            else:
                print(f"Warning: Loop file not found at {full_src}")

    # 5. Provision Templates
    print("[+] Porting templates and Agent rules...")
    template_src = os.path.join(src_root, "templates")
    template_dest = os.path.join(target_agents_dir, "templates")
    if os.path.exists(template_src):
        if os.path.exists(template_dest):
            shutil.rmtree(template_dest)
        shutil.copytree(template_src, template_dest)
        
        agents_dest = os.path.join(target_agents_dir, "AGENTS.md")
        if not os.path.exists(agents_dest):
            template_base = os.path.join(template_src, "AGENTS-TEMPLATE.md")
            if os.path.exists(template_base):
                shutil.copy(template_base, agents_dest)
                print("    - Created base .agents/AGENTS.md")

        budget_dest = os.path.join(target_agents_dir, "loop-budget.md")
        if not os.path.exists(budget_dest):
            budget_base = os.path.join(template_src, "loop-budget.md")
            if os.path.exists(budget_base):
                shutil.copy(budget_base, budget_dest)
                print("    - Created base .agents/loop-budget.md")

        log_dest = os.path.join(target_agents_dir, "loop-run-log.md")
        if not os.path.exists(log_dest):
            log_base = os.path.join(template_src, "loop-run-log.md")
            if os.path.exists(log_base):
                shutil.copy(log_base, log_dest)
                print("    - Created base .agents/loop-run-log.md")

    # 6. Copy Programmatic Rule Engine & code
    print("[+] Porting rule engine execution library...")
    code_src = os.path.join(src_root, "code")
    if os.path.exists(code_src):
        # Remove target code dir contents first to avoid merge noise
        if os.path.exists(target_code_dir):
            shutil.rmtree(target_code_dir)
        shutil.copytree(code_src, target_code_dir)
        print("    - Copy complete: RajaJeevanLoopEngineering/code/")

        # Copy gradle wrappers
        for wrapper in ["gradlew", "gradlew.bat"]:
            w_src = os.path.join(src_root, wrapper)
            if os.path.exists(w_src):
                shutil.copy(w_src, target_code_dir)
                os.chmod(os.path.join(target_code_dir, wrapper), 0o755)
        
        gradle_folder = os.path.join(src_root, "gradle")
        if os.path.exists(gradle_folder):
            shutil.copytree(gradle_folder, os.path.join(target_code_dir, "gradle"))
            print("    - Added standalone Gradle wrapper files.")

    # 7. Configure Dev Container settings
    print("[+] Setting up Dev Container environment...")
    devcontainer_file = os.path.join(target_devcontainer_dir, "devcontainer.json")
    setup_script_file = os.path.join(target_devcontainer_dir, "devcontainer-setup.sh")

    with open(devcontainer_file, 'w', encoding='utf-8') as f:
        json.dump(get_devcontainer_json(), f, indent=2)
    print("    - Generated .devcontainer/devcontainer.json with secure sandboxing")

    with open(setup_script_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(get_setup_script_sh())
    os.chmod(setup_script_file, 0o755)
    print("    - Generated .devcontainer/devcontainer-setup.sh")

    print()
    print("=== Configuration Ported Successfully! ===")
    print("To execute loops:")
    print("  1. Open target project in VS Code.")
    print("  2. Reopen in Container.")
    print("  3. The container will automatically compile rules and cache dependencies.")
    print("==========================================")

if __name__ == '__main__':
    main()
