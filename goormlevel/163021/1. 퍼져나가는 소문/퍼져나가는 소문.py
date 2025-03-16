N = int(input()) # 친구의 수 N
M = int(input()) # 친구 관계의 수 M

friends = {i : [] for i in range(1, N+1)}

for _ in range(M):
	x, y = map(int, input().split())
	friends[x].append(y)
	friends[y].append(x)
	
# print(friends)

gossip = set()
	
def dfs(start, friends):
	while friends[start]:
		next_friend = friends[start].pop(0)
		if next_friend not in gossip:
			gossip.add(next_friend)
			dfs(next_friend, friends)
		
dfs(1, friends)

print(len(gossip) if len(gossip) > 0 else 1)