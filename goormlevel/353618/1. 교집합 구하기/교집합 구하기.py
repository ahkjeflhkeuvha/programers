import sys

N, M = map(int, sys.stdin.readline().strip().split())

a = set(list(map(int, sys.stdin.readline().strip().split())))
b = set(list(map(int, sys.stdin.readline().strip().split())))

c = list(sorted(list(a & b)))
print(len(c))
print(*c)
