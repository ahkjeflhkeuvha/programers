import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
        ArrayList <Integer> list = new ArrayList<>();
        int cnt = 0;
        for(int i = l; i<=r; i++){
            String str[] = Integer.toString(i).split("");
            cnt = 0;
            for(int j = 0; j<str.length; j++){
                if(str[j].equals("5")||str[j].equals("0")) cnt++;
                else break;
            }
            if(cnt == str.length) list.add(i);
        }
        int answer[];
        if(list.size() == 0) {
            answer = new int[1];
            answer[0] = -1;
        }
        else {
            answer = new int[list.size()];
            int i = 0;
            for(int n : list) answer[i++] = n;
            return answer;
        }
        return answer;
    }
}