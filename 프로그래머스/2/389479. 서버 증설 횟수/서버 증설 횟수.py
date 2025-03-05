from collections import deque
import math

def solution(players, m, k):
    answer = 0
    servers = deque()
    
    for time in range(24):
        while servers and servers[0] == time:
            servers.popleft()
            
            
        need_servers = math.floor(players[time] / m)
        cur_servers = len(servers)
        
        if need_servers > cur_servers:
            needed = need_servers - cur_servers
            answer += needed
            for _ in range(needed):
                servers.append(time + k)
        
    return answer