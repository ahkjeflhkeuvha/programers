import java.util.*;

class Solution {
    static int answer = 0;
    static String[] words = {"A", "E", "I", "O", "U"};
    static int count = 0;
    
    public int solution(String word) {
        answer = 0;
        count = 0;
        dfs(words, "", word);
        return answer;
    }
    
    public void dfs(String[] words, String str, String word){
        if(str.length() > 5) return; // 단어 길이를 5로 제한
        
        if(str.equals(word)) {
            answer = count;
            return;
        }
        
        count++; // 각 조합에 대해 카운트를 증가
        
        for(int i = 0; i < 5; i++) {
            dfs(words, str + words[i], word);
        }
    }
}
