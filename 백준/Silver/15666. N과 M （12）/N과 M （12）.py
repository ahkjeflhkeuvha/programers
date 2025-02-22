N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def recombination(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for (i, num) in enumerate(arr):
        for j in recombination(arr[i:], n-1):
            result.append([num] + j)

    return result

res = sorted(list(set([tuple(i) for i in recombination(arr, M)])))

for temp in res:
    for t in temp:
        print(t, end = " ")
    print()