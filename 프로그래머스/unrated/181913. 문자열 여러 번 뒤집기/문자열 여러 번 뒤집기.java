import java.util.*;
class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        String strArr[] = my_string.split("");
        for(int i = 0; i<queries.length; i++){
            for(int j = queries[i][0], k = queries[i][1]; j <= (int)(queries[i][0] + queries[i][1]) / 2; j++, k--){
                String temp = strArr[j];
                strArr[j] = strArr[k];
                strArr[k] = temp;
            }
        }
        for(String str : strArr) answer += str;
        return answer;
    }
}