function solution(k, d) {
    var answer = 0;
    for(let i = 0; i<=d; i+=k) {
        let max_y = Math.pow(Math.pow(d, 2) - Math.pow(i, 2), 1/2)
        answer += Math.floor(max_y/k) + 1
    }
    return answer;
}