const readline = require('readline');

let sA = [0, 1];  // 첫 두 피보나치 수

const MOD = 1000000007; // 나머지 값

function sequence(num) {
    // num 번째 피보나치 수를 구하기 위한 반복문
    while (sA.length <= num) {
        let res = (sA[sA.length - 1] + sA[sA.length - 2]) % MOD;
        sA.push(res);
    }
    return sA[num-1];  // 1-based index로 반환
}

(async () => {
    let rl = readline.createInterface({ input: process.stdin });
    let input;

    for await (const line of rl) {
        input = parseInt(line, 10);  // 입력값을 숫자로 변환
        rl.close();
    }

    console.log(sequence(input));  // 결과 출력 (1000000007로 나눈 나머지)

    process.exit();
})();
