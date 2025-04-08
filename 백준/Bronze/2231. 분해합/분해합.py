N = int(input())

sums = []
num = 1

def sum_digit(number):
    return sum([int(i) for i in str(number)])

while num < N:
    tot = num + sum_digit(num)
    if tot == N:
        break
    num += 1

print(0 if num == N else num)