n = int(input())
l = []

for _ in range(n):
    x, y = map(int, input().split())

    l.append([x, y])

l = sorted(l, key= lambda x : (x[0], x[1]))

for x, y in l:
    print(x, y)
