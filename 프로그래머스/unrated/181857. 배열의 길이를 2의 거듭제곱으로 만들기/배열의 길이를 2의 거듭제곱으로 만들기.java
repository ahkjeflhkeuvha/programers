import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        ArrayList <Integer> list = new ArrayList<>();
        for(int n : arr) list.add(n); 
        
        int res = 0;
        for(int i = 0; i<=10; i++){
            if(list.size() <= (int)Math.pow(2, i)){
                res = (int)Math.pow(2, i);
                break;
            }
        }
        for(int i = 0; i<res; i++){
            if(list.size() < res) list.add(0);
        }
        int[] answer = new int[list.size()];
        int i = 0;
        for(int n : list) answer[i++] = n;
        return answer;
    }
}