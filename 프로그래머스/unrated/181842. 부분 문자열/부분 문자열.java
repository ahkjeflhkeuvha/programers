class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        int len = (str1.length() == str2.length()) ? 1 : str2.length() - str1.length();
        
        // str2 = 5, str1 = 2, len = 3, i = 0, 1, 2
        // (0, 2) ,, (2, 4)
        for(int i = 0; i<len; i++){
            if(str2.substring(i, i + str1.length()).equals(str1)){
                answer = 1;
                break;
            }
            if(str2.substring(len).equals(str1)) answer = 1;
        }
        return answer;
    }
}