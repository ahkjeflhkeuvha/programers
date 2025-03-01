import sys

N = int(input())

def change_base(num, base):
    res = ""
    while num:
        diff = num%base if num%base < 10 else chr(ord('A') + num%base - 10)
        res = str(diff) + res
        num //= base
    
    return res

for _ in range(N):
    num, base = map(int, sys.stdin.readline().strip().split())
    
    t = change_base(num, base)
    rt = ''.join(reversed(list(t)))

    print(1 if t == rt else 0)