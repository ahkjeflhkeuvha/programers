import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> player = new HashMap<>();
        
        for(int i = 0; i<players.length; i++) player.put(players[i], i);
        
        for(String call : callings){
            int idx = player.get(call);
            
            String temp = players[idx - 1];
            players[idx - 1] = players[idx];
            players[idx] = temp;
            
            player.put(players[idx - 1], idx - 1);
            player.put(players[idx], idx);
        }
        
        return players;
    }
}