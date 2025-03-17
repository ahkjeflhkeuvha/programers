import math

def solution(arrayA, arrayB):
    answer = 0
    tempA, tempB = arrayA[0], arrayB[0]
    for i in range(1, len(arrayA)):
        tempA = math.gcd(tempA, arrayA[i])
        tempB = math.gcd(tempB, arrayB[i])
    
    flagA = all(arrayB[i] % tempA != 0 for i in range(len(arrayB)))
    flagB = all(arrayA[i] % tempB != 0 for i in range(len(arrayA)))
    
    print(flagA, tempA, flagB, tempB)
    
    return max(0, tempA if flagA else -1, tempB if flagB else -1)