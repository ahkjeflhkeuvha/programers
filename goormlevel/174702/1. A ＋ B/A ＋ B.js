// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let inputedData;
	
	for await (const line of rl) {
		inputedData = line
		rl.close();
	}
	
	console.log(parseInt(inputedData.split(" ")[0], 10) + parseInt(inputedData.split(" ")[1], 10))
	
	process.exit();
})();
