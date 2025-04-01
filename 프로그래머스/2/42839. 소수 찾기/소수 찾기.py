from itertools import permutations
import math

def is_prime_number(n):
    array = [True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]

def solution(numbers):
    answer = 0
    arr = set()
    
    for i in range(len(numbers)):
        arr.update([int(''.join(a)) for a in list(permutations(list(numbers), i+1))])
    
    primes = is_prime_number(max(list(arr)))
    for num in list(arr):
        if num in primes:
            answer += 1
    return answer