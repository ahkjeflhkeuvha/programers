import sys

while True:
    n, v = map(int, sys.stdin.readline().strip().split())
    if n == 0 or v == 0:
        break

    if v % n == 0:
        print('factor')
    elif n % v == 0:
        print('multiple')
    else:
        print('neither')