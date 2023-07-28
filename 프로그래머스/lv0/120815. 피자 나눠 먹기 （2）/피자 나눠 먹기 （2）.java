class Solution {
    public int solution(int n) {
        int answer = 0, i = 1;
        // n/6*i이 0이면 됨, i는 계속 ++ 시키면 됨
        
        while(true){
            if((6*i)%n == 0) break;
            i++;
        }
        return answer = i;
    }
}