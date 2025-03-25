def solution(babbling):
    answer = 0
    exp = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in range(len(exp)):
            babbling[i] = babbling[i].replace(exp[j], ' ')
        if babbling[i].strip() == "":
            answer += 1
    return answer