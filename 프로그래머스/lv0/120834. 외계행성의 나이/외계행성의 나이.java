class Solution {
    public String solution(int age) {
        String answer = "";
        String st = Integer.toString(age);
        
        for(int i = 0; i<st.length(); i++){
            answer += (char)(st.charAt(i) + 49);
        }
        return answer;
    }
}