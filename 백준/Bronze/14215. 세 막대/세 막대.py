line = list(map(int, input().split()))
line.sort(reverse=True)

# print(line)

if line[0] >= line[1] + line[2]:
    print((line[1]+line[2])*2 - 1)
else:
    print(line[0] + line[1] + line[2])