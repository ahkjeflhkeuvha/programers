import java.util.ArrayList;
class Solution {
    public int[] solution(int n) {
        ArrayList <Integer> collatz = new ArrayList<>();
        collatz.add(n);
        while(n != 1){
            n = (n%2 == 0) ? n/2 : 3 * n + 1;
            collatz.add(n);
        }
        int[] answer = new int[collatz.size()];
        int i = 0;
        for(int temp : collatz){
            answer[i++] = temp;
        }
        return answer;
    }
}