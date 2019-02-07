function workit(commands) {
    const history = [];
    let content = '';

    commands.map(command => {
        if (command === '') {
            return;
        }
        [action, arg] = command.split(' ');
        if (action == 1) {
            history.push(content);
            content += arg;
        } else if (action == 2) {
            history.push(content);
            content = content.substring(0, content.length-arg);
        } else if (action == 3) {
            console.log(content[arg-1]);
            
        } else if (action == 4) {
            content = history.pop();
        }
        // console.log(history);
        
    })
    
}
function processData(input) {
    let res = workit(input.split("\n"));
} 

input = `
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1
`;

let res = processData(input)
