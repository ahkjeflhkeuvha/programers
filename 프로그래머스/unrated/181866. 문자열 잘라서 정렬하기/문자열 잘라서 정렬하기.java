import java.util.*;
class Solution {
    public String[] solution(String myString) {
        String[] strArr= myString.split("x");
        ArrayList <String> list = new ArrayList<>();
        for(String str : strArr) {
            if(str.equals("")) continue;
            list.add(str);
        }

        String[] answer = new String[list.size()];
        int n = 0;
        for(String str : list) answer[n++] = str;
        Arrays.sort(answer);
        return answer;
    }
}