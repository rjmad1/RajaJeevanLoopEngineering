import os
import json
import re
import markdown
from pathlib import Path

ROOT = Path(".")
MANIFEST_PATH = ROOT / "shared" / "loops-manifest.json"
CATALOG_PATH = ROOT / "docs" / "loop-catalog.md"
LOOPS_DIR = ROOT / "loops"

def get_project_types():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    ptypes = {}
    for pt, paths in manifest.items():
        for path in paths:
            match = re.search(r'(LOOP-\d+)', path)
            if match:
                loop_id = match.group(1)
                if loop_id not in ptypes:
                    ptypes[loop_id] = []
                ptypes[loop_id].append(pt)
    return ptypes

def get_catalog():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    loops = {}
    for line in content.split("\n"):
        if line.startswith("|") and "**LOOP-" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 7:
                loop_id = parts[1].replace("**", "")
                name = parts[2]
                category = parts[3]
                complexity = parts[4]
                deps = parts[5]
                desc = parts[6]
                loops[loop_id] = {
                    "id": loop_id,
                    "name": name,
                    "category": category,
                    "complexity": complexity,
                    "dependencies": deps,
                    "description": desc,
                }
    return loops

def get_detailed_desc(loop_id):
    for root, dirs, files in os.walk(LOOPS_DIR):
        for f in files:
            if loop_id in f and f.endswith(".md"):
                with open(os.path.join(root, f), "r", encoding="utf-8") as md_file:
                    content = md_file.read()
                # Remove the metadata headers
                content = re.sub(r'^\*\*.*?\*\*.*?$', '', content, flags=re.MULTILINE)
                content = content.strip()
                return markdown.markdown(content)
    return "No detailed description available."

def main():
    ptypes = get_project_types()
    catalog = get_catalog()
    loops = []
    
    for loop_id, data in catalog.items():
        data["projectTypes"] = ptypes.get(loop_id, [])
        data["detailedDescription"] = get_detailed_desc(loop_id)
        loops.append(data)
        
    loops_json = json.dumps(loops)
    
    for html_file in ["docs/loops-quick-reckoner.html", "remote-loops-quick-reckoner.html"]:
        if os.path.exists(html_file):
            with open(html_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = re.sub(r'const loops = \[.*?\];', f'const loops = {loops_json};', content, flags=re.DOTALL)
            
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {html_file}")

if __name__ == "__main__":
    main()
