dwarf = sorted([int(input()) for _ in range(9)])

diff = sum(dwarf) - 100

answer = []

for i in range(9):
    for j in range(i, 9):
        if i != j and dwarf[i] + dwarf[j] == diff:
            answer = dwarf[:i] + dwarf[i+1:j] + dwarf[j+1:]
            break

print(*answer, sep="\n")