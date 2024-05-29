def solution(s):
    answer = ''
    strArr = s.split(" ")
    
    for strItem in strArr:
        for idx in range(0, len(strItem)):
            if(idx%2 == 0):
                answer += strItem[idx].upper()
            else:
                answer += strItem[idx].lower()
        answer += ' '
        
    return answer[0:len(s)]