def solution(arr1, arr2):
    n, m = len(arr1), len(arr2[0])
    answer = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            tot = 0
            for k in range(len(arr1[i])):
                tot += arr1[i][k] * arr2[k][j] 
            answer[i][j] = tot
    return answer