import os
import shutil

def sync():
    workspace = r"c:\Users\rajaj\Projects\RajaJeevanLoopEngineering"
    loops_dir = os.path.join(workspace, "loops")
    docs_dir = os.path.join(workspace, "docs")
    wiki_dir = os.path.join(workspace, "RajaJeevanLoopEngineering.wiki")
    
    if not os.path.exists(wiki_dir):
        print(f"Error: Wiki directory does not exist at {wiki_dir}")
        return
        
    copied_loops = 0
    # 1. Sync all loops markdown files (recursive to flat)
    for root, dirs, files in os.walk(loops_dir):
        for file in files:
            if file.endswith('.md'):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(wiki_dir, file)
                shutil.copy2(src_path, dest_path)
                copied_loops += 1
                
    copied_docs = 0
    # 2. Sync all docs markdown files (flat to flat)
    for file in os.listdir(docs_dir):
        if file.endswith('.md'):
            src_path = os.path.join(docs_dir, file)
            dest_path = os.path.join(wiki_dir, file)
            shutil.copy2(src_path, dest_path)
            copied_docs += 1
            
    print(f"Sync complete:")
    print(f"  - Copied {copied_loops} loop spec files from 'loops/' to wiki root.")
    print(f"  - Copied {copied_docs} doc files from 'docs/' to wiki root.")

if __name__ == '__main__':
    sync()
