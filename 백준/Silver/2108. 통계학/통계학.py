import sys
n = int(input())

nums = []
num_dic = {}

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    nums.append(num)

nums.sort()

print(round(sum(nums)/n))
print(nums[len(nums)//2])

for n in nums:
    if n not in num_dic:
        num_dic[n] = 1
    else:
        num_dic[n] += 1

num_dic = sorted(num_dic.items(), key=lambda x : (-x[1], x[0]))

print(num_dic[1][0] if len(num_dic) > 1 and num_dic[0][1] == num_dic[1][1] else num_dic[0][0])
print(max(nums) - min(nums))