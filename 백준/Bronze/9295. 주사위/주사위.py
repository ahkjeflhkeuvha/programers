n = int(input())

for i in range(1, n+1):
    f, s = map(int, input().split())

    print("Case {}: {}".format(i, f+s))