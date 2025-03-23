import sys

N = int(sys.stdin.readline().strip())
tot = 0

for _ in range(N):
    tot += int(sys.stdin.readline().strip())

print(tot)