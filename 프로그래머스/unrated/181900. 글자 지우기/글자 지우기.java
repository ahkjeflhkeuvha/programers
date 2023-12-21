class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        String str[] = my_string.split("");
        for(int idx : indices) str[idx] = "";
        for(String strArr : str) answer += strArr;
        return answer;
    }
}