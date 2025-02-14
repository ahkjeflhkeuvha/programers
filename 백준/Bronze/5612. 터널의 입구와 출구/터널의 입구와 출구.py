n = int(input())
m = int(input())

diff = m
res = m
for i in range(n):
    e, o = map(int, input().split())
    diff = diff + e - o

    res = 0 if diff < 0 else max(res, diff)
    if res == 0:
        break

print(res)