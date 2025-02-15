import sys

N, M = map(int, input().split())

pass_dict = {}

for _ in range(N):
    site, pw = sys.stdin.readline().strip().split()

    pass_dict[site] = pw


for _ in range(M):
    site = sys.stdin.readline().strip()

    print(pass_dict[site])