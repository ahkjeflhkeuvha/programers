class Solution {
    public int solution(int n) {
        int answer = 0, bin = n, binCnt = 0;
        int cnt = Integer.bitCount(n);
        while(binCnt != cnt){
            bin++;
            binCnt = Integer.bitCount(bin);
        }
        return answer = bin;
    }
}