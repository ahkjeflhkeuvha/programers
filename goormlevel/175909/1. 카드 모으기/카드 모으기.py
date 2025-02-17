# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = map(int, input().split())
cards = set()

cnt = -1

for i in range(M):
	card = int(input())
	
	cards.add(card)
	
	if len(cards) == N:
		cnt = i + 1
		break

print(cnt)