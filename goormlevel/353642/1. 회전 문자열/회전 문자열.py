import sys

sen = list(reversed(str(sys.stdin.readline().strip())))
answer = ""

for s in sen:
	if s == '6':
		answer += '9'
	elif s == '9':
		answer += '6'
	else:
		answer += s

print(answer)