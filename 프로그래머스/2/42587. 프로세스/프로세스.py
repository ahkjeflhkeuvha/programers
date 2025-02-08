from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])
    
    
    co = priorities
    n = 0
    while queue:
        idx, process = queue.popleft()

        if max(co) > process:
            queue.append([idx, process])
        else:
            print(idx, process)
            co[idx] = -1
            n += 1
            
            if idx == location:
                break
        
        
    
    
    return n