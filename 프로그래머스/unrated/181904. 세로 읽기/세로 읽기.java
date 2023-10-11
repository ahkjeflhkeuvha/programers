class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        String[][] st = new String[my_string.length()/m][m];
        
        int k = 0;
        for(int i = 0; i<st.length; i++){
            for(int j = 0; j<st[i].length; j++){
                st[i][j] = Character.toString(my_string.charAt(k));
                k++;
            }
        }
        for(int i = 0; i<st.length; i++){
            answer += st[i][c - 1];
        }
        return answer;
    }
}