import sys

while True:
    sub = list(map(int, sys.stdin.readline().strip().split()))
    if sub == [0, 0, 0]:
        break

    sub.sort(reverse=True)
    
    if sub[0]**2 == sub[1]**2 + sub[2]**2:
        print("right")
    else:
        print("wrong")