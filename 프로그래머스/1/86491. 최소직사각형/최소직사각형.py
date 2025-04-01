def solution(sizes):
    answer = 0
    max_width, max_height = 0, 0
    
    for (width, height) in sizes:
        max_width = max(max(width, height), max_width)
        max_height = max(min(width, height), max_height)
        
    return max_width * max_height