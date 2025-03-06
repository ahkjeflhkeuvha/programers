def solution(board):
    answer = 0
    dx, dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    danger_area = set()
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger_area.add((i, j))
                for k in range(9):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        danger_area.add((nx, ny))
                        
    return pow(len(board), 2) - len(danger_area)