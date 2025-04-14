N = int(input())
memo = {}

def fibo(n):
    if n in memo:
        return memo[n]
    elif n <= 1:
        memo[n] = n
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
    
print(fibo(N))