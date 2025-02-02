def solution(land):
    answer = 0
    dp = [[0 for i in range(4)] for i in range(100001)]
    
    n = len(land)
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(n):
        for j in range(4):
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])
    
    for i in range(4):
        answer = max(answer, dp[n-1][i])
    
    return answer