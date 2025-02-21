from collections import deque

N, M = map(int, input().split())
queue = deque([])

graph = [list(map(int, input().split())) for _ in range(N)]
dis = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            queue.append((i, j))
            dis[i][j] = 0
        if graph[i][j] == 0:
            dis[i][j] = 0

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                if dis[nx][ny] == -1:
                    dis[nx][ny] = dis[x][y] + 1
                    queue.append((nx, ny))

bfs()
for i in range(N):
    for j in range(M):
        print(dis[i][j], end = " ")
    print()