def chk_level(diffs, times, limit, level):
    tot_times = 0
    n = len(diffs)
    
    for i in range(n):
        cur_diff = diffs[i]
        cur_time = times[i]
        prev_time = times[i - 1]
        
        if cur_diff <= level:
            tot_times += cur_time
        else:
            tot_times += (prev_time * (cur_diff - level)) + (cur_time * (cur_diff - level)) + cur_time
            
        if tot_times > limit:
            return False
    
    return True


def solution(diffs, times, limit):
    answer = 0
    
    max_num = max(diffs)
    min_num = 1
    
    while min_num <= max_num:
        mid_num = (min_num + max_num) // 2
        
        res = chk_level(diffs, times, limit, mid_num)
        
        if res:
            max_num = mid_num - 1
        else:
            min_num = mid_num + 1
    
    return min_num