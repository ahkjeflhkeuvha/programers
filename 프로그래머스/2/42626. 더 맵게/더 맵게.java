import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i = 0; i<scoville.length; i++){
            heap.add(scoville[i]);
        }
        
        while(heap.size() > 1 && heap.peek() < K){
            heap.add(heap.poll() + (heap.poll() * 2));
            answer++;
        }
        
        return (heap.size() <= 1 && heap.peek() < K) ? -1 : answer;
    }
}