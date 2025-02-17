// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
	}
	
	rl.close();
	
	let removeNum = input[0].split(" ")[1];
	let numArr = input[1].split(" ");
	
	let cnt = 0;
	
	for(let num of numArr) {
		if(num.indexOf(removeNum) < 0) cnt++
	}
	
	console.log(cnt)
	process.exit();
})();
