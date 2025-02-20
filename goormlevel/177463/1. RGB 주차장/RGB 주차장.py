MOD = 100000007

N = int(input())
dp = [3]*(N+1)
for i in range(2, N+1):
	dp[i] = (dp[i-1]*2) % MOD
print(dp[N]%MOD)