import java.util.*;
class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        ArrayList <Integer> list = new ArrayList<>();
        for(int i = 0; i<rank.length; i++){
            if(attendance[i]) list.add(rank[i]);
            
        }
        Collections.sort(list);
        

        int answer = 0;
        for(int i = 0; i<rank.length; i++){
            if(list.get(0) == rank[i]) answer += i * 10000;
            else if(list.get(1) == rank[i]) answer += i * 100;
            else if(list.get(2) == rank[i]) answer += i;
        }
        
        return answer;
    }
}