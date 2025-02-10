function solution(array, commands) {
    var answer = [];
    for(let command of commands){
        [i, j, k] = command
        newArr = array.slice(i-1, j).sort((a, b) => a - b)
        answer.push(newArr[k-1])
    }
    return answer;
}