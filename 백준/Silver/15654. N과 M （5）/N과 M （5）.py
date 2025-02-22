N, M = map(int, input().split())
arr = list(map(int, input().split()))

def permutation(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for i, num in enumerate(arr):
        for j in permutation(arr[:i] + arr[i+1:], n - 1):
            result.append([num] + j)

    return result

arr.sort()
res = permutation(arr, M)

for temp in res:
    for t in temp:
        print(t, end=" ")
    print()