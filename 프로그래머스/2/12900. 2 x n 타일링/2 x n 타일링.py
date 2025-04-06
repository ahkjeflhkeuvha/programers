def solution(n):
    dp = [1, 1, 2]
    
    while len(dp) <= n:
        dp.append((dp[-1] + dp[-2]) % 1000000007)
        
    return dp[n]