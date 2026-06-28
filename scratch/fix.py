import re, json

files = ['docs/loops-quick-reckoner.html', 'remote-loops-quick-reckoner.html']

book_svg = '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width: 22px; height: 22px;" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>'

exclamation_svg = '<svg fill="none" stroke="#f59e0b" viewBox="0 0 24 24" style="width: 20px; height: 20px; vertical-align: text-bottom; margin-left: 8px;" xmlns="http://www.w3.org/2000/svg" title="Missing Context"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>'

copy_script = """
    // Initialize copy buttons for modal pre tags
    document.querySelectorAll('.modal-overlay pre').forEach(pre => {
        if (pre.parentNode.classList.contains('copy-container')) return; // Already wrapped
        const wrapper = document.createElement('div');
        wrapper.className = 'copy-container';
        wrapper.style.position = 'relative';
        wrapper.style.display = 'block';
        wrapper.style.padding = '0';
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        
        pre.style.margin = '0';
        
        const btn = document.createElement('button');
        btn.className = 'copy-btn';
        btn.innerText = 'Copy';
        btn.style.position = 'absolute';
        btn.style.top = '10px';
        btn.style.right = '10px';
        btn.style.zIndex = '10';
        
        wrapper.appendChild(btn);
        
        btn.onclick = () => {
            const code = pre.querySelector('code');
            const text = code ? code.innerText : pre.innerText;
            copyCommand(btn, text.trim());
        };
    });
"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 1. Update Github icon for Wiki
    pattern = r'(<a href="[^"]*?wiki" target="_blank" class="icon-link" title="GitHub Wiki">\s*)<svg.*?</svg>(\s*</a>)'
    text = re.sub(pattern, r'\g<1>' + book_svg + r'\g<2>', text, flags=re.DOTALL)
    
    # 2. Add copy script if not exists
    if 'Initialize copy buttons for modal pre tags' not in text:
        text = text.replace('searchInput.addEventListener(\'input\', render);', copy_script + '\n    searchInput.addEventListener(\'input\', render);')
    
    # 3. Find empty loops and add exclamation mark
    loops_match = re.search(r'const loops = (\[.*?\]);', text, re.DOTALL)
    if loops_match:
        loops = json.loads(loops_match.group(1))
        for l in loops:
            det = l.get('detailedDescription', '').strip()
            desc = l.get('description', '').strip()
            # If no context/content
            if len(det) < 50 or 'TBD' in det or 'TODO' in det:
                # Find the loop card in HTML
                card_pattern = r'(<div class="loop-card" data-id="' + l['id'] + r'".*?<h3 class="loop-name">)(.*?)(</h3>)'
                def replacer(m):
                    name_content = m.group(2)
                    if 'title="Missing Context"' not in name_content:
                        return m.group(1) + name_content + exclamation_svg + m.group(3)
                    return m.group(0)
                text = re.sub(card_pattern, replacer, text, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Updated {filepath}")
