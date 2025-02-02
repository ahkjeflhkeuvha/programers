def solution(arr, k):
    answer = []
    flag = True if k%2 == 0 else False
    
    for d in arr:
        if flag:
            answer.append(d+k)
        else:
            answer.append(d*k)
    return answer