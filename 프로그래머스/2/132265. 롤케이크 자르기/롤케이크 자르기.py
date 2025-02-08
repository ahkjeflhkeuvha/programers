def solution(topping):
    o_d = {}
    y_d = {}
    
    answer = 0
    for t in topping:
        if t in o_d:
            o_d[t] += 1
        else:
            o_d[t] = 1
    
    for t in topping:
        if len(o_d) == len(y_d):
            answer += 1
        
        if t not in y_d:
            y_d[t] = 1
        
        o_d[t] -= 1
        
        if o_d[t] == 0:
            del o_d[t]
    return answer