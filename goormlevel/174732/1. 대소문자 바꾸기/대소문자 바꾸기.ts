// Run by Node.js
import * as readline from 'readline';

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let answer = "";
	let inputedData = [];
	
	for await (const line of rl) {
		inputedData.push(line)
		rl.close();
	}
	
	let num:number = parseInt(inputedData[0], 10)
	let str:string = inputedData[1]
	
	for(const s of str){
		if(s.toUpperCase() == s) answer += s.toLowerCase();
		else answer += s.toUpperCase();
	}
	
	console.log(answer)
	
	process.exit();
})();
