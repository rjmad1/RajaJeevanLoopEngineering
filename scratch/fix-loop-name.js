const fs = require('fs');

const files = [
    'remote-loops-quick-reckoner.html',
    'docs/loops-quick-reckoner.html'
];

for (const file of files) {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, 'utf8');
        if (content.includes('"name": "Doc Governance"')) {
            content = content.replace('"name": "Doc Governance"', '"name": "Documentation Governance"');
            fs.writeFileSync(file, content, 'utf8');
            console.log('Successfully updated ' + file);
        } else {
            console.log('Could not find string in ' + file);
        }
    } else {
        console.log('File does not exist: ' + file);
    }
}
