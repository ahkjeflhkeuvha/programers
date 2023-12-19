class Solution {
    public String solution(String myString, String pat) {
        String answer = "", str = "";
        for(int i = myString.length(); i>=0; i--){
            str = myString.substring(0, i);
            if(str.endsWith(pat)) break;
        }
        return answer = str;
    }
}