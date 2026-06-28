import os
import re
from pathlib import Path

ROOT = Path(".")
LOOPS_DIR = ROOT / "loops"

def modernize_loop(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content

    # 1. Role Prompting - Update ## Agents
    # Look for "## Agents" and if not already modernized, append specific role expectations
    if "## Agents" in content and "Role Context:" not in content:
        agent_pattern = re.compile(r"(## Agents.*?)(?=\n## )", re.DOTALL)
        match = agent_pattern.search(content)
        if match:
            old_agents = match.group(1)
            new_agents = old_agents + "\n\n**Role Context:** You are a highly precise, deterministic Agent executing this loop. You must strictly adhere to the Workflow and output schemas. You must not deviate from the defined scope. All actions must be auditable and verifiable."
            content = content.replace(old_agents, new_agents)

    # 2. Output Schema Enforcement - Update ## Deliverables
    if "## Deliverables" in content and "Strict Output Schema:" not in content:
        deliverable_pattern = re.compile(r"(## Deliverables.*?)(?=\n## )", re.DOTALL)
        match = deliverable_pattern.search(content)
        if match:
            old_deliv = match.group(1)
            new_deliv = old_deliv + "\n\n**Strict Output Schema:** All deliverables must be strictly formatted. Markdown artifacts must comply with GitHub Flavored Markdown (GFM). Data payloads must be strictly typed JSON matching the expected schema. No extraneous conversational text is permitted in final artifacts."
            content = content.replace(old_deliv, new_deliv)
            
    # 3. Chain of Verification - Update ## Verification
    if "## Verification" in content and "Self-Verification Chain:" not in content:
        ver_pattern = re.compile(r"(## Verification.*?)(?=\n## )", re.DOTALL)
        match = ver_pattern.search(content)
        if match:
            old_ver = match.group(1)
            new_ver = old_ver + "\n\n**Self-Verification Chain:**\n1. **Format Check:** Verify all outputs against the strict schema.\n2. **Dependency Check:** Ensure all dependencies were satisfied.\n3. **Logic Check:** Confirm no contradictory statements or unresolved placeholders remain.\n4. **Final Affirmation:** The Checker Agent must explicitly affirm \"Verification Passed\" before clearing any Soft or Hard Gate."
            content = content.replace(old_ver, new_ver)

    # 4. Deterministic Execution - Update ## Workflow
    if "## Workflow" in content and "Execution Constraints:" not in content:
        flow_pattern = re.compile(r"(## Workflow.*?)(?=\n## )", re.DOTALL)
        match = flow_pattern.search(content)
        if match:
            old_flow = match.group(1)
            new_flow = old_flow + "\n\n**Execution Constraints:** Execution must be purely deterministic. The agent must proceed sequentially from step 1 to the final step. Parallel execution of sequential steps is forbidden. If a step fails, the agent must immediately proceed to the Failure Recovery procedure."
            content = content.replace(old_flow, new_flow)
            
    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    updated = 0
    for root_dir, dirs, files in os.walk(LOOPS_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root_dir, file)
                if modernize_loop(file_path):
                    updated += 1
                    print(f"Modernized {file}")
                    
    print(f"\nSuccessfully modernized {updated} loops.")

if __name__ == "__main__":
    main()
