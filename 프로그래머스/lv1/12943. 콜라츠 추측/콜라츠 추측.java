class Solution {
    public int solution(int num) {
        int answer = 0;
        
        while(num > 1 && answer < 500){
            if(num%2 ==0) num /= 2;
            else if(num%2==1) num = (num*3) + 1;  
            answer++;
        }
        return num == 1 ? answer : -1;
    }
}