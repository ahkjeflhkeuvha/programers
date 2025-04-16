N = int(input())

board = [[0 for _ in range(500)] for _ in range(500)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    
    for j in range(y1, y2):
        for i in range(x1, x2):
            board[i][j] = 1

cnt = 0
for row in board:
    for col in row:
        if col > 0:
            cnt += 1

print(cnt)