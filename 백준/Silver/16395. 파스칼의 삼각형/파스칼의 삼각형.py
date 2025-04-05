N, M = map(int, input().split())

def binomial(n, r):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(N+1):
        for j in range(0, min(i, r) + 1):
            if j == 0 or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    return dp

print(binomial(N, M)[N][M])