class Solution {
    public int solution(int n) {
        int answer = 1, num = 1;
        
        while(true){
            answer *= num;
            if(answer > n) break;
            num++;
        }
        return num - 1;
    }
}