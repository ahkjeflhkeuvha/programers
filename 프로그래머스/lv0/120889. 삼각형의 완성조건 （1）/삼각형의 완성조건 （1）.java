class Solution {
    public int solution(int[] sides) {
        int answer = 0, i;
        int max = sides[0];
        for(i = 0; i<sides.length; i++){
            if(max<sides[i]) max = sides[i];
            answer += sides[i];
        }
        if(max < answer-max) answer = 1;
        else answer = 2;
        
        return answer;
    }
}