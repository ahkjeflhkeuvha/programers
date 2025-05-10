# depth가 2 이하인 친구를 찾자!

from collections import deque

n = int(input())
m = int(input())

graph = {i : [] for i in range(1, n+1)}

for i in range(m):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n+1)

def bfs(start, graph):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        node, depth = queue.popleft()

        if depth >= 2:
            continue

        for next in graph[node]:
            if not visited[next]:
                queue.append((next, depth + 1))
                visited[next] = True
    return visited

print(bfs(1, graph).count(True) - 1)