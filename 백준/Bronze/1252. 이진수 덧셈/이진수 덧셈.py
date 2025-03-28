A, B = map(int, input().split())

def binToInt(num):
    tot = 0
    p = 0

    for s in reversed(str(num)):
        if s == "1":
            tot += pow(2, p)
        p += 1

    return tot

print(bin(binToInt(A) + binToInt(B))[2:])