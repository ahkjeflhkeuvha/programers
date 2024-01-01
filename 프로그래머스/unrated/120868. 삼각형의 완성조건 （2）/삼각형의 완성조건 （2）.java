import java.util.*;
class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        Arrays.sort(sides);
        // 가장 긴 변이 sides[1]일 때 
        for(int i = 1; i<=sides[1]; i++){
            if(sides[0] + i > sides[1]) answer++;
        }
        // 가장 긴 변이 나머지 한 변 일 때
        for(int i = 1; i<sides[0]+sides[1]; i++){
            if(i>sides[1]) answer++;
        }
        return answer;
    }
}