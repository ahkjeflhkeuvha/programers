def solution(myString, pat):
    answer = 0
    pat = pat.replace('A', 'C')
    pat = pat.replace('B', 'A')
    pat = pat.replace('C', 'B')
    
    if pat in myString:
        answer = 1
    return answer