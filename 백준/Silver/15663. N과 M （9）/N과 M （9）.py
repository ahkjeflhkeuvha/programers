N, M = map(int, input().split())
arr = list(map(int, input().split()))

def repermutation(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for (i, num) in enumerate(arr):
        for j in repermutation(arr[:i] + arr[i+1:], n-1):
            result.append(([num] + j))
    
    return result

res = sorted(list(set([tuple(i) for i in repermutation(arr, M)])))

for temp in res:
    for t in temp:
        print(t, end = " ")
    print()