import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int[] ar = new int[progresses.length];
        int function = 0;
            for(int i = 0; i<progresses.length; i++){
                ar[i] = (99 - progresses[i])/speeds[i] + 1;
            }
            System.out.println(Arrays.toString(ar));
            
            int Max = ar[0];
            for(int i = 0; i<ar.length; i++){
                if(Max>=ar[i]) function++;
                else {
                    list.add(function);
                    function = 1;
                    Max = ar[i];
                }
            }
            list.add(function);
        
        int[] answer = new int[list.size()];
        for(int i = 0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}