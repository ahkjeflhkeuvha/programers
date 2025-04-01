def solution(gems):
    gem_set = set(gems)
    gem_count = {}
    left, right = 0, 0
    min_len = float('inf')
    answer = [0, len(gems)]
    
    while right < len(gems):
        gem_count[gems[right]] = gem_count.get(gems[right], 0) + 1
        right += 1
        
        while len(gem_count) == len(gem_set):
            if right - left < min_len:
                min_len = right - left
                answer = [left + 1, right]
            
            gem_count[gems[left]] -= 1
            if gem_count[gems[left]] == 0:
                del gem_count[gems[left]]
            left += 1
    
    return answer
