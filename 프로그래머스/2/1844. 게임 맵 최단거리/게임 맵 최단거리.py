from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(i, j, maps, visited):
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1 
                visited[nx][ny] = True

    return maps

def solution(maps):
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 0:
                visited[i][j] = True
                
    maps = bfs(0, 0, maps, visited)
    answer = maps[len(maps)-1][len(maps[0])-1]
    
    return answer if answer > 1 else -1 
