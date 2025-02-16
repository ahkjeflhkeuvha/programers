N = int(input())

for _ in range(N):
    M = int(input())

    clothes = {}
    for i in range(M):
        name, type = input().split()

        if type not in clothes:
            clothes[type] = 2
        else:
            clothes[type] += 1

    tot = 1

    for type, val in clothes.items():
        tot *= val
    
    print(tot - 1)