function solution(n, left, right) {
    var answer = [];
    
    for(var i = left; i<=right; i++){
        var r = parseInt(i/n)
        var c = i%n
        answer.push(Math.max(r, c) + 1)
    }
    return answer;
}