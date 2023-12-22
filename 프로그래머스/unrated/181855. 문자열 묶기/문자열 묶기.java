class Solution {
    public int solution(String[] strArr) {
        int[] lengthArr = new int[31];
        int answer = 0;
        for(int i = 0; i<strArr.length; i++){
            lengthArr[strArr[i].length()]++;
            if(lengthArr[strArr[i].length()] > answer) answer = lengthArr[strArr[i].length()];
        }

        return answer;
    }
}