class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for(int[] query : queries){
            int a = query[0];
            int b = query[1];
            int temp = 0;
            
            temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
        }
        return answer = arr;
    }
}