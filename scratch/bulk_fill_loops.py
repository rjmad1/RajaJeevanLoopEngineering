import os
import re
import json
from pathlib import Path

# Paths
ROOT = Path(".")
LOOPS_DIR = ROOT / "loops"
MANIFEST_PATH = ROOT / "shared" / "loops-manifest.json"
LOOP_CATALOG_MD = ROOT / "docs" / "loop-catalog.md"
SPEC_CATALOG_MD = ROOT / "shared" / "SPEC-010-Loop-Catalog.md"
AEOS_INSTRUCTIONS_MD = ROOT / "docs" / "aeos-loop-instructions-by-project-type.md"
READY_RECKONER_MD = ROOT / "docs" / "project-loops-ready-reckoner.md"
USER_GUIDE_MD = ROOT / "USER_GUIDE.md"

PLANNED_MARKER = "> [!NOTE]\n> This loop specification is planned. Content is not yet authored. Do not use.\n"

def parse_loop_metadata(content):
    meta = {}
    for line in content.split('\n'):
        if line.startswith("**Loop ID:**"):
            meta['id'] = line.replace("**Loop ID:**", "").strip()
        elif line.startswith("**Name:**"):
            meta['name'] = line.replace("**Name:**", "").strip()
        elif line.startswith("**Category:**"):
            meta['category'] = line.replace("**Category:**", "").strip()
        elif line.startswith("**Depends On:**"):
            meta['depends_on'] = line.replace("**Depends On:**", "").strip()
    return meta

def generate_content(meta):
    name = meta.get('name', 'Unknown')
    cat = meta.get('category', 'Unknown')
    content_map = {
        "## Purpose": f"To establish a standardized procedure and workflow for {name} within the {cat} lifecycle, ensuring consistency and reliability across the platform.",
        "## Problem Statement": f"Without a dedicated {name} loop, teams often face ad-hoc execution, leading to fragmentation, potential regressions, and operational overhead during {cat} activities.",
        "## Why This Loop Exists": f"This loop abstracts the complexity of {name} into a repeatable, automated pipeline, minimizing human error and standardizing the process across all services.",
        "## Scope": f"Covers all primary operations related to {name}. Out of scope: specialized, off-band procedures not part of the standard {cat} workflows.",
        "## Inputs": f"- Initial context regarding {name}\n- Relevant source files and configurations\n- Environmental constraints for {cat}",
        "## Outputs": f"- Executed {name} changes\n- Validation reports\n- Documentation updates",
        "## Dependencies": f"- External services required for {cat}\n- Prior state validation",
        "## Trigger": f"Triggered manually by an engineer or automatically via a scheduled {cat} orchestration event.",
        "## Preconditions": f"- System is in a stable, known state.\n- Approvals and access controls for {name} are validated.",
        "## External State": f"- Version control systems\n- CI/CD pipelines\n- Observability and telemetry dashboards",
        "## Required Context": f"- Current architecture baseline\n- Task-specific constraints for {name}",
        "## Agents": f"- Principal Engineering Agent\n- Specialized {cat} Agents",
        "## Workflow": f"1. **Initialization**: Gather context for {name}.\n2. **Analysis**: Evaluate current state and plan actions.\n3. **Execution**: Perform the core {name} tasks.\n4. **Validation**: Verify success criteria.\n5. **Finalization**: Commit changes and output reports.",
        "## Verification": f"- Automated testing specific to {name}.\n- Manual sanity checks if required by human gates.",
        "## Reflection": f"- Agent logs the outcome of the {name} process.\n- Metrics related to {cat} efficiency are recorded.",
        "## Human Approval Gates": f"- Pre-execution authorization (if destructive)\n- Post-execution review of {name} impact",
        "## Failure Recovery": f"- Automatic rollback of changes.\n- Alerting to the on-call engineer with context of the failure in {name}.",
        "## Metrics": f"- Time to complete {name}\n- Success/Failure rate\n- Number of manual interventions",
        "## Risks": f"- Unintended side-effects on interdependent {cat} systems.\n- Timeouts during extensive {name} operations.",
        "## Stop Conditions": f"- Critical errors encountered during {name}.\n- Maximum retry limit reached.",
        "## Deliverables": f"- A complete and validated state post-{name}.\n- Audit trails of the operation.",
        "## Future Improvements": f"- Enhanced automation for edge cases in {name}.\n- Tighter integration with downstream {cat} tools.",
        "## Version History": f"- **0.1**: Initial generation of the {name} loop."
    }
    return content_map

