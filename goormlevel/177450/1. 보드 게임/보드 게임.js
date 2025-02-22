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

	let dp = new Array(n + 1).fill(0);
	
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2
	
	for(let i = 3; i<=n; i++){
		dp[i] = (dp[i-1] + dp[i-3]) % 1000000007;
	}
	
	console.log(dp[n-1]);
	
	process.exit();
})();
