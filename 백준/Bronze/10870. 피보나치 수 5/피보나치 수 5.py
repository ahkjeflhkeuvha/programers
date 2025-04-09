def fibonacchi(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibonacchi(N-2) + fibonacchi(N-1)
    
N = int(input())
print(fibonacchi(N))