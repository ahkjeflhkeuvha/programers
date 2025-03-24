from functools import reduce

def mul(x, y):
    return x*y

tot = reduce(mul, [int(input()) for i in range(3)])

num_cnt = [0] * 10

for s in str(tot):
    num_cnt[int(s)] += 1

print(*num_cnt, sep="\n")