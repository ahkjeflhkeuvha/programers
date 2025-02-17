// Run by Node.js
import * as readline from 'readline';

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		let s1:string = line.toString();
		console.log(s1.length)
		rl.close();
	}
	
	process.exit();
})();
