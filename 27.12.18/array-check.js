const n = 1000000;
let loops = new Array(n).fill(0);

console.time('for')
for (let i=0; i<n; i++) {
    let x = loops[i];
}
console.timeEnd('for')

console.time('while')
let i=0;
while (i<n) {
    let x = loops[i];
    i++;
}
console.timeEnd('while')

console.time('foreach')
loops.forEach(element => {
    let x = element;
});
console.timeEnd('foreach')

console.time('map')
loops.map(element => {
    let x = element;
});
console.timeEnd('map')

console.time('for of')
for (element of loops) {
    let x = element;
};
console.timeEnd('for of')