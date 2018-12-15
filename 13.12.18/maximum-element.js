function processData(input) {
    const stack = [];
    const lines = input.split("\n");
    lines.shift();
    const commands = lines.map(line => {
        const splited = line.split(' ');
        const command = splited[0];
        if (command === '1') {
            const element = splited[1];
            stack.push(element);
        } else if (command === '2') {
            stack.pop();
        } else if (command === '3') {
            const curMax = Math.max(...stack);
            console.log(curMax);
        }
    })
    
        
}

let input = `10
1 97
2
1 20
2
1 26
1 20
2
3
1 91
3`;

processData(input);