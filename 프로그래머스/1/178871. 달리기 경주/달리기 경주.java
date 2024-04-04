import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> player = new HashMap<>();
        
        for(int  i = 0; i<players.length; i++) player.put(players[i], i);
        
        for(String call : callings){
            int idx = player.get(call);
            String current = players[idx - 1];
            players[idx - 1] = players[idx];
            players[idx] = current;
            
            player.put(players[idx - 1], idx - 1);
            player.put(players[idx], idx);
        }
        return players;
    }
}