// Run by Node.js
const readline = require('readline');

let queue = [];

function push(n, M) {
	if(queue.length >= M) return "Overflow";
	else queue.push(n);
}

function pop(M) {
	if(queue.length <= 0) return "Underflow";
	else return queue.shift();
}

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = []
	
	for await (const line of rl) {
		input.push(line);
	}
	rl.close();
	
	let [N, M] = input[0].split(" ");
	let arr = input.slice(1);
	
	for(let el of arr) {
		let temp = el.split(" ");
		
		if(temp[0] == "push") {
			let t = push(temp[1], M)
			
			if(t != undefined) console.log(t);
		}
		else console.log(pop(M))
	}
	
	process.exit();
})();
