import sys

N, M = map(int, sys.stdin.readline().strip().split())

nums = [0] + list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, N+1):
    nums[i] = nums[i] + nums[i-1]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().strip().split())

    print(nums[e] - nums[s-1])