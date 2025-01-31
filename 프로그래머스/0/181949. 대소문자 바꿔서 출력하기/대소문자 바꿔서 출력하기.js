const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    let str = ""
    for(let s of line) {
        if(s.toLowerCase() == s) str += s.toUpperCase()
        else str += s.toLowerCase()
    }
    console.log(str)
    input = [str];
    
}).on('close',function(){
    str = input[0];
});