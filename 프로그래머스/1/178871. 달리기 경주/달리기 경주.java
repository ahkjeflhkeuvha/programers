import java.util.HashMap;

public class Solution {
    public String[] solution(String[] players, String[] callings) {
        int n = players.length;
        HashMap<String, Integer> indexMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            indexMap.put(players[i], i);
        }

        for (String calling : callings) {
            int idx = indexMap.get(calling);
            // 여기는 return하기 위해서!
            String temp = players[idx - 1];
            players[idx - 1] = players[idx];
            players[idx] = temp;

            // 이렇게 하는 이유! map에 이름과 순위를 저장 -> map에 변화가 없으면 idx에 계속 처음과 같은 값이 들어감 (idx를 map에서 가져옴)
            // 따라서 순위가 변함에 따라 map의 순위도 변경
            
            indexMap.put(players[idx - 1], idx - 1);
            indexMap.put(players[idx], idx);
        }

        return players;
    }
}