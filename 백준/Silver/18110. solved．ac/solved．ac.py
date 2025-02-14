import math
import sys

def round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

n = int(input())
if n == 0:
    print(0)
else:
    level = []

    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        level.append(num)

    trimmed = round(n * 0.15)
    level.sort()

    if trimmed > 0:
        print(round(sum(level[trimmed:-trimmed])/len(level[trimmed:-trimmed])))
    else:
        print(round(sum(level)/len(level)))
    
