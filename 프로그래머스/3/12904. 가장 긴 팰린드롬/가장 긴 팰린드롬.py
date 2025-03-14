def expand_from_center(left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
        
    return right - left - 1

def solution(s):
    n = len(s)
    if n == 0:
        return 0
    
    max_len = 1
    for i in range(n):
        len1 = expand_from_center(i, i, s)
        len2 = expand_from_center(i, i + 1, s)
        max_len = max(max_len, len1, len2)
    
    return max_len
