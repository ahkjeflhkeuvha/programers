def solution(s):
    answer = s.split(" ")
    answer = [str.capitalize() for str in answer]
    return ' '.join(answer)