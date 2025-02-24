A, B, C, D = map(int, input().split())

print('G' if A*B > C*D else 'B' if A*B != C*D else 'D')