class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        int sum = 0, j = 0;
        for(int i = -100; i<=total; i++){
            sum = 0;
            for(j = i; j<num+i; j++){
                sum += j;
            }
            if(sum == total) break;
        }
        j -= num;
        for(int i = 0; i<answer.length; i++) answer[i] = j++;
        return answer;
    }
}