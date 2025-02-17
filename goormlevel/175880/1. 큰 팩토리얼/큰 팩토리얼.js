const readline = require("readline");

const MOD = 1000000007n;

function factorial(n) {
  let result = 1n;
  for (let i = 2; i <= n; i++) {
    result = (result * BigInt(i)) % MOD;
  }
  return result;
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let num;

  for await (const line of rl) {
    num = parseInt(line, 10);
    rl.close();
  }

  let str = factorial(num).toString();
  console.log(str);

  process.exit();
})();
