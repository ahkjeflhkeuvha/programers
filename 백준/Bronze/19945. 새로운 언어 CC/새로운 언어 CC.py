import sys

N = int(sys.stdin.readline().strip())

if N > 0:
    print(len(bin(N)) - 2)
elif N == 0:
    print(1)
else:
    print(32)