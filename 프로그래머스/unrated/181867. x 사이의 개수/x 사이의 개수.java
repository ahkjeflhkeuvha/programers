import java.util.Arrays;
class Solution {
    public int[] solution(String myString) {
        int count = 0;
        for(int i = 0; i<myString.length(); i++){
            if(myString.charAt(i) == 'x') count++;
        }
        int[] answer = new int[count + 1];
        String[] answer_s = new String[count + 1];
        answer_s = myString.split("x");
        
        for(int i = 0; i<answer_s.length; i++){
            answer[i] = answer_s[i].length();
        }
        return answer;
    }
}