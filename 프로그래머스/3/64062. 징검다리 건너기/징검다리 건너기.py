def chk_jump(jump, stones, k):
    skip = 0
    for stone in stones:
        if stone < jump: 
            skip += 1
            if skip >= k:
                return False
        else:
            skip = 0
    return True

def solution(stones, k):
    left, right = 1, max(stones)

    while left <= right:
        mid = (left + right) // 2
        if chk_jump(mid, stones, k):
            left = mid + 1 
        else:
            right = mid - 1
            
    return right
