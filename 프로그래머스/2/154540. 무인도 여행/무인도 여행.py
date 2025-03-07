from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(i, j, n, m, maps, visited):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    survival = int(maps[i][j])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                survival += int(maps[nx][ny])
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    return survival
                
    

def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for (i, row) in enumerate(maps):
        for (j, d) in enumerate(row):
            if d == 'X':
                visited[i][j] = True
                
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not visited[i][j]:
                answer.append(bfs(i, j, len(maps), len(maps[0]), maps, visited))
    
    return sorted(answer) if len(answer) > 0 else [-1]