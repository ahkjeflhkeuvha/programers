def solution(sequence, k):
    answer = []
    
    n = len(sequence)
    left, right = 0, 0
    cur_sum = sequence[0]
    
    while right < n:
        if cur_sum == k:
            answer.append([left, right])
        if cur_sum >= k:
            cur_sum -= sequence[left]
            left += 1
        else:
            right += 1
            if right < len(sequence):
                cur_sum += sequence[right]
            
    
    
    return sorted(answer, key=lambda x: x[1] - x[0])[0]