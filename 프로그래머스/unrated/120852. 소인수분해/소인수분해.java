import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 2; i<=n; i++){
            while(n%i==0){
                if(!list.contains(i)) list.add(i);
                n/=i;
            }
        }
        int[] answer = new int[list.size()];
        int idx = 0;
        for(int num : list) answer[idx++] = num;
        return answer;
    }
}