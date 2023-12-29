class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int StartRow = 0, EndRow = n - 1, StartCol = 0, EndCol = n - 1, num = 1;
        
        while(num <= n*n){
            // 위왼 -> 위오
            for(int i = StartCol; i<=EndCol; i++) answer[StartRow][i] = num++;
            StartRow++;
            
            // 오위 -> 오아래
            for(int i = StartRow; i<=EndRow; i++) answer[i][EndCol] = num++;
            EndCol--;
            
            // 아래오 -> 아래왼
            for(int i = EndCol; i>=StartCol; i--) answer[EndRow][i] = num++;
            EndRow--;
            
            //아래왼 -> 위왼
            for(int i = EndRow; i>=StartRow; i--) answer[i][StartCol] = num++;
            StartCol++;
        }
        return answer;
    }
}