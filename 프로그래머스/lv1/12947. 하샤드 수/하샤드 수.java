class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String str = Integer.toString(x);
        int i, sum = 0;
        
        for(i=0; i<str.length(); i++){
            sum += str.charAt(i) - 48;
        }
        if(x%sum == 0) answer = true;
        else answer = false;
        
        return answer;
    }
}