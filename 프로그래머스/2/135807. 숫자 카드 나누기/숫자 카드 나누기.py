from functools import reduce
from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    tempA, tempB = reduce(gcd, arrayA), reduce(gcd, arrayB)
    
    flagA = all(arrayB[i] % tempA != 0 for i in range(len(arrayB)))
    flagB = all(arrayA[i] % tempB != 0 for i in range(len(arrayA)))
    
    return max(0, tempA if flagA else -1, tempB if flagB else -1)