def solution(a, b):
    answer = 0
    aCon = str(a) + str(b)
    bCon = str(b) + str(a)
    if int(aCon)>int(bCon):
        answer = int(aCon)
    else:
        answer = int(bCon)
    return answer 