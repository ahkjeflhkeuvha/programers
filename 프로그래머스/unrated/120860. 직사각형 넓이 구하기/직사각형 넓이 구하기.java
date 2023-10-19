class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        int width = 0, height = 0;
        
        for(int i = 0; i<3; i++){
            if(dots[i][0] != dots[i + 1][0]) width = dots[i+1][0] - dots[i][0];
            if(dots[i][1] != dots[i + 1][1]) height = dots[i+1][1] - dots[i][1];
        }
        
        if(width*height < 0) answer = -(width*height);
        else answer = width*height;
        
        return answer;
    }
}