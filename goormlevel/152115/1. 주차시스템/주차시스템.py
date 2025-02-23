from collections import deque
import sys

N, M = map(int, sys.stdin.readline().strip().split())
park = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    score = 1 if park[x][y] == 0 else -2

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
              visited[nx][ny] = True
              queue.append((nx, ny))
              if park[nx][ny] == 0:
                  score += 1
              elif park[nx][ny] == 2:
                  score -= 2

    return score

score = float("-inf")

for i in range(N):
    for j in range(M):
        if park[i][j] == 1:
            visited[i][j] = True

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            score = max(score, bfs(i, j))


print(max(0, score))
