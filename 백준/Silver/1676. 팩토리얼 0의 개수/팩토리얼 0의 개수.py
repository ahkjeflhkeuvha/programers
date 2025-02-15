def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = int(input())
fac_num = ''.join(reversed(list(str(factorial(n)))))

i = 0

while str(fac_num)[i] == '0':
    i += 1

print(i)