Pn = int(input())
P = 'IO'*Pn + 'I'
N = int(input())
S = input()

cnt = 0


for i in range(0, N - (Pn*2 + 1) + 1):
    if S[i:i+(Pn*2 + 1)] == P:
        cnt += 1

print(cnt)