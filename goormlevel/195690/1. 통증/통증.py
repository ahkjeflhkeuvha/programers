health = int(input())

stamina = [14, 7, 1]

i = 0
answer = 0

while True:
	if health >= stamina[i]:
		needs = health // stamina[i]
		answer += needs
		health -= stamina[i] * needs
	else:
		i += 1
		
	if health == 0:
		break
		
print(answer)