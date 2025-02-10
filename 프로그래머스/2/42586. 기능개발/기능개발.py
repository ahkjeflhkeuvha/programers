from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for i in range(len(progresses)):
        diff = 100 - progresses[i]
        days = (diff // speeds[i]) + (0 if diff%speeds[i] == 0 else 1)
        queue.append(days)

    while queue:
        n = queue.popleft()
        c = 1
        while queue:
            if queue[0] <= n:
                queue.popleft()
                c += 1
            else:
                break
        answer.append(c)
    
    
    return answer