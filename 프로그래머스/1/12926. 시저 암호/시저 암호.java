class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == ' ') answer += ' ';
            else if(Character.isLowerCase(s.charAt(i))) answer += (char) ((s.charAt(i) - 'a' + n) % 26 + 'a');
            else answer += (char)((s.charAt(i) - 'A' + n) % 26 + 'A'); 
        }
        return answer;
    }
}