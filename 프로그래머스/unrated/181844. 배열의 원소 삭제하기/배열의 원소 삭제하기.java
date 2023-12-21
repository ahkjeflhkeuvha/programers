import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        ArrayList <Integer> list = new ArrayList<>();
        for(int n : arr){
            for(int d : delete_list) {
                if(n != d && d == delete_list[delete_list.length - 1]) list.add(n);
                else if(n == d) break;
            }
        }
        
        int[] answer = new int[list.size()];
        int i = 0;
        for(int n : list) answer[i++] = n;
        return answer;
    }
}