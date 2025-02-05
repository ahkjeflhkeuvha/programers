import sys

wordlist = []

for i in range(5):
    sub = sys.stdin.readline().strip()
    wordlist.append(list(sub))

answer = ""

for i in range(15):
    for j in range(5):
        try:
            answer += wordlist[j][i]
        except:
            pass

print(answer)
