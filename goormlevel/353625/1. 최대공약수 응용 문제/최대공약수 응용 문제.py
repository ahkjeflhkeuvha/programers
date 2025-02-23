import math, sys

N, M = map(int, sys.stdin.readline().strip().split())
tot = 1

for i in range(1, N + 1):
	for j in range(1, M + 1):
		tot *= math.gcd(i, j)
		
print(tot % 1000000007)