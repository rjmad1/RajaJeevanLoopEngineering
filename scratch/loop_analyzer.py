import os
import re
import json
from pathlib import Path

ROOT = Path(".")
LOOPS_DIR = ROOT / "loops"

def extract_metadata(content):
    meta = {
        "version": "Unknown",
        "status": "Unknown",
        "category": "Unknown",
        "depends_on": "Unknown"
    }
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("**Version:**"):
            meta["version"] = line.replace("**Version:**", "").strip()
        elif line.startswith("**Status:**"):
            meta["status"] = line.replace("**Status:**", "").strip()
        elif line.startswith("**Category:**"):
            meta["category"] = line.replace("**Category:**", "").strip()
        elif line.startswith("**Depends On:**"):
            meta["depends_on"] = line.replace("**Depends On:**", "").strip()
    return meta

def extract_sections(content):
    sections = []
    # match markdown H2 headers
    pattern = re.compile(r"^##\s+(.*)$", re.MULTILINE)
    for match in pattern.finditer(content):
        sections.append(match.group(1).strip())
    return sections

def analyze_loops():
    inventory = []
    dependencies = {}
    
    for root_dir, dirs, files in os.walk(LOOPS_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root_dir, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Try to extract the loop ID from filename
                loop_id = "Unknown"
                id_match = re.search(r"(LOOP-\d+)", file)
                if id_match:
                    loop_id = id_match.group(1)
                
                meta = extract_metadata(content)
                sections = extract_sections(content)
                
                # Parse dependencies
                deps = []
                dep_str = meta.get("depends_on", "")
                if dep_str and dep_str != "Unknown" and dep_str.lower() != "none":
                    for d in dep_str.split(","):
                        d = d.strip()
                        if d.startswith("LOOP-"):
                            deps.append(d.split(" ")[0])
                
                dependencies[loop_id] = deps
                
                inventory.append({
                    "id": loop_id,
                    "filename": file,
                    "path": str(Path(file_path).relative_to(ROOT)).replace("\\", "/"),
                    "version": meta["version"],
                    "status": meta["status"],
                    "category": meta["category"],
                    "dependencies": deps,
                    "sections": sections
                })
                
    return inventory, dependencies

if __name__ == "__main__":
    inv, deps = analyze_loops()
    
    output = {
        "inventory": inv,
        "dependencies": deps
    }
    
    with open("scratch/loop_analysis.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    
    print(f"Analyzed {len(inv)} loops.")
    print("Output saved to scratch/loop_analysis.json")
