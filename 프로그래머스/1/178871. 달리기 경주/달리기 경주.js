function solution(players, callings) {
    let map = new Map()
    
    for(var player of players) map.set(player, players.indexOf(player))
    
    for(var i = 0; i<callings.length; i++){
        var idx = map.get(callings[i])
        
        var temp = players[idx]
        players[idx] = players[idx - 1]
        players[idx - 1] = temp
        
        map.set(players[idx - 1], idx - 1)
        map.set(players[idx], idx)
    }
    return players;
}