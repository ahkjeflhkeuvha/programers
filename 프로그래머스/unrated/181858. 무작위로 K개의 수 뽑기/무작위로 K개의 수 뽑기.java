import java.util.*;
class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        ArrayList <Integer> list = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            answer[i] = -1;
        }
        
        int cnt = 0;
        for(int i = 0; i<arr.length; i++){
            if(!list.contains(arr[i])) {
                answer[cnt++] = arr[i];
                list.add(arr[i]);
            }
            if(list.size() == k) break;
        }
        return answer;
    }
}