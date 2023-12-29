class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        if(denom1 == denom2) {
            answer[0] = numer1 + numer2;
            answer[1] = denom1;
        }
        else {
            answer[0] = numer1 * denom2 + denom1 * numer2;
            answer[1] = denom1 * denom2;
        }
        
        int num = 2;
        while(true){
            if(answer[0] % num == 0 && answer[1] % num == 0) {
                answer[0] /= num;
                answer[1] /= num;
                num--;
            }
            num++;
            
            if(num > answer[0] && num > answer[1]) break;
        }
        return answer;
    }
}