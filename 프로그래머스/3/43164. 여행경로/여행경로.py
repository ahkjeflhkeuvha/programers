from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    for start, end in sorted(tickets):
        graph[start].append(end)

    route = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        route.append(airport)

    dfs("ICN")
    return route[::-1]
