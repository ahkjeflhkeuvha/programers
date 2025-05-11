function solution(picture, k) {
    var answer = [];
    
    for(let row of picture) {
        let str = row.split("").map((s) => s.repeat(k)).join('')
        for(let n = 1; n <= k; n++) answer.push(str)
    }
    return answer;
}