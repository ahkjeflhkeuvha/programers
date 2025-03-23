N = int(input())

for _ in range(N):
    M, T = input().split()

    if T == "C":
        alpha = list(map(str, input().split()))
        trans = [ord(alp) - 64 for alp in alpha]
        print(*trans, sep=" ")
    else:
        alpha = list(map(int, input().split()))
        trans = [chr(alp+64) for alp in alpha]
        print(*trans, sep=" ")

