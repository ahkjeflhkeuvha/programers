import sys

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return M * N / gcd(a, b)

N = int(sys.stdin.readline().strip())
for _ in range(N):
    M, N, x, y = map(int, sys.stdin.readline().strip().split())
    max_year = lcm(M , N)
    answer = x
    while answer <= max_year:
        if (answer - 1) % N + 1 == y:
            break
        answer += M
    if answer > max_year:
        print(-1)
    else:
        print(answer)