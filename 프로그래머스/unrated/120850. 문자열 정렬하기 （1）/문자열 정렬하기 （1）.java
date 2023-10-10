import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(String my_string) {
        ArrayList<Integer> answerList = new ArrayList<>();
        
        for(int i = 0; i<my_string.length(); i++){
            if(my_string.charAt(i)-48 >= 0 && my_string.charAt(i)-48 <=9){
                answerList.add(my_string.charAt(i)-48);
            }
        }
        Collections.sort(answerList);
        
        int answer[] = new int[answerList.size()];
        for(int i = 0; i<answer.length; i++) answer[i] = answerList.get(i);
        
        return answer;
    }
}