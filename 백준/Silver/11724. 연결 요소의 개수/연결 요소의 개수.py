import sys

N, M = map(int, input().split())

graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())

    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

visited = [False]*N
cnt = 0

def bfs(graph, start):
    global visited 
    global cnt

    stack = [start]
    visited[start] = True
    cnt += 1

    while stack:
        node = stack.pop(0)
        for j in range(N):
            if graph[node][j] == 1 and not visited[j]:
                visited[j] = True
                stack.append(j)


bfs(graph, 0)

for i in range(N):
    if visited[i] == False:
        bfs(graph, i)

print(cnt)