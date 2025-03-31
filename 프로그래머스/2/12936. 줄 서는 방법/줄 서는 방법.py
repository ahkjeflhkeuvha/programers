import math

def get_kth_permutation(n, k):
    numbers = list(range(1, n + 1))
    k -= 1
    result = []

    factorial = [math.factorial(i) for i in range(n)]
    
    for i in range(n - 1, -1, -1):
        idx = k // factorial[i]
        result.append(numbers.pop(idx))
        k %= factorial[i]

    return result

def solution(n, k):
    return get_kth_permutation(n, k)