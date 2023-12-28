import java.util.*;
class Solution {
    public int[] solution(int[] arr, int k) {
        ArrayList <Integer> list = new ArrayList<>();
        for(int i = 0; i<arr.length; i++){
            if(!list.contains(arr[i])) list.add(arr[i]);
        }
        System.out.println(list);
        
        if(list.size() > k) {
            while(list.size() != k) list.remove(list.size() - 1);
        }
        else if(list.size() < k){
            while(list.size() != k) list.add(-1);
        }
        int[] answer = new int[list.size()];
        int i = 0;
        for(int n : list) answer[i++] = n;
        return answer;
    }
}