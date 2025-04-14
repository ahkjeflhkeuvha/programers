def hanoi_tower(n, a, b, c, answer):
    if n == 1:
        answer.append([a, c])
    else:
        hanoi_tower(n-1, a, c, b, answer)
        answer.append([a, c])
        hanoi_tower(n-1, b, a, c, answer)
        
    return answer

def solution(n):
    answer = []
    return hanoi_tower(n, 1, 2, 3, answer)