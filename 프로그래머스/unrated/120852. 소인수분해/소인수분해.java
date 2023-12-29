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
        int answer[];
        return answer = list.stream().mapToInt(i->i).toArray();
    }
}