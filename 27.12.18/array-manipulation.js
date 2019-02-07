function arrayManipulationGreedy(n, queries) {
    const resArr = new Array(n).fill(0);

    queries.map((action) => {
        const startIdx = action[0]-1;
        const endIdx = action[1]-1;
        const addValue = action[2];
        for (let i=startIdx; i<=endIdx; i++) {
            resArr[i] += addValue
        }
    })

    return Math.max(...resArr);
}

const getMax = arr => {
    let max = 0;
    let sum = 0;
    arr.map((cur) => {  
        sum += cur;
        if (sum > max) {
            max = sum;
        }
    });
    return max;
}

function arrayManipulation(n, queries) {
    const resArr = new Array(n).fill(0);

    for (const [sIdx, eIdx, val] of queries ) {
        resArr[sIdx-1] += val;
        if (eIdx < n) {
            resArr[eIdx] -= val;
        }
    }

    return getMax(resArr);
    
}


const res = arrayManipulation(5, [ [ 1, 2, 100 ], [ 2, 5, 100 ], [ 3, 4, 100 ] ]);
console.log(res);

// console.log(getMax([100,-100,0]));

