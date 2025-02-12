num = []

for i in range(5):
    num.append(int(input()))

num.sort()
print("{:d}".format(sum(num)//5))
print("{:d}".format(num[2]))