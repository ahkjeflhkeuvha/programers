def solution(board):
    answer = 0
    danger_area = set()
    n = len(board)
    
    for (i, row) in enumerate(board):
        for (j, x) in enumerate(row):
            if not x == 1:
                continue
            danger_area.update((i+nx, j+ny) for nx in [-1, 0, 1] for ny in [-1, 0, 1] if 0 <= i + nx < n and 0 <= j + ny < n)

    return n*n - len(danger_area)