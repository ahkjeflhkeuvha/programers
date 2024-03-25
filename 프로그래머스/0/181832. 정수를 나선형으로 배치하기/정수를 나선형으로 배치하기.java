class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        
        int i = 1, startRow = 0, endRow = n - 1, startCol = 0, endCol = n-1;
        while(i <= n*n){
            // 왼위 -> 오위
            for(int j = startCol; j <= endCol; j++) answer[startRow][j] = i++;
            startRow++;
            
            // 오위 -> 오아래
            for(int j = startRow; j <= endRow; j++) answer[j][endCol] = i++;
            endCol--;
            
            // 오아래 -> 왼아래
            for(int j = endCol; j >= startCol; j--) answer[endRow][j] = i++;
            endRow--;
            
            // 왼아래 -> 왼위
            for(int j = endRow; j >= startRow; j--) answer[j][startCol] = i++;
            startCol++;
        }
        return answer;
    }
}