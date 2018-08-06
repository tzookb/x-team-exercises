
function arrayValsToObjectKeys(arr) {
	const newObj = {};

	arr.map(val => {
		if (val in newObj) {
			newObj[val] = newObj[val] + 1;	
		} else {
			newObj[val] = 1;
		}
	});

	return newObj;
}

function solve(magazine, ransome) {
	const magazineDict = arrayValsToObjectKeys(magazine);
	const ransomeDict = arrayValsToObjectKeys(ransome);
    
    for (let key in ransomeDict) {

    	if (key in magazineDict && magazineDict[key] >= ransomeDict[key]) {
    		//all good
    	} else {
    		return false;
    	}
    }
    return true;
}

function main() {
    var m_temp = readLine().split(' ');
    var m = parseInt(m_temp[0]);
    var n = parseInt(m_temp[1]);
    magazine = readLine().split(' ');
    ransom = readLine().split(' ');

    const result = solve(magazine, ransom);
    if (result) {
        console.log("Yes");
    } else {
        console.log("No");
    }
}
