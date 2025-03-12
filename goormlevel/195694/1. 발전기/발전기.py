N = int(input())
			
def bfs(i, j):
	visited[i][j] = True
	queue = [(i, j)]
	
	while queue:
		x, y = queue.pop(0)
		
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			
			if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
				visited[nx][ny] = True
				queue.append((nx, ny))
							 
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]	

for i in range(N):
	for j in range(N):
		if graph[i][j] == 0:
			visited[i][j] = True
			
answer = 0
			
for i in range(N):
	for j in range(N):
		if not visited[i][j]:
			bfs(i, j)
			answer += 1
							 
print(answer)