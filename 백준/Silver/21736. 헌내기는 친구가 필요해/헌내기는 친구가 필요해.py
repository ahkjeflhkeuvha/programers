from collections import deque
N, M = map(int, input().split())

maze = []
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    maze.append(list(input()))

x, y = 0, 0


for i in range(N):
    for j in range(M):
        if maze[i][j] == 'I':
            x, y = i, j

visited[x][y] = True

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    people = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if maze[nx][ny] == 'X':
                continue

            if maze[nx][ny] == 'P' and not visited[nx][ny]:
                people += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
                continue
            
            if maze[nx][ny] == 'O' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return people


# print(x, y)
res = bfs(x, y)
print(res if res > 0 else 'TT')