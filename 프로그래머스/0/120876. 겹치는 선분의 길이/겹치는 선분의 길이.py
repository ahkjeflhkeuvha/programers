import math

def combination(lines, n):
    result = []
    
    if n == 0:
        return [[]]
    
    for (i, num) in enumerate(lines):
        for j in combination(lines[i+1:], n-1):
            result.append([num] + j)
            
    return result

def solution(lines):
    length = set()
    res = combination(lines, 2)
    
    for seg1, seg2 in res:
        start1, end1 = sorted(seg1)
        start2, end2 = sorted(seg2)

        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)

        if overlap_start < overlap_end:
            for i in range(math.ceil(overlap_start), math.floor(overlap_end)):
                length.add(i)

    return len(length)