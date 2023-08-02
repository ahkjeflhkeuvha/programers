class Solution {
    public String solution(String s) {
        String answer = "";
        char arr[] = s.toCharArray(); // a, b, c, d, e toCharArray는 문자열을 char 배열로 만들어줌
        if(arr.length%2 == 1){
            answer += arr[arr.length/2];
        }
        else{
            answer += arr[arr.length/2 - 1];
            answer += arr[arr.length/2 ];
        }
        
        
        return answer;
    }
}