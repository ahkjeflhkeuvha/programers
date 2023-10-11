class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String Snum = Integer.toString(num);
        
        for(int i = 0; i<Snum.length(); i++){
            if(Snum.charAt(i) - 48 == k) {
                answer = i + 1;
                break;
            }
        }
        return answer;
    }
}