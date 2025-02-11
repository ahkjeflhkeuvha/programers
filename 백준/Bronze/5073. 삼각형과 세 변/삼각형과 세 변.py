# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우

import sys

while True:
    sub = list(map(int, sys.stdin.readline().strip().split()))
    if sub[0] == 0 and sub[2] == 0:
        break

    sub.sort(reverse=True)
    
    if sub[0] >= sub[1] + sub[2]:
        print("Invalid")
    else:
        if sub[0] == sub[2]:
            print("Equilateral")
        elif sub[0] == sub[1] or sub[1] == sub[2]:
            print("Isosceles")
        else:
            print("Scalene")

    