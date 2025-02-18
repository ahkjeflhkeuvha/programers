// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
	}
	rl.close();
	
	let removeWord = input[1];
	let sen = input[2];
	const regexp = new RegExp(`(${removeWord})`);
	
	while(sen.indexOf(removeWord) > -1) {
		sen = sen.replace(regexp, '')			
	}
	
	if(sen.length == 0) sen = "EMPTY";
	console.log(sen)
	
	process.exit();
})();