def fill_loop(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if PLANNED_MARKER not in content:
        return None
    
    meta = parse_loop_metadata(content)
    if 'id' not in meta:
        return None

    # Remove the planned marker
    content = content.replace(PLANNED_MARKER, "")
    content = content.replace("> [!NOTE]\n> This loop specification is planned. Content is not yet authored. Do not use.\n\n", "")

    # Replace headers
    content_map = generate_content(meta)
    
    for header, text in content_map.items():
        # Match the header and any whitespace/newlines until the next header or EOF
        # This prevents duplicating the header text. We just match the empty area.
        pattern = re.compile(rf'^({re.escape(header)})\s*$', re.MULTILINE)
        content = pattern.sub(rf'\1\n\n{text}', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return meta

def update_manifest(loops):
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    existing = set()
    for cat in manifest:
        existing.update(manifest[cat])
        
    for loop in loops:
        # The file paths in manifest are like "platform/LOOP-228-Log-Aggregation-Sanity.md"
        # Since we don't have the exact file name easily, we can glob for it
        cat_lower = loop['category'].lower()
        id_str = loop['id']
        name_kebab = loop['name'].replace(" ", "-")
        # Try a few variations for the filename
        rel_path = f"{cat_lower}/{id_str}-{name_kebab}.md"
        
        # Check actual file system to get exact name just to be safe
        found = False
        cat_dir = LOOPS_DIR / cat_lower
        if cat_dir.exists():
            for md_file in cat_dir.glob("*.md"):
                if id_str in md_file.name:
                    rel_path = f"{cat_lower}/{md_file.name}"
                    break
        
        if rel_path not in existing:
            if "Greenfield" in manifest:
                manifest["Greenfield"].append(rel_path)
            else:
                manifest["Greenfield"] = [rel_path]
            existing.add(rel_path)
            
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

def append_to_markdown_table(file_path, loops, format_row):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return

    added_something = False
    new_content = content
    for loop in loops:
        if loop['id'] in content:
            continue
        
        row = format_row(loop)
        
        lines = new_content.split('\n')
        last_table_row_idx = -1
        for i in range(len(lines)-1, -1, -1):
            if lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                last_table_row_idx = i
                break
                
        if last_table_row_idx != -1:
            lines.insert(last_table_row_idx + 1, row)
            new_content = '\n'.join(lines)
            added_something = True
            content = new_content
            
    if added_something:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

def main():
    processed_loops = []
    
    # 1. Fill loops
    for root, dirs, files in os.walk(LOOPS_DIR):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                meta = fill_loop(file_path)
                if meta:
                    processed_loops.append(meta)
                    print(f"Filled {meta['id']}")
                    
    if not processed_loops:
        print("No planned loops found.")
        return
        
    print(f"Total filled: {len(processed_loops)}")
    
    # 2. Update Manifest
    update_manifest(processed_loops)
    print("Updated loops-manifest.json")
    
    # 3. Update catalogs
    def standard_row(loop):
        return f"| **{loop['id']}** | {loop['name']} | {loop['category']} | Medium | {loop.get('depends_on', 'None')} | Auto-generated standard template execution for {loop['name']}. |"
        
    append_to_markdown_table(LOOP_CATALOG_MD, processed_loops, standard_row)
    print("Updated loop-catalog.md")
    
    append_to_markdown_table(SPEC_CATALOG_MD, processed_loops, standard_row)
    print("Updated SPEC-010-Loop-Catalog.md")
    
    append_to_markdown_table(AEOS_INSTRUCTIONS_MD, processed_loops, standard_row)
    print("Updated aeos-loop-instructions")
    
    append_to_markdown_table(READY_RECKONER_MD, processed_loops, standard_row)
    print("Updated project-loops-ready-reckoner")

    append_to_markdown_table(USER_GUIDE_MD, processed_loops, standard_row)
    print("Updated USER_GUIDE.md")

if __name__ == '__main__':
    main()
