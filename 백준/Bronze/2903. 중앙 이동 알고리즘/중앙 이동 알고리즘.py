# 1 -> 4 -> 16 -> 64 -> 256 -> 1024
# 4 -> 9 -> 25 -> 81 -> 287 -> 1089

# 3 -> 5 -> 9 -> 17 -> 33 -> 65
#   2 -> 4 -> 8 -> 16 -> 32

i = int(input())

squareNum = pow(4, i)

diff = 3

for i in range(1, i+1):
    diff += pow(2, i)

print(squareNum + diff)