import sys

N = int(sys.stdin.readline().strip())
answers = list(map(int, sys.stdin.readline().strip().split()))

scores = [0]
num = 0

for answer in answers:
	if answer == 1:
		num += 1
		scores.append(num)
	else:
		num = 0
		
print(max(scores))