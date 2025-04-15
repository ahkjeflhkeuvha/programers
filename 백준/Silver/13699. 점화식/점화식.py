N = int(input())

# t(1)=t(0)*t(0)=1
# t(2)=t(0)*t(1)+t(1)*t(0)=2
# t(3)=t(0)*t(2)+t(1)*t(1)+t(2)*t(0)=5

dp = [0] * (N+1)
dp[0] = 1

for i in range(1, N+1):
    for j in range(0, i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[-1])

