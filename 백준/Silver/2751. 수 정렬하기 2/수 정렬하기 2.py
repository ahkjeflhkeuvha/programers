import sys
n = int(input())
l = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    l.append(num)

l.sort()

for num in l:
    print(num)