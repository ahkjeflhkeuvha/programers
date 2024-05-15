import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> max = new PriorityQueue<>();
        PriorityQueue<Integer> min = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0; i<operations.length; i++){
            String strArr[] = operations[i].split(" ");
            
            if(strArr[0].equals("I")){
                max.add(Integer.parseInt(strArr[1]));
                min.add(Integer.parseInt(strArr[1]));
            }
            // max는 최대값이 첫 번째에 min은 최소값이 첫 번째에
            else if(max.size() > 0) {
                if(strArr[1].equals("1")) max.remove(min.poll());
                else min.remove(max.poll());
            }
        }
        
        int[] answer = new int[2];
        if(max.size() == 0) {
            answer[0] = 0;
            answer[1] = 0;
        }
        else {
            answer[0] = min.poll();
            answer[1] = max.poll();
        }
 
        return answer;
    }
}