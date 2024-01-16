class Solution {
    public String[] solution(String my_str, int n) {
        String[] answer = new String[(my_str.length()+n-1)/n];
        int str = 0, end = n;
        for(int i = 0; i<answer.length; i++){
            answer[i] = my_str.substring(str, end);
            str += n;
            end += n;
            if(end > my_str.length()) end = my_str.length();   
        }
        return answer;
    }
}