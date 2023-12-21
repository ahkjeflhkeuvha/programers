import java.util.*;
class Solution {
    public String[] solution(String my_string) {
        String[] strArr = my_string.split(" ");
        ArrayList<String> list = new ArrayList<>();
        for(String str : strArr) {
            if(!str.equals("")) list.add(str);
        }
        String[] answer = new String[list.size()];        
        int n = 0;
        for(String str : list) answer[n++] = str;
        return answer;
    }
}