n = int(input())

l = []
for i in range(2, n+1):
    while n%i == 0:
        l.append(i)
        n //= i

for num in l:
    print(num)