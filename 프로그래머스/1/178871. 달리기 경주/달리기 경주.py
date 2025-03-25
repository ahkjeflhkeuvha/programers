def solution(players, callings):
    answer = []
    player_dict = {players[i] : i for i in range(len(players))}
    
    for calling in callings:
        calling_idx = player_dict[calling]
        
        temp = players[calling_idx]
        players[calling_idx] = players[calling_idx - 1]
        players[calling_idx - 1] = temp
        
        player_dict[players[calling_idx]] = calling_idx
        player_dict[players[calling_idx - 1]] = calling_idx - 1
    
    return players