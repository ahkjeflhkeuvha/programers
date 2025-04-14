N = int(input())

for _ in range(N):
    k = int(input())
    n = int(input())

    dp = [[i if t == 0 else 0 for i in range(1, n+1)] for t in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(n):
            for p in range(0, j+1):
                dp[i][j] += dp[i-1][p]

    print(dp[k][n-1])