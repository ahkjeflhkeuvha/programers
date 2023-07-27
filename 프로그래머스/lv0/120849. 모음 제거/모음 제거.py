def solution(my_string):
    answer = ''
    for i in range(0, len(my_string)):
        if my_string[i] == 'a':
            continue
        elif my_string[i] == 'e':
            continue
        elif my_string[i] == 'u':
            continue
        elif my_string[i] == 'o':
            continue
        elif my_string[i] == 'i':
            continue
        else:
            answer += my_string[i]
    return answer