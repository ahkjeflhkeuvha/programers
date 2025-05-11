function solution(n) {
    var answer = Array.from(Array(n), () => Array(n).fill(null));
    let num = 1
    let [startRow, endRow, startCol, endCol] = [0, n - 1, 0, n - 1]
    
    while(num <= Math.pow(n, 2)) {
        for(let j = startCol; j <= endCol; j++) answer[startRow][j] = num++
        startRow += 1
        
        for(let i = startRow; i <= endRow; i++) answer[i][endCol] = num++
        endCol -= 1
        
        for(let j = endCol; j>= startCol; j--) answer[endRow][j] = num++
        endRow -= 1
        
        for(let i = endRow; i >= startRow; i--) answer[i][startCol] = num++
        startCol += 1
    }
    
    return answer;
}