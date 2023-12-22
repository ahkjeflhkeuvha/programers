class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        for(int i = 0; i<my_string.length(); i++){
            char str = my_string.charAt(i);
            if(str >= 65 && str <= 90) answer[str - 65]++;
            else answer[str - 71]++;
        }
        return answer;
    }
}