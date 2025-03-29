N = int(input())
lines = list(map(int, input().split()))
stack = []
get = []
person = 1


while person <= N:
    if lines and lines[0] == person: # 순서대로 선 경우
        lines.pop(0)
        get.append(person)
        person += 1   
    elif stack and stack[-1] == person: # 공간에 들어간 경우
        stack.pop()
        get.append(person)
        person += 1
    elif lines: # 공간에 들어가야하는 경우
        stack.append(lines.pop(0))

    if lines == [] and stack != [] and stack[-1] != person:
        break

if stack:
    print("Sad")
else:
    print("Nice")

