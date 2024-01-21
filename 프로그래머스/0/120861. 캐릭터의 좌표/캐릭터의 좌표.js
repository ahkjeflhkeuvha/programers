function solution(keyinput, board) {
    var answer = [0, 0];
    for(let i = 0; i<keyinput.length; i++){
        if(keyinput[i] === 'left') answer[0] += answer[0] > -((board[0]-1)/2) ? -1 : 0;
        else if(keyinput[i] === 'right') answer[0] += answer[0] < ((board[0]-1)/2) ? 1 : 0;
        else if(keyinput[i] === 'up') answer[1] += answer[1] < ((board[1]-1)/2) ? 1 : 0;
        else if(keyinput[i] === 'down') answer[1] += answer[1] > -((board[1]-1)/2) ? -1 : 0;
    }
    return answer;
}