import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        ArrayList <Integer> list = new ArrayList<>();
        for(int i = 0; i<arr.length; i++){
            if(list.size() == 0) list.add(arr[i]);
            else if(list.get(list.size() - 1) == arr[i]) list.remove(list.size() - 1);
            else if(list.get(list.size() - 1) != arr[i]) list.add(arr[i]);
        }
        int i = 0;
        int[] answer = new int[list.size()];
        if(list.size() == 0) return new int[]{-1};
        else for(int n : list) answer[i++] =  n;
        
        return answer;
    }
}