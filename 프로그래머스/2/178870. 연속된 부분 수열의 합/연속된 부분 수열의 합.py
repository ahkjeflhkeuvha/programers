def solution(sequence, k):
    answer = []
    
    n = len(sequence)
    left, right = 0, 0
    cur_sum = sequence[0]
    min_len = float('inf')
    
    while right < n:
        if cur_sum == k:
            if right - left < min_len:
                min_len = right - left
                answer = [left, right]
        if cur_sum >= k:
            cur_sum -= sequence[left]
            left += 1
        else:
            right += 1
            if right < len(sequence):
                cur_sum += sequence[right]
            
    return answer