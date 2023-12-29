class Solution {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        char[] charArr = my_string.toCharArray();
        
        charArr[num1] = my_string.charAt(num2);
        charArr[num2] = my_string.charAt(num1);
        
        answer = String.valueOf(charArr);
        return answer;
    }
}