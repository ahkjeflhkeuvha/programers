class Solution {
    public int solution(String before, String after) {
        int answer = 0;
        int Bar[] = new int[26];
        int Aar[] = new int[26];
        
        for(int i = 0; i<before.length(); i++){
            Bar[before.charAt(i)-97]++;
            Aar[after.charAt(i)-97]++;
        }
        
        for(int i = 0; i<26; i++){
            if(Bar[i] == Aar[i]) answer = 1;
            else {
                answer = 0;
                break;
            }
        }
    
        
        return answer;
    }
}