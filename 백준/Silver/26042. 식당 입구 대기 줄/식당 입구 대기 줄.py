import sys
from collections import deque

N = int(sys.stdin.readline())
students = deque()
max_len = 0
max_case = []

food = 0

for _ in range(N):
    option = list(map(int, sys.stdin.readline().split()))
    food += 1

    if option[0] == 1:
        students.append(option[1])

        if len(students) > max_len:
            max_len = len(students)
            max_case = [(max_len, option[1])]
        elif len(students) == max_len:
            max_case.append((max_len, option[1]))

    else:
        if students:
            students.popleft()
            food -= 1 

print(*sorted(max_case, key=lambda x: x[1])[0])
