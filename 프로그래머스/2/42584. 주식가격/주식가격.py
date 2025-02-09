from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    
    for i in range(len(prices)):
        cur = queue.popleft() 
        time = 0
        
        for fu in queue:
            if fu >= cur:
                time += 1
            else:
                time += 1
                break
        answer.append(time)        
        
    return answer