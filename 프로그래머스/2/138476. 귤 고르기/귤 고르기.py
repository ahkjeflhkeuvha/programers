def solution(k, tangerine):
    answer = 0
    tangerine_count = {}
    
    for i in tangerine:
        if i not in tangerine_count.keys():
            tangerine_count[i] = 1
        else:
            n = tangerine_count[i]
            tangerine_count[i] = n + 1
    tangerine_count = dict(sorted(tangerine_count.items(), key=lambda item: -item[1]))
    
    tot = 0
    for i in tangerine_count.keys():
        if tot < k:
            tot += tangerine_count[i]
            answer += 1
        else:
            return answer
        
    return answer