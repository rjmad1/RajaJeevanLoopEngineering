import re
import os

filepath = 'docs/loops-quick-reckoner.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add output-mode select
controls_insertion = """        <div class="control-group">
            <label for="output-mode">Output Mode</label>
            <select id="output-mode" onchange="toggleMode()">
                <option value="cli">CLI Commands</option>
                <option value="ide">Intelligent IDE Prompt</option>
            </select>
        </div>
    </div>"""

content = content.replace('    </div>\n\n    <div class="loops-grid" id="grid">', controls_insertion + '\n\n    <div class="loops-grid" id="grid">')

# First, add a class 'cli-mode' to existing copy-containers.
content = content.replace('class="copy-container"', 'class="copy-container cli-mode"')

# Now, after the PS cli-mode copy-container, insert the ide-mode container.
def repl(match):
    loop_id = match.group(2)
    # create the ide mode container
    ide_prompt = f"Loop: {loop_id}\\nGoal: [Enter goal here]\\nTask: [Enter task details here]\\nContext: [Enter context here]\\nConstraints: [Enter constraints here]"
    
    ide_html = f"""
            <div class="copy-container ide-mode hidden">
                <span class="command-text" title='{ide_prompt}'>IDE Loop Instruction Template</span>
                <button class="copy-btn" onclick="copyCommand(this, '{ide_prompt}')">Copy IDE Text</button>
            </div>
        </div>"""
    
    return match.group(1) + ide_html

content = re.sub(r'(<div class="copy-container cli-mode">\s*<span class="command-text" title=\'Invoke-Loop -Id (LOOP-\d+) -Target "<target_path>"\'>.*?</div>\s*)</div>', repl, content)

# Add Javascript for toggleMode
js_insertion = """
    function toggleMode() {
        const mode = document.getElementById('output-mode').value;
        if (mode === 'ide') {
            document.querySelectorAll('.cli-mode').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.ide-mode').forEach(el => el.classList.remove('hidden'));
        } else {
            document.querySelectorAll('.ide-mode').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.cli-mode').forEach(el => el.classList.remove('hidden'));
        }
    }
"""

content = content.replace("</script>", js_insertion + "</script>")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
