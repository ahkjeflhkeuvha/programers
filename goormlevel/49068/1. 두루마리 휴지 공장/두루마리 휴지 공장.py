import sys

def chk_length(length, tissues, M):
    needed = sum(max(0, length - tissue) for tissue in tissues)
    return needed <= M

N, M = map(int, sys.stdin.readline().strip().split())
tissues = list(map(int, sys.stdin.readline().strip().split()))

low, high = max(tissues), max(tissues) + M
result = -1

while low <= high:
    mid = (low + high) // 2
    if chk_length(mid, tissues, M):
        result = mid
        low = mid + 1
    else:
        high = mid - 1 

print(result if result >= max(tissues) else 'No way!')
