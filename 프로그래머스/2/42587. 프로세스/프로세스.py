from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])
    
    n = 0
    while queue:
        idx, process = queue.popleft()

        if any(process < data[1] for data in queue):
            queue.append([idx, process])
        else:
            answer += 1
            
            if idx == location:
                break
    
    return answer