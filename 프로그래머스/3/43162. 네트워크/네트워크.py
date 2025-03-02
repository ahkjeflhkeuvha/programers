def dfs(i, n, computers, visited):
    stack = [i]
    visited[i] = True
    
    while stack:
        node = stack.pop()
        
        for j in range(n):
            if computers[node][j] == 1 and not visited[j]:
                visited[j] = True
                stack.append(j)

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, n, computers, visited)
    
    return answer