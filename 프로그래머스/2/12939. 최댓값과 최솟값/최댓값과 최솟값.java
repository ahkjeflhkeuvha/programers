import java.util.Arrays;

class Solution {
    public String solution(String s) {
        String answer = "";
        String st[] = s.split(" ");
        int ar[] = new int[st.length];
        
        for(int i = 0; i<st.length; i++){
            ar[i] = Integer.parseInt(st[i]);
        }
        Arrays.sort(ar);
        
        answer += ar[0] + " " + ar[ar.length - 1];
        return answer;
    }
}