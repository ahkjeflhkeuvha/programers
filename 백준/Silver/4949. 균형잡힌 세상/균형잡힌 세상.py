import sys

def chk_sen(sub):
    queue = []

    for s in sub:
        if s == '(' or s == '[':
            queue.append(s)
        elif s == ')':
            if len(queue) != 0 and queue[-1] == '(':
                queue.pop()
            else:
                return False
        elif s == ']':
            if len(queue) != 0 and queue[-1] == '[':
                queue.pop()
            else:
                return False
    return True if len(queue) == 0 else False

while True:
    sub  = sys.stdin.readline().rstrip()
    if sub == ".":
        break

    if chk_sen(sub):
        print("yes")
    else:
        print("no")