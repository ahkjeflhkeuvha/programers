def solution(my_string):
    strAlp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = [0]*52
    for i in my_string:
        answer[strAlp.index(i)] += 1
    return answer