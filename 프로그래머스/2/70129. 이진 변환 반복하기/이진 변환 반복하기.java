class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int cnt = 0, rmv = 0;
        while(true) {
            rmv += (int)s.chars().filter(str -> String.valueOf((char)str).equals("0")).count();
            s = s.replaceAll("0", ""); // 0제거
            s = Integer.toBinaryString(s.length());
            cnt++;
            if(s.equals("1")) break;
        }
        answer[0] = cnt;
        answer[1] = rmv;
        return answer;
    }
}