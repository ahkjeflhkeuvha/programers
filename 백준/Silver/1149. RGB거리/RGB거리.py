N = int(input())

c = [list(map(int, input().split())) for _ in range(N)]
dp = [[float('inf'), float('inf'), float('inf')] for _ in range(N)]

for i in range(3):
    dp[0][i] = c[0][i]

for i in range(1, N):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = min(dp[i][j], c[i][j] + dp[i-1][k])

print(min(dp[-1]))