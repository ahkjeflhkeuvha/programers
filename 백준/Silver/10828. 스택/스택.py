import sys

n = int(input())
stack = []

for i in range(n):
    sen = sys.stdin.readline().strip().split()
    
    if sen[0] == "push":
        stack.append(sen[1])
    elif sen[0] == "top":
        print(-1 if len(stack) == 0 else stack[-1])
    elif sen[0] == "size":
        print(len(stack))
    elif sen[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    else:
        print(-1 if len(stack) == 0 else stack.pop())