N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
dp = [row[:] for row in triangle]

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])