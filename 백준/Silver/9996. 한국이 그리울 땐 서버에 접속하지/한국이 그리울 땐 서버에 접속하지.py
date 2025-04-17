import re

N = int(input())
case_str = list(map(re.escape, re.split(r"\*", input())))

for _ in range(N):
    s = input()
    if re.match(r"^" + case_str[0] + "[a-z]*" + case_str[1] + "$", s):
        print("DA")
    else:
        print("NE")
