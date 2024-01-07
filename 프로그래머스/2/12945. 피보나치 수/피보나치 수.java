class Solution {
    public int solution(int n) {
        return fibonacci(n);
    }
    public int fibonacci(int num){
        int first = 0, second = 1, nTarget = 0;
        for(int i = 2; i <= num; i++){
            nTarget = (first + second) % 1234567;

            first = second;
            second = nTarget;
        }
        return nTarget;
    }
    
}