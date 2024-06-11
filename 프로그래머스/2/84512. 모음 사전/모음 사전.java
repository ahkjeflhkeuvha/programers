import java.util.*;

class Solution {
    static String strArr[] = {"A", "E", "I", "O", "U"};
    static ArrayList<String> list;
    
    public int solution(String word) {
        list = new ArrayList<>();
        int answer = 0;
        ExSearch("", 0);
        
        for(int i = 0; i<list.size(); i++){
            if(list.get(i).equals(word)) {
                answer = i;
                break;
            }
        }
        return answer;
    }
    static void ExSearch(String str, int idx){
        list.add(str);
        if(str.length() == 5) return;
        for(int i = 0; i<5; i++){
            ExSearch(str + strArr[i], idx + 1);
        }
    }
}

