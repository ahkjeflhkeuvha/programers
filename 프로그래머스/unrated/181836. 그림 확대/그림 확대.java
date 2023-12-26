import java.util.*;
class Solution {
    public String[] solution(String[] picture, int k) {
        ArrayList <String> list = new ArrayList<>();
        for(int i = 0; i < picture.length; i++){
            String strArr[] = picture[i].split("");
            String str = "";
            for(int j = 0; j<strArr.length; j++){
                str += strArr[j].repeat(k);
            }
            for(int p = 0; p < k; p++){
                list.add(str);
            }
        }
        String[] answer = new String[list.size()];
        int n = 0;
        for(String str : list) answer[n++] = str;
        return answer;
    }
}