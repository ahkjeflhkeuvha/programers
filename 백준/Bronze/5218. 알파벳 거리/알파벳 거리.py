N = int(input())

for _ in range(N):
    sen1, sen2 = input().split()
    dis = []
    
    for i in range(len(sen1)):
        if ord(sen1[i]) <= ord(sen2[i]):
            dis.append(ord(sen2[i]) - ord(sen1[i]))
        else:
            dis.append(ord(sen2[i]) + 26 - ord(sen1[i]))

    print("Distances:", *dis)