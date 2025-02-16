N, K = map(int, input().split())

wallet = []
for _ in range(N):
    money = int(input())
    wallet.append(money)

wallet.sort(reverse=True)

tot = 0
cnt = 0

while K != 0:
    temp = wallet.pop(0)

    if temp <= K:
        tot += temp * (K//temp)
        cnt += (K//temp)
        K = K%temp

print(cnt)