def chk_day(want_dic, discount):
    dis_dic = {}
    for dis in discount:
        if dis in dis_dic:
            dis_dic[dis] += 1
        else:
            dis_dic[dis] = 1
    
    if any(key not in dis_dic or want_dic[key] != dis_dic[key] for key in want_dic.keys()):
        return False
    return True
    
def solution(want, number, discount):
    answer = 0
    want_dic = dict(zip(want, number))
    for i in range(0, len(discount)-10+1):
        if chk_day(want_dic, discount[i:i+10]):
            answer += 1
    return answer