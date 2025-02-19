// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
	}
	rl.close();
	
	
	let data = input.slice(1).map((v, i) => [i+1, ...v.split(" ").map(Number)]);
	data.sort((a, b) => {
		if(a[1] / a[2] != b[1] / b[2]) return b[1]/b[2] - a[1]/a[2]
		else {
			if(a[1] == b[1]) return a[0] - b[0]
			else return b[1] - a[1]
		}
	});
	
	// console.log(data)
	console.log(data[0][0]);
	
	process.exit();
})();
