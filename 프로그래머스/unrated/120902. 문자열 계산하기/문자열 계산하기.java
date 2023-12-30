class Solution {
    public int solution(String my_string) {
        int answer = 0, num = 1;
        String strArr[] = my_string.split(" ");
        for(int i = 0; i< strArr.length; i++){
            if(strArr[i].equals("-") || strArr[i].equals("+")) num = strArr[i].equals("+") ? 1 : -1;
            else answer += Integer.parseInt(strArr[i]) * num;
        }
        return answer;
    }
}