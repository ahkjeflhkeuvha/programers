import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> people = new HashMap<>();
        HashMap<Integer, String> rank = new HashMap<>();
        
        for(int i = 0; i<players.length; i++){
            people.put(players[i], i);
            rank.put(i, players[i]);
        }
        
        for(int i = 0; i<callings.length; i++){
            // 추월 할 선수 인덱스, 선수
            int currentRank = people.get(callings[i]);
            String currentPlayer = rank.get(currentRank);
            
            // 추월 당할 선수
            String lastPlayer = rank.get(currentRank - 1);
            
            people.put(currentPlayer, currentRank - 1);
            people.put(lastPlayer, currentRank);
            
            rank.put(currentRank, lastPlayer);
            rank.put(currentRank - 1, currentPlayer);
            
        }
        String[] answer = new String[players.length];
        
        for(int i = 0; i<answer.length; i++){
            answer[i] = rank.get(i);
        }
        
        return answer;
    }
}