import java.util.Arrays;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0, temp, WidthMax = 0, LengthMax = 0;
        
        for(int i = 0; i<sizes.length; i++){
            if(sizes[i][0] < sizes[i][1]){
                temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }
            
            if(sizes[i][0] > WidthMax) WidthMax = sizes[i][0];
            if(sizes[i][1] > LengthMax) LengthMax = sizes[i][1];
        }
        
        
        
        return answer = WidthMax*LengthMax;
    }
}