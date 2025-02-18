// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
	}
	rl.close();
	
	let n = parseInt(input[0], 10);
	let arr = input.slice(1).map((v) => v.split(" ").map((v) => Number(v)));
	let x, y;
	
	for(let i in arr) {
		for(let j in arr[i]) {
			if(arr[i][j] == 0) [x, y] = [i, j]
		}
	}
	
	let sum = 0;
	
	for(let k in arr) sum += arr[x][k] + arr[k][y];
	
	console.log(sum);

	process.exit();
})();
