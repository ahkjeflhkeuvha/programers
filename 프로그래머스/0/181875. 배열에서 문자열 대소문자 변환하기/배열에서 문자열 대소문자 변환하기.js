function solution(strArr) {
    var answer = [];
    
    for(let idx in strArr) {
        if (idx % 2 == 0) answer.push(strArr[idx].toLowerCase())
        else answer.push(strArr[idx].toUpperCase())
    }
    return answer;
}