function solution(numbers, hand) {
    var answer = '';
    var leftStr = "*741";
    var midStr = "0852";
    var rightStr = "#963";
    
    var leftCol = 0;
    var rightCol = 2;
    
    var leftRow = 0;
    var rightRow = 0;
    
    for (var num of numbers) {
        if (num % 3 == 1) { // 왼쪽 열의 숫자
            answer += 'L';
            leftCol = 0;
            leftRow = leftStr.indexOf(num.toString());
        } 
        else if (num % 3 == 0 && num != 0) { // 오른쪽 열의 숫자
            answer += 'R';
            rightCol = 2;
            rightRow = rightStr.indexOf(num.toString());
        } 
        else { // 가운데 열의 숫자
            var midRow = midStr.indexOf(num.toString());
            var left = Math.abs(leftCol - 1) + Math.abs(leftRow - midRow);
            var right = Math.abs(rightCol - 1) + Math.abs(rightRow - midRow);
            
            if (left == right) {
                if (hand == "left") {
                    answer += 'L';
                    leftCol = 1;
                    leftRow = midRow;
                } else {
                    answer += 'R';
                    rightCol = 1;
                    rightRow = midRow;
                }
            }
            else if (left < right) {
                answer += 'L';
                leftCol = 1;
                leftRow = midRow;
            } else {
                answer += 'R';
                rightCol = 1;
                rightRow = midRow;
            }
        }
    }
    return answer;
}
