import java.util.Arrays;
import java.util.Collections;
class Solution {
    public long solution(long n) {
        long answer = 0;
        String str = Long.toString(n);
        String st[] = str.split("");
        Arrays.sort(st, Collections.reverseOrder());
        
        str = "";
        for(int i = 0; i<st.length; i++){
            str += st[i];
        }
        
        answer = Long.parseLong(str);
        return answer;
    }
}