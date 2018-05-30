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

function mergeSort(array, item) {
    let a = 0;
    let b = array.length;
    
    while (a !== b) {
        const m = Math.floor((a + b) / 2);
        if (array[m] < item) {
            a = m + 1;
        } else {
            b = m;
        }
    }
    array.splice(a, 0, item);
}


function main() {
    const n = Number.parseInt(readLine(), 10);

    const array = [];

    for (let i = 0; i < n; ++i) {
        const item = Number.parseInt(readLine(), 10);
        mergeSort(array, item);
        
        const j = Math.floor(i / 2);
        if (i % 2 === 0) { // even
            console.log(array[j].toFixed(1));
        } else { // odd
            console.log(((array[j] + array[j+1]) / 2).toFixed(1));
        }
    }
}

