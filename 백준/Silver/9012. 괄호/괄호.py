def chk(sen):
    stack = []

    for s in sen:
        if s == '(':
            stack.append(s)
        if s == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False

N = int(input())

for _ in range(N):
    print('YES' if chk(input()) else 'NO')
        