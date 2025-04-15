N = int(input())

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 2, 1, 2, 3, 4, 2, 1, 2]

dp = [float('inf')] * (N+1) # 최소 경우의 수를 구할 dp 배열
dp[0] = 0
pow_nums = [i**2 for i in range(1, int(N**0.5) + 1)] # 제곱수 리스트 생성

for i in range(1, N+1):
    for square in pow_nums:
        if i >= square:
            dp[i] = min(dp[i], dp[i-square] + 1)

print(dp[N])