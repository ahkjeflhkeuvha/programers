# 1 -> 1 -> 2 -> 3 -> 5 -> 8
def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1) * n
    
n = int(input())

print(factorial(n))