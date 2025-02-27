import sys

N = int(sys.stdin.readline().strip())
answers = list(map(int, sys.stdin.readline().strip().split()))

tot = 0
score = 0

for answer in answers:
	if answer == 1:
		score += 1
		tot += score
	else:
		score = 0
		
print(tot)