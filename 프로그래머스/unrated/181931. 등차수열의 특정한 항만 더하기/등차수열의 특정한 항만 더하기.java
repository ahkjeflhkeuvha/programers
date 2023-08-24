class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int j = 0;
        for(int i = a; i<=a + d*(included.length-1); i+=d){
            if(included[j] == true) answer += i;
            j++;
        }
        return answer;
    }
}