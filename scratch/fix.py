import re
import os

for html_file in ['docs/loops-quick-reckoner.html', 'remote-loops-quick-reckoner.html']:
    if not os.path.exists(html_file):
        continue
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace .info-btn
    new_info_btn = '''    .info-btn {
        background: var(--surface-hover);
        border: 1px solid var(--border);
        color: var(--primary);
        cursor: pointer;
        font-size: 0.9rem;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-left: 0.5rem;
        vertical-align: middle;
        transition: all 0.2s;
        font-weight: bold;
        font-family: monospace;
    }
    .info-btn:hover {
        background: var(--primary);
        color: white;
        transform: scale(1.1);
        border-color: var(--primary-hover);
    }'''
    
    # We replace the whole info-btn rule to hover rule
    content = re.sub(r'\.info-btn\s*\{.*?\.info-btn:hover\s*\{.*?\}', new_info_btn, content, flags=re.DOTALL)
    
    # Add h1 rule in modal
    if '.modal-body h1' not in content:
        h1_css = '''    .modal-body h1 {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text);
        background: none;
        -webkit-text-fill-color: initial;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid var(--border);
        padding-bottom: 0.5rem;
    }
    '''
        content = content.replace('</style>', h1_css + '</style>')
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated CSS in {html_file}')
