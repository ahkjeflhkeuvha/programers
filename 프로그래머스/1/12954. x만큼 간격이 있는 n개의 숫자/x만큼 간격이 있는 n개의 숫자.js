function solution(x, n) {
    var answer = [];
    for(let i = 0, num = x; i<n; i++, num += x){
        answer.push(num);
    }
    return answer;
}