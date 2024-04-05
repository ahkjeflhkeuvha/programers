import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0, first = 0, last = 0, n = 0;
        String strArr[] = s.split("");
            
        
        for(int i = 0; i<strArr.length; i++){
            if(strArr[n].equals(strArr[i])) first++;
            else last++;
            
            if(first == last) {
                answer++;
                first = 0;
                last = 0;
                n = i + 1;
            }
            
            if(i == strArr.length - 1 && (first > 0 || last > 0)) answer++;
        }
        return answer;
    }
}