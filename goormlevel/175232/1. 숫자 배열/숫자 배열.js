// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let num;
	
	for await (const line of rl) {
		num = parseInt(line, 10);
		rl.close();
	}
	
	let arr = Array.from({length : num*num}, (v, i) => i+1);
	let answer = "";
	
	for(let i = 0; i<arr.length; i++) {
		answer += arr[i].toString();
		if((i+1)%num == 0) answer += "\n";
		else answer += " ";
	}
	
	console.log(answer)
	
	process.exit();
})();
