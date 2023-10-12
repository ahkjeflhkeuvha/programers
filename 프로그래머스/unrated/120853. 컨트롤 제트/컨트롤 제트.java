class Solution {
    public int solution(String s) {
        int answer = 0;
        String st[] = s.split(" ");
        
        for(int i = 0; i<st.length; i++){
            if(st[i].equals("Z")) {
                answer -= Integer.parseInt(st[i - 1]);
            }
            else answer += Integer.parseInt(st[i]);
        }
        return answer;
    }
}