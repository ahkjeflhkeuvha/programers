from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])
    
    n = 0
    while queue:
        idx, process = queue.popleft()

        if any(process < data for data in priorities):
            queue.append([idx, process])
        else:
            print(idx, process)
            priorities[idx] = -1
            answer += 1
            
            if idx == location:
                break
    
    return answer