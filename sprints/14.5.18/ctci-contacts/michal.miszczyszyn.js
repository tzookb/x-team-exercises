'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

const contacts = new Map();

function main() {
    const n = parseInt(readLine(), 10);

    for (let nItr = 0; nItr < n; nItr++) {
        const opContact = readLine().split(' ');

        const [op, contact] = opContact;
        
        if (op === "add") {
            for (let i = 1; i <= contact.length; ++i) {
                const key = contact.slice(0, i);
                const val = (contacts.get(key) || 0) + 1;
                contacts.set(key, val);
            }
        } else {
            console.log(contacts.get(contact) || 0);
        }
    }
}

