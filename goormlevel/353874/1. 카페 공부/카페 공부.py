n, m = map(int, sorted(input().split()))

an, am = map(int, sorted(input().split()))
bn, bm = map(int, sorted(input().split()))

def can_place(n, m, an, am, bn, bm):
    if (an + bn <= n and max(am, bm) <= m) or (max(an, bn) <= n and am + bm <= m):
        return True
    if (am + bm <= m and max(an, bn) <= n) or (an + bm <= n and max(am, bn) <= m):
        return True
    return False

if can_place(n, m, an, am, bn, bm) or can_place(n, m, am, an, bn, bm) or can_place(n, m, an, am, bm, bn) or can_place(n, m, am, an, bm, bn):
    print("YES")
else:
    print("NO")
