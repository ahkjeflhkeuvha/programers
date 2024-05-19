def solution(my_string, is_prefix):
    answer = 0
    
    for i in range(0, len(my_string) + 1):
        if(is_prefix == my_string[0:i]):
            answer += 1
    return answer