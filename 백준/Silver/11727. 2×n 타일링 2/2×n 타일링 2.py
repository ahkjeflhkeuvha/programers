N = int(input())

dp = [1, 1, 3]

while len(dp) <= N:
    dp.append((dp[-2] * 2 + dp[-1])%10007)

print(dp[N] % 10007)