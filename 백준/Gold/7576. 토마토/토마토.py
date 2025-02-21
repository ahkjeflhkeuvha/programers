from collections import deque

M, N = map(int, input().split())
queue = deque([])
tomatoes = [list(map(int, input().split())) for _ in range(N)]

res = 0

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append((nx, ny))

bfs()

for i in tomatoes:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    res = max(res, max(i))

print(res - 1)