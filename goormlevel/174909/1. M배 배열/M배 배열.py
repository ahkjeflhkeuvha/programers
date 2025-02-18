# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = map(int, input().split())
A = map(int, input().split())
mA = []

for el in A:
	if el%M == 0:
		print(el, end=" ")
	else:
		print(el*M, end=" ")
	