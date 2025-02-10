def solution(clothes):
    cloth_dic = {i[1]:1 for i in clothes}
    
    for cloth in clothes:
        cloth_name, cloth_type = cloth
        
        cloth_dic[cloth_type] += 1
    
    answer = 1
    for i in cloth_dic.values():
        answer *= i
        
    return answer - 1
        