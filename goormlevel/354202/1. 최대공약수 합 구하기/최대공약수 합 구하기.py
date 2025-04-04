import math

N = int(input())
nums = list(map(int, input().split()))

def combination(arr, n):
	result = []
	
	if n == 0:
		return [[]]

	for (i, num) in enumerate(arr):
		for j in combination(arr[i+1:], n - 1):
			result.append([num] + j)
	
	return result

tot_res = combination(nums, 2)
tot = 0

for res in tot_res:
	tot += math.gcd(res[0], res[1])

print(tot)