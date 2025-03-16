from collections import deque

N, M = map(int, input().split())

sand_castle = [list(map(int, input().split())) for _ in range(N)]
visited = [[True if column == 0 else False for column in row] for row in sand_castle]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

answer = 0
flag = True

def increase_water(sand_castle):
    new_sand_castle = [row[:] for row in sand_castle]
    all_true = True

    for i in range(N):
        for j in range(M):
            if sand_castle[i][j] == 0:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and sand_castle[nx][ny] == 1:
                        new_sand_castle[nx][ny] = 0

    for i in range(N):
        for j in range(M):
            if new_sand_castle[i][j] == 1:
                all_true = False
                break
    if all_true:
        return -1

    return new_sand_castle

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

cnt = 0

while flag:
    visited = [[True if column == 0 else False for column in row] for row in sand_castle]
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                answer += 1
                bfs(i, j)
    sand_castle = increase_water(sand_castle)
		
    if answer >= 2:
      print(cnt)
      break
			
    if sand_castle == -1:
        print(-1)
        break
				
    cnt += 1
    answer = 0
