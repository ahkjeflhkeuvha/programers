import java.util.*;
class Solution {
    public String solution(String my_string) {
        String answer = "";
        String strArr[] = my_string.split("");
        ArrayList <String> list = new ArrayList<>();
        
        for(String str : strArr) {
            if(!list.contains(str)) list.add(str);
        }
        
        for(String str : list) answer += str;
        return answer;
    }
}