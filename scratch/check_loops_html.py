import re
with open('docs/loops-quick-reckoner.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find loop cards
cards = re.findall(r'<div class="loop-card.*?</p>\s*</div>\s*</div>\s*</div>', text, re.DOTALL)
print(f'Found {len(cards)} cards')
for card in cards:
    desc = re.search(r'<p class="loop-desc">(.*?)</p>', card, re.DOTALL)
    id_match = re.search(r'data-id="(.*?)"', card)
    loop_id = id_match.group(1) if id_match else 'Unknown'
    
    if desc and not desc.group(1).strip():
        print(f'Empty loop desc: {loop_id}')
    if 'No context available' in card or 'No detailed description available' in card:
        print(f'Empty detailed context: {loop_id}')
