N = int(input())

cycle = 0
temp = N

while True:
    S = str(sum(list(map(int, list(str(temp))))) % 10)
    temp = int(str(temp)[-1] + S)
    cycle += 1

    if temp == N:
        break

print(cycle)