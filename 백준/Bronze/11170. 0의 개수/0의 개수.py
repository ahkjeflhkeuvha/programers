N = int(input())

for _ in range(N):
    S, E = map(int, input().split())
    cnt = 0

    for i in range(S, E + 1):
        cnt += str(i).count('0')

    print(cnt)