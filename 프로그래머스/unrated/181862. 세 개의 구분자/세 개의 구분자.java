import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        String s[] = myStr.split("[abc]");
        ArrayList <String> list = new ArrayList();
        for(String str : s){
            if(str.length() > 0) list.add(str);
        }
        if(list.size() == 0) list.add("EMPTY");
        String[] answer = new String[list.size()];
        int n = 0;
        for(String str : list) answer[n++] = str;
        
        return answer;
    }
}