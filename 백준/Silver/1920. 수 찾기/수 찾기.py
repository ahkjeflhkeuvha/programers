import sys

N = int(sys.stdin.readline().strip())
nums = set(sys.stdin.readline().split())

M = int(sys.stdin.readline().strip())
chk = sys.stdin.readline().split()

for x in chk:
    if x in nums:
        print(1)
    else:
        print(0)
    