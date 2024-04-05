import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0, cnt = 0, n = 0;
        String strArr[] = s.split("");
            
        
        for(int i = 0; i<strArr.length; i++){
            if(strArr[n].equals(strArr[i])) cnt++;
            else cnt--;
            
            if(cnt == 0) {
                answer++;
                n = i + 1;
            }
            
            if(i == strArr.length - 1 && cnt > 0) answer++;
        }
        return answer;
    }
}