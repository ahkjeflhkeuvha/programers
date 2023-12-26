class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int min = 1000000;
        for(int i = 0; i<queries.length; i++){
            min = 1000000;
            for(int j = queries[i][0]; j <= queries[i][1]; j++){
                if(arr[j] > queries[i][2] && min > arr[j]) min = arr[j];

            }
            if(min == 1000000) min = -1;
            answer[i] = min;
        }
        return answer;
    }
}