def solution(arr):
    answer = []
    row, col = len(arr), len(arr[0])  # 리스트([]) 대신 튜플로 변경

    if row == col:
        return arr
    elif row < col:
        answer.extend(arr) 
        answer.extend([[0] * col for _ in range(col - row)])
    else:
        for i in range(row):
            arr[i].extend([0] * (row - len(arr[i])))
            answer.append(arr[i])  
    return answer
