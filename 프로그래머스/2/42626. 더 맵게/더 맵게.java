import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i = 0; i<scoville.length; i++){
            heap.add(scoville[i]);
        }
        
        while(heap.peek() < K){
            if(heap.size() >= 2) heap.add(heap.poll() + (heap.poll() * 2));
            answer++;
            if(heap.size() == 1 && heap.peek() < K) {
                answer = -1;
                break;
            }
        }
        
        return answer;
    }
}