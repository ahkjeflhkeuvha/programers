tot = 0

nums = list(map(int, input().split()))

for num in nums:
    tot += pow(num, 2)

print(tot%10)