def solution(n):
    if n % 2 != 0: 
        return 0
    dp = [1, 3, 11]
    
    p = max(n//2, 0)
    
    for i in range(p-2):
        dp.append((4 * dp[-1] - dp[-2]) % 1000000007)
        
    return dp[1] if n == 2 else dp[-1]