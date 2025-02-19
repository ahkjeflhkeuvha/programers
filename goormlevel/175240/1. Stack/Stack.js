// Run by Node.js
const readline = require('readline');

let stack = [];

function push(n, M) {
	if(stack.length == M) return "Overflow";
	else stack.push(n);
}

function pop() {
	if(stack.length == 0) return "Underflow";
	else return stack.pop();
}

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
	}
	rl.close();
	
	let [N, M] = input[0].split(" ");
	let commands = input.slice(1);
	
	for(let i in commands) {
		let command = commands[i].split(" ");
		
		if(command[0] == "push") {
			let res = push(parseInt(command[1], 10), M);
			
			if(res != undefined) console.log(res);
		} else {
			console.log(pop())
		}
	}
	
	process.exit();
})();
