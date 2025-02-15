from collections import deque
import sys

n = int(input())
queue = deque()

for _ in range(n):
    sen = sys.stdin.readline().strip().split()

    if sen[0] == "push":
        queue.append(sen[1])
    elif sen[0] == "pop":
        print(-1 if len(queue) == 0 else queue.popleft())
    elif sen[0] == "size":
        print(len(queue))
    elif sen[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif sen[0] == "front":
        print(-1 if len(queue) == 0 else queue[0])
    else:
        print(-1 if len(queue) == 0 else queue[-1])