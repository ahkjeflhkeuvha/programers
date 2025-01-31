def solution(board, h, w):
    answer = 0
    chk_w = [-1, 0, 1, 0]
    chk_h = [0, -1, 0, 1]
    n = len(board)
    
    for i in range(4):
        n_w = w + chk_w[i]
        n_h = h + chk_h[i]
        
        if 0 <= n_w < n and 0 <= n_h < n and board[h][w] == board[n_h][n_w]:
            answer += 1
    
    return answer