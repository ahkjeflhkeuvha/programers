import heapq, sys
inf = sys.maxsize
answer = 0

def dfs(graph, start, distance):
    global answer
    distance[start] = 0
    pq = [[0,start]]

    while pq:
        dist, cur = heapq.heappop(pq)

        if dist > distance[cur]:
            continue

        for dis,j in graph[cur]:
            a = dist + dis
            if a < distance[j]:
                heapq.heappush(pq, [a,j])
                distance[j] = a

    distance.sort(reverse=True)
    answer = distance.count(distance[0])

def solution(n, edge):
    global answer

    distance = [inf] * n
    graph = [[] for _ in range(n)]

    for start, end in edge:
        graph[start-1].append([1,end-1])
        graph[end-1].append([1,start-1])

    dfs(graph, 0, distance)

    return answer