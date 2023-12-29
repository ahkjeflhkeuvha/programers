import java.util.*;

class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        int res = 0;
        for(int i = 0; i<answer.length; i++){
            String[] strArr = quiz[i].split(" ");
            if(strArr[1].equals("+")) res = Integer.parseInt(strArr[0]) + Integer.parseInt(strArr[2]);
            else res = Integer.parseInt(strArr[0]) - Integer.parseInt(strArr[2]);
            
            if(Integer.toString(res).equals(strArr[4])) answer[i] = "O";
            else answer[i] = "X";
        }
        return answer;
    }
}