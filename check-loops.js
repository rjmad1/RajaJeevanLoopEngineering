const fs = require('fs');
const content = fs.readFileSync('remote-loops-quick-reckoner.html', 'utf8');
const match = content.match(/const loops = (\[.*?\]);/s);
const remoteLoops = JSON.parse(match[1]);

const localFiles = fs.readdirSync('./loops', {recursive: true}).filter(f => f.endsWith('.md') && f.startsWith('LOOP'));

let differences = 0;

for (const loop of remoteLoops) {
    const file = localFiles.find(f => f.includes(loop.id));
    if (!file) {
        console.log(Missing local file for );
        differences++;
        continue;
    }
    const localContent = fs.readFileSync(./loops/, 'utf8');
    
    // Check if the local content contains the description
    // Note: The HTML might have markdown converted to HTML, so an exact match is hard.
    // Let's check for the loop name and complexity.
    if (!localContent.includes(**Name:** )) {
        console.log(${loop.id} Name mismatch);
        differences++;
    }
}
console.log(Total differences found: );
