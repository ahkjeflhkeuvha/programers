import itertools 

N, M = map(int, input().split())

def combination(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for (i, num) in enumerate(arr):
        for j in combination(arr[i + 1:], n-1):
            result.append(([num] + j))

    return result

result = combination(list(range(1, N + 1)), M)
result.sort(key=lambda x : (x[0]))

for res in result:
    for d in res:
        print(d ,end = " ")
    print()