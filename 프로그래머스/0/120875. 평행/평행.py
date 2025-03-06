import math

def get_inc(x, y, x1, y1):
    return abs((y - y1) / (x - x1))

def solution(dots):
    answer = 0
    for i in range(1, 4):
        idx_list = [n for n in range(1, 4) if n != i]
        inc1 = get_inc(dots[0][0], dots[0][1], dots[i][0], dots[i][1])
        inc2 = get_inc(dots[idx_list[0]][0], dots[idx_list[0]][1], dots[idx_list[-1]][0], dots[idx_list[-1]][1])
        
        if inc1 == inc2:
            return 1
    return answer