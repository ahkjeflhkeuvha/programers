N = int(input())

visited = [[False for _ in range(N)] for _ in range(N)]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
graph = []
town = []

for _ in range(N):
    graph.append(list(map(int, input())))


for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            visited[i][j] = True


def BFS(N, start_x, start_y):
    queue = [(start_x, start_y)]
    visited[start_x][start_y] = True
    cnt = 1

    while queue:
        start_x, start_y = queue.pop(0)

        for x, y in move:
            new_x = start_x + x
            new_y = start_y + y

            if 0 <= new_x < N and 0 <= new_y < N and graph[new_x][new_y] == 1 and not visited[new_x][new_y]:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True
                cnt += 1
    
    town.append(cnt) 


for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            BFS(N, i, j)
    
town.sort()

print(len(town))
for t in town:
    print(t)


