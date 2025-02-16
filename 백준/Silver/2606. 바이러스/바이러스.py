N = int(input()) 
R = int(input()) 

computer = [[0] * N for _ in range(N)]

for _ in range(R):
    x, y = map(int, input().split())
    computer[x-1][y-1] = 1
    computer[y-1][x-1] = 1

visited = [False] * N

def dfs(start):
    stack = [start]
    visited[start] = True
    cnt = 0

    while stack:
        node = stack.pop()
        for i in range(N):
            if computer[node][i] == 1 and not visited[i]:
                visited[i] = True
                stack.append(i)
                cnt += 1  

    return cnt

infected_count = dfs(0)
print(infected_count)
