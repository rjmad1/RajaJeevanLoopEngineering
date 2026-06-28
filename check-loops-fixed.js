const fs = require('fs');
const content = fs.readFileSync('remote-loops-quick-reckoner.html', 'utf8');
const match = content.match(/const loops = (\[.*?\]);/s);
const remoteLoops = JSON.parse(match[1]);

const glob = require('fs').readdirSync('./loops', {recursive: true, withFileTypes: true});
const localFiles = glob.filter(f => f.isFile() && f.name.endsWith('.md') && f.name.startsWith('LOOP'));

let differences = 0;

for (const loop of remoteLoops) {
    const file = localFiles.find(f => f.name.includes(loop.id));
    if (!file) {
        console.log('Missing local file for ' + loop.id);
        differences++;
        continue;
    }
    const fullPath = file.parentPath + '\\' + file.name;
    const localContent = fs.readFileSync(fullPath, 'utf8');
    
    // Some basic checks
    if (!localContent.includes(loop.name)) {
        console.log(loop.id + ' Name mismatch in file ' + fullPath);
        differences++;
    }
}
console.log('Total differences found: ' + differences);
