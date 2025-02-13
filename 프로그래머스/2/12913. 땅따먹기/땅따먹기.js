function solution(land) {
    let dp = Array.from(Array(land.length), () => Array(4).fill(0))
    
    for(let i = 0; i<4; i++){
        dp[0][i] = land[0][i]
    }
    
    let n = land.length
    
    for(let i = 1; i<n; i++) {
        for(let j = 0; j<4; j++) {
            for(let k = 0; k<4; k++) {
                if(j !== k) {
                    dp[i][j] = Math.max(dp[i][j], land[i][j] + dp[i-1][k])
                }
            }
        }
    }

    return Math.max(...dp[n-1]);
}