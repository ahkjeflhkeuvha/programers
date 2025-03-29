import sys

N = int(sys.stdin.readline().strip())

xyList = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

xyList.sort(key=lambda x: (x[1], x[0]))

print("\n".join([f"{x} {y}" for x, y in xyList]))

