N, M = map(int ,input().split())


def recombination(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for (i, num) in enumerate(arr):
        for j in recombination(arr[i:], n-1):
            result.append(([num] + j))

    return result

res = recombination(list(range(1, N + 1)), M)

for temp in res:
    for t in temp:
        print(t, end = " ")
    print()