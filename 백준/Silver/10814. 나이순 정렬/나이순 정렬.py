n = int(input())
infos = []

for i in range(n):
    age, name = input().split()
    infos.append((int(age), name, i))

infos = sorted(infos, key=lambda x : (x[0], x[2]))

for age, name, i in infos:
    print(age, name)