import sys

n = int(input())
sets = set()

for _ in range(n):
    sen = sys.stdin.readline().strip().split()

    if sen[0] == "add":
        sets.add(int(sen[1]))
    elif sen[0] == "remove":
        if int(sen[1]) in sets:
            sets.discard(int(sen[1]))
    elif sen[0] == "check":
        print(1 if int(sen[1]) in sets else 0)
    elif sen[0] == "toggle":
        if int(sen[1]) in sets:
            sets.discard(int(sen[1]))
        else:
            sets.add(int(sen[1]))
    elif sen[0] == "all":
        sets = set([i for i in range(1, 21)])
    else:
        sets = set()

    # print(sets)
    

