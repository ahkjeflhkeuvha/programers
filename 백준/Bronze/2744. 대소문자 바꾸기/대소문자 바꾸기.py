sen = input()
answer = ""

for s in sen:
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()

print(answer)