N = int(input())

fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

while len(fibo) <= N:
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[N])