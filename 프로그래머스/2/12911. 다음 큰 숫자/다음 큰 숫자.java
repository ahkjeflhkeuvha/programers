class Solution {
    public int solution(int n) {
        int answer = 0, bin = n + 1, binCnt = 0;
        int cnt = Integer.bitCount(n);
        while(binCnt != cnt){
            binCnt = Integer.bitCount(bin);
            bin++;
        }
        return answer = bin - 1;
    }
}