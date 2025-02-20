# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())

x, y = map(int, input().split())
x -= 1
y -= 1

graph = []

for _ in range(N):
	graph.append(list(map(int, input().split())))

k = graph[x][y]
visited = [[True for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == k:
            visited[i][j] = False
	
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
size = []

def dfs(n, start_x, start_y):
	stack = [(start_x, start_y)]
	visited[start_x][start_y] = True
	cnt = 1
	
	while stack:
		d_x, d_y = stack.pop()
		
		for x, y in move:
			n_x = d_x + x
			n_y = d_y + y
			
			if 0 <= n_x < N and 0 <= n_y < N and graph[n_x][n_y] == n and not visited[n_x][n_y]:
				stack.append((n_x, n_y))
				visited[n_x][n_y] = True
				cnt += 1
	
	size.append(cnt)

for i in range(N):
	for j in range(N):
		if graph[i][j] == k and not visited[i][j]:
			dfs(k, i, j)
			
print(max(size))