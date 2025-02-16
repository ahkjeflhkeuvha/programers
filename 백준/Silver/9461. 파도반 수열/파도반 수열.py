# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21


import sys

T = int(input())
PN = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21]

for _ in range(T):
    N = int(sys.stdin.readline().strip())

    cnt = 0
    while len(PN) < N:
        PN.append(PN[-1] + PN[len(PN) - 5])
        cnt += 1
    
    print(PN[N-1])