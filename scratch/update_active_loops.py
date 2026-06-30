import os
import re

def update_loop_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Standardize newlines
    content = content.replace('\r\n', '\n')
    
    # Check if already updated
    if '## Scheduling' in content:
        print(f"Skipping {filepath} (already updated)")
        return False
        
    # Extract Loop ID
    loop_id_match = re.search(r'Loop ID:\*\* (LOOP-\d+|LOOP-XXX)', content)
    if not loop_id_match:
        loop_id_match = re.search(r'# (LOOP-\d+)', content)
    loop_id = loop_id_match.group(1) if loop_id_match else "LOOP-XXX"
    
    # 1. Insert Scheduling before Preconditions
    scheduling_block = f"""---

## Scheduling

- **Cadence:** On-demand / Trigger-based
- **First Run Behavior:** Fire immediately on start
- **Durability:** Durable (survives session restarts via status file)
- **Off-Hours Behavior:** Paused overnight
- **Self-Cleanup:** Automatically deletes scheduler when watchlist is empty

"""
    # Replace Preconditions with Scheduling + Preconditions
    if '\n---\n\n## Preconditions' in content:
        content = content.replace('\n---\n\n## Preconditions', scheduling_block + '## Preconditions')
    elif '\n## Preconditions' in content:
        content = content.replace('\n## Preconditions', scheduling_block + '## Preconditions')
        
    # 2. Insert Connectors before Required Context
    connectors_block = f"""---

## Connectors (MCP)

- **Required Servers:** github-server, filesystem-server
- **Permissions:** Read-only access to source code, Write access to docs/loops/
- **PR/Ticket Operations:** Allowed to open/update PRs, create issues, and add comments
- **Identity:** Bot Identity: "AEOS Loop Engine — {loop_id}"

"""
    if '\n---\n\n## Required Context' in content:
        content = content.replace('\n---\n\n## Required Context', connectors_block + '## Required Context')
    elif '\n## Required Context' in content:
        content = content.replace('\n## Required Context', connectors_block + '## Required Context')
        
    # 3. Insert Cost & Limits and Safety before Stop Conditions
    cost_safety_block = f"""---

## Cost & Limits

- **Token Budget:** Estimated budget of 500k tokens per run
- **Daily Budget Cap:** Daily cap of $5.00 across all runs, checked via loop-budget.md
- **Max Iterations:** Max 5 iterations per item per run
- **Max Auto-PRs:** Max 3 auto-PRs per day
- **Kill Switch Criteria:** Immediate halt if spending exceeds budget or loop iterations exceed 5

---

## Safety

- **Auto-Merge Policy:** No auto-merge allowed; human checker must approve PR merge
- **Secrets/Env Denylist:** Git changes to .env, keys, credentials, config/secrets are forbidden
- **Flake Handling:** Do not retry flaky tests; isolate and log test failure for manual triage

"""
    if '\n---\n\n## Stop Conditions' in content:
        content = content.replace('\n---\n\n## Stop Conditions', cost_safety_block + '## Stop Conditions')
    elif '\n## Stop Conditions' in content:
        content = content.replace('\n## Stop Conditions', cost_safety_block + '## Stop Conditions')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully updated {filepath}")
    return True

def main():
    loops_dir = r"c:\Users\rajaj\Projects\RajaJeevanLoopEngineering\loops"
    count = 0
    for root, dirs, files in os.walk(loops_dir):
        for file in files:
            if file.endswith('.md') and not file.startswith('README'):
                filepath = os.path.join(root, file)
                if update_loop_file(filepath):
                    count += 1
    print(f"Total loops updated: {count}")

if __name__ == '__main__':
    main()
