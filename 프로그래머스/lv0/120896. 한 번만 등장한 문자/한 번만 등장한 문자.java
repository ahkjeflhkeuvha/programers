class Solution {
    public String solution(String s) {
        String answer = "";
        int ar[] = new int[26];
        
        for(int i = 0; i<s.length(); i++){
            ar[s.charAt(i)-97]++;
        }
        for(int i = 0; i<ar.length; i++){
            if(ar[i] == 1){
                answer += (char)(i + 97);
            }
        }
        return answer;
    }
}