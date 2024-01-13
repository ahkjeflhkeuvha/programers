class Solution {
    public int solution(int a, int b) {
        return prime(fraction(a, b));
    }
    public int fraction(int a, int b){
        int i = 2;
        while(i <= a){
            if(a%i == 0 && b%i == 0){
                a/=i;
                b/=i;
                i--;
            }
            i++;
        }
        return b;
    }
    
    public int prime(int b){
        while(b != 1){
            if(b%2 == 0) b/=2;
            else if(b%5 == 0) b/=5;
            else break;
        }
        if(b==1) return 1;
        else return 2;
    }
}