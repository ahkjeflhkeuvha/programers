import math

N, M = map(int, input().split())
answer = []

for num in range(N, M+1):
	if math.sqrt(num) % 1 == 0:
		answer.append(num)
		
print(-1 if len(answer) == 0 else len(answer))
print(sum(answer))