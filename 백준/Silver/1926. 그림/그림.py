from collections import deque

N, M = map(int, input().split())

picture = [list(map(int, input().split())) for _ in range(N)]
visited = [[False if picture[i][j] == 1 else True for j in range(M)] for i in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt

dump = [0]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dump.append(bfs(i, j))

print(len(dump) - 1)
print(max(dump))       