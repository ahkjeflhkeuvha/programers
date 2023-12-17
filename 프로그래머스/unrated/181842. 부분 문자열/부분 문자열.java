class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        int len = (str1.length() == str2.length()) ? 1 : str2.length() - str1.length();
        
        if(str2.substring(len).equals(str1)) answer = 1;
        
        for(int i = 0; i<len; i++){
            if(str2.substring(i, i + str1.length()).equals(str1)){
                answer = 1;
                break;
            }
            
        }
        return answer;
    }
}