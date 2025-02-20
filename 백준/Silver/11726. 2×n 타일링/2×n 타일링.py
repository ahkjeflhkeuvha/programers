import sys
sys.setrecursionlimit(60000)

N = int(input())

case_arr = [-1 for _ in range(60001)]

def dp(N):
    if case_arr[N] != -1:
        return case_arr[N]
    if N == 0:
        return 1
    if N == 1:
        return 1
    case_arr[N] = (dp(N-1) + dp(N-2)) % 10007
    return case_arr[N]

print(dp(N))
