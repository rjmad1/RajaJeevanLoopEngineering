import os
import re
from pathlib import Path

ROOT = Path(".")
LOOPS_DIR = ROOT / "loops"

def load_canonical_loops():
    loops = set()
    for root_dir, dirs, files in os.walk(LOOPS_DIR):
        for file in files:
            if file.endswith(".md"):
                id_match = re.search(r"(LOOP-\d+)", file)
                if id_match:
                    loops.add(id_match.group(1))
    return loops

def validate_loop(file_path, canonical_loops):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    validation_results = {
        "logical_correctness": True, # Ensure no duplicate sections
        "dependencies": True,        # Ensure dependencies resolve
        "prompt_consistency": True,  # Ensure our injected prompts exist
        "errors": []
    }

    # 1. Verify Logical Correctness (Check for duplicate sections)
    sections = re.findall(r"^##\s+(.*)$", content, re.MULTILINE)
    if len(sections) != len(set(sections)):
        validation_results["logical_correctness"] = False
        validation_results["errors"].append("Duplicate markdown sections found.")

    # 2. Verify Dependencies
    dep_pattern = re.search(r"\*\*Depends On:\*\*(.*)", content)
    if dep_pattern:
        deps = dep_pattern.group(1).strip()
        if deps.lower() != "none" and deps != "Unknown":
            for dep in deps.split(","):
                d = dep.strip().split(" ")[0]
                if d.startswith("LOOP-") and d not in canonical_loops:
                    validation_results["dependencies"] = False
                    validation_results["errors"].append(f"Broken dependency: {d} is not a registered loop.")

    # 3. Verify Prompt Consistency & Determinism
    # If the modernization ran, these should exist in the sections
    if "## Agents" in content and "Role Context:" not in content:
        validation_results["prompt_consistency"] = False
        validation_results["errors"].append("Missing Agent Role Prompting.")
        
    if "## Deliverables" in content and "Strict Output Schema:" not in content:
        validation_results["prompt_consistency"] = False
        validation_results["errors"].append("Missing Output Schema Enforcement.")

    return validation_results

def main():
    canonical_loops = load_canonical_loops()
    
    total_validated = 0
    passed = 0
    failed_loops = []

    for root_dir, dirs, files in os.walk(LOOPS_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root_dir, file)
                total_validated += 1
                
                results = validate_loop(file_path, canonical_loops)
                if not results["errors"]:
                    passed += 1
                else:
                    failed_loops.append((file, results["errors"]))
                    
    print(f"Validation Phase 7 complete.")
    print(f"Total Loops Validated: {total_validated}")
    print(f"Passed: {passed}")
    print(f"Failed: {len(failed_loops)}")
    
    if failed_loops:
        print("\nFailures:")
        for file, errs in failed_loops:
            print(f"- {file}: {', '.join(errs)}")

if __name__ == "__main__":
    main()
