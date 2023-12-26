class Solution {
    public int[][] solution(int[][] arr) {
        int row = arr.length, col = arr[0].length;
        if(row > col) col = arr.length;
        else row = arr[0].length;
        
        int[][] answer = new int[row][col];
        for(int i = 0; i<arr.length; i++){
            for(int j = 0; j<arr[i].length; j++){
                answer[i][j] = arr[i][j];
            }
        }
        return answer;
    }
}