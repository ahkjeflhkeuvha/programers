def solution(arr):
    answer = arr
    i = 0
    
    while len(answer) > pow(2, i):
        i += 1
        
    while len(answer) != pow(2, i):
        answer.append(0)
    
    return answer