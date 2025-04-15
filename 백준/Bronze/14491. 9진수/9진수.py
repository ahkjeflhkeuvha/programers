N = int(input())
answer = ""

while N != 0:
    answer += str(N % 9)
    N //= 9

print(''.join(reversed(list(answer))))