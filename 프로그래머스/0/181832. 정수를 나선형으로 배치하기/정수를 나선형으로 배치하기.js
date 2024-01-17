function solution(n) {
    const answer =  Array.from(Array(n), () => Array(n).fill(null));
    var num = 1, strRow = 0, endRow = n-1, strCol = 0, endCol = n-1;
    while(num <= n*n){
        //오위 -> 왼위
        for(let i = strCol; i<=endCol; i++) 
            answer[strRow][i] = num++;
        strRow++;
        
        //왼위 -> 왼아래
        for(let i = strRow; i<=endRow; i++) 
            answer[i][endCol] = num++;
        endCol--;
        
        //왼아래 -> 오아래
        for(let i = endCol; i>=strCol; i--) 
            answer[endRow][i] = num++;
        endRow--;
        
        //오아래 -> 오위
        for(let i = endRow; i>=strRow; i--) 
            answer[i][strCol] = num++;
        strCol++;
        
    }
    return answer;
}