function solution(num, total) {
    var answer = [];
    let str = (2 * total / num + 1 - num) / 2;
    for(let i = str; i<str+num; i++) answer.push(i);
    return answer;
}