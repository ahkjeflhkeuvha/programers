import java.util.*;
class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList <Integer> list = new ArrayList<>();
        for(String str : intStrs){
            int res = Integer.parseInt(str.substring(s, s + l));
            if(res > k) list.add(res);
        }
        int[] answer = new int[list.size()];
        int n = 0;
        for(int i : list){
            answer[n++] = i;
        }
        return answer;
    }
}