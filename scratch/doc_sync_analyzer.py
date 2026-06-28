import os
import json
import re
from pathlib import Path

ROOT = Path(".")
DOCS_DIR = ROOT / "docs"
LOOPS_DIR = ROOT / "loops"

def discover_docs():
    docs = []
    # Discover in ROOT (README, USER_GUIDE, etc)
    for file in ["README.md", "USER_GUIDE.md", "CHANGELOG.md", "architecture.md"]:
        if (ROOT / file).exists():
            docs.append(file)
            
    # Discover in docs/
    for root_dir, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith((".md", ".html")):
                docs.append(str(Path(root_dir, file).relative_to(ROOT)).replace("\\", "/"))
                
    return docs

def load_canonical_loops():
    loops = []
    for root_dir, dirs, files in os.walk(LOOPS_DIR):
        for file in files:
            if file.endswith(".md"):
                id_match = re.search(r"(LOOP-\d+)", file)
                if id_match:
                    loops.append(id_match.group(1))
    return loops

def audit_docs(docs, canonical_loops):
    report = {
        "inventory": docs,
        "missing_quick_reckoner": [],
        "missing_wiki": [],
        "broken_links": [],
        "drift": [],
        "score": 100
    }
    
    # Check Quick Reckoner
    reckoner_path = DOCS_DIR / "loops-quick-reckoner.html"
    if reckoner_path.exists():
        with open(reckoner_path, "r", encoding="utf-8") as f:
            content = f.read()
        for loop in canonical_loops:
            if loop not in content:
                report["missing_quick_reckoner"].append(loop)
                report["score"] -= 1
                report["drift"].append(f"{loop} missing from loops-quick-reckoner.html")
    else:
        report["score"] -= 20
        report["drift"].append("loops-quick-reckoner.html not found")
        
    # Check Catalog
    catalog_path = DOCS_DIR / "loop-catalog.md"
    if catalog_path.exists():
        with open(catalog_path, "r", encoding="utf-8") as f:
            content = f.read()
        for loop in canonical_loops:
            if loop not in content:
                report["score"] -= 0.5
                report["drift"].append(f"{loop} missing from loop-catalog.md")

    # Normalize score
    report["score"] = max(0, min(100, int(report["score"])))
    
    return report

def main():
    docs = discover_docs()
    loops = load_canonical_loops()
    
    report = audit_docs(docs, loops)
    
    with open("scratch/doc_sync_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
        
    print(f"Discovered {len(docs)} documents.")
    print(f"Analyzed {len(loops)} canonical loops.")
    print(f"Documentation Sync Score: {report['score']}%")
    print("Report saved to scratch/doc_sync_report.json")

if __name__ == "__main__":
    main()
