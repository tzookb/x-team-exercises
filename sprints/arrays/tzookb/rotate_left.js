
function rotLeft(a, d) {
    const origLen = a.length;
    const minRotate = d % origLen;
    return [...a.slice(minRotate, origLen), ...a.slice(0, minRotate)]
}

console.log(rotLeft([1,2,3,4,5], 7));
