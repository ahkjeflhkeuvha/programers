import java.util.*;

class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        int res = 0;
        for(int i = 0; i<answer.length; i++){
            String[] strArr = quiz[i].split(" ");
            res = Integer.parseInt(strArr[0]) + Integer.parseInt(strArr[2]) * (strArr[1].equals("+") ? 1 : -1);
            answer[i] = res == Integer.parseInt(strArr[4]) ? "O" : "X";
        }
        return answer;
    }
}