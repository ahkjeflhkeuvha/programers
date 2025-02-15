import sys
N, M = map(int, input().split())

nev_p = {}

for _ in range(N+M):
    p = sys.stdin.readline().strip()

    if p not in nev_p:
        nev_p[p] = 1
    else:
        nev_p[p] += 1

cnt = 0
peo = []


for key, val in nev_p.items():
    if val == 2:
        cnt += 1
        peo.append(key)

print(cnt)
peo.sort()
for t in peo:
    print(t)