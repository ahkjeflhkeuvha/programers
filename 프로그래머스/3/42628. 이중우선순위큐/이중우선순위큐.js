function solution(operations) {
    var answer = [];
    for(let operation of operations) {
        let [command, num] = operation.split(" ")
        
        answer.sort((a, b) => a - b)
        
        if(command == "I") answer.push(Number(num))
        else if(num == "1") answer.pop()
        else if(num == "-1") answer.shift()
    }
    answer.sort((a, b) => a - b)
    return answer.length == 0 ? [0, 0] : [answer[answer.length - 1], answer[0]];
}