import java.util.*;
class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList <Integer> list = new ArrayList<>();
        for(String str : intStrs){
            int res = Integer.parseInt(str.substring(s, s + l));
            if(res > k) list.add(res);
        }

        return list.stream().mapToInt(i -> i).toArray();
    }
}