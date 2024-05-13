def solution(arr, k):
    answer = [-1 for i in range(k)]
    n = 0
    
    for i in arr:
        if not i in answer:
            answer[n] = i
            n += 1
            
        if not -1 in answer:
            break
    return answer