class Solution {
    public int[] solution(int[] num_list, int n) {
        int len = (num_list.length-1)/n;
        int[] answer = new int[len+1];
        System.out.println(len);
        for(int i = 0, j = 0; i<num_list.length; i+=n, j++){
            answer[j] = num_list[i];
        }
        return answer;
    }
}